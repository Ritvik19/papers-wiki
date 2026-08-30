# NVFP4

**Type**: concept  
**Tags**: #concept

## Overview

**NVFP4** is NVIDIA’s 4-bit floating-point format for efficient training and inference on Blackwell-generation GPUs. Open model releases often ship an NVFP4 checkpoint alongside BF16/FP8 to cut weight memory while targeting native Blackwell kernels.

## Appearances

- [[Inkling]] — `thinkingmachines/Inkling-NVFP4` (~600 GB VRAM vs ~2 TB BF16) for Blackwell inference.
- [[Papers Explained - Nemotron 3 Super]] — Nemotron 3 Super pre-trained in NVFP4.
- [[Introducing NVIDIA Nemotron 3 Nano Omni: Long-Context Multimodal Intelligence for Documents, Audio and Video Agents]] — BF16 / FP8 / NVFP4 checkpoints.

## Notes

NVFP4 is a packing/precision choice for NVIDIA hardware, not a training algorithm. Serving still requires multi-GPU or multi-node setups for ~1T-parameter MoEs.

## Related

- [[NVIDIA]]
- [[Inkling]]
- [[Model Compression and Efficiency]]
- [[GPU Inference Hardware]]
- [[Inference Engineering]]
