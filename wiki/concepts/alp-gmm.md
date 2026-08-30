# ALP-GMM

**Type**: concept  
**Tags**: #concept

## Overview

**ALP-GMM** (Absolute Learning Progress – Gaussian Mixture Model; Portelas et al., 2019) is an advanced, automated curriculum generation framework designed for **continuous task parameter spaces**. 

While precursor frameworks like [[Teacher-Student Curriculum Learning]] (TSCL) rely on discrete sets of tasks modeled via multi-armed bandits, real-world robotic control and simulation environments often feature an uncountably infinite parameter space (e.g., continuous variations in gravity, mass, friction, obstacle sizes, or goal coordinates). ALP-GMM addresses this continuous challenge by dynamically fitting a Gaussian Mixture Model (GMM) over the task parameter space, weighted by a local metric called **Absolute Learning Progress (ALP)**.

---

## The Core Metric: Absolute Learning Progress (ALP)

In discrete task spaces, learning progress can be measured chronologically by tracking the change in performance on the *same task* at two different times. In a continuous task space, however, the agent rarely encounters the exact same task twice.

To solve this, ALP-GMM calculates learning progress by comparing the reward of a newly executed task parameter $p$ with the reward of the *nearest historically visited* task parameter $p_{old}$:

$$ALP_p = |r - r_{old}|$$

