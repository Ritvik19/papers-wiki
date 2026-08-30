# Roofline Model

**Type**: concept  
**Tags**: #concept

## Overview

The Roofline Model is an intuitive visual performance model developed by Samuel Williams, Andrew Waterman, and David Patterson (2009) that provides realistic upper bounds on the attainable floating-point performance of a computer system as a function of operational [[Arithmetic Intensity]].

## Mathematical Formulation

Attainable performance (in FLOP/s) is bounded by the minimum of two hardware ceilings:

$$\text{Attainable Performance} = \min\left(\text{Peak Compute Throughput},\; \text{Peak Memory Bandwidth} \times \text{Arithmetic Intensity}\right)$$

In log-log scale:
1. **Memory Roof (Slanted Region)**: For kernels with low arithmetic intensity ($I < I^*$), performance scales linearly with arithmetic intensity: $\text{Performance} = \text{Bandwidth} \times I$. In this region, arithmetic execution units are underutilized, and wall-clock execution time is dominated by memory traffic (the kernel is **memory-bound**).
2. **Compute Roof (Flat Region)**: For kernels with high arithmetic intensity ($I \ge I^*$), performance is capped by the maximum arithmetic capacity of the execution units ($\text{Peak Compute}$). Further increases in arithmetic intensity cannot increase throughput (the kernel is **compute-bound**).
3. **Ridge Point ($I^*$)**: The intersection point where the memory ceiling meets the compute ceiling:
   $$I^* = \frac{\text{Peak Compute (FLOP/s)}}{\text{Peak Memory Bandwidth (Bytes/s)}}$$
   The ridge point is an inherent hardware characteristic (e.g., ~300 FLOPs/byte on NVIDIA H100 SXM5, ~165 FLOPs/byte on NVIDIA RTX 4090).

## Optimization Strategies by Regime

- **Memory-Bound Workloads** ($I < I^*$):
  - [[Kernel Fusion]]: Collapse operator chains to eliminate global memory writes and reads.
  - **Quantization / Low-Precision Formats**: Switch from FP32 (4 bytes) to FP16/BF16 (2 bytes) or FP8/FP4, cutting memory traffic by $2\times$ or $4\times$.
  - **Memory Tiling & Caching**: Cache reused data in fast on-chip SRAM/shared memory (e.g., FlashAttention).
- **Compute-Bound Workloads** ($I \ge I^*$):
  - **Tensor Cores**: Leverage specialized matrix multiplication units (e.g., NVIDIA Tensor Cores).
  - **Algorithmic Optimizations**: Reduce unnecessary mathematical operations or restructure matrix dimensions.

## Appearances

- [[Two Speeds of a GPU]] — presents a complete walkthrough of the roofline model comparing vector add and matmul regimes on H100 and RTX 4090.
- [[Inference Engineering]] — applies roofline analysis to LLM generation (decode vs prefill).

## Related

- [[Arithmetic Intensity]]
- [[GPU Kernel]]
- [[Kernel Fusion]]
- [[GPU Inference Hardware]]
- [[Torch Compile]]
