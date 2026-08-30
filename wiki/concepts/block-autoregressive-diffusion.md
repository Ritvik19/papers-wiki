# Block Autoregressive Diffusion

**Tags**: #concept

## Overview

**Block Autoregressive Diffusion** extends parallel text diffusion to sequences longer than a single canvas. [[DiffusionGemma]] denoises 256-token blocks in parallel; once a block converges, causal prefill commits it to the [[KV Cache]], then a fresh 256-token canvas is initialized conditioned on prior committed history. Inference alternates **causal prefill** (prompt ingestion and block append) with **bidirectional denoising** (parallel canvas refinement).

## Appearances

- [[DiffusionGemma]] — 256-token canvas length; vLLM `--diffusion-config '{"canvas_length": 256}'`.

## Notes

- Combines diffusion parallelism within blocks with autoregressive sequential stability across blocks for long-form text.
- Reuses the same Gemma 4 26B A4B backbone—serving frameworks add a denoising step rather than a new model architecture.
- Global context during denoising: canvas tokens attend to each other and to the KV cache from committed prefix blocks.

## Related

- [[Uniform State Diffusion]]
- [[Text Diffusion LLMs]]
- [[KV Cache]]
- [[DiffusionGemma]]
