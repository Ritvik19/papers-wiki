# Convolution

**Type**: concept  
**Tags**: #concept

## Overview

Convolution applies a shared filter across positions of an input (discrete convolution on grids or sequences), producing translation-equivariant feature maps. In deep learning, cross-correlation is often used without flipping the kernel.

## Appearances

- [[Deep Learning]] — Section 9.1 (Figure 9.1) defines the operation; Sections 9.2–9.5 connect it to [[Convolutional Neural Networks]] and variants.
- [[Object Detection for Dummies Part 2]] — 2D conv on images; padding and stride control output map size.

## Notes

Part 1 uses fixed kernels (Sobel, Prewitt) for [[Image Gradient|gradients]]; Part 2+ use learned CNN filters as hierarchical features for detection.

## Related

- [[Convolutional Neural Networks]]
- [[Image Gradient]]
- [[Object Detection for Dummies Part 2]]
- [[Pooling]]
- [[Parameter Sharing]]
- [[Deep Learning]]
