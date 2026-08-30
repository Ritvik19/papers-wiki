# Reinforcement Learning: An Introduction

**Source**: `raw/reinforcement-learning-an-introduction/Reinforcement Learning - An Introduction.pdf`  
**Authors**: Richard S. Sutton and Andrew G. Barto  
**Edition**: Second edition (MIT Press, 2018)  
**Ingested**: 2026-05-19  
**Tags**: #summary

## Summary

*Reinforcement Learning: An Introduction* (Sutton & Barto, 2nd ed.) is the canonical textbook for classical reinforcement learning. Across 548 pages and 17 chapters it builds RL from first principles: an agent interacts with an environment, receives scalar rewards, and must learn a policy that maximizes long-term return. The book's organizing idea is the **agent–environment interface** formalized as a [[Markov Decision Process]], with value functions, Bellman equations, and optimality conditions as the mathematical backbone.

Part I (Chapters 2–8) covers **tabular** methods: multi-armed bandits for the exploration–exploitation tradeoff; dynamic programming for exact planning when the model is known; Monte Carlo methods for learning from complete episodes; temporal-difference (TD) learning for bootstrapped online updates (Sarsa, [[Q-learning]], Expected Sarsa); n-step returns; and integrated planning/learning (Dyna, prioritized sweeping, RTDP). Part II (Chapters 9–13) scales to large problems via **function approximation** (linear methods, tile coding, neural networks), off-policy learning with importance sampling and the deadly triad, policy-gradient and actor–critic methods (REINFORCE, natural policy gradients), and applications including the famous backgammon program TD-Gammon.

Part III connects RL to psychology and neuroscience (Chapters 14–15), surveys landmark applications from Samuel's checkers player through Watson, Atari DQN, and **AlphaGo / AlphaGo Zero** (Chapter 16), and closes with frontiers: options and temporal abstraction, reward design, and remaining open problems (Chapter 17). For readers of this wiki's LLM-focused RL material ([[Reinforcement Learning from Human Feedback]], [[GRPO]], [[Reinforcement Learning Topic]]), Sutton & Barto supplies the foundational vocabulary—returns, bootstrapping, on-policy vs off-policy control, value vs policy methods, and the exploration problem—that modern post-training algorithms inherit and reinterpret at scale.

## Key Claims

- RL is distinguished from supervised learning by **trial-and-error interaction** and **delayed reward**; the agent must discover which actions produce reward, not merely imitate labeled outputs.
- The **Markov decision process** formalism (states, actions, rewards, transition dynamics, discount factor γ) unifies episodic and continuing tasks and defines policies, value functions, and optimality via Bellman equations.
- **Dynamic programming** (policy iteration, value iteration) solves MDPs exactly when the model is known; it provides the backup-diagram intuition that TD and Monte Carlo methods approximate from samples.
- **Monte Carlo** methods learn from complete episode returns; **temporal-difference** methods bootstrap from successor estimates—TD can learn online, before episode end, and often with lower variance than MC in practice.
- **Q-learning** is an off-policy TD control algorithm that converges to q* under standard conditions; **Sarsa** is on-policy and accounts for the exploration policy's consequences.
- The **exploration–exploitation** dilemma appears first in bandits (ε-greedy, UCB, gradient bandits, contextual bandits) and persists throughout control; optimistic initialization and upper-confidence bounds are practical tools.
- **Function approximation** is necessary for large state spaces but introduces instability when combined with bootstrapping and off-policy learning—the **deadly triad** (Chapter 11).
- **Policy gradient** methods optimize parameterized policies directly, enabling stochastic policies and continuous action spaces; actor–critic architectures combine policy gradients with learned value baselines.
- **Eligibility traces** provide a backward-view mechanism unifying TD and Monte Carlo; n-step methods provide a forward-view bridge (Chapter 12).
- Deep RL milestones in the 2nd edition—including **DQN**, **AlphaGo**, and **AlphaGo Zero**—illustrate how value learning, planning, and self-play combine at scale.
- RL connects to animal learning (Rescorla–Wagner, TD models of classical conditioning) and to dopamine **reward prediction error** signals in neuroscience.

## Figures

99 image assets in `wiki/assets/reinforcement-learning-an-introduction/` (`fig-1`–`fig-99`), mapped to the book's numbered figures where possible. Captions are from the textbook's `Figure X.Y:` labels (with manual fixes where PDF line breaks truncated them).

### Extracted assets

