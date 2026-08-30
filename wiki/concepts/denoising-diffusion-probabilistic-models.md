# Denoising Diffusion Probabilistic Models

**Type**: concept  
**Tags**: #concept

## Overview

Denoising Diffusion Probabilistic Models (DDPM) are a class of latent variable generative models that construct a data distribution by learning to reverse a forward Markov chain that systematically adds Gaussian noise to a sample.

## Appearances

- [[What are Diffusion Models?]] — The fundamental mathematical framework of diffusion generative models.
- [[How Diffusion Models Work: The Math from Scratch]] — AI Summer step-by-step DDPM derivation: reparameterization, ELBO, \(L_{\text{simple}}\), U-Net architecture, training/sampling algorithms.
- [[Papers Explained - GLIDE]] — A conditional image generation framework built on guided diffusion models.

## Detailed Formulations

DDPM defines a forward process $q(x_1, \dots, x_T \mid x_0)$ that corrupts data $x_0 \sim q(x)$ over $T$ steps using a schedule of variance bounds $\beta_t \in (0, 1)$:

$$q(x_t \mid x_{t-1}) = \mathcal{N}(x_t; \sqrt{1 - \beta_t}x_{t-1}, \beta_t \mathbf{I})$$

Through the reparameterization trick with $\alpha_t = 1 - \beta_t$ and $\bar{\alpha}_t = \prod_{i=1}^t \alpha_i$, we can directly sample any arbitrary step $t$ in closed form:

$$x_t = \sqrt{\bar{\alpha}_t}x_0 + \sqrt{1 - \bar{\alpha}_t}\epsilon \quad \text{where} \quad \epsilon \sim \mathcal{N}(0, \mathbf{I})$$

### Derivation of the Reverse Step Posterior

The reverse process $p_\theta(x_{t-1} \mid x_t)$ is parameterized by a neural network that predicts the mean $\mu_\theta(x_t, t)$ and variance $\Sigma_\theta(x_t, t)$ of the Gaussian denoising step:

$$p_\theta(x_{t-1} \mid x_t) = \mathcal{N}(x_{t-1}; \mu_\theta(x_t, t), \Sigma_\theta(x_t, t))$$

When conditioned on the original uncorrupted image $x_0$, the posterior of the transition step $q(x_{t-1} \mid x_t, x_0)$ is analytically tractable via Bayes' rule:

$$q(x_{t-1} \mid x_t, x_0) = q(x_t \mid x_{t-1}, x_0) \frac{q(x_{t-1} \mid x_0)}{q(x_t \mid x_0)}$$

Substituting the Gaussian definitions for each of these terms and solving for the exponent terms:

$$\tilde{\mu}_t(x_t, x_0) = \frac{\sqrt{\alpha_t}(1 - \bar{\alpha}_{t-1})}{1 - \bar{\alpha}_t} x_t + \frac{\sqrt{\bar{\alpha}_{t-1}}\beta_t}{1 - \bar{\alpha}_t} x_0$$

$$\tilde{\beta}_t = \frac{1 - \bar{\alpha}_{t-1}}{1 - \bar{\alpha}_t} \beta_t$$

Since we can express $x_0$ in terms of $x_t$ and the noise vector $\epsilon_t$ as $x_0 = \frac{1}{\sqrt{\bar{\alpha}_t}}(x_t - \sqrt{1 - \bar{\alpha}_t}\epsilon_t)$, we can rewrite the posterior mean solely as a function of the input $x_t$ and the noise injected at step $t$:

$$\tilde{\mu}_t(x_t, x_0) = \frac{1}{\sqrt{\alpha_t}} \left( x_t - \frac{\beta_t}{\sqrt{1 - \bar{\alpha}_t}} \epsilon_t \right)$$

This derivation motivates parameterizing the network to predict the noise vector $\epsilon_\theta(x_t, t)$ instead of directly predicting the mean $\mu_\theta$.

---

## Training and Sampling Algorithms

### Algorithm 1: Training a DDPM

```python
# Training Loop
repeat:
    x_0 = sample_data_distribution()
    t = sample_uniform(1, T)
    epsilon = sample_gaussian(0, I)
    
    # Take a gradient descent step on:
    loss = MSE(epsilon - epsilon_theta(sqrt(alpha_bar_t) * x_0 + sqrt(1 - alpha_bar_t) * epsilon, t))
    optimize(loss)
until converged
```

### Algorithm 2: Reverse Process Sampling

```python
# Sampling Loop
x_T = sample_gaussian(0, I)
for t = T down to 1:
    z = sample_gaussian(0, I) if t > 1 else 0
    
    # Predict noise
    pred_noise = epsilon_theta(x_t, t)
    
    # Reconstruct denoised step
    mean = (1 / sqrt(alpha_t)) * (x_t - (beta_t / sqrt(1 - alpha_bar_t)) * pred_noise)
    sigma_t = sqrt(tilde_beta_t)  # or sqrt(beta_t)
    
    x_{t-1} = mean + sigma_t * z
return x_0
```

---

## Variance Schedules and Noise Dynamics

The selection of $\beta_t$ controls how rapidly information is destroyed. 

1. **Linear Schedule**: Ho et al. (2020) proposed a linear schedule ramping from $\beta_1 = 10^{-4}$ to $\beta_T = 0.02$. However, for larger $T$, the signal is destroyed too quickly in the early forward steps, making learning difficult.
2. **Cosine Schedule**: Nichol & Dhariwal (2021) proposed a cosine-based variance schedule that maintains data structure much longer:
   $$\bar{\alpha}_t = \frac{f(t)}{f(0)} \quad \text{where} \quad f(t) = \cos^2\left(\frac{t/T + s}{1 + s} \frac{\pi}{2}\right)$$
   This schedule yields smoother noise transitions and improves log-likelihood scores.

---

## Worked Example: A Single Forward Step

Let's compute a single forward corruption step for a one-dimensional data point $x_0 = 2.0$.
* Assume timestep $t$, where the variance schedule gives $\beta_t = 0.1$.
* Therefore, $\alpha_t = 1 - \beta_t = 0.9$.
* Assume the accumulated product up to the previous step is $\bar{\alpha}_{t-1} = 0.8$.
* The accumulated product at step $t$ is:
  $$\bar{\alpha}_t = \bar{\alpha}_{t-1} \cdot \alpha_t = 0.8 \cdot 0.9 = 0.72$$
* We sample standard normal noise $\epsilon \sim \mathcal{N}(0, 1)$. Let $\epsilon = 0.5$.
* We calculate the corrupted sample $x_t$:
  $$x_t = \sqrt{\bar{\alpha}_t} x_0 + \sqrt{1 - \bar{\alpha}_t} \epsilon$$
  $$x_t = \sqrt{0.72} (2.0) + \sqrt{1 - 0.72} (0.5)$$
  $$x_t \approx 0.8485 (2.0) + 0.5291 (0.5)$$
  $$x_t \approx 1.6970 + 0.2646 = 1.9616$$
* The original signal $x_0 = 2.0$ has been corrupted to $1.9616$ at step $t$. During training, the neural network $\epsilon_\theta(1.9616, t)$ will take this corrupted value and attempt to predict the target noise value $\epsilon = 0.5$.

## Related

- [[Denoising Score Matching]]
- [[Denoising Diffusion Implicit Models]]
- [[Classifier-Free Guidance]]
- [[Latent Diffusion Models]]
- [[What are Diffusion Models?]]
