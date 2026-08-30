# Beyond Standard LLMs

**Source**: `raw/beyond-standard-llms/full-article.md` (566 KB), `raw/beyond-standard-llms/full-article.md` (markdown view)  
**URL**: https://magazine.sebastianraschka.com/p/beyond-standard-llms  
**Ingested**: 2026-06-07  
**Tags**: #summary

## Summary

Sebastian Raschka's November 2025 *Ahead of AI* survey follows his *Big LLM Architecture Comparison* and covers four families of **non-standard** open-weight LLM approaches: [[Linear Attention Hybrids]], [[Text Diffusion LLMs]], [[Code World Models]], and [[Small Recursive Transformers]]. The article's premise is that decoder-style autoregressive transformers (DeepSeek R1, Qwen3, Kimi K2, MiniMax-M2, etc.) remain state-of-the-art and the practical default for new projects—but researchers are actively exploring alternatives for efficiency, parallelism, execution-aware code modeling, and tiny specialized reasoning.

The longest section covers **linear attention hybrids**. Raschka revisits classic linear attention (kernel approximations that avoid the n×n attention matrix) and why early variants never reached SOTA, then walks through the 2025 revival: MiniMax-M1 (lightning attention), Qwen3-Next (Gated DeltaNet + gated full attention in a 3:1 ratio), DeepSeek V3.2 (sparse/subquadratic attention), MiniMax-M2's retreat back to regular attention for reasoning/agentic quality, and Kimi Linear's renewed bet on linear attention with Kimi Delta Attention (channel-wise decay gates). [[Gated DeltaNet]] is explained as a recurrent state-update alternative to softmax attention—fixed-size memory S instead of growing [[KV Cache]]—with α/β gates controlling decay and update, plus an output gate. Qwen3-Next and Kimi Linear both interleave three linear layers per one full-attention layer to recover global context. Kimi Linear adds MLA (multi-head latent attention) with NoPE on global layers and reports ~75% KV-cache reduction and up to 6× decoding throughput vs full attention.

**Text diffusion LLMs** (LLaDA, Gemini Diffusion, etc.) remove the causal mask and train a bidirectional decoder to iteratively unmask corrupted token sequences—parallel token updates across denoising steps instead of strict next-token autoregression. The efficiency pitch: dozens of diffusion steps can beat thousands of serial decode steps for long outputs. Raschka flags ParallelBench findings that parallel decoding can break token dependencies (e.g., sampling "New" and "City" independently), that quality degrades on real tasks, and that tool-calling chains are awkward without sequential generation.

**Code world models** shift from static next-token code completion to simulating program execution: CWM (32B, 131k context) mid-trains on Python execution traces and agentic Docker trajectories, predicting variable states after each line. At inference it remains autoregressive but emits structured execution traces; with best@k test-time scaling it rivals much larger reasoning models on SWE-bench. Raschka frames this as a performance-oriented complement to efficiency-focused hybrids.

**Small recursive transformers** (HRM, Mixture-of-Recursions, TRM) are puzzle specialists—not general text LLMs. TRM (7M params) alternates latent-state and answer updates over up to 16 refinement steps with full backprop through the recursion; it beats HRM on ARC/Sudoku while training for under ~$500 on 4× H100 for two days. Ablations show 2-layer transformers generalize better than 4-layer and that self-attention can be replaced by MLP on fixed small grids. Raschka closes by recommending standard autoregressive transformers as the default, with hybrids for long-context efficiency, diffusion as an experimental parallel-decoding path, CWM as a promising code-understanding direction, and tiny recursive models as future tool modules inside larger agent systems.

## Key Claims

