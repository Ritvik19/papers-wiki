# AC-GAN

**Type**: concept  
**Tags**: #concept

## Overview

Auxiliary Classifier GAN (AC-GAN, Odena et al. 2017) extends conditional GANs by adding a decoder head on the discriminator that reconstructs class labels from real and generated images. The auxiliary (reconstruction) loss stabilizes training and improves high-resolution (128×128) class-conditional synthesis on ImageNet-scale data.

## Appearances

- [[GANs in Computer Vision: Conditional Image Synthesis and 3D Object Generation]] — architecture, MS-SSIM diversity evaluation, latent-space walks, 100-model ensemble scaling to 1000 classes.
- [[Papers Explained Review 05 - Generative Adversarial Networks]] — paper survey entry.

## Notes

Combines ideas from conditional GAN (class labels) and InfoGAN-style side information. Generator latent \(z\) is learned independent of class at inference. Evaluated with [[Inception Score]] (discriminability) and MS-SSIM (diversity).

## Related

- [[Generative Adversarial Networks]]
- [[InfoGAN]]
- [[Inception Score]]
