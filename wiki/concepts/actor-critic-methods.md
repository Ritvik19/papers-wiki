# Actor-Critic Methods

**Type**: concept  
**Tags**: #concept

## Overview

Actor–critic methods combine **policy gradient** (the actor: updates policy parameters to increase expected return) with a **value function** (the critic: estimates state or state–action values to reduce variance). The critic provides a baseline or advantage estimate so policy updates are less noisy than raw [[REINFORCE]]. Sutton & Barto present one-step actor–critic, advantage actor–critic, and connections to neuroscience (Chapter 13; Chapter 15.5).

## Appearances

- [[Reinforcement Learning: An Introduction]] — Chapter 13; TD-Gammon and AlphaGo use value networks as critics in deep RL (Chapter 16).
- [[Unravel Policy Gradients and REINFORCE]] — AI Summer positions actor–critic as the remedy for REINFORCE's high-variance, hard-to-stabilize updates (cliffhanger to TRPO/PPO series).
- [[The Idea behind Actor-Critics and How A2C and A3C Improve Them]] — AI Summer architecture primer: actor/critic split, per-step TD updates, [[Advantage Actor-Critic]], [[Asynchronous Advantage Actor-Critic]].

## Notes

Modern LLM RL (PPO, [[GRPO]]) is actor–critic–like: a policy is optimized using advantage estimates, though the “critic” may be a learned value model, group-relative baselines, or reward model rather than a classical v(s) table.

## Related

- [[Policy Gradient]]
- [[REINFORCE]]
- [[Advantage Actor-Critic]]
- [[Asynchronous Advantage Actor-Critic]]
- [[Proximal Policy Optimization]]
- [[Temporal-Difference Learning]]
- [[Function Approximation in RL]]
- [[Reinforcement Learning: An Introduction]]
