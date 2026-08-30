# Curriculum for Reinforcement Learning

**Source**: https://lilianweng.github.io/posts/2020-01-29-curriculum-rl/
**Author**: Lilian Weng
**Published**: 2020-01-29
**Updated**: 2020-02-04

---

It sounds like an impossible task if we want to teach integral or derivative to a 3-year-old who does not even know basic arithmetics. That's why education is important, as it provides a systematic way to break down complex knowledge and a nice curriculum for teaching concepts from simple to hard. A curriculum makes learning difficult things easier and approachable for us humans. But, how about machine learning models? Can we train our models more efficiently with a curriculum? Can we design a curriculum to speed up learning?

Back in 1993, Jeffrey Elman has proposed the idea of training neural networks with a curriculum. His early work on learning simple language grammar demonstrated the importance of such a strategy: starting with a restricted set of simple data and gradually increasing the complexity of training samples; otherwise the model was not able to learn at all.

Compared to training without a curriculum, we would expect the adoption of the curriculum to expedite the speed of convergence and may or may not improve the final model performance. To design an efficient and effective curriculum is not easy. Keep in mind that, a bad curriculum may even hamper learning.

Five types of curriculum for reinforcement learning are covered:

1. Task-Specific Curriculum
2. Teacher-Guided Curriculum
3. Curriculum through Self-Play
4. Automatic Goal Generation
5. Skill-Based Curriculum
6. Curriculum through Distillation

---

## Task-Specific Curriculum

Bengio, et al. (2009) provided a good overview of curriculum learning in the old days. The paper presented two ideas:
- Cleaner Examples may yield better generalization faster.
- Introducing gradually more difficult examples speeds up online training.

A good question: What could be the general principles that make some curriculum strategies work better than others? The hypothesis is that it would be beneficial to make learning focus on "interesting" examples that are neither too hard nor too easy.

One idea to quantify difficulty is to use minimal loss with respect to another pretrained model (Weinshall et al., 2018).

Zaremba & Sutskever (2014) trained LSTM to predict Python program outputs. Three strategies:
- **Naive curriculum**: increase complexity parameter step by step.
- **Mix curriculum**: sample parameters from full range.
- **Combined**: naive + mix. Always outperforms the other two.

Procedural Content Generation (PCG) is used in game environments (GVGAI, CoinRun, Procgen). OpenAI's **POET** (Wang et al., 2019) uses evolutionary algorithms and PCG.

OpenAI's Rubik's cube paper (2019) used **Automatic Domain Randomization (ADR)** to grow a distribution of environments with increasing complexity.

---

## Teacher-Guided Curriculum

**Automatic Curriculum Learning** (Graves et al., 2017) models a N-task curriculum as an N-armed bandit problem.

Two learning signals:
- **Loss-driven progress**: loss change before/after gradient update.
- **Complexity-driven progress**: KL divergence between posterior and prior over network weights.

**Teacher-Student Curriculum Learning (TSCL)** (Matiisen et al., 2017): A student RL agent works on actual tasks while a teacher agent is a policy for selecting tasks. The teacher operates on a POMDP:
- Unobserved state: full state of student model.
- Observed: list of scores for N tasks.
- Action: pick a subtask.
- Reward: score delta across all tasks.

Uniformly sampling from all tasks is a surprisingly strong baseline.

**ALP-GMM** (Portelas et al., 2019): Continuous teacher-student framework. Absolute Learning Progress (ALP) is measured as |r - r_old|. A Gaussian Mixture Model is trained over the task parameter space to fit the ALP distribution. ε-greedy sampling.

---

## Curriculum through Self-Play

**Asymmetric Self-Play** (Sukhbaatar et al., 2017): Two agents Alice and Bob.
- Alice challenges Bob to achieve the same state.
- Bob attempts to complete it as fast as possible.
- Alice's reward: R_A = γ·max(0, t_B - t_A)
- Bob's reward: R_B = -γ·t_B
- If B fails: t_B = t_max - t_A

Only works in reversible or resettable environments. Alice guarantees tasks are solvable because she demonstrates them first.

---

## Automatic Goal Generation

**Generative Goal Learning / Goal GAN** (Florensa et al., 2018): Uses a GAN to generate goals of intermediate difficulty (GOID).
- GOID_i := {g : R_min ≤ R^g(π_i) ≤ R_max}
- Generator G(z): produces a new goal from GOID.
- Discriminator D(g): tells whether goal is from GOID.
- Uses LSGAN (Least-Squared GAN) for stability.

**Racaniere & Lampinen et al. (2019)**: Three components: Solver/Policy π, Judge/Discriminator D, Setter/Generator G(z,f). Three objectives for generator:
1. **Goal validity**: achievable by expert policy.
2. **Goal feasibility**: appropriate difficulty for current policy.
3. **Goal coverage**: maximize entropy for diverse goals.

---

## Skill-Based Curriculum

**CARML** (Jabri et al., 2019): Curricula for Unsupervised Meta-RL.
- Frames unsupervised interaction as variational EM.
- E-step: organize trajectories into latent skill space q_φ.
- M-step: meta-RL training with skills as task distribution.
- Reward: r_z(s) = (λ-1)·log q_φ(s|z) + log q_φ(z|s) + C

**Hausman et al. (2018)**: Learn a task-conditioned policy via a latent skill space. Policy = mixture of K sub-policies, trained with SAC.

---

## Curriculum through Distillation

**Progressive Neural Networks** (Rusu et al., 2016): Curriculum through progressively stacked network columns.
- First task trains a single column to convergence (θ^(1)).
- New task: add a new column, freeze θ^(1).
- Layer i of column k depends on layer i-1 of all previous columns:
  h^(k)_i = f(W^(k)_i · h^(k)_{i-1} + Σ_{j<k} U_i^(k:j) · h^(j)_{i-1})

Tested on Atari games: better than top-layer fine-tuning, similar to full network fine-tuning.

**Mix-and-Match** (Andreas et al., 2017): Trains sub-policies ("skills") separately, then combines them for complex tasks via a modular policy. Three-step training process using "skill seeding" from a teacher policy. Achieves near-Oracle performance on StarCraft micromanagement tasks.

---

## Key References

- Elman (1993): "The importance of starting small"
- Bengio et al. (2009): Curriculum Learning overview
- Weinshall et al. (2018): Transfer learning for curriculum difficulty
- Zaremba & Sutskever (2014): LSTM on Python programs
- Graves et al. (2017): Automatic Curriculum Learning
- Matiisen et al. (2017): Teacher-Student Curriculum Learning (TSCL)
- Portelas et al. (2019): ALP-GMM
- Sukhbaatar et al. (2017): Asymmetric Self-Play
- Florensa et al. (2018): Goal GAN / Generative Goal Learning
- Racaniere & Lampinen et al. (2019): Setter-Judge-Solver
- Jabri et al. (2019): CARML
- Rusu et al. (2016): Progressive Neural Networks
- Andreas et al. (2017): Mix-and-Match modular policies
- Wang et al. (2019): POET
- OpenAI et al. (2019): Rubik's cube / ADR
