# Adaptive Instance Normalization

**Type**: concept  
**Tags**: #concept

## Overview

Adaptive instance normalization (AdaIN; Huang & Belongie, 2017) aligns the channel-wise mean and variance of a **content** feature map x to those of a **style** reference y:

AdaIN(x, y) = σ(y) · (x − μ(x)) / σ(x) + μ(y)

A single AdaIN layer can transfer arbitrary artistic styles in real time within an encoder–decoder architecture.

## Appearances

- [[In-layer Normalization Techniques for Training Very Deep Neural Networks]] — AdaIN architecture and results; extends [[Instance Normalization]] with style-injected affine parameters.
- [[GANs in Computer Vision: Self-Supervised Adversarial Training and High-Resolution Image Synthesis with Style Incorporation]] — core mechanism in [[StyleGAN]] per-layer style control.
- [[GANs in Computer Vision: Semantic Image Synthesis and Learning a Generative Model from a Single Image]] — global AdaIN loses spatial semantics; motivates [[SPADE]] in [[GauGAN]].
- [[GANs in Computer Vision: Conditional Image Synthesis and 3D Object Generation]] — style transfer lineage.

## Notes

Unlike IN's learned γ, β, AdaIN's scale and shift come directly from style image statistics. Precursor to segmentation-conditioned [[SPADE]].

## Related

- [[Instance Normalization]]
- [[SPADE]]
- [[Generative Adversarial Networks]]
