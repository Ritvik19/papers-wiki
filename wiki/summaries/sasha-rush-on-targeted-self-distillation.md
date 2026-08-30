# Sasha Rush Explains Targeted On-Policy Self-Distillation

**Source**: `raw/sasha-rush-on-targeted-self-distillation/video.mp4` (video), `raw/sasha-rush-on-targeted-self-distillation/transcript.txt` (auto-transcribed)  
**URL**: https://x.com/dwarkesh_sp/status/2062353335529935114  
**Ingested**: 2026-06-04  
**Tags**: #summary

## Summary

In an impromptu iPhone-recorded lecture, [[Sasha Rush]] walks [[Dwarkesh Patel]] through three distillation regimes — sequence knowledge distillation, [[On-Policy Distillation]], and [[On-Policy Self-Distillation]] — and explains how [[Cursor]] applied the last of these as [[Targeted Textual Feedback]] to train [[Introducing Composer 2.5|Composer 2.5]].

The progression is motivated by a single question: whose trajectory does the student learn from? In sequence knowledge distillation, the student trains on the teacher's output — like watching Rafael Nadal play tennis and trying to copy his game. In on-policy distillation, the student generates its own rollout and the teacher scores each token — like having Nadal stand over your shoulder correcting your swing. The key shift is that the training states are the student's own, not the teacher's, which means the student learns corrections to the mistakes it actually makes rather than trying to imitate states it would never visit.

For Composer 2.5, Cursor has no external teacher model. Instead they use on-policy self-distillation: the student's own trajectory is taken, a short textual hint is injected at a turn identified as problematic, and the policy is re-scored (forward pass only, no new decode) under this modified context. The log-probability shift induced by the hint defines a teacher signal. Crucially, the original and modified trajectories share identical tokens — the only change is the injected hint text, and the model simply assigns different probabilities to the existing tokens under the altered context. This makes the method computationally cheap: one rollout, one reader pass to locate the error, one forward pass with the hint, then a standard backprop step combined with the RL loss.

Rush acknowledges the core trade-off: because you never leave your own trajectory, progress is local and incremental. You will not make "amazing, incredible" leaps because by the time you reach the end of the rollout, you are still executing the same bad decisions you made before — you are only getting "little local corrections." This contrasts with sequence knowledge distillation, where the teacher's full trajectory could demonstrate globally better play.

## Key Claims

- **Sequence knowledge distillation** produces training data from the teacher's trajectory; the student matches teacher outputs via cross-entropy. Analogy: watching Nadal play.
- **On-policy distillation (OPD)** has the student produce its own rollout, then the teacher scores each token via log-probability comparison. The student updates toward the teacher's preferences on its own states. Analogy: Nadal correcting your swing over your shoulder.
- **OPD integrates cleanly with RL**: the student is already doing rollouts and forward/backward passes for the RL loss, so adding a distillation KL term is cheap — you reuse the student log-probs you already computed.
- **On-policy self-distillation (OPSD)** synthesizes a teacher by injecting text feedback into the student's own trajectory. No external teacher model is needed.
- **No new rollout or decode is required**: the same token sequence is re-scored under modified context (with hint tokens inserted). This is a forward pass, not a generation step.
- **Credit assignment motivation**: in Composer's hundred-turn RL rollouts, sparse trajectory reward cannot pinpoint which single turn failed. Automated prompts scan for specific mistakes (styling, tool errors) and inject targeted text feedback at the problematic turn.
- **Automated error detection**: Cursor wrote manual prompts that read the trajectory, look for specific mistake patterns, and suggest where to inject text feedback and what to say.
- **Trade-off**: OPSD gives only local, incremental corrections. The student cannot make dramatic progress because it is still executing its own bad trajectory; it is getting small corrections, not a globally better plan.
- **Current scope**: the method complements RL rather than replacing it; Cursor focuses on easily identifiable error types as a starting point.

## Figures

No images; source is a video recording.

## Entities

- [[Sasha Rush]] — lecturer; explains the distillation progression and Cursor's OPSD implementation.
- [[Dwarkesh Patel]] — interviewer; recorded the impromptu lecture and posted it to X.
- [[Cursor]] — company that applied targeted OPSD to train Composer 2.5.

## Questions & Gaps

- Rush mentions "manual prompts" for error detection — are these static templates or model-generated? The transcript suggests human-authored patterns, but the scope of automation is unclear.
- How many error categories does the targeted feedback currently cover? Rush says they started with easily identifiable ones.
- Does the text feedback ever backfire — i.e., does the hint sometimes shift probability mass in unhelpful directions? The Will Brown article ([[On SFT RL and On-Policy Distillation]]) warns about dense, biased, concentrated gradients from OPSD.
- The tennis analogy is vivid but raises a question: in real coaching, the coach sometimes interrupts and forces a redo. Does Cursor ever re-roll parts of the trajectory, or is it strictly re-scoring only?

## Related

- [[Introducing Composer 2.5]] — the blog post describing the same technique; this video provides Sasha Rush's verbal walkthrough with additional intuitions.
- [[Targeted Textual Feedback]] — concept page for the hint-injection credit-assignment method.
- [[On-Policy Distillation]] — the teacher-scored student-rollout regime that OPSD extends.
- [[On-Policy Self-Distillation]] — concept page for using the student itself as a teacher under privileged context.
- [[On SFT RL and On-Policy Distillation]] — Will Brown's article providing the theoretical framework (gradient taxonomy, KL concentration risk).
- [[Distillation Regimes Compared]] — comparison of classical KD, completion-SFT, and OPD.
- [[Model Distillation]] — parent concept.
- [[KL Regularization]] — used in the distillation KL loss.
- [[Reinforcement Learning Topic]] — RL context for coding agents.
