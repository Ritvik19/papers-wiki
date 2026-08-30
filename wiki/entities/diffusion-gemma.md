# DiffusionGemma

**Type**: concept  
**Tags**: #entity

## Overview

**DiffusionGemma** (`google/diffusiongemma-26B-A4B-it`) is Google's June 2026 experimental open-weight text model: a 26B-total / 3.8B-active MoE built on the [[Gemma 4]] backbone with a diffusion head for parallel 256-token canvas generation. Released under Apache 2.0 on Hugging Face.

## Appearances

- [[DiffusionGemma]] — launch announcement and developer guide covering architecture, benchmarks, serving, and Sudoku fine-tuning.

## Notes

- Prioritizes inference speed over output quality; Google recommends standard autoregressive Gemma 4 for production.
- Uses [[Uniform State Diffusion]] and [[Block Autoregressive Diffusion]]; integrated into vLLM, MLX, Transformers, and SGLang.
- Cited throughput: 1000+ tok/s (H100), 700+ tok/s (RTX 5090) at low batch sizes.

## Related

- [[Gemma 4]] — parent model family and shared 26B-A4B architecture.
- [[Google DeepMind]] — research lineage.
- [[Text Diffusion LLMs]] — architectural category.
- [[Uniform State Diffusion]]
- [[Block Autoregressive Diffusion]]
