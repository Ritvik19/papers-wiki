# VAAL

**Type**: concept  
**Tags**: #concept

## Overview

Variational Adversarial Active Learning (VAAL; Sinha et al., ICCV 2019) selects unlabeled samples in a **latent space** without using task loss or softmax confidence. A $\beta$-VAE maps inputs to latents; a discriminator $D$ learns to separate labeled from unlabeled encodings; acquisition picks unlabeled points with **low** $D(\mathbf{z})$ — farthest from the labeled manifold in latent space.

## Appearances

- [[Learning with not Enough Data Part 2: Active Learning]] — Full loss equations, ablations (joint VAE+discriminator training critical), robustness to biased initial pools and noisy oracles.

## Architecture

| Component | Role |
|-----------|------|
| $\beta$-VAE encoder $q_\phi(\mathbf{z}|\mathbf{x})$ | Maps labeled $\mathbf{x}^l$ and unlabeled $\mathbf{u}$ to latents |
| Decoder $p_\theta(\mathbf{x}|\mathbf{z})$ | Reconstruction (ELBO) |
| Discriminator $D(\mathbf{z})$ | Predicts labeled (1) vs unlabeled (0) |

**Acquisition**: unlabeled $\mathbf{u}$ with low $D(q_\phi(\mathbf{z}^u|\mathbf{u}))$ — discriminator thinks they look unlike labeled pool → **diversity**.

## Losses

**VAE** (reconstruction + adversarial fooling of $D$):
$$\mathcal{L}_\text{VAE} = \lambda_1 \mathcal{L}^\text{rec}_\text{VAE} + \lambda_2 \mathcal{L}^\text{adv}_\text{VAE}$$

**Discriminator**:
$$\mathcal{L}_D = -\mathbb{E}[\log D(\mathbf{z}^l)] - \mathbb{E}[\log(1 - D(\mathbf{z}^u))]$$

Prior $p(\tilde{\mathbf{z}})$ is standard Gaussian; $\beta$ controls KL weight in VAE.

## Design notes

- Task classifier is **not** required for scoring — useful when representation learning decouples from downstream head
- Joint training of VAE and $D$ is essential (ablation)
- Extended by [[MAL]] with explicit uncertainty via minimax entropy

## Related

- [[MAL]]
- [[Active Learning]]
- [[Core-Set Active Learning]]
- [[Contrastive Active Learning]]
