# Value Iteration

**Type**: concept  
**Tags**: #concept

## Overview

Value iteration is a [[Dynamic Programming]] algorithm that iteratively applies the Bellman optimality backup to a value function until convergence, then derives a greedy policy. Each sweep updates every state (or state–action pair) toward the max over actions of the one-step lookahead. It is closely related to policy iteration but combines policy evaluation and improvement into a single update rule.

## Appearances

- [[Reinforcement Learning: An Introduction]] — Chapter 4; gambler’s problem.

## Notes

Value iteration is planning with a known model. Sample-based analogs include Q-learning (off-policy TD control toward q*).

## Related

- [[Dynamic Programming]]
- [[Policy Iteration]]
- [[Q-learning]]
- [[Markov Decision Process]]
- [[Reinforcement Learning: An Introduction]]
