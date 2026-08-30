# LLM-as-a-Verifier

**Type**: concept  
**Tags**: #concept

## Overview
A general-purpose verification framework that computes expectations over next-token scoring distributions to provide continuous, fine-grained rewards for reasoning and agent trajectories without specialized reward model training.

## Appearances
- [[Papers Explained 588: LLM-as-a-Verifier]] — original paper introduction by Zhang et al. (2026).

## Notes
- Decomposes verification along three complementary scaling axes: token granularity ($G$), repetitions ($K$), and criteria decomposition ($C$).
- Converts continuous scores into Bradley-Terry pairwise preferences.

## Related
- [[Probabilistic Pivot Tournament]]
- [[Value-Order Correlation]]
- [[LLM-as-a-Judge]]
