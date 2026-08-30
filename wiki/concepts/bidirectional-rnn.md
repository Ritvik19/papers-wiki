# Bidirectional RNN

**Type**: concept  
**Tags**: #concept

## Overview

A bidirectional RNN processes a sequence in both forward and backward directions, concatenating (or combining) hidden states so each position can depend on past and future context. Essential for tagging and encoding tasks before transformers.

## Appearances

- [[Deep Learning]] — Section 10.3; widely used in early NLP encoders (e.g. BiLSTM for ELMo-era models).
- [[Recurrent Neural Networks: Building a Custom LSTM Cell]] — bidirectional LSTM doubles parameters; forward and backward hidden states are concatenated; reverse-time context only helps when the task benefits from it.

## Notes

Setting `bidirectional=True` in PyTorch runs two LSTMs (forward and backward) over the same input; outputs are concatenated along the feature dimension, doubling hidden size and parameter count.

## Related

- [[Recurrent Neural Networks]]
- [[LSTM]]
- [[Encoder-Decoder Architecture]]
- [[Deep Learning]]
