# Papers Explained 594: Teacher-Routed Exploration via Forward KL (TREK)

**Source**: `raw/2026-08-13_Papers-Explained-594--Teacher-Routed-Exploration-via-Forward-KL--TREK--da20a690b2ad.html`  
**Paper**: https://arxiv.org/abs/2607.05339  
**Ingested**: 2026-08-23  
**Tags**: #summary

## Summary

**Teacher-Routed Exploration via Forward KL (TREK)** addresses a fundamental exploration failure in reinforcement learning with verifiable rewards (RLVR) and on-policy distillation: when a student policy has near-zero probability on the correct reasoning path, standard on-policy sampling never generates it, causing RL updates to stall. Standard teacher guidance (such as SFT or standard distillation) often induces distribution mismatch or forces the student into paths it cannot complete. TREK introduces an intelligent **Prompt Routing** mechanism combined with **Forward KL** guidance: when a student fails to reach a correct solution, prompts are dynamically routed to a stronger teacher to supply high-probability proposal trajectories, while on-policy exploration refines the student policy.

![Papers Explained 594: TREK overview banner](../assets/papers-explained-594-teacher-routed-exploration-via-forward-kl-trek/fig-1.png)

### Method and Reachability Mechanism

TREK formally defines the *reachability* of a problem: whether the student policy $\pi_\theta$ can generate at least one valid trajectory with non-zero probability.
1. **Prompt Routing**: Prompts are categorized into Student-Reachable and Student-Unreachable sets. Unreachable prompts trigger teacher intervention.
2. **Proposal Learning (Forward KL)**: The student is guided toward teacher proposals using Forward KL divergence $\mathbb{D}_{KL}(p_T \parallel p_S)$, which exhibits mode-covering behavior that broadens the student's reachability envelope without collapsing into premature local minima.
3. **On-Policy Refinement**: Once reachability is restored, on-policy policy gradients (or reverse KL distillation) refine the student policy toward mode-seeking precision.

![TREK Routing and Proposal Learning](../assets/papers-explained-594-teacher-routed-exploration-via-forward-kl-trek/fig-2.png)

## Key Claims

- Unreachable reasoning tasks cause standard on-policy RLVR and reverse-KL distillation to plateau due to lack of positive reward signals.
- Forward KL guidance on teacher-routed proposals expands the support of the student policy, restoring reachability.
- Combining teacher-routed forward KL exploration with on-policy refinement significantly accelerates convergence on difficult math and coding benchmarks.

## Figures

| Figure | Caption | Page |
|--------|---------|------|
| ![fig-1](../assets/papers-explained-594-teacher-routed-exploration-via-forward-kl-trek/fig-1.png) | Papers Explained 594 banner. | Overview |
| ![fig-2](../assets/papers-explained-594-teacher-routed-exploration-via-forward-kl-trek/fig-2.png) | TREK prompt routing and exploration mechanism. | Method |
| ![fig-3](../assets/papers-explained-594-teacher-routed-exploration-via-forward-kl-trek/fig-3.png) | Reachability bottleneck in standard on-policy RL. | Analysis |
| ![fig-4](../assets/papers-explained-594-teacher-routed-exploration-via-forward-kl-trek/fig-4.png) | Forward KL proposal learning vs on-policy refinement. | Method |
| ![fig-5](../assets/papers-explained-594-teacher-routed-exploration-via-forward-kl-trek/fig-5.png) | Benchmark accuracy progression on complex reasoning datasets. | Results |
| ![fig-6](../assets/papers-explained-594-teacher-routed-exploration-via-forward-kl-trek/fig-6.png) | Sample efficiency comparison: TREK vs RLVR vs GKD. | Efficiency |
| ![fig-7](../assets/papers-explained-594-teacher-routed-exploration-via-forward-kl-trek/fig-7.png) | Exploration coverage heatmaps across problem difficulty tiers. | Analysis |
| ![fig-8](../assets/papers-explained-594-teacher-routed-exploration-via-forward-kl-trek/fig-8.png) | Routing threshold and teacher query budget ablation. | Ablations |
| ![fig-9](../assets/papers-explained-594-teacher-routed-exploration-via-forward-kl-trek/fig-9.png) | Forward KL vs Reverse KL during proposal phase. | Ablations |
| ![fig-10](../assets/papers-explained-594-teacher-routed-exploration-via-forward-kl-trek/fig-10.png) | Performance on MATH, AIME, and Codeforces problems. | Evaluation |
| ![fig-11](../assets/papers-explained-594-teacher-routed-exploration-via-forward-kl-trek/fig-11.png) | Training stability curves and policy entropy. | Training |
| ![fig-12](../assets/papers-explained-594-teacher-routed-exploration-via-forward-kl-trek/fig-12.png) | Reachability recovery rate across training iterations. | Results |
| ![fig-13](../assets/papers-explained-594-teacher-routed-exploration-via-forward-kl-trek/fig-13.png) | Qualitative trajectory case study of teacher routing. | Qualitative |

## Entities

- [[TREK]] — Teacher-Routed Exploration via Forward KL framework.
- [[On-Policy Distillation]] — distillation with on-policy trajectories.
- [[Reasoning Models]] — multi-step reasoning capabilities.
- [[Reinforcement Learning Topic]] — RL exploration techniques.

## Questions & Gaps

- Managing teacher query budgets when scaling to millions of synthetic reasoning problems.
- Dynamic adaptation of the routing threshold during training as the student becomes progressively stronger.

## Related

- [[On-Policy Distillation]] — core distillation framework.
- [[Papers Explained 591: Generalized Knowledge Distillation]] — Forward vs. Reverse KL foundations.
- [[Papers Explained 592: Self-Distilled Reasoner]] — self-distillation reasoning.
- [[Exploration Strategies in Deep Reinforcement Learning]] — exploration methods.
