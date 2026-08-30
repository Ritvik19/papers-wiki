# GRPO++: Tricks for Making RL Actually Work

**Source**: `raw/grpo-tricks/full-article.html` (928 KB HTML) · `raw/grpo-tricks/full-article.md` (markdown view)  
**URL**: https://cameronrwolfe.substack.com/p/grpo-tricks  
**Author**: Cameron R. Wolfe, Ph.D. (Deep (Learning) Focus newsletter)  
**Ingested**: 2026-05-11  
**Tags**: #summary

## Summary

This comprehensive Deep (Learning) Focus newsletter article surveys the practical improvements made to Group Relative Policy Optimization ([[GRPO]]) — the default RL optimizer for training open-source reasoning models like DeepSeek-R1. Vanilla GRPO suffers from four interconnected failure modes — entropy collapse, noisy reward curves, training instability, and poor sample efficiency — that collectively make it difficult to reproduce the results reported in the original DeepSeek-R1 paper. The article systematically reviews the research papers that diagnosed and solved these problems, arriving at a practical cookbook of tricks for making RL training actually work at scale.

The article's architecture follows the research chronology: first reviewing DAPO's four algorithmic improvements (clip higher, dynamic sampling, token-level loss, overlong reward shaping), then Dr. GRPO's analysis of base-model properties and loss biases, then the off-policy engine-gap paper proposing Truncated Importance Sampling (TIS), and finally a broader survey of newer algorithms including GSPO (used in Qwen 3), GMPO, and CISPO (used in MiniMax-M1). The article closes with a practical synthesis using OLMo 3 as a worked example of how to combine multiple improvements into a coherent training recipe.

Throughout, the article emphasizes that healthy RL training can be monitored via four key metrics: average response length (should increase), training reward (should increase stably), policy entropy (should remain in a reasonable range — neither collapsing nor exploding), and held-out evaluation accuracy. These health indicators reveal whether interventions help or hurt, and they underpin all the paper comparisons in the article.

## Key Claims

- **Vanilla GRPO's entropy collapse** is caused by the symmetric clipping mechanism: exploration tokens (low probability) face a proportionally much harder time increasing in probability than exploitation tokens, so the policy concentrates on a small token set.
- **DAPO's "clip higher"** fix decouples the upper and lower clipping bounds: ε_low = 0.2 (unchanged) and ε_high = 0.28, preventing entropy collapse while maintaining the lower bound's role in keeping token sampling space alive.
- **Dynamic sampling** removes prompts for which all group completions receive the same reward (zero gradient elements), keeping effective batch size constant and improving sample efficiency dramatically.
- **Token-level loss aggregation** (average over all tokens rather than average within each sequence then average across sequences) eliminates a length bias where shorter sequences receive disproportionately large gradient updates.
- **Overlong reward shaping** (masking or soft-penalizing truncated completions) improves stability; simply assigning -1 to all truncated samples confuses the policy when the reasoning was valid but too verbose.
- **Dr. GRPO** ([3]) identifies two further biases: (1) sequence-level normalization causes longer incorrect answers to receive smaller penalties than shorter ones; (2) the standard deviation term in the advantage denominator causes advantage explosion on easy/hard prompts. Both are fixed by removing std from the advantage and normalizing loss by a fixed constant.
- **Qwen-2.5 base models** behave like SFT models without a template (concatenated Q-A format during pretraining), which means observed RL-Zero performance gains may be less impressive than they appear — the model wasn't truly unaligned.
- **The Aha moment** (self-reflection emerging mid-training) is partially pre-existing in DeepSeek-V3-Base; RL training increases its frequency but it doesn't measurably improve accuracy.
- **Off-policy engine gap**: Using separate sampler (vLLM/SGLang) and learner (FSDP/DeepSpeed) engines creates token-probability mismatches even with identical weights, effectively making on-policy RL off-policy. Different parallelism strategies (tensor vs. sequence parallelism) are the largest contributor. The engineering fix is incomplete; the algorithmic fix is **Truncated Importance Sampling (TIS)** — scaling the policy gradient by the (capped) importance ratio π_learner/π_sampler.
- **GSPO** (used for Qwen 3 training) computes importance ratios at the sequence level rather than the token level, reducing gradient variance and naturally stabilizing MoE training without the routing-replay hack needed for standard GRPO.
- **GMPO** keeps token-level importance ratios but aggregates with geometric mean (less sensitive to outliers) rather than arithmetic mean.
- **CISPO** (MiniMax-M1) uses stop-gradient on the importance ratio so that pivotal low-probability "fork" tokens (e.g., "wait", "aha") contribute to all policy updates rather than being clipped out after the first.
- **OLMo 3** serves as a practical synthesis, combining: zero-gradient filtering, active sampling, token-level loss, no KL loss, higher upper clipping bound, TIS, and no standard deviation in advantage.

