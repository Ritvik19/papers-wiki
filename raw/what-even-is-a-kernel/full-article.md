# What even is a kernel?

**Author**: Adam Mainz (@MainzOnX)  
**Date**: July 14, 2026  
**Canonical HTML**: `raw/what-even-is-a-kernel/full-article.md`  

## Overview
A beginner-friendly architectural walkthrough of what happens under the hood when PyTorch executes tensor operations on a GPU. The post demystifies GPU execution by defining kernels, tracing CPU launch mechanics and thread grids, demonstrating how eager mode causes intermediate tensors to round-trip through GPU global memory (HBM/GDDR), explaining kernel fusion and `torch.compile`, and walking through a practical profiling exercise using `torch.profiler`.

## Key Sections
1. **Two numbers on a GPU**: Definition of a GPU kernel as a small parallel program executed on GPU memory.
2. **Your first kernel**: CPU launch overhead (microseconds), thread mapping, 32-thread warps, counting input/output transfers.
3. **What happens between two ops**: Eager mode execution of `c = (a + b).relu()` creates 2 kernels, incurring 5 array-sized memory transfers due to intermediate `tmp` spilling to HBM/GDDR.
4. **Fusion: two ops, one kernel**: Combining add + relu into a single kernel keeps intermediates in thread-local registers, cutting transfers from 5 to 3. `torch.compile` automates this rewrite.
5. **See it for yourself**: Using `torch.profiler` to observe `vectorized_elementwise_kernel` (2 rows) collapse into `triton_poi_fused_add_relu_0` (1 row) under `torch.compile`.
6. **Summary**: Counting kernels = counting memory round-trips.

## Figures
- `images/fig-1.jpg`: Header banner for "What even is a kernel?"
- `images/fig-2.jpg`: GPU thread execution and roundtrip memory traffic diagram.
- `images/fig-3.jpg`: Kernel fusion diagram combining add and relu into a single pass.
- `images/fig-4.jpg`: Profiler trace comparison (2 eager CUDA kernels vs 1 fused Triton kernel).
