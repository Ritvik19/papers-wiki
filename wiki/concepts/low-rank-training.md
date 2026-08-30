# Low-Rank Training

**Type**: concept  
**Tags**: #concept

## Overview
The study and technique of parameterizing neural network weight matrices as low-rank factorizations $W = AB$ during pretraining, utilizing techniques like rank annealing to achieve parameter efficiency without sacrificing optimization dynamics.

## Appearances
- [[Papers Explained: Low-Rank Training in Transformer LMs]] — empirical analysis (arXiv:2407.09835).

## Notes
- Full-rank exploration in early pretraining is necessary to avoid saddle points before transitioning to factorized representations.

## Related
- [[Model Compression and Efficiency]]
- [[Papers Explained 145 - LoRA]]
