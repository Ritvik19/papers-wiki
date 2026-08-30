# MoCo

**Type**: concept  
**Tags**: #concept

## Overview

MoCo (Momentum Contrast) is a self-supervised visual representation learning framework that treats contrastive learning as a dynamic dictionary lookup. The dictionary is structured as a large, first-in-first-out (FIFO) queue of encoded keys, decoupling the dictionary size (number of negative samples) from the training mini-batch size. To prevent representational drift and keep keys in the queue consistent, MoCo updates its key encoder using an exponential moving average (momentum) of the query encoder.

## Appearances

- [[Contrastive Representation Learning]] — *Contrastive Representation Learning* (May 31, 2021): Synthesizes MoCo's dynamic dictionary lookup structure, its queue-based implementation, and the momentum update equations.

## Notes

*   **Dictionary Lookup Abstraction**: MoCo frames contrastive learning as a dynamic dictionary lookup. An input query $\mathbf{q} = f_q(\mathbf{x}_q)$ is matched against one positive key $\mathbf{k}^+ = f_k(\mathbf{x}_k)$ (a different augmented view of the same image) and a dynamic queue of negative keys. The objective is to correctly identify $\mathbf{k}^+$ from the queue of negatives.
*   **Decoupling Batch Size via FIFO Queue**: In standard in-batch contrastive learning (e.g., SimCLR), the number of negative samples is strictly tied to the mini-batch size. MoCo decouples these variables by maintaining an external, persistent first-in-first-out (FIFO) queue of negative key embeddings (e.g. 65,536 keys). When a new mini-batch of keys is encoded, it is added to the queue, and the oldest keys are dequeued. This allows training with huge negative pools using standard batch sizes (e.g., 256), greatly reducing GPU memory consumption.
*   **Momentum Encoder Update**: Because the queue is massive, backpropagation through all negative keys is computationally impossible. Thus, only the query encoder $\theta_q$ is updated via gradient descent. To ensure that the keys stored in the queue remain consistent representations of a stable latent space, the key encoder $\theta_k$ is updated as a slowly moving average of $\theta_q$ (momentum update):
    $$\theta_k \leftarrow m \theta_k + (1-m) \theta_q$$
    where $m \in [0.99, 0.9999]$ is the momentum coefficient. This momentum update prevents representation drift and collapse, stabilizing the dictionary learning.

*   **Progression of MoCo Versions**:
    MoCo has evolved continuously to incorporate state-of-the-art vision components:

    | Feature | MoCo v1 (He et al. 2019) | MoCo v2 (Chen et al. 2020) | MoCo v3 (Chen et al. 2021) |
    | :--- | :--- | :--- | :--- |
    | **Base Encoder** | ResNet-50 | ResNet-50 | Vision Transformer (ViT-S/B/L) |
    | **Projection Head** | 1-layer Linear | 2-layer MLP (SimCLR-style) | 3-layer MLP + Prediction Head |
    | **Data Augmentation** | Random Crop, Flip, Color Jitter | + Gaussian Blur (SimCLR-style) | Vision Transformer augmentations |
    | **Dictionary Size** | 65,536 (Queue) | 65,536 (Queue) | Removed Queue (uses large batch e.g., 4096) |
    | **Training Stability** | Standard BN | Standard BN | Random Patch Projection freeze |

*   **Shuffling Batch Normalization (Cheat Prevention)**:
    In multi-GPU training, standard Batch Normalization (BN) computes mean and variance statistics across samples on the same GPU. 
    Because positive pairs (query and positive key) are passed through the same model in the same batch, the batch normalization operation can "leak" intra-batch information across samples. The network can exploit these batch-wide statistics to easily match queries with keys based purely on batch statistics rather than semantic content, resulting in representation collapse (a phenomenon known as "cheating").
    To resolve this, MoCo implements **Shuffling BN**:
    1.  Before distributing keys to the key encoder GPUs, MoCo shuffles the sample order across the GPUS.
    2.  The key encoder processes the shuffled batch and computes BN statistics.
    3.  After encoding, the key embeddings are shuffled back to their original order to match the queries.
    This ensures that the BN statistics for queries and keys are calculated over entirely different sample subsets, preventing the network from utilizing batch statistics as a shortcut.

