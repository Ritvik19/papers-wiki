# Vision Transformer

**Type**: concept  
**Tags**: #concept

## Overview

The Vision Transformer (ViT; Dosovitskiy et al., 2020) applies a **standard transformer encoder** to image classification by treating non-overlapping image patches as token sequences. Each \(P \times P\) patch is flattened and linearly projected to dimension \(D\); trainable [[Positional Embeddings]] restore spatial order; a prepended **[CLS] token** aggregates the sequence for an MLP classification head. ViT lacks CNN inductive biases (locality, translation equivariance) and typically requires **large-scale pretraining** (14M+ images) to outperform [[ResNet]] or [[EfficientNet]] on downstream tasks.

## Appearances

- [[How the Vision Transformer (ViT) Works in 10 Minutes: An Image Is Worth 16×16 Words]] — concise tutorial: patch tokenization, einops reshaping, data-scale requirements, fine-tuning with resolution interpolation, attention-distance analysis, PyTorch implementation.
- [[How Transformers Work in Deep Learning and NLP: An Intuitive Introduction]] — notes transformers extend to vision via ViT (2020).
- [[Papers Explained 25 - Vision Transformers]] — paper-level architecture and results for Dosovitskiy et al.
- [[Papers Explained 40 - MobileViT]] — lightweight hybrid combining conv local processing with ViT-style global attention.
- [[Papers Explained 26 - Swin Transformer]] — hierarchical patch-merging ViT variant.
- [[Papers Explained 39 - DeiT]] — knowledge-distillation recipe making ViT competitive on ImageNet alone.

## Notes

**Patch embedding**: for image \(x \in \mathbb{R}^{H \times W \times C}\) and patch size \(P\), sequence length \(N = HW/P^2\); each token has dimension \(P^2 C\) before projection to \(D\).

**Architecture**: identical transformer encoder blocks to NLP (multi-head [[Self-Attention]], MLP, residuals, layer norm); **no decoder**. Hidden size \(D\) fixed across depth.

**Training recipe**: pretrain on large labeled corpus → fine-tune on downstream task by replacing the \(D \rightarrow K\) head. Higher-resolution fine-tuning uses 2D interpolation of learned position embeddings.

**Attention vs conv RF**: with patch size 16, layer-1 self-attention connects all pixels within each 16×16 patch (max distance 128 px); mean attention distance grows with depth. Some early heads remain highly localized; hybrid ResNet→ViT models reduce localized heads, suggesting conv stems substitute for early local feature extraction.

## Related

- [[Self-Attention]]
- [[Multi-Head Attention]]
- [[Positional Embeddings]]
- [[Convolutional Neural Networks]]
- [[Receptive Field]]
- [[Skip Connections]]
- [[Computer Vision]]
- [[Papers Explained 25 - Vision Transformers]]
