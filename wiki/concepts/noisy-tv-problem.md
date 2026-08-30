# Noisy-TV Problem

**Type**: concept  
**Tags**: #concept

## Overview

The noisy-TV problem (Burda et al., 2018) is a failure mode of **curiosity-driven / intrinsic-reward RL** agents. It describes an agent that encounters a TV emitting uncontrollable, unpredictable random noise. If the agent is rewarded for novelty or prediction error, the TV continuously provides high intrinsic reward—yet the agent makes no meaningful progress on any real task. The agent becomes a "couch potato," fixated on the noise source forever.

This problem highlights a fundamental challenge: **intrinsic rewards based on prediction error or novelty cannot distinguish between (a) genuinely learnable, agent-relevant novelty and (b) irreducible stochastic noise from uncontrollable environment factors.**

## Manifestations by Method

| Method | Vulnerability |
|--------|--------------|
| Forward dynamics error (raw pixels) | High—noise in pixels = permanent high bonus |
| VAE encoding | Moderate—still encodes random noise |
| ICM / IDF | Reduced—inverse dynamics excludes uncontrollable factors, but only if agent cannot control access to the noise source |
| Random features (RF) | High—similar to raw pixels |
| RND | Moderate—random target means random-TV images are "similar" in hash space eventually |
| Count-based (hashing) | Moderate—random states get unique hashes but counts eventually grow |
| Episodic Curiosity (EC) | Claimed to overcome it—reachability-based bonus is not directly driven by signal content |

## Appearances

- [[Exploration Strategies in Deep Reinforcement Learning]] — Introduced as a "thought experiment"; empirical experiments show RF and IDF features in environments with noisy TV; Episodic Curiosity (EC) is claimed to resolve it.

## Notes

- The noisy-TV problem is distinct from the **hard-exploration problem**: hard exploration is about sparse task rewards, whereas noisy-TV is about misleading intrinsic rewards.
- No single method fully eliminates the problem; practical solutions combine careful feature engineering with diversity mechanisms.

## Related

- [[Intrinsic Curiosity Module (ICM)]] — Partially mitigates via inverse-dynamics encoding.
- [[Exploration Strategies in Deep Reinforcement Learning]] — Source article.
- [[Exploration-Exploitation Tradeoff]] — Broader RL concept.
