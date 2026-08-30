# Adam

**Type**: concept  
**Tags**: #concept

## Overview

Adam (Adaptive Moment Estimation) combines momentum with per-parameter adaptive learning rates using estimates of first and second moments of gradients. It is widely used for training deep networks and fine-tuning language models.

## Appearances

- [[Deep Learning]] — Chapter 8.5.3 describes Adam and related adaptive methods (AdaGrad, RMSProp) as solutions to per-parameter scaling in deep optimization.

## Notes

Adam's default hyperparameters work well across many tasks but may interact with weight decay implementations (AdamW fixes conflation of L2 and adaptive steps in practice). The book predates widespread AdamW usage but covers the underlying moment estimates.

## Related

- [[Stochastic Gradient Descent]]
- [[Momentum]]
- [[Weight Decay]]
- [[Deep Learning]]
