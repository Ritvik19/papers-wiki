# KL Regularization

#concept

KL Regularization constrains how far a learned policy or distribution moves from a reference distribution, often using Kullback-Leibler divergence as the distance measure.

In [[On SFT RL and On-Policy Distillation]], KL is central to teacher-guided token updates and to the stability question. The article's optimal-teacher framing asks for reward improvement under a KL budget, especially when dense distillation signals might otherwise become too concentrated.

[[Reinforcement Learning from Human Feedback]] dedicates a chapter to KL in RL optimization, double regularization, and why KL-biased RL updates forget less than offline SFT.

[[Deep Learning]] defines KL divergence in information-theoretic terms (Chapter 3) and uses it in variational inference (Chapter 19); see [[KL Divergence]].

## Related

- [[KL Divergence]]
- [[Deep Learning]]
- [[Reinforcement Learning from Human Feedback]]
- [[RLHF]]
- [[On SFT RL and On-Policy Distillation]]
- [[On-Policy Distillation]]
- [[Policy Gradient]]
- [[Reinforcement Learning Topic]]
- [[Model Distillation]]
- [[Papers Explained - Composer 2]]
- [[Papers Explained 39 - DeiT]]
- [[Papers Explained 123 - WebGPT]]
- [[Papers Explained 209 - Minitron Approach in Practice]]
- [[Papers Explained 304 - Constrained Generative Policy Optimization (Mixture of Judges)]]
- [[Papers Explained 307 - Diverse Preference Optimization]]
