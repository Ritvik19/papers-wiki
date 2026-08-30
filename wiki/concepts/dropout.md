# Dropout

**Type**: concept  
**Tags**: #concept

## Overview

Dropout is a regularization technique that randomly drops units (and their connections) during training with probability p, then scales activations at test time (or uses inverted dropout during training). It approximates training an ensemble of exponentially many thinned networks and reduces co-adaptation of features.

## Appearances

- [[Deep Learning]] — Section 7.12 provides the full derivation, interpretation as bagging, and practical guidance for where to apply dropout in deep nets.

## Notes

Dropout was standard in pre-transformer vision and NLP; modern large models often use other regularizers (weight decay, data scale, early stopping) but dropout remains common in smaller models and fine-tuning. The book connects dropout to [[Feedforward Neural Networks]] and CNN/RNN extensions.

## Related

- [[Weight Decay]]
- [[Early Stopping]]
- [[Data Augmentation]]
- [[Overfitting]]
- [[Deep Learning]]
- [[Feedforward Neural Networks]]
- [[Model Compression and Efficiency]]
