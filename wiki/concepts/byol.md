# BYOL

**Type**: concept  
**Tags**: #concept

## Overview

Bootstrap Your Own Latent (BYOL; Grill et al., 2020) is a **negative-free** self-supervised visual representation learning method. An online encoder predicts the EMA target encoder's representation of a second augmented view of the same image, using a predictor MLP to break symmetry. Despite no explicit negative pairs, BYOL learns useful features when combined with batch normalization and EMA weight updates.

## Appearances

- [[Grokking Self-Supervised (Representation) Learning: How It Works in Computer Vision and Why]] — pedagogical walkthrough: predictor network, EMA teacher, BN as implicit contrastive learning; Fetterman & Albrecht ablation showing collapse without BN.
- [[Contrastive Representation Learning]] — listed in SSL paradigm comparison table as non-contrastive (MSE on cosine distance, BN anti-collapse).
- [[Contrastive Learning]] — paradigm comparison table entry.
- [[Mean Teacher]] — related EMA teacher-student weight update pattern.

## Notes

Architecture: two augmented views → online network + predictor vs stop-gradient target network; target weights updated by EMA ($w_{teacher} \leftarrow k\, w_{teacher} + (1-k)\, w_{student}$, typically $k > 0.95$). Mean subtraction from batch normalization substitutes for explicit negative contrast in the loss denominator.

## Related

- [[SimCLR]]
- [[MoCo]]
- [[Mean Teacher]]
- [[Batch Normalization]]
- [[Contrastive Learning]]
- [[Papers Explained 249 - DINO]]
