# Papers Explained: Subproblem Curriculum Reinforcement Learning (SCRL)

**Source**: `raw/draft_Papers-Explained--Subproblem-Curriculum-Reinforcement-Learning--SCRL--c1d94c6f3b00.html`  
**Paper**: https://arxiv.org/abs/2605.22074  
**Ingested**: 2026-08-23  
**Tags**: #summary

## Summary

**Subproblem Curriculum Reinforcement Learning (SCRL)** solves the sparse-reward bottleneck in long-horizon reasoning by decomposing monolithic reasoning tasks into an ordered DAG of verifiable subproblems. Rather than assigning rewards only upon full terminal correctness, SCRL introduces **Progress-Aware Subproblem Rewards**: as the agent successfully solves intermediate milestones, intermediate rewards are dispatched along the curriculum graph, guiding the policy step-by-step through complex multi-step deductions.

![Papers Explained SCRL banner](../assets/papers-explained-scrl/fig-1.png)

### Method & Progress-Aware Rewards

- **Subproblem Graph Decomposition**: Complex tasks (e.g., Olympiad proofs, multi-file code bugs) are decomposed into sub-goals with formal entry and exit specifications.
- **Progress-Aware Rewards**: Reward shaping credits valid subproblem completion while discounting repeated or redundant exploratory loops.
- **Curriculum Scheduling**: As the agent masters early subproblems, difficulty thresholds dynamically advance to focus sampling on downstream bottleneck steps.

![SCRL Subproblem Graph and Reward Flow](../assets/papers-explained-scrl/fig-2.png)

## Key Claims

- Subproblem DAG decomposition provides dense, verifiable milestone rewards without requiring human step annotations.
- Drastically improves exploration sample efficiency on long-horizon mathematical proofs and multi-step programming.
- Eliminates reward hacking by enforcing strict verification contracts at each intermediate sub-goal.

## Figures

| Figure | Caption | Page |
|--------|---------|------|
| ![fig-1](../assets/papers-explained-scrl/fig-1.png) | SCRL overview banner. | Overview |
| ![fig-2](../assets/papers-explained-scrl/fig-2.png) | Subproblem DAG decomposition and curriculum scheduling. | Method |
| ![fig-3](../assets/papers-explained-scrl/fig-3.png) | Progress-Aware Subproblem Reward formulation. | Method |
| ![fig-4](../assets/papers-explained-scrl/fig-4.png) | Exploration efficiency comparison: SCRL vs Standard RLVR. | Results |
| ![fig-5](../assets/papers-explained-scrl/fig-5.png) | Benchmark accuracy on OlympiadBench and Codeforces. | Results |
| ![fig-6](../assets/papers-explained-scrl/fig-6.png) | Ablation of subproblem granularity and DAG depth. | Ablations |
| ![fig-7](../assets/papers-explained-scrl/fig-7.png) | Policy entropy and milestone completion rates over training. | Dynamics |
| ![fig-8](../assets/papers-explained-scrl/fig-8.png) | Qualitative proof decomposition example. | Qualitative |
| ![fig-9](../assets/papers-explained-scrl/fig-9.png) | Verification failure recovery analysis. | Analysis |
| ![fig-10](../assets/papers-explained-scrl/fig-10.png) | Cross-domain transfer on complex software bug localization. | Transfer |

## Entities

- [[SCRL]] — Subproblem Curriculum Reinforcement Learning.
- [[Curriculum Learning]] — curriculum progression in RL.
- [[Reasoning Models]] — long-horizon multi-step reasoning.
- [[Reinforcement Learning Topic]] — verifiable milestone rewards.

## Questions & Gaps

- Automated DAG generation reliability for messy, ill-posed natural language problems.
- Computational cost of verifying intermediate milestones in heavy sandbox environments.

## Related

- [[Curriculum Learning]] — core curriculum topic.
- [[Papers Explained: Self-Optimization via Asymmetric RL (SOAR)]] — automated curriculum peer.
- [[Reasoning Models]] — reasoning architectures.
