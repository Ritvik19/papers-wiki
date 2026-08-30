# DivideMix

**Type**: concept  
**Tags**: #concept

## Overview

DivideMix (Li et al., 2020) treats learning with noisy labels as semi-supervised learning: fit a two-component GMM on per-sample cross-entropy losses to split data into clean (low-loss cluster) and noisy sets, then apply SSL-style co-guessing and co-refinement across **two diverged networks** to reduce confirmation bias (analogous to Double Q-learning).

## Appearances

- [[Learning with not Enough Data Part 1: Semi-Supervised Learning]] — GMM co-divide, dual-network training diagram, algorithm figure.

## Co-divide

Per-sample loss $\ell_i = y_i^\top \log f_\theta(\mathbf{x}_i)$; GMM posterior $w_i = p_\text{GMM}(c|\ell_i)$ for clean component $c$. If $w_i > \tau$, sample is clean; else noisy/unlabeled for SSL branch.

## Dual-network mechanisms

| Stage | Action |
|-------|--------|
| Co-divide | Each net uses the other's GMM split |
| Co-refinement | Blend ground-truth $y_i$ with averaged multi-aug prediction $\hat{y}_i$, weighted by $w_i$ from peer |
| Co-guessing | Average both nets' predictions on unlabeled/noisy branch |

## Related

- [[MixMatch]]
- [[FixMatch]]
- [[Semi-Supervised Learning]]
- [[Co-teaching]]
