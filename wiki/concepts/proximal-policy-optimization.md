# Proximal Policy Optimization

**Type**: concept  
**Tags**: #concept

## Overview

Proximal Policy Optimization (PPO) is a policy-gradient algorithm that stabilizes updates by limiting how far the new policy can diverge from the old one. The standard **PPO-Clip** objective clips the importance-sampling ratio r_t(θ) = π_θ(a|s)/π_θ_old(a|s) to [1−ε, 1+ε] when multiplying advantage estimates, preventing destructively large policy steps while reusing rollouts from the behavior policy.

## Appearances

- [[Trust Region and Proximal Policy Optimization (TRPO and PPO)]] — AI Summer intro: penalized KL form, adaptive coefficient, and canonical clipped surrogate L^CLIP.
- [[GRPO]] — retains PPO-style clipping; replaces learned critic with group-relative advantage baselines for LLM training.

## Notes

PPO is the dominant deep RL and LLM post-training optimizer before GRPO variants. Related stabilization work: [[GRPO++: Tricks for Making RL Actually Work]], [[DAPO]], [[KL Regularization]].

## Related

- [[Trust Region Policy Optimization]]
- [[Actor-Critic Methods]]
- [[Importance Sampling]]
- [[Policy Gradient]]
- [[GRPO]]
