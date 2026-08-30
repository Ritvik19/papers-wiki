Source URL: https://huggingface.co/blog/microsoft/diff-attn-v2
Title: Differential Transformer V2

Hugging Face's logo Hugging Face 

* Models
* Datasets
* Spaces
* Buckets new
* Docs
* Enterprise
* Pricing
* * Website  
         * Tasks  
         * HuggingChat  
         * Collections  
         * Languages  
         * Organizations  
   * Community  
         * Blog  
         * Posts  
         * Daily Papers  
         * Hardware  
         * Learn  
         * Discord  
         * Forum  
         * GitHub  
   * Solutions  
         * Team & Enterprise  
         * Hugging Face PRO  
         * Enterprise Support  
         * Inference Providers  
         * Inference Endpoints  
         * Storage Buckets
* ---
* Log In
* Sign Up

 Back to Articles

#  Differential Transformer V2 

Enterprise Article 

Published January 20, 2026 

 Upvote 53 
* +47

Li Dong's avatar 

Li Dong unilm Follow 

Microsoft's avatar microsoft

* Abstract
* Code
* Motivation  
   * **Faster Decoding & No Custom Kernels**  
   * **Softmax Magnitude Constraint**  
   * **Beyond Softmax Constraint & Elimination of Attention Sinks**
* Experimental Observations
* Discussions  
   * Construction of Differential Operation  
   * Design Ablations  
   * Miscellaneous

Tianzhu Ye, Li Dong, Yutao Sun, Furu Wei 

Github Link

Notion Link (for better readability)

##  Abstract 

We introduce **Differential Transformer V2** (DIFF V2), an improved version of Differential Transformer (DIFF V1). This revision focuses on inference efficiency, training stability for production-level LLMs, and architectural elegance.

Key improvements:

1. **Faster Inference & No Need of Custom Attention Kernels**Instead of forcing the attention parameter count to match the baseline Transformer (as in DIFF V1), we introduce additional parameters (borrowed from other parts of the model) for Q2Q\_2Q2​. This design allows DIFF V2 to match the baseline Transformer's decoding speed and directly use FlashAttention without custom kernels.
2. **Improved Training Stability**We remove the per-head RMSNorm after differential attention. We find the per-head RMSNorm can lead to instability in later stages of large-scale pretraining of LLM.
3. **Simpler Parameterization & Initialization**We replace the globally shared λ\\lambdaλ with a token-specific, head-wise projected λ\\lambdaλ. This eliminates the exponential re-parameterization and initialization of λ\\lambdaλ.

We conduct pretraining experiments on production-scale LLMs, including dense models and a 30A3 MoE on trillions of tokens using large learning rate of 6e-4 to 1e-3\. Experimental observations:

* **Notably lower language modeling loss** compared to Transformer.
* **Reduced loss and gradient spikes during training**, particularly under large learning rate settings where the Transformer baseline becomes unstable.
* **Reduced activation outliers magnitude.**

The experiments are still running. We expect to explore in later stages of training:

* If learning efficiency is improved in mid- and post-training.
* If performance on downstream long-context benchmarks improves (alleviating context rot).

After the experiments complete and we evaluate the results, we will prepare a more formal report.

##  Code 

We compare DIFF V2 with DIFF V1 below:

(For simplicity, we omit the batch dimension and assume that both the input and output of the following `flash_attn_func` are three-dimensional tensors `(tokens, heads, head dimension)`. Heads belonging to the same GQA group are arranged contiguously in the output)

**Note DIFF V2 subtracts two heads that are in the same GQA group, which means they share the same key and value. This is crucial to performance.** See design ablations section and Github code.

```python
def DiffAttnV1(
        layer_index, q1, q2, k1, k2, v,
        lam_q1, lam_k1, lam_q2, lam_k2,
):
        """
      q1, q2: (N, h/2, d)
      k1, k2: (N, h_kv/2, d)
      v:      (N, h_kv/2, 2d)
      lam_*: (d,)
      """
      attn1 = flash_attn_func(q1, k1, v)
        attn2 = flash_attn_func(q2, k2, v)
        
        lam_init = 0.8 - 0.6 * \
            exp(-0.3 * layer_index)
        lam1 = exp(sum(lam_q1 * lam_k1)
    lam2 = exp(sum(lam_q2 * lam_k2)
    lam = lam1 - lam2 + lam_init
    attn = attn1 - lam * attn2
    
    attn = rmsnorm(attn)
    attn = attn * (1 - lam_init)
    return attn

```

