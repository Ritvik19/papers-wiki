# Triplet Loss

**Type**: concept  
**Tags**: #concept

## Overview

Triplet Loss is a loss function used in deep metric learning where the network is trained to minimize the distance between an anchor and a positive sample (belonging to the same class), while maximizing the distance between the anchor and a negative sample (belonging to a different class) by at least a predefined margin. It is a foundational objective in representation learning, facial recognition, and metric verification tasks.

## Appearances

- [[Contrastive Representation Learning]] — *Contrastive Representation Learning* (May 31, 2021): Synthesizes triplet loss as a precursor to multi-negative contrastive objectives and highlights the critical need for hard negative mining.

## Notes

*   **Mathematical Formulation**: Given an anchor representation $\mathbf{a} = f(\mathbf{x})$, a positive sample representation $\mathbf{p} = f(\mathbf{x}^+)$, and a negative sample representation $\mathbf{n} = f(\mathbf{x}^-)$, triplet loss learns an embedding function $f$ mapping high-dimensional inputs to a unit hypersphere (i.e., $\|\mathbf{z}\|_2 = 1$) by minimizing:
    $$\mathcal{L}_\text{triplet}(\mathbf{a}, \mathbf{p}, \mathbf{n}) = \max\left(0, \|\mathbf{a} - \mathbf{p}\|^2_2 - \|\mathbf{a} - \mathbf{n}\|^2_2 + \alpha\right)$$
    where the margin parameter $\alpha > 0$ defines the minimum offset required between positive and negative pair distances. If the negative is pushed further than the positive plus the margin, the loss becomes zero.
*   **The Negative Mining Spectrum**: Proper sample selection is crucial. Triplet triplets fall into three distinct classes based on the relative distances:
    1.  **Easy Triplets**: $\mathcal{L}_\text{triplet} = 0 \iff \|\mathbf{a} - \mathbf{n}\|^2_2 > \|\mathbf{a} - \mathbf{p}\|^2_2 + \alpha$. The negative is already far away. These triplets produce no gradients and stall optimization if not filtered.
    2.  **Hard Triplets**: $\|\mathbf{a} - \mathbf{n}\|^2_2 < \|\mathbf{a} - \mathbf{p}\|^2_2$. The negative sample is closer to the anchor than the positive sample is. This produces highly active gradients but can lead to bad local minima or training instability if overemphasized early in training.
    3.  **Semi-Hard Triplets**: $\|\mathbf{a} - \mathbf{p}\|^2_2 < \|\mathbf{a} - \mathbf{n}\|^2_2 < \|\mathbf{a} - \mathbf{p}\|^2_2 + \alpha$. The negative sample is further than the positive, but within the margin cone. FaceNet (Schroff et al. 2015) demonstrated that mining semi-hard negatives in online batch construction is the most stable and effective strategy for convergence.
*   **Batch Construction Strategies**:
    *   *Offline Mining*: Compute embeddings for the entire dataset, find hard/semi-hard triplets, and construct batches. This is computationally expensive, requiring periodic re-evaluation.
    *   *Online Mining*: Formulate standard batches, and dynamically select triplets within each batch. Two main techniques:
        *   **Batch All**: Compute loss on all valid active triplets, averaging only over non-zero triplets.
        *   **Batch Hard**: Select the hardest positive and hardest negative for each anchor in the batch.

## PyTorch Reference Implementation

Below is a standard PyTorch implementation of Triplet Loss with online batch-hard mining, showcasing matrix-based distance computation:

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class BatchHardTripletLoss(nn.Module):
    """
    Computes Triplet Loss over a batch by dynamically mining the 
    hardest positive and hardest negative for each anchor.
    """
    def __init__(self, margin=0.3):
        super(BatchHardTripletLoss, self).__init__()
        self.margin = margin

    def forward(self, embeddings, labels):
        # embeddings shape: [BatchSize, EmbeddingDim]
        # labels shape: [BatchSize]
        
        # 1. Compute pairwise Euclidean distance matrix
        # dist_matrix[i, j] = ||e_i - e_j||^2
        dot_product = torch.matmul(embeddings, embeddings.t())
        square_norm = torch.diag(dot_product)
        distances = square_norm.unsqueeze(1) - 2.0 * dot_product + square_norm.unsqueeze(0)
        distances = F.relu(distances) # Ensure numerical stability (no negative values)
        
        # 2. Build masks for positive and negative pairs
        labels_equal = labels.unsqueeze(0) == labels.unsqueeze(1) # [B, B]
        
        # Positive mask: same label, but not the anchor itself
        mask_anchor_positive = labels_equal.clone()
        mask_anchor_positive.fill_diagonal_(False)
        
        # Negative mask: different label
        mask_anchor_negative = ~labels_equal
        
        # 3. Mine hardest positive for each anchor (largest distance)
        # Apply mask by setting negative distance to 0
        anchor_positive_dist = distances * mask_anchor_positive.float()
        hardest_positive_dist, _ = torch.max(anchor_positive_dist, dim=1, keepdim=True)
        
        # 4. Mine hardest negative for each anchor (smallest distance)
        # Apply mask by setting positive/self distances to infinity
        max_dist = torch.max(distances).item()
        anchor_negative_dist = distances + max_dist * labels_equal.float()
        hardest_negative_dist, _ = torch.min(anchor_negative_dist, dim=1, keepdim=True)
        
        # 5. Compute triplet loss margin: max(0, d(a,p) - d(a,n) + margin)
        triplet_loss = hardest_positive_dist - hardest_negative_dist + self.margin
        triplet_loss = F.relu(triplet_loss)
        
        return triplet_loss.mean()
```

*   **Origins & Limits**: While foundational (FaceNet 2015), triplet loss is statistically inefficient: it evaluates combinations of 3 items at a time, ignoring all other batch items. Modern contrastive losses (e.g. InfoNCE) frame learning as multi-class categorization, comparing 1 positive to $N-1$ negatives simultaneously to achieve faster training and tighter representations.

## Related

- [[Contrastive Learning]]
- [[Contrastive Representation Learning]]
- [[infonce-loss]]
