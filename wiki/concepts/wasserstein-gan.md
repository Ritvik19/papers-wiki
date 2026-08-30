# Wasserstein GAN

**Type**: concept  
**Tags**: #concept

## Overview

Wasserstein GAN (WGAN, Arjovsky et al. 2017) replaces the standard GAN minimax objective with the Wasserstein (Earth Mover) distance between real and generated distributions. The critic (not a probability discriminator) estimates \(\sup_{\|f\|_L \leq 1} [\mathbb{E}[f(x_{\text{real}})] - \mathbb{E}[f(x_{\text{fake}})]]\). Weight clipping enforces the K-Lipschitz constraint; train the critic for multiple steps (\(n_{\text{critic}}\)) per generator update.

## Appearances

- [[GANs in Computer Vision: Improved Training with Wasserstein Distance, Game Theory Control, and Progressively Growing Schemes]] — Wasserstein loss derivation, PyTorch training code, WGAN-GP gradient-penalty snippet, stability trade-offs (RMSProp vs Adam).
- [[GANs in Computer Vision: Semantic Image Synthesis and Learning a Generative Model from a Single Image]] — WGAN-GP stabilizes [[SinGAN]] training.
- [[Papers Explained Review 05 - Generative Adversarial Networks]] — algorithm summary and WGAN-GP note.

## Notes

Reduces [[Mode Collapse]] and discriminator saturation vs JS divergence. Weight clipping is a crude Lipschitz enforcement; WGAN-GP (Gulrajani et al. 2017) uses gradient penalty on interpolated samples as the preferred fix. Does not require balancing G/D capacities.

## Related

- [[Generative Adversarial Networks]]
- [[Mode Collapse]]
- [[Progressive GAN]]