| Asset | Caption | Page |
|-------|---------|------|
| ![fig-1](../assets/reinforcement-learning-an-introduction/fig-1.webp) | **Figure 2.4**: Average performance of UCB action selection on the 10-armed testbed. | 58 |
| ![fig-2](../assets/reinforcement-learning-an-introduction/fig-2.webp) | **Figure 2.5**: Average performance of the gradient bandit algorithm with and without a reward baseline on the 10-armed testbed. | 60 |
| ![fig-3](../assets/reinforcement-learning-an-introduction/fig-3.webp) | **Figure 2.5** (panel 2): Average performance of the gradient bandit algorithm with and without a reward baseline on the 10-armed testbed. | 60 |
| ![fig-4](../assets/reinforcement-learning-an-introduction/fig-4.webp) | **Figure 3.1**: The agent–environment interaction in a Markov decision process. | 70 |
| ![fig-5](../assets/reinforcement-learning-an-introduction/fig-5.webp) | **Figure 3.1** (panel 2): The agent–environment interaction in a Markov decision process. | 70 |
| ![fig-6](../assets/reinforcement-learning-an-introduction/fig-6.webp) | **Figure 5.1**: Approximate state-value functions for the blackjack policy that sticks only on 20 or 21, computed by Monte Carlo policy evaluation. | 117 |
| ![fig-7](../assets/reinforcement-learning-an-introduction/fig-7.webp) | **Figure 5.1**: Approximate state-value functions for the blackjack policy that sticks only on 20 or 21, computed by Monte Carlo policy evaluation. | 117 |
| ![fig-8](../assets/reinforcement-learning-an-introduction/fig-8.webp) | **Figure 5.3**: Weighted importance sampling produces lower error estimates of the value of a single blackjack state from off-policy episodes. | 128 |
| ![fig-9](../assets/reinforcement-learning-an-introduction/fig-9.webp) | **Figure 5.4**: Ordinary importance sampling produces surprisingly unstable estimates on the one-state MDP shown inset. | 129 |
| ![fig-10](../assets/reinforcement-learning-an-introduction/fig-10.webp) | **Figure 6.5**: Comparison of Q-learning and Double Q-learning on a simple episodic MDP. | 157 |
| ![fig-11](../assets/reinforcement-learning-an-introduction/fig-11.webp) | **Figure 7.2**: Performance of n-step TD methods as a function of α, for various values of n, on a 19-state random walk task. | 167 |
| ![fig-12](../assets/reinforcement-learning-an-introduction/fig-12.webp) | **Figure 8.11**: A slice through the space of reinforcement learning methods, highlighting depth and width of updates. | 212 |
| ![fig-13](../assets/reinforcement-learning-an-introduction/fig-13.webp) | **Figure 8.11** (panel 2): A slice through the space of reinforcement learning methods, highlighting depth and width of updates. | 212 |
| ![fig-14](../assets/reinforcement-learning-an-introduction/fig-14.webp) | **Figure 9.1**: Function approximation by state aggregation on the 1000-state random walk task. | 226 |
| ![fig-15](../assets/reinforcement-learning-an-introduction/fig-15.webp) | **Figure 9.2**: Bootstrapping with state aggregation on the 1000-state random walk task. | 230 |
| ![fig-16](../assets/reinforcement-learning-an-introduction/fig-16.webp) | **Figure 9.2** (panel 2): Bootstrapping with state aggregation on the 1000-state random walk task. | 230 |
| ![fig-17](../assets/reinforcement-learning-an-introduction/fig-17.webp) | **Figure 9.4**: A selection of six two-dimensional Fourier cosine features, each labeled by the vector cᵢ that defines it. | 235 |
| ![fig-18](../assets/reinforcement-learning-an-introduction/fig-18.webp) | **Figure 9.4** (panel 2): A selection of six two-dimensional Fourier cosine features, each labeled by the vector cᵢ that defines it. | 235 |
| ![fig-19](../assets/reinforcement-learning-an-introduction/fig-19.webp) | **Figure 9.4** (panel 3): A selection of six two-dimensional Fourier cosine features, each labeled by the vector cᵢ that defines it. | 235 |
| ![fig-20](../assets/reinforcement-learning-an-introduction/fig-20.webp) | **Figure 9.4** (panel 4): A selection of six two-dimensional Fourier cosine features, each labeled by the vector cᵢ that defines it. | 235 |
| ![fig-21](../assets/reinforcement-learning-an-introduction/fig-21.webp) | **Figure 9.4** (panel 5): A selection of six two-dimensional Fourier cosine features, each labeled by the vector cᵢ that defines it. | 235 |
| ![fig-22](../assets/reinforcement-learning-an-introduction/fig-22.webp) | **Figure 9.4** (panel 6): A selection of six two-dimensional Fourier cosine features, each labeled by the vector cᵢ that defines it. | 235 |
| ![fig-23](../assets/reinforcement-learning-an-introduction/fig-23.webp) | **Figure 9.4** (panel 7): A selection of six two-dimensional Fourier cosine features, each labeled by the vector cᵢ that defines it. | 235 |
| ![fig-24](../assets/reinforcement-learning-an-introduction/fig-24.webp) | **Figure 9.4** (panel 8): A selection of six two-dimensional Fourier cosine features, each labeled by the vector cᵢ that defines it. | 235 |
| ![fig-25](../assets/reinforcement-learning-an-introduction/fig-25.webp) | **Figure 9.4** (panel 9): A selection of six two-dimensional Fourier cosine features, each labeled by the vector cᵢ that defines it. | 235 |
| ![fig-26](../assets/reinforcement-learning-an-introduction/fig-26.webp) | **Figure 9.4** (panel 10): A selection of six two-dimensional Fourier cosine features, each labeled by the vector cᵢ that defines it. | 235 |
| ![fig-27](../assets/reinforcement-learning-an-introduction/fig-27.webp) | **Figure 9.4** (panel 11): A selection of six two-dimensional Fourier cosine features, each labeled by the vector cᵢ that defines it. | 235 |
| ![fig-28](../assets/reinforcement-learning-an-introduction/fig-28.webp) | **Figure 9.5**: Fourier basis vs polynomials on the 1000-state random walk. | 236 |
| ![fig-29](../assets/reinforcement-learning-an-introduction/fig-29.webp) | **Figure 9.10**: Why we use coarse coding. | 240 |
| ![fig-30](../assets/reinforcement-learning-an-introduction/fig-30.webp) | **Figure 9.15**: Deep Convolutional Network. | 249 |
| ![fig-31](../assets/reinforcement-learning-an-introduction/fig-31.webp) | **Figure 10.1**: The Mountain Car task (upper left panel) and the cost-to-go function learned during one run. | 267 |
| ![fig-32](../assets/reinforcement-learning-an-introduction/fig-32.webp) | **Figure 10.2**: Mountain Car learning curves for the semi-gradient Sarsa method with tile-coding function approximation. | 268 |
| ![fig-33](../assets/reinforcement-learning-an-introduction/fig-33.webp) | **Figure 10.3**: Performance of one-step vs 8-step semi-gradient Sarsa on the Mountain Car task. | 270 |
| ![fig-34](../assets/reinforcement-learning-an-introduction/fig-34.webp) | **Figure 10.4**: Effect of α and n on early performance of n-step semi-gradient Sarsa on the Mountain Car task. | 270 |
| ![fig-35](../assets/reinforcement-learning-an-introduction/fig-35.webp) | **Figure 10.5**: The policy and value function found by differential semi-gradient one-step Sarsa on the access-control queuing task. | 274 |
| ![fig-36](../assets/reinforcement-learning-an-introduction/fig-36.webp) | **Figure 11.2**: Demonstration of instability on Baird’s counterexample. | 284 |
| ![fig-37](../assets/reinforcement-learning-an-introduction/fig-37.webp) | **Figure 11.2** (panel 2): Demonstration of instability on Baird’s counterexample. | 284 |
| ![fig-38](../assets/reinforcement-learning-an-introduction/fig-38.webp) | **Figure 11.5**: The behavior of the TDC algorithm on Baird’s counterexample. | 302 |
| ![fig-39](../assets/reinforcement-learning-an-introduction/fig-39.webp) | **Figure 11.5** (panel 2): The behavior of the TDC algorithm on Baird’s counterexample. | 302 |
| ![fig-40](../assets/reinforcement-learning-an-introduction/fig-40.webp) | **Figure 11.6**: The behavior of the one-step Emphatic-TD algorithm in expectation on Baird's counterexample. | 305 |
| ![fig-41](../assets/reinforcement-learning-an-introduction/fig-41.webp) | **Figure 12.3**: 19-state random walk: performance of the offline λ-return algorithm. | 313 |
| ![fig-42](../assets/reinforcement-learning-an-introduction/fig-42.webp) | **Figure 12.6**: 19-state random walk: performance of TD(λ) alongside the offline λ-return algorithm. | 317 |
| ![fig-43](../assets/reinforcement-learning-an-introduction/fig-43.webp) | **Figure 12.8**: 19-state random walk: performance of online and offline λ-return algorithms. | 321 |
| ![fig-44](../assets/reinforcement-learning-an-introduction/fig-44.webp) | **Figure 12.10**: Early performance on the Mountain Car task of Sarsa(λ) with replacing traces. | 328 |
| ![fig-45](../assets/reinforcement-learning-an-introduction/fig-45.webp) | **Figure 12.14**: The effect of λ on reinforcement learning performance in four different test problems. | 345 |
| ![fig-46](../assets/reinforcement-learning-an-introduction/fig-46.webp) | **Figure 13.1**: REINFORCE on the short-corridor gridworld (Example 13.1). | 350 |
| ![fig-47](../assets/reinforcement-learning-an-introduction/fig-47.webp) | **Figure 13.2**: Adding a baseline to REINFORCE can make it learn much faster, as illustrated on the short-corridor gridworld. | 352 |
| ![fig-48](../assets/reinforcement-learning-an-introduction/fig-48.webp) | **Figure 14.2**: Temporal primacy overriding blocking in the TD model. | 375 |
| ![fig-49](../assets/reinforcement-learning-an-introduction/fig-49.webp) | **Figure 14.2**: Temporal primacy overriding blocking in the TD model. | 375 |
| ![fig-50](../assets/reinforcement-learning-an-introduction/fig-50.webp) | **Figure 14.2**: Temporal primacy overriding blocking in the TD model. | 375 |
| ![fig-51](../assets/reinforcement-learning-an-introduction/fig-51.webp) | **Figure 14.2**: Temporal primacy overriding blocking in the TD model. | 376 |
| ![fig-52](../assets/reinforcement-learning-an-introduction/fig-52.webp) | **Figure 14.3**: Second-order conditioning with the TD model. | 377 |
| ![fig-53](../assets/reinforcement-learning-an-introduction/fig-53.webp) | **Figure 14.4**: Time course of US prediction over the course of acquisition for the TD model | 378 |
| ![fig-54](../assets/reinforcement-learning-an-introduction/fig-54.webp) | **Figure 14.4**: Time course of US prediction over the course of acquisition for the TD model | 380 |
| ![fig-55](../assets/reinforcement-learning-an-introduction/fig-55.webp) | **Figure 14.5**: Model-based and model-free strategies to solve a hypothetical sequential action-selection task. | 387 |
| ![fig-56](../assets/reinforcement-learning-an-introduction/fig-56.webp) | **Figure 14.5** (panel 2): Model-based and model-free strategies to solve a hypothetical sequential action-selection task. | 387 |
| ![fig-57](../assets/reinforcement-learning-an-introduction/fig-57.webp) | **Figure 14.5** (panel 3): Model-based and model-free strategies to solve a hypothetical sequential action-selection task. | 387 |
| ![fig-58](../assets/reinforcement-learning-an-introduction/fig-58.webp) | **Figure 14.5** (panel 4): Model-based and model-free strategies to solve a hypothetical sequential action-selection task. | 387 |
| ![fig-59](../assets/reinforcement-learning-an-introduction/fig-59.webp) | **Figure 14.5** (panel 5): Model-based and model-free strategies to solve a hypothetical sequential action-selection task. | 387 |
| ![fig-60](../assets/reinforcement-learning-an-introduction/fig-60.webp) | **Figure 14.5** (panel 6): Model-based and model-free strategies to solve a hypothetical sequential action-selection task. | 387 |
| ![fig-61](../assets/reinforcement-learning-an-introduction/fig-61.webp) | **Figure 14.5** (panel 7): Model-based and model-free strategies to solve a hypothetical sequential action-selection task. | 387 |
| ![fig-62](../assets/reinforcement-learning-an-introduction/fig-62.webp) | **Figure 14.5** (panel 8): Model-based and model-free strategies to solve a hypothetical sequential action-selection task. | 387 |
| ![fig-63](../assets/reinforcement-learning-an-introduction/fig-63.webp) | **Figure 14.5** (panel 9): Model-based and model-free strategies to solve a hypothetical sequential action-selection task. | 387 |
| ![fig-64](../assets/reinforcement-learning-an-introduction/fig-64.webp) | **Figure 14.5** (panel 10): Model-based and model-free strategies to solve a hypothetical sequential action-selection task. | 387 |
| ![fig-65](../assets/reinforcement-learning-an-introduction/fig-65.webp) | **Figure 14.5** (panel 11): Model-based and model-free strategies to solve a hypothetical sequential action-selection task. | 387 |
| ![fig-66](../assets/reinforcement-learning-an-introduction/fig-66.webp) | **Figure 15.1**: Spine of a striatal neuron showing input from both cortical and dopamine neurons. | 407 |
| ![fig-67](../assets/reinforcement-learning-an-introduction/fig-67.webp) | **Figure 15.1**: Spine of a striatal neuron showing input from both cortical and dopamine neurons. | 408 |
| ![fig-68](../assets/reinforcement-learning-an-introduction/fig-68.webp) | **Figure 15.2**: The response of dopamine neurons shifts from initial responses to primary reward | 410 |
| ![fig-69](../assets/reinforcement-learning-an-introduction/fig-69.webp) | **Figure 15.3**: The response of dopamine neurons drops below baseline at the expected time of reward if the reward is omitted. | 411 |
| ![fig-70](../assets/reinforcement-learning-an-introduction/fig-70.webp) | **Figure 15.4**: The behavior of the TD error δ during TD learning is consistent with features of dopamine responses. | 413 |
| ![fig-71](../assets/reinforcement-learning-an-introduction/fig-71.webp) | **Figure 15.5**: Actor–critic ANN and a hypothetical neural implementation. | 418 |
| ![fig-72](../assets/reinforcement-learning-an-introduction/fig-72.webp) | **Figure 15.5** (panel 2): Actor–critic ANN and a hypothetical neural implementation. | 418 |
| ![fig-73](../assets/reinforcement-learning-an-introduction/fig-73.webp) | **Figure 15.5** (panel 3): Actor–critic ANN and a hypothetical neural implementation. | 418 |
| ![fig-74](../assets/reinforcement-learning-an-introduction/fig-74.webp) | **Figure 15.5** (panel 4): Actor–critic ANN and a hypothetical neural implementation. | 418 |
| ![fig-75](../assets/reinforcement-learning-an-introduction/fig-75.webp) | **Figure 15.5** (panel 5): Actor–critic ANN and a hypothetical neural implementation. | 418 |
| ![fig-76](../assets/reinforcement-learning-an-introduction/fig-76.webp) | **Figure 15.5** (panel 6): Actor–critic ANN and a hypothetical neural implementation. | 418 |
| ![fig-77](../assets/reinforcement-learning-an-introduction/fig-77.webp) | **Figure 15.5** (panel 7): Actor–critic ANN and a hypothetical neural implementation. | 418 |
| ![fig-78](../assets/reinforcement-learning-an-introduction/fig-78.webp) | **Figure 15.5** (panel 8): Actor–critic ANN and a hypothetical neural implementation. | 418 |
| ![fig-79](../assets/reinforcement-learning-an-introduction/fig-79.webp) | **Figure 15.5** (panel 9): Actor–critic ANN and a hypothetical neural implementation. | 418 |
| ![fig-80](../assets/reinforcement-learning-an-introduction/fig-80.webp) | **Figure 16.3**: High-level view of the reinforcement learning DRAM controller. | 455 |
| ![fig-81](../assets/reinforcement-learning-an-introduction/fig-81.webp) | **Figure 16.4**: Performances of four controllers over a suite of 9 simulated benchmark applications. | 457 |
| ![fig-82](../assets/reinforcement-learning-an-introduction/fig-82.webp) | **Figure 16.6**: AlphaGo pipeline (policy and value networks, MCTS, self-play). Adapted from Silver et al., Nature 2016. | 467 |
| ![fig-83](../assets/reinforcement-learning-an-introduction/fig-83.webp) | **Figure 16.6** (panel 2): AlphaGo pipeline (policy and value networks, MCTS, self-play). Adapted from Silver et al., Nature 2016. | 467 |
| ![fig-84](../assets/reinforcement-learning-an-introduction/fig-84.webp) | **Figure 16.6** (panel 3): AlphaGo pipeline (policy and value networks, MCTS, self-play). Adapted from Silver et al., Nature 2016. | 467 |
| ![fig-85](../assets/reinforcement-learning-an-introduction/fig-85.webp) | **Figure 16.6** (panel 4): AlphaGo pipeline (policy and value networks, MCTS, self-play). Adapted from Silver et al., Nature 2016. | 467 |
| ![fig-86](../assets/reinforcement-learning-an-introduction/fig-86.webp) | **Figure 16.6** (panel 5): AlphaGo pipeline (policy and value networks, MCTS, self-play). Adapted from Silver et al., Nature 2016. | 467 |
| ![fig-87](../assets/reinforcement-learning-an-introduction/fig-87.webp) | **Figure 16.6** (panel 6): AlphaGo pipeline (policy and value networks, MCTS, self-play). Adapted from Silver et al., Nature 2016. | 467 |
| ![fig-88](../assets/reinforcement-learning-an-introduction/fig-88.webp) | **Figure 16.7**: AlphaGo Zero self-play reinforcement learning. | 470 |
| ![fig-89](../assets/reinforcement-learning-an-introduction/fig-89.webp) | **Figure 16.8**: Click through rate (CTR) versus life-time value (LTV). | 475 |
| ![fig-90](../assets/reinforcement-learning-an-introduction/fig-90.webp) | **Figure 16.9**: Thermal soaring model: snapshot of the vertical velocity field and sample trajectories. | 476 |
| ![fig-91](../assets/reinforcement-learning-an-introduction/fig-91.webp) | **Figure 16.10**: Sample thermal soaring trajectories, with arrows showing wind direction. | 478 |
| ![fig-92](../assets/reinforcement-learning-an-introduction/fig-92.webp) | **Figure 17.1**: A conceptual agent architecture including a model, a planner, and a state-update function. | 489 |
| ![fig-93](../assets/reinforcement-learning-an-introduction/fig-93.webp) | **Figure 3.1** (full-page render): The agent–environment interaction in a Markov decision process. | 70 |
| ![fig-94](../assets/reinforcement-learning-an-introduction/fig-94.webp) | **Figure 3.2** (full-page render): Gridworld example: exceptional reward dynamics (left) and state-value function for the equiprobable random policy (right). | 82 |
| ![fig-95](../assets/reinforcement-learning-an-introduction/fig-95.webp) | **Figure 6.1** (full-page render): Changes recommended in the driving home example by Monte Carlo methods (left) | 145 |
| ![fig-96](../assets/reinforcement-learning-an-introduction/fig-96.webp) | **Figure 6.4** (full-page render): The backup diagrams for Q-learning and Expected Sarsa. | 156 |
| ![fig-97](../assets/reinforcement-learning-an-introduction/fig-97.webp) | **Figure 13.1** (full-page render): REINFORCE on the short-corridor gridworld (Example 13.1). | 324 |
| ![fig-98](../assets/reinforcement-learning-an-introduction/fig-98.webp) | **Figure 9.15** (full-page render): Deep Convolutional Network. | 256 |
| ![fig-99](../assets/reinforcement-learning-an-introduction/fig-99.webp) | **Figure 16.6** (full-page render): AlphaGo pipeline (policy and value networks, MCTS, self-play). Adapted from Silver et al., Nature 2016. | 441 |

