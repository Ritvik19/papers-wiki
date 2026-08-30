# Spectrum-to-Signal Principle

**Type**: concept  
**Tags**: #concept

## Overview

The **Spectrum-to-Signal Principle (SSP)** assigns complementary roles to SFT and RL in reasoning post-training: SFT maximizes output diversity (Pass@K) to build a broad solution spectrum; RL then amplifies the correct signal (Pass@1) from that spectrum. A diversity-optimized SFT checkpoint is a better RL prerequisite than a narrow Pass@1-optimized one.

## Appearances

- [[Papers Explained 584: VibeThinker-1.5B]] — Two-stage diversity distillation + MGPO RL.
- [[Papers Explained 585: VibeThinker-3B]] — Curriculum SFT, specialist merge, multi-domain MGPO, offline self-distillation.

## Notes

Implementation uses domain specialist checkpoint selection (Pass@K probing), parameter fusion, and **MaxEnt-Guided Policy Optimization** weighting GRPO advantages toward maximum-entropy (p_c ≈ 0.5) problems.

## Related

- [[VibeThinker]]
- [[GRPO]]
- [[Reasoning Models]]
- [[Model Distillation]]
