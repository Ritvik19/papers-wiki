# Classifier-Free Guidance

**Type**: concept  
**Tags**: #concept

## Overview

Classifier-Free Guidance (CFG) is a technique for steering conditional diffusion models by linearly interpolating between conditional and unconditional score estimates. It avoids the need to train a separate noise-robust classifier.

## Appearances

- [[What are Diffusion Models?]] — Section on guided diffusion and generation paradigms.
- [[How Diffusion Models Work: The Math from Scratch]] — AI Summer introduction to classifier vs classifier-free guidance; Imagen alignment role; Ho & Salimans interpolation formula.
- [[An Overview of Classifier-Free Guidance for Diffusion Models]] — Extended survey: classifier guidance derivation, γ=w−1 formulation, dynamic thresholding, CADS, limited-interval CFG, spatial CFG, attention appendix.
- [[An Overview of Classifier-Free Diffusion Guidance: Impaired Model Guidance with a Bad Version of Itself (Part 2)]] — Positive/negative generalization; SAG, PAG, autoguidance, ICG.
- [[Papers Explained - GLIDE]] — An empirical study comparing CLIP guidance against classifier-free guidance for text-to-image synthesis.

## Detailed Formulations

In traditional classifier-guided diffusion, a separate classifier $p_\phi(y \mid x_t)$ must be trained on noisy latents $x_t$ to guide the reverse process mean $\mu_\theta(x_t \mid y)$ by additively perturbing it with the score of the classifier:

$$\tilde{\epsilon}_\theta(x_t, y) = \epsilon_\theta(x_t, y) - s \sqrt{1 - \bar{\alpha}_t} \nabla_{x_t} \log p_\phi(y \mid x_t)$$

To eliminate this separate classifier, Ho & Salimans (2021) proposed **Classifier-Free Guidance**. During training, the conditioning variable $y$ (such as a text prompt or class index) is randomly replaced with a null token $\emptyset$ with a fixed probability (typically $10\%$ to $20\%$). This trains a single neural network to predict both conditional noise $\epsilon_\theta(x_t, y)$ and unconditional noise $\epsilon_\theta(x_t, \emptyset)$.

During inference, the guided noise prediction $\tilde{\epsilon}_\theta(x_t, y)$ is computed by extrapolating away from the unconditional prediction towards the conditional prediction, scaled by a guidance factor $w \ge 0$:

$$\tilde{\epsilon}_\theta(x_t, y) = (1 + w)\epsilon_\theta(x_t, y) - w\epsilon_\theta(x_t, \emptyset)$$

Rearranging terms shows that this formulation scales up the implicit classifier score:

$$\tilde{\epsilon}_\theta(x_t, y) = \epsilon_\theta(x_t, \emptyset) + (1 + w) \left( \epsilon_\theta(x_t, y) - \epsilon_\theta(x_t, \emptyset) \right)$$

Increasing the guidance scale $w$ boosts prompt adherence and sample fidelity (improving metrics like CLIP score) at the cost of sample diversity (increasing truncation risk or saturation).

---

## Step-by-Step Derivation via Bayes' Rule

To understand how classifier-free guidance operates without an external classifier, we derive the implicit classifier gradient using Bayes' rule.

1. **Apply Bayes' Rule**:
   The conditional data probability $p(x_t \mid y)$ is given by:
   $$p(x_t \mid y) = \frac{p(y \mid x_t) p(x_t)}{p(y)}$$

2. **Take the Gradient of the Log-Likelihood**:
   $$\nabla_{x_t} \log p(x_t \mid y) = \nabla_{x_t} \log p(y \mid x_t) + \nabla_{x_t} \log p(x_t) - \nabla_{x_t} \log p(y)$$

   Since $p(y)$ does not depend on the latent state $x_t$, its spatial gradient is zero ($\nabla_{x_t} \log p(y) = 0$). This simplifies the equation to:
   $$\nabla_{x_t} \log p(x_t \mid y) = \nabla_{x_t} \log p(y \mid x_t) + \nabla_{x_t} \log p(x_t)$$

