# Gated Attention

**Tags**: #concept

Gated attention refers to stability-oriented modifications applied to **retained full-attention** layers inside modern LLM stacks—not a separate attention family alongside MHA or GQA. It is distinct from [[Gated DeltaNet]], which is a linear-time mixer, though both use gating for controlled information flow.

## Overview

In hybrid architectures ([[Linear Attention Hybrids]]), most layers are replaced by cheaper sequence modules; periodic full-attention layers remain for exact content retrieval. Those full-attention blocks are where gated attention typically appears—for example Qwen3-Next and Qwen3.5 interleave three [[Gated DeltaNet]] blocks with one gated full-attention layer (3:1). Trinity Large applies a related gating idea in a conventional (non-hybrid) attention stack.

Per the Gated Attention paper and Raschka's summary, the block is essentially scaled dot-product attention plus:

- an **output gate** scaling the attention result before the output projection (and residual),
- a **zero-centered QK-norm** variant instead of standard RMSNorm on queries and keys,
- **partial RoPE** (partial rotary position embedding).

These are control/stability tweaks—not the large architectural shifts seen in MLA or linear attention.

## Appearances

- [[A Visual Guide to Attention Variants in Modern LLMs]] — gated attention in Qwen3-Next/3.5 and Trinity; contrast with Gated DeltaNet in hybrid stacks.
- [[Beyond Standard LLMs]] — Gated DeltaNet and Qwen3-Next hybrid context.
- [[Gated DeltaNet]] — co-occurs in 3:1 hybrid pattern; different mechanism.

## Notes

- Kimi Linear replaces Qwen-style gated full attention with **gated MLA** while keeping the same 3:1 hybrid rhythm.
- Output gating in gated attention (sigmoid on attention output) parallels—but is not identical to—the gates in Gated DeltaNet's recurrent update.

## Related

- [[Gated DeltaNet]]
- [[Linear Attention Hybrids]]
- [[Multi-Head Attention]]
- [[Self-Attention]]
