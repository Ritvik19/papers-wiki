# Relative Attention

**Type**: concept  
**Tags**: #concept

## Overview

Relative attention is Inkling's learned positional encoding mechanism: instead of [[Rotary Positional Embedding]] (RoPE), each attention layer learns position directly in the attention logits via a fourth projection producing per-token, per-head relative features, combined with distance information between query and key positions.

## Appearances

- [[Inkling]] — primary architectural choice; Thinking Machines reports better long-context extrapolation than RoPE.
- [[Inkling-Small]] — inherits the same relative-attention stack.

## Notes

- In Inkling's 5:1 sliding-window/global hybrid (66 layers), 55 layers use 512-token local windows where relative bias provides positional signal within the window.
- In 11 global layers, the released Transformers implementation applies the learned bias only over the preceding 1,024 tokens; attention beyond that range is effectively content-based with respect to the positional bias — analogous to NoPE-style global layers in other architectures.
- [[Sebastian Raschka]] notes this pairs naturally with the SWA-heavy design.

## Related

- [[Positional Encoding]]
- [[Inkling]]
- [[A Visual Guide to Attention Variants in Modern LLMs]]
- [[Long Context]]
