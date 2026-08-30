# Feature Matching

**Type**: concept  
**Tags**: #concept

## Overview

Feature matching is a GAN training objective (Salimans et al. 2016) where the generator is trained to match the expected value of intermediate discriminator activations on real data, using an L2 distance. This stabilizes training by aligning feature statistics rather than only fooling the final real/fake logit—effective when standard adversarial loss becomes unstable.

## Appearances

- [[GANs in Computer Vision: Introduction to Generative Learning]] — described as part of Improved GAN; produces globally coherent statistics recognizable by human vision even when local anatomy is imperfect.
- [[GANs in Computer Vision: 2K Image and Video Synthesis, and Large-Scale Class-Conditional Image Generation]] — multi-scale feature matching loss in Pix2PixHD and vid2vid across image-pyramid discriminators.
- [[Papers Explained Review 05 - Generative Adversarial Networks]] — Improved GAN survey entry.

## Notes

Distinct from perceptual or style losses in other generative models. Often combined with minibatch discrimination, label smoothing, and virtual batch normalization in the same paper.

## Related

- [[Generative Adversarial Networks]]
- [[Mode Collapse]]
- [[Inception Score]]
