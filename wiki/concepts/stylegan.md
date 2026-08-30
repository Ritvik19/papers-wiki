# StyleGAN

**Type**: concept  
**Tags**: #concept

## Overview

StyleGAN (Karras et al., 2019) replaces the conventional GAN generator with a style-based architecture: mapping network \(f: Z \to W\), synthesis network \(g\) with per-layer AdaIN style injection (A blocks) and per-pixel noise (B blocks), progressive 4×4→1024×1024 upsampling (from [[Progressive GAN]]). Controls global attributes (pose, age, lighting) via style vectors and local stochastic detail via noise. Uses truncation in \(W\) and style-mixing regularization. Introduces perceptual path length and linear separability metrics for latent disentanglement.

## Appearances

- [[GANs in Computer Vision: Self-Supervised Adversarial Training and High-Resolution Image Synthesis with Style Incorporation]] — full architecture walkthrough, AdaIN/noise localization, truncation, metrics.
- [[Progressive GAN]] — architectural precursor from same authors.

## Notes

Revolutionary face synthesis quality; foundation for StyleGAN2/3. Mapping network induces less entangled \(W\) than \(Z\). Each AdaIN layer overrides previous style statistics.

## Related

- [[Adaptive Instance Normalization]]
- [[Progressive GAN]]
- [[BigGAN]]
- [[InfoGAN]]
- [[Generative Adversarial Networks]]
