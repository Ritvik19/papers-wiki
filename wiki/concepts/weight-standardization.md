# Weight Standardization

**Type**: concept  
**Tags**: #concept

## Overview

Weight standardization (WS; Qiao et al., 2019) normalizes **convolutional filter weights** per output channel (zero mean, unit variance across the kernel) before applying the convolution, rather than normalizing activations. WS smooths the loss landscape, reduces Lipschitz constants of the loss and gradients, and pairs strongly with [[Group Normalization]] — GN+WS outperforms BN and GN alone on ImageNet and COCO.

## Appearances

- [[In-layer Normalization Techniques for Training Very Deep Neural Networks]] — theoretical motivation (compact weight space); GN+WS results; adopted in [[Big Transfer]] for large-scale visual pretraining.
- [[Best Deep CNN Architectures and Their Principles: from AlexNet to EfficientNet]] — BiT replaces BN with GN+WS for TPU distributed training.
- [[Papers Explained Review 10 - Normalization Layers]] — implementation survey.

## Notes

Evolution of [[Weight Normalization]] with per-channel weight statistics. Particularly valuable when batch statistics are unreliable (small per-device batches, transfer learning).

## Related

- [[Group Normalization]]
- [[Weight Normalization]]
- [[Big Transfer]]
- [[Batch Normalization]]
