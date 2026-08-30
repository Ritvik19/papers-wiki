# Multi-Head Attention

**Type**: concept  
**Tags**: #concept

## Overview

Multi-head attention runs several parallel self-attention operations ("heads") on different learned linear projections of queries, keys, and values. Each head attends in a lower-dimensional subspace (\(d_k = d_{model}/h\)); outputs are concatenated and projected back to \(d_{model}\). This lets the model jointly attend to information from different representation subspaces at different positions — a single head's averaging would inhibit this.

## Appearances

- [[How Transformers Work in Deep Learning and NLP: An Intuitive Introduction]] — parallel head implementation, \(h=8\), \(d_{model}=512\), \(d_k=64\); encoder/decoder/masked variants.
- [[Why Multi-Head Self Attention Works: Math, Intuitions and 10+1 Hidden Insights]] — Voita head types (positional/syntactic/rare-word) and ~2/3 encoder-head pruning; Cordonnier shared projections; Michel cross-attention pruning sensitivity; GPU parallelization per (batch, head).
- [[How Positional Embeddings Work in Self-Attention (Code in PyTorch)]] — PE shared across heads inside MHSA; absolute and relative bias added to \(QK^T\).
- [[Papers Explained 01 - Transformer]] — original multi-head attention definition.
- [[Papers Explained Review 09 - Attention Layers]] — scaled dot-product attention building block.
- [[A Visual Guide to Attention Variants in Modern LLMs]] — visual MHA baseline (OLMo 2/3, GPT-2) and comparison to GQA/MLA efficiency variants.

## Notes

\[
\text{MultiHead}(Q,K,V) = \text{Concat}(\text{head}_1, \ldots, \text{head}_h) W^O
\]
\[
\text{head}_i = \text{Attention}(Q W_i^Q, K W_i^K, V W_i^V)
\]

Heads are **independent and parallelizable** — key to transformer training speed on GPUs.

**Variants in the original architecture:**
- Encoder: full self-attention over input.
- Decoder: **masked** multi-head self-attention (causal; future tokens masked).
- Decoder: **encoder–decoder** multi-head attention (cross-attention; encoder output as K,V).

Intuition (Vaswani et al.): different heads capture different syntactic/positional/contextual relationships. Voita et al. (2019) empirically classify heads and show many are prunable; Cordonnier et al. (2020) find heads share overlapping subspaces despite independent computation; Michel et al. (2019) show cross-attention heads are least prunable.

## Related

- [[Self-Attention]]
- [[Attention Mechanism]]
- [[Positional Encoding]]
- [[Encoder-Decoder Architecture]]
- [[Papers Explained 01 - Transformer]]
