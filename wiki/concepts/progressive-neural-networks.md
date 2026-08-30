# Progressive Neural Networks

**Type**: concept  
**Tags**: #concept

## Overview

**Progressive Neural Networks** (PNN; Rusu et al., 2016) is a neural network architecture designed for **continual learning** and **multi-task curriculum transfer**. PNNs solve two of the most persistent bottlenecks in deep learning:

1. **Catastrophic Forgetting**: The tendency of standard neural networks to overwrite previously learned knowledge when trained on a new task.
2. **Negative Transfer**: A phenomenon where features learned in prior tasks conflict with or actively degrade performance on a newly introduced task.

PNNs achieve this by **freezing previously trained task parameters** and sequentially **stacking new neural network columns** for each new task. Information is shared across tasks using lateral connections between the layers of different columns.

---

## Architectural Mechanics

When learning a sequence of tasks, PNNs construct a column of layers for each task. The parameters of existing columns are frozen to prevent catastrophic forgetting, while new lateral connections are introduced to transfer prior knowledge.

```
Task 1 (Frozen)       Task 2 (Active)
  [ h^(1)_2 ]  ------>   [ h^(2)_2 ]
       ^                      ^  \
       |                     /    \
  [ h^(1)_1 ]  ------------->    [ h^(2)_1 ]
       ^                      ^
       |                      |
    Input 1                Input 2
```

### Mathematical Layer Formulation

Let $L$ be the number of layers in each network column, and let $k$ be the index of the current column (task $k$). 

- **First Task ($k=1$)**: The network consists of a single standard column. The activation at layer $i$ is standard feed-forward:
  $$h^{(1)}_i = f(W^{(1)}_i h^{(1)}_{i-1})$$
  Where $W^{(1)}_i$ is the weight matrix of column 1 at layer $i$, and $f$ is an activation function (e.g. ReLU).
  
- **Subsequent Tasks ($k > 1$)**: For a new column $k$, layer $i$ receives inputs from layer $i-1$ of its own column *and* from layer $i-1$ of all previous columns $j < k$:
  $$h^{(k)}_i = f\left( W^{(k)}_i h^{(k)}_{i-1} + \sum_{j < k} U^{(k:j)}_i h^{(j)}_{i-1} \right)$$
  Where:
  - $W^{(k)}_i$ is the active weight matrix representing the internal feedforward connections of column $k$.
  - $U^{(k:j)}_i$ is the **lateral connection weight matrix** that projects features from layer $i-1$ of the frozen column $j$ to layer $i$ of the active column $k$.
  - $h^{(j)}_{i-1}$ are the frozen, cached activations of prior columns from the same input batch.

---

## Transfer Mechanics: How Knowledge Flows

When training on task $k$:
- Only the parameters $\{W^{(k)}_i\}_{i=1}^L$ and the lateral parameters $\{U^{(k:j)}_i\}_{i=1, j<k}^L$ are updated.
- Parameters of columns $1$ through $k-1$ remain strictly frozen:
  $$\nabla_{\theta^{(j)}} \mathcal{L}_k = 0 \quad (\forall j < k)$$
- **Lateral Projection (Adapter Blocks)**: Because different columns may have different hidden dimensionalities, $U^{(k:j)}_i$ acts as a dimensionality adapter (similar to projection layers in Transformer architectures).
- **Evaluating Transfer Quality**: The active column can choose to rely heavily on prior columns by allocating high absolute weights to $U$, or it can choose to ignore them entirely if the transfer is unhelpful (avoiding negative transfer) by setting $U \approx 0$.

---

## PNN vs. Standard Continual Learning Paradigms

| Aspect / Strategy | Progressive Neural Networks (PNN) | Fine-Tuning with L2 / EWC Regularization | Multitask Learning (Joint Training) |
|---|---|---|---|
| **Catastrophic Forgetting** | **Zero** (Prior weights are frozen) | Mitigated but present (prior weights shift under regularization constraints) | None (Trained simultaneously on all data) |
| **Parameter Scaling** | **Linear** growth: $O(K \times L)$ parameters for $K$ tasks | **Constant** parameter size | **Constant** parameter size |
| **Computational Complexity** | Scales linearly with tasks during forward pass | Constant during training/inference | Constant |
| **Data Requirements** | Sequentially available | Sequentially available | Requires all task datasets simultaneously |
| **Transfer Efficiency** | High (direct lateral routing) | High (shared parameter space) | High (shared representation layers) |

---

## Empirical Findings and Limitations

In empirical evaluations on reinforcement learning benchmarks (such as transferring policies across different Atari games or standard physics tasks like Cartpole/Pendulum):

1. **Beating Fine-Tuning**: PNNs consistently outperform standard fine-tuning (which typically suffers from catastrophic forgetting) and L2 regularization baselines.
2. **Transfer Efficiency**: PNNs converge faster than training a single network from scratch, proving that the lateral connections successfully reuse learned representations.
3. **The Parameter Scaling Trap**: The primary drawback of PNNs is their linear growth in parameters as the number of tasks scales. If $K=50$ tasks are trained, the network is $50\times$ larger than a standard model. This limits their applicability in long-lifetime agentic environments.
4. ** lateral Connection Bias**: Lilian Weng notes that high lateral connection weights do *not* always mean successful transfer. Sometimes, early layers of prior tasks can lock the active column into suboptimal local minima, introducing architectural biases.

## Appearances

- [[Curriculum for Reinforcement Learning]] — Covered in the section on Curriculum through Distillation.

## Related

- [[Curriculum Learning]] — Foundational parent concept.
- [[Curriculum for Reinforcement Learning]] — Parent survey page.
- [[Mix-and-Match]] — Modular transfer alternative that does not grow linearly.
- [[Transfer Learning]] — Core topic of feature transfer.
- [[Catastrophic Forgetting]] — Foundational continual learning bottleneck.
- [[Reinforcement Learning Topic]] — Parent topic.
