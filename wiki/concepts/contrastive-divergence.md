# Contrastive Divergence

**Type**: concept  
**Tags**: #concept

## Overview

Contrastive divergence (CD) approximates the gradient of log-likelihood for undirected models by running a few steps of MCMC from data points and contrasting statistics of data vs model samples. CD-k uses k Gibbs steps.

## Appearances

- [[Deep Learning]] — Chapter 18.2 (with [[Restricted Boltzmann Machine]] training in Chapter 20).

## Notes

Biased but fast approximation that enabled training RBMs and deep belief nets. Largely historical for frontier generative modeling but important for understanding energy-based learning.

## Related

- [[Partition Function]]
- [[Restricted Boltzmann Machine]]
- [[Gibbs Sampling]]
- [[Deep Learning]]
