# On-Policy Self-Distillation

#concept

On-Policy Self-Distillation, or OPSD, uses the student itself as a teacher under privileged context, then trains the normal student policy on its own on-policy rollouts.

In [[On SFT RL and On-Policy Distillation]], OPSD is treated as algorithmically close to [[On-Policy Distillation]], but riskier because answer-conditioned teacher signals can create dense, biased, concentrated gradients. That concentration can require KL clipping or related defenses.

## Appearances

- [[Introducing Composer 2.5]] — Cursor's Composer 2.5 uses OPSD for targeted credit assignment: a hint is injected at a problematic turn, the policy is re-scored under the modified context (no new decode), and the log-probability shift defines the teacher signal.
- [[Sasha Rush Explains Targeted On-Policy Self-Distillation]] — Sasha Rush gives a detailed verbal walkthrough of OPSD, explaining the "no new rollout" property and the trade-off of only getting local corrections.

## Related

- [[Sasha Rush Explains Targeted On-Policy Self-Distillation]]
- [[On SFT RL and On-Policy Distillation]]
- [[On-Policy Distillation]]
- [[KL Regularization]]
- [[Targeted Textual Feedback]]
- [[Reinforcement Learning Topic]]
- [[Model Distillation]]
- [[Papers Explained 249 - DINO]]
- [[Papers Explained 320 - SigLIP 2]]
