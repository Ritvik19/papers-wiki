# Early Stopping

**Type**: concept  
**Tags**: #concept

## Overview

Early stopping halts training when validation performance stops improving, using the validation set as a regularizer. It approximates finding a parameter setting with good generalization without explicit penalty terms.

## Appearances

- [[Deep Learning]] — Section 7.8 formalizes early stopping as regularization via the optimization trajectory and validation monitoring.

## Notes

Requires a held-out validation set and careful tuning of patience and checkpoints. Common in deep learning alongside [[Weight Decay]] and [[Dropout]].

## Related

- [[Overfitting]]
- [[Weight Decay]]
- [[Deep Learning]]
