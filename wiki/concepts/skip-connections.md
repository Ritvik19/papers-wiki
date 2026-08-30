# Skip Connections

**Type**: concept  
**Tags**: #concept

## Overview

Skip connections route activations from an earlier layer directly to a later layer, bypassing intermediate transformations. In [[ResNet]], identity shortcuts let blocks learn residuals F(x) with output F(x)+x, easing optimization in very deep nets. [[DenseNet]] extends the idea by concatenating all prior feature maps within a block.

## Appearances

- [[Best Deep CNN Architectures and Their Principles: from AlexNet to EfficientNet]] — ResNet residual blocks and bottleneck 1×1 variants; DenseNet dense concatenation; Inception auxiliary classifiers as a related gradient shortcut.
- [[Understanding the Receptive Field of Deep Convolutional Networks]] — skip paths multiply RF routes; tend to shrink effective receptive field (Luo et al.).
- [[How Attention Works in Deep Learning: Understanding the Attention Mechanism in Sequence Models]] — attention paths between encoder and decoder act similarly to skip connections for gradient flow in seq2seq models.
- [[How Transformers Work in Deep Learning and NLP: An Intuitive Introduction]] — residual connections around attention and MLP sublayers enable top-down understanding and multi-path gradients.
- [[Why Multi-Head Self Attention Works: Math, Intuitions and 10+1 Hidden Insights]] — skip connections prevent pure self-attention from collapsing to rank-1 representations exponentially with depth (Dong et al.).

## Related

- [[ResNet]]
- [[DenseNet]]
- [[Vanishing Gradients]]
- [[Convolutional Neural Networks]]
