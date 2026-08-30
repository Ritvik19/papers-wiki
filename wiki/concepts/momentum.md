# Momentum

**Type**: concept  
**Tags**: #concept

## Overview

Momentum accelerates gradient descent by accumulating a velocity vector in directions of persistent gradient sign, dampening oscillations in ravines and speeding progress along consistent directions. Nesterov momentum looks ahead before computing the gradient.

## Appearances

- [[Deep Learning]] — Chapter 8.3.2 covers classical momentum and Nesterov accelerated gradient as core deep-learning optimizers.

## Notes

Momentum helps navigate ill-conditioned loss landscapes common in deep nets. Modern practice often combines momentum ideas with adaptive per-parameter scaling (Adam).

## Related

- [[Gradient Descent]]
- [[Adam]]
- [[Deep Learning]]