3. **Isolate the Classifier Gradient**:
   $$\nabla_{x_t} \log p(y \mid x_t) = \nabla_{x_t} \log p(x_t \mid y) - \nabla_{x_t} \log p(x_t)$$

4. **Map to Score Functions**:
   Using the standard connection between the score function $\nabla_{x_t} \log p(x_t)$ and the noise predictor $\epsilon_\theta(x_t, t)$:
   $$\nabla_{x_t} \log p(x_t) \approx -\frac{1}{\sqrt{1 - \bar{\alpha}_t}} \epsilon_\theta(x_t, \emptyset)$$
   $$\nabla_{x_t} \log p(x_t \mid y) \approx -\frac{1}{\sqrt{1 - \bar{\alpha}_t}} \epsilon_\theta(x_t, y)$$

   Substituting these approximations back into step 3:
   $$\nabla_{x_t} \log p(y \mid x_t) \approx -\frac{1}{\sqrt{1 - \bar{\alpha}_t}} \left( \epsilon_\theta(x_t, y) - \epsilon_\theta(x_t, \emptyset) \right)$$

5. **Formulate the Guided Score**:
   In classifier guidance, we amplify the classifier's gradient with a scale factor $w$:
   $$\tilde{\nabla}_{x_t} \log p(x_t \mid y) = \nabla_{x_t} \log p(x_t \mid y) + w \nabla_{x_t} \log p(y \mid x_t)$$

   Substituting the conditional score and the implicit classifier gradient:
   $$\tilde{\nabla}_{x_t} \log p(x_t \mid y) \approx -\frac{1}{\sqrt{1 - \bar{\alpha}_t}} \epsilon_\theta(x_t, y) - \frac{w}{\sqrt{1 - \bar{\alpha}_t}} \left( \epsilon_\theta(x_t, y) - \epsilon_\theta(x_t, \emptyset) \right)$$
   $$\tilde{\nabla}_{x_t} \log p(x_t \mid y) \approx -\frac{1}{\sqrt{1 - \bar{\alpha}_t}} \left[ (1 + w)\epsilon_\theta(x_t, y) - w\epsilon_\theta(x_t, \emptyset) \right]$$

This matches the classifier-free guidance update rule exactly, demonstrating that the linear interpolation of noise predictions mathematically mirrors classifier-guided diffusion without requiring a separate classifier model.

---

## Guidance Dynamics and Dynamic Thresholding

While increasing the guidance scale $w$ dramatically improves image-text alignment, it introduces a severe artifact known as the **exposure problem** or **saturation collapse**. Because the noise prediction $\tilde{\epsilon}_\theta(x_t, y)$ is scaled up, it often overshoots the standard normal distribution bounds $[-1, 1]$ in early denoising steps.

To combat this, Saharia et al. (2022) in Google's **Imagen** introduced two key thresholding techniques applied at each denoising step on the reconstructed clean estimate $\hat{x}_0$:

### 1. Static Thresholding
At each step, the pixel values of the predicted $\hat{x}_0$ are clamped directly to the target range:
$$\hat{x}_0^{\text{static}} = \text{clamp}(\hat{x}_0, -1, 1)$$
This prevents unbounded latent explosion but still causes flat, over-exposed, and low-contrast regions at high guidance scales ($w > 10$).

### 2. Dynamic Thresholding
Instead of clipping peak pixels, dynamic thresholding rescales the activation of the entire image to preserve structural contrast:
1. Define a high percentile threshold $p \in (0.5, 1)$ (typically $p = 99.5\%$).
2. Let $s$ be the $p$-th absolute percentile value of all pixels in the reconstructed image $\hat{x}_0$:
   $$s = \max\left(\text{percentile}(|\hat{x}_0|, p), 1.0\right)$$
