# Denoising Diffusion Implicit Models

**Type**: concept  
**Tags**: #concept

## Overview

Denoising Diffusion Implicit Models (DDIM) are an accelerated deterministic sampling formulation that maps the forward process of a diffusion model to a non-Markovian family of distributions, enabling identical marginals with significantly fewer discretization steps.

## Appearances

- [[What are Diffusion Models?]] — Under the accelerated sampling and progressive distillation section.

## Detailed Formulations

DDIM generalizes the Markovian forward process of [[Denoising Diffusion Probabilistic Models]] (DDPM) to a class of non-Markovian forward processes parameterized by a standard deviation parameter $\sigma_t$. While the marginals $q(x_t \mid x_0)$ remain identical to DDPM, the transition probabilities $q(x_{t-1} \mid x_t, x_0)$ are modified to allow for customizable noise levels during sampling:

$$q(x_{t-1} \mid x_t, x_0) = \mathcal{N} \left( x_{t-1}; \sqrt{\bar{\alpha}_{t-1}}x_0 + \sqrt{1 - \bar{\alpha}_{t-1} - \sigma_t^2} \frac{x_t - \sqrt{\bar{\alpha}_t}x_0}{\sqrt{1 - \bar{\alpha}_t}}, \sigma_t^2 \mathbf{I} \right)$$

When setting $\sigma_t = 0$ for all timesteps, the forward process becomes entirely deterministic, mapping each initial sample $x_0$ to a unique latent representation $x_T$. During inference, the generative step is defined as:

$$x_{t-1} = \sqrt{\bar{\alpha}_{t-1}} \hat{x}_0(x_t) + \sqrt{1 - \bar{\alpha}_{t-1} - \sigma_t^2} \epsilon_\theta(x_t, t) + \sigma_t \epsilon_t$$

where $\hat{x}_0(x_t) = \frac{x_t - \sqrt{1 - \bar{\alpha}_t}\epsilon_\theta(x_t, t)}{\sqrt{\bar{\alpha}_t}}$ represents the predicted clean image at step $t$, and $\epsilon_t \sim \mathcal{N}(0, \mathbf{I})$.

---

## Subsequence Sampling and Acceleration

Rather than sampling over all $T$ timesteps, we can define a subsequence $\tau = [\tau_1, \tau_2, \dots, \tau_S]$ of length $S \ll T$ (where $\tau_S = T$). The generative step over the subsequence is formulated as:

$$x_{\tau_{i-1}} = \sqrt{\bar{\alpha}_{\tau_{i-1}}} \left( \frac{x_{\tau_i} - \sqrt{1 - \bar{\alpha}_{\tau_i}} \epsilon_\theta(x_{\tau_i}, \tau_i)}{\sqrt{\bar{\alpha}_{\tau_i}}} \right) + \sqrt{1 - \bar{\alpha}_{\tau_{i-1}} - \sigma_{\tau_i}^2} \epsilon_\theta(x_{\tau_i}, \tau_i) + \sigma_{\tau_i} \epsilon$$

Here, the coefficient $\sigma_{\tau_i}$ controls the degree of stochasticity:

$$\sigma_{\tau_i} = \eta \sqrt{\frac{1 - \bar{\alpha}_{\tau_{i-1}}}{1 - \bar{\alpha}_{\tau_i}}} \sqrt{1 - \frac{\bar{\alpha}_{\tau_i}}{\bar{\alpha}_{\tau_{i-1}}}}$$

* **$\eta = 1$**: The transition stochasticity matches DDPM exactly.
* **$\eta = 0$**: The transition becomes entirely deterministic (standard DDIM), yielding a smooth, reproducible trajectory from a noise sample.

---

## Continuous Limit: The Probability Flow ODE

By taking the step size to the continuous limit ($dt \to 0$), the deterministic DDIM process ($\eta = 0$) converges to the **Probability Flow ODE** (Song et al., 2020). Let $x(t)$ be the continuous variable. The ODE sharing the exact same marginal probability densities $p_t(x_t)$ as the corresponding stochastic DDPM SDE is given by:

