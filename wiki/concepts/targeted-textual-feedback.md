# Targeted Textual Feedback

**Type**: concept  
**Tags**: #concept

## Overview

Targeted textual feedback is a localized RL training technique used for Composer 2.5: at a specific turn in a long agent rollout where behavior should improve, a short textual hint is inserted into context. The policy with the hint defines a teacher distribution; the policy without the hint is the student. An [[On-Policy Distillation]] KL loss on that turn nudges student token probabilities toward the teacher's, while trajectory-level RL reward still applies over the full rollout.

## Appearances

- [[Introducing Composer 2.5]] — primary source; motivates the method as credit assignment for hundred-thousand-token rollouts where sparse final rewards under-specify which decision failed (e.g. a single invalid tool call).
- [[Sasha Rush Explains Targeted On-Policy Self-Distillation]] — Sasha Rush's video walkthrough of the method. Key clarifications: (1) no new rollout or decode is needed — the same token sequence is re-scored under modified context; (2) Cursor wrote manual prompts that scan trajectories for specific mistake patterns and suggest where to inject feedback; (3) the method currently complements RL rather than replacing it, limited to easily identifiable error types.

## Notes

- Example from the post: after a "tool not found" error, a hint listing available tools shifts teacher mass toward valid tools; only that turn's student weights are updated.
- Applied beyond tool use to coding style and model communication.
- Related literature cited in the post: Self-Distillation Enables Continual Learning, Reinforcement Learning via Self-Distillation, Self-Distilled Reasoner (arXiv 2601.19897, 2601.20802, 2601.18734).
- Rush's tennis analogy: sequence KD is watching Nadal play and copying his game; OPD/OPSD is having Nadal stand over your shoulder correcting your swing on your own strokes. The distinction is whose trajectory the student trains on.

## Related

- [[Introducing Composer 2.5]]
- [[Sasha Rush Explains Targeted On-Policy Self-Distillation]]
- [[On-Policy Distillation]]
- [[On-Policy Self-Distillation]]
- [[KL Regularization]]
- [[Reinforcement Learning]]
- [[Agent Harness]]
- [[Tool Call Reliability]]
