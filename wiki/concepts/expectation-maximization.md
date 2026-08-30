# Expectation Maximization

**Type**: concept  
**Tags**: #concept

## Overview

Expectation–maximization (EM) alternates an E-step (infer latent variables given parameters) and an M-step (maximize parameters given expected latents) for models with incomplete data. It climbs a lower bound on log-likelihood.

## Appearances

- [[Deep Learning]] — Section 19.2 connects EM to variational and MAP inference frameworks.

## Notes

Gaussian mixture models and factor analysis are classic EM examples; deep generative models often use amortized inference (neural nets) instead of closed-form E-steps.

## Related

- [[Variational Inference]]
- [[Maximum Likelihood Estimation]]
- [[Deep Learning]]
