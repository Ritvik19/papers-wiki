# Back-Propagation

**Type**: concept  
**Tags**: #concept

## Overview

Back-propagation is the reverse-mode automatic differentiation algorithm for computing gradients of a scalar loss with respect to all parameters in a feedforward (or general differentiable) computational graph. It applies the chain rule layer by layer, reusing intermediate activations stored during the forward pass.

## Appearances

- [[Deep Learning]] — Chapter 6.5 gives the full treatment: symbolic vs numeric differentiation, computational graphs, vector-Jacobian products, and connections to general AD frameworks.

## Notes

The book distinguishes **symbol-to-symbol** (build a graph, then evaluate derivatives) from **symbol-to-number** (numerical finite differences) approaches. Modern frameworks (PyTorch, JAX) implement the same idea with dynamic graphs. Vanishing/exploding gradients in deep chains motivate initialization, normalization, and architectural choices covered in Chapters 8 and 10.

## Related

- [[Computational Graphs]]
- [[Vanishing Gradients]]
- [[Feedforward Neural Networks]]
- [[Deep Learning]]
- [[Recurrent Neural Networks]]
