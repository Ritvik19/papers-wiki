# Generative Adversarial Networks

**Type**: concept  
**Tags**: #concept

## Overview

Generative adversarial networks (GANs) train a generator to fool a discriminator that distinguishes real from generated samples—a minimax game. GANs produce sharp samples without explicit likelihood for the generator.

## Appearances

- [[Deep Learning]] — Section 20.10 (directed generative nets); Goodfellow is lead author of both the book and the original GAN paper.
- [[GANs in Computer Vision: Introduction to Generative Learning]] — AI Summer part-1 survey: vanilla GAN, cGAN, DCGAN, InfoGAN, Improved GAN training tricks, mode collapse, PyTorch training loops.
- [[GANs in Computer Vision: Conditional Image Synthesis and 3D Object Generation]] — AI Summer part-2: AC-GAN, 3D-GAN, PacGAN, Pix2Pix, CycleGAN, image-to-image translation.
- [[GANs in Computer Vision: Improved Training with Wasserstein Distance, Game Theory Control, and Progressively Growing Schemes]] — AI Summer part-3: WGAN, BEGAN, Progressive GAN, megapixel training.
- [[GANs in Computer Vision: 2K Image and Video Synthesis, and Large-Scale Class-Conditional Image Generation]] — AI Summer part-4: Pix2PixHD, vid2vid, BigGAN.
- [[GANs in Computer Vision: Self-Supervised Adversarial Training and High-Resolution Image Synthesis with Style Incorporation]] — AI Summer part-5: self-supervised GAN, StyleGAN, AdaIN.
- [[GANs in Computer Vision: Semantic Image Synthesis and Learning a Generative Model from a Single Image]] — AI Summer part-6 (finale): GauGAN/SPADE, SinGAN single-image generation.
- [[Papers Explained Review 05 - Generative Adversarial Networks]] — wiki paper survey from GAN (2014) through CycleGAN.

## Notes

Training can be unstable (mode collapse, delicate balance). Diffusion and flow models partly supplanted GANs for image generation, but adversarial losses remain common (e.g. discriminators in alignment).

## Related

- [[Adversarial Training]]
- [[Ian Goodfellow]]
- [[Deep Learning]]
