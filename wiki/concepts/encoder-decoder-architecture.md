# Encoder-Decoder Architecture

**Type**: concept  
**Tags**: #concept

## Overview

Encoder–decoder (sequence-to-sequence) models map a variable-length input sequence to a fixed or variable-length output via an encoder that compresses input context and a decoder that generates outputs step by step. Attention mechanisms later augmented this design.

## Appearances

- [[Deep Learning]] — Sections 10.4 and 10.12 (Figure 10.12) present encoder–decoder RNNs for machine translation and structured prediction.
- [[How Attention Works in Deep Learning: Understanding the Attention Mechanism in Sequence Models]] — vanilla seq2seq bottleneck (fixed context vector \(z\)) and how [[Attention Mechanism|attention]] lets the decoder query all encoder states dynamically.
- [[How Transformers Work in Deep Learning and NLP: An Intuitive Introduction]] — transformer decoder cross-attention: encoder output supplies K/V, decoder state supplies Q for input–output alignment.

## Notes

Transformers retain encoder–decoder structure (e.g. T5, original "Attention is All You Need") but replace recurrence with self-attention. The book's treatment is the direct precursor to modern seq2seq LLM APIs.

## Related

- [[Attention Mechanism]]
- [[Self-Attention]]
- [[Recurrent Neural Networks]]
- [[LSTM]]
- [[Large Language Models]]
- [[Deep Learning]]
