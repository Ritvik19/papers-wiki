# Pooling

**Type**: concept  
**Tags**: #concept

## Overview

Pooling downsamples spatial representations in CNNs (max pooling, average pooling) by aggregating local neighborhoods. It adds translation robustness, reduces dimensionality, and increases receptive field size.

## Appearances

- [[Deep Learning]] — Section 9.3 defines pooling and its role with convolution in [[Convolutional Neural Networks]].
- [[Object Detection for Dummies Part 3]] — [[RoI Pooling]] as max-pool over adaptive bins per region proposal.
- [[Understanding the Receptive Field of Deep Convolutional Networks]] — pooling and strided convolutions **multiplicatively** increase receptive field size; among the fastest practical ways to enlarge the [[Effective Receptive Field]] (Luo et al.).

## Notes

Strided convolution can replace some pooling in modern architectures. [[RoIAlign]] avoids quantization artifacts of RoI Pooling for masks. The book discusses pooling as part of the CNN inductive bias alongside local connectivity and weight sharing.

## Related

- [[Receptive Field]]
- [[Convolutional Neural Networks]]
- [[RoI Pooling]]
- [[Object Detection for Dummies Part 3]]
- [[Deep Learning]]
