# Cursor

**Type**: org  
**Tags**: #entity

## Overview

Cursor (Anysphere) builds an AI-native code editor and coding-agent product. The team publishes research on agent harness design, in-house models (Composer family), and large-scale RL training for software engineering.

## Appearances

- [[Composer: Building a fast frontier model with RL]] — original Composer (1) announcement: MoE agent model, Cursor Bench, MXFP8 async RL at scale, harness-unified sandboxes.
- [[Introducing Composer 1.5]] — Composer 1.5: 20× RL scale on same base, adaptive thinking tokens, RL-trained self-summarization, Terminal-Bench 2.0 results.
- [[Introducing Composer 2]] — Composer 2 product launch: benchmark scorecard (CursorBench 61.3, Terminal-Bench 61.7, SWE-bench Multilingual 73.7), continued pretraining + long-horizon RL, fast-tier pricing.
- [[Introducing Composer 2.5]] — announces Composer 2.5 training methods (targeted textual feedback, synthetic RL tasks, sharded Muon) and product pricing.
- [[Grok Models#Grok 4.5 (Jul 2026)]] — Grok 4.5 MoE model co-trained with SpaceXAI; Cursor's first model beyond pure software engineering.
- [[Sasha Rush Explains Targeted On-Policy Self-Distillation]] — Sasha Rush explains to Dwarkesh Patel how Cursor applied targeted on-policy self-distillation for Composer 2.5, clarifying the no-decode re-scoring mechanism and automated error detection prompts.
- [[Continually Improving Our Agent Harness]] — harness engineering: dynamic context, evals, tool reliability, per-model customization.
- [[Introducing Cursor Router]] — Jul 2026 launch of intelligent per-request model router for Teams/Enterprise: cache-aware classifier, three Auto modes, 30–60% cost savings at frontier quality.
- [[CursorBench]] — internal coding-agent benchmark built from real engineering sessions.

## Notes

- Composer models are trained in the same [[Agent Harness]] used in production, aligning RL environments with deployment.
- Grok 4.5 (Jul 2026) is the shipped result of co-training with SpaceXAI on a larger MoE model, fulfilling the forward-looking note in the Composer 2.5 post.

## Related

- [[Composer: Building a fast frontier model with RL]]
- [[Introducing Composer 1.5]]
- [[Introducing Composer 2]]
- [[Introducing Composer 2.5]]
- [[Grok Models]]
- [[Papers Explained - Composer 2]]
- [[Agent Harness]]
- [[Introducing Cursor Router]]
- [[Cursor Router]]
- [[CursorBench]]
- [[Code Models]]
