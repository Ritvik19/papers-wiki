# Feedforward Neural Networks

**Type**: concept  
**Tags**: #concept

## Overview

Feedforward neural networks (multilayer perceptrons) map an input through a stack of hidden layers to an output without cycles. Each layer applies an affine transform followed by a nonlinear activation (ReLU, sigmoid, tanh, etc.). They are the universal building block for deep learning before adding convolutions or recurrence.

## Appearances

- [[Deep Learning]] — Chapter 6 covers XOR as a representation-learning example, hidden-unit design, architecture depth/width tradeoffs, and gradient-based learning with back-propagation.

## Notes

The book emphasizes that depth enables **compositional representations**—each layer reuses features from the previous layer—while shallow networks may need exponentially more units for the same function class. Universal approximation theorems are discussed with caveats about optimization and data.

## Related

- [[Back-Propagation]]
- [[Dropout]]
- [[Deep Learning]]
