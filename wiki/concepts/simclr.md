# SimCLR

**Type**: concept  
**Tags**: #concept

## Overview

SimCLR (Simple Framework for Contrastive Learning of Visual Representations) is an unsupervised visual representation learning pipeline. It maximizes agreement between differently augmented views (distortions) of the same image anchor in the latent space using a Normalized Temperature-scaled Cross Entropy (NT-Xent) loss, operating on a low-dimensional projection head. It established data augmentation and MLP projection heads as critical components of state-of-the-art self-supervised vision models.

## Appearances

- [[Contrastive Representation Learning]] — *Contrastive Representation Learning* (May 31, 2021): Discusses SimCLR's parallel augmentation design, the critical role of projection heads, and the NT-Xent training objective.
- [[Papers Explained 200 - SimCLR]] — Detailed breakdown of the original SimCLR paper and performance benchmarks on ImageNet.
- [[Grokking Self-Supervised (Representation) Learning: How It Works in Computer Vision and Why]] — Intuitive derivation of NT-Xent from log-softmax, augmentation ablation diagram, and practical pre-training workflow.

## Notes

*   **Four Core Components**:
    1.  **Stochastic Data Augmentation Module**: Generates two correlated views ($\tilde{\mathbf{x}}_i, \tilde{\mathbf{x}}_j$) of an image anchor via stochastic transforms (random cropping, color jittering, Gaussian blur).
    2.  **Base Encoder**: A neural network $f(\cdot)$ (typically ResNet-50) that extracts representation vectors $\mathbf{h}_i = f(\tilde{\mathbf{x}}_i)$.
    3.  **Projection Head**: A small MLP $g(\cdot)$ with one hidden layer and a ReLU non-linearity that maps $\mathbf{h}$ to a low-dimensional space $\mathbf{z} = g(\mathbf{h}) = \mathbf{W}^{(2)}\sigma(\mathbf{W}^{(1)}\mathbf{h})$. Contrastive loss is computed on $\mathbf{z}$ rather than $\mathbf{h}$ to prevent loss of semantic information (like color and orientation).
    4.  **Contrastive Loss Function**: NT-Xent (Normalized Temperature-scaled Cross Entropy) loss, a symmetric InfoNCE variant computed over a batch:
        $$\mathcal{L}_{\text{SimCLR}}^{(i,j)} = - \log \frac{\exp(\text{sim}(\mathbf{z}_i, \mathbf{z}_j) / \tau)}{\sum_{k=1}^{2N} \mathbb{1}_{[k \neq i]} \exp(\text{sim}(\mathbf{z}_i, \mathbf{z}_k) / \tau)}$$

*   **SimCLR v1 vs. SimCLR v2**:
    Chen et al. (2020) refined the framework in SimCLR v2 to improve semi-supervised learning performance. The key changes are summarized below:

    | Feature | SimCLR v1 | SimCLR v2 |
    | :--- | :--- | :--- |
    | **Base Encoder** | Standard ResNet-50 | Deeper/wider ResNets (ResNet-152 3x with Selective Kernels) |
    | **Projection Head** | 2-layer MLP ($g(\mathbf{h}) = \mathbf{W}^{(2)}\text{ReLU}(\mathbf{W}^{(1)}\mathbf{h})$) | 3-layer MLP ($g(\mathbf{h}) = \mathbf{W}^{(3)}\text{ReLU}(\mathbf{W}^{(2)}\text{ReLU}(\mathbf{W}^{(1)}\mathbf{h}))$) |
    | **Fine-tuning Setup** | Linear classifier trained on top of frozen encoder | Fine-tuned from the middle layer of the projection head (1st or 2nd layer) |
    | **Distillation** | Not incorporated | Active self-distillation using unlabeled/labeled data onto smaller student ResNet-50s |

*   **Gradient Flow & Projection Head Dynamics**:
    Why compute loss on $\mathbf{z}$ but use $\mathbf{h}$ for downstream tasks?
    During training, the NT-Xent objective forces the projection head $g(\mathbf{h})$ to discard features that vary under data augmentation (such as local pixel colors, lighting textures, and high-frequency noise) in order to classify the augmented views as identical. 
    If we evaluate downstream performance directly on $\mathbf{z}$, the model fails on tasks that require fine-grained details (like semantic segmentation or color-sensitive classification). 
    By introducing the non-linear projection head $g(\cdot)$, the contractive objective's discarding force is concentrated entirely within the projection head parameters. The representation space $\mathbf{h} = f(\mathbf{x})$ directly preceding the projection head is protected, preserving crucial downstream-relevant features (color, object parts, textures) while learning rotation and crop-invariant spatial layouts.

## PyTorch Reference Implementation

Below is a complete, modular PyTorch implementation of the SimCLR visual pretraining forward loop and augmentations:

```python
import torch
import torch.nn as nn
from torchvision import transforms

class ContrastiveAugmentation:
    """
    Applies SimCLR's stochastic double-view augmentation.
    """
    def __init__(self, size=224):
        self.transform = transforms.Compose([
            transforms.RandomResizedCrop(size=size),
            transforms.RandomHorizontalFlip(),
            transforms.RandomApply([
                transforms.ColorJitter(0.8, 0.8, 0.8, 0.2)
            ], p=0.8),
            transforms.RandomGrayscale(p=0.2),
            transforms.GaussianBlur(kernel_size=int(0.1 * size) | 1, sigma=(0.1, 2.0)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])

    def __call__(self, x):
        # Returns two distinct stochastic views of the same anchor image x
        return self.transform(x), self.transform(x)


class SimCLRModel(nn.Module):
    """
    SimCLR architecture containing a base ResNet encoder 
    and a non-linear projection head.
    """
    def __init__(self, base_encoder, projection_dim=128):
        super(SimCLRModel, self).__init__()
        # 1. Base Encoder: Remove ResNet's final FC layer
        self.encoder = base_encoder
        self.encoder.fc = nn.Identity()
        
        # Determine ResNet representation dimension (typically 2048 for ResNet-50)
        repr_dim = 2048 
        
        # 2. Projection Head: 2-layer MLP with ReLU activation
        self.projector = nn.Sequential(
            nn.Linear(repr_dim, repr_dim),
            nn.ReLU(),
            nn.Linear(repr_dim, projection_dim)
        )

    def forward(self, x):
        # Extract representation vector h
        h = self.encoder(x)
        # Map to low-dimensional projection space z
        z = self.projector(h)
        return h, z
```

*   **Scale Dependency**: SimCLR relies heavily on large batch sizes (e.g. 4096) to provide a sufficient number of negative samples (yielding 8190 negatives per pair). Performance degrades severely when the batch size is reduced, as gradients become noisy and easy to optimize.

## Related

- [[Contrastive Learning]]
- [[Contrastive Representation Learning]]
- [[infonce-loss]]
- [[moco]]
- [[Papers Explained 200 - SimCLR]]
