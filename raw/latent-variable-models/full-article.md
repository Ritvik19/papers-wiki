# The theory behind Latent Variable Models: formulating a Variational Autoencoder

**Source URL**: https://theaisummer.com/latent-variable-models/  
**Author**: Sergios Karagiannakos (AI Summer)  
**Date**: 2021-02-04

---

Over the past few years, there has been a turn in research focus towards Generative models and unsupervised learning. Generative Adversarial models and Latent Variable models have been the two most prominent architectures. In this article, we will deeply examine how latent variable models work, their core principles and we will formulate their most popular representant: Variational Autoencoders (VAE).

## Discriminative vs Generative models

Discriminative models learn \(p(y|x)\); generative models learn \(p(x)\); conditional generative models learn \(p(x|y)\). All are connected via Bayes' rule. This article focuses on generative models and derives VAEs through probabilities.

## Generative models

Goal: learn \(p(x)\) to match data distribution \(p_{data}(x)\). **Explicit density models** compute or approximate \(p(x)\) (VAEs are approximate explicit / latent-variable models). **Implicit density models** (e.g. GANs) sample without computing density.

## Latent Variable models

Latent variables \(z\) map data \(x \sim p(x)\) into a lower-dimensional space \(z \sim p(z)\). Five terms:

- Prior \(p(z)\)
- Likelihood \(p(x|z)\)
- Joint \(p(x,z) = p(x|z)p(z)\)
- Marginal \(p(x)\) — training target
- Posterior \(p(z|x)\)

**Generation**: sample \(z \sim p(z)\), then \(x \sim p(x|z)\).  
**Inference**: sample \(x \sim p(x)\), then \(z \sim p(z|x)\).

## Training with maximum likelihood

\[\theta^{ML} = \arg\max_{\theta} \sum_{i=1}^{N} \log p_{\theta}(x_i)\]

Gradient of marginal log-likelihood requires the posterior \(p(z|x)\) — the inference problem.

## Approximate inference

Most posteriors are intractable. Approximate methods include MCMC and **variational inference**.

## Variational Inference

Approximate \(p_{\theta}(z|x)\) with tractable \(q_{\phi}(z|x)\). Maximize the **Evidence Lower Bound (ELBO)**:

\[L_{\theta,\phi}(x) = \mathbb{E}_{q_{\phi}(z)} \left[ \log \frac{p_{\theta}(x,z)}{q_{\phi}(z|x)} \right] \leq \log p_{\theta}(x)\]

Equivalently:

\[L_{\theta,\phi}(x) = \log p_{\theta}(x) - \mathrm{KL}(q_{\phi}(z|x) \| p_{\theta}(z|x))\]

The KL term is the **variational gap**; maximizing ELBO increases \(\log p_{\theta}(x)\) and tightens the approximation.

## Amortized Variational Inference

Instead of per-datapoint variational parameters, train a neural **inference network** to predict \(\phi\) for any \(x\).

## Computing ELBO gradients

Model-parameter gradients via Monte Carlo samples from \(q_{\phi}(z|x)\). Variational-parameter gradients use the **reparameterization trick**: \(z = \mu + \sigma\epsilon\), \(\epsilon \sim \mathcal{N}(0,1)\), decoupling randomness from \(\phi\).

## Variational Autoencoders

TensorFlow/Keras conv VAE on MNIST:

- **Encoder** (inference network): outputs mean and log-variance of \(q_{\phi}(z|x)\)
- **Decoder** (generative network): maps \(z\) to \(p_{\theta}(x|z)\)
- **Reparameterization**: `eps * exp(logvar * .5) + mean`
- **ELBO** = reconstruction term \(\mathbb{E}_{q}[\log p_{\theta}(x|z)] - \mathrm{KL}(q_{\phi}(z|x) \| p(z))\) with standard normal prior

Training: encode → reparameterize → decode → compute ELBO → backprop. Generation: sample \(z \sim \mathcal{N}(0,I)\) or encode test samples and decode.

## References

Kingma & Welling (2013) Auto-Encoding Variational Bayes; Goodfellow et al. Deep Learning; Lilian Weng Beta-VAE post; Blei et al. Variational Inference review.
