# Stochastic Gradient Descent

**Type**: concept  
**Tags**: #concept

## Overview

Stochastic gradient descent (SGD) estimates the gradient of a training objective using a minibatch of examples rather than the full dataset, enabling scalable learning on large data. Each update uses noisy but unbiased gradient estimates, trading variance for computational efficiency.

## Appearances

- [[Deep Learning]] — Section 5.9 introduces SGD; Chapter 8 connects it to momentum, adaptive methods, and practical minibatch sizing for deep nets.

## Notes

SGD remains the default outer loop for deep learning even when per-parameter adaptive methods (Adam) modify the effective step sizes. Learning rate, batch size, and gradient noise interact with generalization.

## Related

- [[Gradient Descent]]
- [[Adam]]
- [[Deep Learning]]
