# Data Augmentation

**Type**: concept  
**Tags**: #concept

## Overview

Data augmentation artificially expands the training set by applying label-preserving transformations (crops, flips, noise, color jitter) so the model sees more diverse inputs without collecting new data. It reduces overfitting and improves robustness.

## Appearances

- [[Deep Learning]] — Section 7.4 covers dataset augmentation as a regularization strategy, especially for vision.

## Notes

Augmentation encodes prior knowledge about invariances (e.g. translation for images). Modern LLM training uses synthetic data and rephrasing as a conceptual extension at text scale.

## Related

- [[Overfitting]]
- [[Convolutional Neural Networks]]
- [[Deep Learning]]
