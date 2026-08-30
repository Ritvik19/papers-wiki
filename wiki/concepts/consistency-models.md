# Consistency Models

**Type**: concept  
**Tags**: #concept

## Overview

Consistency Models are a family of generative models designed to map any point along a continuous-time diffusion trajectory directly to the origin $x_0$. By enforcing this trajectory consistency, they enable high-fidelity, single-step or few-step image synthesis.

## Appearances

- [[What are Diffusion Models?]] — Section on continuous-time diffusion trajectories and accelerated sampling.

## Detailed Formulations

Given a probability flow ODE that transforms a noise distribution to a data distribution, let $\{x_t\}_{t \in [0, T]}$ be a continuous trajectory. A **Consistency Model** defines a parametric function $f_\theta(x_t, t)$ that satisfies the self-consistency property:

$$f_\theta(x_t, t) = f_\theta(x_{t'}, t') = x_0 \quad \text{for all} \quad t, t' \in [0, T]$$

---

## Boundary Condition and Parameterization

By definition, the consistency function at $t=\epsilon$ (where $\epsilon$ represents a small positive noise threshold, typically $\epsilon = 0.002$) must return the identity: $f_\theta(x_\epsilon, \epsilon) = x_\epsilon$. To strictly enforce this boundary condition without imposing optimization constraints during training, the consistency model is parameterized using differentiable skip connections:

$$f_\theta(x_t, t) = c_{\text{skip}}(t) x_t + c_{\text{out}}(t) F_\theta(x_t, t)$$

where $F_\theta(x_t, t)$ is a deep neural network, and the scalar coefficients $c_{\text{skip}}(t)$ and $c_{\text{out}}(t)$ are defined as:

$$c_{\text{skip}}(t) = \frac{\sigma_{\text{data}}^2}{(t - \epsilon)^2 + \sigma_{\text{data}}^2}$$

$$c_{\text{out}}(t) = \frac{\sigma_{\text{data}} (t - \epsilon)}{\sqrt{(t - \epsilon)^2 + \sigma_{\text{data}}^2}}$$

Here, $\sigma_{\text{data}}$ represents the standard deviation of the training dataset (typically $\sigma_{\text{data}} = 0.5$). 
* **At the boundary ($t = \epsilon$)**: $c_{\text{skip}}(\epsilon) = 1$ and $c_{\text{out}}(\epsilon) = 0$, forcing $f_\theta(x_\epsilon, \epsilon) = x_\epsilon$.
* **At high noise ($t \gg \epsilon$)**: $c_{\text{skip}}(t) \to 0$ and $c_{\text{out}}(t)$ scales the network's predictions, allowing $F_\theta$ to drive the denoising process.

---

## Multi-Step Consistency Sampling

While a Consistency Model can synthesize an image in a single forward pass ($x_\epsilon = f_\theta(x_T, T)$), sampling quality can be iteratively refined by alternating between deterministic denoising steps and stochastic noise injection.

### Algorithm: Multi-Step Consistency Sampling

```python
def multi_step_consistency_sampling(f_theta, steps, epsilon=0.002):
    # steps: a list of decreasing timesteps [tau_1, tau_2, ..., tau_N] where tau_1 = T, tau_N = epsilon
    # f_theta: the trained consistency model
    
    # 1. Initialize from random Gaussian noise
    x = sample_gaussian(0, I)
    
    for i in range(len(steps) - 1):
        t_curr = steps[i]
        t_next = steps[i+1]
        
        # 2. Map current latent onto the estimated origin (denoise)
        x_0 = f_theta(x, t_curr)
        
        # 3. Inject noise to lift the state to the next intermediate noise level
        z = sample_gaussian(0, I)
        x = x_0 + sqrt(t_next**2 - epsilon**2) * z
        
    # 4. Final step: map directly to the data manifold
    x_final = f_theta(x, steps[-1])
    return x_final
```

---

## Comparative Analysis: CMs vs. GANs vs. Progressive Distillation

| Dimension | Generative Adversarial Networks (GANs) | Progressive Distillation (PD) | Consistency Models (CM) |
| :--- | :--- | :--- | :--- |
| **Inference Speed** | **Fastest** (exactly 1 generator step). | Fast (typically 4 to 8 steps). | **Fastest / Flexible** (1 step to any arbitrary $N$ steps). |
| **Training Stability** | Low (adversarial minimax loss causes instabilities). | High (MSE-based distillation training). | **High** (stable MSE-based consistency loss). |
| **Sampling Step Adaptability** | None (generator is fixed to a single pass). | Rigid (requires separate model for each step count). | **Dynamic** (same model handles 1 to 100 steps dynamically). |
| **Mode Collapse Risk** | High (frequently drops modes to fool discriminator). | Low (inherits mode coverage of teacher model). | **Low** (retains full mode coverage of diffusion path). |
| **Distillation Pipeline** | N/A (trained from scratch). | Slow (requires $K$ separate student model training phases). | **Fast** (distills the entire trajectory in a **single stage**). |

---

## Worked Example: Skip Connection Coefficient Scaling

Let's compute the skip connection weights $c_{\text{skip}}(t)$ and $c_{\text{out}}(t)$ at two different timesteps along the trajectory.
* Assume $\epsilon = 0.002$ and $\sigma_{\text{data}} = 0.5$ ($\sigma_{\text{data}}^2 = 0.25$).

### Case A: Early Noise Stage ($t = 1.0$)
1. **Compute differences**:
   $$t - \epsilon = 1.0 - 0.002 = 0.998$$
   $$(t - \epsilon)^2 = 0.998^2 = 0.996004$$
2. **Calculate $c_{\text{skip}}(1.0)$**:
   $$c_{\text{skip}}(1.0) = \frac{0.25}{0.996004 + 0.25} = \frac{0.25}{1.246004} \approx 0.2006$$
3. **Calculate $c_{\text{out}}(1.0)$**:
   $$c_{\text{out}}(1.0) = \frac{0.5 \cdot 0.998}{\sqrt{1.246004}} = \frac{0.499}{1.116245} \approx 0.4470$$

*At $t=1.0$, the input $x_t$ is highly noisy, so $c_{\text{skip}}$ is small ($0.20$), letting the neural network $F_\theta$ (scaled by $0.45$) dominate.*

---

### Case B: Near-Boundary Stage ($t = 0.01$)
1. **Compute differences**:
   $$t - \epsilon = 0.01 - 0.002 = 0.008$$
   $$(t - \epsilon)^2 = 0.008^2 = 0.000064$$
2. **Calculate $c_{\text{skip}}(0.01)$**:
   $$c_{\text{skip}}(0.01) = \frac{0.25}{0.000064 + 0.25} = \frac{0.25}{0.250064} \approx 0.9997$$
3. **Calculate $c_{\text{out}}(0.01)$**:
   $$c_{\text{out}}(0.01) = \frac{0.5 \cdot 0.008}{\sqrt{0.250064}} = \frac{0.004}{0.500064} \approx 0.0080$$

*Near the boundary at $t=0.01$, the weight of the raw input $c_{\text{skip}}$ is almost $1.0$, and the neural network scale $c_{\text{out}}$ is nearly $0.0$, forcing identity behavior to guarantee boundary stability.*

## Related

- [[Denoising Diffusion Probabilistic Models]]
- [[Denoising Diffusion Implicit Models]]
- [[What are Diffusion Models?]]

#concept
#topic
