# Linear Attention Hybrids

**Tags**: #concept

Linear attention hybrids are decoder-style transformer LLMs that replace most softmax attention layers with subquadratic or linear-time attention variants—while retaining a minority of full-attention layers for global context. They target long-context efficiency: lower FLOPs, smaller or constant memory versus growing [[KV Cache]], and higher decode throughput.

## Overview

Classic linear attention (e.g., kernel-feature approximations à la *Transformers are RNNs*, 2020) avoided explicit n×n attention matrices but historically degraded accuracy and never reached open SOTA. A 2025 revival paired improved linear mechanisms—especially [[Gated DeltaNet]]—with hybrid stacking: e.g., Qwen3-Next and Kimi Linear use three linear layers per one full-attention layer (3:1). Related models include MiniMax-M1 (lightning attention), DeepSeek V3.2 (sparse/subquadratic attention), and Kimi Linear (48B, Oct 2025). MiniMax-M2 notably reverted to regular attention, citing reasoning and agentic quality issues with linear attention in production.

Reported benefits on Kimi Linear include ~75% KV-cache reduction and up to 6× decoding throughput versus full attention, with benchmark competitiveness when hybrids are tuned carefully.

## Appearances

- [[A Visual Guide to Attention Variants in Modern LLMs]] — hybrid 3:1 pattern across Qwen3-Next/3.5, Kimi Linear, Ling 2.5, and Nemotron Mamba-2 stacks; inference-stack maturity caveats.
- [[Beyond Standard LLMs]] — survey of 2025 linear-attention timeline, Qwen3-Next vs Kimi Linear, and efficiency/accuracy trade-offs.

## Notes

- Raschka classifies Qwen3-Next and Kimi Linear as "transformers with SSM/linear components" rather than pure SSM-first hybrids.
- Future hybrids are expected to focus on long-context stability and closing the accuracy gap to full-attention SOTA.

## Related

- [[Gated DeltaNet]]
- [[KV Cache]]
- [[Model Compression and Efficiency]]
- [[Beyond Standard LLMs]]
