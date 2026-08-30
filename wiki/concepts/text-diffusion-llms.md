# Text Diffusion LLMs

**Tags**: #concept

Text diffusion LLMs generate text through iterative denoising of masked token sequences rather than strict left-to-right next-token prediction. Architecturally they are usually decoder-style transformers **without** a causal mask (bidirectional attention), trained with a generative diffusion/masking objective instead of autoregressive cross-entropy.

## Overview

Inspired by image diffusion (DDPM, Stable Diffusion) and early *Diffusion-LM* work, modern text diffusion models (e.g., LLaDA, Google's Gemini Diffusion) corrupt text by randomly replacing tokens with a mask symbol, then learn to predict missing tokens across multiple refinement steps. All positions can be updated in parallel each step, so total inference may require far fewer serial passes than generating thousands of tokens autoregressively—though each step still runs a full forward pass.

Raschka highlights trade-offs: parallel sampling can break token dependencies (ParallelBench "New City" example), quality can collapse under aggressive parallelism, models cannot stream answers token-by-token, and tool-calling chains are awkward without sequential generation. Gemini Diffusion is positioned as faster than prior fast autoregressive models with comparable benchmark scores to Gemini 2.0 Flash-Lite, but large-scale production feedback was still pending at article time.

[[DiffusionGemma]] (Jun 2026) is Google's first **open-weights** text diffusion release at Gemma scale: 26B MoE / 3.8B active on the Gemma 4 backbone, Apache 2.0, with [[Uniform State Diffusion]] and [[Block Autoregressive Diffusion]] over 256-token canvases. Google cites up to 4× faster local GPU decode (1000+ tok/s on H100) by shifting the bottleneck from memory bandwidth to compute, but explicitly positions output quality below standard autoregressive Gemma 4—validating the speed-first experimental niche Raschka described while retaining quality trade-offs.

## Appearances

- [[Beyond Standard LLMs]] — overview of LLaDA denoising, ParallelBench limitations, and Gemini Diffusion benchmarks.
- [[DiffusionGemma]] — open Gemma 4-based release with measured tok/s claims, vLLM serving, and Sudoku fine-tuning demo.

## Notes

- Diffusion LLMs share structural similarity with BERT-style masked modeling extended into iterative generative refinement.
- Raschka sees them as interesting for smaller on-device models or as alternatives to distilled autoregressive LMs, not yet as SOTA replacements.
- DiffusionGemma extends the category with a production-oriented serving stack (vLLM, MLX, NVFP4) while remaining experimental on quality.

## Related

- [[Large Language Models]]
- [[Beyond Standard LLMs]]
- [[Model Compression and Efficiency]]
