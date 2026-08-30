# Monte Carlo Methods

**Type**: concept  
**Tags**: #concept

## Overview

Monte Carlo (MC) methods in RL learn value functions and policies from **sampled complete returns**—the sum of rewards from a state (or state–action pair) until episode termination. Unlike [[Temporal-Difference Learning]], MC does not bootstrap from successor estimates; each update uses an actual observed return G_t. MC requires episodes to have well-defined endings (or use discounting in continuing tasks with care).

Sutton & Barto cover MC prediction, MC control (exploring starts, ε-soft policies), off-policy MC via [[Importance Sampling]], and incremental implementation (Chapter 5).

## Appearances

- [[Reinforcement Learning: An Introduction]] — Chapter 5; blackjack example, racetrack control, weighted vs ordinary importance sampling.

## Notes

MC has higher variance than TD for a given amount of data but is unbiased. MC methods underpin many evaluation protocols and appear in planning (rollouts) and modern RL (Monte Carlo tree search in AlphaGo, Chapter 16).

## Related

- [[Temporal-Difference Learning]]
- [[Importance Sampling]]
- [[Off-Policy Learning]]
- [[Reinforcement Learning: An Introduction]]
- [[Eligibility Traces]]
