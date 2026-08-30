# Positional Encoding

**Type**: concept  
**Tags**: #concept

## Overview

Positional encodings inject **order information** into transformer inputs. Because self-attention treats tokens as an unordered set, position must be encoded explicitly — typically by adding position-dependent vectors to word embeddings before the first attention layer. The original Transformer (Vaswani et al. 2017) uses **fixed sinusoidal** functions. Distinct from trainable [[Positional Embeddings]] (learned vectors, often inside MHSA); modern models also use rotary (RoPE) and ALiBi schemes.

## Appearances

- [[How Transformers Work in Deep Learning and NLP: An Intuitive Introduction]] — sinusoidal PE formulas; explains permutation invariance without PE and contrast with RNN implicit ordering.
- [[How Positional Embeddings Work in Self-Attention (Code in PyTorch)]] — clarifies encodings (fixed sinusoidal) vs embeddings (trainable); why input-only PE is insufficient for vision.
- [[Papers Explained Review 06 - Position Encodings]] — survey of position-encoding methods in the Papers Explained corpus.
- [[Papers Explained 01 - Transformer]] — original sinusoidal encoding in "Attention Is All You Need."

## Notes

**Sinusoidal PE** (original paper, \(d_{model}=512\)):

\[
PE_{(pos, 2i)} = \sin\left(\frac{pos}{10000^{2i/d_{model}}}\right), \quad
PE_{(pos, 2i+1)} = \cos\left(\frac{pos}{10000^{2i/d_{model}}}\right)
\]

Same word at different positions gets different final representations. Sinusoids allow extrapolation to unseen sequence lengths and provide unique encodings per position/dimension.

Without positional signal, transformers are **permutation invariant** — order of tokens would not affect output (modulo identical embeddings).

## HF Blog Cross-References

- [You could have designed state of the art positional encoding](https://huggingface.co/blog/designing-positional-encoding) (2024-11-25) — a first-principles derivation that motivates RoPE from scratch: starts from integer and binary position encodings, works through sinusoidal PE and the absolute-vs-relative distinction, then arrives at Rotary Positional Encoding (used in Llama 3.2 and most modern transformers) and its extension to n-dimensional inputs.

## Related

- [[Positional Embeddings]]
- [[Self-Attention]]
- [[Word Embedding]]
- [[Multi-Head Attention]]
- [[Papers Explained Review 06 - Position Encodings]]
- [[How Transformers Work in Deep Learning and NLP: An Intuitive Introduction]]
