Source URL: https://unsloth.ai/docs/basics/faster-moe
Title: Fine-tune MoE Models 12x Faster with Unsloth

> For the complete documentation index, see [llms.txt](https://unsloth.ai/docs/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://unsloth.ai/docs/basics/faster-moe.md).

# Fine-tune MoE Models 12x Faster with Unsloth

We’re introducing \~12x faster Mixture of Experts (MoE) LLM training with **>35% less VRAM** and **\~6x longer context** with our new MoE Triton kernels and new mathematical optimizations, all with no loss in accuracy.

* Unsloth now supports fast training for MoE architectures including [gpt-oss](/docs/models/gpt-oss-how-to-run-and-fine-tune.md), [Qwen3](/docs/models/tutorials/qwen3-how-to-run-and-fine-tune.md) (30B, 235B, VL, Coder), DeepSeek [R1](/docs/models/tutorials/deepseek-r1-0528-how-to-run-locally.md), [V3](/docs/models/tutorials/deepseek-v3.1-how-to-run-locally.md) and GLM ([4.6](https://unsloth.ai/docs/basics/pages/kubJWq6dZSW06gdjy3QO#glm-4.6v-flash), [4.7](/docs/models/tutorials/glm-4.7.md), [Flash](/docs/models/tutorials/glm-4.7-flash.md)).
* gpt-oss-20b fine-tunes in **12.8 GB VRAM**. Qwen3-30B-A3B (16-bit LoRA) uses 63GB.
* Our kernels work on both data-center (B200, H100), **consumer** and older GPUs (e.g., RTX 3090), and FFT, LoRA and QLoRA.

In collaboration with 🤗Hugging Face, we made all MoE training runs standardized with PyTorch’s new `torch._grouped_mm` function. Transformers v5 was recently optimized with \~6x faster MoE than v4 and Unsloth pushes this even further with custom Triton grouped‑GEMM + LoRA kernels for an **additional** \~2x speedup, >35% VRAM reduction and >6x longer context (12-30x overall speedup vs v4).

Try our Unsloth Notebooks for fast MoE training:

| [**gpt-oss (20b)**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-\(20B\)-Fine-tuning.ipynb) **(free)** | [Qwen3-30B-A3B](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_MoE.ipynb) (A100)                                  | [GLM-4.7-Flash](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/GLM_Flash_A100\(80GB\).ipynb) (A100) |
| ------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| [gpt-oss-120b](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-\(120B\)_A100-Fine-tuning.ipynb) (A100)    | [gpt-oss (500K context)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt_oss_\(20B\)_500K_Context_Fine_tuning.ipynb) | [TinyQwen3 MoE](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/TinyQwen3_MoE.ipynb) (test only)     |

<figure><img src="/files/IPo24TGuAVWIhOq9DI2w" alt="" width="563"><figcaption></figcaption></figure>

### 🦥 Unsloth MoE Triton Kernels

Alongside `torch._grouped_mm` (see [#what-is-torch.\_grouped\_mm](#what-is-torch._grouped_mm "mention")), we created custom Triton MoE kernels that can be even faster in some cases. They are also **backwards compatible** with older hardware like A100, and older PyTorch versions.

{% columns %}
{% column width="50%" %}
On A100, our **Triton kernels are \~2.5× faster** than `torch._grouped_mm`. The kernels also have a one‑time autotune step to pick the best kernel config.

Auto-tuning takes \~2 minutes once at the start of training, but can speed up the full run by 35% on A100 vs `_grouped_mm`, which is well worth it for longer runs.
{% endcolumn %}

{% column width="50%" %}

<figure><img src="/files/4zD3FkCcME4Q14Y5Kw8u" alt="" width="295"><figcaption></figcaption></figure>
{% endcolumn %}
{% endcolumns %}

{% hint style="success" %}
The larger the model and more context you use, **the more pronounced the memory savings from our Unsloth kernels will be** (efficiency will scale exponentially).
{% endhint %}

### :compass: Automatic backend selection

Our main innovation is our **Split LoRA approach** for efficient MoE, which uses \~35% less memory and is 2x faster training when compared to Transformers v5 + `torch._grouped_mm`. Custom `torch._grouped_mm` + our Triton kernels are \~12-30x faster than Transformers v4.

<figure><img src="/files/bZWr0eXJ6fx8o4II28lh" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="warning" %}
Training MoE models in **4-bit** QLoRA isn’t recommended right now because BitsandBytes doesn’t support it. This isn’t specific to Unsloth. For now, use bf16 for LoRA or full fine-tuning.
{% endhint %}

Unsloth will auto select either the following backends depending on your hardware:

<table><thead><tr><th width="144.95001220703125">Backend</th><th>Optimizations</th></tr></thead><tbody><tr><td>grouped_mm</td><td><code>torch._grouped_mm</code> - available on T4s all the way until B200s, but optimized for H100s+.</td></tr><tr><td>unsloth_triton</td><td>Unsloth Triton kernels - which will turn on automatically for A100s, and older PyTorch versions.</td></tr><tr><td>native_torch</td><td>Native PyTorch. It's 12x slower, but our VRAM reductions are still there!</td></tr></tbody></table>

You can also toggle them yourself:

```python
os.environ["UNSLOTH_MOE_BACKEND"] = "grouped_mm"
os.environ["UNSLOTH_MOE_BACKEND"] = "unsloth_triton"
os.environ["UNSLOTH_MOE_BACKEND"] = "native_torch"
```

{% hint style="success" %}
To enable faster MoE training, update Unsloth via `pip install --upgrade unsloth unsloth_zoo`
{% endhint %}

### ❓What is torch.\_grouped\_mm?

Previously, Mixture-of-Experts (MoE) weights were stored as a `ModuleList` of per‑expert linear layers. The only practical way to run a forward pass was a for‑loop over experts, which is expensive and suboptimal.

```python
for expert_idx in expert_hit:
    expert_idx = expert_idx[0]
    if expert_idx == num_experts: continue
    _, token_idx = torch.where(expert_mask[expert_idx])
    current_state = hidden_states[token_idx]
    gate, up = nn.functional.linear(current_state, self.gate_up_proj[expert_idx]).chunk(2, dim=-1)
```

PyTorch recently introduced [`grouped_mm`](https://docs.pytorch.org/docs/main/generated/torch.nn.functional.grouped_mm.html) to address this exact bottleneck. In parallel, we provide our own MoE‑optimized Triton kernels. This also lines up with a key Transformers change: as of Transformers v5, expert weights are stored as a [`single nn.Parameter`](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/qwen3_moe/modeling_qwen3_moe.py#L226), making `grouped_mm` a natural fit for faster MoE training and inference.

So [transformers 4.57.6](https://github.com/huggingface/transformers/blob/v4.57.6/src/transformers/models/qwen3_moe/modeling_qwen3_moe.py#L222) changed:

{% code overflow="wrap" %}

```python
self.experts = nn.ModuleList(
    [Qwen3MoeMLP(config, intermediate_size) for _ in range(self.num_experts)]
)
```

{% endcode %}

to [transformers 5.0.0](https://github.com/huggingface/transformers/blob/v5.0.0/src/transformers/models/qwen3_moe/modeling_qwen3_moe.py#L226) style:

{% code overflow="wrap" %}

```python
self.gate_up_proj = nn.Parameter(torch.empty(num_experts, 2 * intermediate_dim, hidden_dim))
```

{% endcode %}

`torch._grouped_mm` works on GPUs starting with the NVIDIA T4, and we’ve verified it on H100, A100, B200, and RTX 6000 Pro, so support is broadly available.

We also previously introduced Unsloth [Flex Attention](/docs/models/gpt-oss-how-to-run-and-fine-tune/long-context-gpt-oss-training.md) for gpt-oss, and these optimizations should make it even more efficient.

## 📊 Kernel Results + Benchmarks

Below is a comparison across sequence lengths for training speed and memory usage versus Transformers v5 (which already uses `torch._grouped_mm` for MoE). For **gpt-oss BF16 MoE training, we see 7x faster training and 36% VRAM reduction** on NVIDIA B200. For Qwen3-30B-A3B, it's 1.8x faster, and **GLM 4.7 Flash is 2.1x faster on RTX PRO 6000**. All benchmarks are done with LoRA rank = 64 and all LoRA modules on MoE layers (gate, up, down).

### gpt-oss Benchmarks

We fine-tuned [unsloth/gpt-oss-20b-BF16](https://huggingface.co/unsloth/gpt-oss-20b-BF16) for benchmarking. Unsloth is 7x faster and uses 36% less VRAM at 16K context lengths. Transformers v5 + TRL goes out of memory whilst Unsloth does not. Also the speed up increases with sequence length in this case thanks to our [Long Context gpt-oss](/docs/models/gpt-oss-how-to-run-and-fine-tune/long-context-gpt-oss-training.md#unsloths-flex-attention-implementation), and our MoE kernels.

<div><figure><img src="/files/4AHGgTbBNsBwLZ77rW51" alt="" width="563"><figcaption></figcaption></figure> <figure><img src="/files/7GfQ13W0itOfD0gQJcZF" alt="" width="188"><figcaption><p>Comparison with transformers v4</p></figcaption></figure></div>

<table data-full-width="true"><thead><tr><th>Context Length</th><th>Unsloth (ms)</th><th>TF v5 (ms)</th><th>Unsloth Mem (GB)</th><th>TF v5 Mem (GB)</th><th>Speed Up</th><th>VRAM Saving</th><th data-hidden>Rank</th><th data-hidden>Unsloth Warmup (ms)</th><th data-hidden>TRL Warmup (ms)</th></tr></thead><tbody><tr><td>1024</td><td>275.35</td><td>376.99</td><td>40.91</td><td>43.88</td><td>1.4x</td><td>6.76%</td><td>8</td><td>2601.17</td><td>615.62</td></tr><tr><td>2048</td><td>292.88</td><td>696.57</td><td>41.83</td><td>44.93</td><td>2.4x</td><td>6.89%</td><td>8</td><td>4996.62</td><td>928.42</td></tr><tr><td>4096</td><td>370.30</td><td>1785.89</td><td>43.68</td><td>49.86</td><td>4.8x</td><td>12.39%</td><td>8</td><td>6648.94</td><td>2130.33</td></tr><tr><td>8192</td><td>712.33</td><td>5226.86</td><td>47.43</td><td>73.80</td><td>7.3x</td><td>35.73%</td><td>8</td><td>9632.44</td><td>5472.66</td></tr><tr><td>16384</td><td>1775.80</td><td><strong>OOM</strong></td><td>55.13</td><td><strong>OOM</strong></td><td>N/A</td><td>N/A</td><td>8</td><td>12696.26</td><td>N/A</td></tr></tbody></table>

### Qwen3 Benchmarks

On an **NVIDIA B200**, we see **\~1.7x speedup and \~35% better memory efficiency with Qwen3-30B-A3B LoRA**, with memory savings improving further at longer sequence lengths.

Qwen3-Next and Coder surprisingly fit on a single B200 GPU in bf16 LoRA.

<figure><img src="/files/YcqKUlp5avSX81UHeruB" alt="" width="563"><figcaption></figcaption></figure>

On H100 GPU, we perform significantly better than the baseline getting up to **1.77x speed up** in training while also saving \~5.3GB when fine tuning at 4K context length. While we seamlessly scale to 8192 context lengths, Transformers v5 + TRL OOMs at 8K. Notice that we use less memory at 8K than the baseline does at 4K so we can keep pushing the context length further.

<table data-full-width="true"><thead><tr><th>Context Length</th><th>Unsloth (ms)</th><th>TF v5 (ms)</th><th>Unsloth Mem (GB)</th><th>TF v5 Mem (GB)</th><th>Speed Up</th><th>VRAM Saving</th><th data-hidden>Rank</th></tr></thead><tbody><tr><td>1024</td><td>366.3</td><td>628.3</td><td>80.88</td><td>104.80</td><td>1.7x</td><td>2.06%</td><td>8</td></tr><tr><td>2048</td><td>467.0</td><td>745.3</td><td>80.88</td><td>104.81</td><td>1.6x</td><td>2.57%</td><td>8</td></tr><tr><td>4096</td><td>711.6</td><td>975.5</td><td>80.89</td><td>104.80</td><td>1.4x</td><td>5.08%</td><td>8</td></tr><tr><td>8192</td><td>1376.6</td><td>1633.5</td><td>80.90</td><td>104.81</td><td>1.2x</td><td>9.17%</td><td>8</td></tr><tr><td>16384</td><td>3182.2</td><td>3407.9</td><td>85.53</td><td>116.61</td><td>1.1x</td><td>15.26%</td><td>8</td></tr></tbody></table>

### GLM 4.7 Benchmarks

Unsloth achieves **2.6x faster throughput with >15% less VRAM** across all batch sizes for GLM 4.7 Flash. GLM 4.7 Flash is a 30B MoE (3B active parameters) agentic & coding model and employs a configuration similar to the DeepSeek MoE style, featuring 64 routed experts and 1 shared expert. We benchmarked Unsloth MoE training vs the new optimized Transformers v5.

Use our new Colab notebook for GLM 4.7 Flash below:

{% embed url="<https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/GLM_Flash_A100(80GB).ipynb>" %}
GLM 4.7 Flash MoE Notebook A100 80GB
{% endembed %}

<figure><img src="/files/JY7Dmo9LU7eGzr3Bpwdo" alt="" width="563"><figcaption></figcaption></figure>

<table data-full-width="true"><thead><tr><th>Context Length</th><th>Unsloth (ms)</th><th>TF v5 (ms)</th><th>Unsloth Mem (GB)</th><th>TF v5 Mem (GB)</th><th>Speed Up</th><th>VRAM Saving</th><th data-hidden>Rank</th><th data-hidden>Unsloth Warmup (ms)</th><th data-hidden>TRL Warmup (ms)</th></tr></thead><tbody><tr><td><p></p><p>512</p></td><td>1145.0</td><td>2992.1</td><td>57.81</td><td>60.89</td><td>2.6x</td><td>6.51%</td><td>8</td><td>13317.46</td><td>893.04</td></tr><tr><td>1024</td><td>1298.9</td><td>3323.3</td><td>58.76</td><td>62.55</td><td>2.6x</td><td>6.22%</td><td>8</td><td>12895.28</td><td>937.37</td></tr><tr><td>2048</td><td>1831.9</td><td>4119.3</td><td>60.09</td><td>67.32</td><td>2.3x</td><td>9.46%</td><td>8</td><td>12531.37</td><td>1039.45</td></tr><tr><td>4096</td><td>2883.9</td><td>5646.1</td><td>63.34</td><td>76.78</td><td>2x</td><td>14.83%</td><td>8</td><td>7671.60</td><td>1643.26</td></tr></tbody></table>

### ⚡Faster LoRA MoE training

In Transformers/PEFT, the usual approach is to **merge the LoRA adapter into the base weight** and then run the MoE computation (especially since MoE often uses `nn.Parameter` instead of `nn.Linear`). The problem is that this merge effectively **materializes the LoRA delta (for all the experts)** `lora_B @ lora_A.t`, which is **very memory-hungry**.

Unsloth avoids that. We previously used the same idea to optimize generic LoRA training and inference, and we’ve now applied it to **MoE + LoRA** as well. The math is identical, so the loss, gradients, and outputs stay the same. The only change is **the order of operations**, made possible by matrix-multiplication associativity. With this reordering, we get major speedups and memory reductions.

{% hint style="warning" %}
Training MoE models in **4-bit** QLoRA isn’t recommended right now because BitsandBytes doesn’t support it. This isn’t specific to Unsloth. For now, use bf16 for LoRA or full fine-tuning.
{% endhint %}

These optimizations are **enabled by default** when training MoE models with Unsloth (notably Qwen-3 MoE, gpt-oss, and the models mentioned above). You can switch implementations via the `UNSLOTH_MOE_BACKEND` environment variable: either `torch._grouped_mm` **Triton kernels** or a **basic PyTorch for-loop**, depending on compatibility and preference. We default to `grouped_mm` for the best performance and broad support.

```python
import os
# if you want to choose a different backend (grouped_mm by default), set the below variable:
# os.environ['UNSLOTH_MOE_BACKEND'] = 'unsloth_triton' # or grouped_mm or native_torch
lora_rank = 16
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "Qwen/Qwen3-30B-A3B-Instruct-2507", #MoE model
    max_seq_length = max_seq_length,
    load_in_4bit = False, # MoE nn.Parameter doesn't support bnb 4bit yet
)
model = FastLanguageModel.get_peft_model(
    model,
    r = lora_rank,
    target_modules = [
        "q_proj", "k_proj", "v_proj", "o_proj",
        "gate_up_proj", "down_proj", # LoRA on MoE layers!
    ],
    lora_alpha = lora_rank*2, # *2 speeds up training
    use_gradient_checkpointing = "unsloth", # Reduces memory usage
    random_state = 3407,
)
```

## 📚 Details of implementation

LoRA is a parameter-efficient fine-tuning method: instead of updating the full weight matrix, you train a low-rank “adapter” with far fewer parameters, which drastically reduces optimizer memory.

If the original weight has shape **(m, n)**, LoRA adds two trainable matrices with shapes **(m, r)** and **(r, n)**. Their product is **(m, n)**, but you only track optimizer states and gradients for:

* `m*r + r*n` parameters (LoRA) instead of
* `m*n` parameters (full fine-tuning)

{% hint style="info" %}
On fine-tuning MoE's - it's not a good idea to fine-tune the router layer so we disabled it by default.
{% endhint %}

For typical MLP layers, `m ≈ 4096, n ≈ 12k, and r ≈ 64`, that’s roughly **\~1M LoRA parameters vs \~48M full parameters -** about **\~2%,** often with minimal to no accuracy loss.

<figure><img src="/files/Oy2irTy2csZKayfYFw6N" alt="" width="255"><figcaption></figcaption></figure>

#### MoE LoRA changes things

MoE layers are different because you have **E expert MLPs in parallel**, so any per‑expert change (like adding LoRA) scales across all experts.

Take **Qwen3‑30B‑A3B**: hidden size **m=2048**, intermediate size **n=768**, **E=128** experts with **k=8** activated per token. Per expert:

* `gate_proj` and `up_proj`: `(m, n) = (2048, 768)`
* `down_proj`: `(n, m) = (768, 2048)`

With **LoRA rank r=64**, each projection adds `r*(m+n)=64*(2048+768)=180,224` parameters per expert (≈ `11%` of a `2048×768` matrix). The core issue is that `r/n = 64/768` is large compared to typical MLP setups, for e.g., `r/n = 64/25600` in [Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B/blob/main/config.json#L13) of similar size.

If you materialize this across *all* experts, memory adds up quickly. And since `gate_proj` and `up_proj` are often fused as `gate_up_proj`, you typically materialize both together, roughly doubling the overhead/peak memory.

**In terms of memory, for a sequence length s, E experts and `k` chosen, we have the following common for both approaches**

```
# All these values are per expert
Final output: (s, n)
Input activations: (s, m)
Final output: (s, n)
```

This is where things start to diverge. For peft’s approach we have

```
delta = loraA@loraB  = (m,n) per expert = Emn parameters
```

For Unsloth’s split LoRA approach, we perform the following operations

```
Y = X @ loraA : (s,m) @ (m, r)       # but sparse for k experts = ksr parameters
Y @ loraB: (s, r) @ (r, n)           # but sparse again for k experts = ksn parameters
```

Now lets take the case of Qwen3-30B-A3B.

`E = 128, k = 8, m = 2048, n = 768.` Plugging all these in , we get `s < 32K.`&#x20;

$$
\begin{aligned}
\text{PEFT params}                       &:\quad Emn \\
\text{Unsloth Split LoRA params}         &:\quad ks(r+n) \\
\text{In typical LoRA we have}           &:\quad r \ll n \\
\text{Split LoRA is better when}         &:\quad Emn > ksn ;=; Em > ks \\
\\
\text{For Qwen3-30B-A3B, we have} \\
E &= 128, \quad k = 8, \quad m = 2048, \quad n = 768 \\
\\
\text{So, Split LoRA is mathematically better when} \\
s &< \frac{Emn}{kn} = 32K
\end{aligned}
$$

**In terms of compute, for a sequence length `s`, `E` experts and top `k` chosen, we're doing:**

$$
\begin{aligned}
\Delta = AB,
A \in \mathbb{R}^{m \times r}, ;
B \in \mathbb{R}^{r \times n}
&\quad \Rightarrow \quad 2mnr \text{ flops per expert lora} \\
\\
W' = W + \Delta
\quad &\Rightarrow \quad mn \text{ flops} \\
\\
XW'  \quad | \quad
X \in \mathbb{R}^{s \times m}, ;
W' \in \mathbb{R}^{m \times n}
\quad &\Rightarrow \quad 2smn \text{ flops} \\
\\
\text{MoE peft lora flops}
&= E\big(2mnr + mn\big)

* 2k,smn
  \end{aligned}
  $$

In case of Unsloth split lora that we mentioned, we have

$$
\begin{aligned}
XW &= 2smn  \text{  flops} \\
Y = XA, &= 2smr
\quad \text{(applied only to routed token--expert pairs)} \\
\
Z = YB &= 2srn \\
\text{MoE split lora flops}
&= 2k\big(smn + smr + srn\big) \\
\text{Crossover condition}
&:\quad 2ksr(m+n) > 2Emn(r+1/2)
\Rightarrow
s > \frac{Emn}{k(m+n)} \times (1+ \frac{1}{2r}) \\
\\
\text{For Qwen3-30B-A3B with}
&:
E = 128,;
m = 2048,;
n = 768,;
k = 8 \\
\\
\Rightarrow \quad
s
& ;\approx; 16\text{K tokens}
\end{aligned}
$$

The point till where the Split LoRA from analytical perspective  is better is when `s > Emn/k(m+n)` which is in the order of `16K` tokens for Qwen3-30B-A3B style model.

Finally, some speedups come from **reduced memory traffic**: modern GPUs are often **bandwidth‑bound**, so transferring less data can matter more than FLOPs. A rough speedup estimate is `Emn / [k·s·(m+n)]`, so it depends strongly on **s, E, k**, and the matrix shapes.

### 🔮 Model Support

Unsloth supports faster MoE training for Qwen, gpt-oss, DeepSeek and GLM models:

* **Qwen3** (Thinking and Instruct): VL • 2507 • Coder&#x20;
* **gpt-oss**: 20B • 120B • safeguard
* **GLM**: 4.5 • 4.6 • 4.6-Air • 4.7 • 4.7-Flash
* **DeepSeek**: V3 • R1 • V3.1 • V3.2

We may have not uploaded some MoE models, but Unsloth should still support them.

### 📈 More Benchmarks

#### gpt-oss BF16 Benchmarks

Training Speed including vs Transformers v4

<table data-full-width="false"><thead><tr><th align="right">Context length</th><th align="right">Unsloth (ms)</th><th align="right">TF v5 (ms)</th><th align="right">TF v4 (ms)</th><th align="right">Speed Up</th></tr></thead><tbody><tr><td align="right">1024</td><td align="right">275.35</td><td align="right">376.99</td><td align="right">2111.18</td><td align="right">1.37x</td></tr><tr><td align="right">2048</td><td align="right">292.88</td><td align="right">696.57</td><td align="right">2626.80</td><td align="right">2.38x</td></tr><tr><td align="right">4096</td><td align="right">370.30</td><td align="right">1785.89</td><td align="right">4027.93</td><td align="right">4.82x</td></tr><tr><td align="right">8192</td><td align="right">712.33</td><td align="right">5226.86</td><td align="right">8513.52</td><td align="right">7.34x</td></tr><tr><td align="right">16384</td><td align="right">1775.80</td><td align="right">OOM</td><td align="right">OOM</td><td align="right">N/A</td></tr></tbody></table>

**Memory VRAM usage**

<table data-full-width="false"><thead><tr><th align="right">Context length</th><th align="right">Unsloth Mem (GB)</th><th align="right">TF v5 Mem (GB)</th><th align="right">TF v4 Mem (GB)</th><th align="right">VRAM Saving</th></tr></thead><tbody><tr><td align="right">1024</td><td align="right">40.91</td><td align="right">43.88</td><td align="right">89.75</td><td align="right">6.76%</td></tr><tr><td align="right">2048</td><td align="right">41.83</td><td align="right">44.93</td><td align="right">90.47</td><td align="right">6.89%</td></tr><tr><td align="right">4096</td><td align="right">43.68</td><td align="right">49.86</td><td align="right">92.72</td><td align="right">12.39%</td></tr><tr><td align="right">8192</td><td align="right">47.43</td><td align="right">73.80</td><td align="right">100.3</td><td align="right">35.73%</td></tr><tr><td align="right">16384</td><td align="right">55.13</td><td align="right">OOM</td><td align="right">OOM</td><td align="right">N/A</td></tr></tbody></table>

## :tada: Important Unsloth Updates

1. As part of our MoE release, we also made **Gemma-3 now use Flex-Attention** by default, and this works in float16 settings as well (there were infinities which we solved a while back). **Gemma-3 now uses O(N) memory and not O(N^2) memory, and trains >3x faster** (scales even better with context length). Previous Unsloth versions would OOM.

<figure><img src="/files/sLIhPTSM85zwn3qoJfTD" alt="" width="375"><figcaption></figcaption></figure>

| Context | Old Peak VRAM | New Peak VRAM | VRAM Saving   |
| ------- | ------------- | ------------- | ------------- |
| 1K      | 20.1 GB       | 20.1 GB       | 0 GB (0%)     |
| 2K      | 21.5 GB       | 21.1 GB       | 0.3 GB (2%)   |
| 4K      | 27.7 GB       | 23.3 GB       | 4.5 GB (16%)  |
| 8K      | 52.3 GB       | 27.5 GB       | 24.8 GB (47%) |
| 16K     | OOM           | 36.0 GB       | --            |
| 24K     | OOM           | 44.6 GB       | --            |
| 32K     | OOM           | 53.1 GB       | --            |
| 48K     | OOM           | 38.4 GB       | --            |
| 64K     | OOM           | 44.7 GB       | --            |

2. Vision fine-tuning now accepts mixed data of only images and text data!
3. [Windows is now officially supported with no need for WSL](/docs/get-started/install/windows-installation.md).
4. `trl==0.27.1` and `transformers==5.1.0` are supported well - previous coverage was 30% of all our 120 notebooks, but now we have >80% coverage - we plan to make it 100% over the next few days.
5. Many bug fixes and other updates - see <https://github.com/unslothai/unsloth/releases/tag/February-2026>

{% hint style="success" %}
To enable faster MoE training, update Unsloth via `pip install --upgrade unsloth unsloth_zoo`
{% endhint %}

### Acknowledgements

We thank the Hugging Face team for collaborating with us on improving MoE training for the community.

We also sincerely thank the torchao team, especially Vasily Kuznetsov (vkuzo) for working helping us enabling grouped\_mm support for float16 to get it work on T4 and backward compatibility with A100.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://unsloth.ai/docs/basics/faster-moe.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
