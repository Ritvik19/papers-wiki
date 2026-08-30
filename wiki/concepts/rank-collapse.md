# Rank Collapse

**Type**: concept  
**Tags**: #concept

## Overview

Rank collapse is the tendency of deep self-attention stacks to converge representations toward a low-rank (often rank-1) subspace, causing token outputs to become nearly uniform. Dong et al. (2021, "Attention is Not All You Need") showed pure attention without auxiliary components degenerates exponentially with depth. Standard transformer blocks mitigate this via [[Skip Connections]] and the MLP sublayer; layer normalization alone does not prevent collapse.

## Appearances

- [[Why Multi-Head Self Attention Works: Math, Intuitions and 10+1 Hidden Insights]] — Insight 7: pure attention → rank-1 exponentially; skip connections and MLP counteract; LN ineffective for collapse prevention.
- [[Skip Connections]] — residual paths prevent transformer output from degenerating to rank one across depth.

## Notes

Distinct from but related to the observation that **post-softmax attention matrices** \(P = \text{softmax}(QK^T/\sqrt{d_k})\) are low-rank (Linformer, Wang et al. 2020) — that concerns the attention weight matrix, not necessarily token representation collapse.

## Related

- [[Self-Attention]]
- [[Multi-Head Attention]]
- [[Skip Connections]]
- [[How Transformers Work in Deep Learning and NLP: An Intuitive Introduction]]
