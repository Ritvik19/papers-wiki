# Expected Sarsa

**Type**: concept  
**Tags**: #concept

## Overview

Expected Sarsa is a temporal-difference control algorithm that uses the **expected value over next actions** under the current policy, rather than the single sampled next action as in [[Sarsa]]. It reduces variance compared to Sarsa while remaining on-policy. In deterministic environments, Expected Sarsa can match [[Q-learning]]’s targets without Q-learning’s off-policy max.

## Appearances

- [[Reinforcement Learning: An Introduction]] — Section 6.6; cliff-walking performance comparison.

## Notes

Double learning (Double Q-learning) addresses maximization bias in Q-learning; Expected Sarsa addresses variance in Sarsa-family updates.

## Related

- [[Sarsa]]
- [[Q-learning]]
- [[Temporal-Difference Learning]]
- [[Reinforcement Learning: An Introduction]]
