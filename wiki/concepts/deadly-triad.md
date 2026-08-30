# Deadly Triad

**Type**: concept  
**Tags**: #concept

## Overview

The **deadly triad** in reinforcement learning names three ingredients that together can cause instability and divergence in value learning: (1) **function approximation**, (2) **bootstrapping** (TD-style updates), and (3) **off-policy training**. Any two are usually safe; all three together require careful algorithms (e.g., gradient TD, emphatic TD).

Sutton & Barto illustrate divergence on Baird’s counterexample (Chapter 11).

## Appearances

- [[Reinforcement Learning: An Introduction]] — Chapter 11; TDC, GTD, Emphatic-TD.

## Notes

LLM RL often stays on-policy partly to avoid the worst triad interactions, though large neural policies still face related optimization instabilities (see [[GRPO++: Tricks for Making RL Actually Work]]).

## Related

- [[Function Approximation in RL]]
- [[Off-Policy Learning]]
- [[Temporal-Difference Learning]]
- [[Reinforcement Learning: An Introduction]]
