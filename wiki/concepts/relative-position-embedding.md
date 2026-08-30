# Relative Position Embedding

**Type**: concept  
**Tags**: #concept

## Overview

**Relative position embeddings** encode the distance between query and key tokens in attention logits rather than absolute indices. Classic formulations include Shaw et al. (2018) self-attention with relative position representations and the Music Transformer relative scheme. They often extrapolate to longer sequences better than absolute encodings or some RoPE setups.

## Appearances

- [[Inkling]] — uses relative attention instead of RoPE: a fourth projection produces per-token, per-head relative features R, adjusted by key–query distance and injected into attention.
- [[How Positional Embeddings Work in Self-Attention (Code in PyTorch)]] — tutorial covering absolute vs relative 1D PE.
- [[Positional Embeddings]] — concept covering absolute index vs relative distance buckets.
- [[Papers Explained Review 06 - Position Encodings]] — survey of position-encoding families.

## Notes

Inkling reports better long-context performance and extrapolation with relative PE than with the more common RoPE recipe, interleaved with 5:1 sliding-window / global attention.

## Related

- [[Positional Embeddings]]
- [[Papers Explained Review 06 - Position Encodings]]
- [[Inkling]]
- [[Short Convolution]]
- [[Long Context]]