$$dx_t = \left[ f(t)x_t - \frac{1}{2} g(t)^2 \nabla_{x_t} \log p_t(x_t) \right] dt$$

Using the relation between the score function and the predicted noise, $\nabla_{x_t} \log p_t(x_t) = -\frac{\epsilon_\theta(x_t, t)}{\sqrt{1 - \bar{\alpha}_t}}$, the ODE can be rewritten as:

$$\frac{dx_t}{dt} = \frac{d \sqrt{\bar{\alpha}_t}}{dt} \frac{x_t - \sqrt{1 - \bar{\alpha}_t}\epsilon_\theta(x_t, t)}{\sqrt{\bar{\alpha}_t}} + \frac{d \sqrt{1 - \bar{\alpha}_t}}{dt} \epsilon_\theta(x_t, t)$$

This ODE connection establishes a direct bridge between diffusion models and continuous-time normalizing flows, enabling advanced ODE solvers (such as Runge-Kutta or adaptive step-size solvers) to generate samples with extremely high efficiency.

---

## Deterministic Image Inversion

Because the $\eta = 0$ trajectory is completely deterministic, we can invert a real-world image $x_0$ into a latent representation $x_T$ that reconstructs the original image perfectly under reverse sampling. Assuming small step sizes, the forward ODE is solved in the positive time direction:

$$x_{t+\Delta t} = \sqrt{\bar{\alpha}_{t+\Delta t}} \left( \frac{x_t - \sqrt{1 - \bar{\alpha}_t} \epsilon_\theta(x_t, t)}{\sqrt{\bar{\alpha}_t}} \right) + \sqrt{1 - \bar{\alpha}_{t+\Delta t}} \epsilon_\theta(x_t, t)$$

This deterministic inversion is the cornerstone of semantic image editing (e.g., in Prompt-to-Prompt or Null-text Inversion), allowing users to invert an image to its latent representation, alter a prompt or conditioning factor, and denoise it along a highly consistent trajectory.

---

## Velocity ($\mathbf{v}$) Parameterization in DDIM

Under $\mathbf{v}$-parameterization, the model targets the combined velocity vector $\mathbf{v}_t = \alpha_t \boldsymbol{\epsilon} - \sigma_t \mathbf{x}$. By parameterizing the diffusion schedule using the angular coordinate $\phi_t = \arctan(\sigma_t/\alpha_t)$, the deterministic DDIM step simplifies to a pure trigonometric rotation:

$$\mathbf{z}_{\phi_s} = \cos(\phi_t - \phi_s)\mathbf{z}_{\phi_t} + \sin(\phi_s - \phi_t)\hat{\mathbf{v}}_\theta$$

This trigonometric formulation ensures robust numerical stability across long DDIM sampling schedules. It prevents high-noise color drift and contrast decay in high-resolution and video generations by maintaining balanced gradients for both signals and noise early in the reverse path. (See [[v-parameterization]] for the complete derivation).

---

## Zero-Shot Motion Warping in DDIM (Text2Video-Zero)

Text2Video-Zero leverages the deterministic property of the DDIM Probability Flow ODE to inject camera dynamics into zero-shot video generation without any network training. By applying localized spatial warping in the latent space during the early stages of denoising, DDIM trajectories are forced to align.

Given a motion displacement vector $\boldsymbol{\delta} = (\delta_x, \delta_y)$, motion scale $\lambda > 0$, and step interval $\Delta t$:

1. **Deterministic Inversion**: The latent for the first frame is sampled at random, $\mathbf{x}^1_T \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$, and inverted back by $\Delta t$ steps using the DDIM backward ODE trajectory:
   $$\mathbf{x}^1_{T'} = \text{DDIM-backward}(\mathbf{x}^1_T, \Delta t) \quad \text{where} \quad T' = T - \Delta t$$
2. **Latent Warping**: For each subsequent frame $k \in \{2, \dots, m\}$, a spatial warp operator $W_k$ representing camera translation $\boldsymbol{\delta}^k = \lambda(k-1)\boldsymbol{\delta}$ is applied to the inverted latent:
   $$\tilde{\mathbf{x}}^k_{T'} = W_k(\mathbf{x}^1_{T'})$$
