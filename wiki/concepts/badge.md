# BADGE

**Type**: concept  
**Tags**: #concept

## Overview

Batch Active learning by Diverse Gradient Embeddings (BADGE; Ash et al., 2020) selects batches that are simultaneously **uncertain** and **diverse** by clustering gradient embeddings in the final layer. For each unlabeled $\mathbf{x}$, compute gradient $g_\mathbf{x}$ of loss w.r.t. final-layer weights using the model's predicted label; high $\|g_\mathbf{x}\|$ indicates high influence; $k$-means++ on embeddings spreads picks across gradient space.

## Appearances

- [[Learning with not Enough Data Part 2: Active Learning]] — Algorithm figure; comparison to uncertainty-only and core-set baselines.

## Two roles in one pass

| Signal | Mechanism |
|--------|-----------|
| Uncertainty | Large gradient norm $\|g_\mathbf{x}\|$ |
| Diversity | $k$-means++ over $\{g_\mathbf{x}\}$ in batch |

Avoids redundant highly-uncertain but similar points in one acquisition round.

## Related

- [[Active Learning]]
- [[BALD]]
- [[Core-Set Active Learning]]
- [[Policy Gradient]]
