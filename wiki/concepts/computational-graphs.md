# Computational Graphs

**Type**: concept  
**Tags**: #concept

## Overview

A computational graph represents a differentiable program as a directed acyclic graph of operations; [[Back-Propagation]] traverses it in reverse to compute gradients. Modern frameworks build graphs dynamically (PyTorch) or statically (TensorFlow 1.x).

## Appearances

- [[Deep Learning]] — Figures 1.3 and 6.10; Chapter 6.5 formalizes symbol-to-symbol differentiation over graphs.

## Notes

Enables modular composition of layers, automatic differentiation, and efficient memory use (checkpointing trades compute for memory on long graphs).

## Related

- [[Back-Propagation]]
- [[Feedforward Neural Networks]]
- [[Deep Learning]]
