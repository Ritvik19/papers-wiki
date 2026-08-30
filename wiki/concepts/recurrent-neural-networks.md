# Recurrent Neural Networks

**Type**: concept  
**Tags**: #concept

## Overview

Recurrent neural networks (RNNs) process sequences by maintaining a hidden state updated at each time step, unfolding into a deep computational graph through time. Variants include bidirectional RNNs, encoder–decoder models, deep and recursive architectures, and gated units (LSTM, GRU) for long-term dependencies.

## Appearances

- [[Deep Learning]] — Chapter 10 covers unfolding, vanilla RNNs, sequence-to-sequence models, the long-term dependency problem, LSTM/GRU, and optimization tricks for long sequences.
- [[Recurrent Neural Networks: Building a Custom LSTM Cell]] — practitioner tutorial on time unrolling, BPTT, stacking cells in time and space, flexible I/O mappings, and RNN vs CNN receptive-field tradeoffs.
- [[Recurrent Neural Networks: Building GRU Cells VS LSTM Cells in PyTorch]] — when RNNs still beat transformers (long sequences, real-time control, small data, weakly supervised action recognition); GRU as compact gated variant.
- [[How Attention Works in Deep Learning: Understanding the Attention Mechanism in Sequence Models]] — seq2seq RNN bottleneck, vanishing gradients in stacked layers, and how attention augments encoder–decoder before transformers.
- [[Graph Neural Networks — An Overview]] — RNNs reinterpreted as GNNs on chained (sequential) graphs; recurrence preserves embeddings traveling node-to-node.

## Notes

Modern LLMs largely replaced vanilla RNN stacks with transformers, but RNN concepts (hidden state, BPTT, vanishing gradients, encoder–decoder) remain essential for understanding pre-transformer NLP and some efficient sequence models. The book's encoder–decoder treatment (Figure 10.12) foreshadows machine translation and dialogue architectures.

RNN cells use shared weights across timesteps: output at step \(t\) feeds the next input, giving memory over the sequence. Training unrolls the graph for [[Backpropagation Through Time]]; complexity is linear in sequence length. Stacking in **space** means feeding one cell's hidden output as the next layer's input at the same timestep.

Despite transformer dominance in NLP, gated RNNs ([[LSTM]], [[GRU]]) remain relevant for very long sequences, online/real-time control, limited training data, and weakly supervised video (e.g. with CTC loss). Hybrid RNN+GAN time-series models also persist in specialized domains.

## Related

- [[Attention Mechanism]]
- [[LSTM]]
- [[GRU]]
- [[Backpropagation Through Time]]
- [[Bidirectional RNN]]
- [[Encoder-Decoder Architecture]]
- [[Vanishing Gradients]]
- [[Deep Learning]]
- [[Large Language Models]]
- [[Back-Propagation]]
