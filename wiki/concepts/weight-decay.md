# Weight Decay

**Type**: concept  
**Tags**: #concept

## Overview

Weight decay (L2 regularization) penalizes large parameter norms by adding λ‖w‖² to the loss, encouraging smoother, smaller weights and reducing overfitting. In practice it is often implemented as decoupled weight decay (AdamW) during optimization.

## Appearances

- [[Deep Learning]] — Chapter 7.1 treats L2 and L1 parameter norm penalties; Section 7.2 frames them as constrained optimization.

## Notes

Weight decay differs from [[Dropout]] (stochastic structure) and [[Early Stopping]] (optimization trajectory). The book discusses when norm penalties help under-constrained problems.

## Related

- [[Dropout]]
- [[Overfitting]]
- [[Adam]]
- [[Deep Learning]]
