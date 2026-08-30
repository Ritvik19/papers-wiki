# Graph Laplacian

**Type**: concept  
**Tags**: #concept

## Overview

The graph Laplacian \(L = D - A\) is the fundamental linear operator on graphs, where \(D\) is the diagonal degree matrix and \(A\) is the adjacency matrix. Off-diagonal entries are \(-1\) for connected node pairs and \(0\) otherwise; diagonal entries equal node degree. The normalized Laplacian \(L_{\text{norm}} = D^{-1/2} L D^{-1/2} = I - D^{-1/2} A D^{-1/2}\) (with self-loops: \(D^{-1/2}(A+I)D^{-1/2}\)) stabilizes gradient-based learning when node degrees vary widely.

## Appearances

- [[How Graph Neural Networks (GNN) Work: Introduction to Graph Convolutions from Scratch]] — full derivation, PyTorch implementations, eigenvalue interpretation (connected components), spectral image segmentation, and use as the GCN aggregation operator.
- [[Graph Convolutional Networks]] — GCN layers multiply features by the normalized Laplacian.
- [[In-layer Normalization Techniques for Training Very Deep Neural Networks]] — cited analogy: varying node degrees cause the same instability that normalization addresses in deep nets.

## Notes

**Spectral properties**: The multiplicity of eigenvalue 0 equals the number of connected components. Smallest non-zero eigenvalues support spectral clustering/segmentation.

**Chebyshev approximation**: Defferrard et al. expand filters as polynomials of a rescaled Laplacian \(\tilde{L}_h = \frac{2}{\lambda_{\max}} L_{\text{norm}} - I\), avoiding costly SVD while controlling K-hop receptive fields.

## Related

- [[Graph Convolutional Networks]]
- [[Graph Neural Networks]]
- [[Singular Value Decomposition]]
