# Big Transfer

**Type**: concept  
**Tags**: #concept

## Overview

Big Transfer (BiT; Kolesnikov et al., 2020) is large-scale visual representation learning using widened [[ResNet]]-152 variants (up to ResNet-152×4) pretrained on massive datasets (ImageNet-21K, JFT-300M). Key architectural change: **group normalization + weight standardization** replace batch normalization for stable transfer at extreme batch sizes on TPUs.

## Appearances

- [[In-layer Normalization Techniques for Training Very Deep Neural Networks]] — GN+[[Weight Standardization]] replace BN in BiT ResNets for TPU-scale pretraining and transfer; `fig-14.gif` animates BN→GN+WS layer swap.
- [[Best Deep CNN Architectures and Their Principles: from AlexNet to EfficientNet]] — three BiT sizes (S/M/L); GN avoids BN stat mismatch between pretrain and fine-tune; 5-shot ImageNet fine-tuning can match AlexNet-level performance.

## Notes

BN batch statistics become unreliable when distributed across hundreds of TPU workers (tiny per-worker batches). GN is batch-independent. Scaling data (ILSVRC → ImageNet-21K → JFT) in parallel with model width yields strong transfer to small downstream datasets — complementary to EfficientNet's architecture engineering rather than data scale alone.

## Related

- [[ResNet]]
- [[Batch Normalization]]
- [[Transfer Learning]]
- [[Convolutional Neural Networks]]
