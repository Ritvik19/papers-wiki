# Graph Attention Networks

**Type**: concept  
**Tags**: #concept

## Overview

Graph Attention Networks (GATs; Veličković et al., arXiv:1710.10903) replace the fixed neighborhood weights of **[[Graph Convolutional Networks]]** with learned attention coefficients. For node \(i\), attention scores \(a_{ij} = \text{attention}(h_i, h_j)\) are softmax-normalized over neighbors \(j \in N_i\), yielding update \(h^{(l)}_i = \sigma(\sum_{j \in N_i} a_{ij} W h_j)\). Multi-head attention concatenates \(K\) independent attention heads.

## Appearances

- [[Best Graph Neural Network Architectures: GCN, GAT, MPNN and More]] — full survey: GCN coefficient \(c_{ij} = 1/\sqrt{|N_i||N_j|}\) vs learned \(a_{ij}\); Bahdanau additive attention; multi-head; scalability and edge-feature extensions; used inside Temporal Graph Networks.
- [[Graph Convolutional Networks]] — GAT generalizes GCN aggregation with data-dependent neighbor weights.
- [[Attention Mechanism]] — GAT applies attention to graph neighborhoods rather than sequence positions.

## Notes

**Key difference from GCN**: Attention coefficients depend on node representations, not only graph structure (degree matrix).

**Practical traits**: Computationally efficient; scalable; can incorporate edge features in extended variants.

## Related

- [[Graph Neural Networks]]
- [[Graph Convolutional Networks]]
- [[Message Passing Neural Networks]]
- [[Self-Attention]]
