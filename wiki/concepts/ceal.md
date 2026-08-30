# CEAL

**Type**: concept  
**Tags**: #concept

## Overview

Cost-Effective Active Learning (CEAL; Yang et al., TCSVT 2016) runs **two parallel tracks** each round: (1) **active learning** — label the most uncertain unlabeled samples (human budget); (2) **pseudo labeling** — assign labels to high-confidence unlabeled samples (free). Threshold $\delta$ on prediction entropy decays over time as the model improves, expanding the pseudo-labeled pool without extra annotation cost.

## Appearances

- [[Learning with not Enough Data Part 2: Active Learning]] — Hybrid AL + SSL; fig-12 architecture diagram.
- [[Learning with not Enough Data Part 3: Data Generation]] — Conceptual cousin to GPT-3 + AL pipelines that relabel uncertain synthetic data.

## Per-round loop

```
Train classifier on L ∪ pseudo-labeled P
├── Track A: score U by uncertainty → label top-b (costs budget B)
└── Track B: if H(p(y|u)) < δ(t), add u to P with argmax label (free)
```

$\delta(t)$ decreases over training — early rounds only very confident pseudo labels; later rounds accept slightly noisier self-labels as model matures.

## Why it saves budget

| Mechanism | Labels acquired |
|-----------|-----------------|
| Uncertainty AL | Expensive human labels on informative points |
| Confident pseudo | Free labels on easy unlabeled majority |

Bridges [[Active Learning]] and [[Semi-Supervised Learning]] in one cyclic workflow — same family as [[FixMatch]]-style self-training but acquisition explicitly optimizes *which* humans label.

## Related

- [[Active Learning]]
- [[Semi-Supervised Learning]]
- [[FixMatch]]
- [[Suggestive Annotation]]