## Figures

| Figure | Caption | Notes |
|--------|---------|-------|
| ![fig-1](../assets/grpo-tricks/fig-1.png) | RL training pipeline overview (RLHF vs. RLVR) | Intro section |
| ![fig-2](../assets/grpo-tricks/fig-2.png) | RLVR verifiable reward setup (string matching for math) | RLVR section |
| ![fig-3](../assets/grpo-tricks/fig-3.png) | Reasoning model training stages with RL-Zero | Training stages |
| ![fig-4](../assets/grpo-tricks/fig-4.png) | PPO surrogate objective with clipping | PPO section |
| ![fig-5](../assets/grpo-tricks/fig-5.png) | GRPO advantage estimation formula | GRPO section |
| ![fig-6](../assets/grpo-tricks/fig-6.png) | DAPO health metrics (entropy, reward, response length) | DAPO analysis |
| ![fig-7](../assets/grpo-tricks/fig-7.png) | Entropy collapse from symmetric clipping | Clip higher motivation |
| ![fig-8](../assets/grpo-tricks/fig-8.png) | DAPO AIME 2024 accuracy vs. vanilla GRPO | DAPO experiments |
| ![fig-9](../assets/grpo-tricks/fig-9.png) | GRPO length bias — incorrect responses grow longer | Dr. GRPO analysis |
| ![fig-10](../assets/grpo-tricks/fig-10.png) | Token probability mismatch between sampler/learner engines | Off-policy engine gap |

## Entities

- [[GRPO]] — The central algorithm this article dissects and improves.
- [[DAPO]] — Decoupled Clip and Dynamic Sampling Policy Optimization; the main improved algorithm from ByteDance/Tsinghua.
- [[Dr. GRPO]] — Modified GRPO from [3] that removes std from advantage and uses fixed-constant loss normalization.
- [[GSPO]] — Group Sequence Policy Optimization; used in Qwen 3 training; sequence-level importance ratios.
- [[GMPO]] — Geometric Mean Policy Optimization; geometric mean aggregation of token-level losses.
- [[CISPO]] — Clipped Importance Sampling Weight Policy Optimization; from MiniMax-M1; soft clipping via stop-gradient.
- [[Truncated Importance Sampling]] — Algorithmic fix for the sampler-learner engine gap in RL frameworks.
- [[Cameron R. Wolfe]] — Author; Deep Learning PhD; Senior Research Scientist at Netflix.
- [[DeepSeek-R1]] — The reasoning model whose RL training recipe this article aims to understand and improve upon.
- [[Qwen 3]] — Model family that adopted GSPO for RL training.
- [[OLMo 3]] — Practical synthesis example combining all major GRPO improvements.
- [[Reinforcement Learning Topic]] — Broader topic page for RL in LLMs.
- [[Reasoning Models]] — Topic page for reasoning model research.

## Questions & Gaps

- The article focuses exclusively on math/coding RLVR. Do these tricks transfer to RLHF and preference-based domains? The author acknowledges this is an open question.
- No ablation comparing all four DAPO tricks individually on MoE models — only GSPO's impact is shown there.
- The Aha moment analysis was done only on DeepSeek-V3-Base. Whether other families exhibit it pre-RL is unknown.
- TIS is tested mostly with DAPO/PPO and early-stopped runs. Its behavior over full training runs at large scale is not analyzed.
- Data curriculum learning is acknowledged as understudied; authors note data diversity beats curriculum selection in current practice.

## Related

- [[Reinforcement Learning Topic]] — Broader RL-in-LLM topic covering RLHF, RLVR, PPO, GRPO, and related papers.
- [[Reasoning Models]] — Topic page collecting reasoning model papers including DeepSeek-R1, o1, and RLVR-trained models.
- [[Policy Gradient]] — Concept page for the optimization lens underlying all PPO/GRPO variants.
- [[KL Regularization]] — Concept page; article notes KL is commonly dropped for reasoning model RL.
- [[On SFT RL and On-Policy Distillation]] — Related discussion of how RL differs from SFT and distillation.