Where:
- $p \in \mathbb{R}^D$ is the vector representing the continuous task parameters.
- $r$ is the episodic reward obtained when training the student on task parameter $p$.
- $p_{old}$ is the task parameter in the historical database $D$ closest to $p$ in terms of Euclidean distance:
  $$p_{old} = \text{argmin}_{p' \in D} \|p - p'\|_2$$
- $r_{old}$ is the episodic reward historically obtained on task $p_{old}$.

Taking the **absolute value** $|r - r_{old}|$ ensures that the teacher is highly attracted to both:
1. **Positive progress (learning)**: where $r \gg r_{old}$ (the student is starting to master a previously failed area).
2. **Negative progress (forgetting)**: where $r \ll r_{old}$ (the student is regressing, indicating a need for target reinforcement).

Tasks with $|r - r_{old}| \approx 0$ are ignored because they are either already fully mastered ($r \approx r_{old} \approx \text{max\_reward}$) or still completely impossible ($r \approx r_{old} \approx \text{min\_reward}$).

---

## The ALP-GMM Algorithm

ALP-GMM operates as a periodic fitting and sampling loop:

### 1. The Database and Periodicity
A database $D$ stores history pairs of $(p_i, \text{ALP}_{p_i})$. After every $N_{step}$ episodes, the Gaussian Mixture Model is refitted to the database.

### 2. Task Selection (Action Space)
To select the next continuous task parameter $p_{next}$ for the student, ALP-GMM uses an $\epsilon$-greedy strategy:
- With probability $\epsilon$ (exploration): sample $p_{next}$ uniformly at random from the entire task parameter space. This ensures the teacher continuously searches for new "learning frontiers."
- With probability $1 - \epsilon$ (exploitation):
  1. Fit a Gaussian Mixture Model $M$ over the parameters $\{p_i\}$ in the database $D$, where each data point's contribution is weighted by its absolute learning progress $\text{ALP}_{p_i}$.
  2. Sample a Gaussian component $C_k$ from $M$ proportionally to its aggregated ALP weight.
  3. Sample the parameter vector $p_{next} \sim \mathcal{N}(\mu_k, \Sigma_k)$ from the chosen component.

### 3. Updating the Model
The student policy executes task $p_{next}$, receives reward $r_{next}$, computes $\text{ALP}_{p_{next}}$ using the nearest-neighbor lookup, and appends the tuple to the database.

---

## Detailed Algorithm Pseudocode

```python
import numpy as np
from sklearn.mixture import GaussianMixture

class ALPGMMTeacher:
    def __init__(self, bounds, epsilon=0.2, fit_interval=250, n_components=10):
        self.bounds = bounds             # e.g., [(0.1, 2.0), (0.0, 1.0)]
        self.epsilon = epsilon
        self.fit_interval = fit_interval
        self.n_components = n_components
        self.database = []               # list of dicts: {"p": array, "r": float, "alp": float}
        self.gmm = None
        
    def select_task(self):
        # 1. Exploration: Uniform sampling
        if np.random.rand() < self.epsilon or len(self.database) < self.fit_interval:
            return np.random.uniform([b[0] for b in self.bounds], [b[1] for b in self.bounds])
            
        # 2. Exploitation: Sample from GMM
        # Pick a random point in GMM space according to component weights
        weights = self.gmm.weights_
        component_idx = np.random.choice(len(weights), p=weights)
        mean = self.gmm.means_[component_idx]
        cov = self.gmm.covariances_[component_idx]
        task = np.random.multivariate_normal(mean, cov)
        return np.clip(task, [b[0] for b in self.bounds], [b[1] for b in self.bounds])

    def register_run(self, task_p, reward):
        # Find nearest neighbor in database
        if len(self.database) == 0:
            alp = 0.0
        else:
            distances = [np.linalg.norm(task_p - entry["p"]) for entry in self.database]
            nearest_idx = np.argmin(distances)
            r_old = self.database[nearest_idx]["r"]
            alp = abs(reward - r_old)
            
        self.database.append({"p": task_p, "r": reward, "alp": alp})
        
        # Periodic fitting
        if len(self.database) % self.fit_interval == 0:
            self._fit_gmm()
            
    def _fit_gmm(self):
        X = np.array([entry["p"] for entry in self.database])
        alps = np.array([entry["alp"] for entry in self.database])
        
        # Normalize weights to sum to 1
        weights = alps / (np.sum(alps) + 1e-8)
        
        # Fit Weighted GMM
        self.gmm = GaussianMixture(n_components=self.n_components, covariance_type='full')
        # Scikit-learn allows sample weights during fit
        self.gmm.fit(X, sample_weight=weights)
```

---

## Comparison: Continuous Task Curriculum Methods

| Metric / Aspect | ALP-GMM | Goal GAN (Florensa et al.) | ADR (OpenAI Rubik's) |
|---|---|---|---|
| **Underlying Math** | Gaussian Mixture Models + KNN | Generative Adversarial Networks | Parameter Boundary Tracking |
| **Progress Representation** | Multi-modal density estimates | Generative sample distribution | Uniform distribution boundary |
| **Computational Overhead** | Low (fast scikit-learn GMM fit) | High (training GAN discriminator/generator) | Low (simple boundary adjustments) |
| **Task Parameter Bounds** | Fixed bounds over parameter dimensions | Implicitly bounded or free-form | Dynamically expanding boundaries |
| **Multi-modal hot-spots?**| Yes (fits multiple Gaussians) | Yes (adversarial modeling) | No (unimodal uniform box) |

---

## Key Design Insights

1. **Euclidean Metric Caveat**: ALP-GMM uses Euclidean distance in the parameter space to find $p_{old}$. If different dimensions of the task parameter space have widely different scales (e.g., mass in kilograms vs. friction coefficient), standardizing the dimensions or defining a custom distance metric is essential.
2. **Mitigating "Curse of Dimensionality"**: Nearest-neighbor lookups scale poorly as the parameter dimension $D$ increases. ALP-GMM is typically deployed in parameter spaces where $D \le 10$.
3. **The Multimodal Advantage**: If an environment has two disjoint zones of intermediate difficulty (e.g. extremely light objects with high friction vs. heavy objects with low friction), the GMM can naturally place two distinct Gaussian components over these regions, sampling from both. Unimodal boundary frameworks like ADR cannot handle this.

## Appearances

- [[Curriculum for Reinforcement Learning]] — Section on Teacher-Guided Curriculum; introduced as the primary paradigm for automated training in continuous parameter spaces.

## Related

- [[Teacher-Student Curriculum Learning]] — Foundational discrete teacher-student paradigm.
- [[Curriculum Learning]] — Main concept page.
- [[Goal GAN]] — Adversarial continuous goal proposal.
- [[Automatic Domain Randomization]] — OpenAI's continuous boundary tracker.
- [[Reinforcement Learning Topic]] — Main parent page.
