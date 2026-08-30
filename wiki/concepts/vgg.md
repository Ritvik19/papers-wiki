# VGG

**Type**: concept  
**Tags**: #concept

## Overview

VGG (Simonyan & Zisserman, 2014) demonstrated that **depth** — stacking many small 3×3 convolutions — reliably improves ImageNet accuracy. Three 3×3 layers approximate a 7×7 receptive field with fewer parameters and more non-linearities than a single large kernel.

## Appearances

- [[Best Deep CNN Architectures and Their Principles: from AlexNet to EfficientNet]] — depth-as-scaling principle; 27×C² params for three 3×3 vs 49×C² for one 7×7; normalization challenges at depth; still used for perceptual loss and neural style transfer.
- [[Object Detection for Dummies Part 2]] — VGG as detection backbone.

## Notes

Trained on 224×224 RGB images. VGG-16/19 remain common feature extractors despite high parameter counts (138–144M). The "deeper is better" assumption holds only up to a point before optimization and normalization issues dominate.

## Related

- [[AlexNet]]
- [[ResNet]]
- [[Convolutional Neural Networks]]
- [[Batch Normalization]]
