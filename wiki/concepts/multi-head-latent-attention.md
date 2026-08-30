# Multi-Head Latent Attention

**Tags**: #concept

Multi-head latent attention (MLA) is a [[KV Cache]] compression strategy introduced in DeepSeek-V2. Instead of caching full-resolution key and value tensors (as in [[Multi-Head Attention]] or [[Grouped-Query Attention]]), MLA stores a compressed latent representation and reconstructs usable K/V state when needed—also applying compression to queries in the full design.

## Overview

MLA targets the same bottleneck as GQA—growing cache memory at long context—but compresses **what** is stored rather than **how many** K/V heads exist. DeepSeek-V2 ablations cited by Raschka show GQA falling below MHA on modeling quality while MLA remains competitive or can slightly outperform MHA when tuned, making MLA a quality-preserving efficiency move at large scale—not merely a memory hack.

The tradeoff is implementation and serving complexity. MLA spread through DeepSeek V3/R1/V3.1, Kimi K2, GLM-5 (with [[DeepSeek Sparse Attention]]), Ling 2.5, and Sarvam 105B. Sarvam's deliberate 30B GQA vs 105B MLA pair is a useful reference: same team, different scale, different attention choice.

Practitioners report MLA works best at large model sizes (~100B+); below that GQA may be easier to tune and deploy.

## Appearances

- [[A Visual Guide to Attention Variants in Modern LLMs]] — MLA vs GQA diagrams, DeepSeek-V2 ablations, Sarvam cache-size comparison.
- [[Beyond Standard LLMs]] — MLA appears in Ling 2.5 and Kimi Linear hybrid discussions.
- [[Papers Explained 451 - Kimi K2]] — trillion-parameter MoE with MLA following DeepSeek-V3 design.

## Notes

- MLA is often paired with sparse or hybrid attention in newer stacks (DSA + MLA in DeepSeek V3.2; Lightning Attention + MLA in Ling 2.5).
- Kimi Linear replaces Qwen-style gated full attention with **gated MLA** in its 3:1 hybrid.

## Related

- [[Grouped-Query Attention]]
- [[KV Cache]]
- [[DeepSeek Sparse Attention]]
- [[Linear Attention Hybrids]]
- [[Model Compression and Efficiency]]