## PyTorch Reference Implementation

Below is a PyTorch-style implementation of MoCo's queue management, momentum update, and forward loop:

```python
import torch
import torch.nn as nn

class MoCo(nn.Module):
    """
    Momentum Contrast (MoCo) dynamic queue and momentum encoder implementation.
    """
    def __init__(self, encoder_q, encoder_k, dim=128, K=65536, m=0.999, T=0.07):
        super(MoCo, self).__init__()
        self.K = K  # Dictionary size (queue length)
        self.m = m  # Momentum coefficient
        self.T = T  # Temperature
        
        # Create encoders
        self.encoder_q = encoder_q
        self.encoder_k = encoder_k
        
        # Initialize key encoder weights to match query encoder
        for param_q, param_k in zip(self.encoder_q.parameters(), self.encoder_k.parameters()):
            param_k.data.copy_(param_q.data)
            param_k.requires_grad = False  # Key encoder does not receive gradients
            
        # Create the dynamic queue queue
        self.register_buffer("queue", torch.randn(dim, K))
        self.queue = torch.nn.functional.normalize(self.queue, dim=0)
        self.register_buffer("queue_ptr", torch.zeros(1, dtype=torch.long))

    @torch.no_grad()
    def _momentum_update_key_encoder(self):
        """
        Slowly update key encoder via exponential moving average.
        """
        for param_q, param_k in zip(self.encoder_q.parameters(), self.encoder_k.parameters()):
            param_k.data = param_k.data * self.m + param_q.data * (1.0 - self.m)

    @torch.no_grad()
    def _dequeue_and_enqueue(self, keys):
        """
        Maintains the FIFO queue of negative embeddings.
        """
        batch_size = keys.shape[0]
        ptr = int(self.queue_ptr)
        
        # Ensure batch size fits evenly inside the queue
        assert self.K % batch_size == 0, "Queue size K must be divisible by batch size"
        
        # Replace the oldest keys in the queue with the new keys
        self.queue[:, ptr:ptr + batch_size] = keys.t()
        
        # Move pointer forward (wrap around if it hits the end)
        ptr = (ptr + batch_size) % self.K
        self.queue_ptr[0] = ptr

    def forward(self, im_q, im_k):
        # 1. Compute query features
        q = self.encoder_q(im_q) # [B, D]
        q = torch.nn.functional.normalize(q, dim=1)
        
        # 2. Compute key features (using momentum encoder with no gradients)
        with torch.no_grad():
            self._momentum_update_key_encoder() # Update key encoder weights
            k = self.encoder_k(im_k) # [B, D]
            k = torch.nn.functional.normalize(k, dim=1)
            
        # 3. Compute logits: Positive pairs
        # l_pos shape: [B, 1]
        l_pos = torch.einsum('nc,nc->n', [q, k]).unsqueeze(-1)
        
        # 4. Compute logits: Negative pairs (using the dynamic queue)
        # l_neg shape: [B, K]
        l_neg = torch.matmul(q, self.queue.clone().detach())
        
        # 5. Concatenate positive and negative logits
        # logits shape: [B, 1+K]
        logits = torch.cat([l_pos, l_neg], dim=1)
        logits /= self.T
        
        # Targets: Ground truth is always at index 0 (positive key)
        targets = torch.zeros(logits.shape[0], dtype=torch.long, device=q.device)
        
        # Dequeue oldest keys and enqueue new keys
        self._dequeue_and_enqueue(k)
        
        return logits, targets
```

## Related

- [[Contrastive Learning]]
- [[Contrastive Representation Learning]]
- [[infonce-loss]]
- [[simclr]]
