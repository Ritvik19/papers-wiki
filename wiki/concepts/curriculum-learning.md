# Curriculum Learning

**Type**: concept  
**Tags**: #concept

## Overview

Curriculum learning presents training examples in a meaningful order—from easier to harder—rather than i.i.d. sampling, often improving convergence and final performance on difficult tasks. Originally proposed by Jeffrey Elman (1993) for language models, formalized for deep learning by Bengio et al. (2009). Applied to RL, curriculum design becomes particularly important: without a curriculum, some tasks are impossible to learn directly; with a bad curriculum, learning can be actively harmed.

Key paradigms in RL curriculum design:
- **Task-specific curriculum**: human-designed difficulty ordering; combined (naive + random mix) strategies beat pure sequential orderings.
- **Teacher-guided curriculum**: a teacher RL agent selects tasks to maximize student learning progress (see [[Teacher-Student Curriculum Learning]], [[ALP-GMM]]).
- **Self-play curriculum**: agents challenge each other, guaranteeing solvability (see [[Asymmetric Self-Play]]).
- **Automatic goal generation**: GANs or normalizing flows propose goals of intermediate difficulty (see [[Goal GAN]]).
- **Skill-based curriculum**: unsupervised skill discovery defines the task distribution (see [[CARML]]).
- **Curriculum through distillation**: progressively stacked model expansions prevent forgetting (see [[Progressive Neural Networks]]).

## Appearances

- [[Deep Learning]] — Section 8.7.3 (optimization strategies and meta-algorithms) discusses curriculum and continuation strategies.
- [[Curriculum for Reinforcement Learning]] — Lilian Weng's 2020 survey of six curriculum paradigms for RL.

## Notes

- A uniformly random task selection baseline is surprisingly competitive against active teacher-guided curriculum methods (Matiisen et al. 2017; Graves et al. 2017).
- Mixing easy tasks throughout training (combined strategy) consistently outperforms pure sequential curricula (Zaremba & Sutskever 2014).

## Related

- [[Stochastic Gradient Descent]]
- [[Hyperparameter Tuning]]
- [[Deep Learning]]
- [[Curriculum for Reinforcement Learning]]
- [[Teacher-Student Curriculum Learning]]
- [[ALP-GMM]]
- [[Asymmetric Self-Play]]
- [[Goal GAN]]
- [[Automatic Domain Randomization]]
- [[Progressive Neural Networks]]
- [[CARML]]
- [[Reinforcement Learning Topic]]
- [[Transfer Learning]]
