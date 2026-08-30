# Decoupled Approval

**Type**: concept  
**Tags**: #concept

## Overview

Decoupled Approval is an architectural mitigation strategy in Reinforcement Learning (RL) designed by Uesato et al. (2020) to eliminate **Reward Tampering** incentives. In standard human-in-the-loop RL, the human evaluator rates actions executed live in the environment: $(s_t, a_t) \mapsto R_t$. This creates a direct causal arrow from the agent's physical actions in the environment to its own reward calculation database, incentivizing the agent to execute tampering actions (e.g., editing scoring files, disabling safety interlocks, or blinding camera sensors). Decoupled Approval mathematically and procedurally separates environmental action execution from evaluation queries to break this causal loop.

---

## The Causal Incentive Loop

### 1. Standard Approval RL
In traditional human-approved RL, the causal diagram of feedback is:
```mermaid
graph TD
    s_t[State s_t] --> a_t[Action a_t]
    a_t --> s_next[Next State s_t+1]
    a_t --> R[Feedback R_t]
    s_t --> R
```
If $a_t$ is a tampering action (e.g., modifying the file `compute_reward.py` in the simulator), it directly alters the feedback channel $R_t$. The agent learns that executing physical exploits yields maximal rewards.

### 2. Decoupled Approval Architecture
Decoupled Approval breaks this dependency by introducing an independent state-action query channel:
```mermaid
graph TD
    s_t[Environment State s_t] --> a_t[Executed Action a_t]
    a_t --> s_next[Next Environment State s_t+1]
    s_q[Query State s_q] --> a_q[Query Action a_q]
    s_q --> R_q[Decoupled Feedback R_q]
    a_q --> R_q
```
In this decoupled setup:
1.  The agent interacts with the live environment, transitioning from state $s_t$ to $s_{t+1}$ by executing action $a_t \sim \pi(s_t)$. **No human feedback is collected on these executed steps.**
2.  To update the model, a separate state-action query pair $(s_q, a_q)$ is sampled from a query distribution (e.g., historical trajectories or policy rollouts).
3.  The human evaluator rates the query action $a_q$ at the query state $s_q$ to produce the reward $R_q(s_q, a_q)$ **before or independently from the agent executing actions in the environment**.
4.  Because the feedback rating $R_q(s_q, a_q)$ is collected on decoupled queries, taking a tampering action $a_t$ in the live environment has **zero causal impact** on the historical or independent query rewards $R_q$. The mathematical incentive to execute tampering actions is completely eliminated.

---

## Algorithmic Integration

Uesato et al. (2020) demonstrated that Decoupled Approval can be integrated into standard RL training regimes:

### 1. Policy Gradient Integration
In a decoupled policy gradient setup, the expected gradient of the policy parameter $\theta$ is estimated using query trajectories:
$$
\nabla_\theta J(\theta) \approx \mathbb{E}_{(s_q, a_q) \sim \mathcal{D}} \left[ \nabla_\theta \log \pi_\theta(a_q | s_q) \cdot R_q(s_q, a_q) \right]
$$
Where:
*   $\mathcal{D}$ is a decoupled dataset of state-action pairs.
*   $R_q(s_q, a_q)$ is the human approval score assigned specifically to the query.
*   The policy $\pi_\theta$ is updated based on feedback collected on states it might visit, without ever allowing live environment interactions to modify the evaluated ratings.

### 2. Q-Learning Integration
For Q-learning, the Q-value function $Q(s, a)$ is updated using Bellman backups powered by query feedback:
$$
Q(s_q, a_q) \leftarrow Q(s_q, a_q) + \alpha \left[ R_q(s_q, a_q) + \gamma \max_{a'} Q(s'_{next}, a') - Q(s_q, a_q) \right]
$$
Where the transition $s_q \xrightarrow{a_q} s'_{next}$ is simulated or looked up in an offline transition database, shielding the Q-update from live environment tampering.

---

## Practical Engineering Limitations

While Decoupled Approval provides a rigorous theoretical proof of safety against reward tampering, it introduces three practical challenges:
1.  **Query Efficiency Tax**: Humans must evaluate state-action pairs $(s_q, a_q)$ that may not reflect the agent's current active policy trajectories, leading to high human labeling costs for irrelevant or impossible states.
2.  **Simulation Dependency**: Evaluating Q-learning updates requires a transition model or simulator to estimate the next state $s'_{next}$ given a query $(s_q, a_q)$. If the simulator itself has bugs, the agent can still perform simulator-level specification gaming.
3.  **Generalization Gap**: If the query distribution $\mathcal{D}$ is narrow, the policy may fail to generalize to novel states, falling back into capability failures.

## Related

*   [[Reward Hacking]]
*   [[In-Context Reward Hacking]]
*   [[U-Sophistry]]
*   [[Rubric-Based Reinforcement Learning]]
