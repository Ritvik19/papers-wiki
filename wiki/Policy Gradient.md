# Policy Gradient

#concept

Policy Gradient methods optimize a policy by estimating how changes in action probabilities affect expected reward.

In [[On SFT RL and On-Policy Distillation]], policy gradient provides the common lens for comparing [[Reinforcement Learning]], [[Supervised Fine-Tuning]], [[On-Policy Distillation]], and self-distillation. The article uses this lens to distinguish sparse/unbiased signals from dense/biased signals and to analyze when gradients become dangerously concentrated.

[[GRPO++: Tricks for Making RL Actually Work]] provides a detailed dissection of the PPO/GRPO surrogate objective and explains precisely how clipping, importance sampling, and loss normalization choices create or resolve gradient pathologies in reasoning model training.

[[Reinforcement Learning: An Introduction]] (Chapter 13) covers classical policy gradient theory: the policy gradient theorem, REINFORCE, baselines, and actor–critic methods—the algorithmic lineage behind modern LLM policy optimizers.

[[Unravel Policy Gradients and REINFORCE]] is AI Summer's 2018 pedagogical primer: policy-based vs value-based RL, the log-π gradient trick, REINFORCE on CartPole with a Keras softmax policy network, and the high-variance motivation for actor–critic methods.

[[The Idea behind Actor-Critics and How A2C and A3C Improve Them]] and [[Trust Region and Proximal Policy Optimization (TRPO and PPO)]] continue the AI Summer arc through actor–critic variance reduction and PPO-style clipped policy updates.

## Related

- [[REINFORCE]]
- [[Actor-Critic Methods]]
- [[Reinforcement Learning: An Introduction]]
- [[Richard S. Sutton]]
- [[On SFT RL and On-Policy Distillation]]
- [[Reinforcement Learning]]
- [[On-Policy Learning]]
- [[KL Regularization]]
- [[Reinforcement Learning Topic]]
- [[Reasoning Models]]
- [[GRPO]] — Group Relative Policy Optimization; a key policy gradient variant for LLMs.
- [[DAPO]] — Practical improvements to GRPO policy gradient objective.
- [[Truncated Importance Sampling]] — Corrects off-policy importance weights in GRPO.
- [[Unravel Policy Gradients and REINFORCE]] — AI Summer intro with REINFORCE code and Pong visual.
- [[Proximal Policy Optimization]] — Clipped surrogate stabilizing policy-gradient updates.
- [[The Idea behind Actor-Critics and How A2C and A3C Improve Them]] — Actor–critic hybrid reducing REINFORCE variance.
