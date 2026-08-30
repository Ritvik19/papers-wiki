# GPU Inference Hardware

**Type**: concept  
**Tags**: #concept

## Overview

Modern AI inference relies on GPU accelerators, with NVIDIA dominating the market. Inference engineers must understand GPU compute (Tensor Cores, FLOPS), memory hierarchy (VRAM/HBM, L1/L2 cache), and interconnect topology (NVLink, NVSwitch, InfiniBand) to make informed optimization decisions.

## Key Architecture Generations

| Generation | Example GPUs | FP8 Compute (dense) | Memory | Bandwidth | Key Feature |
|-----------|-------------|---------------------|--------|-----------|-------------|
| Hopper | H100, H200 | ~2 petaFLOPS | 80–141 GB | 3.35–4.8 TB/s | Introduced FP8 Tensor Cores |
| Blackwell | B200, B300 | ~5 petaFLOPS | 192–288 GB | Up to 8 TB/s | FP4, microscaling formats |
| Rubin | TBD (2026) | TBD | HBM4 | TBD | CPX for compute-bound prefill |

## Bottleneck Rules

- **LLM prefill**: Compute-bound → pick GPU with more FLOPS.
- **LLM decode**: Memory-bandwidth-bound → pick GPU with higher bandwidth (e.g., H200 over H100).
- **Image/video generation**: Compute-bound → more FLOPS.

## Multi-GPU Topology

- **NVLink**: Up to 1800 GB/s (Blackwell) GPU-to-GPU within a node.
- **NVSwitch**: All-to-all coordination among 8 GPUs in a node.
- **InfiniBand**: Up to 400 Gb/s per NIC between nodes; much slower than NVLink.
- **NVL72/NVL144**: Rack-scale systems with 72+ GPUs connected via NVLink.

## Multi-Instance GPU (MIG)

Larger GPUs (A100, H100, H200, B200) can be partitioned into up to 7 fractional instances, useful for small models that would underutilize a full GPU.

## Appearances

- [[Inference Engineering]] — Chapter 3 provides detailed hardware coverage from spec sheets to instance selection.
- [[Two Speeds of a GPU]] — benchmarks H100 SXM5 (989 TFLOPS, 3.35 TB/s) and RTX 4090 under the Roofline Model.
- [[What Even Is a Kernel?]] — contrasts HBM datacenter memory with GDDR consumer memory in GPU kernel execution.

## Related

- [[Inference Engineering]]
- [[Model Compression and Efficiency]]
- [[Roofline Model]]
- [[Arithmetic Intensity]]
- [[GPU Kernel]]
- [[Kernel Fusion]]
