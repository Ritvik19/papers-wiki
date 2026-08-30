# Dilated Convolution

**Type**: concept  
**Tags**: #concept

## Overview

Dilated (atrous) convolutions apply a kernel with spacing \(r\) (dilation rate) between weights, enlarging the receptive field without increasing parameters or reducing resolution. Effective kernel size becomes \(k' = r(k - 1) + 1\). Stacked dilated convolutions grow receptive field **exponentially** while parameter count grows linearly.

## Appearances

- [[Understanding the Receptive Field of Deep Convolutional Networks]] — Yu & Koltun (2015) multi-scale context aggregation; 3×3 dilations 1/2/4 yield 3×3 → 7×7 → 15×15 RF; commonly placed in late CNN layers.
- [[Deep Learning]] — textbook mentions dilated convolutions as a CNN variant.

## Notes

A 3×3 kernel with dilation 2 matches a 5×5 receptive field at 9 parameters; dilation 4 matches 9×9. Alternatives to pooling for RF expansion without losing spatial resolution. Used in semantic segmentation (DeepLab lineage) and audio models.

## Related

- [[Receptive Field]]
- [[Effective Receptive Field]]
- [[Convolutional Neural Networks]]
- [[Pooling]]
