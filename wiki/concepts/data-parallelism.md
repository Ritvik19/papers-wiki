# Data Parallelism

**Type**: concept  
**Tags**: #concept

## Overview

Data Parallelism (DP) is a distributed training paradigm where the model weights are duplicated across multiple worker nodes (GPUs or TPUs), while the training mini-batch is partitioned (sharded) equally among these workers. Each worker independently processes its assigned data shard through the forward and backward passes to compute gradients, which are then synchronized (aggregated) across all workers to perform a unified parameter update.

## Appearances

- [[How to Train Really Large Models on Many GPUs?]] — *How to Train Really Large Models on Many GPUs?* (Sep 25, 2021): Synthesizes standard data-parallel mechanisms, synchrony trade-offs, and gradient accumulation.

## Notes

*   **Naive Data Parallelism Limitations**: Naive DP assumes that a full copy of the model parameters, gradients, and optimizer states can comfortably fit within the memory of a single device. As models scale to billions of parameters, this assumption breaks down. Methods like **GeePS** (Cui et al. 2016) mitigate memory bounds in naive DP by temporarily offloading unused parameters back to the CPU host memory, though this introduces severe PCIe bottleneck slowdowns.
*   **Gradient Synchronization Modes**:
    To maintain statistical learning consistency, workers must synchronize their computed gradients at the end of each backward pass. Weng highlights two key approaches:
    -   **Bulk Synchronous Parallel (BSP)**: Workers halt and wait for all other devices to finish computing gradients before performing a global `AllReduce` synchronization. While BSP guarantees learning consistency and matches standard single-device mathematical updates, it introduces significant idle overhead as fast workers stall waiting for slower "straggler" workers.
    -   **Asynchronous Parallel (ASP)**: Workers update a global parameter server or local copies independently without waiting. While ASP maximizes computational throughput by eliminating synchronization barriers, it suffers from the "stale gradient" problem, where updates are applied to stale weight versions. This significantly degrades statistical efficiency and increases training time to convergence.
*   **Gradient Accumulation**:
    A compromise between synchronization frequency and batch size is **Gradient Accumulation**. Workers compute and accumulate gradients locally over $x$ iterations ($x > 1$) without synchronizing. A global `AllReduce` operation is only performed once every $x$ iterations. This decreases communication overhead and allows training with virtually unlimited effective batch sizes even on limited network bandwidth.
*   **PyTorch Distributed Data Parallel (DDP)**:
    Modern implementations, such as PyTorch DDP (Li et al. 2021), optimize communication overhead by overlap-scheduling:
    -   **Gradient Bucketing**: Instead of initiating an `AllReduce` for every individual tensor, DDP groups multiple gradients into contiguous memory "buckets" (processed in reverse order of the computation graph).
    -   **Communication-Computation Overlap**: DDP schedules the `AllReduce` collective communication of a bucket asynchronously while the worker is still computing gradients for earlier layers in the backward pass.
    
    See [[How to Train Really Large Models on Many GPUs?]] fig-1 for the DDP execution flow and bucketing pseudocode.
*   **Ring-AllReduce Communication Volume**:
    The standard all-reduce algorithm for gradient synchronization across $N$ workers is the **Ring-AllReduce** (Baidu, 2017). All $N$ GPUs are arranged in a logical ring. In two phases (Scatter-Reduce then AllGather), each GPU sends and receives gradient data exactly $(N-1)$ times. The total communication volume per GPU is:
    $$V_{\text{comm}} = 2 \cdot \frac{N-1}{N} \cdot \Psi$$
    where $\Psi$ is the total size of all model gradients (in bytes). As $N \to \infty$, this asymptotically approaches $2\Psi$ bytes per GPU, meaning Ring-AllReduce's communication cost is **bandwidth-optimal and independent of the number of workers**.
*   **Fully Sharded Data Parallel (FSDP)**:
    PyTorch **FSDP** (Zhao et al. 2023) extends standard DDP with ZeRO-style sharding. Rather than replicating all parameters on every device, FSDP shards model parameters, gradients, and optimizer states across data-parallel ranks (equivalent to ZeRO Stage 3). Parameters are gathered on demand before each layer's forward and backward pass via `AllGather`, then discarded immediately. This allows training models that far exceed the capacity of any single GPU while retaining the simple DDP programming interface.
*   **Communication vs. Computation Trade-off**:
    The fundamental limitation of data parallelism at extreme scale is the communication wall. As model size $\Psi$ (in parameters) grows, the `AllReduce` communication volume grows proportionally. For a model with $\Psi$ FP16 parameters, Ring-AllReduce costs approximately $2 \times 2\Psi$ bytes (forward and backward passes). On a 100 Gbps interconnect, synchronizing a 70B parameter model's gradients ($\approx 140$ GB) takes $\sim 11$ seconds — far exceeding the computation time on a fast GPU cluster. This is why data parallelism is always combined with [[Tensor Parallelism]] or [[Pipeline Parallelism]] in modern large-scale training setups.

## Related

- [[Model Parallelism]]
- [[Pipeline Parallelism]]
- [[Tensor Parallelism]]
- [[ZeRO]]
- [[How to Train Really Large Models on Many GPUs?]]
