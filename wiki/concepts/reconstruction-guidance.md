# reconstruction-guidance

**Type**: concept  
**Tags**: #concept

## Overview

In video generation, conditional sampling is essential for tasks such as **autoregressive extension** (generating subsequent clips conditioned on prior frames), **temporal interpolation** (generating in-between frames to increase frame rate), and **spatial super-resolution** (upscaling low-resolution sequences). **Reconstruction guidance** is an training-free conditioning method proposed by Ho & Salimans et al. (2022) in the Video Diffusion Models (VDM) framework. It allows a joint diffusion model to generate a set of target frames $\mathbf{x}^b$ conditioned on a set of constraint frames $\mathbf{x}^a$, denoted as $p(\mathbf{x}^b \mid \mathbf{x}^a)$, by modifying the denoising score function using an auxiliary MSE gradient step during inference.

---

## Appearances

- [[Diffusion Models for Video Generation]] — Survey post where reconstruction guidance is established as the primary mathematical approach to autoregressive conditioning and cascading super-resolution.

---

## Mathematical Derivation

Let the joint clean video sequence be partitioned into $\mathbf{x} = [\mathbf{x}^a, \mathbf{x}^b]$, where $\mathbf{x}^a$ are the conditioning frames (known) and $\mathbf{x}^b$ are the target frames to be generated. Let the noisy latent variables at step $t$ be $\mathbf{z}_t = [\mathbf{z}^a_t, \mathbf{z}^b_t]$.

We wish to sample from the conditional posterior trajectory $p(\mathbf{z}^b_{t-1} \mid \mathbf{z}^b_t, \mathbf{x}^a)$. The standard denoising step requires estimating the clean target state. Under the standard diffusion framework, the conditional expectation of the clean targets $\mathbf{x}^b$ given the current noisy latent state $\mathbf{z}_t$ and the clean constraints $\mathbf{x}^a$ is:

$$\mathbb{E}_q [\mathbf{x}^b \mid \mathbf{z}_t, \mathbf{x}^a] = \mathbb{E}_q [\mathbf{x}^b \mid \mathbf{z}_t] + \frac{\sigma_t^2}{\alpha_t} \nabla_{\mathbf{z}^b_t} \log q(\mathbf{x}^a \mid \mathbf{z}_t)$$

Where:
- $\alpha_t$ and $\sigma_t$ are the signal and noise coefficients of the schedule.
- $\mathbb{E}_q [\mathbf{x}^b \mid \mathbf{z}_t]$ is approximated by the model's clean data prediction $\hat{\mathbf{x}}^b_\theta(\mathbf{z}_t)$.
- $q(\mathbf{x}^a \mid \mathbf{z}_t)$ is the transition probability of the conditioning data given the noisy state.

### The Gaussian Approximation
Since the clean data distribution is unknown, the exact transition probability $q(\mathbf{x}^a \mid \mathbf{z}_t)$ has no closed form. VDM resolves this by approximating $q(\mathbf{x}^a \mid \mathbf{z}_t)$ as a Gaussian distribution centered at the model's denoised reconstruction of the constraint frames $\hat{\mathbf{x}}^a_\theta(\mathbf{z}_t)$:

$$q(\mathbf{x}^a \mid \mathbf{z}_t) \approx \mathcal{N}\left(\mathbf{x}^a; \hat{\mathbf{x}}^a_\theta(\mathbf{z}_t), \frac{\sigma_t^2}{\alpha_t^2}\mathbf{I}\right)$$

Taking the log density of this Gaussian:

$$\log q(\mathbf{x}^a \mid \mathbf{z}_t) \approx -\frac{\alpha_t^2}{2\sigma_t^2} \|\mathbf{x}^a - \hat{\mathbf{x}}^a_\theta(\mathbf{z}_t)\|^2_2 + \text{constant}$$

### Gradient of the Constraint
We take the gradient of the log density with respect to the generated latent variables $\mathbf{z}^b_t$:

$$\nabla_{\mathbf{z}^b_t} \log q(\mathbf{x}^a \mid \mathbf{z}_t) \approx -\frac{\alpha_t^2}{2\sigma_t^2} \nabla_{\mathbf{z}^b_t} \|\mathbf{x}^a - \hat{\mathbf{x}}^a_\theta(\mathbf{z}_t)\|^2_2$$

Plugging this gradient back into the conditional expectation equation:

$$\mathbb{E}_q [\mathbf{x}^b \mid \mathbf{z}_t, \mathbf{x}^a] \approx \hat{\mathbf{x}}^b_\theta(\mathbf{z}_t) - \frac{\alpha_t}{2} \nabla_{\mathbf{z}^b_t} \|\mathbf{x}^a - \hat{\mathbf{x}}^a_\theta(\mathbf{z}_t)\|^2_2$$

### Conditioning Scale and the Denoising Step
To allow stronger, user-controlled conditioning, a reconstruction guidance scale factor $w_r \geq 1$ is introduced. The final guided reconstruction estimate $\tilde{\mathbf{x}}^b_\theta(\mathbf{z}_t)$ used for the denoising update is:

