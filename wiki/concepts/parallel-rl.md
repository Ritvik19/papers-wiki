# Parallel-RL

**Type**: concept  
**Tags**: #concept

## Overview

Parallel-RL is a distributed post-training framework where distinct reasoning tasks (e.g. math, science, code, logic) are trained independently in parallel using reinforcement learning (such as [[GRPO]]), and their resulting parameter updates ($\Delta W_i$) are merged into a single model without catastrophic task interference.

## Mechanisms & Merging Strategies

Because on-policy RL parameter updates across distinct tasks occupy approximately orthogonal parameter subspaces ($\langle \Delta W_i, \Delta W_j \rangle \approx 0$), inter-task interference is negligible.

1. **Naive Sum / Mean**: Directly summing independent task updates ($\Delta W = \sum_i \Delta W_i$) retains ~95% of single-task gains (+5.0% over base), whereas Parallel-SFT collapses (retaining only 66%).
2. **Sparse Merging**: Applying [[TIES]] or rank-1 [[Singular Value Decomposition|SVD]] retains 98% and 96% of single-task RL performance.
3. **Adapted Parallel-RL**: Brief post-merge adaptation on a tiny data subset (5% of original training size) yields +9.4% over the base model, exceeding even individual task-specific models (102.8% retention).

## Appearances

- [[Papers Explained: SFT Conflicts, RL Coexists]] — Introduced as an empirical application of multi-task gradient orthogonality in RL.

## Notes

- Bypasses the catastrophic forgetting observed in sequential multi-stage SFT and eliminates the complex hyperparameter balancing required by joint multi-task training mixtures.

## Related

- [[Task Coexistence]]
- [[Gradient Interference]]
- [[GRPO]]
- [[Model Merging]]
- [[Multi-Task Learning]]
