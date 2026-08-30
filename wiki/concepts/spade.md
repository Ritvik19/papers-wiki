# SPADE

**Type**: concept  
**Tags**: #concept

## Overview

SPADE (Spatially-Adaptive Normalization; Park et al., 2019) performs per-channel activation normalization like [[Batch Normalization]], then applies **spatially varying** scale γ and shift β predicted by convolutions on a segmentation mask. Unlike global affine parameters, γ and β are 3D tensors (C×H×W), preserving semantic layout during GAN-based image synthesis.

## Appearances

- [[GANs in Computer Vision: Semantic Image Synthesis and Learning a Generative Model from a Single Image]] — GauGAN tutorial: SPADE math, ResNet blocks, generator without encoder, vs AdaIN and pix2pixHD++.
- [[In-layer Normalization Techniques for Training Very Deep Neural Networks]] — SPADE module diagram; extends [[Adaptive Instance Normalization]] idea to layout-conditioned synthesis.
- [[Papers Explained 253 - SPADE]] — paper-level coverage.
- [[GauGAN]] — primary application (semantic image synthesis).

## Notes

Also called semantic image synthesis with spatially-adaptive normalization. Replaces batch norm in generator blocks where naive BN would wash out semantic information from the mask.

## Related

- [[GauGAN]]
- [[Pix2PixHD]]
- [[Adaptive Instance Normalization]]
- [[Instance Normalization]]
- [[Generative Adversarial Networks]]