3. Scale the image back and clamp:
   $$\hat{x}_0^{\text{dynamic}} = \text{clamp}\left( \frac{\hat{x}_0}{s}, -1, 1 \right) \cdot s$$

If the absolute pixel values exceed $1.0$, dividing by $s$ pulls the extreme activations back into the $[-1, 1]$ range uniformly, allowing the model to leverage extremely high guidance scales ($w = 15$ to $20$) to generate vivid and highly detailed images without saturation artifacts.

---

## Guidance Paradigms Comparison

| Feature | Classifier Guidance | Classifier-Free Guidance (CFG) | CLIP Guidance |
| :--- | :--- | :--- | :--- |
| **Separate Classifier Required** | Yes (trained on noisy latent states) | **No** (joint single-network modeling) | Yes (uses frozen pretrained CLIP image-text encoders) |
| **Model Inferences per Step** | 1 forward (diffusion) + 1 gradient backward (classifier) | **2 forwards** (conditional + unconditional) | 1 forward (diffusion) + 1 gradient backward (CLIP) |
| **Training Pipeline** | Complex (classifier must be robust to all noise levels) | **Simple** (randomly drop condition $y \to \emptyset$ at training) | Simple (leverages zero-shot pretrained models) |
| **Alignment Strength** | Moderate (tied to classifier categories) | **Exceptional** (open-ended language generation) | Strong (direct text-image cosine distance alignment) |
| **Adversarial Susceptibility** | High (can easily exploit classifier gradients) | **Extremely Low** (stays on natural generative path) | High (susceptible to adversarial high-frequency noise) |

---

## Worked Example: A Guided Denoising Step

Let's compute a classifier-free guidance noise correction step.
* Let the guidance scale be $w = 3.0$ (which corresponds to an extrapolation factor of $1 + w = 4.0$).
* Let the unconditional noise prediction at a given latent coordinate be $\epsilon_\theta(x_t, \emptyset) = 0.20$.
* Let the conditional noise prediction (conditioned on prompt $y$) at the same coordinate be $\epsilon_\theta(x_t, y) = 0.50$.

1. **Calculate using the standard CFG formula**:
   $$\tilde{\epsilon}_\theta(x_t, y) = (1 + w)\epsilon_\theta(x_t, y) - w\epsilon_\theta(x_t, \emptyset)$$
   $$\tilde{\epsilon}_\theta(x_t, y) = (1 + 3.0) \cdot 0.50 - 3.0 \cdot 0.20$$
   $$\tilde{\epsilon}_\theta(x_t, y) = 4.0 \cdot 0.50 - 0.60 = 2.00 - 0.60 = 1.40$$

2. **Verify using the implicit classifier score representation**:
   $$\tilde{\epsilon}_\theta(x_t, y) = \epsilon_\theta(x_t, \emptyset) + (1 + w) \left( \epsilon_\theta(x_t, y) - \epsilon_\theta(x_t, \emptyset) \right)$$
   $$\tilde{\epsilon}_\theta(x_t, y) = 0.20 + 4.0 \cdot (0.50 - 0.20) = 0.20 + 4.0 \cdot 0.30 = 0.20 + 1.20 = 1.40$$

The final guided noise prediction is pushed from the baseline $0.50$ up to $1.40$, dramatically magnifying the semantic features demanded by prompt $y$.

## Related

- [[Denoising Diffusion Probabilistic Models]]
- [[Autoguidance]]
- [[Perturbed Attention Guidance]]
- [[An Overview of Classifier-Free Guidance for Diffusion Models]]
- [[An Overview of Classifier-Free Diffusion Guidance: Impaired Model Guidance with a Bad Version of Itself (Part 2)]]
- [[Papers Explained - GLIDE]]
- [[Latent Diffusion Models]]
- [[What are Diffusion Models?]]

#concept
#topic
