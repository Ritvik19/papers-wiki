# Importance Sampling

**Type**: concept  
**Tags**: #concept

## Overview

Importance sampling in RL corrects for **distribution mismatch** when learning from data generated under a behavior policy different from the target policy. Each return or update is weighted by the product of probability ratios π(a|s)/b(a|s) along the trajectory. Sutton & Barto cover ordinary vs **weighted** importance sampling for off-policy Monte Carlo prediction and control (Chapter 5), and per-decision variants (Chapter 7).

## Appearances

- [[Reinforcement Learning: An Introduction]] — Chapter 5 (blackjack, random walk); Chapter 7; Chapter 11 (off-policy stability).
- [[Trust Region and Proximal Policy Optimization (TRPO and PPO)]] — PPO/TRPO use ratio r_t(θ) = π_θ(a|s)/π_θ_old(a|s) to evaluate policy improvements from old-policy rollouts.

## Notes

High-variance importance weights plague naive off-policy RL. Truncated importance sampling (TIS) in [[GRPO++: Tricks for Making RL Actually Work]] addresses a related sampler–learner gap in LLM training.

## Related

- [[Proximal Policy Optimization]]
- [[Trust Region Policy Optimization]]
- [[Off-Policy Learning]]
- [[Monte Carlo Methods]]
- [[Truncated Importance Sampling]]
- [[Reinforcement Learning: An Introduction]]
