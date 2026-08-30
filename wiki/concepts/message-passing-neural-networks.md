# Message Passing Neural Networks

**Type**: concept  
**Tags**: #concept

## Overview

Message Passing Neural Networks (MPNNs; Gilmer et al., arXiv:1704.01212) formalize spatial **[[Graph Neural Networks]]** as three steps: (1) **message** \(m_{ij} = f_e(h_i, h_j, e_{ij})\) computed on each edge by message function \(f_e\) (typically an MLP); (2) **aggregate** incoming messages with a permutation-invariant function (e.g. sum); (3) **update** \(h_i = f_v(h_i, \sum_{j \in N_i} m_{ji})\) via update function \(f_v\). MPNN is a unifying framework — GCN, GAT, and GraphSAGE are specific instantiations with different \(f_e\), aggregators, and \(f_v\).

## Appearances

- [[Best Graph Neural Network Architectures: GCN, GAT, MPNN and More]] — defines MPNN message/aggregate/update; notes scalability limits from storing edge messages; TGN uses MPNN-style memory updates.
- [[Graph Attention Networks]] — GAT is an MPNN variant with attention-weighted messages.
- [[GraphSAGE]] — sampling-based MPNN for large inductive graphs.

## Notes

**Strength**: Most generic spatial GNN template; supports edge features natively via \(e_{ij}\) in \(f_e\).

**Weakness**: Requires storing and processing messages on all edges — memory-intensive for very large graphs.

## Related

- [[Graph Neural Networks]]
- [[Graph Convolutional Networks]]
- [[Graph Attention Networks]]
- [[GraphSAGE]]
