# Latent Variable Models

**Type**: concept  
**Tags**: #concept

## Overview

Latent variable models explain observed data \(x\) through unobserved variables \(z\) in a lower-dimensional space. They define a prior \(p(z)\), likelihood \(p(x|z)\), joint \(p(x,z)\), marginal \(p(x)\), and posterior \(p(z|x)\); training targets the marginal likelihood while inference estimates the posterior.

## Appearances

- [[Deep Learning]] — Chapters 14 and 19 develop autoencoders, variational inference, and deep latent-variable generative models.
- [[The Theory behind Latent Variable Models: Formulating a Variational Autoencoder]] — AI Summer (2021) full derivation: generation vs inference, MLE training, variational approximation, and VAE as amortized latent-variable model.

## Notes

**Generation**: \(z \sim p(z)\), then \(x \sim p(x|z)\). **Inference**: given \(x\), estimate \(p(z|x)\). The posterior is usually intractable, motivating [[Variational Inference]] and MCMC. [[Variational Autoencoders]] are the canonical neural amortized latent-variable model.

## Related

- [[Variational Autoencoders]]
- [[Variational Inference]]
- [[Autoencoders]]
- [[Directed Graphical Models]]
- [[Deep Learning]]
