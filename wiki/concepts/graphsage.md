# GraphSAGE

**Type**: concept  
**Tags**: #concept

## Overview

GraphSAGE (Graph SAmple and aggreGatE; Hamilton et al., arXiv:1706.02216) trains inductive node representations on large graphs by **sampling** a fixed-size neighborhood subset at each layer instead of using all neighbors. Each layer: sample neighbors → aggregate sampled features with a **learnable aggregator** (mean, LSTM, or max-pooling) → combine with the node's current representation. Stacking layers grows the K-hop receptive field analogously to deeper CNNs.

## Appearances

- [[Best Graph Neural Network Architectures: GCN, GAT, MPNN and More]] — sampling pipeline; unsupervised (nearby nodes similar, distant nodes dissimilar) vs supervised training; learnable aggregators; PinSAGE as billion-scale extension.
- [[Message Passing Neural Networks]] — GraphSAGE is a scalable MPNN with neighborhood subsampling.
- [[Graph Neural Networks]] — primary inductive-learning architecture for large graphs.

## Notes

**Inductive**: Generalizes to unseen nodes/graphs at inference — unlike transductive GCN training on a fixed graph.

**PinSAGE** (Pinterest): GraphSAGE + random-walk neighborhood importance scores + importance-sampling aggregation on a 3B-node recommender graph.

## Related

- [[Graph Neural Networks]]
- [[Graph Convolutional Networks]]
- [[Message Passing Neural Networks]]
