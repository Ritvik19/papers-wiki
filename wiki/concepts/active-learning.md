# Active Learning

**Type**: concept  
**Tags**: #concept

## Overview

Active learning selects which unlabeled examples to label under a fixed budget $B$, maximizing model improvement per annotation cost. The standard loop: train → score unlabeled pool with acquisition function $U(\mathbf{x})$ → label top-$b$ batch → repeat. Critical in domains like medical imaging where expert labels are expensive.

## Appearances

- [[Learning with not Enough Data Part 2: Active Learning]] — Deep batch-mode survey: uncertainty, diversity, model-change, hybrids.
- [[Learning with not Enough Data Part 3: Data Generation]] — GPT-3 pipeline sends high-uncertainty synthetic labels for human relabeling.

## Strategy axes

| Axis | Goal | Examples |
|------|------|----------|
| Uncertainty | Model unsure now | Entropy, margin, MC dropout, BALD |
| Diversity | Cover data manifold | Core-sets, VAAL, BADGE $k$-means++ |
| Model change | Max influence if labeled | EGL, gradient norm |
| Hybrid | Both uncertain & representative | BADGE, MAL, SA, CEAL |

## Deep learning challenges

- Softmax **overconfidence** — scores poorly calibrated
- **Batch mode** — must pick diverse batches, not just top-$b$ uncertain points
- **Compute** — ensembles accurate but costly; MC dropout practical default

## Related

- [[Semi-Supervised Learning]]
- [[BADGE]]
- [[BALD]]
- [[VAAL]]
- [[MAL]]
- [[CEAL]]
- [[Core-Set Active Learning]]
- [[MC Dropout]]
- [[Suggestive Annotation]]
- [[Synthetic Data]]
