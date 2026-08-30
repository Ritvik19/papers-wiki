# Gradient Descent

**Type**: concept  
**Tags**: #concept

## Overview

Gradient descent iteratively moves parameters in the direction of steepest descent of a loss function, using the negative gradient. For differentiable models (including neural networks), it is the core optimization paradigm when combined with [[Back-Propagation]].

## Appearances

- [[Deep Learning]] — Chapter 4.3 (numerical computation) and Chapter 8 (optimization for deep models) cover gradient-based methods, saddle points, and ill-conditioning.

## Notes

Deep networks have non-convex objectives; gradient descent may converge to local minima, saddle points, or flat regions rather than global optima. The book discusses curvature, conditioning, and why naive gradient descent struggles without momentum or adaptive scaling.

## Related

- [[Stochastic Gradient Descent]]
- [[Momentum]]
- [[Back-Propagation]]
- [[Deep Learning]]
