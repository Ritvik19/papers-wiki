# Pix2Pix

**Type**: concept  
**Tags**: #concept

## Overview

Pix2Pix (Isola et al. 2017) is a conditional GAN for **paired** image-to-image translation: input image conditions generation of a corresponding output image. Uses a U-Net generator (skip connections for shared low-level structure), PatchGAN discriminator (classifies local patches, averages for global score), and combined L1 + adversarial loss—L1 captures low frequencies, adversarial loss refines high-frequency detail.

## Appearances

- [[GANs in Computer Vision: Conditional Image Synthesis and 3D Object Generation]] — architecture rationale, PatchGAN design, L1 vs adversarial ablation.
- [[GANs in Computer Vision: 2K Image and Video Synthesis, and Large-Scale Class-Conditional Image Generation]] — extended by [[Pix2PixHD]] to 2K multi-scale synthesis and vid2vid video pipeline.
- [[Papers Explained Review 05 - Generative Adversarial Networks]] — paper survey entry.

## Notes

Noise sampling removed for near-deterministic mappings; dropout/BN kept active at test time for minor stochasticity. Upper bound for unpaired methods like CycleGAN. Reference implementation: github.com/junyanz/pytorch-CycleGAN-and-pix2pix.

## Related

- [[CycleGAN]]
- [[Generative Adversarial Networks]]
- [[DCGAN]]
