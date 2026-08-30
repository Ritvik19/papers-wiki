# Curriculum for Reinforcement Learning

**Source**: `raw/curriculum-for-reinforcement-learning/full-article.html` · `raw/curriculum-for-reinforcement-learning/full-article.md`  
**URL**: https://lilianweng.github.io/posts/2020-01-29-curriculum-rl/  
**Author**: [[Lilian Weng]]  
**Ingested**: 2026-05-22  
**Tags**: #summary

## Overview

In this comprehensive survey, [[Lilian Weng]] traces the history and modern developments of **Curriculum Learning** in the context of **Reinforcement Learning** (RL). Just as human pedagogy relies on structured curricula to guide students from foundational concepts to advanced topics, RL systems benefit immensely from phased training schedules. Training a policy on a complex target task from scratch can be extraordinarily slow, or even mathematically impossible due to sparse rewards. A well-constructed curriculum accelerates convergence, whereas a poorly designed curriculum can introduce suboptimal local minima or actively derail training.

The survey categorizes curriculum generation in RL into six core paradigms:

```
                  ======================================
                  Curriculum for Reinforcement Learning
                  ======================================
                                    |
     -----------------------------------------------------------------
     |               |               |               |               |
Task-Specific Teacher-Guided Self-Play   Goal Gen    Skill-Based Distillation
  (ADR/PCG)    (TSCL/ALP-GMM) (Asymmetric)  (Goal GAN)   (CARML)     (PNN)
```

---

## Master Paradigm Matrix

The six paradigms differ across representation complexity, environmental interactions, and transfer mechanisms:

| Paradigm | Key Mechanisms / Algorithms | State/Task Space | Solvability Guarantee | Primary Limitation |
|---|---|---|---|---|
| **1. Task-Specific** | Automatic Domain Randomization ([[Automatic Domain Randomization]]), PCG (POET) | Hand-crafted or parametric dimensions | None (Parameters can scale to impossible boundaries) | Requires human domain knowledge to parameterize |
| **2. Teacher-Guided** | Bandit selection (Graves 2017), POMDP controllers ([[Teacher-Student Curriculum Learning]]), GMMs ([[ALP-GMM]]) | Discrete tasks or continuous parameter vectors | None (Teacher can pick impossible settings) | Susceptible to teacher-estimation noise |
| **3. Self-Play** | Alice/Bob mutual challenges ([[Asymmetric Self-Play]]) | Continuous environment states | **Yes** (Alice demonstrates the task beforehand) | Requires reversible or resettable environment dynamics |
| **4. Goal Generation** | GOID search ([[Goal GAN]]), Setter-Judge-Solver networks | Continuous target goal coordinates | None (GAN may propose out-of-bounds or invalid goals) | GAN optimization is notoriously unstable |
| **5. Skill-Based** | Variational EM trajectory mapping ([[CARML]]) | Latent behavioral embeddings | None (Discovered skills might not map to target task) | Discovered skills can be redundant or task-irrelevant |
| **6. Distillation** | Column stacking ([[Progressive Neural Networks]]), modular seeding (Mix-and-Match) | Multi-task model architecture | None (Transfer is conditional on task similarity) | Parameter size scales linearly with number of tasks (for PNN) |

---

## Detailed Breakdown of the Six Paradigms

### 1. Task-Specific Curriculum
Human-designed heuristics map out the training trajectory. Difficulty is defined either by:
- **Filtering cleaner data** or applying simpler training samples first (Bengio et al., 2009).
- **Environmental procedural content generation (PCG)** to dynamically scale layouts or physics.
- **Distribution boundaries (ADR)**: OpenAI's [[Automatic Domain Randomization]] widens uniformity bounds ($\theta \sim \mathcal{U}(L, U)$) when policy performance exceeds a threshold ($C^{high} \ge 80\%$) and contracts them when performance falls ($C^{low} \le 50\%$).
- **Key Finding**: Zaremba & Sutskever (2014) demonstrated that a **combined curriculum** (randomly mixing easy examples throughout training) consistently outperforms a naive sequential curriculum because it prevents the policy from catastrophically forgetting simpler controls.

