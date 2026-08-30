# Graph Neural Networks

**Type**: concept  
**Tags**: #concept

## Overview

Graph Neural Networks (GNNs) are neural architectures that operate on graph-structured data by repeatedly transforming node features while respecting connectivity. A graph is defined by an adjacency matrix \(A \in \mathbb{R}^{N \times N}\) (structure) and node features \(X \in \mathbb{R}^{N \times F}\) (signal). GNN layers aggregate information from each node's neighborhood — generalizing [[Convolutional Neural Networks|CNN]] locality to irregular topologies.

## Appearances

- [[Graph Neural Networks — An Overview]] — earliest AI Summer GNN primer (2020): RNNs as GNNs on chained graphs; node=RNN, edge=NN, synchronous message passing until global mixing; sum readout for graph embedding.
- [[Best Graph Neural Network Architectures: GCN, GAT, MPNN and More]] — architecture survey: spectral (Spectral Nets, ChebNets, GCN), spatial (MPNN, GAT), sampling (GraphSAGE, PinSAGE), dynamic (TGN); node/edge/graph task readouts.
- [[How Graph Neural Networks (GNN) Work: Introduction to Graph Convolutions from Scratch]] — full primer: structure/signal decomposition, Laplacian math, inductive vs transductive tasks, spectral and 1-hop GCN layers, MUTAG training, batching and readout.
- [[Self-Attention]] — Adaloglou notes self-attention applies beyond NLP to vision, healthcare, and GNNs.
- [[How Attention Works in Deep Learning: Understanding the Attention Mechanism in Sequence Models]] — attention generalizes to GNNs as one instantiation of relational modeling.

## Notes

**Task types**: *Graph classification* (inductive) assigns one label per graph; *node classification* (transductive) predicts labels for unlabeled nodes on a single large graph using few labeled examples.

**Practical stack**: PyTorch Geometric for production GNN training; block-diagonal adjacency batches variable-size graphs; readout layers (mean/max) produce graph-level embeddings from node embeddings.

## Related

- [[Graph Convolutional Networks]]
- [[Graph Attention Networks]]
- [[Message Passing Neural Networks]]
- [[GraphSAGE]]
- [[Graph Laplacian]]
- [[Convolutional Neural Networks]]
