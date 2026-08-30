# Influence Functions in DL

**Type**: concept  
**Tags**: #concept

## Overview

Influence Functions (Koh & Liang, ICML 2017) are a classical technique from robust statistics repurposed to explain deep neural network predictions by tracing model output back to specific training instances. They calculate how a model's parameters and test predictions would change if a given training instance was infinitesimally upweighted or removed from the training set. This closed-form linear approximation bypasses the massive computational cost of actually retraining the model (leave-one-out retraining), making it a powerful diagnostic tool for identifying mislabeled training examples, detecting data poisoning, and understanding model generalization.

## Appearances

- [[2024-02-05-human-data-quality]] — Utilized as a training dynamics diagnostic tool to analyze how individual human-labeled training samples influence parameter updates and downstream test loss.

## Mathematical Formulation

Let $D = \{z_1, \dots, z_n\}$ be the training set where each point $z_i = (x_i, y_i) \in \mathcal{X} \times \mathcal{Y}$. Let $L(z, \theta)$ be the loss function, and let $\hat{\theta}$ be the empirical risk minimizer:

$$\hat{\theta} = \arg\min_{\theta \in \Theta} \frac{1}{n} \sum_{i=1}^{n} L(z_i, \theta)$$

Assuming the empirical risk is twice continuously differentiable and strictly convex, we define the Hessian matrix $H_{\hat{\theta}}$ of the loss over all training samples as:

$$H_{\hat{\theta}} = \frac{1}{n} \sum_{i=1}^{n} \nabla^2_{\theta} L(z_i, \hat{\theta})$$

### 1. Influence on Parameters
Suppose we perturb the training distribution by infinitesimally upweighting a training point $z$ by a small weight $\epsilon$. The new parameters $\hat{\theta}_{\epsilon, z}$ are given by:

$$\hat{\theta}_{\epsilon, z} = \arg\min_{\theta \in \Theta} \left[ \frac{1}{n} \sum_{i=1}^{n} L(z_i, \theta) + \epsilon L(z, \theta) \right]$$

The **influence of upweighting $z$ on the parameters** is the derivative of $\hat{\theta}_{\epsilon, z}$ with respect to $\epsilon$, evaluated at $\epsilon = 0$:

$$\mathcal{I}_{\text{up,params}}(z) = \left. \frac{d\hat{\theta}_{\epsilon, z}}{d\epsilon} \right|_{\epsilon=0} = -H_{\hat{\theta}}^{-1} \nabla_{\theta} L(z, \hat{\theta})$$

### 2. Influence on Test Loss
To calculate how upweighting a training point $z$ affects the loss on a specific test point $z_{\text{test}}$, we apply the chain rule:

$$\mathcal{I}_{\text{up,loss}}(z, z_{\text{test}}) = \left. \frac{d L(z_{\text{test}}, \hat{\theta}_{\epsilon, z})}{d\epsilon} \right|_{\epsilon=0} = \nabla_{\theta} L(z_{\text{test}}, \hat{\theta})^T \left. \frac{d\hat{\theta}_{\epsilon, z}}{d\epsilon} \right|_{\epsilon=0}$$

Substituting the parameter influence formula yields:

$$\mathcal{I}_{\text{up,loss}}(z, z_{\text{test}}) = -\nabla_{\theta} L(z_{\text{test}}, \hat{\theta})^T H_{\hat{\theta}}^{-1} \nabla_{\theta} L(z, \hat{\theta})$$

A highly negative $\mathcal{I}_{\text{up,loss}}(z, z_{\text{test}})$ indicates that the training point $z$ **helps** the model make a better prediction on $z_{\text{test}}$. Conversely, a positive value indicates $z$ is **harmful** to the test point's performance.

## Computational Challenges & Scaling (IHVP)

Directly calculating the inverse Hessian $H_{\hat{\theta}}^{-1}$ is computationally intractable for deep networks because the Hessian size scales quadratically with the number of parameters $P$ (e.g., $10^9 \times 10^9$ for a 1B parameter model).

To bypass this bottleneck, practitioners never construct the Hessian explicitly. Instead, they compute the **Inverse Hessian-Vector Product (IHVP)** directly:

$$\mathbf{v} = H_{\hat{\theta}}^{-1} \nabla_{\theta} L(z_{\text{test}}, \hat{\theta})$$

This is solved efficiently using iterative numerical optimization methods:
1. **Conjugate Gradient (CG) Descent**: Solves the linear system $H_{\hat{\theta}} \mathbf{v} = \nabla_{\theta} L(z_{\text{test}}, \hat{\theta})$.
2. **Linear-time Stochastic Second-Order Algorithm (LiSSA)**: Approximates $H_{\hat{\theta}}^{-1}$ as a Taylor series expansion and stochastic vector updates, reducing the time complexity to $O(n P)$.

## Applications to Human Data Quality

* **Mislabeled Data Detection**: Mislabeled samples (noisy labels) present a severe contradiction to the surrounding clean data manifold. The model works hard to fit them, resulting in massive gradient updates. These outliers typically exhibit high-magnitude positive influence values on many related test samples, signaling that their removal will universally improve generalization.
* **Data Debugging**: If a model makes an egregious prediction error on a test case, calculating the influence function identifies which specific training samples were most responsible for pulling the parameters toward that failure mode.

## Related

- [[Data Maps]]
- [[Area Under the Margin]]
- [[2024-02-05-human-data-quality]]
