# Instance Normalization

**Type**: concept  
**Tags**: #concept

## Overview

Instance normalization (IN; Ulyanov et al., 2016) computes mean and variance **per sample and per channel** over spatial dimensions H×W only. It removes instance-specific contrast/style from feature maps while learnable affine parameters γ, β can encode a target style. Widely used in neural style transfer and generative models.

## Appearances

- [[In-layer Normalization Techniques for Training Very Deep Neural Networks]] — IN for fast stylization; affine params can fully change output style; conditional IN for finite style sets.
- [[GANs in Computer Vision: Conditional Image Synthesis and 3D Object Generation]] — style transfer and image-to-image context.
- [[Papers Explained Review 10 - Normalization Layers]] — paper survey.

## Notes

GN with groups equal to channel count is equivalent to IN. [[Adaptive Instance Normalization]] extends IN by injecting style statistics from a reference image.

## Related

- [[Adaptive Instance Normalization]]
- [[Group Normalization]]
- [[Batch Normalization]]
