# Unravel Policy Gradients and REINFORCE

Sergios Karagiannakos on 2018-11-1 · 4 mins

**Source URL**: https://theaisummer.com/Policy-Gradients/

This time, we are going to keep ourselves busy with another family of Reinforcement learning algorithms, called policy-based methods. If you recall, there are two main groups of techniques when it comes to model-free Reinforcement Learning.

- Value-Based
- Policy-Based

We analyze the first ones in two previous articles where we talked about Q-learning and Deep Q Networks and different improvement on the basic models such as Double Deep Q Networks and Prioritized Replay.

Let's do a quick rewind. Remember that we frame our problems as Markov Decision Processes and that our goal is to find the best Policy, which is a mapping from states to actions. In value-based methods, we achieve that by finding or approximating the Value function and then extract the Policy. What if we completely ditch the value part and find directly the Policy. This is what Policy-based methods do.

Policy-based methods offer some different advantages:

- They converge more easily to a local or global maximum and they don't suffer from oscillation
- They are highly effective in high-dimensional or **continuous** spaces
- They can learn **stochastic** policies (probability distribution over actions; useful in stochastic/POMDP environments)

Policy based reinforcement learning is an **optimization problem**. We have a policy π with parameters θ that outputs a probability distribution over actions. We evaluate policies with objective J(θ), most often expected accumulative reward.

π_θ(a|s) = P[a|s]

J(θ) = E_πθ[∑ γr]

**Policy Search** families:
- Gradient-free: hill climbing, simplex, simulated annealing, evolutionary algorithms
- Gradient-based: gradient ascent on J(θ)

Vanilla policy gradient loop:
1. Initialize θ
2. Generate episode
3. Get long-term reward
4. Update θ based on reward for all time steps
5. Repeat

With differentiable policy and log trick on trajectory τ:

θ ← θ + α ∇_θ J(θ)

∇_θ J(θ) = E_π[∇_θ(log π(τ|θ)) R(τ)]

**REINFORCE** (Monte Carlo policy gradient): replaces expectation with stochastic gradient descent — sample episode return and update parameters each step.

Essence: positive-reward episodes increase action probabilities; negative-reward episodes decrease them.

REINFORCE + neural networks: policy network (e.g. softmax over actions) approximates π_θ. Famous example: Karpathy Pong agent. Article includes Keras REINFORCE on CartPole-v1 with discounted returns, mean/std normalization, and categorical cross-entropy training.

Drawbacks: **high variance**, difficult to stabilize parameters. Hint: actor-critic methods address this.
