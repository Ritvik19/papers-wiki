# Autoencoders

**Type**: concept  
**Tags**: #concept

## Overview

Autoencoders learn to compress inputs through an encoder into a code and reconstruct them with a decoder, minimizing reconstruction error. They learn useful representations for denoising, dimensionality reduction, and pretraining.

## Appearances

- [[Deep Learning]] — Chapter 14 (Figure 14.1) covers undercomplete, regularized, denoising, contractive, and sparse autoencoders.
- [[How to Generate Images using Autoencoders]] — AI Summer (2018) intuitive primer: encoder compresses input to a latent bottleneck, decoder reconstructs; applications include compression, dimensionality reduction, denoising, augmentation, and anomaly detection via reconstruction error.
- [[The Theory behind Latent Variable Models: Formulating a Variational Autoencoder]] — AI Summer (2021) theoretical follow-up: probabilistic [[Latent Variable Models]] framework and full [[Variational Autoencoders|VAE]] derivation via [[ELBO]].

## Notes

Precursor to modern masked modeling and VAEs. [[Denoising Autoencoders]] corrupt inputs during training to learn robust features. See also [[Papers Explained Review 11 - Auto Encoders]] in this wiki.

## Related

- [[Denoising Autoencoders]]
- [[Representation Learning]]
- [[Deep Learning]]
- [[Papers Explained Review 11 - Auto Encoders]]
