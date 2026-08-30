# Final Token Preference Optimization

**Type**: concept  
**Tags**: #concept

## Overview

**Final Token Preference Optimization** (FTPO) is a preference-learning variant scoped to the single token that starts a [[Doom Loop|doom loop]]. Instead of comparing full completions as in standard [[Papers Explained 148 - Direct Preference Optimization|DPO]], FTPO pairs one chosen next token against several rejected loop-trigger tokens at the same position and optimizes in logit space with KL regularization.

## Appearances

- [[Antidoom]] — Liquid AI blog applying FTPO to LFM2.5-2.6B and Qwen3.5-4B (2026).
- [[Doom Loop]] — failure mode FTPO targets.

## Notes

- Adapted from Antislop, which used similar final-token preference pairs for slop reduction.
- The two-part regularizer limits how far the policy can move from the reference model while still suppressing high-probability loop starters.
- Reported gains are largest under greedy decoding, where doom loops are most common.

## Related

- [[Antidoom]] — primary source and results.
- [[Doom Loop]] — target failure mode.
- [[Direct Preference Optimization]] — broader DPO concept stub.
- [[Papers Explained 148 - Direct Preference Optimization]] — paper summary.
- [[Liquid AI]] — implementer.
