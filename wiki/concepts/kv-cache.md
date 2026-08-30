# KV Cache

**Type**: concept  
**Tags**: #concept

## Overview

The KV (key-value) cache stores precomputed attention keys and values for each token during LLM inference, eliminating redundant recomputation across the autoregressive decoding loop. Without KV caching, each new token would require recalculating attention over the entire preceding sequence.

## Mechanism

During prefill, the inference engine computes and stores KV pairs for all input tokens. During decode, the cache is updated incrementally for each new token. The cache grows linearly with sequence length and can consume significant GPU VRAM — often 80% or more of available memory after model weights are loaded.

## Optimization Techniques

- **Prefix caching** — reuses KV cache entries across requests that share input prefixes (system prompts, code context, multi-turn chat history). Shared prefixes must start from token position 0; a single differing token breaks the prefix match.
- **PagedAttention** — partitions the KV cache into fixed-size pages accessible via lookup tables, allowing fragmented VRAM allocation instead of requiring contiguous memory blocks.
- **Cache offloading** — stores KV cache across a tiered memory hierarchy: GPU VRAM (TB/s), CPU RAM (tens to hundreds of GB/s), local SSD (5–10 GB/s), and networked SSD (GB/s). NVIDIA Dynamo's KVBM manages block movement across levels.
- **Cache-aware routing** — routes repeat users to the same inference replica to maximize prefix cache hits, rather than using simple load-balanced distribution.
- **Quantized KV cache** — reduces cache memory footprint by storing keys/values at lower precision.

## From-Scratch Implementation (Educational)

Sebastian Raschka's [[Understanding and Coding the KV Cache in LLMs from Scratch]] walks through a minimal PyTorch KV cache on the GPT model from *Build a Large Language Model (From Scratch)*:

1. **`register_buffer("cache_k"/"cache_v")`** in `MultiHeadAttention` to persist keys/values across forward passes.
2. **`use_cache` flag** — concatenate new keys/values with `torch.cat`; attend over the full cached tensors.
3. **`reset_kv_cache`** — clear buffers between unrelated prompts to prevent stale-key attention.
4. **`current_pos` tracking** in `GPTModel` — positional embeddings must continue from the cached sequence length during incremental decode.
5. **Generation loop** — prefill the full prompt once, then pass only the new token on each decode step.

The educational version prioritizes readability over performance; production code pre-allocates fixed-size tensors and may apply sliding-window truncation instead of unbounded `torch.cat`.

## Appearances

- [[Understanding and Coding the KV Cache in LLMs from Scratch]] — conceptual diagrams, O(n²)→O(n) complexity argument, and readable PyTorch implementation with ~5× CPU speedup on 124M GPT.
- [[A Visual Guide to Attention Variants in Modern LLMs]] — systematic comparison of MHA, [[Grouped-Query Attention]], and [[Multi-Head Latent Attention]] cache footprints; SWA and sparse patterns reduce revisit cost.
- [[Beyond Standard LLMs]] — contrasts growing MHA KV cache with fixed recurrent state in [[Gated DeltaNet]] hybrid layers; Kimi Linear reports ~75% KV reduction.
- [[DiffusionGemma]] — [[Block Autoregressive Diffusion]] commits denoised 256-token blocks to the KV cache via causal prefill between bidirectional denoising passes.
- [[Inference Engineering]] — Chapter 5.3 covers KV cache reuse, storage tiering, cache-aware routing, and long-context handling.
- [[Prefill and Decode for Concurrent Requests - Optimizing LLM Performance]] — TNG's production analysis of prefill (compute-bound) vs. decode (memory-bandwidth-bound) phases, and how chunked prefill balances time-to-first-token against per-token decode latency under concurrent load.
- [[Unsloth Long Context Training]] — attention sinks and Flex Attention for GPT-OSS long-context training; KV implications of sliding-window patterns.
- [[Papers Explained 586: Gemma 4]] — Demonstrates 37.5% global KV cache reduction via [[p-RoPE]] ($p=0.25$) and $K=V$ key-value sharing, combined with [[Per-Layer Embedding]] to offload token representations to flash storage.

## Notes

Research tools like CacheBlend and LMCache extend prefix caching to non-prefix sequences by correcting positional embeddings and selectively recomputing KV entries, though these are not yet widely deployed in production.

Hugging Face's [KV Cache from scratch in nanoVLM](https://huggingface.co/blog/kv-cache) (2025-06-04) implements the same mechanism covered above inside the minimal nanoVLM codebase: caching keys/values per attention block, tracking the cache across layers with a `start_pos` offset for correct RoPE alignment, and splitting generation into prefill (full-prompt forward pass) and decode (one cached token at a time) phases. Reports a 38% generation speedup from the change.

## Related

- [[Inference Engineering]]
- [[Linear Attention Hybrids]]
- [[Gated DeltaNet]]
- [[Speculative Decoding]]
- [[Large Language Models]]
- [[p-RoPE]]
- [[Per-Layer Embedding]]
