# Inference Engine

**Type**: concept  
**Tags**: #concept

## Overview

An inference engine is specialized software that serves generative AI models in production, handling batching, scheduling, KV cache management, and hardware-specific optimizations. The three dominant open-source inference engines for LLMs are vLLM, SGLang, and TensorRT-LLM.

## Key Engines

- **vLLM** — pioneered PagedAttention for efficient KV cache management; broadly used for its ease of deployment and wide model support.
- **SGLang** — focuses on structured generation and co-design of frontend language with backend runtime; strong performance on constrained-output workloads.
- **TensorRT-LLM** — NVIDIA's engine built on TensorRT; deep integration with NVIDIA hardware features, EAGLE speculation, and Dynamo for disaggregated serving.

## Software Stack

Inference engines sit atop a layered stack:
1. **CUDA** — GPU programming model; custom kernels like FlashAttention are written in CUDA.
2. **PyTorch** — deep learning framework; provides model definitions and basic execution.
3. **Inference engines** — add batching, scheduling, caching, and production-grade serving.
4. **NVIDIA Dynamo** — orchestration layer for distributed serving, disaggregation, and KV cache management across replicas.

## Appearances

- [[Inference Engineering]] — Chapter 4 covers the full software stack from CUDA to inference engines and Dynamo.

## Related

- [[Inference Engineering]]
- [[KV Cache]]
- [[Speculative Decoding]]
- [[Large Language Models]]
