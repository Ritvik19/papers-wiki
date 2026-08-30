# BigGAN

**Type**: concept  
**Tags**: #concept

## Overview

BigGAN (Brock et al., 2018) scales class-conditional ImageNet generation via large-batch distributed training (batch 2048), increased width/depth on an SA-GAN backbone, spectral normalization, hinge loss, conditional batch norm with shared class embedding, orthogonal initialization, skip-z latent injections to multiple G layers, and the truncation trick (resample high-norm \(z\) at inference for higher quality, lower diversity).

## Appearances

- [[GANs in Computer Vision: 2K Image and Video Synthesis, and Large-Scale Class-Conditional Image Generation]] — scaling ablations, truncation trick, class leakage, texture vs structure class difficulty.
- [[Papers Explained Review 05 - Generative Adversarial Networks]] — survey context if listed.

## Notes

Requires multi-GPU training; official TensorFlow weights. Stability depends on balanced G/D adversarial dynamics. Orthogonal regularization supports truncation across latent space.

## Related

- [[StyleGAN]] — truncation trick in Z; StyleGAN truncates in intermediate W space.
- [[Generative Adversarial Networks]]
- [[AC-GAN]]
- [[Mode Collapse]]
- [[Inception Score]]
