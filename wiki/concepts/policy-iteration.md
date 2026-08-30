# Policy Iteration

**Type**: concept  
**Tags**: #concept

## Overview

Policy iteration is a [[Dynamic Programming]] method that alternates between **policy evaluation** (computing v_π for the current policy) and **policy improvement** (making the policy greedy with respect to the current value function). It converges to an optimal policy in finite MDPs, often in few iterations. Generalized policy iteration (GPI) describes the ongoing interaction of evaluation and improvement in many RL algorithms.

## Appearances

- [[Reinforcement Learning: An Introduction]] — Chapter 4; gridworld, Jack’s car rental.

## Notes

Actor–critic and many practical RL loops are approximate GPI: a critic estimates values while an actor improves the policy.

## Related

- [[Dynamic Programming]]
- [[Value Iteration]]
- [[Actor-Critic Methods]]
- [[Reinforcement Learning: An Introduction]]
