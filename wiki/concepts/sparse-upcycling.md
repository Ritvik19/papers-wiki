# Sparse Upcycling

**Type**: concept  
**Tags**: #concept

## Overview
A model transformation technique developed by Google Research (Komatsuzaki et al., 2022) that initializes a sparsely activated Mixture-of-Experts (MoE) model by duplicating the MLP layers of a pretrained dense checkpoint, enabling compute-efficient sparse scaling.

## Appearances
- [[Papers Explained 599: Sparse Upcycling]] — foundational paper.
- [[Mixture of Experts]] — model scaling strategy.

## Notes
- Drastically reduces the compute required to train competitive MoE models compared to training sparse architectures from scratch.

## Related
- [[Mixture of Experts]]
- [[Model Compression and Efficiency]]
- [[Switch Transformers]]
