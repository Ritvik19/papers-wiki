# Papers Explained: Yet another RoPE extensioN method (YaRN)

Papers Explained: Yet another RoPE extensioN method (YaRN)

Papers Explained: Yet another RoPE extensioN method (YaRN)

YaRN (Yet another RoPE extensioN method) is a compute-efficient technique for extending the context window of models trained with Rotary…

Papers Explained: Yet another RoPE extensioN method (YaRN)

YaRN (Yet another RoPE extensioN method) is a compute-efficient technique for extending the context window of models trained with Rotary Position Embeddings (RoPE), allowing models to extrapolate to much longer contexts than originally allowed and even beyond the limits of the fine-tuning dataset. This method can extend context windows over 2x without any fine-tuning when combined with Dynamic Scaling, all while requiring less than ~0.1% of the original pre-training data for fine-tuning.

Background

Suppose the hidden dimension is D. For each dimension d, RoPE has a frequency: θ_d = b ^ (−2d/∣D∣), where b=10000.

At position m, RoPE rotates that complex number by m . θ_d. Using complex numbers, rotation is simply multiplication by e ^(i . m . θ_d). Thus:

for any linear operator W . The functions fq , fk in RoPE are given by: fq = fWq , fk = fWk .

A context length interpolation usually aims to modify the equation above and take the form:

where g(m) is a map between real numbers and h(θ) acts on the entries of the diagonal matrix θ.

Given the pretrained maximal context length L, our goal is to extend it to L′ > L either with or without finetuning. A scaling factor s is defined as s = L′ / L .

The wavelength λd associated with the d-th hidden dimension of RoPE is:

The wavelength describes the length of tokens needed in order for the rotary position embedding at dimension d to perform a full rotation (2π). ​ Position Interpolation (PI) is one of the earlier works extending context lengths of RoPE, it sets:

Method

NKT Aware Interpolation

In the case of Positional Interpolation (PI), as all dimensions are stretched equally by a factor s, it removes the high frequency components of RoPE. This degradation is worsened as the scaling factor s grows, and at some point, the network will not be able to recover.
Suppose its wavelength is 10 tokens: λ=10After PI, for s = 4 :  λ′ = 10 . s = 40This makes the rapidly changing dimension 4× slower.So information that used to distinguish position 100 vs 101 vs 102 becomes much less distinct.
In order to alleviate this issue, the “NTK-aware” (Neural Tangent Kernel (NTK) theory: that deep neural networks have trouble learning high frequency information if the input dimension is low and the corresponding embeddings lack high frequency components) interpolation was developed.

Instead of scaling every dimension of RoPE equally by a factor s, the interpolation pressure is spread out across multiple dimensions by scaling high frequencies less and low frequencies more. Such a transformation can be obtained in many ways, but the simplest would be to perform a base change on the value of θ.

NTL by Parts Interpolation

In theory RoPE encodes relative position. But only partially true. Different RoPE dimensions can actually behave differently.

Given a context size L, there are some dimensions d where the wavelength is longer than the maximum context length seen during pretraining (λ > L); this suggests that some dimensions’ rotary embeddings might not be distributed evenly in the rotational domain (i.e., do not perform a full rotation for the entire training context size). In such cases, having unique position pairs implies that the absolute positional information remains intact in those dimensions. On the contrary, when the wavelength is short, only relative positional information is accessible to the network.

Given these observations:

Region 1: very short wavelengths (λ≪L)

These are high-frequency dimensions.
They already rotate many times during training.
These dimensions are mainly useful for relative local position.So:
Don’t interpolate

Region 2:  very long wavelengths (λ≫L)

These dimensions barely rotate during training.
They are essentially carrying absolute position.
For extending the context, they need to cover the larger range.
Interpolate

Region 3: in-between (λ≈L)

These have properties of both.
Partially interpolate​

It is more convenient to introduce the ratio r to represent the number of rotations a certain RoPE dimension makes, given a fixed pretrained context length L.

Two extra parameters α, β are introduced and the ramp function γ is defined to be:

With the help of the ramp function, the “NTK-by-parts” method can be described as a modification of RoPE with the following functions:

YaRN

In addition to the previous interpolation techniques, it is also observed that introducing a temperature t on the logits before the attention softmax has a uniform impact on perplexity regardless of the data sample and the token position over the extended context window.

Instead of changing the attention scores, a “length scaling” trick can be used which scales both qm and kn by a constant factor 1/sqrt(t). For Llama and Llama 2 models, the following values are recommended:
An outline of the relationship between different interpolation methods.
YaRN = NTK-by-parts RoPE interpolation + attention temperature scaling​

The first fixes the positional encoding problem.

The second fixes the attention distribution problem.

Dynamic Scaling

In a lot of use cases, multiple forward-passes are performed with varying sequence lengths from 1 to the maximal context size.

If throughout the whole inference cycle, the embedding layer is fixed including the scale factor s, the model may experience a performance discount at a length less than L
and an abrupt degradation when the sequence length is longer than L′.

Instead let the scale depend on the current sequence length l’:
s = max(1, l′/L)

By doing this Dynamic Scaling, the model is allowed to gracefully degrade instead of immediately breaking when hitting the trained context limit L′.

Evaluation

Llama 2 models (7B and 13B) were fine-tuned with embedding frequency modifications (using s = 16 and s = 32) and tested on long-context tasks; training used the PG19 dataset chunked into 64k segments. The s = 32 model was fine-tuned for an additional 200 steps from the s = 16 checkpoint.
Sliding window perplexity (S = 256) of ten 128k Proof-pile documents over Llama 2 models extended via YaRN.
YaRN enables the s = 32 model to extrapolate to 128k context lengths even though it was only trained on 64k context data, demonstrating effective generalization and transfer learning.
Sliding window perplexity (S = 256) of ten 128k Proof-pile documents and passkey retrieval accuracy at different prompt lengths for finetuned LLaMA 7B models fine-tuned to 32k context for 400 steps using different interpolation techniques.
YaRN consistently outperforms other interpolation approaches in both fine-tuned and non-fine-tuned settings on long-sequence modeling task.
On the passkey retrieval task, YaRN achieves higher accuracy than other interpolation techniques at equivalent training budgets.
Performance of context window extensions methods, fine-tuned for 400 steps, on the Hugging Face Open LLM benchmark suite.Performance of YaRN on the Hugging Face Open LLM benchmark suite.
Minimal performance degradation is observed in short-context standardized benchmarks.

Paper

YaRN: Efficient Context Window Extension of Large Language Models 2309.00071

That’s a wrap!

If you enjoyed this breakdown, follow for more. I publish new paper explanations most weekdays.

More papers in this series, organized by lab and topic, are in the start here guide.

What paper should I cover next? Let me know in the responses.

View original.

Exported from Medium on August 22, 2026.
