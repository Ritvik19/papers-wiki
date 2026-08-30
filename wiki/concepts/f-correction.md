# F-Correction

**Type**: concept  
**Tags**: #concept

## Overview

F-correction (Patrini et al., CVPR 2017) corrects training loss under label noise using an estimated noise transition matrix $C_{ij} = p(\tilde{y}=j|y=i)$: forward correction $-\log\sum_j C_{ji}\hat{p}(y=j|\mathbf{x})$ accounts for random label flipping.

## Appearances

- [[Learning with not Enough Data Part 3: Data Generation]] — Compared to [[Co-teaching]] at high asymmetric noise rates.

## Related

- [[Generalized Cross Entropy]]
- [[Co-teaching]]
- [[Synthetic Data]]
