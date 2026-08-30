# Sarsa

**Type**: concept  
**Tags**: #concept

## Overview

Sarsa (State–Action–Reward–State–Action) is an **on-policy** temporal-difference control algorithm. It updates the action-value function Q toward the TD target R_{t+1} + γ Q(S_{t+1}, A_{t+1}), using the **actual next action** taken under the current policy (including exploration). Sarsa accounts for how exploratory actions affect future value—important in cliff-walking and other safety-sensitive tasks where [[Q-learning]]’s off-policy max can be overly optimistic.

## Appearances

- [[Reinforcement Learning: An Introduction]] — Section 6.4; cliff-walking comparison with Q-learning and Expected Sarsa.

## Notes

Expected Sarsa reduces variance by using the expectation over next actions instead of a single sample. n-step Sarsa extends the algorithm (Chapter 7).

## Related

- [[Q-learning]]
- [[Temporal-Difference Learning]]
- [[On-Policy Learning]]
- [[Reinforcement Learning: An Introduction]]
- [[n-Step Methods]]
