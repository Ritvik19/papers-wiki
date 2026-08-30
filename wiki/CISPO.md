# CISPO

**Type**: concept  
**Tags**: #concept

## Overview

Clipped Importance Sampling Weight Policy Optimization (CISPO) is a GRPO variant from the MiniMax-M1 technical report (Chen et al., 2025). It targets the problem of pivotal low-probability "fork" tokens (e.g., "wait", "aha", self-reflection markers) being clipped out of the policy gradient after the first policy update when multiple gradient updates are performed per batch.

In GRPO and DAPO, the importance ratio for a token exceeding the clipping bounds receives **zero gradient** — the token is completely excluded from the update. This is problematic for fork tokens because: (1) they are rare and have low base probabilities; (2) after even one policy update, their importance ratio can exceed the clipping range; (3) subsequent policy updates over the same batch ignore them entirely. Yet these tokens are crucial for stabilizing entropy and enabling the kind of exploratory reasoning that makes reasoning models effective.

CISPO uses the GRPO advantage estimation but structures the surrogate objective like REINFORCE: the policy gradient is scaled by a **stop-gradient clamped importance ratio**. This means the importance ratio is treated as a constant (not backpropagated) that caps each token's contribution, rather than completely zeroing out clipped tokens. Clipped tokens still contribute gradient — their weight is just capped at a maximum value.

MiniMax-M1 performs 16 policy updates per batch (vs. the typical 2–4), making standard clipping especially damaging to fork tokens. CISPO is shown to improve both stability and sample efficiency in comparison to GRPO and DAPO.

## Appearances

- [[GRPO++: Tricks for Making RL Actually Work]] — Covered in the "More Tweaks" section.
- [[Introducing North Mini Code]] — Cohere uses CISPO for async multi-environment agentic RLVR on North Mini Code (token-level loss with importance-sampling correction).

## Notes

- Addresses a complementary failure mode to DAPO's clip-higher: clip-higher allows exploration tokens to grow, while CISPO ensures they don't get zeroed out in multi-update settings.
- Particularly relevant when performing many gradient updates per rollout batch.

## Related

- [[GRPO]] — Base algorithm.
- [[DAPO]] — "Clip higher" is a related but distinct fix for the clipping problem.
