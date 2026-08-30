# CARML

**Type**: concept  
**Tags**: #concept

## Overview

**CARML** (Curricula for Unsupervised Meta-Reinforcement Learning; Jabri et al., 2019) is a state-of-the-art framework that integrates **unsupervised skill discovery** with **Meta-Reinforcement Learning** (Meta-RL) to automatically construct a training curriculum. 

While classic skill discovery methods (such as DIAYN) require access to low-level, low-dimensional true state vectors to train their discriminators, CARML is designed to scale to **pixel-level observations** (images). CARML achieves this by framing unsupervised trajectory interaction and skill modeling as a **Variational Expectation-Maximization (EM)** algorithm, optimizing a lower bound on the mutual information between trajectories and a latent skill space.

---

## Mathematical Formulation: Variational EM

CARML models unsupervised skill discovery as fitting a latent variable mixture model over trajectories. Let:
- $\tau = (s_0, a_0, s_1, a_1, \dots, s_T)$ be a trajectory of states and actions.
- $z \in \mathcal{Z}$ be a latent skill variable (which can be discrete or continuous).
- $q_\phi(z | \tau)$ be a variational posterior (the skill classifier/discriminator).
- $p_\theta(\tau | z)$ be the policy generative model of trajectories given skill $z$.

The system attempts to maximize the marginal log-likelihood of trajectories:

$$\max_{\theta, \phi} \sum_{\tau} \log p(\tau)$$

Using the variational lower bound (ELBO), this marginal likelihood is decomposed into a two-step Expectation-Maximization loop over the parameters of the skill model ($\phi$) and the policy ($\theta$):

$$\log p(\tau) \ge \mathbb{E}_{z \sim q_\phi(z | \tau)} \left[ \log p_\theta(\tau | z) \right] - \text{KL}\left( q_\phi(z | \tau) \mid\mid p(z) \right)$$

---

## The EM Optimization Steps

```
         Trajectory Dataset D
                  |
                  v
       =======================
       E-Step: Skill Classifier
       -----------------------
       Fit posterior q_phi(z|s) to organize
       trajectories into latent skills
       =======================
                  |
                  v
       =======================
       M-Step: Meta-RL Policy
       -----------------------
       Optimize policy rewards using skills
       as the task distribution
       =======================
```

### 1. The E-Step (Unsupervised Skill Organization)
In the E-step, the goal is to organize gathered environment trajectories into distinct behavioral components. The variational posterior $q_\phi(z | \tau)$ is trained to identify which skill $z$ generated trajectory $\tau$:

$$\max_\phi \mathbb{E}_{\tau \sim \mathcal{D}, z \sim q_\phi(z | \tau)} \left[ \sum_{s \in \tau} \log q_\phi(s | z) \right]$$

To scale to high-dimensional pixel inputs, CARML approximates the trajectory-level classifier $q_\phi(z | \tau)$ using a **state-level classifier** $q_\phi(z | s)$ that operates on single frames or short sequences.

### 2. The M-Step (Meta-RL Policy Training)
In the M-step, the policy parameters $\theta$ are trained to execute the learned skills. The discovered skill distribution is treated as the task distribution for a Meta-RL algorithm (e.g., MAML or RL$^2$). 

During the M-step, the policy is rewarded for both **exploring the task space** and **conforming to the designated skill**. The reward function for skill $z$ at state $s$ is formulated as:

$$r_z(s) = (\lambda - 1) \log q_\phi(s | z) + \log q_\phi(z | s) + C$$

Where:
- **Red Term $(\lambda - 1) \log q_\phi(s | z)$**: Encourages task-specific exploration. Since $q_\phi(s | z)$ is the probability of visiting state $s$ given skill $z$, visiting rare states (where $q_\phi(s | z)$ is low) yields a higher reward because $(\lambda - 1)$ is negative for $\lambda \in [0, 1]$.
- **Blue Term $\log q_\phi(z | s)$**: Encourages latent skill matching. Rewards the policy for visiting states that clearly distinguish skill $z$ from other skills (high predictability).
- $\lambda \in [0, 1]$ is a hyperparameter balancing exploration vs. predictability.

---

## Mutual Information Optimization

CARML's objectives are mathematically tied to maximizing the **Mutual Information** $I(\tau; z)$ between trajectories and latent skills:

$$I(\tau; z) = H(z) - H(z | \tau) \ge \mathbb{E}_{s \in \tau} \left[ H(z) - H(z | s) \right]$$

Maximizing this lower bound forces:
1. **Diverse Trajectories ($H(z)$ is maximized)**: Ensures that the agent discovers a wide range of different behaviors, preventing mode collapse.
2. **Predictable Skills ($H(z | s)$ is minimized)**: Guarantees that given a state $s$ within a trajectory, the skill $z$ is highly identifiable, meaning each skill represents a clean, distinct option.

---

## Comparison: Skill Discovery Methods

| Metric / Aspect | CARML (Jabri et al.) | DIAYN (Eysenbach et al.) | VIC (Gregor et al.) |
|---|---|---|---|
| **Primary Goal** | Automated Meta-RL Task Curriculum | Option Discovery | Option Discovery |
| **Observation Type** | **High-dimensional pixels** | Low-dimensional states | Low-dimensional states |
| **Math Framework** | Variational EM Loop | Direct Mutual Information | Variational Information Bottleneck |
| **Meta-RL Ready?** | **Yes** (directly feeds task vectors) | No (requires manual meta-wrap) | No |
| **Exploration Term** | Explicitly balanced via $\lambda$ parameter | Pure predictability maximization | Pure predictability maximization |

---

## Notes

- CARML's EM formulation mirrors classical Expectation-Maximization for GMMs, but here the hidden variables are active policy options rather than static parameters.
- By using variational inference, $q_\phi$ can be parameterized as a discrete classifier (yielding a finite curriculum of $K$ skills) or as a continuous VAE (yielding an infinite, continuous curriculum).
- Unsupervised skill discovery is mathematically a form of **intrinsic motivation** (curiosity), establishing a strong connection to [[Exploration Strategies in Deep Reinforcement Learning]].

## Appearances

- [[Curriculum for Reinforcement Learning]] — Covered under the Skill-Based Curriculum section.

## Related

- [[Curriculum Learning]] — Foundational parent concept.
- [[Curriculum for Reinforcement Learning]] — Parent survey.
- [[Exploration Strategies in Deep Reinforcement Learning]] — Companion survey page.
- [[Variational Autoencoders]] — Underlying variational framework.
- [[Expectation Maximization]] — Optimization lineage.
- [[Meta-Learning]] — Paradigm that CARML utilizes for policy transfer.
- [[Reinforcement Learning Topic]] — Parent topic.
