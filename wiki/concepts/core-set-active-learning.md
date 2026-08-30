# Core-Set Active Learning

**Type**: concept  
**Tags**: #concept

## Overview

Core-set active learning (Sener & Savarese, ICLR 2018) reframes acquisition as approximate **$k$-center selection**: choose $b$ labeled points so the maximum distance from any data point to its nearest center is minimized. Minimizing the core-set error bound reduces gap between training on labeled subset vs full data.

## Appearances

- [[Learning with not Enough Data Part 2: Active Learning]] — CIFAR/SVHN results; curse of dimensionality limitation; SVP proxy acceleration (Coleman et al. 2020).

## Optimization problem

At step $t$, select $\mathcal{S}^{(t+1)}$ of size $b$ minimizing:
$$\left|\frac{1}{N}\sum_{i=1}^N \mathcal{L}(\mathbf{x}_i,y_i) - \frac{1}{|\mathcal{S}^{(t)}\cup\mathcal{S}^{(t+1)}|}\sum_{j}\mathcal{L}(\mathbf{x}^l_j,y_j)\right|$$

Equivalent to $k$-center (NP-hard; greedy approximation).

## Practical notes

- Strong when class count is small
- Degrades in very high-dimensional feature spaces (Sinha et al. 2019)
- **SVP**: use smaller/weaker model as proxy for faster selection cycles

## Related

- [[Active Learning]]
- [[BADGE]]
- [[Computer Vision]]
