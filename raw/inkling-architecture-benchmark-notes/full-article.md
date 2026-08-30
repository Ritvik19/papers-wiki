# Inkling Architecture and Benchmark Notes

Source URL: https://sebastianraschka.com/blog/2026/inkling-architecture-benchmark-notes.html

Interesting surprise open-weight LLM drop from Thinking Machines Lab yesterday. Their nearly 1T-parameter Inkling model looks pretty solid on the reported benchmarks.

Compared with GLM-5.2, Inkling performs better on evaluations such as IFBench (79.8% versus 73.3%) and SimpleQA Verified (43.9% versus 38.1%). It performs worse on several reasoning and coding-agent benchmarks, including HLE without tools (29.7% versus 40.1%), SWE-Bench Pro Public (54.3% versus 62.1%), and Terminal-Bench 2.1 (63.8% versus 82.7%).

These are release-time numbers, and some rows combine externally reported values with internal harness results. I would therefore not over-interpret small differences. Overall, Inkling looks like a good all-rounder that is intended for further fine-tuning and specialization. That direction makes sense given that Thinking Machines Lab also develops Tinker, its model customization and fine-tuning platform.

Architecture-wise, Inkling is a 975B-parameter sparse Mixture-of-Experts model with 41B active parameters and a context window of up to 1M tokens.

Some side-by-side observations:

1. Inkling has about 231B more total parameters than GLM-5.2 (975B versus 744B), although their active footprints are almost identical at 41B and 40B parameters.
2. Inkling is less sparse than Kimi K2.5. It activates 4.2% of its parameters per token, compared with 3.2% for Kimi K2.5 (41B of 975B versus 32B of 1T).
3. Inkling uses a regular Transformer decoder rather than the hybrid Mamba-Transformer approach used by Nemotron 3 Ultra.

The overall design follows the recent large-MoE trend, but the architecture has a few interesting surprises:

- Small convolution layers in several places. Each decoder layer applies short kernel-4 convolutions after the key and value projections and on the attention and MLP branch outputs.
- An additional RMSNorm directly after the token embedding layer, separate from the pre-attention RMSNorm inside every transformer block.
- A learned, input-dependent relative-position bias instead of RoPE. Thinking Machines says that the relative-position approach "performs better and extrapolates better to longer sequences" than RoPE.
- Of the 66 decoder layers, 55 use local attention with a small 512-token window. In the 11 global layers, the released implementation applies the learned bias only over the preceding 1,024 tokens.

Overall, Inkling is an interesting variation on the DeepSeek-V3-style MoE recipe and a solid release with a broad and mixed benchmark profile.
