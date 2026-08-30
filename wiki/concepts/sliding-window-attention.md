# Sliding Window Attention

**Tags**: #concept

Sliding window attention (SWA), also called local attention, restricts each token to attending only within a fixed window of recent positions instead of the full prefix. It reduces memory and compute for long-context inference; practical stacks interleave local SWA layers with periodic **global** full-attention layers so information can still propagate across the sequence.

## Overview

SWA turns many layers from global \(O(n^2)\) attention into local attention over a bounded neighborhood. What matters in deployment is usually the **local:global layer ratio** and **window size**—not merely "uses SWA." Examples from Raschka's 2026 survey:

- **Gemma 3**: 5:1 local:global, 1024-token window (more aggressive than Gemma 2's 1:1 / 4096).
- **OLMo 3** and **Arcee Trinity**: 3:1 local:global pattern.
- **Xiaomi**: 5:1 with a very small 128-token window.

Gemma 3 ablations suggest the more aggressive setup hurt perplexity only slightly—local attention's cost savings were already known; the surprise was how little quality moved. SWA commonly co-occurs with [[Grouped-Query Attention]] because SWA limits how much context a layer revisits while GQA limits per-token K/V cache size.

## Appearances

- [[A Visual Guide to Attention Variants in Modern LLMs]] — SWA vs global attention, Gemma 3 ablations, long-context savings diagrams.
- [[Mistral 7B]] — influential early open model combining GQA with SWA (4096 window).
- [[Papers Explained 157 - Gemma 2]] — prior Gemma hybrid local/global setup baseline for Gemma 3 comparisons.
- [[Unsloth Long Context Training]] — GPT-OSS alternating SWA/FA with 128-token windows and attention sinks.

## Notes

- [[DeepSeek Sparse Attention]] also limits each token to a subset of past positions but learns **which** tokens via an indexer rather than a fixed window.
- SWA layers still use a [[KV Cache]] for their local window; global layers retain full-prefix cache needs.

## Related

- [[Grouped-Query Attention]]
- [[DeepSeek Sparse Attention]]
- [[Long Context]]
- [[KV Cache]]
- [[Model Compression and Efficiency]]
