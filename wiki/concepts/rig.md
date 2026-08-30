# Reinforcement Learning with Imagined Goals

**Type**: concept  
**Tags**: #concept

## Overview

Reinforcement Learning with Imagined Goals (RIG) is a self-supervised, end-to-end framework developed by Nair et al. (2018) that enables robotic systems to learn goal-conditioned control policies directly from raw visual inputs (pixels) without manual reward engineering or physical coordinates. RIG addresses a core challenge of visual RL: the extreme sample inefficiency of training deep networks on raw pixels. By training a Variational Autoencoder ($\beta$-VAE) on unstructured, unlabeled image sequences, RIG structures a compact, continuous latent representation space. The robot samples "imagined goals" directly from the VAE's prior, computes dense control rewards as Euclidean distances in the latent space, and applies Hindsight Experience Replay (HER) to accelerate policy optimization.

```
                             RIG Policy Training Execution Loop
                             
       +-------------------------------------------------------------+
       |                  Variational Autoencoder                    |
       |  s (State Image) ===> [e(s) = \mu_\phi(s)] ===> z (Latent)  |
       +-------------------------------------------------------------+
               ||                                           ^
         (State Embedding)                                  | (Imagined Goal
               ||                                           |  z_g ~ N(0,I))
               \/                                           |
     +-------------------+     Actions a_t     +--------------------------+
     |   State s_t       | <================== |  Goal-Conditioned Policy |
     |   (Environment)   | ==================> |      \pi(a | e(s), z_g)  |
     +-------------------+     Next State s'   +--------------------------+
               ||                                           ||
               \/                                           \/
     +--------------------------------------------------------------------+
     |                     Hindsight Experience Replay                    |
     |  Compute Reward: R_t = - ||e(s_t) - z_g||_2                       |
     |  HER Relabeling: Replace z_g with e(s_future) with probability p   |
     +--------------------------------------------------------------------+
```

---

## The RIG Algorithmic Pipeline

RIG runs in three distinct phases: Latent Space Learning, Goal Imagination, and Policy Training.

### Phase 1: Latent Space Representation Learning
Before policy training begins, the robot collects a small dataset of unstructured interaction images $\mathcal{D} = \{s_i\}$ by executing random actions in the environment (e.g. random arm sweeping). A $\beta$-VAE is trained on $\mathcal{D}$ to map images $s$ to latent variables $z \sim q_\phi(z \mid s)$ while ensuring a smooth, disentangled latent distribution.

The encoder $q_\phi(z \mid s) = \mathcal{N}(\mu_\phi(s), \sigma_\phi^2(s))$ and decoder $p_\theta(s \mid z)$ are optimized using the standard Evidence Lower Bound (ELBO) loss:
$$ \mathcal{L}_{\text{ELBO}}(\theta, \phi; s) = \mathbb{E}_{z \sim q_\phi(z \mid s)} \left[ \log p_\theta(s \mid z) \right] - \beta D_{\text{KL}}\left(q_\phi(z \mid s) \parallel p(z)\right) $$
where $p(z) = \mathcal{N}(\mathbf{0}, \mathbf{I})$ is the standard Gaussian prior, and $\beta > 1$ is a scaling factor that encourages disentanglement of latent features.

For state mapping, RIG discards the decoder and utilizes the encoder's mean output as the state embedding function:
$$ e(s) = \mu_\phi(s) $$

### Phase 2: Goal Imagination
To train a goal-conditioned policy $\pi(a \mid s, g)$, the agent requires a diverse set of target goals. In the physical world, manually arranging objects to define goal states is incredibly slow and labor-intensive. 
RIG solves this by **imagining goals** in the latent space. Because the $\beta$-VAE regularizes the latent space toward a standard Gaussian distribution, the agent can sample highly realistic and diverse goal configurations directly from the prior:
$$ z_g \sim \mathcal{N}(\mathbf{0}, \mathbf{I}) $$

These sampled latent vectors $z_g$ represent the coordinates of "imagined" workspace configurations (e.g. block arrangements) that the robot will attempt to achieve.

### Phase 3: Goal-Conditioned Policy Training & HER
The policy $\pi(a \mid e(s), z_g)$ and action-value function $Q(e(s), a, z_g)$ are trained entirely in the latent space:
1. **Initialize**: Sample an imagined goal representation $z_g \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$.
2. **Execute**: For each step $t$ in the episode, input the current visual state representation $e(s_t)$ and goal $z_g$ to the policy to select action $a_t = \pi(a \mid e(s_t), z_g)$.
3. **Reward**: Compute a dense reward as the negative Euclidean distance in the latent space:
   $$ R_t = - \| e(s_t) - z_g \|_2 $$
4. **Hindsight Experience Replay (HER)**: Trajectories are stored in a replay buffer. During off-policy training, transitions are sampled. With a probability $p$ (typically $p=0.8$), the original goal $z_g$ is retroactively **relabeled** with the representation of a state visited *later in the same episode*:
   $$ z_{g'} = e(s_{t'}) \quad \text{where } t' > t $$
   The reward is then recomputed as:
   $$ R_t' = - \| e(s_t) - e(s_{t'}) \|_2 $$

HER significantly accelerates training by teaching the agent how to achieve the states it actually visited, even if it failed to achieve the originally imagined goal $z_g$.

---

## Context-Conditioned RIG (CC-RIG)

Standard VAEs can generate blurry or physically unrealistic goals when trained on complex multi-object scenes, causing the policy to receive noisy reward signals. To solve this, Nair et al. (2020) introduced **CC-RIG**, which utilizes a Context-Conditioned VAE (CC-VAE).

In CC-RIG, the encoder and decoder are conditioned on a context image $c$ (typically the starting frame of the episode):
- Encoder: $q_\phi(z \mid s, c)$
- Decoder: $p_\theta(s \mid z, c)$

The ELBO loss becomes:
$$ \mathcal{L}_{\text{CC-ELBO}} = \mathbb{E}_{q_\phi(z \mid s, c)} \left[ \log p_\theta(s \mid z, c) \right] - \beta D_{\text{KL}}\left(q_\phi(z \mid s, c) \parallel p(z \mid c)\right) $$

By conditioning on the initial workspace configuration $c$, the CC-VAE can generate highly sharp, realistic imagined goals that display much higher variance in object colors, block shapes, and positions, while keeping static elements (like table boundaries or gripper bases) perfectly aligned.

---

## Appearances

- [[Self-Supervised Representation Learning]] — Detailed as a self-supervised reinforcement learning architecture operating over $\beta$-VAE latent states, along with extensions like Context-Conditioned RIG (CC-RIG).

## Related

- [[Representation Learning]]
- [[Self-Supervised Representation Learning]]
- [[Variational Autoencoders]]
