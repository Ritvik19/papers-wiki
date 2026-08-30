# Inception Network

**Type**: concept  
**Tags**: #concept

## Overview

Inception / GoogLeNet (Szegedy et al., 2014–2016) scales **width** via parallel multi-scale branches (1×1, 3×3, 5×5, pooling) within Inception modules, using 1×1 bottleneck convolutions to limit compute. Motivation: process information at multiple scales like the human visual system without a memory explosion.

## Appearances

- [[Best Deep CNN Architectures and Their Principles: from AlexNet to EfficientNet]] — GoogLeNet (22 layers, 9 Inception modules); auxiliary classifiers for vanishing gradients; V2/V3 factorized convolutions and batch norm; 1×1 convs as low-dimensional embeddings.

## Notes

Inception V2/V3 factor 5×5 and 7×7 convs into sequential 3×3 stacks (VGG principle) and use spatially separable 1×3 + 3×1 convs. Global average pooling replaces large FC heads. Later variants include Inception V4 and Inception-ResNet.

## Related

- [[Convolutional Neural Networks]]
- [[Vanishing Gradients]]
- [[Pooling]]
- [[EfficientNet]]
