# Gradient Interference

**Type**: concept  
**Tags**: #concept

## Overview

Gradient Interference measures the conflict between different tasks during multi-task learning, defined as the expected inner product between task gradient directions $\mathbb{E}[\langle g_i(x), g_j(x') \rangle]$ across task distributions $\mathcal{D}_i$ and $\mathcal{D}_j$.

## SFT vs. RL Mechanisms

In [[Supervised Fine-Tuning]], gradient updates target fixed expert completions $y^* \sim \pi^*$. The expected interference is **norm-limited**, bounded by the absolute magnitude of the task score functions:
$$\mathbb{E}[\langle g_i^{SFT}, g_j^{SFT} \rangle] \le M_i M_j$$
Since expert score functions have large norms and shared directional components, SFT suffers from severe cross-task conflict and catastrophic forgetting.

In **Reinforcement Learning** (e.g. [[GRPO]]), the standardized advantage function has a zero-sum property ($\sum_k \hat{A}_{i,k}(x) = 0$) that algebraically eliminates the prompt-level mean score direction $\bar{S}_i(x)$, retaining only intra-group residual vectors $\delta S_{i,k}(x)$. The expected interference is **variance-limited**:
$$\mathbb{E}[\langle g_i^{RL}, g_j^{RL} \rangle] \le \frac{V_i V_j}{G}$$
where $V_i, V_j$ bound the intra-group residual variance and $G$ is rollout group size. Because intra-group variances are small and diminish during training, RL multi-task gradients remain practically orthogonal.

## Appearances

- [[Papers Explained: SFT Conflicts, RL Coexists]] — Formalizes Theorem 4.5 establishing norm-limited vs. variance-limited multi-task interference bounds.

## Related

- [[Task Coexistence]]
- [[RL's Razor]]
- [[Parallel-RL]]
- [[GRPO]]
- [[Multi-Task Learning]]
- [[Catastrophic Forgetting]]
