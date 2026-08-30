# GMPO

**Type**: concept  
**Tags**: #concept

## Overview

Geometric Mean Policy Optimization (GMPO) is a GRPO variant proposed in arXiv 2507.20673 (Zhao et al., 2025). It addresses the same high-variance token-level importance ratio problem as GSPO, but takes a different approach: instead of computing importance ratios at the sequence level, GMPO keeps token-level importance ratios and changes how they are **aggregated** within a sequence.

Standard GRPO aggregates token-level losses using an arithmetic mean, which is sensitive to outlier importance ratios. GMPO instead uses a **geometric mean**, which is inherently less sensitive to outliers. Since geometric means require non-negative inputs, GMPO computes the geometric mean over absolute values of token-level losses and then multiplies by the sign of the advantage.

Practical notes:
- Geometric mean computation is performed via log probabilities for numerical stability.
- A wider clipping range [~0.7, ~1.5] (vs. GRPO's [0.8, 1.2]) is needed, corresponding to clipping the log importance ratio within [-0.4, 0.4].
- Token-level clipping outperforms sequence-level clipping in GMPO ablations.
- Improves Pass@1 on math tasks by up to 4% absolute, with largest gains for multimodal and MoE models.

## Appearances

- [[GRPO++: Tricks for Making RL Actually Work]] — Covered in the "More Tweaks" section.

## Notes

- "Plug-and-play" replacement for GRPO's arithmetic mean aggregation.
- More stable entropy during training (positive sign of exploration).

## Related

- [[GRPO]] — Base algorithm.
- [[GSPO]] — Alternative fix for the same variance problem via sequence-level importance ratios.
