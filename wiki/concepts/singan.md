# SinGAN

**Type**: concept  
**Tags**: #concept

## Overview

SinGAN (Shaham et al., 2019, ICCV best paper) learns a generative model from a **single** natural image by training a pyramid of fully convolutional patch-GANs on multi-scale downsampled versions. Coarse scales train first then freeze; [[Wasserstein GAN]] gradient penalty stabilizes training. Per-scale noise injection and limited receptive fields prevent memorization. Reconstruction loss with zero noise anchors each scale's distribution. Applications: diverse random samples, super-resolution, paint-to-image, image harmonization, editing, single-image animation.

## Appearances

- [[GANs in Computer Vision: Semantic Image Synthesis and Learning a Generative Model from a Single Image]] — architecture, scale pyramid, reconstruction loss, harmonization results.

## Notes

Patch statistics within one image carry enough information for generation. Analogous coarse-to-fine training to [[Progressive GAN]] but per-scale GANs frozen sequentially. Official code released by authors.

## Related

- [[Wasserstein GAN]]
- [[Progressive GAN]]
- [[Pix2Pix]]
- [[Generative Adversarial Networks]]
