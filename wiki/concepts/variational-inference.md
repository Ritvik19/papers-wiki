# Variational Inference

**Type**: concept  
**Tags**: #concept

## Overview

Variational inference approximates intractable posteriors by optimizing over a simpler parametric family (e.g. factorized Gaussians) to minimize [[KL Divergence]] to the true posterior. It turns inference into optimization.

## Appearances

- [[Deep Learning]] — Chapter 19.4; used for learning deep latent-variable models and approximate Bayesian neural nets.
- [[The Theory behind Latent Variable Models: Formulating a Variational Autoencoder]] — AI Summer (2021): approximate intractable \(p_\theta(z|x)\) with \(q_\phi(z|x)\); maximize [[ELBO]]; amortized inference via neural network; alternative to MCMC.

## Notes

VAEs combine variational inference with neural encoders/decoders (stochastic autoencoders in Section 14.4). Scales better than MCMC for many high-dimensional problems. Maximizing ELBO simultaneously increases \(\log p_\theta(x)\) and reduces the variational gap \(\mathrm{KL}(q_\phi \| p_\theta(z|x))\).

## Related

- [[KL Divergence]]
- [[Expectation Maximization]]
- [[Autoencoders]]
- [[Deep Learning]]
