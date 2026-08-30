# DenseNet

**Type**: concept  
**Tags**: #concept

## Overview

DenseNet (Huang et al., 2017) connects each layer to every subsequent layer within a **dense block** via channel concatenation (not addition like ResNet). **Feature reuse** yields very compact models with fewer repeated feature maps; growth rate k controls how many channels each layer adds.

## Appearances

- [[Best Deep CNN Architectures and Their Principles: from AlexNet to EfficientNet]] — dense blocks + transition layers (avg-pool downsample); 1×1 bottlenecks with k=featmaps/2; dropout p=0.2; strong in segmentation and medical imaging despite slow training.

## Notes

Input channels to layer l: k₀ + k·(l−1). Bottleneck size (bn_size) limits memory explosion from concatenation. DenseNet-121 achieves competitive accuracy with only ~8M parameters. Trade-off: high memory use from storing all intermediate feature maps.

## Related

- [[ResNet]]
- [[Convolutional Neural Networks]]
- [[Computer Vision]]
