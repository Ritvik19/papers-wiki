# Tensor Parallelism

**Type**: concept  
**Tags**: #concept

## Overview

Tensor Parallelism (TP) is a horizontal model-parallel training paradigm that shards individual tensor operations and matrix multiplications (GEMMs) across multiple accelerators. Unlike vertical pipeline parallelism which partitions layers sequentially across devices, Tensor Parallelism shards the parameter matrices *within* a single layer (e.g. attention or MLP blocks), allowing all devices to compute fractions of the same layer simultaneously.

## Appearances

- [[How to Train Really Large Models on Many GPUs?]] — *How to Train Really Large Models on Many GPUs?* (Sep 25, 2021): Synthesizes Megatron-LM's horizontal sharding equations for transformer layers, communication boundaries, and interleaved multi-chunk schedules.

## Notes

*   **Megatron-LM Horizontal Transformer Sharding**:
    Developed by NVIDIA (Shoeybi et al. 2020), **Megatron-LM** provides an elegant formulation to split Transformer MLP and Self-Attention layers across parallel devices while minimizing expensive cross-device communication boundaries.
    
    ### 1. Multi-Layer Perceptron (MLP) Sharding
    A transformer MLP layer contains two dense linear GEMM operations. The first GEMM's weight matrix $A$ is sharded **column-wise** across devices, while the second GEMM's weight matrix $B$ is sharded **row-wise**:
    
    $$\begin{aligned}
    \text{Column Split (Layer 1):} \quad A &= [A_1, A_2] \\
    [Y_1, Y_2] &= [\text{GeLU}(X A_1), \text{GeLU}(X A_2)] \\
    \text{Row Split (Layer 2):} \quad B &= \begin{bmatrix} B_1 \\ B_2 \end{bmatrix} \\
    Z &= Y_1 B_1 + Y_2 B_2
    \end{aligned}$$
    
    Because the first layer is split column-wise, each GPU can compute its non-linear activation independently without communicating. The second layer is split row-wise, which naturally sums the parallel outputs back together. This sum only requires a single collective `AllReduce` operation at the very end of the FFN block to synchronize the outputs, completely avoiding intermediate synchronization barriers.
    
    ### 2. Multi-Head Self-Attention Sharding
    Megatron-LM parallelizes multi-head attention by grouping the Query, Key, and Value ($Q, K, V$) projections and sharding them **column-wise** (with attention heads partitioned across GPUs). The attention matrix multiplication is computed locally, and the final output projection matrix ($W_O$) is sharded **row-wise**. An `AllReduce` sum synchronizes the head outputs, preserving parallel execution.
    
    See [[How to Train Really Large Models on Many GPUs?]] fig-8 for the MLP and Attention tensor sharding diagrams.

*   **Communication Volume per Transformer Layer**:
    With $t$ tensor-parallel devices per node, each transformer layer requires exactly **2 forward + 2 backward `AllReduce`** operations (one each for the MLP and Attention blocks). The communication volume per transformer block is:
    $$V_{\text{TP}} = 4 \times \frac{t-1}{t} \times B \times s \times h$$
    where $B$ is the batch size, $s$ is the sequence length, and $h$ is the hidden dimension. This is independent of model parameter count — only activations are communicated, not weights. This property makes Tensor Parallelism well-suited for **intra-node** parallelism over high-bandwidth NVLink interconnects.

*   **NVLink & NVSwitch Hardware Alignment**:
    The `AllReduce` collectives required by Tensor Parallelism are latency-sensitive (many small synchronized operations). This makes TP only practical on devices connected by high-bandwidth, low-latency links:
    -   **NVLink 3.0** (A100): 600 GB/s bidirectional bandwidth per GPU
    -   **NVSwitch** (H100 SXM): 900 GB/s bidirectional per GPU, all-to-all non-blocking fabric
    
    Tensor Parallelism degree $t$ is therefore typically bounded by the number of GPUs on a single node (usually 8), beyond which inter-node communication via InfiniBand becomes too slow for inline `AllReduce`.

*   **Interleaved 1F1B (PTD-P Schedule)**:
    Narayanan et al. (2021) combined Tensor Parallelism with Pipeline and Data Parallelism into a unified framework named **PTD-P**. To further reduce the vertical pipeline bubble, they introduced an **interleaved 1F1B schedule**.
    Instead of assigning a single contiguous set of layers to a device (e.g. GPU 0 gets layers 1–4), each device is assigned multiple smaller non-contiguous "model chunks" (e.g. GPU 0 gets layers 1, 2, 9, 10; GPU 1 gets layers 3, 4, 11, 12). If there are $v$ model chunks per worker, the sequential pipeline bubble time is reduced by a factor of $v$ compared to a standard GPipe schedule, dramatically boosting throughput at extreme scale.
    
    See [[How to Train Really Large Models on Many GPUs?]] fig-9 for the PTD-P interleaved pipeline schedule.

*   **Optimal 3D Parallelism Configuration**:
    For a cluster of $N_{\text{total}}$ GPUs, the optimal combination of DP, PP, and TP degrees satisfies:
    $$N_{\text{total}} = N_{\text{DP}} \times N_{\text{PP}} \times N_{\text{TP}}$$
    
    General heuristics from Megatron-LM:
    - **$N_{\text{TP}}$** ≤ number of GPUs per node (NVLink-connected). Usually 4 or 8.
    - **$N_{\text{PP}}$** ≥ 1 when model does not fit in a single TP group; prefer $v > 1$ interleaving for lower bubble cost.
    - **$N_{\text{DP}}$** fills the remaining degree; governed by global batch size target.

## Related

- [[Pipeline Parallelism]]
- [[Data Parallelism]]
- [[Megatron-LM]]
- [[Model Parallelism]]
- [[How to Train Really Large Models on Many GPUs?]]
