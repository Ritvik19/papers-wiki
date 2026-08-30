# AlexNet

**Type**: concept  
**Tags**: #concept

## Overview

AlexNet (Krizhevsky, Sutskever & Hinton, 2012) was the first deep [[Convolutional Neural Networks|CNN]] to win ImageNet at scale (63.3% Top-1). It established the modern stack: stacked conv layers, ReLU activations, max [[Pooling]], and dropout on large fully connected heads.

## Appearances

- [[Best Deep CNN Architectures and Their Principles: from AlexNet to EfficientNet]] — 5 conv layers from 11×11 kernels; CUDA training difficulty pre-autograd; baseline for the ImageNet accuracy timeline.
- [[Object Detection for Dummies Part 2]] — detection-relevant AlexNet summary (5 conv + 2 FC + softmax).

## Notes

Five convolutional layers (11×11 → 5×5 → 3×3 stacks) with three large FC layers and heavy dropout. Introduced GPU-trained deep conv nets to mainstream vision. Superseded by deeper, more parameter-efficient designs (VGG, ResNet) but remains the historical reference point for ImageNet-era deep learning.

## Related

- [[Convolutional Neural Networks]]
- [[Pooling]]
- [[Dropout]]
- [[VGG]]
- [[Computer Vision]]
