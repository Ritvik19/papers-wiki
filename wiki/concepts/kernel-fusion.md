# Kernel Fusion

**Type**: concept  
**Tags**: #concept

## Overview

Kernel fusion is a compiler optimization technique that combines multiple adjacent operations into a single executable [[GPU Kernel]], avoiding the need to write intermediate tensor arrays out to high-latency global device memory (HBM/GDDR) and read them back in for downstream operations.

## Mechanism and Benefits

- **Eliminating Round-Trip Memory Traffic**: In eager execution, chaining $N$ operations requires writing $N-1$ intermediate tensors to GPU memory and re-reading them. For example, `(a + b).relu()` executed eagerly requires 5 array-sized memory transfers (read `a`, read `b`, write `tmp`, read `tmp`, write `c`). A fused kernel maintains intermediate values directly in fast on-chip registers or scratchpad memory, completing the computation in 3 array-sized transfers.
- **Overcoming Memory-Bound Ceilings**: Because elementwise and normalization operations have low [[Arithmetic Intensity]] and are heavily memory-bound, cutting global memory traffic directly reduces kernel runtime proportionally.
- **Reducing Launch Overhead**: Fusing operations collapses multiple CPU-to-GPU launch dispatches into a single launch call, reducing host overhead.
- **Automated vs Manual Fusion**: While frameworks like PyTorch 2.x provide automated fusion via [[Torch Compile]] (using TorchInductor and Triton backends), complex operator blocks (e.g., FlashAttention, custom fused MLP layers) are frequently handwritten in Triton or CUDA to maximize register and shared memory utilization.

## Appearances

- [[What Even Is a Kernel?]] — walks through step-by-step memory transfer counting for eager vs fused `(a + b).relu()` kernels.
- [[Two Speeds of a GPU]] — explains why fusing memory-bound elementwise operations yields major wall-clock speedups.
- [[Profiling in PyTorch (Part 1): A Beginner's Guide to torch.profiler]] — examines fusion behavior under Inductor dispatcher rewrites.

## Related

- [[GPU Kernel]]
- [[Torch Compile]]
- [[Arithmetic Intensity]]
- [[Roofline Model]]
- [[GPU Inference Hardware]]
