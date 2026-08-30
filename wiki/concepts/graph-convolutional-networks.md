# Graph Convolutional Networks

**Type**: concept  
**Tags**: #concept

## Overview

Graph Convolutional Networks (GCNs) implement graph convolutions via multiplication by a graph operator — typically the normalized graph Laplacian with self-loops. The canonical 1-hop layer (Kipf & Welling, arXiv:1609.02907) is \(Y = D^{-1/2}(A+I)D^{-1/2} X W\), which aggregates each node's direct neighbors before a learned linear transform. Higher-order spectral filters (Defferrard et al.) use Chebyshev polynomial expansions of the Laplacian to reach K-hop neighborhoods without explicit eigendecomposition.

## Appearances

- [[Best Graph Neural Network Architectures: GCN, GAT, MPNN and More]] — GCN as K=1 ChebNet simplification (Kipf & Welling): self-loops, renormalized \(\tilde{D}^{-1/2}\tilde{A}\tilde{D}^{-1/2}\), most cited GNN paper; limitations vs MPNN/GAT (no edge features, fixed coefficients).
- [[How Graph Neural Networks (GNN) Work: Introduction to Graph Convolutions from Scratch]] — defines GCN from spectral convolution principle; implements `GCN_AISUMMER` in PyTorch; trains 3-layer GCN on MUTAG with mean readout (~82% val accuracy).
- [[Graph Laplacian]] — normalized Laplacian is the operator used in GCN layers.
- [[Graph Neural Networks]] — GCN is the introductory GNN architecture in the AI Summer tutorial series.

## Notes

**Principle**: Convolution in the vertex domain equals multiplication in the graph spectral domain. Multiplying a graph operator by a signal computes a weighted sum over each node's neighborhood.

**Receptive field**: \(L^K\) (or K-term Chebyshev expansion) aggregates information from nodes up to K hops away — analogous to increasing CNN kernel size.

**Self-loops**: Adding identity to \(A\) before degree normalization stabilizes training (modified normalized Laplacian).

## Related

- [[Graph Neural Networks]]
- [[Graph Attention Networks]]
- [[Graph Laplacian]]
- [[Convolution]]
