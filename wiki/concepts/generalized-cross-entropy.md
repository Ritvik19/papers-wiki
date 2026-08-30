# Generalized Cross Entropy

**Type**: concept  
**Tags**: #concept

## Overview

Generalized Cross Entropy (GCE; Zhang & Sabuncu, NeurIPS 2018) is a robust classification loss interpolating between categorical cross-entropy (noise-sensitive) and mean absolute error (noise-robust but slow). Uses the negative Box-Cox transform; hyperparameter $q \in (0,1]$ trades off robustness vs convergence speed.

## Appearances

- [[Learning with not Enough Data Part 3: Data Generation]] — Compared to NPCL on CIFAR-10 with label noise; noisier data → higher optimal $q$ threshold before overfitting.

## Loss

$$\mathcal{L}_q(f(\mathbf{x}_i, y_i=j)) = \frac{1 - f^{(j)}(\mathbf{x}_i)^q}{q}$$

| $q$ | Limit behavior |
|-----|----------------|
| $q \to 0$ | Approaches CCE |
| $q = 1$ | MAE (equal sample weighting) |

## Motivation

- **MAE**: robust to noisy labels but no per-sample reweighting → slow training
- **CCE**: fast but overfits corruption
- **GCE**: intermediate reweighting via $f^{(j)}(\mathbf{x})^q$ damping

## Related

- [[Cross-Entropy Loss]]
- [[Co-teaching]]
- [[Noise-Pruned Curriculum Loss]]
- [[Synthetic Data]]
