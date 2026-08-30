# v-parameterization

**Type**: concept  
**Tags**: #concept

## Overview

Velocity prediction ($\mathbf{v}$-parameterization) is a diffusion model target formulation proposed by Salimans & Ho (2022) to resolve sampling instabilities, particularly **color shifts** and contrast degradation, at high resolution and in video generation. Unlike standard formulations that predict either the original clean data ($\mathbf{x}_0$) or the added noise ($\boldsymbol{\epsilon}$), $\mathbf{v}$-parameterization models a combined velocity vector:
$$\mathbf{v}_t \equiv \alpha_t \boldsymbol{\epsilon} - \sigma_t \mathbf{x}$$
where $\alpha_t$ and $\sigma_t$ define the signal and noise coefficients of the differentiable diffusion schedule.

## Appearances

- [[What are Diffusion Models?]] — Pre-read foundations of diffusion targets.
- [[Diffusion Models for Video Generation]] — Primary survey post where $\mathbf{v}$-parameterization is established as a critical technique to prevent color drift across frames.

---

## Detailed Mathematical Derivation

Let the forward diffusion process be defined as:
$$\mathbf{z}_t = \alpha_t \mathbf{x} + \sigma_t \boldsymbol{\epsilon} \quad \text{where} \quad \boldsymbol{\epsilon} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$$

To derive the $\mathbf{v}$-parameterization, we apply a geometric reparameterization in the **angular coordinate** space by defining the angle $\phi_t$ such that:
$$\tan \phi_t = \frac{\sigma_t}{\alpha_t}$$
Assuming a variance-preserving schedule where $\alpha_t^2 + \sigma_t^2 = 1$, we can express the coefficients as:
$$\alpha_t = \cos \phi_t, \quad \sigma_t = \sin \phi_t$$
Substituting these back into the latent variable equation:
$$\mathbf{z}_{\phi} = \cos \phi \mathbf{x} + \sin \phi \boldsymbol{\epsilon}$$
Now, we define the **velocity** $\mathbf{v}_{\phi}$ of this state representation as the derivative of $\mathbf{z}_{\phi}$ with respect to the angle $\phi$:
$$\mathbf{v}_{\phi} \equiv \frac{d\mathbf{z}_{\phi}}{d\phi} = \frac{d(\cos \phi)}{d\phi} \mathbf{x} + \frac{d(\sin \phi)}{d\phi} \boldsymbol{\epsilon}$$
Using standard derivative properties:
$$\mathbf{v}_{\phi} = -\sin \phi \mathbf{x} + \cos \phi \boldsymbol{\epsilon} = \cos \phi \boldsymbol{\epsilon} - \sin \phi \mathbf{x}$$
By restoring the original time-dependent schedule coefficients $\alpha_t = \cos\phi_t$ and $\sigma_t = \sin\phi_t$, we obtain the velocity vector formula:
$$\mathbf{v}_t = \alpha_t \boldsymbol{\epsilon} - \sigma_t \mathbf{x}$$

---

### Solving for Data and Noise

Using the system of equations defined by $\mathbf{z}_{\phi}$ and $\mathbf{v}_{\phi}$, we can solve for both the clean data $\mathbf{x}$ and the noise $\boldsymbol{\epsilon}$:

1. **Solving for $\mathbf{x}$**:
   Multiply $\mathbf{z}_{\phi}$ by $\cos \phi$ and $\mathbf{v}_{\phi}$ by $-\sin \phi$:
   $$\cos \phi \mathbf{z}_{\phi} = \cos^2 \phi \mathbf{x} + \cos \phi \sin \phi \boldsymbol{\epsilon}$$
   $$-\sin \phi \mathbf{v}_{\phi} = \sin^2 \phi \mathbf{x} - \cos \phi \sin \phi \boldsymbol{\epsilon}$$
   Summing the two equations yields:
   $$\cos \phi \mathbf{z}_{\phi} - \sin \phi \mathbf{v}_{\phi} = \left(\cos^2 \phi + \sin^2 \phi\right) \mathbf{x}$$
   Since $\cos^2 \phi + \sin^2 \phi = 1$:
   $$\mathbf{x} = \cos \phi \mathbf{z}_{\phi} - \sin \phi \mathbf{v}_{\phi}$$

2. **Solving for $\boldsymbol{\epsilon}$**:
   Multiply $\mathbf{z}_{\phi}$ by $\sin \phi$ and $\mathbf{v}_{\phi}$ by $\cos \phi$:
   $$\sin \phi \mathbf{z}_{\phi} = \cos \phi \sin \phi \mathbf{x} + \sin^2 \phi \boldsymbol{\epsilon}$$
   $$\cos \phi \mathbf{v}_{\phi} = -\cos \phi \sin \phi \mathbf{x} + \cos^2 \phi \boldsymbol{\epsilon}$$
   Summing these:
   $$\sin \phi \mathbf{z}_{\phi} + \cos \phi \mathbf{v}_{\phi} = \left(\sin^2 \phi + \cos^2 \phi\right) \boldsymbol{\epsilon}$$
   $$\boldsymbol{\epsilon} = \sin \phi \mathbf{z}_{\phi} + \cos \phi \mathbf{v}_{\phi}$$

---

## Trigonometric DDIM Update Rule

