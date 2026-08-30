# Semi-Supervised Learning

**Type**: concept  
**Tags**: #concept

## Overview

Semi-supervised learning (SSL) trains on a small labeled set $\mathcal{X}$ and large unlabeled set $\mathcal{U}$, exploiting assumptions that nearby points share labels (smoothness), clusters are class-pure, and decision boundaries lie in low-density regions. The standard objective is $\mathcal{L} = \mathcal{L}_s + \mu(t)\mathcal{L}_u$ with $\mu(t)$ ramped over time.

Vision dominates SSL research; NLP more often uses pre-train + fine-tune. Two main $\mathcal{L}_u$ families: **consistency regularization** (invariance under augmentation/dropout) and **pseudo labeling** (high-confidence self-labels).

## Appearances

- [[Deep Learning]] — Sections 7.6 and 15.3 cover semi-supervised regularization and disentangling causal factors.
- [[Learning with not Enough Data Part 1: Semi-Supervised Learning]] — Full survey: Π-model → Mean Teacher → VAT/ICT/UDA; pseudo labels → Noisy Student → Meta Pseudo Labels; MixMatch → DivideMix → FixMatch; SimCLRv2 distillation.

## Method map

| Era | Representative methods |
|-----|------------------------|
| Consistency | Π-model, temporal ensembling, [[Mean Teacher]], [[Virtual Adversarial Training]], ICT, [[Unsupervised Data Augmentation]] |
| Pseudo label | Lee 2013, label propagation, self-training, [[Noisy Student]], [[Meta Pseudo Labels]] |
| Hybrid SOTA | [[MixMatch]], ReMixMatch, [[DivideMix]], [[FixMatch]] |
| Pre-train + SSL | SimCLRv2 fine-tune + distillation (Chen et al. 2020) |

## Notes

Confirmation bias is the central failure mode — mitigated by EMA teachers, dual networks (DivideMix), confidence thresholds, MixUp soft labels, and minimum labeled samples per batch. At web scale, self-supervised pre-training + self-training often supersedes dedicated SSL losses.

## Related

- [[Consistency Regularization]]
- [[FixMatch]]
- [[MixMatch]]
- [[DivideMix]]
- [[Mean Teacher]]
- [[Noisy Student]]
- [[Meta Pseudo Labels]]
- [[Virtual Adversarial Training]]
- [[Unsupervised Learning]]
- [[Transfer Learning]]
- [[Deep Learning]]
- [[Active Learning]]
- [[Learning with not Enough Data Part 2: Active Learning]]
- [[Learning with not Enough Data Part 3: Data Generation]]
