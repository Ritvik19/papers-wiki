# Class Activation Mapping

**Type**: concept  
**Tags**: #concept

## Overview

Class Activation Mapping (CAM) is a CNN saliency technique that localizes image regions discriminative for a target class by weighting convolutional feature maps with class-specific weights from a global average pooling (GAP) layer placed before the final fully connected classifier.

## Appearances

- [[Explainable AI (XAI): A Survey of Recent Methods, Applications and Frameworks]] — foundational visual XAI method; \(M_c(x,y) = \sum_k w_c^k f_k(x,y)\) where \(w_c^k\) are GAP-to-softmax weights and \(f_k\) are conv activations (Zhou et al. 2016).

## Notes

CAM requires a specific architecture (conv layers → GAP → FC). **[[Grad-CAM]]** relaxes this constraint by using gradients instead of fixed GAP weights. CAM heatmaps are class-specific and highlight spatial regions that most influence the softmax score for class \(c\).

## Related

- [[Grad-CAM]]
- [[Layer-Wise Relevance Propagation]]
- [[Explainable AI]]
- [[Convolutional Neural Networks]]
