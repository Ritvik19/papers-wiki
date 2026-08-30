# GPipe

**Type**: tool  
**Tags**: #entity

## Overview

GPipe is an open-source distributed model-parallelism library developed by Google. It facilitates the training of giant neural networks by partitioning layers across different hardware accelerators and dividing a training mini-batch into smaller, synchronous microbatches to overlap computation and minimize idle pipeline bubble time.

## Appearances

- [[How to Train Really Large Models on Many GPUs?]] — Detailed as Google's pioneering framework that introduced microbatch-based synchronous **Pipeline Parallelism** and mathematically analyzed pipeline bubble overhead.

## Notes

GPipe is historically significant as one of the first formal Pipeline Parallelism frameworks. Although it guarantees strict mathematical equivalence to standard gradient descent by accumulating gradients across all microbatches before performing a synchronized parameter update, this synchronization step requires storing activation tensors for every in-flight microbatch. Consequently, GPipe is heavily dependent on **[[Activation Recomputation]]** to curb memory usage, which exchanges extra computation (re-evaluating the forward pass of a layer during backward propagation) for lower memory consumption.

### Publication Details

- **Paper**: "GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism" (Huang et al., 2019)
- **Published at**: NeurIPS 2019
- **Organization**: Google Brain
- **Key result**: Trained AmoebaNet-B (557M parameters) and Transformer (6B parameters) — previously intractable models

### Core Algorithm

Given a mini-batch of size $N$ and pipeline depth $d$:
1. Split the batch into $m$ microbatches of size $N/m$.
2. Each microbatch is fed forward sequentially through all $d$ stages.
3. Gradients for all $m$ microbatches are accumulated at each stage.
4. After all microbatches complete backward, a single global parameter update is performed.

This is mathematically equivalent to training with batch size $N$ on a single device, making GPipe a **synchronous** system (unlike PipeDream which is asynchronous).

### Bubble Fraction Analysis

With $m$ microbatches and $d$ pipeline stages (each taking 1 unit forward + 1 unit backward):
$$\text{Idle time} = (d-1) \times 2 \text{ units} \quad \text{per batch}$$
$$\text{Total time} = 2md + 2(d-1) \text{ units}$$
$$\text{Bubble Fraction} = \frac{d-1}{m + d - 1}$$

For $m=32$ microbatches and $d=4$ stages: bubble fraction $\approx 8.1\%$ — negligible overhead.

### Historical Significance

GPipe demonstrated that pipeline parallelism could be implemented cleanly on top of standard deep learning frameworks, paving the way for PipeDream, Megatron-LM's PTD-P, and modern FSDP/ZeRO-3 based systems. Its microbatch concept became a fundamental building block in all subsequent pipeline systems.

## Related

- [[Pipeline Parallelism]]
- [[Activation Recomputation]]
- [[Model Parallelism]]
- [[Megatron-LM]]
- [[How to Train Really Large Models on Many GPUs?]]