```python
def DiffAttnV2(
        q, k, v, lam
):
        """
      q:   (N, 2h, d)
      k:   (N, h_kv, d)
      v:   (N, h_kv, d)
      lam: (N, h, 1)
      """
        
        attn = flash_attn_func(q, k, v)
        attn1, attn2 = (attn[:, 0::2], 
                        attn[:, 1::2])
        
        lam_val = sigmoid(lam)
        attn = attn1 - lam_val * attn2
    return attn

```

Full code at: unilm/Diff-Transformer/Diff-Transformer-V2 at master · microsoft/unilmIn the script, `h` represents number of query heads, `h_kv` represents number of key-value heads, and `d` means head dimension. The λ\\lambdaλ in DIFF V2 is projected from XXX for each token each head.

DIFF V2 doubles number of query heads while maintaining number of key value heads, and the extra dimension is reduced back to `h*d` after the differential operation so the WOW\_OWO​ projection remains the same as baseline Transformer.

##  Motivation 

### **Faster Decoding & No Custom Kernels** 

DIFF V2 introduces additional query heads compared to the baseline Transformer, **but does not increase the number of key-value (KV) heads**. Since LLM decoding is typically memory-bound, this design allows DIFF V2 to achieve decoding speeds on par with standard Transformer. **Besides, since head dimension is aligned between query, key and value, there is no need for custom attention kernels for DIFF V2**. In contrast, DIFF V1 can be slower during decoding because the value cache must be loaded twice, and a custom attention kernel is needed. DIFF V2 can also increase the arithmetic intensity of the attention module during decoding.

**During pretraining**, when using cutting-edge FlashAttention kernels on H-series and B-series GPUs, the throughput reduction introduced by DIFF V2 is negligible. **For long-sequence prefilling**, we recommend combining DIFF V2 with techniques such as YOCO (also used in Gemma 3n), which already reduces prefilling complexity to linear time with respect to sequence length.

**An alternative perspective is to compare DIFF V2 with a Transformer that has the same query dimension** `2h*d`. Under this comparison, both models exhibit same attention kernel speed, while DIFF V2 has less parameters and flops in output projection.

### **Softmax Magnitude Constraint** 

In the standard Scaled Dot-Product Attention (SDPA), let Q,K,V∈Rn×dQ, K, V \\in \\mathbb{R}^{n \\times d}Q,K,V∈Rn×d be the queries, keys, and values. The context vector CCC is defined as:

C\=Softmax(QKTd)V\=AVC = \\text{Softmax}\\left(\\frac{QK^T}{\\sqrt{d}}\\right)V = AVC\=Softmax(d​QKT​)V\=AV

Where A∈Rn×nA \\in \\mathbb{R}^{n \\times n}A∈Rn×n is the attention weight matrix. Let's focus on a single row of CCC, denoted as ci\\mathbf{c}\_ici​, which is a weighted sum of value vectors vj\\mathbf{v}\_jvj​:

ci\=∑j\=1naijvj\\mathbf{c}\_i = \\sum\_{j=1}^{n} a\_{ij} \\mathbf{v}\_jci​\=j\=1∑n​aij​vj​

We define the **Context RMS** (Root Mean Square) to represent the magnitude of this output:

RMS(ci)\=1d∥ci∥2\\text{RMS}(\\mathbf{c}\_i) = \\sqrt{\\frac{1}{d} \\|\\mathbf{c}\_i\\|^2}RMS(ci​)\=d1​∥ci​∥2​

The weights aija\_{ij}aij​ are non-negative and sum to 1 ( ∑j\=1naij\=1\\sum\_{j=1}^{n} a\_{ij} = 1∑j\=1n​aij​\=1 ). Assume the value vectors vj\\mathbf{v}\_jvj​ are uncorrelated and have an RMS of 1, **the Context RMS is strictly bounded in range \[1n,1)\[\\frac{1}{\\sqrt{n}},1)\[n​1​,1) however the attention distribution changes**:

* If the attention is focused entirely on one token, the Context RMS is 111.
* If the attention is spread equally across all tokens ( aij\=1na\_{ij} = \\frac{1}{n}aij​\=n1​ ), the Context RMS drops to 1n\\frac{1}{\\sqrt{n}}n​1​.
* In other situations, the Context RMS is between 1n\\frac{1}{\\sqrt{n}}n​1​ and 111.

In DIFF V1 we add a per-head RMSNorm on context vectors:

c^i\=ciRMS(ci)\\mathbf{\\hat{c}}\_i = \\frac{\\mathbf{c}\_i}{\\text{RMS}(\\mathbf{c}\_i)}c^i​\=RMS(ci​)ci​​

