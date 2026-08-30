# Convolutional Neural Networks

**Type**: concept  
**Tags**: #concept

## Overview

Convolutional neural networks (CNNs) apply shared local filters across spatial (or temporal) grids, with pooling for downsampling and translation robustness. They encode strong inductive biases—local connectivity, parameter sharing, and equivariance—that make them the default architecture for images and many structured signals.

## Appearances

- [[Deep Learning]] — Chapter 9 defines convolution, pooling, variants (dilated, separable), and ties CNN success to neuroscience and ImageNet-era history (Figure 9.11).

## Notes

The textbook predates Vision Transformers; its CNN treatment remains the standard reference for understanding modern vision backbones that still use convolutions or hybrid designs. Cross-reference [[Papers Explained Review 01 - Convolutional Neural Networks]] for paper-level follow-ups in this wiki.

[[Object Detection for Dummies Part 2]] summarizes detection-relevant CNN milestones: **AlexNet** (5 conv + 2 FC + softmax, heavy augmentation), **VGG** (deep 3×3 stacks), **ResNet** (residual blocks enabling 100+ layers). These backbones pre-train R-CNN-family detectors in [[Object Detection for Dummies Part 3]].

## Appearances (additional)

- [[Object Detection for Dummies Part 2]] — AlexNet, VGG, ResNet architecture notes for detection backbones.
- [[Understanding the Receptive Field of Deep Convolutional Networks]] — how stacked conv, pooling, dilation, and skip connections compose receptive fields; Araujo et al. closed-form RF and Luo et al. effective RF analysis.
- [[Best Deep CNN Architectures and Their Principles: from AlexNet to EfficientNet]] — historical survey of ImageNet CNN families (AlexNet → EfficientNet) organized around width/depth/resolution scaling and compound scaling.
- [[How the Vision Transformer (ViT) Works in 10 Minutes: An Image Is Worth 16×16 Words]] — contrasts CNN locality/translation biases with permutation-invariant transformers on patch sequences; ResNet/EfficientNet recommended below 14M-image scale.
- [[Explainable AI (XAI): A Survey of Recent Methods, Applications and Frameworks]] — CAM, Grad-CAM, LRP, and related saliency methods target CNN internal representations for visual explanation of classification decisions.

## Related

- [[Receptive Field]]
- [[Pooling]]
- [[Dilated Convolution]]
- [[Data Augmentation]]
- [[Deep Learning]]
- [[Computer Vision]]
- [[Papers Explained Review 01 - Convolutional Neural Networks]]
