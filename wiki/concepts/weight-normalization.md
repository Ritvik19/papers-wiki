# Weight Normalization

**Type**: concept  
**Tags**: #concept

## Overview

Weight normalization (Salimans & Kingma, 2016) reparameterizes each weight vector as **w = (g/‖v‖) v**, decoupling the learned magnitude g from direction v without reducing expressiveness. It normalizes **weights** rather than activations, offering an alternative stabilization strategy to [[Batch Normalization]].

## Appearances

- [[In-layer Normalization Techniques for Training Very Deep Neural Networks]] — brief coverage; precursor to [[Weight Standardization]].

## Notes

Less commonly used in modern vision pipelines than activation normalization or weight standardization, but conceptually important as a reparameterization trick.

## Related

- [[Weight Standardization]]
- [[Batch Normalization]]
