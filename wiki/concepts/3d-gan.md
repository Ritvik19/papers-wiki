# 3D-GAN

**Type**: concept  
**Tags**: #concept

## Overview

3D-GAN (Wu et al. 2016) applies generative adversarial learning to volumetric shape synthesis using 3D convolutions in a DCGAN-style architecture (no pooling; symmetric G/D with LeakyReLU in D). **3D-VAE-GAN** extends this with a 2D image encoder that maps RGB views to latent \(z\), combining adversarial, KL, and MSE reconstruction losses for single-image 3D reconstruction from paired 2D–3D data.

## Appearances

- [[GANs in Computer Vision: Conditional Image Synthesis and 3D Object Generation]] — architecture, G/D balancing tricks (lower D lr, batch 100, conditional D updates), latent interpolation and arithmetic.

## Notes

64³ voxels are ~64× more parameters than 64² pixels. Training imbalance (D faster than G) addressed with heuristics rather than Wasserstein distance. Supports generation, 3D classification via D, and single-view reconstruction.

## Related

- [[DCGAN]]
- [[Variational Autoencoders]]
- [[Generative Adversarial Networks]]
