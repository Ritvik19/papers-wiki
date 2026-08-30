# Gradient Accumulation

**Type**: concept  
**Tags**: #concept

## Overview

Training technique that accumulates gradients over multiple micro-batches before an optimizer step, simulating larger batch sizes on limited VRAM. Unsloth fixed incorrect loss scaling in standard HF gradient accumulation that caused higher loss vs true full-batch training.

## Appearances

- [[Unsloth Training Efficiency and Kernels]]

## Related

- [[Sample Packing]]
- [[Unsloth]]
