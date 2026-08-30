# Function Approximation in RL

**Type**: concept  
**Tags**: #concept

## Overview

Function approximation in RL replaces tabular value functions with parameterized estimates—linear features, tile coding, Fourier bases, neural networks—so learning scales to large or continuous state spaces. Sutton & Barto cover semi-gradient methods, feature design (coarse coding, tile coding), and deep networks for value and policy approximation (Chapters 9–10, 11).

Combining function approximation with bootstrapping and off-policy learning can cause instability—the **deadly triad** (Chapter 11).

## Appearances

- [[Reinforcement Learning: An Introduction]] — Chapters 9–11; Mountain Car, Baird’s counterexample; convolutional networks (Figure 9.15).

## Notes

Deep RL (DQN, AlphaGo) is function approximation at scale. LLM post-training uses the same idea: the “value” or “policy” is a billion-parameter network updated by TD-style or policy-gradient objectives.

## Related

- [[Deadly Triad]]
- [[Policy Gradient]]
- [[Temporal-Difference Learning]]
- [[Reinforcement Learning: An Introduction]]
