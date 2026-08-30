# Effective Receptive Field

**Type**: concept  
**Tags**: #concept

## Overview

The effective receptive field (ERF) is the subset of a unit's theoretical [[Receptive Field]] where input pixels have non-negligible impact on the output — measured via gradient magnitude from backpropagation. Not all pixels in the theoretical RF contribute equally; central pixels dominate because they have many paths to the output.

## Appearances

- [[Understanding the Receptive Field of Deep Convolutional Networks]] — Luo et al. (2016) analysis: ERF resembles a 2D Gaussian; ReLU non-linearities distort it; ERF grows slower than theoretical RF but increases after training.

## Notes

Luo et al. show that in forward pass central pixels propagate through many paths while border pixels have few; in backward pass central pixels receive larger gradient magnitudes. Adding layers increases theoretical RF but **decreases ERF ratio**. Skip connections multiply RF paths but tend to make ERF smaller. Pooling and [[Dilated Convolution]] quickly enlarge ERF in practice.

## Related

- [[Receptive Field]]
- [[Dilated Convolution]]
- [[Convolutional Neural Networks]]
