# Coding Harness

**Type**: concept  
**Tags**: #concept

## Overview

A **coding harness** is a task-specific [[Agent Harness]] optimized for software engineering in a repository: it assembles prompts, exposes structured coding tools (read, search, edit, shell), tracks file and git state, manages permissions, caches stable prompt prefixes, compacts session context, and supports resumable transcripts and bounded subagents. [[Components of A Coding Agent]] by [[Sebastian Raschka]] names six core components—live repo context, prompt shape and cache reuse, structured tools, context reduction, structured session memory, and delegation with bounded subagents—and implements them in the [[Mini Coding Agent]] reference repo.

## Six Components (Raschka Taxonomy)

1. **Live repo context** — workspace summary (git branch/status, repo root, `AGENTS.md` / README instructions) gathered before acting on underspecified tasks.
2. **Prompt shape and cache reuse** — stable prefix (system instructions, tool descriptions, workspace summary) separated from volatile per-turn state (recent transcript, working memory, latest user request) to avoid rebuilding and to exploit prefix caching.
3. **Structured tools, validation, permissions** — named tools with schema-checked arguments, optional user approval, and path sandboxing inside the workspace.
4. **Context reduction** — clipping verbose tool outputs, deduplicating repeated file reads, and compressing older transcript events while keeping recency rich ([[Context Rot]] mitigation).
5. **Structured session memory** — durable full transcript (resumption) plus smaller working memory (task continuity) and a compact transcript view for prompt reconstruction.
6. **Bounded subagents** — delegated side tasks with inherited but constrained context (read-only, depth limits, task scoping).

## Distinction From General Agent Harnesses

Raschka distinguishes a coding harness from broader platforms like [[OpenClaw]], which also use workspace instruction files and session compaction but optimize for long-lived multi-channel local agents rather than repo-centric terminal coding. Products such as [[Claude Code]], Codex CLI, and Cursor's [[Agent Harness]] are coding-harness instances in this taxonomy.

## Appearances

- [[Components of A Coding Agent]] — primary pedagogical source and six-component taxonomy.
- [[Continually Improving Our Agent Harness]] — production harness engineering (dynamic context, evals, per-model customization) complementing Raschka's from-scratch reference.
- [[Composer: Building a fast frontier model with RL]] — RL training inside the production coding harness, treating harness tools as part of the training environment.
- [[Harness Engineering for Self-Improvement]] — research survey on evolving harnesses via observability, self-editing loops, and evolutionary search.

## Related

- [[Agent Harness]]
- [[Components of A Coding Agent]]
- [[Mini Coding Agent]]
- [[Claude Code]]
- [[Dynamic Context]]
- [[Context Rot]]
- [[Tool Call Reliability]]
- [[Code Models]]
- [[Agentic AI]]
- [[Harness Engineering for Self-Improvement]]
- [[Self-Improving Harness]]
