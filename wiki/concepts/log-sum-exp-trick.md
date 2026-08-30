# Log-Sum-Exp Trick

**Type**: concept  
**Tags**: #concept

## Overview

The log-sum-exp trick rewrites log ∑ exp(xᵢ) as max(x) + log ∑ exp(xᵢ − max(x)) for numerical stability, avoiding overflow when computing softmax denominators and log-partition functions.

## Appearances

- [[Deep Learning]] — Section 4.1 (overflow and underflow) and softmax/stable cross-entropy practice in supervised learning chapters.

## Related

- [[Softmax]]
- [[Cross-Entropy Loss]]
- [[Deep Learning]]
