# Quantization-Aware Training

**Type**: concept  
**Tags**: #concept

## Overview

Training with simulated ("fake") quantization in the forward pass so deployed INT4/FP8 weights retain accuracy. Preferred over post-training quantization when quality loss must stay below ~2% at 4-bit. Unsloth documents QAT with TorchAO/ExecuTorch and Gemma 4 QAT checkpoints.

## Appearances

- [[Unsloth Quantization-Aware Training]]
- [[Gemma 4 QAT]]

## Related

- [[Model Compression and Efficiency]]
- [[Unsloth Dynamic Quantization]]
- [[Gemma 4]]
