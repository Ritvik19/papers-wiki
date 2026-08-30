# Teacher-Student Curriculum Learning

**Type**: concept  
**Tags**: #concept

## Overview

Teacher-Student Curriculum Learning (TSCL; Matiisen et al., 2017) formalizes the problem of automatic curriculum design as a **reinforcement learning problem over the task space**. A *teacher* RL agent selects which sub-task a *student* RL agent should train on at each step. The teacher's goal is to maximize the student's total learning progress, choosing tasks that are either at the frontier of the student's current capability or at risk of being forgotten.

TSCL builds directly on the Automatic Curriculum Learning (ACL) framework of Graves et al. (2017), which first cast N-task curriculum selection as an N-armed bandit problem. TSCL extends this into a fully formalized teacher-student setup with an explicit POMDP model.

---

## Precursor: Automatic Curriculum Learning (Graves et al., 2017)

Graves et al. model a curriculum over N tasks as an **N-armed bandit** where the reward signal encodes learning progress. Two types of progress signals are considered:

**1. Loss-driven progress**  
Measures the change in the task loss before and after a gradient update:

> progress_t = L(x_{t-1}, θ_{t-1}) − L(x_t, θ_t)

The greatest task-loss decrease is equivalent to the fastest learning. This signal tracks convergence speed.

**2. Complexity-driven progress**  
Measures the KL divergence between the posterior and prior distribution over network weights after seeing task data:

> progress_t = KL(q(θ | D_t) || p(θ))

Inspired by the Minimum Description Length (MDL) principle: "increasing model complexity by a certain amount is only worthwhile if it compresses the data by a greater amount." Model complexity is expected to increase most when the model generalises well to training examples.

---

## The TSCL POMDP Formulation

TSCL frames teacher training as solving a **partially observable MDP** (POMDP):

| POMDP component | TSCL mapping |
|---|---|
| Unobserved state s_t | Full internal state of the student model (weights, optimizer state) |
| Observation o_t | Vector of N per-task scores x_t^(i), one per subtask |
| Action a_t | Select subtask i ∈ {1, …, N} |
| Reward r_t | Score delta: r_t = Σ_i (x_t^(i) − x_{t-1}^(i)) |
| Objective | Maximize Σ_t r_t = maximize Σ_i x_T^(i) at end of episode |

The reward is therefore equivalent to maximising the sum of scores on *all tasks* at the end of the episode. This encourages the teacher to pick tasks that help the student improve globally, not just locally.

### Teacher Objectives

The teacher wants to select tasks for the student that:

1. **Maximise learning progress** — pick tasks where the student is improving fastest.
2. **Prevent forgetting** — pick tasks that the student has learned but is at risk of forgetting (score regressing).

These two objectives correspond to selecting tasks where `Δscore` is currently high (positive or negative).

### Task Selection Strategy

Because task scores are noisy and non-stationary, task selection borrows from the **non-stationary multi-armed bandit** literature:

- **ε-greedy**: with probability ε pick a random task; otherwise pick the task with highest recent Δscore.
- **Thompson sampling**: maintain a posterior over each task's expected progress, sample from posteriors to select a task.

Both strategies balance exploration (trying underexplored tasks) with exploitation (focusing on currently productive tasks).

---

## Algorithm Sketch

```
initialise student policy π_θ, teacher policy π_φ
initialise score history x^(i) for each task i
for each training step:
    teacher observes x_t = [x_t^(1), ..., x_t^(N)]
    teacher selects task i ~ π_φ(i | x_t)           # ε-greedy or Thompson
    student trains on task i for K steps
    update x_{t+1}^(i) with new task score
    teacher reward: r_t = Σ_j (x_{t+1}^(j) - x_t^(j))
    update teacher π_φ using r_t
```

---

## Key Empirical Finding

Both Graves et al. (2017) and Matiisen et al. (2017) independently found that **uniformly sampling from all N tasks at random** is a surprisingly strong baseline for teacher-guided curriculum methods. This result has important implications:

- The benefit of active task selection is context-dependent and may not always justify added complexity.
- When it *does* help, it typically helps in settings where task difficulty is very heterogeneous or where forgetting is a major risk.

---

## Comparison: TSCL vs. Related Approaches

| | TSCL | Graves ACL | ALP-GMM | Asymmetric Self-Play |
|---|---|---|---|---|
| **Task space** | Discrete N tasks | Discrete N tasks | Continuous parameters | Continuous states |
| **Teacher type** | RL agent / bandit | Bandit | GMM model | Alice agent (also in env) |
| **Progress signal** | Σ Δscore across all tasks | Loss-driven or complexity-driven | ALP = \|r − r_old\| in param space | Alice's reward grows with Bob's difficulty |
| **Teacher trains on env?** | No | No | No | Yes (Alice plays same env) |
| **Guarantees solvability?** | No | No | No | Yes (Alice demonstrates task) |

---

## Notes

- TSCL's teacher operating in task-selection space is structurally similar to Neural Architecture Search (NAS): NAS uses an RL agent to propose architectures, TSCL uses an RL agent to propose tasks (Lilian Weng's observation).
- [[ALP-GMM]] extends TSCL to continuous task parameter spaces by replacing the discrete bandit with a GMM over the ALP distribution.
- Unlike [[Asymmetric Self-Play]], the TSCL teacher never interacts with the environment itself—it operates purely in the abstract task-selection space.
- TSCL is agnostic to the student's learning algorithm; the student can use any RL or SL method.

## Appearances

- [[Curriculum for Reinforcement Learning]] — core framework; presented alongside Graves et al. 2017 and ALP-GMM as the teacher-guided curriculum family.

## Related

- [[ALP-GMM]] — continuous task-space extension.
- [[Asymmetric Self-Play]] — self-play alternative where "teacher" also acts in the environment.
- [[Goal GAN]] — generative model alternative for goal-space curriculum.
- [[Curriculum Learning]] — parent concept.
- [[Curriculum for Reinforcement Learning]] — source survey.
- [[Multi-Armed Bandits]] — task selection borrows exploration strategies from bandit literature.
- [[Exploration-Exploitation Tradeoff]] — core tradeoff in task selection.
- [[Neural Architecture Search]] — noted structural analogy to TSCL.
- [[Reinforcement Learning Topic]] — parent topic.
