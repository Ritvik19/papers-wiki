# ResNet

**Type**: concept  
**Tags**: #concept

## Overview

ResNet (He et al., 2015) enables very deep [[Convolutional Neural Networks]] via **identity skip connections**: blocks learn residuals F(x) so the output is F(x)+x rather than H(x) directly. Combined with batch normalization, ResNets scale from 18 to 152+ layers without severe [[Vanishing Gradients]].

## Appearances

- [[Best Deep CNN Architectures and Their Principles: from AlexNet to EfficientNet]] — residual formulation; bottleneck 1×1–3×3–1×1 blocks for ResNet-50+; wide ResNet variants; foundation for [[Big Transfer]].
- [[Object Detection for Dummies Part 2]] — ResNet as detection backbone enabling 100+ layer stacks.
- [[Understanding the Receptive Field of Deep Convolutional Networks]] — skip paths multiply RF paths (HighResNet analysis).
- [[How the Vision Transformer (ViT) Works in 10 Minutes: An Image Is Worth 16×16 Words]] — ResNet recommended over ViT when pretraining data is below ~14M images; hybrid ResNet→ViT reduces localized attention heads.

## Notes

Bottleneck blocks reduce then restore channel dimensions around the 3×3 conv. torchvision provides ResNet-18 through ResNet-152 and wide variants. ResNet remains the default vision backbone family and the base for large-scale pretraining (BiT, many downstream detectors).

## Related

- [[Skip Connections]]
- [[Vanishing Gradients]]
- [[Batch Normalization]]
- [[Big Transfer]]
- [[Convolutional Neural Networks]]
