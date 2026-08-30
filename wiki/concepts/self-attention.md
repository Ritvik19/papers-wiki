# Self-Attention

**Type**: concept  
**Tags**: #concept

## Overview

Self-attention computes attention scores **within a single sequence** — each token attends to all others (including itself) rather than aligning separate encoder and decoder sequences. Formally, \(\text{self-attention}(x, x)\) produces contextualized representations before any cross-sequence mapping. It is the core building block of transformer architectures and can be viewed as a fully connected weighted graph over tokens.

## Appearances

- [[How Attention Works in Deep Learning: Understanding the Attention Mechanism in Sequence Models]] — introduced as the transformer key component; graph interpretation (symmetric in undirected view).
- [[How Transformers Work in Deep Learning and NLP: An Intuitive Introduction]] — scaled dot-product formula \(\text{Attention}(Q,K,V)=\text{softmax}(QK^T/\sqrt{d_k})V\); Q/K/V database analogy; fast vs slow weights.
- [[Why Multi-Head Self Attention Works: Math, Intuitions and 10+1 Hidden Insights]] — two-matmul decomposition; self-attention is **not symmetric** (\(W_Q \neq W_K\)); directed-graph view; fast-weight memory interpretation; post-softmax low-rank structure; rank collapse without skip/MLP.
- [[How Positional Embeddings Work in Self-Attention (Code in PyTorch)]] — MHSA is permutation equivariant without position; absolute and relative PE injected into attention scores.
- [[How the Vision Transformer (ViT) Works in 10 Minutes: An Image Is Worth 16×16 Words]] — ViT applies standard encoder self-attention on image patch tokens; mean attention distance analysis vs conv receptive fields.
- [[An Overview of Classifier-Free Guidance for Diffusion Models]] — U-Net self-attention preserves structure vs cross-attention for text binding; spatial CFG from attention maps.
- [[An Overview of Classifier-Free Diffusion Guidance: Impaired Model Guidance with a Bad Version of Itself (Part 2)]] — SAG blurs high-attention patches; PAG replaces self-attention maps with identity.
- [[Papers Explained 01 - Transformer]] — scaled dot-product multi-head self-attention replaces RNN recurrence.
- [[Papers Explained Review 09 - Attention Layers]] — scaled dot-product attention mechanism in the Papers Explained corpus.
- [[Understanding and Coding the KV Cache in LLMs from Scratch]] — diagrams of K/V projection and why recomputing them each decode step is wasteful; motivates [[KV Cache]].
- [[A Visual Guide to Attention Variants in Modern LLMs]] — compressed visual recap of causal masked self-attention, Q/K/V pipeline, and transition to multi-head attention.

## Notes

Unlike encoder–decoder (cross) attention, self-attention mixes information along one sequence. In transformers, queries, keys, and values are linear projections of the same input; multi-head variants run parallel attention subspaces. Cost is \(O(n^2)\) in sequence length unless sparsified (e.g. [[Papers Explained 38 - Longformer]], [[Papers Explained 122 - Sparse Transformer]]).

Adaloglou (2020) notes self-attention generalizes beyond NLP to vision (ViT), healthcare, and graph neural networks. Adaloglou (2021) emphasizes that despite shared input \(X\), \(QK^T \neq KQ^T\) unless projection matrices are tied; attention routes information rather than merely selecting subspaces (Schlag et al.).

## Related

- [[Rank Collapse]]
- [[Multi-Head Attention]]
- [[Positional Encoding]]
- [[Attention Mechanism]]
- [[Encoder-Decoder Architecture]]
- [[Large Language Models]]
- [[KV Cache]]
- [[Papers Explained 01 - Transformer]]
