# Contrastive Learning

**Type**: concept  
**Tags**: #concept

## Overview

Contrastive learning is a self-supervised training paradigm that teaches models to embed similar items closer together (in angle or distance) and dissimilar items farther apart, typically using losses such as InfoNCE, NT-Xent, or triplet loss. It is the dominant recipe for training modern text and vision embedding models.

## Appearances

- [[Cosine Similarity in High-Dimensional Embedding Spaces]] — identified as the key mechanism that keeps cosine similarity useful in high-dimensional spaces: contrastive training explicitly forces semantically similar items into smaller angular neighborhoods, preserving discriminative structure despite the curse of dimensionality.
- [[Contrastive Representation Learning]] — *Contrastive Representation Learning* (May 31, 2021): A highly detailed tutorial and synthesis of deep metric learning loss functions (Triplet, InfoNCE), vision frameworks (SimCLR, MoCo, Barlow Twins, BYOL, SwAV, CLIP), and natural language sentence representation alignment approaches (SimCSE, whitening).
- [[Grokking Self-Supervised (Representation) Learning: How It Works in Computer Vision and Why]] — Pedagogical CV SSL primer: GAN-as-contrastive analogy, augmentation principles, log-softmax loss decomposition, implicit contrast via BN mean subtraction.

## Notes

*   **Self-Supervised Learning Paradigm Comparison**:
    Modern representation learning evolved from standard contrastive setups to negative-free and clustering-based architectures. The table below synthesizes the core differences between these landmark paradigms:

    | Method | Contrastive? | Positive Generator | Negative / Non-Collapsing Strategy | Key Math Objective | Core Technical Innovation |
    | :--- | :---: | :--- | :--- | :--- | :--- |
    | **[[SimCLR]]** | **Yes** | Stochastic vision augmentations | In-batch negatives (requires large batch sizes) | NT-Xent (symmetric InfoNCE) | Non-linear MLP projection head; heavy augmentation composition |
    | **[[MoCo]]** | **Yes** | Stochastic vision augmentations | FIFO Queue of negative keys (decoupled from batch size) | InfoNCE with momentum encoder | Momentum key encoder; dynamic negative queue; Shuffling BN |
    | **BYOL** | **No** | Stochastic vision augmentations | None; relies on predictor network and Batch Normalization | Mean Squared Error over cosine distance | Bootstrap representations using interacting online and target networks |
    | **Barlow Twins** | **No** | Stochastic vision augmentations | None; cross-correlation normalization | Covariance matrix redundancy reduction loss | Drives cross-correlation matrix of distorted batch representations to identity |
    | **SwAV** | **No** | Stochastic vision augmentations | Multi-crop online prototype swapped clustering | Sinkhorn-Knopp swapped assignment cross-entropy | Maps representation features to shared cluster prototypes online |
    | **[[Papers Explained 100 - CLIP]]** | **Yes** | Natural image-caption pair mapping | Dense batch-wide image-text cross-negatives | Symmetric cross entropy over similarity matrix | Joint multimodal pretraining for zero-shot transfer |

*   **Mathematical Drivers**:
    *   **InfoNCE & NT-Xent**: Frame similarity learning as multi-class categorization. Rather than separating simple pairs, they maximize positive similarity against a massive noise negative distribution, maximizing the lower bound of mutual information.
    *   **Redundancy Reduction**: Barlow Twins demonstrated that representation learning does not require contrastive negatives or clustering assignments. Instead, by aligning cross-correlations to the identity matrix, it forces features to become decorrelated and informative.

*   **Key Empirical Insights**:
    *   **Hard Negative Mining**: Easy negatives (e.g. totally unrelated images) quickly yield zero loss and no gradients. Convergence and performance rely heavily on selecting semi-hard and hard negatives.
    *   **Role of Batch Normalization**: In negative-free systems like BYOL, batch statistics normalization (BN) distributes activations across the batch dimension, mathematically preventing representational collapse (where all inputs map to a constant vector).
    *   **Natural Text Augmentation**: In NLP, explicit edits (deletion, substitution) often destroy grammar or change semantics. Gaussian dropout perturbations (e.g., SimCSE) act as highly effective, task-agnostic positive generators, aligning text spaces and mitigating the anisotropy (narrow cone) problem.

## Related

- [[Cosine Similarity]]
- [[Curse of Dimensionality]]
- [[Embedding and Retrieval]]
- [[Contrastive Representation Learning]]
- [[triplet-loss]]
- [[infonce-loss]]
- [[simclr]]
- [[moco]]
- [[Papers Explained 90 - E5]]
- [[Papers Explained 100 - CLIP]]
