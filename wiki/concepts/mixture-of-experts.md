# Mixture of Experts

**Type**: concept  
**Tags**: #concept

## Overview

Mixture of Experts (MoE) is a sparse architectural paradigm designed to dramatically scale model capacity (number of parameters) without a proportional increase in computational cost (FLOPs). Rather than passing inputs through a single dense layer, an MoE layer contains multiple specialized "expert" neural networks (typically Feed-Forward Networks) and a trainable "gating" (router) network. The gating network dynamically routes each input token to only one or a few selected experts, enabling conditional computation where only a fraction of the total model parameters are activated per token.

## Appearances

- [[How to Train Really Large Models on Many GPUs?]] — *How to Train Really Large Models on Many GPUs?* (Sep 25, 2021): Compiles sparsely gated MoE layers, load-balancing losses, GShard, Switch Transformer, and Expert Choice (EC) routing mathematical foundations.
- [[Inkling]] — 975B/41B-active multimodal MoE (256 routed + 2 shared experts, 6 active, sigmoid router, aux-loss-free load balancing) following the DeepSeek-V3 recipe.

## Notes

*   **Sparsely-Gated MoE and Noisy Gating**:
    Originally formulated by Shazeer et al. (2017), a sparsely gated MoE layer contains $n$ expert networks $\{E_i\}_{i=1}^n$ and a gating network $G(x)$. To maintain routing sparsity and encourage exploration, **Noisy Top-k Gating** adds Gaussian noise to the logits before keeping only the top $k$ values and zeroing out the rest:
    
    $$\begin{aligned}
    G(x) &= \text{softmax}(\text{topk}(H(x), k)) \\
    H^{(i)}(x) &= (x W_g)^{(i)} + \epsilon \cdot \text{softplus}((x W_{\text{noise}})^{(i)}) \quad \text{where } \epsilon \sim \mathcal{N}(0, 1) \\
    \text{topk}^{(i)}(v, k) &= \begin{cases} v^{(i)} & \text{if } v^{(i)} \text{ is in the top } k \text{ elements of } v \\ -\infty & \text{otherwise} \end{cases}
    \end{aligned}$$
*   **The Load Balancing Problem & Auxiliary Losses**:
    A core challenge in MoE training is the self-reinforcing gating bias: the router network tends to favor a few highly trained "expert" nodes, routing almost all traffic to them. This leaves the remaining experts under-trained and causes severe computational bottlenecks (where the favored experts exceed memory and compute capacities). To prevent this, an **Auxiliary Importance Loss** based on the batchwise average coefficient of variation (CV) is added to the training objective:
    $$L_{\text{aux}} = w_{\text{aux}} \cdot \text{CV}\left(\sum_{x \in X} G(x)\right)^2$$
*   **GShard (Top-2 Gating with Sharding)**:
    Developed by Google (Lepikhin et al. 2020), **GShard** shards the MoE layers across multiple devices, while copying other standard layers. GShard implements:
    -   **Top-2 Gating with Random Routing**: Routes each token to its best-scoring expert; the second expert is selected with a probability proportional to its score to add stochastic exploration.
    -   **Expert Capacity Limits**: Caps the number of tokens routed to a single expert. If an expert hits its capacity limit, extra tokens overflow and are dropped (output is set to a zero vector).
    -   **Local Group Dispatching**: Partitioning tokens into local groups to enforce capacity limits at the group level.
*   **Switch Transformer (Top-1 Routing)**:
    Developed by Fedus et al. (2021), **Switch Transformer** scales models to trillions of parameters by simplifying routing to a **Top-1 routing** pattern (each token is sent to exactly one expert). This minimizes routing computation and reduces communication overhead. Switch Transformer stabilizes training via:
    -   **Selective Precision**: Executing routing logits in high FP32 precision, but casting outputs back to FP16 to keep fast execution.
    -   **Expert-Specific Dropout**: Increasing the dropout rate within sparse expert layers (e.g. 0.4) while keeping standard dropout in dense layers (0.1) to prevent overfitting during downstream fine-tuning.
    
    Switch Transformer's auxiliary load balance loss distributes tokens more uniformly using the cross-entropy of the fraction of tokens $f_i$ routed to expert $i$ and the mean routing probability $p_i$ over the batch:
    $$L_{\text{aux}} = w_{\text{aux}} \sum_{i=1}^n f_i \cdot p_i$$
    Since $f_i$ is not differentiable (top-1 is discrete), $p_i$ is used as its differentiable surrogate.

*   **Expert Capacity**:
    Each expert has a fixed **capacity** $C$ defining the maximum number of tokens it can process per batch. If more tokens are routed to an expert than $C$, the excess tokens are **dropped** (their contribution to that layer is zeroed). Capacity is typically expressed as a **capacity factor** $\lambda > 1$:
    $$C = \lambda \times \frac{\text{batch tokens}}{\text{number of experts}}$$
    A capacity factor of 1.0 means perfect balance (no slack); 1.25–1.5 provides headroom for natural imbalance. Dropped tokens are a key inefficiency in token-choice routing (GShard, Switch).
    
    See [[How to Train Really Large Models on Many GPUs?]] fig-13 for the Switch Transformer sparse FFN routing diagram, and fig-14 for its sharding strategies.

*   **Expert Choice (EC) Routing**:
    Developed by Zhou et al. (2022), **Expert Choice Routing** reverses the standard routing assignment. Instead of having tokens choose experts (which causes load imbalance and dropped tokens), each expert independently selects its top-$k$ tokens from the batch based on token-to-expert affinity scores $S = \text{softmax}(X \cdot W_g)$:
    $$G, I = \text{top-k}(S^\top, k) \quad P = \text{one-hot}(I)$$
    This mathematically guarantees perfect load balancing and fixed expert capacities. However, EC requires future token visibility, making it incompatible with autoregressive sequence generation at inference time.

*   **MoE Scaling Properties**:
    The key scaling advantage of MoE is that model capacity (parameters) can grow much faster than compute cost (FLOPs). For a dense model with $d$ hidden size FFN, replacing it with $n$ experts of the same size gives:
    - **Parameters**: $n \times$ the dense FFN parameters (e.g. 64 experts → 64× more parameters)
    - **FLOPs per token**: same as the dense model (only top-$k$ experts are active per token)
    - **Communication**: $O(n)$ routing decisions + expert dispatch across devices
    
    This is the fundamental MoE trade-off: massive capacity gains at the cost of routing overhead and load-balancing complexity.

*   **Routing Method Comparison**:

    | Method | Router | Load Balance | Drops Tokens | AR-Compatible |
    |---|---|---|---|---|
    | Noisy Top-k (Shazeer 2017) | Token → Expert | Soft (CV loss) | Yes | Yes |
    | GShard | Token → Top-2 Expert | Soft (aux loss) | Yes | Yes |
    | Switch Transformer | Token → Top-1 Expert | Soft (aux loss) | Yes | Yes |
    | Expert Choice (Zhou 2022) | Expert → Top-k Tokens | Hard (exact) | No | **No** |

    See [[How to Train Really Large Models on Many GPUs?]] fig-10 for the sparsely-gated MoE layer, fig-11 for expert scaling perplexity results, and fig-12 for GShard's group-level top-2 gating pseudocode.

## Related

- [[Pipeline Parallelism]]
- [[Tensor Parallelism]]
- [[GPipe]]
- [[DeepSpeed]]
- [[How to Train Really Large Models on Many GPUs?]]
