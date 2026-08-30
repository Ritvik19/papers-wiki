# REINFORCE

**Type**: concept  
**Tags**: #concept

## Overview

REINFORCE is a Monte Carlo **policy gradient** algorithm: it updates policy parameters in the direction that increases the log-probability of actions, weighted by the **return** G_t from each episode (or trajectory segment). It is the simplest policy-gradient method and illustrates the core idea that policy parameters should move to make high-return action sequences more likely.

Adding a learned **baseline** (value function) to the return reduces variance without biasing the gradient—leading to actor–critic methods (Sutton & Barto, Chapter 13).

## Appearances

- [[Reinforcement Learning: An Introduction]] — Sections 13.3–13.4; short-corridor gridworld example.
- [[Unravel Policy Gradients and REINFORCE]] — AI Summer CartPole Keras demo: discounted returns, mean/std normalization, softmax policy network updated per episode.

## Notes

REINFORCE requires complete episodes (or segments) before updating; actor–critic allows stepwise updates. LLM RL optimizers (PPO, GRPO) are descendants with clipping, importance sampling, and batched advantage estimation.

## Related

- [[Policy Gradient]]
- [[Actor-Critic Methods]]
- [[Monte Carlo Methods]]
- [[Reinforcement Learning: An Introduction]]
