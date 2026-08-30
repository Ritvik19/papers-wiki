# Scaling Laws

**Type**: concept  
**Tags**: #concept

## Overview

Scaling laws describe power-law relationships between the loss (or performance) of neural language models and three key variables: model parameter count (N), training dataset size in tokens (D), and compute budget (C ≈ 6ND FLOPs). The foundational form introduced by Kaplan et al. (2020) and refined by [[Papers Explained 49 - Chinchilla|Chinchilla]] (Hoffmann et al., 2022) is:

> L(N, D) = E + A/N^α + B/D^β

where E is the irreducible loss floor (the entropy of natural text), A and B are scaling coefficients, and α and β govern how quickly loss decreases with more parameters or data respectively.

The **compute-optimal frontier** derived from this law gives, for a fixed FLOPs budget C, the optimal split between N and D. Chinchilla concluded this split is roughly 1:1 (equal scaling of parameters and tokens), contradicting the then-common practice of over-parameterizing models relative to their training data.

## Kaplan vs. Chinchilla

Kaplan et al. (2020) fit mostly on smaller models and excluded embedding parameters from N. They reported $N_\text{opt} \propto C^{0.73}$: grow the model faster than the data. Chinchilla (2022) scanned 400+ models up to 16B parameters and used three methods ([[IsoFLOP Profiles]], fixed-N token sweeps, parametric fit) to get $N_\text{opt} \propto C^{0.5}$. Pearce & Song (2024) show much of the gap comes from embedding counting and local extrapolation in Kaplan's model-size range. See [[Scaling Laws, Carefully]] for a full synthesis.

## Data-limited regime

Classic laws assume unlimited unique tokens. When high-quality data runs out, repetition and overfitting change the frontier. Hernandez et al. (2022) observed double descent under controlled repetition. Muennighoff et al. (2023) and Lovelace et al. (2026) extend the parametric form with discounted effective data and explicit capacity-ratio penalties. See [[Data-Constrained Scaling Laws]].

## Fitting pitfalls

Extrapolation is sensitive to how parameters are counted, how loss is aggregated, rounding of fitted exponents, and which model sizes enter the fit. Besiroglu et al. (2024) replicated Chinchilla Method 3 and found optimizer and reporting choices moved the result. [[Scaling Laws, Carefully]] includes a toy simulation of these failure modes.

## Appearances

- [[Papers Explained 49 - Chinchilla]] — established the Chinchilla form of the scaling law and the 1:1 parameter-token scaling result.
- [[Scaling Laws, Carefully]] — Weng (2026) survey from early learning curves through data-limited extensions and fitting pitfalls.
- [[gzip Predicts Data-dependent Scaling Laws]] — shows that all five parameters (E, A, B, α, β) are functions of data complexity (gzip compressibility), making the compute-optimal frontier data-dependent rather than universal.
- [[Papers Explained 85 - Scaling Data-Constrained Language Models]] — extends scaling laws to the data-constrained regime.

## Notes

- The key assumption in Chinchilla — that E is "the entropy of natural text" and scaling laws are data-agnostic — is challenged by the gzip paper, which shows E and all other parameters shift with data complexity.
- α–β relationship: when α > β, the optimal frontier favors more parameters; when β > α, it favors more tokens. Compressibility affects which regime applies.
- Real-world datasets (code, web text, books) have different compressibilities and thus different optimal compute allocations.

## Related

- [[Papers Explained 49 - Chinchilla]] — the canonical scaling law reference.
- [[Scaling Laws, Carefully]] — pedagogical synthesis and reconciliation narrative.
- [[IsoFLOP Profiles]] — Chinchilla Method 2.
- [[Data-Constrained Scaling Laws]] — repetition-aware extensions.
- [[Kolmogorov Complexity]] — information-theoretic grounding for data complexity metrics.
- [[gzip Predicts Data-dependent Scaling Laws]] — extends scaling laws to be data-sensitive.
