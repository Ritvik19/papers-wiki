# Representation Learning

**Type**: concept  
**Tags**: #concept

## Overview

Representation learning discovers useful features from data automatically rather than relying on hand-crafted features. Deep learning is representation learning with multiple learned layers; good representations disentangle explanatory factors and transfer across tasks.

## Appearances

- [[Deep Learning]] — Chapter 15 surveys greedy layer-wise pretraining, transfer learning, distributed representations, exponential gains from depth, and clues for discovering underlying causes.
- [[Self-Supervised Representation Learning]] — Synthesizes major self-supervised representation learning techniques across image, video, and robotic control modalities.
- [[Learning with not Enough Data Part 1: Semi-Supervised Learning]] — Manifold and cluster assumptions (H1–H4) underpin SSL; self-supervised pre-training increasingly replaces dedicated SSL.
- [[Grokking Self-Supervised (Representation) Learning: How It Works in Computer Vision and Why]] — CV-focused SSL pedagogy: contrastive feature-space objectives, augmentation design, mode collapse, EMA teachers, SimCLR/BYOL/DINO.

## Notes

The book's framing (Figure 1.4) places deep learning inside representation learning inside machine learning. Modern foundation models inherit this view at scale—pretraining learns general representations fine-tuned for downstream tasks—though the specific pretraining objectives evolved beyond the book's autoencoder/RBM emphasis.

## Related

- [[Transfer Learning]]
- [[Distributed Representations]]
- [[Autoencoders]]
- [[Greedy Layer-Wise Pretraining]]
- [[Deep Learning]]
- [[Embedding and Retrieval]]
- [[Model Distillation]]
- [[Self-Supervised Representation Learning]]
- [[Semi-Supervised Learning]]
- [[Learning with not Enough Data Part 1: Semi-Supervised Learning]]

