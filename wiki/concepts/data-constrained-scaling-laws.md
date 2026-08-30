# Data-Constrained Scaling Laws

**Type**: concept  
**Tags**: #concept

## Overview

Data-constrained scaling laws extend the Chinchilla parametric form when unique high-quality tokens are finite and training must repeat data across epochs. Instead of treating total tokens $D$ as equally valuable, these models discount repeated exposure and penalize over-parameterization relative to unique data $U_D$.

Muennighoff et al. (2023) decompose $D = U_D(1 + R_D)$ and replace raw $D$ and $N$ with effective quantities $D'$ and $N'$ where repeated tokens and excess parameters decay exponentially with learnable half-lives $r_D$ and $r_N$. Lovelace et al. (2026) keep the Chinchilla base terms but add an explicit penalty $P \cdot R_D^\delta \cdot (N/U_D)^\kappa$ for overfitting under repetition.

## Appearances

- [[Scaling Laws, Carefully]] — Weng survey comparing Hernandez double descent, Muennighoff effective-size decay, and Lovelace capacity-ratio penalty.
- [[Papers Explained 85 - Scaling Data-Constrained Language Models]] — original Muennighoff et al. paper page.

## Notes

- Muennighoff finds $r_N < r_D$: repeated epochs are preferable to oversized models when data is scarce.
- Lovelace shows larger models suffer more from repetition; strong weight decay mitigates the penalty.
- Both approaches are empirical fits; theoretical justification remains incomplete.

## Related

- [[Scaling Laws]]
- [[Papers Explained 49 - Chinchilla]]
- [[gzip Predicts Data-dependent Scaling Laws]]
