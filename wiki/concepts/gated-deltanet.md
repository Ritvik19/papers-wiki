# Gated DeltaNet

**Tags**: #concept

Gated DeltaNet (Gated Delta Network) is a linear-attention layer that replaces softmax pairwise attention with a recurrent state update inspired by delta-rule memory and Mamba-style gating. It was adopted from the *Gated Delta Networks: Improving Mamba2 with Delta Rule* paper and deployed in open models such as Qwen3-Next and Kimi Linear as part of [[Linear Attention Hybrids]].

## Overview

Instead of computing an n×n attention matrix, Gated DeltaNet processes tokens sequentially and maintains a fixed-size memory state **S** (per head, shape d_head × d_head). At each timestep, α (decay gate) controls how much old memory to forget, β (update gate) controls how strongly new inputs modify the state, and an output gate (SiLU-activated) scales what is emitted—analogous to gated attention's sigmoid output gate but applied to a recurrent update rather than softmax attention output.

The design trades global pairwise context for O(n) compute and constant memory with respect to sequence length—no growing [[KV Cache]]—at the cost of compressing history through a fixed bottleneck. Hybrid stacks therefore interleave Gated DeltaNet blocks with periodic full-attention layers (typically 3:1) to recover long-range reasoning.

## Appearances

- [[A Visual Guide to Attention Variants in Modern LLMs]] — hybrid 3:1 stacking with [[Gated Attention]] full layers; memory curves vs ordinary attention; Qwen3.5 flagship promotion.
- [[Beyond Standard LLMs]] — pedagogical walkthrough with code sketches, KV-cache size formulas, and comparison to gated full attention; cites Qwen3-Next and Kimi Linear.

## Notes

- Kimi Linear's Kimi Delta Attention (KDA) refines Gated DeltaNet with channel-wise decay gates instead of scalar per-head gates.
- MiniMax-M2's return to standard attention after MiniMax-M1 is a cautionary production datapoint for linear variants on reasoning and multi-turn tasks.

## Related

- [[Linear Attention Hybrids]]
- [[KV Cache]]
- [[Self-Attention]]
- [[Beyond Standard LLMs]]