### 2. Teacher-Guided Curriculum
Task selection is treated as an active scheduling problem where a "Teacher" policy chooses the tasks for a "Student" policy.
- **Multi-armed Bandit Teacher** (Graves et al., 2017): Uses bandit algorithms to optimize the student's *loss-driven progress* or *complexity-driven progress* (measured via KL divergence of weight posteriors).
- **Discrete POMDP Teacher** ([[Teacher-Student Curriculum Learning]]): Models student learning as a POMDP where the reward is the aggregate student improvement across all N tasks ($\sum \Delta \text{score}$). Uses Thompson sampling for task allocation.
- **Continuous Parameter Teacher** ([[ALP-GMM]]): Uses a Gaussian Mixture Model fitted over Absolute Learning Progress (ALP = $|r - r_{old}|$) computed from a nearest-neighbor buffer. Samples high-progress components to focus on the student's learning frontier.
- **Key Finding**: Uniformly sampling from all tasks at random is a surprisingly strong baseline that competitive active schedulers often struggle to outperform.

### 3. Self-Play Curriculum
A two-agent game automatically drives the curriculum without manual task specification.
- **Asymmetric Self-Play** ([[Asymmetric Self-Play]]): Alice performs actions for $t_A$ steps to set a target state $s_t$, and Bob must return the environment to $s_0$ and reach $s_t$ in $t_B$ steps.
- **Rewards**: Bob is penalized for time ($R_B = -\gamma t_B$). Alice is rewarded for challenging Bob but penalized for excessive setup time ($R_A = \gamma \max(0, t_B - t_A)$).
- **Core Benefit**: Alice's physical navigation of the environment provides a constructive **solvability guarantee** for every goal she proposes.

### 4. Automatic Goal Generation
Generative models propose coordinates of intermediate difficulty.
- **Goal GAN** ([[Goal GAN]]): Trains a Generator to output goals in the Goals of Intermediate Difficulty (GOID) set:
  $$\text{GOID} := \{g : R_{min} \le R^g(\pi) \le R_{max}\}$$
  The LSGAN objective keeps training stable.
- **Setter-Judge-Solver**: A three-part expansion that conditions goal generation on a target feasibility metric $f \in [0, 1]$ and current environment state $s$. The Setter is optimized using three loss objectives: *validity* (achievability), *feasibility* (matching $f$), and *coverage* (maximizing goal entropy using reversible flows).

### 5. Skill-Based Curriculum
The environment is explored in an unsupervised fashion to discover options, which then form the training curriculum.
- **CARML** ([[CARML]]): Frames skill discovery as a Variational Expectation-Maximization (EM) loop over latent skills $z$.
  - **E-Step**: organizies trajectories into a latent skill representation space using a variational posterior state classifier $q_\phi(z | s)$.
  - **M-Step**: trains the policy $\pi$ using Meta-RL, where tasks are sampled from the discovered skill space. Intrinsic rewards balance task-specific exploration with skill matching:
    $$r_z(s) = (\lambda - 1)\log q_\phi(s | z) + \log q_\phi(z | s) + C$$

### 6. Curriculum through Distillation
Curriculum is built directly into model architecture expansion to prevent forgetting when migrating to new tasks.
- **Progressive Neural Networks** ([[Progressive Neural Networks]]): Spawns a frozen network column for each task. New tasks get a new active column, with lateral connection layers drawing on the features of prior frozen columns:
  $$h^{(k)}_i = f\left( W^{(k)}_i h^{(k)}_{i-1} + \sum_{j < k} U^{(k:j)}_i h^{(j)}_{i-1} \right)$$
- **Mix-and-Match**: Progressively trains modular sub-policies ("skills") independently, then merges them into a single modular multi-task agent using teacher-student policy distillation (skill seeding).

---

## Related

- [[Exploration Strategies in Deep Reinforcement Learning]] — Sister blog post survey on intrinsic motivation and exploration mechanics; overlaps significantly with self-play and skill discovery.
- [[Curriculum Learning]] — Foundational parent concept page.
- [[Teacher-Student Curriculum Learning]] — POMDP discrete task selection.
- [[ALP-GMM]] — Continuous teacher-student curriculum.
- [[Asymmetric Self-Play]] — Alice/Bob curriculum interaction.
- [[Goal GAN]] — Adversarial goal-space curriculum.
- [[Automatic Domain Randomization]] — OpenAI's boundary-expansion curriculum.
- [[Progressive Neural Networks]] — Multi-task architecture expansion.
- [[CARML]] — Latent skill unsupervised Meta-RL curriculum.
- [[Reinforcement Learning Topic]] — Main parent page.
- [[Meta-Learning]] — Paradigm utilizing CARML and TSCL.
