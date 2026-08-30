# How diffusion models work: the math from scratch

Sergios Karagiannakos, Nikolas Adaloglou on 2022-09-29 · 14 mins

Source: https://theaisummer.com/diffusion-models/

Diffusion models are state-of-the-art generative models for diverse high-resolution images (GLIDE, DALL·E 2, Imagen, Stable Diffusion). This post builds DDPM math from scratch (Sohl-Dickstein; Ho et al. 2020), with shorter coverage of guided diffusion, scaling (cascade + latent diffusion), and score-based / SDE formulations.

## Diffusion process

Forward process: gradually add Gaussian noise to image x₀ over T Markov steps. Reverse process: train a neural network to denoise step-by-step and generate new samples. Iterative refinement is powerful but slower than GAN sampling.

## Forward diffusion

Markov chain q(x_t | x_{t-1}) = N(√(1−β_t) x_{t-1}, β_t I). Reparameterization with α_t = 1−β_t, ᾱ_t = ∏α_s gives closed-form sampling:

x_t = √ᾱ_t x₀ + √(1−ᾱ_t) ε,  ε ~ N(0,I)

Variance schedule β_t can be linear (Ho: 10⁻⁴→0.02) or cosine (Nichol & Dhariwal 2021).

## Reverse diffusion

Learn p_θ(x_{t-1}|x_t) = N(μ_θ(x_t,t), Σ_θ(x_t,t)). As T→∞, x_T ≈ N(0,I); sampling starts from noise.

## Training

ELBO decomposes into reconstruction L₀, prior-matching L_T (no trainable params), and denoising terms L_{t-1}. Conditioning on x₀ makes q(x_{t-1}|x_t,x₀) tractable. Network predicts noise ε_θ(x_t,t); simplified loss:

L_simple = E[||ε − ε_θ(√ᾱ_t x₀ + √(1−ᾱ_t)ε, t)||²]

Ho et al. fixed variance; Nichol et al. 2021 learned covariance too.

## Architecture

U-Net (Wide ResNet blocks, group norm, self-attention) with sinusoidal timestep embedding; input/output same spatial size.

## Guided diffusion

Classifier guidance: separate classifier f_φ(y|x_t,t) perturbs mean via ∇ log f_φ. GLIDE uses CLIP embedding dot-product guidance for text.

Classifier-free guidance (Ho & Salimans): single network trained with y randomly dropped; inference interpolates conditional and unconditional ε predictions. Key for Imagen text alignment.

## Scaling

Cascade diffusion (Ho et al. 2021): pipeline of super-resolution diffusion models; conditioning augmentation (Gaussian blur) reduces compounding error.

Latent diffusion / Stable Diffusion (Rombach et al.): encode to latent z, diffuse in low-dim space, decode. Loss L_LDM = E[||ε − ε_θ(z_t,t)||²].

## Score-based models

Song & Ermon: score matching + Langevin dynamics. NCSN adds multi-scale noise. Song et al. 2021 unifies DDPM and score models via SDEs; reverse SDE uses learned score s_θ(x,t).

## Summary bullets

- Forward noise + learned reverse denoising
- ELBO training; predict ε not mean
- U-Net backbone; guided / classifier-free conditioning
- Cascade and latent diffusion for high resolution
- Score-based and SDE formulations equivalent in spirit
