# Megatron-LM

**Type**: tool  
**Tags**: #entity

## Overview

Megatron-LM is a large-scale deep learning framework developed by NVIDIA's Applied Deep Learning Research team. It specializes in training massive Transformer-based language models in highly distributed environments by introducing innovative intra-layer model parallelism techniques, most notably horizontal Tensor Parallelism and the PTD-P (Pipeline, Tensor, Data Parallelism) hybrid scheduling.

## Appearances

- [[How to Train Really Large Models on Many GPUs?]] — Detailed as NVIDIA's primary framework that implements horizontal **Tensor Parallelism** for Multi-Head Attention and MLP layers, and pioneering multi-chunk interleaved pipeline schedules.

## Notes

Megatron-LM resolved a major scaling bottleneck by introducing intra-layer sharding. Instead of sharding models vertically (by layer boundaries, which causes pipeline bubbles), Megatron-LM shards individual matrix operations inside each transformer block column-wise and row-wise, ensuring that communication overhead is kept to a minimum by utilizing high-speed NVLink interconnects for inline `AllReduce` operations. Megatron-LM's design principles underpin many state-of-the-art training infrastructures and were crucial in training monumental models like Megatron-Turing NLG 530B.

### Paper Timeline

| Paper | Year | Key Contribution |
|---|---|---|
| **Megatron-LM** (Shoeybi et al.) | 2019 | Tensor Parallelism for MLP + Attention; 8.3B parameter GPT-2 |
| **Efficient Large-Scale Training** (Narayanan et al.) | 2021 | PTD-P (3D parallelism) + interleaved 1F1B pipeline; 1T parameter scale |
| **Megatron-Turing NLG** (Smith et al.) | 2022 | 530B parameter language model trained on 2,240 A100 GPUs; TP=8, PP=35, DP=12 |
| **Sequence Parallelism** (Korthikanti et al.) | 2022 | Sharding layer-norm and dropout activations along sequence dimension |

### Key Features

- **Tensor Parallelism**: Column-wise / row-wise splitting of MLP and Attention GEMMs, with single `AllReduce` at the block boundary.
- **Pipeline Parallelism**: Interleaved 1F1B with $v$ model chunks per device, reducing bubble fraction by $v\times$.
- **Sequence Parallelism**: Extends TP to distribute layer-norm and dropout activations along the sequence dimension, eliminating the activation memory bottleneck in long-context training.
- **Flash Attention Integration**: Modern Megatron checkpoints use FlashAttention-2/3 for memory-efficient attention computation, further reducing peak memory.
- **Distributed Checkpointing**: Saves model state sharded across TP/PP groups, enabling rapid restore from large-scale training runs.

### Optimal Parallelism Degrees (Megatron-LM Heuristics)

- **Tensor Parallel ($N_{TP}$)**: Must be $\leq$ GPUs per node. Typically 4 or 8 (NVLink-connected).
- **Pipeline Parallel ($N_{PP}$)**: Scales with model depth. Higher $N_{PP}$ lowers per-device memory but increases bubble fraction if microbatch count is low.
- **Data Parallel ($N_{DP}$)**: Fills remaining GPU count. Controls effective global batch size.

## Related

- [[Tensor Parallelism]]
- [[Pipeline Parallelism]]
- [[Model Parallelism]]
- [[Data Parallelism]]
- [[DeepSpeed]]
- [[How to Train Really Large Models on Many GPUs?]]
