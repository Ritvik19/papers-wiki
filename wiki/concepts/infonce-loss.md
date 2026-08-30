# InfoNCE Loss

**Type**: concept  
**Tags**: #concept

## Overview

InfoNCE (Information Noise Contrastive Estimation) is a multi-class categorical cross-entropy loss function used in self-supervised representation learning. It trains models to correctly identify a single target positive sample from a set of negative noise samples, maximizing the mutual information between different views or contexts of the same underlying data point. It is the core mathematical driver behind state-of-the-art visual, text, and multimodal retrievers.

## Appearances

- [[Contrastive Representation Learning]] — *Contrastive Representation Learning* (May 31, 2021): Explains InfoNCE's derivation from Noise Contrastive Estimation (NCE), its density ratio estimation properties, and its role as a fundamental objective in modern models (CPC, SimCLR, CLIP, MoCo).

## Notes

*   **Mathematical Formulation**: Given a query embedding $\mathbf{q}$, a matching positive key embedding $\mathbf{k}^+$, and a set of $M-1$ negative key embeddings $\{\mathbf{k}_i^-\}_{i=1}^{M-1}$, the InfoNCE loss with temperature parameter $\tau$ is defined as:
    $$\mathcal{L}_\text{InfoNCE} = - \log \frac{\exp(\mathbf{q} \cdot \mathbf{k}^+ / \tau)}{\exp(\mathbf{q} \cdot \mathbf{k}^+ / \tau) + \sum_{i=1}^{M-1} \exp(\mathbf{q} \cdot \mathbf{k}_i^- / \tau)}$$
    This is mathematically equivalent to a multi-class categorical cross-entropy loss where the model attempts to classify the single correct positive key among a pool of $M$ candidates.

*   **Mutual Information Lower Bound Derivation**:
    InfoNCE was formulated by van den Oord et al. (2018) as a variational lower bound on the mutual information $I(\mathbf{X}; \mathbf{Y})$ between two random variables.
    Let $\mathbf{x} \sim p(\mathbf{x})$ be a query and let $d = \{\mathbf{y}_1, \dots, \mathbf{y}_M\}$ be a set containing one positive sample $\mathbf{y}^+ \sim p(\mathbf{y} \mid \mathbf{x})$ at index $j$, and $M-1$ negative noise samples $\mathbf{y}_i^- \sim p(\mathbf{y})$ drawn from the marginal distribution.
    The probability that the positive sample is at index $j$ is given by:
    $$p(j \mid d, \mathbf{x}) = \frac{p(\mathbf{x}, \mathbf{y}_j) \prod_{l \neq j} p(\mathbf{y}_l)}{\sum_{i=1}^M p(\mathbf{x}, \mathbf{y}_i) \prod_{l \neq i} p(\mathbf{y}_l)} = \frac{\frac{p(\mathbf{x}, \mathbf{y}_j)}{p(\mathbf{x})p(\mathbf{y}_j)}}{\sum_{i=1}^M \frac{p(\mathbf{x}, \mathbf{y}_i)}{p(\mathbf{x})p(\mathbf{y}_i)}} = \frac{f(\mathbf{x}, \mathbf{y}_j)}{\sum_{i=1}^M f(\mathbf{x}, \mathbf{y}_i)}$$
    where the scoring function $f(\mathbf{x}, \mathbf{y}) \propto \frac{p(\mathbf{x} \mid \mathbf{y})}{p(\mathbf{x})}$ approximates the density ratio.
    When a model optimizes $\mathcal{L}_\text{InfoNCE}$ to classify index $j$ correctly, the cross-entropy loss is:
    $$\mathcal{L}_\text{InfoNCE} = - \mathbb{E}_{d} \left[ \log \frac{f(\mathbf{x}, \mathbf{y}^+)}{\sum_{i=1}^M f(\mathbf{x}, \mathbf{y}_i)} \right]$$
    By expanding the expectation, we establish:
    $$\mathcal{L}_\text{InfoNCE} = \mathbb{E}_{d} \left[ \log \left( 1 + \frac{\sum_{i \neq j} f(\mathbf{x}, \mathbf{y}_i)}{f(\mathbf{x}, \mathbf{y}^+)} \right) \right] \approx \mathbb{E} \left[ \log \left( 1 + M \frac{p(\mathbf{y})}{p(\mathbf{y} \mid \mathbf{x})} \right) \right]$$
    Approximating the expectation yields:
    $$\mathcal{L}_\text{InfoNCE} \approx \mathbb{E}_{p(\mathbf{x}, \mathbf{y})} \left[ \log \frac{p(\mathbf{y})}{p(\mathbf{y} \mid \mathbf{x})} \right] + \log(M) = -I(\mathbf{X}; \mathbf{Y}) + \log(M)$$
    Rearranging terms gives the fundamental inequality:
    $$I(\mathbf{X}; \mathbf{Y}) \ge \log(M) - \mathcal{L}_\text{InfoNCE}$$
    This shows that **minimizing InfoNCE maximizes the lower bound on the mutual information** between representations.

