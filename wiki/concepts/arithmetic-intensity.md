# Arithmetic Intensity

**Type**: concept  
**Tags**: #concept

## Overview

Arithmetic intensity (also known as operational intensity or compute-to-memory ratio) measures the ratio of total arithmetic operations (FLOPs) performed by an algorithm or [[GPU Kernel]] to the total amount of data moved across the memory bus (in bytes):

$$\text{Arithmetic Intensity} = \frac{\text{Total FLOPs}}{\text{Total Bytes Transferred}}$$

It is the primary determinant of whether a workload is memory-bound or compute-bound on modern accelerator architectures under the [[Roofline Model]].

## Regimes and Scaling

| Operation Category | Arithmetic Complexity | Memory Complexity | Arithmetic Intensity | Typical Regime |
|---|---|---|---|---|
| **Vector Add / Elementwise** ($N$ elements) | $N$ FLOPs | $3N \times \text{sizeof(dtype)}$ bytes | Constant ($O(1)$) &approx; 0.17 FLOPs/byte (BF16) | Deeply Memory-Bound |
| **Reduction / LayerNorm / Softmax** | $O(N)$ FLOPs | $O(N)$ bytes | Constant ($O(1)$) | Memory-Bound |
| **Matrix Multiplication** ($N \times N$ matrices) | $2N^3$ FLOPs | $6N^2 \times \text{sizeof(dtype)}$ bytes | Scales with size: $O(N) \approx \frac{N}{3}$ FLOPs/byte (BF16) | Compute-Bound for large $N$ |
| **Attention (Standard)** ($S$ sequence length) | $O(S^2 d)$ FLOPs | $O(S^2)$ intermediate bytes | $O(d)$ | Memory-Bound without tiling |

## Hardware Balance Comparison

A GPU's hardware balance (the "ridge point") is defined as:

$$\text{Ridge Point} = \frac{\text{Peak Compute Throughput (FLOP/s)}}{\text{Peak Memory Bandwidth (Bytes/s)}}$$

- **NVIDIA H100 SXM5 (BF16)**: $\frac{989\text{ TFLOPS}}{3.35\text{ TB/s}} \approx 295\text{ FLOPs/byte} \approx 300\text{ FLOPs/byte}$.
- **NVIDIA RTX 4090 (BF16)**: $\frac{165\text{ TFLOPS}}{1.0\text{ TB/s}} = 165\text{ FLOPs/byte}$.

If a kernel's arithmetic intensity is less than the machine's ridge point, it is **memory-bound**; if greater, it is **compute-bound**.

## Appearances

- [[Two Speeds of a GPU]] — foundational explainer deriving intensity formulas for vector adds (0.17 FLOPs/byte) and matrix multiplications ($N/3$ FLOPs/byte).
- [[Inference Engineering]] — analyzes arithmetic intensity in LLM decode (memory-bound) vs prefill (compute-bound).

## Related

- [[Roofline Model]]
- [[GPU Kernel]]
- [[Kernel Fusion]]
- [[GPU Inference Hardware]]
- [[Torch Compile]]
