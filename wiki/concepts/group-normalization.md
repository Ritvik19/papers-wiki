# Group Normalization

**Type**: concept  
**Tags**: #concept

## Overview

Group normalization (GN; Wu & He, 2018) divides C channels into G groups and normalizes activations within each group over spatial dimensions H×W. Statistics are **batch-independent**, giving stable accuracy when batch size is small — common in detection, segmentation, and video. Special cases: G=C yields [[Instance Normalization]]; G=1 yields [[Layer Normalization]].

## Appearances

- [[In-layer Normalization Techniques for Training Very Deep Neural Networks]] — ResNet-50 ImageNet comparison at batch 32/GPU; GN+[[Weight Standardization]] for transfer learning.
- [[Best Deep CNN Architectures and Their Principles: from AlexNet to EfficientNet]] — [[Big Transfer]] replaces BN with GN for TPU-scale pretraining.
- [[Papers Explained Review 10 - Normalization Layers]] — implementation survey.

## Notes

Hyperparameter G is typically 32. GN avoids BN's small-batch statistic noise but does not provide BN's batch-level regularization effect.

## Related

- [[Batch Normalization]]
- [[Layer Normalization]]
- [[Instance Normalization]]
- [[Weight Standardization]]
- [[Big Transfer]]
