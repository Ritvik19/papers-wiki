# Batch Normalization

**Type**: concept  
**Tags**: #concept

## Overview

Batch normalization standardizes layer inputs across a minibatch (with learnable scale and shift), reducing internal covariate shift and often allowing higher learning rates. It acts as a regularizer and stabilizes very deep network training.

## Appearances

- [[In-layer Normalization Techniques for Training Very Deep Neural Networks]] — per-channel μ, σ over N×H×W; advantages (speed, regularization, gradient flow) and disadvantages (small batch, train/inference mismatch); [[Synchronized Batch Normalization]] for distributed training.
- [[Deep Learning]] — Discussed in the optimization and architecture context (Chapter 8); the book's 2016 edition covers BN as an emerging practice alongside initialization and depth.
- [[GANs in Computer Vision: Self-Supervised Adversarial Training and High-Resolution Image Synthesis with Style Incorporation]] — contrasted with instance normalization and [[Adaptive Instance Normalization]] for style vs content in GAN generators.

## Notes

Variants include layer norm, group norm, and RMS norm (common in transformers). BN depends on batch statistics and behaves differently at train vs inference time (running mean/variance).

## Related

- [[Weight Initialization]]
- [[Adaptive Instance Normalization]]
- [[Feedforward Neural Networks]]
- [[Deep Learning]]
