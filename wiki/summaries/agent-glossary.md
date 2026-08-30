# Harness, Scaffold, and the AI Agent Terms Worth Getting Right

**Source**: `raw/agent-glossary/full-article.md`, `raw/agent-glossary/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

A Hugging Face glossary post prompted by a post-ICLR 2026 question ("what do you mean by 'harness' and 'scaffold'?") that grounds a set of AI-agent terms whose usage has drifted or blurred as the field moved faster than shared vocabulary. Rather than an exhaustive dictionary, it focuses on terms that get conflated in practice, split into inference-time and training-specific vocabulary.

At inference time, the post proposes: a **model** is the bare LLM (no memory, no loop, can only express intent to call a tool); **scaffolding** is the behavior-defining layer around it (system prompt, tool descriptions, response parsing, what's kept in context across steps); a **harness** is the execution layer that actually calls the model, handles its tool calls, and decides when to stop (harness engineering, meaning stopping conditions, error handling, and guardrails, applies at both training and inference, and the same pattern run against a fixed benchmark is called an "eval harness"). The shorthand offered is **Agent = Model + Harness**, tracing back to the term's reinforcement-learning origin (a function from observation to action, with the environment returning the next observation). Products like Claude Code, Codex, and Cursor bundle a specific harness with a specific model as one designed product, but the model, harness, and product remain three conceptually separate things; some product docs (Claude Code's own) use "harness" to mean the whole scaffold+execution stack, which the post flags as the most common point of confusion motivating the piece. **Context engineering** is designing what enters the context window at each step, framed as higher-stakes at training time (bad context design there means retraining) than at inference time (a prompt tweak and redeploy fixes it). A **policy** is the behavior distribution over actions; it is not synonymous with "agent," since an agent's behavior also depends on the surrounding scaffold/harness, not just weights. **Tool use** is the model expressing an action-intent that the harness routes to a function and feeds back as context; **skills** are reusable, structured task-completion packages (broader than a single tool call, narrower/more autonomous than a delegated **sub-agent**, which has its own model, scaffold, and reasoning loop and can itself call further sub-agents or tools).

Training-specific terms cover the RL side: an **RL environment** is a stateful object taking an action and returning an updated observation; a **trainer** (example given: TRL's `GRPOTrainer`) runs many episodes, scores them, and updates weights; a **rollout** (or trajectory/trace) is one full episode's record of observations, actions, and rewards; a **reward** is the training signal, which can be verifiable or learned, sparse or dense, and can be decomposed into weighted **rubrics** (frameworks like OpenEnv and Verifiers implement these as composable objects such as `WeightedSum`, `Sequential`, `Gate`). The authors are explicit that many of these terms lack universally agreed definitions across frameworks, and the glossary aims to establish one practical, internally consistent mental model rather than to prescribe the field's terminology; comments proposed alternatives (e.g. "rigging" instead of "scaffolding," to avoid clashing with software's pre-existing "scaffolding" meaning) and additional terms worth covering in a follow-up (leaderboard, benchmark, MCP's role relative to the harness/tool-use pipeline).

## Key Claims

- Proposed shorthand: **Agent = Model + Harness**, where scaffolding (system prompt, tool descriptions, context/memory management) defines behavior and the harness is the execution loop that calls the model, dispatches tool calls, and decides when to stop.
- "Harness" is used two ways in the wild: narrowly as just the execution loop (this post's preferred sense), or broadly as the whole scaffold+execution stack (as in Claude Code's own documentation). The post flags this split as the field's main terminology ambiguity.
- Context engineering carries asymmetric risk across the training/inference boundary: mistakes at training time require retraining to fix, mistakes at inference time only require redeploying a changed prompt.
- A policy (the behavior distribution given a situation) is distinct from an agent (the full system acting in an environment); part of the policy lives in model weights, but behavior is also shaped by scaffold and harness design.
- Sub-agents are distinguished from tools and skills by having their own model, scaffold, and independent reasoning loop, and by being able to call further tools or sub-agents themselves.
- Training vocabulary: RL environment (stateful action→observation object), trainer (runs episodes, scores, updates weights, e.g. TRL's `GRPOTrainer`), rollout/trajectory (one full episode record), reward (verifiable/learned, sparse/dense), rubric (weighted decomposition of a reward, implemented as composable objects in frameworks like OpenEnv and Verifiers).
- The authors state plainly that many of these terms lack a single agreed-upon definition across frameworks, and community comments proposed real alternatives (e.g. "rigging" over "scaffolding") rather than treating the glossary as settled.

## Figures

No figures were extracted for this ingest, per this batch's no-figure-download policy; the post is text-only.

## Entities

- [[Hugging Face]] — publishes the glossary and builds several of the referenced tools (TRL, `smolagents`).

## Questions & Gaps

- The post does not resolve the "harness" ambiguity it opens with, instead documenting both usages and picking one convention for its own vocabulary rather than arguing the other usage is wrong.
- Additional terms flagged by commenters (leaderboard, benchmark, MCP's relationship to tool use) are explicitly left out of scope for this post, suggesting a possible follow-up.

## Related

- [[Open-Source DeepResearch - Freeing Our Search Agents]] — an earlier HF post using several of these terms (agent framework, agentic system) informally, before this glossary formalized them.
- [[Agent Harness]]
- [[Coding Harness]]
