# Grad-CAM

**Type**: concept  
**Tags**: #concept

## Overview

Gradient-weighted Class Activation Mapping (Grad-CAM) produces coarse visual explanations for CNN decisions by computing gradients of the target class score with respect to the final convolutional feature maps, then forming a weighted combination of activation maps. Generalizes CAM to architectures without a global average pooling layer.

## Appearances

- [[Explainable AI (XAI): A Survey of Recent Methods, Applications and Frameworks]] — core visual XAI method; weights \(a_k^c = \frac{1}{Z}\sum_{i,j} \partial y^c / \partial A_k(i,j)\); heatmap \(L_{\text{Grad-CAM}}^c = \text{ReLU}(\sum_k a_k^c A_k)\); applied to COVID X-ray diagnosis explanation (Brunese et al. 2020).

## Notes

Introduced by Selvaraju et al. (2017). Grad-CAM requires no model retraining and works on off-the-shelf CNNs. Limitations: coarse spatial resolution (conv-layer granularity), can highlight correlated but non-causal regions, and may fail on adversarially robust models.

## Related

- [[Class Activation Mapping]]
- [[Layer-Wise Relevance Propagation]]
- [[Explainable AI]]
- [[Convolutional Neural Networks]]