$$\tilde{\mathbf{x}}^b_\theta(\mathbf{z}_t) = \hat{\mathbf{x}}^b_\theta(\mathbf{z}_t) - \frac{w_r \alpha_t}{2} \nabla_{\mathbf{z}^b_t} \|\mathbf{x}^a - \hat{\mathbf{x}}^a_\theta(\mathbf{z}_t)\|^2_2$$

During sampling:
1. The model predicts both $\hat{\mathbf{x}}^a_\theta(\mathbf{z}_t)$ and $\hat{\mathbf{x}}^b_\theta(\mathbf{z}_t)$ using the joint noisy state $\mathbf{z}_t$.
2. The MSE loss $\|\mathbf{x}^a - \hat{\mathbf{x}}^a_\theta(\mathbf{z}_t)\|^2_2$ is computed on the conditioning frames.
3. The gradient of this loss with respect to the target latents $\mathbf{z}^b_t$ is backpropagated.
4. The predicted target state $\hat{\mathbf{x}}^b_\theta$ is shifted in the direction that minimizes conditioning error, steering target frames to match the boundary constraints.

---

## Applications in Video Diffusion

Reconstruction guidance acts as a unified operator for three main video tasks:

```
Conditional Partitioning:
[     x^a (Conditioning)     ] [       x^b (Generated Target)       ]
  - Video extrapolation: x^a is a prior clip, x^b is the future clip.
  - Video interpolation: x^a are sparse keyframes, x^b are missing middle frames.
  - Super-Resolution:   x^a is a low-res sequence, x^b is the high-res sequence.
```

### 1. Autoregressive Extension
For long video generation, generating all frames at once is memory-prohibitive. Instead, a model generates a clip of length $N$, and then sequentially generates the next $N$ frames by setting the last few frames of the previous clip as the conditioning frames $\mathbf{x}^a$. Reconstruction guidance ensures that the transition between the two clips is seamless without any visual boundary seams.

### 2. Temporal Interpolation (Frame Upsampling)
A base model generates a low-frame-rate video (e.g., 8 fps). A temporal super-resolution model is then conditioned on these 8 frames (as $\mathbf{x}^a$) to generate the missing intermediate frames $\mathbf{x}^b$ to upsample the video to 24 fps.

### 3. Spatial Super-Resolution Cascades
In cascaded diffusion architectures (such as Imagen Video), high-resolution spatial models take a low-resolution video $\mathbf{x}^a$ as input and apply reconstruction guidance to steer the high-resolution output $\mathbf{x}^b$ to remain downsampling-compatible with $\mathbf{x}^a$.

---

## Worked Example: Toy 1D Reconstruction Guidance Step

Let's compute an adjusted reconstruction step for a toy 1D system.
- True conditioning value: $\mathbf{x}^a = 1.0$
- Signal schedule at current step: $\alpha_t = 0.80$
- Guidance scale: $w_r = 1.50$
- Target latent variable: $z^b_t = 0.50$

Assume the model's reconstruction of the conditioning frame is parameterized as a simple function of the target latent:
$$\hat{x}^a_\theta(z^b_t) = 0.60 + 0.30 (z^b_t)^2$$
Let the model's base prediction for the target frame be:
$$\hat{x}^b_\theta = 0.40$$

Let's compute the guided target reconstruction $\tilde{x}^b_\theta$:

1. **Calculate the conditioning reconstruction value at $z^b_t = 0.50$**:
   $$\hat{x}^a_\theta(0.50) = 0.60 + 0.30(0.25) = 0.675$$

2. **Compute the MSE loss**:
   $$\text{MSE} = \|x^a - \hat{x}^a_\theta\|^2_2 = (1.0 - 0.675)^2 = (0.325)^2 = 0.105625$$

3. **Compute the derivative of the MSE with respect to $z^b_t$**:
   $$\frac{d}{d z^b_t} \|x^a - \hat{x}^a_\theta\|^2_2 = 2 (x^a - \hat{x}^a_\theta) \cdot \left( -\frac{d}{d z^b_t} \hat{x}^a_\theta \right)$$
   - Since $\frac{d}{d z^b_t} \hat{x}^a_\theta = 0.60 z^b_t$:
   $$\frac{d}{d z^b_t} \|x^a - \hat{x}^a_\theta\|^2_2 = 2 (1.0 - 0.675) \cdot (-0.60 \cdot 0.50) = 2 (0.325) \cdot (-0.30) = -0.195$$

4. **Calculate the guidance correction term**:
   $$\text{Correction} = -\frac{w_r \alpha_t}{2} \nabla_{z^b_t} \text{MSE} = -\frac{1.5 \cdot 0.8}{2} \cdot (-0.195) = -0.60 \cdot (-0.195) = 0.117$$

5. **Compute the adjusted target prediction**:
   $$\tilde{x}^b_\theta = \hat{x}^b_\theta + \text{Correction} = 0.40 + 0.117 = 0.517$$

The reconstruction guidance successfully adjusted the target frame prediction from $0.40$ to $0.517$, shifting it to satisfy the constraint imposed by the conditioning frame.

---

## Related

- [[Denoising Diffusion Probabilistic Models]] — Standard diffusion models modeling joint distributions.
- [[Classifier-Free Guidance]] — Guidance using auxiliary score scaling.
- [[space-time-u-net]] — Spatial-temporal architecture utilizing cascading super-resolution modules.
