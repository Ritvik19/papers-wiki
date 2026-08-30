# Variational Autoencoders

**Type**: concept  
**Tags**: #concept

## Overview

Variational autoencoders (VAEs) learn a latent generative model by maximizing a variational lower bound: an encoder outputs distribution parameters, a decoder reconstructs samples, and KL terms regularize the latent space.

## Appearances

- [[Deep Learning]] — Section 14.4 (stochastic encoders/decoders) and Chapter 19 [[Variational Inference]] provide the foundation; VAEs became standard shortly after the book's publication.
- [[How to Generate Images using Autoencoders]] — AI Summer (2018) intuitive primer: encoder outputs μ and log-variance; reparameterization \(z = \mu + \sigma \odot \epsilon\); loss = BCE reconstruction + [[KL Divergence]]; MNIST fully connected demo.
- [[The Theory behind Latent Variable Models: Formulating a Variational Autoencoder]] — AI Summer (2021) full probabilistic derivation: [[Latent Variable Models]] framework, [[ELBO]] maximization, amortized inference, reparameterization gradients, conv VAE on MNIST; loss = \(\mathbb{E}_q[\log p_\theta(x|z)] - \mathrm{KL}(q_\phi(z|x) \| p(z))\).

## Notes

The reparameterization trick decouples sampling noise from network parameters so standard backprop applies. At inference, many implementations use μ alone (no sampling) for deterministic reconstruction. Kingma & Welling (2013) introduced the VAE as auto-encoding variational Bayes.

## Related

- [[Variational Inference]]
- [[KL Divergence]]
- [[Autoencoders]]
- [[Deep Learning]]
