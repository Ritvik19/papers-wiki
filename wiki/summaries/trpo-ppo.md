# Trust Region and Proximal Policy Optimization (TRPO and PPO)

**Source**: `raw/trpo-ppo/full-article.md` (331 KB), `raw/trpo-ppo/full-article.md` (markdown view)  
**URL**: https://theaisummer.com/TRPO_PPO/  
**Author**: Sergios Karagiannakos (AI Summer), 2019-01-11  
**Ingested**: 2026-06-06  
**Tags**: #summary

## Summary

This AI Summer article returns to **policy optimization** after [[The Idea behind Actor-Critics and How A2C and A3C Improve Them]], introducing **[[Trust Region Policy Optimization]]** and **[[Proximal Policy Optimization]]** as solutions to policy-gradient pathologies: high variance (partially addressed by [[Actor-Critic Methods]]), delayed rewards, sample inefficiency, and especially **learning-rate sensitivity** — small rates cause vanishing progress, large rates cause exploding destructive updates. The goal is to change the policy enough to improve but not so much that performance collapses.

**TRPO** formalizes this as a **constrained optimization** problem: maximize the importance-sampled policy improvement objective subject to a **[[KL Divergence]]** trust-region constraint E[KL(π_old, π_new)] ≤ δ. Trust regions are local neighborhoods where linear/quadratic approximations of the objective remain accurate; iteratively finding local maxima within expanding/shrinking regions seeks the global optimum. TRPO solves the constrained problem numerically via **conjugate gradient** on a linearized objective with quadratically approximated KL constraint (more practical than analytic natural gradient descent at scale). The loop: collect trajectories → estimate advantages → solve constrained update → repeat.

**PPO** simplifies TRPO by **embedding the trust region as a penalty** (subtract C · KL from the objective) so plain stochastic gradient descent suffices — no conjugate gradient. The penalty coefficient C is adapted dynamically: increase when KL is too high, decrease when too low. However, the article's canonical PPO is not the penalized form but **PPO-Clip**: define importance ratio r_t(θ) = π_θ(a|s) / π_θ_old(a|s) and clip the surrogate objective:

L^CLIP(θ) = E[min(r_t Â_t, clip(r_t, 1−ε, 1+ε) Â_t)]

When the new policy makes an action much more or much less likely than the old policy, the clipped term prevents over-large advantage-weighted updates — a simple, stable surrogate that reuses old-policy samples via [[Importance Sampling]]. Training: collect trajectories → estimate advantages → multi-epoch SGD on L^CLIP → repeat. OpenAI's baseline implementation is cited as reference code.

This 2019 primer is the direct lineage ancestor of LLM RL: [[GRPO]] retains PPO-style clipping while replacing the learned critic with group-relative advantage baselines ([[GRPO++: Tricks for Making RL Actually Work]] surveys further refinements).

## Key Claims

- Policy gradients struggle with variance, delayed reward, sample inefficiency, and learning-rate tuning.
- **Trust region**: region where local policy-improvement approximations remain valid; step size bounded by δ.
- TRPO constrains KL(π_old, π_new) ≤ δ while maximizing importance-weighted advantage surrogate.
- TRPO solved with conjugate gradient on linearized objective + quadratic KL constraint (not naive natural gradient).
- TRPO loop: rollouts → advantage estimation → constrained solve → repeat.
- PPO (penalized): KL penalty inside objective enables unconstrained SGD; adaptive coefficient C tracks KL.
- **PPO-Clip** is the standard practical algorithm: clip importance ratio r_t to [1−ε, 1+ε] when multiplying advantages.
- Clipping prevents destructive updates when new policy diverges too far from behavior policy.
- Importance ratio r_t(θ) enables reusing samples from π_old to evaluate π_θ (sample efficiency).
- PPO training: rollouts → advantages → several epochs of SGD on clipped objective → repeat.
- PPO-Clip is simpler than TRPO while often outperforming prior methods.

## Figures

No in-article figures (OpenGraph hero image excluded per ingest policy).

## Entities

- [[AI Summer]] — published this TRPO/PPO tutorial (2019).
- [[Sergios Karagiannakos]] — author; third article in AI Summer RL policy-optimization arc.
- [[Trust Region Policy Optimization]] — KL-constrained policy improvement via conjugate gradient.
- [[Proximal Policy Optimization]] — clipped surrogate objective; standard deep RL and LLM RL ancestor.
- [[Actor-Critic Methods]] — provides advantage estimates Â_t used in both TRPO and PPO objectives.
- [[Importance Sampling]] — importance ratio r_t = π_new / π_old reuses old-policy rollouts.
- [[KL Divergence]] — trust-region distance measure in TRPO; penalty term in early PPO formulation.
- [[GRPO]] — modern LLM variant retaining PPO clipping with group-relative advantages.
- [[Policy Gradient]] — base optimization framework both methods stabilize.

## Questions & Gaps

- Article omits TRPO paper citation (Schulman et al. 2015) and PPO paper (Schulman et al. 2017).
- Penalized PPO vs PPO-Clip relationship could confuse readers (clip form is the one widely used).
- No implementation walkthrough; points to OpenAI baselines externally.
- GAE (generalized advantage estimation) not mentioned despite being standard with PPO.

## Related

- [[The Idea behind Actor-Critics and How A2C and A3C Improve Them]] — prior article; advantage estimation foundation.
- [[Unravel Policy Gradients and REINFORCE]] — series entry point for policy-based RL.
- [[GRPO++: Tricks for Making RL Actually Work]] — modern PPO/GRPO stabilization tricks for reasoning models.
- [[GRPO]] — group-relative policy optimization for LLMs.
- [[KL Regularization]] — related KL budget ideas in LLM post-training.
- [[Reinforcement Learning Topic]] — topic hub.
