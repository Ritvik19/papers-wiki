# Denoising Autoencoders

**Type**: concept  
**Tags**: #concept

## Overview

Denoising autoencoders train on corrupted inputs but reconstruct clean targets, forcing the model to capture structure rather than memorizing identity. They learn robust, useful representations of the data manifold.

## Appearances

- [[Deep Learning]] — Section 14.5; connected to score matching and generative modeling in later chapters.
- [[How to Generate Images using Autoencoders]] — cited as an autoencoder application: train on noisy inputs, reconstruct clean targets.

## Notes

Conceptually related to masked language modeling (predict clean from corrupted context) though BERT-style objectives came later. Also linked to [[Denoising Score Matching]] (Chapter 18).

## Related

- [[Autoencoders]]
- [[Representation Learning]]
- [[Deep Learning]]
