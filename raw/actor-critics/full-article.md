# The idea behind Actor-Critics and how A2C and A3C improve them

Sergios Karagiannakos on 2018-11-17 · 6 mins

**Source URL**: https://theaisummer.com/Actor_critics/

Actor-Critic algorithms are the base behind almost every modern RL method from Proximal Policy Optimization to A3C.

**Value-based** (Q-learning, DQN variants): find optimal value function, extract policy. Sample-efficient and steady.

**Policy-based** (Policy Gradients, REINFORCE): find optimal policy directly. Better for continuous/stochastic environments, faster convergence.

**Actor-Critic** merges both: actor outputs action from state (policy-based); critic evaluates action via Q-value (value-based). Two networks trained separately with gradient ascent. Updates at each step (TD), not end of episode like REINFORCE.

**A2C (Advantage Actor-Critic)**: Q(s,a) = V(s) + A(s,a); critic learns advantage A(s,a) = Q(s,a) − V(s) ≈ r + γV(s') − V(s). Reduces policy-gradient variance.

**A3C (Asynchronous Advantage Actor-Critic)**: DeepMind 2016. Multiple independent agents with own weights explore parallel environment copies. Agents update global shared network asynchronously; periodically reset weights from global network.

**Synchronous A2C variant**: wait for all agents to finish segment, then update global network and reset all agents. Practical implementation: multiple environment copies, step model collects n-step batches, train model updates, step model syncs weights.

Modern extensions: DDPG, PPO, TRPO.
