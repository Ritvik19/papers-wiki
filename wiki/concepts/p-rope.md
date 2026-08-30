# p-RoPE

**Type**: concept  
**Tags**: #concept

## Overview

**$p$-RoPE (Partial Rotary Position Embedding)** is a position encoding formulation that applies Rotary Position Embeddings to a specified fraction $p$ of head dimensions (or selectively across attention layer types). In [[Papers Explained 586: Gemma 4]], Google employs $p$-RoPE with $p = 0.25$ on global attention layers alongside full RoPE on local sliding-window layers, substantially reducing the long-context [[KV Cache]] footprint.

## Mechanism

1. **Selective Rotary Encoding**:
   - In standard RoPE, all $d_{\text{head}}$ dimensions of query and key projections are rotated according to position index $m$.
   - Under $p$-RoPE, rotary transformation is applied only to a $p$-fraction ($p = 0.25$) of the key and query channels, while the remaining $(1 - p)$ channels retain absolute or unrotated representations.

2. **Dual-Frequency Interleaved Attention**:
   - Gemma 4 pairs local sliding-window attention blocks with global full-attention blocks in fixed ratios (4:1 for E2B; 5:1 for E4B, 12B, 26B-A4B, and 31B).
   - **Global Attention Layers**: Use $p$-RoPE ($p=0.25$) with a long-context base frequency $\theta = 1{,}000{,}000$ ($1\text{M}$) to maintain extrapolation over 128K–256K tokens.
   - **Local Attention Layers**: Use standard RoPE ($p=1.0$) with a local base frequency $\theta = 10{,}000$ ($10\text{k}$).

3. **Memory Footprint & KV Savings**:
   - In global attention layers, $p$-RoPE is paired with $K=V$ value reuse (reusing key tensors as value representations).
   - The combination of $p=0.25$ rotary channel reduction and key-value sharing reduces the global KV cache memory requirement by **37.5%**, enabling long-context inference on memory-constrained hardware.

4. **Cache Layer Sharing**:
   - Edge models further optimize memory by sharing KV caches across layers in fixed ratios: 20/35 shared layers for E2B, and 18/42 for E4B.

## Appearances

- [[Papers Explained 586: Gemma 4]] — Introduces $p$-RoPE ($p=0.25$) with 1M global and 10k local frequencies.
- [[Gemma 4 Technical Report]] — Formal description of long-context efficiency mechanisms and KV reduction.
- [[A Visual Guide to Gemma 4]] — Visual diagrams illustrating $p$-RoPE head slicing and local-to-global attention interleaving.

## Related

- [[Positional Encoding]]
- [[KV Cache]]
- [[Long Context]]
- [[Model Compression and Efficiency]]
- [[Gemma 4]]
