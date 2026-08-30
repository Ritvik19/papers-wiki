# ELBO

**Type**: concept  
**Tags**: #concept

## Overview

The Evidence Lower Bound (ELBO) is a variational lower bound on the log marginal likelihood \(\log p_\theta(x)\). Maximizing ELBO w.r.t. model parameters \(\theta\) and variational parameters \(\phi\) improves the generative model while approximating the intractable posterior \(p_\theta(z|x)\) with \(q_\phi(z|x)\).

## Appearances

- [[Deep Learning]] — Chapter 19 on [[Variational Inference]] motivates optimizing a lower bound when the posterior is intractable.
- [[The Theory behind Latent Variable Models: Formulating a Variational Autoencoder]] — AI Summer (2021) derives ELBO as \(\mathbb{E}_{q_\phi}[\log \tfrac{p_\theta(x,z)}{q_\phi(z|x)}]\) and equivalently \(\log p_\theta(x) - \mathrm{KL}(q_\phi(z|x) \| p_\theta(z|x))\); VAE training maximizes reconstruction minus KL to prior.

## Notes

In VAEs with standard normal prior, ELBO decomposes into expected log-likelihood (reconstruction) minus \(\mathrm{KL}(q_\phi(z|x) \| \mathcal{N}(0,I))\). The KL gap between \(q_\phi\) and the true posterior shrinks as ELBO is tightened.

## Related

- [[Variational Inference]]
- [[Variational Autoencoders]]
- [[KL Divergence]]
- [[Latent Variable Models]]
