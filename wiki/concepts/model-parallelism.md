# Model Parallelism

**Type**: concept  
**Tags**: #concept

## Overview

Model Parallelism (MP) is a distributed training paradigm designed for models whose parameters are too large to fit in the memory of a single accelerator node. Instead of replicating the entire model across all workers (as in Data Parallelism), Model Parallelism partitions the model parameters and computation vertically or horizontally across multiple accelerators. Each worker hosts only a fraction of the model parameters and processes its assigned portion of the network.

## Appearances

- [[How to Train Really Large Models on Many GPUs?]] — *How to Train Really Large Models on Many GPUs?* (Sep 25, 2021): Introduces model-parallel partitioning, details sequential bottlenecks (bubbles), and provides context for the transition to advanced pipeline and tensor parallelism.

## Notes

*   **The Memory Wall: Why Model Parallelism is Necessary**:
    During [[Mixed Precision Training]] with Adam optimizer, a model with $\Psi$ parameters requires approximately:
    - $2\Psi$ bytes for FP16 parameters
    - $2\Psi$ bytes for FP16 gradients
    - $12\Psi$ bytes for FP32 optimizer states (master copy + momentum + variance)
    - Total: $\approx 16\Psi$ bytes of **model state** memory alone, plus activation memory.

    For a 100B parameter model, model state alone requires $\approx 1.6$ TB — roughly 20× the capacity of an 80 GB A100 GPU. Model Parallelism is therefore not optional but necessary for frontier-scale training.

*   **Vertical vs. Horizontal Partitioning**:
    Model Parallelism is divided into two primary categories based on how the partitioning is executed:
    -   **Vertical Model Parallelism (Pipeline Parallelism)**: Splitting the network vertically by assigning consecutive layers to different devices. For example, in a 4-GPU setup, GPU 0 hosts layers 1–8, GPU 1 hosts layers 9–16, and so on.
    -   **Horizontal Model Parallelism (Tensor Parallelism)**: Sharding the internal matrix multiplications of a single layer across multiple devices, so every device computes a fraction of every layer simultaneously.

*   **The Sequential Dependency Bottleneck ("Bubbles")**:
    A naive vertical model parallelism setup suffers from severe under-utilization due to sequential dependency. Because layer $l$ requires the activation output from layer $l-1$, workers can only execute in strict chronological order:
    1.  GPU 0 processes a batch forward and sends activations to GPU 1.
    2.  GPU 1 waits, then processes and sends to GPU 2.
    3.  Once the forward pass reaches the final GPU, the backward pass begins in reverse.

    This strict sequential execution results in massive "idle bubbles" where only one GPU is computing at any given moment, while the other $d-1$ GPUs sit completely idle, yielding an overall device utilization of only $1/d$.
    
    See [[How to Train Really Large Models on Many GPUs?]] fig-2 for a diagram of naive model parallelism idle bubbles.

*   **Memory Partitioning**:
    The key benefit of vertical model parallelism is that it partitions memory proportionally. For $d$ stages with balanced layer distribution:
    $$\text{Memory per device} = \frac{\text{Total model state}}{d} + \text{Activation memory for one stage}$$
    This is a hard partition (unlike ZeRO's sharding, which requires communication to re-assemble), so each stage's parameters are always resident on its device.

*   **Transition to Advanced Systems**:
    To overcome the sequential bottleneck of naive model parallelism, modern systems combine it with data parallelism:
    -   **Pipeline Parallelism (PP)**: Overlaps vertical partitions by splitting the input batch into microbatches and pipelining their execution, reducing idle bubble fraction from $\frac{d-1}{1}$ toward $\frac{d-1}{m+d-1}$ as microbatch count $m$ grows.
    -   **Tensor Parallelism (TP)**: Shards the individual GEMM (General Matrix Multiply) operations horizontally to execute intra-layer computations in parallel across all cores — eliminating sequential dependency entirely within each layer.
    -   **3D Parallelism (DP + PP + TP)**: Production systems combine all three axes. For example, Megatron-Turing NLG (530B parameters) used TP=8, PP=35, DP=12 across 2,240 NVIDIA A100 GPUs.

## Related

- [[Data Parallelism]]
- [[Pipeline Parallelism]]
- [[Tensor Parallelism]]
- [[ZeRO]]
- [[Mixed Precision Training]]
- [[How to Train Really Large Models on Many GPUs?]]
