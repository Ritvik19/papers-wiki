# Vanishing Gradients

**Type**: concept  
**Tags**: #concept

## Overview

Vanishing gradients occur when back-propagated signals shrink exponentially across layers or time steps, slowing or preventing learning in deep or recurrent networks. Saturating activations (sigmoid, tanh) and long RNN unrolls are common causes.

## Appearances

- [[Deep Learning]] — Discussed in Chapters 6, 8, and 10; motivates [[LSTM]], [[GRU]], ReLU, careful [[Weight Initialization]], and gradient clipping.
- [[Best Deep CNN Architectures and Their Principles: from AlexNet to EfficientNet]] — ResNet skip connections and batch norm; Inception auxiliary classifiers as mitigations for deep CNN training.
- [[Recurrent Neural Networks: Building a Custom LSTM Cell]] — long BPTT unrolls exacerbate vanishing gradients; LSTM gating is the article's primary mitigation for long-term dependencies.
- [[How Attention Works in Deep Learning: Understanding the Attention Mechanism in Sequence Models]] — stacked RNN encoder–decoder layers suffer vanishing gradients; attention provides direct encoder–decoder paths that partially mitigate the problem.
- [[How to Generate Images using Autoencoders]] — plain autoencoders share the vanishing-gradient problem with other deep networks.

## Notes

Exploding gradients are the dual problem (handled by clipping). [[Skip Connections]] and [[Batch Normalization]] (post-book) further address depth in CNNs; transformers use residual paths and layer norm.

## Related

- [[Back-Propagation]]
- [[LSTM]]
- [[Activation Functions]]
- [[Deep Learning]]
