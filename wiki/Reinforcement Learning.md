# Reinforcement Learning

#concept

Reinforcement Learning, or RL, is a training method where a policy samples its own actions or rollouts and updates from reward feedback.

In [[On SFT RL and On-Policy Distillation]], RL is framed as sparse but relatively unbiased: many token-level gradient contributions are noisy, but large batches can let uninformative vectors cancel while reward-correlated directions survive. RL is slower than [[Supervised Fine-Tuning]] or [[On-Policy Distillation]] in some regimes, but its ceiling can be set by the verifier rather than by a fixed teacher.

[[Papers Explained: Reward Hacking in Rubric-Based RL]] shows the downside of that verifier ceiling: when the reward comes from rubrics and LLM judges, RL can learn verifier-specific false positives or over-optimize criteria that are easy to state while neglecting quality dimensions the rubric leaves implicit.

[[Reinforcement Learning from Human Feedback]] provides a full textbook treatment of RL in LLM post-training: policy gradients, reward modeling, KL-regularized optimization, and the contrast with [[Supervised Fine-Tuning]].

[[Reinforcement Learning: An Introduction]] (Sutton & Barto) is the foundational textbook: [[Multi-Armed Bandits]], [[Exploration-Exploitation Tradeoff]], [[Dynamic Programming]], [[Monte Carlo Methods]], [[Temporal-Difference Learning]], [[Sarsa]], [[Q-learning]], [[Function Approximation in RL]], [[Policy Gradient]], [[Actor-Critic Methods]], and deep RL case studies (DQN, AlphaGo).

[[Papers Explained: SFT Conflicts, RL Coexists]] uncovers the geometric and theoretical basis of multi-task RL: on-policy RL updates are sparse, bounded in $L_2$ norm by [[RL's Razor]], and practically orthogonal across reasoning tasks (cosine similarity $\approx 10^{-5}$). Standardized advantage zero-sum filtering eliminates prompt-level mean gradient interference, leading to [[Task Coexistence]] (+2.3% on untrained tasks, +24.9% multi-stage gains) and enabling decentralized [[Parallel-RL]] model merging.

## Related

- [[Reinforcement Learning: An Introduction]]
- [[Reinforcement Learning from Human Feedback]]
- [[Papers Explained: SFT Conflicts, RL Coexists]]
- [[Task Coexistence]]
- [[RL's Razor]]
- [[Parallel-RL]]
- [[Gradient Interference]]
- [[Multi-Armed Bandits]]
- [[Exploration-Exploitation Tradeoff]]
- [[Markov Decision Process]]
- [[Dynamic Programming]]
- [[Monte Carlo Methods]]
- [[Temporal-Difference Learning]]
- [[Sarsa]]
- [[Q-learning]]
- [[Policy Gradient]]
- [[Actor-Critic Methods]]
- [[REINFORCE]]
- [[Off-Policy Learning]]
- [[On-Policy Learning]]
- [[RLHF]]
- [[On SFT RL and On-Policy Distillation]]
- [[Policy Gradient]]
- [[Verifier-Bounded Learning]]
- [[Reward Hacking]]
- [[Rubric-Based Reinforcement Learning]]
- [[Reinforcement Learning Topic]]
- [[Reasoning Models]]
- [[Papers Explained - Advancing Search Augmented Language Models]]
- [[Papers Explained - Likelihood-Based Reward Designs for General LLM Reasoning]]
- [[Papers Explained - Sarvam 30B and Sarvam 105B]]
- [[Papers Explained 48 - InstructGPT]]
- [[Papers Explained 57 - LIMA]]
- [[Papers Explained 61 - Humpback]]
- [[Papers Explained 63 - LLaMA 2 Long]]
- [[Papers Explained 67 - GPT-4]]
