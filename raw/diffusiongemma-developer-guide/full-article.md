# DiffusionGemma: The Developer Guide

JUNE 10, 2026

Ian Ballantyne, Omar Sanseviero

Following our announcement in our launch blog post, we are sharing this developer guide to help you understand, serve and customize this experimental model.

Built on the Gemma 4 backbone, **DiffusionGemma** introduces several milestones for developer workflows:

1. **Compute-bound parallel generation**: Bypasses memory-bandwidth limitations by shifting the bottleneck to compute, delivering up to 4x faster token generation on GPUs (up to 700+ tokens per second on NVIDIA GeForce RTX 5090 and 1000+ tokens per second on a single NVIDIA H100).
2. **Bidirectional context & self-correction:** Uses bidirectional attention to evaluate the entire text block simultaneously during generation, enabling real-time error correction and parallel context propagation.
3. **Developer-friendly sizes**: Designed as a 26B Mixture of Experts (MoE) model that activates only 3.8B parameters during inference, allowing quantized deployment within 18 GB VRAM limits.

## The Architecture

For developers building with traditional LLMs on GPUs, the primary bottleneck is memory bandwidth. Autoregressive language models must repeatedly load model weights from memory to generate text one token at a time. DiffusionGemma bypasses this limitation by shifting the bottleneck from memory bandwidth to compute, generating and refining a **256-token canvas** in parallel.

- **Uniform State Diffusion:** Instead of predicting tokens sequentially, DiffusionGemma starts with a canvas of random placeholder tokens and iteratively refines them in parallel. Over multiple denoising passes, highly confident tokens help resolve adjacent positions, causing the entire sequence to snap into focus.
- **Block Autoregressive Diffusion for Variable Length Generation:** For sequences longer than 256 tokens, once a 256-token block is fully denoised, the model processes and commits it to the KV cache. The model then transitions to the next block, initializing a fresh 256-token canvas conditioned on the previously committed history.

## Showcase: Solving Sudoku with Parallel Denoising

Traditional autoregressive models struggle with strict, multivariable constrained problems like Sudoku. DiffusionGemma's denoising step allows every canvas query to attend to all positions in parallel.

- **Error Correction via Re-Noising**: If confidence drops, the sampler replaces digits with random ones, allowing for continuous self-correction.
- **Efficient Early Stopping**: Fine-tuning on Sudoku shows that adapters enhance early stopping.

The base DiffusionGemma model is not specifically trained to solve Sudoku puzzles (~0% success rate). Applying the simple JAX SFT recipe on a Sudoku dataset raises correctness to **80% success**, while decreasing the overall inference step count.

## Block Autoregressive Denoising

- **Prefill / Incremental Prefill (Causal):** Uses causal attention to ingest the prompt context and write to the KV cache.
- **Denoising (Bidirectional):** Uses bidirectional attention to iteratively denoise the canvas.

## Serving DiffusionGemma

vLLM integration with OpenAI-compatible local server:

```
vllm serve google/diffusiongemma-26B-A4B-it \
  --max-model-len 262144 \
  --max-num-seqs 4 \
  --gpu-memory-utilization 0.85 \
  --attention-backend TRITON_ATTN \
  --generation-config vllm \
  --hf-overrides '{"diffusion_sampler": "entropy_bound", "diffusion_entropy_bound": 0.1}' \
  --diffusion-config '{"canvas_length": 256}' \
  --enable-chunked-prefill
```

Also supported: Hugging Face Transformers, SGLang, MLX. Fine-tune with Hackable Diffusion, Unsloth, or NVIDIA NeMo. Deploy via Google Cloud Model Garden or NVIDIA NIM.