*   **Role & Impact of Temperature $\tau$**:
    The temperature hyperparameter $\tau$ controls the scale of the logits (cosine similarities). It has two major effects:
    1.  **Gradient Hardness Scaling**: As $\tau \to 0$, the softmax distribution becomes sharper, concentrating gradients almost entirely on the "hardest" negative samples (those closest to the anchor). This forces the network to establish very tight, well-separated cluster boundaries.
    2.  **Entropy Balancing**: If $\tau$ is too small, the loss is highly sensitive to outliers, noise, or false negatives, causing training to collapse or diverge. If $\tau$ is too large, the loss acts as a uniform penalty over all negatives, failing to resolve fine-grained similarities. Empirical studies show visual models perform best with $\tau \in [0.05, 0.2]$.

## PyTorch Reference Implementation

Below is the standard symmetric NT-Xent (Normalized Temperature Cross-Entropy) loss, which computes the dual-view InfoNCE loss symmetrically across a batch (used in SimCLR and CLIP):

```python
import torch
import torch.nn as nn

class SymmetricNTXentLoss(nn.Module):
    """
    Symmetric NT-Xent loss for two correlated views of a batch.
    Computes InfoNCE symmetrically: View A -> View B and View B -> View A.
    """
    def __init__(self, temperature=0.07):
        super(SymmetricNTXentLoss, self).__init__()
        self.temperature = temperature
        self.cross_entropy = nn.CrossEntropyLoss()

    def forward(self, z_a, z_b):
        # z_a and z_b shape: [BatchSize, EmbeddingDim]
        batch_size = z_a.shape[0]
        
        # 1. Normalize embeddings to unit sphere for cosine similarity
        z_a = torch.nn.functional.normalize(z_a, dim=1)
        z_b = torch.nn.functional.normalize(z_b, dim=1)
        
        # 2. Concat representations to form joint batch
        # representations shape: [2 * BatchSize, EmbeddingDim]
        representations = torch.cat([z_a, z_b], dim=0)
        
        # 3. Pairwise cosine similarity matrix
        # similarity shape: [2 * BatchSize, 2 * BatchSize]
        similarity_matrix = torch.matmul(representations, representations.t()) / self.temperature
        
        # 4. Generate diagonal masks to exclude self-similarities
        # We need to extract positive pairs: (i, i+B) and (i+B, i)
        diag_a = torch.diagonal(similarity_matrix, offset=batch_size)
        diag_b = torch.diagonal(similarity_matrix, offset=-batch_size)
        positives = torch.cat([diag_a, diag_b]).view(2 * batch_size, 1)
        
        # 5. Extract all candidate negatives by masking out the self-similarities
        mask = ~torch.eye(2 * batch_size, dtype=torch.bool, device=z_a.device)
        negatives = similarity_matrix[mask].view(2 * batch_size, -1)
        
        # 6. Formulate cross entropy logits: positive similarity at index 0
        # logits shape: [2 * BatchSize, 2 * BatchSize - 1]
        logits = torch.cat([positives, negatives], dim=1)
        
        # Target: index 0 (the positive key is always at the front)
        targets = torch.zeros(2 * batch_size, dtype=torch.long, device=z_a.device)
        
        return self.cross_entropy(logits, targets)
```

*   **Origins**: CPC (van den Oord et al. 2018) established the loss for predictive sequences. It has since become the standard objective for visual pretraining (SimCLR, MoCo), text models (SimCSE, Contriever), and joint vision-text representations (CLIP).

## Related

- [[Contrastive Learning]]
- [[Contrastive Representation Learning]]
- [[triplet-loss]]
- [[simclr]]
- [[moco]]
- [[Papers Explained 100 - CLIP]]