If the model learns a uniform attention distribution in a head, the Context RMS is approximately 1/n1/\\sqrt{n}1/n​. To normalize this back to 111, RMSNorm must multiply the vector by a scale of n\\sqrt{n}n​. For n\=8192n = 8192n\=8192, n≈90.5\\sqrt{n} \\approx 90.5n​≈90.5. This means the RMSNorm layer applies a **100x** magnification to the output. In large-scale pretraining, we find this leads to massive gradients and numerical instability.

A typical phenomenon is that when DIFF V1 is pre-trained at a large learning rate, the gradient norm experiences a larger increase compared to Transformer in the later stages, along with higher variance. **In DIFF V2, after removing the per-head RMSNorm, the gradient norm scale becomes comparable to that of Transformer, and the gradient norm spike is reduced** (will be discussed further below).

We adopted the per-head RMSNorm design in DIFF V1 primarily because of the doubled value head dimension and the globally shared λ\\lambdaλ across all tokens. Given the modifications made to these two aspects in DIFF V2, we found that removing RMSNorm is now safe.

### **Beyond Softmax Constraint & Elimination of Attention Sinks** 

We demonstrate DIFF V2 can overcome the constraint of Softmax mentioned above. It can also help eliminate attention sinks.

* In original Softmax attention:

aij\=Softmax(zij)\=exp⁡(zij)∑k\=1nexp⁡(zik)ci\=∑j\=1naijvj\=∑j\=1nSoftmax(zij)vjRMS(ci)∈\[1n,1)a\_{ij} = \\text{Softmax}(z\_{ij}) = \\frac{\\exp(z\_{ij})}{\\sum\_{k=1}^{n} \\exp(z\_{ik})} \\\\ \\mathbf{c}\_i = \\sum\_{j=1}^{n} a\_{ij} \\mathbf{v}\_j = \\sum\_{j=1}^{n} \\text{Softmax}(z\_{ij}) \\mathbf{v}\_j \\\\ \\text{RMS}(\\mathbf{c}\_i) \\in \\left\[\\frac{1}{\\sqrt{n}},1\\right)aij​\=Softmax(zij​)\=∑k\=1n​exp(zik​)exp(zij​)​ci​\=j\=1∑n​aij​vj​\=j\=1∑n​Softmax(zij​)vj​RMS(ci​)∈\[n​1​,1)

* In DIFF V2 we introduce a projected λ\\lambdaλ for each token and each head:

ci\=∑j\=1n(Softmax(zij1)−sigmoid(λi)⋅Softmax(zij2))vjRMS(ci)∈(0,2)\\mathbf{c}\_i = \\sum\_{j=1}^{n} \\left( \\text{Softmax}(z\_{ij}^\\text{1}) - \\text{sigmoid}(\\lambda\_i) \\cdot \\text{Softmax}(z\_{ij}^\\text{2}) \\right) \\mathbf{v}\_j \\\\ \\text{RMS}(\\mathbf{c}\_i) \\in \\left(0, \\sqrt{2}\\right)ci​\=j\=1∑n​(Softmax(zij1​)−sigmoid(λi​)⋅Softmax(zij2​))vj​RMS(ci​)∈(0,2​)

The projected λi\\lambda\_iλi​ helps to control the context RMS. We observe that **lowering the lower bound of the context RMS to zero is particularly important**. **It can help eliminate attention sinks and improve training stability**. The upper bound only needs to remain bounded.

Note that our analysis here consider RMS before output projection WOW\_OWO​. Although the RMS can be recovered and adjusted after the output projection, the lack of freedom at Softmax still affects the learning performance.

Other recent works alleviate this constraint as well:

* In Attention Is Off By One:

aijoff\=exp⁡(zij)1+∑k\=1nexp⁡(zik) ci\=∑j\=1naijoffvj\=∑k\=1nexp⁡(zik)1+∑k\=1nexp⁡(zik)∑j\=1nSoftmax(zij)vj RMS(ci)∈(0,1)a\_{ij}^{\\text{off}} = \\frac{\\exp(z\_{ij})}{1 + \\sum\_{k=1}^{n} \\exp(z\_{ik})} \\\\ \\ \\\\ \\mathbf{c}\_i = \\sum\_{j=1}^{n} a\_{ij}^{\\text{off}} \\mathbf{v}\_j = \\frac{\\sum\_{k=1}^{n} \\exp(z\_{ik})}{1 + \\sum\_{k=1}^{n} \\exp(z\_{ik})} \\sum\_{j=1}^{n} \\text{Softmax}(z\_{ij}) \\mathbf{v}\_j \\\\ \\ \\\\ \\text{RMS}(\\mathbf{c}\_i) \\in \\left(0, 1\\right)aijoff​\=1+∑k\=1n​exp(zik​)exp(zij​)​ ci​\=j\=1∑n​aijoff​vj​\=1+∑k\=1n​exp(zik​)∑k\=1n​exp(zik​)​j\=1∑n​Softmax(zij​)vj​ RMS(ci​)∈(0,1)

