# Positional Embeddings

**Type**: concept  
**Tags**: #concept

## Overview

Positional embeddings are **trainable** vectors that encode token position in transformer models, distinct from fixed sinusoidal [[Positional Encoding]]. They can be added to input embeddings or — more powerfully for vision — injected **inside** multi-head self-attention to re-enforce order at every layer. Variants include absolute (per-position index) and relative (token–token distance) embeddings.

## Appearances

- [[How Positional Embeddings Work in Self-Attention (Code in PyTorch)]] — encodings vs embeddings distinction; absolute PE (\(QR\) bias); relative PE with \(2n{-}1\) distance buckets; 2D factorized PE for vision; PyTorch/einsum implementations.
- [[How Transformers Work in Deep Learning and NLP: An Intuitive Introduction]] — contrasts with fixed sinusoidal input encodings.
- [[How the Vision Transformer (ViT) Works in 10 Minutes: An Image Is Worth 16×16 Words]] — trainable absolute PE on patch tokens; 2D structure after training; 2D interpolation for higher-resolution fine-tuning.

## Notes

**Absolute PE**: trainable \(R \in \mathbb{R}^{n \times d}\); attention bias \(\text{softmax}((QK^T + QR)/\sqrt{d})\).

**Relative PE** (Shaw et al. 2018): encode relative distances \(d(i,j)\) with \(R_{rel} \in \mathbb{R}^{(2n-1) \times d}\); provides translation equivariance. Requires `relative_to_absolute` indexing to map to \(n \times n\) bias.

**2D relative PE** (Ramachandran et al. 2019): for \(h \times w\) image tokens, separate row and column offset embeddings summed after expansion.

Shared PE across attention heads reduces memory from \(O(h n^2 d)\) to \(O(n^2 d)\).

## Related

- [[Positional Encoding]]
- [[Self-Attention]]
- [[Multi-Head Attention]]
- [[Papers Explained Review 06 - Position Encodings]]
- [[Computer Vision]]
