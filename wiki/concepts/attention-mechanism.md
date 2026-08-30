# Attention Mechanism

**Type**: concept  
**Tags**: #concept

## Overview

Attention lets a model dynamically weight which parts of an input sequence (or image regions) to use when producing each output. In seq2seq models, it replaces a single fixed context vector with a weighted sum over all encoder hidden states, solving the **bottleneck** where long inputs are poorly compressed. Attention weights act as **memory through time** (Alex Graves). The mechanism generalizes beyond RNNs to vision, recommenders, and graph models.

## Appearances

- [[How Attention Works in Deep Learning: Understanding the Attention Mechanism in Sequence Models]] — full taxonomy (implicit/explicit, soft/hard, global/local), Bahdanau encoder–decoder equations, score-function survey, and applications beyond NLP.
- [[How Transformers Work in Deep Learning and NLP: An Intuitive Introduction]] — scales attention to full transformer: scaled dot-product self-attention, multi-head, masked and cross-attention.
- [[Why Multi-Head Self Attention Works: Math, Intuitions and 10+1 Hidden Insights]] — why multi-head self-attention works: matmul decomposition, asymmetry, head specialization, efficient variants.
- [[Encoder-Decoder Architecture]] — attention first gained prominence augmenting RNN seq2seq for machine translation.

## Notes

**Taxonomy** (from Adaloglou 2020):
- *Implicit*: deep nets naturally emphasize salient inputs without explicit modules.
- *Explicit*: trainable weighting over inputs; standard "attention" in literature.
- *Soft*: differentiable continuous weights (softmax); end-to-end backprop.
- *Hard*: discrete stochastic selection; requires REINFORCE/policy gradients; high variance.
- *Global*: attend over full sequence (\(O(T^2)\) cost).
- *Local*: attend over a window or subset for long sequences.

**Bahdanau seq2seq attention**: scores \(e_{ij} = \text{attention\_net}(y_{i-1}, h_j)\); \(\alpha_{ij} = \text{softmax}_j(e_{ij})\); context \(z_i = \sum_j \alpha_{ij} h_j\). Additive (Bahdanau) score \(v_a^T \tanh(W_a[h; y_{i-1}])\) proved most durable; dot-product and cosine variants also used.

Attention provides direct encoder–decoder paths analogous to [[Skip Connections]], easing [[Vanishing Gradients]] and yielding interpretable alignment heatmaps.

## Related

- [[Self-Attention]]
- [[Encoder-Decoder Architecture]]
- [[Recurrent Neural Networks]]
- [[Skip Connections]]
- [[Vanishing Gradients]]
- [[Large Language Models]]
- [[Papers Explained Review 09 - Attention Layers]]
