# Score-Based Generative Models

**Type**: concept  
**Tags**: #concept

## Overview

Score-based generative models learn the score function \(\nabla_x \log p(x)\) — the gradient of the log data density — without estimating the partition function. Samples are drawn via Langevin dynamics or by solving reverse stochastic differential equations (SDEs). Song et al. (2021) showed this framework unifies score matching with [[Denoising Diffusion Probabilistic Models]] (DDPM).

## Appearances

- [[How Diffusion Models Work: The Math from Scratch]] — Score matching, NCSN multi-scale noise, and SDE formulation as parallel to DDPM.
- [[What are Diffusion Models?]] — Master survey unifying DDPM, NCSN, and continuous-time SDE diffusion.

## Notes

**Score matching** (Song & Ermon 2019): train \(s_\theta(x) \approx \nabla_x \log p(x)\) by minimizing Fisher divergence; sample with Langevin updates \(x_t = x_{t-1} + \frac{\delta}{2}\nabla_x \log p(x_{t-1}) + \sqrt{\delta}\,\epsilon\).

**NCSN** (Noise Conditional Score Networks): multi-scale Gaussian perturbations \(p_{\sigma_i}(x)\) fix inaccurate scores in low-density regions; network \(s_\theta(x, i)\) is conditioned on noise level.

**SDE formulation** (Song et al. 2021): forward diffusion as \(d\mathbf{x} = \mathbf{f}(\mathbf{x}, t)\,dt + g(t)\,d\mathbf{w}\); reverse SDE uses learned score \(s_\theta(\mathbf{x}, t)\). DDPM discretizations are special cases.

Guided diffusion models learn \(\nabla_x \log p(x_t \mid y)\) directly — related to score-based views but typically use DDPM sampling rather than raw Langevin dynamics.

## Related

- [[Score Matching]]
- [[Denoising Score Matching]]
- [[Denoising Diffusion Probabilistic Models]]
- [[What are Diffusion Models?]]
- [[How Diffusion Models Work: The Math from Scratch]]
