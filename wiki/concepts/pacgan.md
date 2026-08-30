# PacGAN

**Type**: concept  
**Tags**: #concept

## Overview

PacGAN (Lin et al. 2018) mitigates [[Mode Collapse]] by modifying the discriminator to accept \(n\) packed independent samples (all real or all fake) concatenated along channels. Binary hypothesis testing on the product distribution lets D detect lack of diversity. Extends minibatch discrimination from Improved GAN with formal statistical grounding.

## Appearances

- [[GANs in Computer Vision: Conditional Image Synthesis and 3D Object Generation]] — packing intuition, PacDCGAN diversity improvements over DCGAN.
- [[GANs in Computer Vision: Introduction to Generative Learning]] — minibatch discrimination introduced as precursor.

## Notes

Packing is independent of training batch size. Only input kernel size changes for convolutional D. Official code: github.com/LTH14/pacgan.

## Related

- [[Mode Collapse]]
- [[Generative Adversarial Networks]]
- [[Feature Matching]]