* In gpt-oss, a learnable scalar sss is introduced for each head:

aijoss\=exp⁡(zij)exp⁡(s)+∑k\=1nexp⁡(zik) ci\=∑j\=1naijossvj\=∑k\=1nexp⁡(zik)exp⁡(s)+∑k\=1nexp⁡(zik)∑j\=1nSoftmax(zij)vj RMS(ci)∈(0,1)a\_{ij}^{\\text{oss}} = \\frac{\\exp(z\_{ij})}{\\exp(s) + \\sum\_{k=1}^{n} \\exp(z\_{ik})} \\\\ \\ \\\\ \\mathbf{c}\_i = \\sum\_{j=1}^{n} a\_{ij}^{\\text{oss}} \\mathbf{v}\_j = \\frac{\\sum\_{k=1}^{n} \\exp(z\_{ik})}{\\exp(s) + \\sum\_{k=1}^{n} \\exp(z\_{ik})} \\sum\_{j=1}^{n} \\text{Softmax}(z\_{ij}) \\mathbf{v}\_j \\\\ \\ \\\\ \\text{RMS}(\\mathbf{c}\_i) \\in \\left(0, 1\\right)aijoss​\=exp(s)+∑k\=1n​exp(zik​)exp(zij​)​ ci​\=j\=1∑n​aijoss​vj​\=exp(s)+∑k\=1n​exp(zik​)∑k\=1n​exp(zik​)​j\=1∑n​Softmax(zij​)vj​ RMS(ci​)∈(0,1)

* In Gated Attention, a projected element-wise sigmoid gate is multiplied:

ci\=sigmoid(gi)⊙∑j\=1nSoftmax(zij)vjRMS(ci)∈(0,1)\\mathbf{c}\_i = \\text{sigmoid} (\\mathbf{g}\_i) \\odot \\sum\_{j=1}^{n} \\text{Softmax}(z\_{ij}) \\mathbf{v}\_j \\\\ \\text{RMS}(\\mathbf{c}\_i) \\in \\left(0, 1\\right)ci​\=sigmoid(gi​)⊙j\=1∑n​Softmax(zij​)vj​RMS(ci​)∈(0,1)

##  Experimental Observations 

We conduct pretraining experiments on production-scale LLMs, including dense models and a 30A3 MoE on trillions of tokens using large learning rate of 6e-4 to 1e-3.

The experiments are still running. What we have observed now:

* **Notably lower language modeling loss** compared to Transformer (a gap of 0.02 to 0.03 at 1T training tokens).
* **Reduced loss and gradient spikes during training**, particularly under large learning rate settings where the Transformer baseline becomes unstable.
* **Reduced activation outliers magnitude.**

We expect to explore in later stages of training:

* Learning efficiency in mid- and post-training.
* Performance on downstream long-context benchmarks (alleviating context rot).

##  Discussions 

###  Construction of Differential Operation 

In theory, a standard Transformer with 2h2h2h attention heads can learn the differential operation by learning WO2i\=−WO2i+1,i\=0,1,…,h−1W\_O^{2i}=-W\_O^{2i+1}, i=0,1,\\ldots,h-1WO2i​\=−WO2i+1​,i\=0,1,…,h−1, where WOiW\_O^{i}WOi​ denotes the output projection of head iii, and head 2i2i2i and 2i+12i+12i+1 belong to the same GQA group.

**Assumption 1.** In practice, such a solution is difficult to learn through optimization, as it requires two sets of parameters to converge to exact negatives of each other.

**Assumption 2.** The differential operation can be learned by the model and the model chooses to learn it in the training. **Then explicitly constructing it before the output projection as in DIFF V2 can save half of the WOW\_OWO​ parameters**. The number of saved parameters is also non-trivial. Under the current GQA setting, the parameters in the attention module are dominated by WQW\_QWQ​ and WOW\_OWO​; Therefore, approximately **25% of the attention-module parameters can be saved.** The saved parameter budget can then be reallocated to other parts of the model.

Even if DIFF V2, after reallocating parameters, does not achieve a lower loss than the baseline but merely matches it, **the method is still worthwhile if it provides additional benefits** such as improved training stability, better control of outliers, or higher training efficiency. This is analogous to GQA, which matches the loss of MHA while reducing KV-cache as an additional benefit. So the key question becomes empirical performance.

