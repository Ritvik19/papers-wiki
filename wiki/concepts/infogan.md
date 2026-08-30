# InfoGAN

**Type**: concept  
**Tags**: #concept

## Overview

InfoGAN (Chen et al. 2016) extends GANs with unsupervised latent codes \(c\) whose mutual information with generated outputs is maximized. An auxiliary network Q (discriminator plus classification head) estimates \(P(c|x)\), preventing the generator from ignoring \(c\). Learns disentangled factors—e.g. digit rotation and stroke thickness on MNIST—without labeled attributes.

## Appearances

- [[GANs in Computer Vision: Introduction to Generative Learning]] — mutual-information motivation, auxiliary-loss implementation, and latent-code traversal results.
- [[Papers Explained Review 05 - Generative Adversarial Networks]] — paper survey entry.

## Notes

Builds on conditional GAN ideas but discovers interpretable codes without supervision. OpenAI reference implementation: github.com/openai/InfoGAN.

## Related

- [[StyleGAN]] — later work quantifying disentanglement (perceptual path length, linear separability).
- [[Generative Adversarial Networks]]
- [[Variational Autoencoders]]
- [[Representation Learning]]
