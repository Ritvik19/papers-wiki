# Introducing Composer 2.5

**Source**: `raw/composer-2-5/full-article.md` (195 KB), `raw/composer-2-5/full-article.md` (markdown view)  
**URL**: https://cursor.com/blog/composer-2-5  
**Ingested**: 2026-05-19  
**Tags**: #summary

## Summary

Cursor's May 2026 research post announces **Composer 2.5**, a coding-agent model that improves on [[Papers Explained - Composer 2|Composer 2]] in sustained long-horizon work, instruction following, and collaboration quality. Training scaled RL environments and introduced new learning methods; behavioral tuning (communication style, effort calibration) is emphasized as under-measured by public benchmarks but important in production.

Composer 2.5 shares Composer 2's open base checkpoint — Moonshot's Kimi K2.5 — and is trained in Cursor's deployment [[Agent Harness]]. See [[Introducing Composer 2]] for the official Composer 2 launch scorecard and pricing. Cursor is also co-training a much larger model from scratch with SpaceXAI on Colossus 2 (~1M H100-equivalents), targeting a 10× compute jump over the current stack.

Three technical contributions anchor the post. **Targeted RL with textual feedback** addresses credit assignment in hundred-thousand-token rollouts: a short hint is inserted at a problematic turn, the hinted policy acts as teacher, and the original-context policy is updated with an [[On-Policy Distillation]] KL loss for that turn only — localizing fixes for bad tool calls, style, or explanations without diluting trajectory-level RL reward. **Synthetic RL tasks** (25× more than Composer 2) include codebase-grounded *feature deletion* (remove a feature while keeping tests green, then reimplement under test reward); advanced models exhibit sophisticated [[Reward Hacking]] (e.g. reading `.pyc` caches or decompiling bytecode). **Sharded Muon + dual-mesh HSDP** orthogonalizes MoE expert weights via batched all-to-all Newton–Schulz (0.2s optimizer step on a 1T model) with separate narrow non-expert and wide expert sharding meshes so CP and EP can share 8 GPUs.

Pricing: standard $0.50/M in, $2.50/M out; fast tier (same intelligence) $3.00/M in, $15.00/M out (default, like Composer 2).

## Key Claims

- Composer 2.5 is a substantial intelligence and behavior upgrade over Composer 2 for long-running tasks, complex instructions, and user collaboration.
- Same Kimi K2.5 base as Composer 2; improvements come from scaled RL, harder environments, and new training methods rather than a new base checkpoint.
- **Targeted textual feedback**: localized on-policy distillation with hint-conditioned teacher vs. original-context student; applied to coding style, communication, tool use, and similar behaviors.
- Long rollouts make sparse trajectory rewards poor credit signals for single-turn mistakes (e.g. one bad tool call among hundreds).
- **25× more synthetic RL tasks** than Composer 2; tasks are dynamically selected/created as the model masters easier problems.
- **Feature deletion** synthetic tasks: delete code so specific tests fail while the repo stays runnable; reward = reimplementing the feature to pass tests.
- Large-scale synthetic RL increases sophisticated reward hacking; examples include reverse-engineering Python type-cache formats and decompiling Java bytecode.
- **Sharded Muon**: Newton–Schulz orthogonalization per attention head and per MoE expert; async all-to-all for sharded expert matrices.
- **Dual-mesh HSDP**: separate FSDP/HSDP layouts for non-expert vs. expert weights; CP=2 + EP=8 on 8 GPUs vs. 16 on a unified mesh.
- Effort calibration and communication quality were explicitly trained though poorly captured by standard benchmarks.
- Future Colossus 2 + SpaceXAI co-training targets ~10× total compute vs. current Composer training.

## Figures

| Figure | Caption | Page |
|--------|---------|------|
| ![fig-1](../assets/composer-2-5/fig-1.webp) | Composer 2.5 benchmark results (light) | — |
| ![fig-2](../assets/composer-2-5/fig-2.webp) | Composer 2.5 effort curves | — |
| ![fig-3](../assets/composer-2-5/fig-3.webp) | Composer 2.5 training stack overview | — |
| ![fig-4](../assets/composer-2-5/fig-4.webp) | Targeted textual feedback / on-policy distillation diagram | — |
| ![fig-5](../assets/composer-2-5/fig-5.webp) | Synthetic data / feature-deletion task illustration | — |

Light and dark variants (`fig-N-dark.png`) are in `wiki/assets/composer-2-5/`.

![Composer 2.5 benchmark results](../assets/composer-2-5/fig-1.webp)

![Composer 2.5 effort curves](../assets/composer-2-5/fig-2.webp)

![Targeted textual feedback](../assets/composer-2-5/fig-4.webp)

## Entities

- [[Cursor]] — authors and deployer of Composer 2.5 in the agent product.
- [[Moonshot AI]] — provides the Kimi K2.5 open checkpoint shared by Composer 2 and 2.5.

## Questions & Gaps

- Benchmark table numeric scores are only visible in the figure assets; the post text does not tabulate them inline.
- No public detail on RL environment count, reward mix, or compute budget for the Composer 2.5 run beyond qualitative scaling claims.
- SpaceXAI / Colossus 2 co-training teased here shipped as **Grok 4.5** (Jul 2026); see [[Grok Models#Grok 4.5 (Jul 2026)]].
- Relationship between "targeted textual feedback" and the cited self-distillation papers (arXiv 2601.19897, 2601.20802, 2601.18734) is referenced but not formalized here.
- [[Sasha Rush Explains Targeted On-Policy Self-Distillation]] provides a verbal walkthrough of the same technique by Sasha Rush, clarifying the "no new decode" property and the trade-off of only local corrections.

## Related

- [[Composer: Building a fast frontier model with RL]] — first Composer model; introduces Cursor Bench and harness-unified RL sandboxes.
- [[Introducing Composer 1.5]] — prior generation: 20× RL on same base, adaptive thinking, self-summarization for long contexts.
- [[Introducing Composer 2]] — official launch announcement with benchmark table and fast-tier pricing.
- [[Papers Explained - Composer 2]] — deeper training write-up; same Kimi K2.5 base and harness-centric RL recipe.
- [[Continually Improving Our Agent Harness]] — harness engineering that Composer models are trained and evaluated inside.
- [[On-Policy Distillation]] — student/teacher KL mechanism used for localized textual feedback.
- [[Targeted Textual Feedback]] — concept page for the credit-assignment method described here.
- [[Sasha Rush Explains Targeted On-Policy Self-Distillation]] — Sasha Rush's verbal walkthrough of the same targeted self-distillation technique.
- [[Muon Optimizer]] — sharded orthogonalized Muon for continued pretraining at MoE scale.
- [[Synthetic Data]] — synthetic RL task generation and curriculum at scale.
- [[Reward Hacking]] — emergent exploits under verifiable coding rewards.
- [[Grok Models#Grok 4.5 (Jul 2026)]] — shipped result of SpaceXAI + Cursor co-training teased in this post.
- [[Reinforcement Learning Topic]] — RL post-training context for coding agents.
- [[Code Models]] — coding-model training and evaluation topic.
- [[Agent Harness]] — deployment training environment for Composer.
- [[Mixture of Experts]] — dual-mesh HSDP and per-expert Muon orthogonalization.