###  Design Ablations 

1. Subtracting two heads that are **not** in the same GQA group, which means they **do not** share the same key and value.

(For simplicity, we omit the batch dimension and assume that both the input and output of the following `flash_attn_func` are three-dimensional tensors `(tokens, heads, head dimension)`. Heads belonging to the same GQA group are arranged contiguously in the output)

```python
# Ablation 1
# ❌ Wrong Implementation of DIFF V2!
...
attn = flash_attn_func(q, k, v)
nh = attn.size(1)
attn1, attn2 = (attn[:, :nh//2], 
                    attn[:, nh//2:])
...

```

```python
# DIFF V2
# ✅ Correct Implementation of DIFF V2
...
attn = flash_attn_func(q, k, v)

attn1, attn2 = (attn[:, 0::2], 
                    attn[:, 1::2])
...

```

In our large learning rate setting, the ablation 1 setting exhibits obvious training instability (much more loss and gradient spikes) and higher loss comparing to DIFF V2\. The value should be shared in the two subtraction heads to construct differential operation, as discussed in DIFF V1 paper.

1. Subtracting two attention maps without λ\\lambdaλ scaling factor, i.e., `attn1 - attn2` instead of `attn1 - lam_val * attn2`. This results in an excessively small context RMS at initialization.
2. Directly using projected λ\\lambdaλ without applying `sigmoid` operation. The context RMS is unbounded from above.

Both ablation 2 and ablation 3 lead to higher language modeling loss than DIFF V2\. Ablation 2 maintains training stability similar to DIFF V2, whereas ablation 3 is less stable (still more stable than ablation 1).

1. A Transformer with `1.5*h` heads which aligns parameter with DIFF V2.

Ablation 4 also has higher training loss comparing to DIFF V2.

###  Miscellaneous 

* In DIFF, the outliers in qk logits can be smaller than those in the baseline. This was already analyzed in DIFF V1: DIFF can achieve attention sparsity comparable to the baseline while using smaller qk logits. We further propose that DIFF's differential mechanism, which cancels out small attention values, **may help mitigate the attention rounding error issue discussed in this blog and paper**.
* **DIFF V2 is compatible with sparse attention**. In many existing sparse attention frameworks, query heads within the same GQA group are required to attend to the same key-value blocks in order to maximize speedup. A common strategy is to select key-value blocks based on the average attention logits across heads. For DIFF V2, the problem shifts to designing an effective block-selection strategy for a larger GQA group that contains pairs of differential heads. This may require handling the two types of differential heads separately during selection, or maybe a simple average of attention logits might already be sufficient in practice. Conceptually, this does not introduce any fundamental differences compared to block sparse attention of standard Transformers.

More from this author

Hugging Face Models on Foundry Managed Compute  10 July 7, 2026 

Introducing OptiMind, a research model designed for optimization  35 January 15, 2026 

### Community

dhruv3006

Jan 20 

Good to see a V2.

🚀

3

3

+

Reply

allendorf

Jan 20 

very cool!

Reply

ProgramerSalar

Jan 24 

This is a fascinating and thorough update on the Differential Transformer architecture. The transition from DIFF V1 to V2 addresses some critical practical hurdles in a very elegant way.

The key design choice of doubling query heads within shared GQA groups is clever. It successfully decouples the innovative "differential" attention operation from the need for custom kernels, making it a much more viable drop-in replacement for standard attention. The analysis of how this design overcomes the softmax magnitude constraint and helps eliminate attention sinks is particularly convincing.

The reported early results—lower loss, reduced gradient spikes, and better control of activation outliers, especially at large learning rates—are highly promising. It suggests DIFF V2 isn't just a parameter-saving trick but may offer fundamental improvements in training dynamics and stability.

I have a couple of questions out of curiosity:

Long-Context Performance: You mention exploring "context rot" alleviation in later stages. Given the modified attention output dynamics, do you have any early hypotheses on whether DIFF V2 might inherently improve performance on very long sequences compared to a baseline Transformer with similar parameter budgets?

Broader Application: The principle seems powerful yet simple. Beyond the dense and MoE models tested here, do you see potential for applying this differential attention mechanism in other architectures, like state-space models or multimodal transformers?

See translation 

🔥

2

2

+

Reply

deleted

Jan 26 

This comment has been hidden 

EditPreview

Upload images, audio, and videos by dragging in the text input, pasting, or clicking here.

Tap or paste here to upload images

 Comment 

· Sign up or log in to comment

 Upvote 53 
* +41

 System theme 

Company

TOS Privacy About Careers 

Website

Models Datasets Spaces Pricing Docs