- Open-weight SOTA LLMs (late 2024–2025) remain autoregressive decoder transformers; Raschka would still choose them for new LLM projects today.
- Classic linear attention reduces attention from O(n²) to O(n) but historically hurt accuracy and never reached open SOTA until the 2025 hybrid revival.
- MiniMax-M2 abandoned linear attention, citing poor reasoning and multi-turn accuracy in production; Kimi Linear (Oct 2025) re-validated linear hybrids at 48B scale.
- Qwen3-Next and Kimi Linear use a 3:1 ratio of Gated DeltaNet linear layers to full attention; Gated DeltaNet keeps fixed recurrent state S instead of growing KV cache.
- Gated DeltaNet memory scales as batch × heads × d_head² (no sequence-length term); full MHA KV cache scales with n_tokens.
- Kimi Linear's Kimi Delta Attention replaces scalar per-head decay gates with channel-wise gates; global layers use MLA with NoPE instead of Qwen3-Next's gated MHA.
- Text diffusion LLMs are bidirectional decoder transformers trained with a masking/denoising objective; LLaDA uses a Llama 3 backbone without causal masking.
- Parallel decoding in diffusion LLMs can produce incoherent joint samples; ParallelBench reports dramatic quality loss and poor adaptive parallelism.
- Diffusion LLMs cannot stream token-by-token and make tool-calling chains non-trivial compared to autoregressive CoT flows.
- CWM learns to predict program state (variable values) after code edits—not just plausible token continuations; 32B CWM matches gpt-oss-20b on coding benchmarks, beats gpt-oss-120b with best@k scaling at 4× smaller size.
- TRM (7M params) outperforms HRM on ARC/Sudoku; fewer layers (2 vs 4) and MLP-instead-of-attention can improve generalization on small fixed grids.
- xLSTMs, Liquid Foundation Models, pure SSMs, and transformer-RNN hybrids are explicitly deferred to a future article.

## Figures

| Figure | Caption | Page |
|--------|---------|------|
| ![fig-1](../assets/beyond-standard-llms/fig-1.webp) | LLM landscape overview; black-framed architectures covered in this article | — |
| ![fig-2](../assets/beyond-standard-llms/fig-2.webp) | Notable decoder-style transformers released in the past year | — |
| ![fig-3](../assets/beyond-standard-llms/fig-3.webp) | Subset of architectures from the Big LLM Architecture Comparison | — |
| ![fig-4](../assets/beyond-standard-llms/fig-4.webp) | Traditional scaled-dot-product attention; quadratic cost in sequence length n | — |
| ![fig-5](../assets/beyond-standard-llms/fig-5.webp) | Timeline of linear attention hybrid architectures (MiniMax-M1 through Kimi Linear) | — |
| ![fig-6](../assets/beyond-standard-llms/fig-6.webp) | Qwen3-Next: gated attention and Gated DeltaNet blocks | — |
| ![fig-7](../assets/beyond-standard-llms/fig-7.webp) | Regular Qwen3 (left) vs Qwen3-Next (right) | — |
| ![fig-8](../assets/beyond-standard-llms/fig-8.webp) | Gated attention vs Gated DeltaNet | — |
| ![fig-9](../assets/beyond-standard-llms/fig-9.webp) | Traditional attention mechanism (quadratic in n) | — |
| ![fig-10](../assets/beyond-standard-llms/fig-10.webp) | KV cache growth: full attention vs 3:1 Gated DeltaNet hybrid | — |
| ![fig-11](../assets/beyond-standard-llms/fig-11.webp) | Qwen3-Next and Kimi Linear architectures side by side | — |
| ![fig-12](../assets/beyond-standard-llms/fig-12.webp) | Kimi Linear speed/accuracy vs GatedDeltaNet-H1 and MLA baselines | — |
| ![fig-13](../assets/beyond-standard-llms/fig-13.webp) | Image diffusion denoising (forward noise, reverse denoise) | — |
| ![fig-14](../assets/beyond-standard-llms/fig-14.webp) | Text diffusion models section overview | — |
| ![fig-15](../assets/beyond-standard-llms/fig-15.gif) | LLaDA 8B instruct: iterative mask-to-text denoising | — |
| ![fig-16](../assets/beyond-standard-llms/fig-16.webp) | ParallelBench: parallel decoding breaks token dependencies | — |
| ![fig-17](../assets/beyond-standard-llms/fig-17.webp) | Gemini Diffusion vs Gemini 2.0 Flash-Lite benchmark comparison | — |
| ![fig-18](../assets/beyond-standard-llms/fig-18.webp) | Conceptual world model: agent observes, acts, and simulates outcomes internally | — |
| ![fig-19](../assets/beyond-standard-llms/fig-19.webp) | CWM step-by-step variable-state prediction during code execution | — |
| ![fig-20](../assets/beyond-standard-llms/fig-20.webp) | CWM vs other LLMs on SWE-bench | — |
| ![fig-21](../assets/beyond-standard-llms/fig-21.webp) | LLM landscape highlighting small recursive transformers | — |
| ![fig-22](../assets/beyond-standard-llms/fig-22.webp) | ARC-AGI-1 example task and HRM leaderboard placement | — |
| ![fig-23](../assets/beyond-standard-llms/fig-23.webp) | Tiny Recursive Model (TRM) architecture | — |
| ![fig-24](../assets/beyond-standard-llms/fig-24.webp) | HRM vs TRM performance on puzzle benchmarks | — |

