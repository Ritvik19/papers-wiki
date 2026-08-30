# ReMixMatch

**Type**: concept  
**Tags**: #concept

## Overview

ReMixMatch (Berthelot et al., ICLR 2020) extends [[MixMatch]] with **distribution alignment** (normalize unlabeled predictions to match labeled class marginal $p(y)$) and **augmentation anchoring** (weak-augment anchor + strong CTAugment views). Adds rotation self-supervised loss and separate CE on heavily augmented unlabeled samples.

## Appearances

- [[Learning with not Enough Data Part 1: Semi-Supervised Learning]]

## Related

- [[MixMatch]]
- [[FixMatch]]
- [[Semi-Supervised Learning]]
