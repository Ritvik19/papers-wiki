# Contrastive Active Learning

**Type**: concept  
**Tags**: #concept

## Overview

Contrastive Active Learning (CAL; Margatina et al., EMNLP 2021) selects unlabeled samples that are **representationally similar to labeled neighbors but predictionally dissimilar** — "contrastive" in the sense of nearby embeddings with diverging label distributions. High average KL between $\mathbf{x}$ and its $k$ nearest labeled neighbors in feature space signals boundary/confusion regions worth labeling.

## Appearances

- [[Learning with not Enough Data Part 2: Active Learning]] — Procedure and contrastive pair definition; results often near entropy baseline on surveyed tasks.

## Contrastive pair criterion

For pair $(\mathbf{x}_i, \mathbf{x}_j)$ with different labels:
$$d(\Phi(\mathbf{x}_i), \Phi(\mathbf{x}_j)) < \epsilon \quad \text{and} \quad \text{KL}(p(y|\mathbf{x}_i) \| p(y|\mathbf{x}_j)) \to \infty$$

## Acquisition for unlabeled $\mathbf{x}$

1. Find top-$M$ nearest labeled neighbors in $\Phi(\cdot)$ feature space
2. Score $s(\mathbf{x}) = \frac{1}{M}\sum_{i=1}^M \text{KL}(p(y|\mathbf{x}^l_i) \| p(y|\mathbf{x}))$
3. Label highest $s(\mathbf{x})$ samples

Targets decision-boundary neighborhoods where the model disagrees with local labeled context despite similar appearance.

## Related

- [[Active Learning]]
- [[BALD]]
- [[Contrastive Learning]]
- [[VAAL]]
