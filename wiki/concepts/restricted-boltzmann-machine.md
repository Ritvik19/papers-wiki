# Restricted Boltzmann Machine

**Type**: concept  
**Tags**: #concept

## Overview

A restricted Boltzmann machine (RBM) is a bipartite undirected model with visible and hidden units, no connections within layers. Training maximizes log-likelihood via approximations like [[Contrastive Divergence]].

## Appearances

- [[Deep Learning]] — Chapter 20.2 (Figure 20.1); building block for deep belief nets and historical deep learning stacks.

## Notes

RBMs enabled layer-wise pretraining before end-to-end CNN training dominated. Inference on hiddens given visibles is tractable due to bipartite structure.

## Related

- [[Deep Belief Networks]]
- [[Contrastive Divergence]]
- [[Undirected Graphical Models]]
- [[Deep Learning]]
