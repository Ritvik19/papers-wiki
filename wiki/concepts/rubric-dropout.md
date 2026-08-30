# Rubric Dropout

**Type**: concept  
**Tags**: #concept

## Overview
A regularization technique for rubric-based reinforcement learning (such as GRPO) that randomly masks a fraction $f \in [0.3, 0.5]$ of rubric criteria at each training step, preventing the policy from gaming specific proxy criteria and eliminating reward hacking.

## Appearances
- [[Papers Explained 600: Rubric Dropout]] — introduced by Rastogi et al. (2026).

## Notes
- Requires prompt-level shared masks so that all group rollouts are judged against identical sub-rubrics.

## Related
- [[Rubric-Based Reinforcement Learning]]
- [[Reward Hacking]]
- [[GRPO]]
