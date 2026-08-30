# MAL

**Type**: concept  
**Tags**: #concept

## Overview

Minimax Active Learning (MAL; Ebrahimi et al., 2021) extends [[VAAL]] with an explicit **uncertainty** signal. Encoder $F$ minimizes entropy on unlabeled features (cluster similar predictions); classifier $C$ maximizes entropy adversarially (avoid premature commitment on unknown labels). Acquisition combines VAAL-style discriminator diversity (low $D$ score) with high classifier entropy.

## Appearances

- [[Learning with not Enough Data Part 2: Active Learning]] — ImageNet table vs BALD, VAAL, core-set; image classification and segmentation.

## Training phases

**(1) Supervised on labeled data** — standard CE on $\ell_2$-normalized features $F(\mathbf{x}^l)$ with weight matrix $\mathbf{W} \in \mathbb{R}^{d \times K}$.

**(2) Minimax on unlabeled data**:
$$\mathcal{L}_\text{Ent} = -\sum_{k=1}^K p(y=k|\mathbf{u})\log p(y=k|\mathbf{u})$$
$$\theta^*_F, \theta^*_C = \min_F \max_C \mathcal{L}_\text{Ent}$$

| Player | Update | Effect |
|--------|--------|--------|
| $F$ | Minimize $\mathcal{L}_\text{Ent}$ | Similar features for similar predicted labels |
| $C$ | Maximize $\mathcal{L}_\text{Ent}$ | Uniform-ish predictions until labels arrive |

Discriminator $D$ trained as in VAAL on latents from $F$.

## Acquisition (hybrid)

| Signal | Score | Interpretation |
|--------|-------|----------------|
| Diversity | Low $D(\mathbf{z})$ | Far from labeled latent distribution |
| Uncertainty | High $H(p(y|\mathbf{u}))$ from $C$ | Model not confident yet |

Select points that are both unfamiliar and entropic — addresses pure-VAAL missing uncertainty and pure-entropy missing coverage.

## Related

- [[VAAL]]
- [[BALD]]
- [[BADGE]]
- [[Active Learning]]