The article's scope within the broader LLM landscape:

![LLM landscape overview](../assets/beyond-standard-llms/fig-1.webp)

Gated DeltaNet vs full attention KV memory:

![KV cache comparison for attention hybrids](../assets/beyond-standard-llms/fig-10.webp)

LLaDA text diffusion denoising:

![LLaDA denoising animation](../assets/beyond-standard-llms/fig-15.gif)

## Entities

- [[Sebastian Raschka]] — author; Ahead of AI columnist and from-scratch LLM educator.
- [[Gated DeltaNet]] — linear-attention layer used in Qwen3-Next and Kimi Linear hybrids.
- [[Linear Attention Hybrids]] — transformer layers mixing subquadratic/linear attention with periodic full attention.
- [[Text Diffusion LLMs]] — bidirectional masked diffusion objective for parallel text generation.
- [[Code World Models]] — execution-trace-trained code LLMs that simulate program state.
- [[Small Recursive Transformers]] — tiny models (HRM, TRM) that refine answers through recursive self-updates.
- [[KV Cache]] — growing memory in full attention; contrasted with fixed recurrent state in DeltaNet.
- [[Self-Attention]] — quadratic softmax attention baseline the article compares against hybrids.

## Questions & Gaps

- Whether Kimi K3 will adopt Kimi Linear's hybrid at flagship scale remains open.
- CWM vs gpt-oss time-to-solution under different test-time-scaling strategies is not compared in the source.
- Text diffusion tool-calling and CoT compatibility are raised as concerns but not resolved.
- Deferred topics (xLSTM, Liquid FM, pure SSMs) are promised for a follow-up article.
- TRM extension to free-form text QA is noted as possible future work, not demonstrated.

## Related

- [[A Visual Guide to Attention Variants in Modern LLMs]] — companion visual survey of GQA, MLA, SWA, DSA, gated attention, and hybrid stacking that motivates DeltaNet layers.
- [[Understanding and Coding the KV Cache in LLMs from Scratch]] — Raschka tutorial on KV cache math that DeltaNet hybrids avoid growing.
- [[Papers Explained 538 - Code World Model]] — detailed CWM paper coverage in the corpus.
- [[Large Language Models]] — topic hub for standard decoder transformers Raschka treats as the default.
- [[Code Models]] — code LLM landscape; CWM adds execution-aware modeling.
- [[Reasoning Models]] — reasoning-focused training; contrasted with tiny recursive puzzle solvers.
- [[Model Compression and Efficiency]] — long-context efficiency motivation for linear attention hybrids.
- [[Inference Engineering]] — production serving context for KV-cache and throughput trade-offs.
- [[DiffusionGemma]] — Google's Jun 2026 open Gemma-scale text diffusion release; first open-weights implementation of the parallel-decoding path surveyed here.
