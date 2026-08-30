# Torch Compile

**Type**: concept  
**Tags**: #concept

## Overview

`torch.compile` is PyTorch's native JIT (just-in-time) graph compiler introduced in PyTorch 2.0. It captures Python tensor computation graphs using TorchDynamo, traces forward and backward graph operations using AOTAutograd, and generates highly optimized, fused GPU code using the TorchInductor backend (often compiling to Triton or C++/CUDA).

## Architecture and Execution

1. **Graph Capture (TorchDynamo)**: Evaluates Python bytecode at runtime, intercepts frame evaluation, and extracts straight-line tensor operation graphs while safely guarding dynamic Python conditions.
2. **AOT (Ahead-of-Time) Autograd**: Traces through PyTorch's dispatcher to capture joint forward-backward computational graphs and functionalized operator representations.
3. **Backend Code Generation (TorchInductor)**: Generates optimized kernel code, automatically performing [[Kernel Fusion]] across elementwise, reduction, and memory-bandwidth-bound operators using OpenAI Triton on GPUs.
4. **Warm-up Requirement**: The first execution of a compiled model or function triggers JIT tracing and kernel code generation, resulting in significant one-time latency. Benchmarking and profiling must discard the initial warm-up call.

## Appearances

- [[What Even Is a Kernel?]] — provides a hands-on profiling example showing eager `add` and `relu` CUDA kernels fusing into a single Triton kernel `triton_poi_fused_add_relu_0`.
- [[Profiling in PyTorch (Part 1): A Beginner's Guide to torch.profiler]] — profiles compilation overhead and dispatcher-level fusions (`aten::addmm`).
- [[Unsloth Origins and Mission]] — discusses compatibility and contrast between custom handwritten kernels and PyTorch 2.x compile graphs.

## Related

- [[GPU Kernel]]
- [[Kernel Fusion]]
- [[PyTorch]]
- [[Roofline Model]]
- [[Arithmetic Intensity]]
