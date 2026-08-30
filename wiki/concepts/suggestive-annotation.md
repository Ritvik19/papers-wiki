# Suggestive Annotation

**Type**: concept  
**Tags**: #concept

## Overview

Suggestive Annotation (SA; Yang et al., MICCAI 2017) is a two-step **hybrid** active learning strategy for batch mode: (1) filter to top-$K$ most uncertain samples via ensemble disagreement; (2) from that candidate pool, greedily select $b$ samples that **maximize representativeness** over the full unlabeled set using cosine similarity in feature space (core-set-style max cover).

## Appearances

- [[Learning with not Enough Data Part 2: Active Learning]] — Greedy max-cover algorithm; NP-hard reduction; biomedical segmentation origin.

## Two-step procedure

**Step 1 — Uncertainty filter**: bootstrapped ensemble on labeled data; disagreement score → candidate pool $\mathcal{S}_c \subseteq \mathcal{U}$ of size $K$.

**Step 2 — Diversity cover**: maximize representativeness
$$F(\mathcal{S}_a, \mathcal{S}_u) = \sum_{\mathbf{x}_j \in \mathcal{S}_u} \max_{\mathbf{x}_i \in \mathcal{S}_a} \text{sim}(\mathbf{x}_i, \mathbf{x}_j)$$

Greedy: start $\mathcal{S}_a = \emptyset$, iteratively add $\mathbf{x}_i \in \mathcal{S}_c$ maximizing $F(\mathcal{S}_a \cup \{\mathbf{x}_i\}, \mathcal{S}_u)$ until $|\mathcal{S}_a| = b$.

## vs Zhdanov (2019)

| | SA | Zhdanov |
|---|-----|---------|
| Diversity mechanism | Greedy max-cover on similarities | $k$-means on prefiltered pool |
| Prefilter | Top-$K$ uncertain | Top $\beta b$ uncertain ($\beta \in [10,50]$) |

## Related

- [[Active Learning]]
- [[Core-Set Active Learning]]
- [[BADGE]]
- [[CEAL]]
