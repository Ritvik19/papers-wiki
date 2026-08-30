# Agent57

**Type**: concept  
**Tags**: #concept

## Overview

Agent57 (Badia et al., 2020b) is a deep RL agent that was the **first to achieve above-human performance on all 57 Atari benchmark games**, including hard-exploration games like Montezuma's Revenge and Pitfall that previously defied DRL.

It builds on [[Never Give Up (NGU)]] with two major improvements:

1. **Population of policies with meta-controller**: A set of $N$ policies are trained simultaneously, each parameterized by a different $(\beta_j, \gamma_j)$ pair controlling the intrinsic/extrinsic reward weighting and discount factor. A **sliding-window UCB bandit (meta-controller)** selects which policy family to prioritize during training. High-$\beta$ / low-$\gamma$ policies explore aggressively early; low-$\beta$ / high-$\gamma$ policies exploit well later.

2. **Decomposed Q-function**: The Q-value is split into intrinsic and extrinsic components:
   $$Q(s, a; \theta_j) = Q(s, a; \theta_j^e) + \beta_j Q(s, a; \theta_j^i)$$
   Each component is trained separately on $r_j^e$ and $r_j^i$, providing cleaner credit assignment.

## Appearances

- [[Exploration Strategies in Deep Reinforcement Learning]] — Presented as the culmination of the exploration research trajectory from DQN to NGU to Agent57; includes the timeline figure.

## Notes

- Agent57 is notable as a systems result: it shows that combining count-free life-long novelty ([[Random Network Distillation (RND)]]), episodic novelty ([[Never Give Up (NGU)]]), and a learned schedule of exploration policies is sufficient to crack all Atari games.
- The UCB meta-controller is a natural application of classic bandit algorithms to policy selection—a meta-level application of the same exploration-exploitation tradeoff the agent is also solving internally.

## Related

- [[Never Give Up (NGU)]] — Direct predecessor.
- [[Random Network Distillation (RND)]] — Life-long novelty module inherited from NGU.
- [[Intrinsic Curiosity Module (ICM)]] — IDF encoder inherited via NGU.
- [[Exploration Strategies in Deep Reinforcement Learning]] — Source survey.
- [[Reinforcement Learning Topic]] — Topic page for RL content.