3. **Forward Generation**: The warped latents are propagated back to the high-noise state $T$ via DDIM forward steps:
   $$\mathbf{x}^k_T = \text{DDIM-forward}(\tilde{\mathbf{x}}^k_{T'}, \Delta t) \quad \text{for} \quad k = 2, \dots, m$$

Denoising then proceeds from the motion-aligned noisy latents $\{\mathbf{x}^1_T, \dots, \mathbf{x}^m_T\}$ using [[cross-frame-attention]] to maintain foreground identity.

---

## Comparative Analysis: DDPM vs. DDIM

| Property | [[Denoising Diffusion Probabilistic Models]] (DDPM) | Denoising Diffusion Implicit Models (DDIM) |
| :--- | :--- | :--- |
| **Underlying Mathematics** | Stochastic Differential Equation (SDE) | Ordinary Differential Equation (ODE) (when $\eta=0$) |
| **Markovian Assumption** | Yes (strictly relies on Markov chain) | No (derived from non-Markovian family) |
| **Deterministic Mapping** | No (stochastic injection at every step) | Yes (completely deterministic when $\sigma_t=0$) |
| **Typical Inference Steps** | $1000$ steps | $20 - 100$ steps |
| **Inversion Capability** | Highly difficult (requires optimization/SDE-inversion) | Trivial and exact (simply reverse the ODE steps) |
| **Training Protocol** | Same (DDIM is applied post-hoc to pretrained DDPMs) | Same (uses identical $\epsilon_\theta$ training target) |

---

## Worked Example: A Deterministic DDIM Step

Let's compute a deterministic DDIM step ($\sigma_t = 0$) over a subsequence interval from step $\tau_i$ to $\tau_{i-1}$.
* Let the current latents be $x_{\tau_i} = 1.5$.
* Let the schedule values be $\bar{\alpha}_{\tau_i} = 0.6$ and $\bar{\alpha}_{\tau_{i-1}} = 0.8$.
* The neural network predicts the noise vector at this step: $\epsilon_\theta(x_{\tau_i}, \tau_i) = 0.4$.

1. **Predict the clean sample $\hat{x}_0$**:
   $$\hat{x}_0(x_{\tau_i}) = \frac{x_{\tau_i} - \sqrt{1 - \bar{\alpha}_{\tau_i}} \epsilon_\theta(x_{\tau_i}, \tau_i)}{\sqrt{\bar{\alpha}_{\tau_i}}}$$
   $$\hat{x}_0 = \frac{1.5 - \sqrt{1 - 0.6}(0.4)}{\sqrt{0.6}} = \frac{1.5 - \sqrt{0.4}(0.4)}{\sqrt{0.6}}$$
   $$\hat{x}_0 \approx \frac{1.5 - 0.6325 \cdot 0.4}{0.7746} = \frac{1.5 - 0.2530}{0.7746} \approx \frac{1.2470}{0.7746} \approx 1.6099$$

2. **Denoise to the previous subsequence step $x_{\tau_{i-1}}$**:
   Since $\sigma_{\tau_i} = 0$, the step equation is:
   $$x_{\tau_{i-1}} = \sqrt{\bar{\alpha}_{\tau_{i-1}}} \hat{x}_0 + \sqrt{1 - \bar{\alpha}_{\tau_{i-1}}} \epsilon_\theta(x_{\tau_i}, \tau_i)$$
   $$x_{\tau_{i-1}} = \sqrt{0.8} (1.6099) + \sqrt{1 - 0.8} (0.4)$$
   $$x_{\tau_{i-1}} \approx 0.8944 (1.6099) + 0.4472 (0.4)$$
   $$x_{\tau_{i-1}} \approx 1.4399 + 0.1789 = 1.6188$$

Thus, the latent representation is deterministically updated from $1.5$ to $1.6188$ closer to the true data manifold.

## Related

- [[Denoising Diffusion Probabilistic Models]]
- [[Consistency Models]]
- [[What are Diffusion Models?]]
- [[v-parameterization]]
- [[cross-frame-attention]]

#concept
#topic
