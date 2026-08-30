# EfficientNet

**Type**: concept  
**Tags**: #concept

## Overview

EfficientNet (Tan & Le, 2019) is a family of ImageNet CNNs built from an NAS-derived baseline (B0) and scaled via **compound scaling** — jointly increasing depth, width, and input resolution under a FLOPs budget. EfficientNet-B1 is 7.6× smaller and 5.7× faster than ResNet-152 at similar accuracy.

## Appearances

- [[Best Deep CNN Architectures and Their Principles: from AlexNet to EfficientNet]] — B0 from NAS; compound coefficients α=1.2, β=1.2, γ=1.15; extended by [[Noisy Student]] and [[Meta Pseudo Labels]] to 88–90% Top-1.
- [[How the Vision Transformer (ViT) Works in 10 Minutes: An Image Is Worth 16×16 Words]] — EfficientNet recommended over ViT when pretraining data is below ~14M images.
- [[Papers Explained - EfficientNetV2]] — follow-on family with faster training in this wiki.

## Notes

Individual scaling of depth, width, or resolution alone saturates; compound scaling balances all three. Constraint α·β²·γ² ≈ 2 reflects that doubling width or resolution quadruples FLOPs vs doubling depth. B0–B7 span the Pareto frontier of accuracy vs parameters at publication time.

## Related

- [[Compound Scaling]]
- [[Noisy Student]]
- [[Meta Pseudo Labels]]
- [[Convolutional Neural Networks]]
- [[Papers Explained - EfficientNetV2]]
