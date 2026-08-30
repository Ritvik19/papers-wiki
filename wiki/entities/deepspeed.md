# DeepSpeed

**Type**: tool  
**Tags**: #entity

## Overview

DeepSpeed is an open-source deep learning optimization library developed by Microsoft Research. It is designed to make distributed training and inference of very large deep learning models highly efficient by implementing advanced memory optimization techniques, such as the Zero Redundancy Optimizer ([[ZeRO]]), CPU/NVMe offloading, and 3D parallelism strategies.

## Appearances

- [[How to Train Really Large Models on Many GPUs?]] — Introduced as Microsoft's primary systems engineering library that implements **ZeRO**, CPU/NVMe offloading, and hybrid 3D parallelism strategies to train massive deep learning models.
- [[Why Multi-Head Self Attention Works: Math, Intuitions and 10+1 Hidden Insights]] — cited for fast GPU implementations of sparse transformers.

## Notes

DeepSpeed has democratized large-scale deep learning by allowing researchers to train models with tens or hundreds of billions of parameters without requiring specialized, low-level model-parallel refactoring. It integrates natively with PyTorch and popular training frameworks like Hugging Face Accelerate, making it an essential building block in the pretraining and fine-tuning pipelines of modern foundation models (such as LLMs like Qwen or Phi).

### ZeRO Stages

| Stage | Shards | Memory Reduction | Communication Overhead |
|---|---|---|---|
| ZeRO-1 | Optimizer states | ~4× | None (no extra comm) |
| ZeRO-2 | Optimizer states + Gradients | ~8× | ReduceScatter during backward |
| ZeRO-3 | Optimizer states + Gradients + Parameters | Linear with $N_{DP}$ | AllGather before every forward/backward |
| ZeRO-Offload | ZeRO-2/3 + CPU RAM offload | 10× on single GPU | PCIe bandwidth bound |
| ZeRO-Infinity | ZeRO-3 + NVMe SSD offload | Near-unlimited | Async PCIe prefetch |

### Key Features Beyond ZeRO

- **3D Parallelism**: DeepSpeed combines DP (ZeRO), PP, and TP into a single unified framework, supporting trillion-parameter models on commodity GPU clusters.
- **Sparse Attention**: Implements sparse attention kernels (e.g. Longformer-style block-sparse patterns) for efficient long-context training.
- **Curriculum Learning**: Sequence-length warmup scheduler for more stable early training on long-document tasks.
- **DeepSpeed Chat**: A full RLHF training pipeline (SFT → Reward Modeling → PPO) with ZeRO integration.
- **DeepSpeed-MII**: Inference microservice with model quantization, kernel fusion, and multi-GPU tensor-parallel inference.

### Key Papers

- **ZeRO** (Rajbhandari et al. 2019): Introduced ZeRO-1/2/3 and ZeRO-R residual memory optimizations.
- **ZeRO-Offload** (Ren et al. 2021): CPU offloading for single-GPU large-model training.
- **ZeRO-Infinity** (Rajbhandari et al. 2021): NVMe offloading for trillion-parameter scale.
- **1-bit Adam / 1-bit LAMB** (Tang et al. 2021): Gradient compression for bandwidth-constrained clusters.

## Related

- [[Microsoft]]
- [[ZeRO]]
- [[Data Parallelism]]
- [[Model Parallelism]]
- [[Pipeline Parallelism]]
- [[Tensor Parallelism]]
- [[Mixed Precision Training]]
- [[How to Train Really Large Models on Many GPUs?]]
