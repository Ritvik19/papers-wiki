# SMEBU

**Type**: concept  
**Tags**: #concept

## Overview

Soft-clamped Momentum Expert Bias Updates (SMEBU) is a load-balancing strategy for Mixture-of-Experts models introduced in the Arcee Trinity Large technical report. It replaces the standard per-step sign-based expert bias update used in auxiliary-loss-free load balancing with a tanh soft-clamped, magnitude-aware update that incorporates a momentum buffer to smooth expert bias updates over time.

## How It Works

1. Compute the normalized per-expert violation (deviation from target load), making the update independent of sequence length and batch size.
2. Apply tanh soft-clamping with a tunable scale κ to prevent large discrete jumps.
3. Maintain a momentum buffer m over experts; the bias update blends the new violation signal with the momentum using factor β and learning rate λ.

This design prevents the oscillatory behavior that can arise from sign-based updates (where overloaded experts immediately swing to underloaded) and stabilizes training at large scale.

## Appearances

- [[Papers Explained: Arcee Trinity]] — introduced for Trinity Large (400B/13B active parameters); Trinity Nano and Mini use the standard auxiliary-loss-free approach instead.

## Notes

- SMEBU is distinct from DeepSeek-style load balancing: it adds magnitude-awareness and momentum on top of the decoupled expert-bias paradigm.
- Whether SMEBU outperforms simpler approaches is described mathematically but not ablated numerically in the Trinity article.

## Related

- [[Mixture of Experts]]
- [[Papers Explained: Arcee Trinity]]
