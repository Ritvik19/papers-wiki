# Layer-Wise Relevance Propagation

**Type**: concept  
**Tags**: #concept

## Overview

Layer-Wise Relevance Propagation (LRP) is a visual explanation method that decomposes a network's classification decision backward through layers, assigning relevance scores to each neuron and ultimately to input pixels, showing which input components contributed most to the output.

## Appearances

- [[Explainable AI (XAI): A Survey of Recent Methods, Applications and Frameworks]] — backward relevance propagation: \(R^l(i) = \sum_j \frac{x(i)w(i,j)}{\sum_i x(i)w(i,j)} R^{l+1}(j)\); implemented in iNNvestigate framework (Samek et al. 2016).

## Notes

LRP provides pixel-level attribution maps distinct from gradient-based methods. Different LRP rules (ε-rule, γ-rule, α-β rule) handle positive/negative contributions differently. Part of the iNNvestigate library alongside CAM and PatternNet.

## Related

- [[Grad-CAM]]
- [[Class Activation Mapping]]
- [[Explainable AI]]
