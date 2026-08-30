# Adversarial Training

**Type**: concept  
**Tags**: #concept

## Overview

Adversarial training improves robustness by training on inputs perturbed to maximize loss (small norm-bounded perturbations). It treats robustness as part of the optimization objective rather than only evaluating on clean data.

## Appearances

- [[Deep Learning]] — Section 7.13 introduces adversarial examples and adversarial training as regularization; Goodfellow co-authored foundational work on adversarial ML.
- [[GANs in Computer Vision: Introduction to Generative Learning]] — contrasts robustness-oriented adversarial training with generative adversarial learning: a generator replaces hand-crafted perturbations to synthesize realistic samples.

## Notes

Distinct from [[Generative Adversarial Networks]] (generator vs discriminator game) though both use "adversarial" terminology. Production LLM safety uses related ideas (red-teaming, robust fine-tuning).

## Related

- [[Generative Adversarial Networks]]
- [[Deep Learning]]
- [[Ian Goodfellow]]
