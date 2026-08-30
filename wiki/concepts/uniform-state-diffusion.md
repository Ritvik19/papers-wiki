# Uniform State Diffusion

**Tags**: #concept

## Overview

**Uniform State Diffusion** is the text-generation paradigm used by [[DiffusionGemma]]: instead of predicting tokens left-to-right, the model starts with a canvas of random placeholder tokens and iteratively refines all positions in parallel across multiple denoising passes. Highly confident tokens lock in and provide context for resolving adjacent positions; low-confidence tokens can be re-noised and replaced, enabling real-time self-correction within a block.

## Appearances

- [[DiffusionGemma]] — primary open-weight implementation on the Gemma 4 26B-A4B backbone with 256-token canvases.

## Notes

- Bidirectional attention during denoising lets every canvas position attend to every other—unlike autoregressive models that cannot revise earlier tokens.
- Demonstrated advantage on globally constrained tasks (Sudoku): base DiffusionGemma ~0% → 80% after SFT with fewer denoising steps.
- Analogous to image diffusion: start from noise/static, iteratively refine toward coherent output.

## Related

- [[Text Diffusion LLMs]]
- [[Block Autoregressive Diffusion]]
- [[DiffusionGemma]]
- [[Beyond Standard LLMs]]
