# Task Coexistence

**Type**: concept  
**Tags**: #concept

## Overview

Task Coexistence refers to the property in reinforcement learning post-training where optimizing a model on a target task preserves and positively transfers to untrained capabilities (+2.3% on out-of-domain tasks), in sharp contrast to the task conflicts and performance degradation (-5.1%) characteristic of [[Supervised Fine-Tuning]].

## Mechanism

Task coexistence arises from two fundamental properties of on-policy RL:
1. **Update Sparsity & Minimal Norms**: RL updates induce parameter changes with $L_2$ norms orders of magnitude smaller than SFT ($\approx 0.03$ vs $7.4$), guided by [[RL's Razor]].
2. **Subspace Orthogonality**: Parameter updates for distinct tasks are mutually orthogonal in high-dimensional space (pairwise cosine similarity $\approx 10^{-5}$), decoupling optimization trajectories across tasks.

## Appearances

- [[Papers Explained: SFT Conflicts, RL Coexists]] — Demonstrates task coexistence across mathematical, scientific, coding, and logical reasoning benchmarks.

## Notes

- Resolves the multi-stage post-training failure mode where sequential SFT results in catastrophic collapse (-23.1% below base).

## Related

- [[Parallel-RL]]
- [[Gradient Interference]]
- [[RL's Razor]]
- [[Catastrophic Forgetting]]
- [[Multi-Task Learning]]
- [[Reinforcement Learning]]
- [[Supervised Fine-Tuning]]
