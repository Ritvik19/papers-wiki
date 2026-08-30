# Dynamic Programming

**Type**: concept  
**Tags**: #concept

## Overview

Dynamic programming (DP) in RL refers to **planning** methods that compute value functions and optimal policies when the MDP model (transition probabilities and rewards) is fully known. Sutton & Barto present policy evaluation, policy improvement, **policy iteration**, **value iteration**, and asynchronous DP variants (Chapter 4). DP provides the backup-diagram intuition—bootstrapping from successor states—that [[Temporal-Difference Learning]] and [[Monte Carlo Methods]] later approximate from samples.

## Appearances

- [[Reinforcement Learning: An Introduction]] — Chapter 4; gridworld, Jack’s car rental, gambler’s problem.

## Notes

“DP” in RL is not the same as DP in classical optimization over sequences; here it means iterative application of Bellman consistency equations. When the model is unknown, sample-based methods replace DP backups.

## Related

- [[Markov Decision Process]]
- [[Temporal-Difference Learning]]
- [[Dyna]]
- [[Reinforcement Learning: An Introduction]]
