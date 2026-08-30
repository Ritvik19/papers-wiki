# Receptive Field

**Type**: concept  
**Tags**: #concept

## Overview

The receptive field (RF) of a unit in a [[Convolutional Neural Networks|CNN]] is the region of the input that can influence that unit's output. The term comes from neuroscience (sensory patch eliciting a neuronal response) and applies only to **local operations** — [[Convolution]] and [[Pooling]] — not fully connected layers, which see the entire input.

## Appearances

- [[Understanding the Receptive Field of Deep Convolutional Networks]] — full survey: biological motivation, Araujo et al. closed-form RF formulas, ways to increase RF (depth, pooling, dilation, depthwise stacks), skip-connection path multiplicity, and [[Effective Receptive Field]] analysis (Luo et al.).
- [[Pooling]] — downsampling multiplicatively increases receptive field size.
- [[Papers Explained 38 - Longformer]] — stacked sliding-window attention achieves large receptive field analogous to CNNs.
- [[How the Vision Transformer (ViT) Works in 10 Minutes: An Image Is Worth 16×16 Words]] — ViT mean attention distance parallels RF growth; layer-1 self-attention spans entire patches (P×P pixels).

## Notes

**Why it matters**: Dense prediction (segmentation, optical flow) needs each output pixel's RF to cover relevant context. Object detection needs RF large enough for big objects. ImageNet accuracy correlates logarithmically with RF (Araujo et al. 2019) with diminishing returns.

**Single-path closed form** (no skip connections): for layers with kernels \(k_i\) and strides \(s_i\), RF at input is \(r_0 = \sum_{i=1}^{L} ((k_i - 1) \prod_{j=1}^{i-1} s_j) + 1\).

**Growth strategies**: deeper conv stacks (linear), pooling/strided conv (multiplicative), [[Dilated Convolution]] sequences (exponential RF, linear params). Skip connections create \(2^n\) paths with diverse RFs but tend to shrink the effective field.

## Related

- [[Effective Receptive Field]]
- [[Dilated Convolution]]
- [[Convolutional Neural Networks]]
- [[Pooling]]
- [[Computer Vision]]
