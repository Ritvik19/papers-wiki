# KL Divergence

**Type**: concept  
**Tags**: #concept

## Overview

Kullback–Leibler (KL) divergence measures how one probability distribution differs from a reference distribution; it is asymmetric and non-negative. In deep learning it appears in variational inference, distillation, and policy regularization.

## Appearances

- [[Deep Learning]] — Section 3.13 (information theory) defines KL divergence; later chapters use it in probabilistic and generative modeling.
- [[How to Generate Images using Autoencoders]] — VAE training adds a KL term \(-\tfrac{1}{2}\sum(1 + \log\sigma^2 - \mu^2 - e^{\log\sigma^2})\) alongside BCE reconstruction loss to regularize the latent distribution.
- [[The Theory behind Latent Variable Models: Formulating a Variational Autoencoder]] — KL appears as the **variational gap** in ELBO: \(\log p_\theta(x) - \mathrm{KL}(q_\phi(z|x) \| p_\theta(z|x))\); VAEs also use \(\mathrm{KL}(q_\phi(z|x) \| p(z))\) to regularize toward a standard normal prior.
- [[Trust Region and Proximal Policy Optimization (TRPO and PPO)]] — TRPO constrains KL(π_old, π_new) ≤ δ; early PPO penalizes KL in the surrogate objective.

## Notes

Related to [[Cross-Entropy Loss]] (cross-entropy equals entropy plus KL). Wiki RL material uses [[KL Regularization]] for policy updates; the book grounds the measure in information theory.

## Related

- [[Trust Region Policy Optimization]]
- [[Proximal Policy Optimization]]
- [[KL Regularization]]
- [[Variational Inference]]
- [[Cross-Entropy Loss]]
- [[Deep Learning]]