### Book figure index (104 numbered figures)

- **Figure 1.1** (Ch. 1): A sequence of tic-tac-toe moves.
- **Figure 2.1** (Ch. 2): An example bandit problem from the 10-armed testbed.
- **Figure 2.2** (Ch. 2): Average performance of "-greedy action-value methods on the 10-armed testbed.
- **Figure 2.3** (Ch. 2): The e↵ect of optimistic initial action-value estimates on the 10-armed testbed.
- **Figure 2.4** (Ch. 2): Average performance of UCB action selection on the 10-armed testbed.
- **Figure 2.5** (Ch. 2): Average performance of the gradient bandit algorithm with and without a reward baseline on the 10-armed testbed.
- **Figure 2.6** (Ch. 2): A parameter study of the various bandit algorithms presented in this chapter.
- **Figure 3.1** (Ch. 3): The agent–environment interaction in a Markov decision process.
- **Figure 3.2** (Ch. 3): Gridworld example: exceptional reward dynamics (left) and state-value function for the equiprobable random policy (right).
- **Figure 3.3** (Ch. 3): A golf example: the state-value function for putting (upper) and the optimal action-value function for using the driver (lower).
- **Figure 3.4** (Ch. 3): Backup diagrams for v⇤and q⇤
- **Figure 3.5** (Ch. 3): Optimal solutions to the gridworld example.
- **Figure 4.1** (Ch. 4): Convergence of iterative policy evaluation on a small gridworld.
- **Figure 4.2** (Ch. 4): The sequence of policies found by policy iteration on Jack's car rental problem.
- **Figure 4.3** (Ch. 4): The solution to the gambler's problem for p_h = 0.4.
- **Figure 5.1** (Ch. 5): Approximate state-value functions for the blackjack policy that sticks only on 20 or 21, computed by Monte Carlo policy evaluation.
- **Figure 5.2** (Ch. 5): The optimal policy and state-value function for blackjack, found by Monte Carlo
- **Figure 5.3** (Ch. 5): Weighted importance sampling produces lower error estimates of the value of a single blackjack state from off-policy episodes.
- **Figure 5.4** (Ch. 5): Ordinary importance sampling produces surprisingly unstable estimates on the one-state MDP shown inset.
- **Figure 5.5** (Ch. 5): A couple of right turns for the racetrack task.
- **Figure 6.1** (Ch. 6): Changes recommended in the driving home example by Monte Carlo methods (left)
- **Figure 6.2** (Ch. 6): Performance of TD(0) and constant-α MC under batch training on the random walk task.
- **Figure 6.3** (Ch. 6): Interim and asymptotic performance of TD control methods on the cli↵-walking
- **Figure 6.4** (Ch. 6): The backup diagrams for Q-learning and Expected Sarsa.
- **Figure 6.5** (Ch. 6): Comparison of Q-learning and Double Q-learning on a simple episodic MDP.
- **Figure 7.1** (Ch. 7): The backup diagrams of n-step methods.
- **Figure 7.2** (Ch. 7): Performance of n-step TD methods as a function of α, for various values of n, on a 19-state random walk task.
- **Figure 7.3** (Ch. 7): The backup diagrams for the spectrum of n-step methods for state–action values.
- **Figure 7.4** (Ch. 7): Gridworld example of the speedup of policy learning due to the use of n-step
- **Figure 7.5** (Ch. 7): The backup diagrams of the three kinds of n-step action-value updates considered
- **Figure 8.1** (Ch. 8): The general Dyna Architecture.
- **Figure 8.2** (Ch. 8): A simple maze (inset) and the average learning curves for Dyna-Q agents varying
- **Figure 8.3** (Ch. 8): Policies found by planning and nonplanning Dyna-Q agents halfway through the
- **Figure 8.4** (Ch. 8): Average performance of Dyna agents on a blocking task.
- **Figure 8.5** (Ch. 8): Average performance of Dyna agents on a shortcut task.
- **Figure 8.6** (Ch. 8): Backup diagrams for all the one-step updates.
- **Figure 8.7** (Ch. 8): Comparison of eﬃciency of expected and sample updates.
- **Figure 8.8** (Ch. 8): Relative efficiency of updates distributed uniformly across the state space.
- **Figure 8.9** (Ch. 8): Heuristic search can be implemented as a sequence of one-step updates (shown
- **Figure 8.10** (Ch. 8): 1. Selection. Starting at the root node, a tree policy based on the action values
- **Figure 8.11** (Ch. 8): A slice through the space of reinforcement learning methods, highlighting depth and width of updates.
- **Figure 9.1** (Ch. 9): Function approximation by state aggregation on the 1000-state random walk task.
- **Figure 9.2** (Ch. 9): Bootstrapping with state aggregation on the 1000-state random walk task.
- **Figure 9.3** (Ch. 9): One-dimensional Fourier cosine-basis features xi, i = 1, 2, 3, 4, for approximating
- **Figure 9.4** (Ch. 9): A selection of six two-dimensional Fourier cosine features, each labeled by the vector cᵢ that defines it.
- **Figure 9.5** (Ch. 9): Fourier basis vs polynomials on the 1000-state random walk.
- **Figure 9.6** (Ch. 9): Coarse coding. Generaliza-
- **Figure 9.7** (Ch. 9): Generalization in linear function approximation methods is determined by the
- **Figure 9.8** (Ch. 9): Example of feature width’s strong e↵ect on initial generalization (ﬁrst row) and
- **Figure 9.9** (Ch. 9): Multiple, overlapping grid-tilings on a limited two-dimensional space.
- **Figure 9.10** (Ch. 9): Why we use coarse coding.
- **Figure 9.11** (Ch. 9): Why tile asymmetrical o↵sets are preferred in tile coding.
- **Figure 9.12** (Ch. 9): Tilings need not be grids.
- **Figure 9.13** (Ch. 9): One-dimensional radial basis functions.
- **Figure 9.14** (Ch. 9): A generic feedforward ANN with four input units, two output units, and two
- **Figure 9.15** (Ch. 9): Deep Convolutional Network.
- **Figure 10.1** (Ch. 10): The Mountain Car task (upper left panel) and the cost-to-go function learned during one run.
- **Figure 10.2** (Ch. 10): Mountain Car learning curves for the semi-gradient Sarsa method with tile-coding function approximation.
- **Figure 10.3** (Ch. 10): Performance of one-step vs 8-step semi-gradient Sarsa on the Mountain Car task.
- **Figure 10.4** (Ch. 10): Effect of α and n on early performance of n-step semi-gradient Sarsa on the Mountain Car task.
- **Figure 10.5** (Ch. 10): The policy and value function found by differential semi-gradient one-step Sarsa on the access-control queuing task.
- **Figure 11.1** (Ch. 11): Baird’s counterexample.
- **Figure 11.2** (Ch. 11): Demonstration of instability on Baird’s counterexample.
- **Figure 11.3** (Ch. 11): The geometry of linear value-function approximation.
- **Figure 11.4** (Ch. 11): Causal relationships among the data distribution, MDPs, and various objectives.
- **Figure 11.5** (Ch. 11): The behavior of the TDC algorithm on Baird’s counterexample.
- **Figure 11.6** (Ch. 11): The behavior of the one-step Emphatic-TD algorithm in expectation on Baird's counterexample.
- **Figure 12.1** (Ch. 12): The backup digram for TD(λ).
- **Figure 12.2** (Ch. 12): Weighting given in the λ-return to each of the n-step returns.
- **Figure 12.3** (Ch. 12): 19-state random walk: performance of the offline λ-return algorithm.
- **Figure 12.4** (Ch. 12): The forward view. We decide how to update each state by looking forward to
- **Figure 12.5** (Ch. 12): The backward or mechanistic view of TD(λ).
- **Figure 12.6** (Ch. 12): 19-state random walk: performance of TD(λ) alongside the offline λ-return algorithm.
- **Figure 12.7** (Ch. 12): The backup diagram for truncated TD(λ).
- **Figure 12.8** (Ch. 12): 19-state random walk: performance of online and offline λ-return algorithms.
- **Figure 12.9** (Ch. 12): Sarsa(λ)’s backup diagram.
- **Figure 12.10** (Ch. 12): Early performance on the Mountain Car task of Sarsa(λ) with replacing traces.
- **Figure 12.11** (Ch. 12): Summary comparison of Sarsa(λ) algorithms on the Mountain Car task.
- **Figure 12.12** (Ch. 12): The backup diagram for Watkins’s Q(λ).
- **Figure 12.13** (Ch. 12): The backup diagram for the λ version of the Tree Backup algorithm.
- **Figure 12.14** (Ch. 12): The effect of λ on reinforcement learning performance in four different test problems.
- **Figure 13.1** (Ch. 13): REINFORCE on the short-corridor gridworld (Example 13.1).
- **Figure 13.2** (Ch. 13): Adding a baseline to REINFORCE can make it learn much faster, as illustrated on the short-corridor gridworld.
- **Figure 14.1** (Ch. 14): Three stimulus representations (in columns) sometimes used with the TD model.
- **Figure 14.2** (Ch. 14): Temporal primacy overriding blocking in the TD model.
- **Figure 14.3** (Ch. 14): Second-order conditioning with the TD model.
- **Figure 14.4** (Ch. 14): Time course of US prediction over the course of acquisition for the TD model
- **Figure 14.5** (Ch. 14): Model-based and model-free strategies to solve a hypothetical sequential action-selection task.
- **Figure 15.1** (Ch. 15): Spine of a striatal neuron showing input from both cortical and dopamine neurons.
- **Figure 15.2** (Ch. 15): The response of dopamine neurons shifts from initial responses to primary reward
- **Figure 15.3** (Ch. 15): The response of dopamine neurons drops below baseline at the expected time of reward if the reward is omitted.
- **Figure 15.4** (Ch. 15): The behavior of the TD error δ during TD learning is consistent with features of dopamine responses.
- **Figure 15.5** (Ch. 15): Actor–critic ANN and a hypothetical neural implementation.
- **Figure 16.1** (Ch. 16): The TD-Gammon ANN
- **Figure 16.2** (Ch. 16): The backup diagram for Samuel’s checkers player.
- **Figure 16.3** (Ch. 16): High-level view of the reinforcement learning DRAM controller.
- **Figure 16.4** (Ch. 16): Performances of four controllers over a suite of 9 simulated benchmark applications.
- **Figure 16.5** (Ch. 16): Go capturing rule. Left: the three white stones are not surrounded because point
- **Figure 16.6** (Ch. 16): AlphaGo pipeline (policy and value networks, MCTS, self-play). Adapted from Silver et al., Nature 2016.
- **Figure 16.7** (Ch. 16): AlphaGo Zero self-play reinforcement learning.
- **Figure 16.8** (Ch. 16): Click through rate (CTR) versus life-time value (LTV).
- **Figure 16.9** (Ch. 16): Thermal soaring model: snapshot of the vertical velocity field and sample trajectories.
- **Figure 16.10** (Ch. 16): Sample thermal soaring trajectories, with arrows showing wind direction.
- **Figure 17.1** (Ch. 17): A conceptual agent architecture including a model, a planner, and a state-update function.

## Techniques

Concept pages indexed from this book (by chapter theme):

| Part | Topics | Wiki concepts |
|------|--------|---------------|
| Ch. 2 | Bandits, exploration | [[Multi-Armed Bandits]], [[Exploration-Exploitation Tradeoff]], [[Contextual Bandits]] |
| Ch. 3 | MDP formalism | [[Markov Decision Process]] |
| Ch. 4 | Planning with known model | [[Dynamic Programming]], [[Policy Iteration]], [[Value Iteration]] |
| Ch. 5 | Episode-based learning | [[Monte Carlo Methods]], [[Importance Sampling]], [[Off-Policy Learning]] |
| Ch. 6 | TD control | [[Temporal-Difference Learning]], [[Sarsa]], [[Q-learning]], [[Expected Sarsa]], [[On-Policy Learning]] |
| Ch. 7 | Multi-step returns | [[n-Step Methods]] |
| Ch. 8 | Model-based RL | [[Dyna]] |
| Ch. 9–10 | Generalization | [[Function Approximation in RL]] |
| Ch. 11 | Stability | [[Deadly Triad]], [[Off-Policy Learning]] |
| Ch. 12 | Credit assignment | [[Eligibility Traces]], [[n-Step Methods]] |
| Ch. 13 | Policy optimization | [[Policy Gradient]], [[REINFORCE]], [[Actor-Critic Methods]] |
| Ch. 17 | Frontiers | [[Options]] |

## Entities

- [[Richard S. Sutton]] — co-author; pioneered TD learning, policy gradients, and many algorithms in the book.
- [[Andrew G. Barto]] — co-author; foundational work connecting RL to neuroscience and adaptive systems.

## Questions & Gaps

- Function approximation with deep networks is covered but predates modern transformer-scale RL; readers need [[Reinforcement Learning from Human Feedback]] for LLM post-training specifics.
- Continuous control, distributional RL, and model-based RL at scale are only lightly touched in Chapter 17.
- Safe RL, offline RL, and human-in-the-loop alignment are outside the book's scope (see [[Safety and Alignment]] and [[RLHF]]).

## Related

- [[Reinforcement Learning]] — wiki concept page; links to all Sutton & Barto technique pages above.
- [[Reinforcement Learning Topic]] — topic hub for RL papers and ingests in this wiki.
- [[Reinforcement Learning from Human Feedback]] — modern post-training textbook building on classical RL ideas.
- [[Policy Gradient]] · [[Actor-Critic Methods]] · [[REINFORCE]] — Chapter 13 and LLM optimizers (PPO, [[GRPO]]).
- [[Multi-Armed Bandits]] · [[Exploration-Exploitation Tradeoff]] — Chapter 2 foundations.
- [[Monte Carlo Methods]] · [[Temporal-Difference Learning]] · [[Q-learning]] — core learning paradigms.
- [[On SFT RL and On-Policy Distillation]] — contrasts RL with SFT and distillation in the LLM regime.
