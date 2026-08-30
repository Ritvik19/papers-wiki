Source URL: https://huggingface.co/blog/native-speed-vllm-transformers-backend
Title: Native-speed vLLM transformers modeling backend

# Native-speed vLLM transformers modeling backend

Published July 8, 2026

Harry Mellor, Lysandre

TL;DR: The transformers vLLM backend is now as fast (or faster) than custom vLLM implementations for many LLM architectures. Model authors can automatically leverage their transformers implementations to get ultra fast vLLM inference, for free.

```
# Upgrade the vllm pip package
uv pip install --upgrade vllm --torch-backend auto
```

The transformers library has become the reference modeling library for Machine Learning. It supports 450+ architectures through consistent APIs, and is designed with the main goal that model implementations are self contained and easy to understand. Going through transformers code makes it easy for contributors to learn how an architecture works, and then port it to other frameworks such as vLLM, SGLang, MLX, llama.cpp, and many others.

A big step in this direction was the integration last year of transformers as a modeling backend in vLLM, allowing model authors to run transformers models (LLMs and VLMs alike) inside vLLM without having to port anything. Transformers provides the modeling code, and vLLM provides extremely optimized inference techniques such as continuous batching and custom attention kernels. This integration gets better now.

## Showcase

The transformers modeling backend for vLLM was put head to head with vLLM's hand-written native implementations across three very different Qwen3 models:

- 4B dense model on a single GPU
- 32B dense model on tensor parallelism
- 235B-parameter FP8 Mixture-of-Experts on data + expert parallelism on the same 8xH100 node

The result: the transformers modeling backend now meets or beats native throughput on every one of them.

Running any Hugging Face model through the transformers modeling backend is a single flag, `--model-impl transformers`. It composes with the usual parallelism options, so nothing about the serving setup changes:

```bash
# Qwen3-4B dense, single GPU
vllm serve Qwen/Qwen3-4B --model-impl transformers

# Qwen3-32B dense, tensor-parallel across 2 GPUs
vllm serve Qwen/Qwen3-32B --model-impl transformers --tensor-parallel-size 2

# Qwen3-235B-A22B-FP8 MoE, data-parallel + expert-parallel across 8 GPUs
vllm serve Qwen/Qwen3-235B-A22B-FP8 --model-impl transformers --data-parallel-size 8 --enable-expert-parallel
# add --max-model-len 8192 if your node is memory constrained
```

Models that use linear attention are not currently supported, but support is planned. Custom models where the code lives in a Hub repo are unlikely to work as they will not have been written compliantly.

### How we measured

Each model is compared under three conditions that are identical in every way except the code path: (1) native, `--model-impl vllm`, vLLM's hand-written model (the bar to match); (2) after, `--model-impl transformers` with the PR; (3) before, `--model-impl transformers` without the PR. The full, reproducible runner is available as a gist.

## So, what's new?

The transformers modeling backend for vLLM used to focus on attention as the bottleneck for inference. By plugging vLLM's attention implementation at runtime, a transformers model could run efficiently inside the vLLM engine. But there are many dimensions to deployments that only a custom port used to target to extract maximum inference performance: parallelization across GPUs, compilation, fused kernels, and more. When model authors wanted the absolute best performance, they were still writing custom vLLM implementations.

The latest iteration of the transformers modeling backend for vLLM dynamically applies inference-specific layer fusions at runtime to match the speed of custom code implementations, for compatible architectures.

## How does it work?

The transformers modeling backend for vLLM now uses `torch.fx` to perform static analysis on the model's graph. This searches for known patterns that can be optimized. After any patterns are identified, it uses `ast` (abstract syntax tree) to manipulate the source code and rewrite some operations in place.

What this achieves:

- Fused operations that are many-to-one mapped to (ultra) optimized vLLM kernels, such as the ones used for Expert Parallelization (EP) in Mixture-of-Experts (MoE) models.
- The main other fused operations are vLLM's `MergedColumnParallelLinear` and `QKVParallelLinear`. These blocks allow inferring parallel plans for TP (tensor-parallel); PP (pipeline-parallel) plans can also be inferred if the decoder block list is easily identifiable.
- The manipulated models are still fully (torch) compilable, passed through `torch.compile` and CUDA Graphs, just the same as a dedicated vLLM model implementation.
- Unlike vLLM model implementations, transformers model implementations can be used in training, so the same model code can serve training, evals, and RL rollouts.

This results in native vLLM inference speed for compatible models, without writing a single line of code to optimize the model for inference. A more detailed follow-up blog post on these optimized inference methods is planned.

## Datasets mentioned in this article

Updated 2 days ago, 28 likes, 3 files.
