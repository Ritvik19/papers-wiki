# Autoguidance

**Type**: concept  
**Tags**: #concept

## Overview

Autoguidance (Karras et al., 2024) generalizes [[Classifier-Free Guidance]] by using an **impaired version of the same conditional model** as the negative term instead of a separately trained unconditional model. The weak model makes similar but stronger errors, and CFG-style extrapolation amplifies the difference.

## Appearances

- [[An Overview of Classifier-Free Diffusion Guidance: Impaired Model Guidance with a Bad Version of Itself (Part 2)]] — Primary survey: capacity reduction, early checkpoints, post-hoc EMA tuning, ImageNet-512/64 SOTA results.
- [[An Overview of Classifier-Free Guidance for Diffusion Models]] — Referenced as concurrent work on limited-interval guidance (Kynkäänniemi et al. / Karras lineage).

## Notes

Update rule (positive/negative notation):

$$\hat{D}_{\text{out}}(x \mid \sigma) = D_{\text{neg}}(x \mid \sigma) + (1+\gamma)\left(D_{\text{pos}}(x \mid c; \sigma) - D_{\text{neg}}(x \mid c; \sigma)\right)$$

Both \(D_{\text{pos}}\) and \(D_{\text{neg}}\) are **conditional** — avoiding vanilla CFG's task discrepancy where the unconditional model must fit all classes simultaneously.

Practical recipe from EDM2 experiments:
- Negative model capacity: 30–50% of positive model parameters.
- Negative training budget: checkpoint at \(\tau \in [T/3.5, T/16]\) of full training images seen.
- Post-hoc EMA grid search over positive/negative EMA length parameters at sampling time.

Limitations: requires training or storing multiple checkpoints; impractical when only a single public weights file is available.

## Related

- [[Classifier-Free Guidance]]
- [[Perturbed Attention Guidance]]
- [[Denoising Diffusion Probabilistic Models]]
- [[An Overview of Classifier-Free Diffusion Guidance: Impaired Model Guidance with a Bad Version of Itself (Part 2)]]
