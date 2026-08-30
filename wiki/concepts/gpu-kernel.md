# GPU Kernel

**Type**: concept  
**Tags**: #concept

## Overview

A GPU kernel is a specialized function or program designed to execute in parallel across thousands of hardware threads on a graphics processing unit (GPU). In machine learning frameworks like PyTorch, high-level tensor operations map to one or more kernel launches dispatched by the host CPU to device memory.

## Execution Model and Mechanics

1. **Host Launch**: The host CPU dispatches a kernel via a driver launch command (taking a few microseconds of launch overhead). Launches are asynchronous by default, meaning CPU execution continues while the GPU queues and runs the kernel.
2. **Thread Hierarchy & Warps**: The GPU schedules threads across streaming multiprocessors (SMs) organized in 32-thread units called warps on NVIDIA architectures. Each thread executes the kernel instructions over assigned elements of the input tensor.
3. **Memory Access**: Inputs must be read from global device memory (HBM on datacenter GPUs like A100/H100 or GDDR on consumer GPUs like RTX 4090) into on-chip registers/SRAM, and results must be written back out to global memory upon completion.
4. **Eager Mode vs Compilation**: In PyTorch eager mode, each tensor operation executes as an isolated kernel launch that reads inputs from and writes intermediate results to global memory. Compilers like `torch.compile` fuse multiple operations into unified kernels to minimize round-trip global memory traffic.

## Appearances

- [[What Even Is a Kernel?]] — introduces GPU kernels from first principles, comparing single-op launches to chained ops in PyTorch.
- [[Two Speeds of a GPU]] — discusses kernel execution time under compute and memory bandwidth constraints.
- [[Profiling in PyTorch (Part 1): A Beginner's Guide to torch.profiler]] — profiles CUDA kernel dispatch traces, overheads, and execution times.

## Related

- [[Kernel Fusion]]
- [[Torch Compile]]
- [[GPU Inference Hardware]]
- [[Arithmetic Intensity]]
- [[Roofline Model]]
