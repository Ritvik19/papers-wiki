# Never Give Up (NGU)

**Type**: concept  
**Tags**: #concept

## Overview

NGU (Badia et al., 2020a) is a deep RL exploration strategy that combines **two complementary novelty modules**:

1. **Episodic novelty module** (short-term): an episodic memory $M$ stores IDF state embeddings (from [[Intrinsic Curiosity Module (ICM)|ICM]]'s inverse-dynamics feature encoder). At each step, the bonus is inversely proportional to kernel similarity between the current state and its $k$ nearest neighbours in $M$:
   $$r^\text{episodic}_t \approx \frac{1}{\sqrt{\sum_{\phi_i \in N_k} K(\phi(x_t), \phi_i)} + c}$$
   using an inverse kernel with Euclidean distance. This **rapidly discourages revisiting states within one episode**.

2. **Life-long novelty module** (long-term): uses [[Random Network Distillation (RND)]] prediction error to form a scalar $\alpha_t = 1 + \frac{e^\text{RND}(s_t) - \mu_e}{\sigma_e}$ that captures how often a state has been visited **across episodes**.

The combined intrinsic reward is: $r^i_t = r^\text{episodic}_t \cdot \text{clip}(\alpha_t, 1, L)$.

NGU uses a **family of policies** trained with different $\beta$ values (weighting intrinsic vs extrinsic reward) to balance exploration and exploitation.

## Appearances

- [[Exploration Strategies in Deep Reinforcement Learning]] — Detailed description in the "Episodic Memory" section; presented as a combination of short-term and long-term novelty that addresses the drawbacks of either alone.

## Notes

- The two-timescale design neatly separates **within-episode** novelty (avoid re-visiting the same corridor) from **across-episode** novelty (stop going to already-mastered rooms across training).
- The tension between these two timescales is the core architectural contribution of NGU.
- [[Agent57]] extends NGU with a meta-controller and decomposed Q-function.

## Related

- [[Intrinsic Curiosity Module (ICM)]] — Provides the IDF embedding used by NGU's episodic module.
- [[Random Network Distillation (RND)]] — Life-long novelty component.
- [[Agent57]] — Direct successor; first DRL agent to beat humans on all 57 Atari games.
- [[Exploration Strategies in Deep Reinforcement Learning]] — Source survey.
