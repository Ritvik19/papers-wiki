# BEGAN

**Type**: concept  
**Tags**: #concept

## Overview

Boundary Equilibrium GAN (BEGAN, Berthelot et al. 2017) uses an autoencoder as the discriminator, optimizing Wasserstein distance between reconstruction-error distributions rather than between sample distributions. Balance ratio \(\gamma = \mathbb{E}[L(G(z))]/\mathbb{E}[L(x)]\) trades image diversity for visual quality; adaptive \(k_t \in [0,1]\) updated each step maintains equilibrium between auto-encoding real images and discriminating fakes.

## Appearances

- [[GANs in Computer Vision: Improved Training with Wasserstein Distance, Game Theory Control, and Progressively Growing Schemes]] — game-theoretic formulation, architecture (U-shaped ELU autoencoder), 128×128 interpolation results.

## Notes

No explicit K-Lipschitz constraint on D. Trains stably with Adam without pretraining. Convergence measured by minimizing \(L(x)\) and \(|\gamma L(x) - L(G(z))|\). Higher \(\gamma\) increases variety but adds artifacts.

## Related

- [[Wasserstein GAN]]
- [[Autoencoders]]
- [[Generative Adversarial Networks]]
