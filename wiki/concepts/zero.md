# ZeRO

**Type**: concept  
**Tags**: #concept

## Overview

ZeRO (Zero Redundancy Optimizer) is a memory optimization paradigm designed to eliminate memory redundancies in data-parallel training while preserving computational efficiency. Formulated by Microsoft (Rajbhandari et al. 2019), ZeRO partitions model states (optimizer states, gradients, and parameters) across standard data-parallel processes instead of duplicating them. This allows training models with hundreds of billions of parameters without resorting to complex model-parallel refactoring.

## Appearances

- [[How to Train Really Large Models on Many GPUs?]] — *How to Train Really Large Models on Many GPUs?* (Sep 25, 2021): Synthesizes ZeRO memory reduction states, dynamic communication schedules, and ZeRO-DP/ZeRO-R stages.

## Notes

*   **Model State Memory Bottlenecks**:
    Weng highlights that during standard mixed-precision training (e.g. using Adam), the majority of GPU memory is consumed by **Model States** rather than the model parameters themselves:
    1.  **Parameters**: An $N$-parameter model consumes $2N$ bytes in FP16.
    2.  **Gradients**: Consumes $2N$ bytes in FP16.
    3.  **Optimizer States**: Under Adam, the optimizer must store:
        -   An FP32 master copy of weights ($4N$ bytes).
        -   FP32 momentum states ($4N$ bytes).
        -   FP32 variance states ($4N$ bytes).
    Total Model State Memory for Adam = $16N$ bytes. For a 10-billion parameter model, this requires $160$ GB of memory—far exceeding the capacity of standard GPUs (e.g., 40GB or 80GB), even though the raw weights are only 20 GB.
*   **ZeRO-DP (Data Parallelism) Stages**:
    ZeRO-DP eliminates memory redundancies by partitioning these states across $N_{DP}$ data-parallel processes:
    
    ```mermaid
    graph TD
        subgraph ZeRO-1
            O[Partition Optimizer States] --> |4x Memory Saved| Z1[ZeRO-1]
        end
        subgraph ZeRO-2
            G[Partition Gradients] --> |8x Memory Saved| Z2[ZeRO-2]
        end
        subgraph ZeRO-3
            P[Partition Parameters] --> |Linear Scaling| Z3[ZeRO-3]
        end
        Z1 --> Z2
        Z2 --> Z3
    ```
    
    -   **ZeRO-Stage 1**: Partitions the FP32 Adam optimizer states across the DP workers. Each worker updates only $1/N_{DP}$ of the optimizer states and master weights, reducing memory by $4\times$ with zero communication overhead.
    -   **ZeRO-Stage 2**: Partitions both optimizer states and gradients. Each worker only stores the gradients needed to update its partitioned optimizer slice. Gradients are reduced and sharded on the fly during the backward pass via `ReduceScatter`, reducing memory by $8\times$ with no additional communication volume.
    -   **ZeRO-Stage 3**: Partitions optimizer states, gradients, and model parameters. During the forward and backward passes, workers perform a collective `AllGather` communication to fetch the required parameters on the fly, immediately discarding them after computation. This scales the memory footprint linearly with the number of devices.
*   **ZeRO-R (Residual Memory Optimization)**:
    Beyond model states, ZeRO-R targets **Residual Memory** (activations, temporary buffers, and memory fragmentation):
    -   **Partitioned Activation Recomputation (PaR)**: Shards activation checkpoints across DP processes, gathering them on the fly via `AllGather` when performing local recomputation.
    -   **Constant Size Buffers**: Sets fixed-size memory buffers for collective communication, avoiding memory spikes during massive operations.
    -   **Defragmentation**: Actively manages and defragments active GPU memory allocations on the fly to prevent out-of-memory (OOM) errors caused by fragmented memory blocks.
*   **CPU/NVMe Offloading (ZeRO-Offload / ZeRO-Infinity)**:
    ZeRO can offload partitioned optimizer states, gradients, and parameters to host CPU memory or NVMe SSDs. This leverages high host RAM capacity (e.g., 512GB or 2TB) to train trillion-parameter models on a single node, using asynchronous PCIe prefetching to hide communication latency.

## Related

- [[Data Parallelism]]
- [[DeepSpeed]]
- [[Activation Recomputation]]
- [[Mixed Precision Training]]
- [[How to Train Really Large Models on Many GPUs?]]