Substituting these expressions into the deterministic Denoising Diffusion Implicit Model (DDIM) update rule allows us to compute the sampling step directly in the angular space. To move from a higher noise state at angle $\phi_t$ to a lower noise state at angle $\phi_s$ ($0 \le \phi_s < \phi_t \le \frac{\pi}{2}$):

$$\mathbf{z}_{\phi_s} = \cos \phi_s \hat{\mathbf{x}}_\theta(\mathbf{z}_{\phi_t}) + \sin \phi_s \hat{\boldsymbol{\epsilon}}_\theta(\mathbf{z}_{\phi_t})$$

Substituting the solved forms of $\hat{\mathbf{x}}_\theta$ and $\hat{\boldsymbol{\epsilon}}_\theta$ using the velocity model prediction $\hat{\mathbf{v}}_\theta$:
$$\mathbf{z}_{\phi_s} = \cos \phi_s \left( \cos \phi_t \mathbf{z}_{\phi_t} - \sin \phi_t \hat{\mathbf{v}}_\theta \right) + \sin \phi_s \left( \sin \phi_t \mathbf{z}_{\phi_t} + \cos \phi_t \hat{\mathbf{v}}_\theta \right)$$

Distributing the terms:
$$\mathbf{z}_{\phi_s} = \left( \cos \phi_s \cos \phi_t + \sin \phi_s \sin \phi_t \right) \mathbf{z}_{\phi_t} + \left( \sin \phi_s \cos \phi_t - \cos \phi_s \sin \phi_t \right) \hat{\mathbf{v}}_\theta$$

Applying standard trigonometric identity functions:
$$\cos(\phi_t - \phi_s) = \cos \phi_t \cos \phi_s + \sin \phi_t \sin \phi_s$$
$$\sin(\phi_s - \phi_t) = \sin \phi_s \cos \phi_t - \cos \phi_s \sin \phi_t$$

We arrive at the elegant, simplified trigonometric DDIM update rule:
$$\mathbf{z}_{\phi_s} = \cos(\phi_t - \phi_s)\mathbf{z}_{\phi_t} + \sin(\phi_s - \phi_t)\hat{\mathbf{v}}_\theta$$

During inference, the DDIM sampler evolves the state by rotating $\mathbf{z}_{\phi_t}$ along the predicted velocity direction $\hat{\mathbf{v}}_\theta$.

---

## Why v-parameterization Prevents Color Shifts

In text-to-image and video models, standard $\boldsymbol{\epsilon}$-parameterization models tend to output predictions where high-noise states are dominated by noise rather than signal. At very early steps (high noise, close to pure Gaussian, $t \approx T$), standard MSE objectives on $\boldsymbol{\epsilon}$-prediction do not penalize errors in the weak signal component $\mathbf{x}$ heavily enough. This leads to **color drift** where the average color of the generated video frame shifts randomly.

By optimizing the $\mathbf{v}$-prediction objective:
$$\mathcal{L}_{\mathbf{v}}(\theta) = \mathbb{E}_{t, \mathbf{x}, \boldsymbol{\epsilon}} \left[ \|\mathbf{v}_t - \hat{\mathbf{v}}_\theta(\mathbf{z}_t, t)\|^2 \right]$$
the model is forced to allocate equal weighting to both signal and noise across the entire schedule. Since $\mathbf{v}_t = \cos\phi_t \boldsymbol{\epsilon} - \sin\phi_t \mathbf{x}$, at $t \approx T$ ($\phi_t \approx \pi/2$), $\mathbf{v}_t \approx -\mathbf{x}$, which forces the network to focus primarily on reconstructing the global signal structure (coarse shapes and colors) early in the denoising process.

---

## Worked Example: A Trigonometric DDIM Step

Let's compute a single deterministic denoising step using the trigonometric formulation.
- Current angle: $\phi_t = 0.90 \text{ rad}$
- Target step angle: $\phi_s = 0.60 \text{ rad}$
- Current noisy state: $\mathbf{z}_{\phi_t} = 0.85$
- Predicted velocity: $\hat{\mathbf{v}}_\theta = -0.30$

1. **Calculate the angular differences**:
   $$\phi_t - \phi_s = 0.90 - 0.60 = 0.30 \text{ rad}$$
   $$\phi_s - \phi_t = 0.60 - 0.90 = -0.30 \text{ rad}$$

2. **Compute trigonometric values**:
   $$\cos(0.30) \approx 0.9553$$
   $$\sin(-0.30) \approx -0.2955$$

3. **Substitute values into the trigonometric update equation**:
   $$\mathbf{z}_{\phi_s} = \cos(\phi_t - \phi_s)\mathbf{z}_{\phi_t} + \sin(\phi_s - \phi_t)\hat{\mathbf{v}}_\theta$$
   $$\mathbf{z}_{\phi_s} = (0.9553 \cdot 0.85) + (-0.2955 \cdot -0.30)$$
   $$\mathbf{z}_{\phi_s} = 0.8120 + 0.0887 = 0.9007$$

The latent state has successfully evolved to the lower-noise state $\mathbf{z}_{\phi_s} = 0.9007$.

---

## Related

- [[Denoising Diffusion Probabilistic Models]] — The mathematical foundation of diffusion state trajectories.
- [[Denoising Diffusion Implicit Models]] — Song et al. (2020) deterministic sampling formulation.
- [[What are Diffusion Models?]] — Master survey of diffusion mathematical formulations.
