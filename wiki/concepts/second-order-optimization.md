# Second-Order Optimization

**Type**: concept  
**Tags**: #concept

## Overview

Second-order optimization uses curvature information (Hessian or approximations like L-BFGS) to scale gradient steps per direction. It can converge faster near optima but is costly for large neural networks.

## Appearances

- [[Deep Learning]] — Section 8.6 covers Newton methods, conjugate gradient, and limited-memory BFGS for deep model training.

## Notes

First-order methods with adaptive diagonals ([[Adam]]) dominate large-scale deep learning; second-order ideas appear in smaller models and research settings.

## Related

- [[Gradient Descent]]
- [[Adam]]
- [[Deep Learning]]
