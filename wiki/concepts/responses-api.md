# Responses API

**Type**: concept  
**Tags**: #concept

## Overview

The **Responses API** is OpenAI's API surface for stateful, tool-using, reasoning-model workflows. It supports passing `previous_response_id` for cross-turn state, reasoning-effort configuration, programmatic and multi-agent tool orchestration, and context management features including **[[Compaction]]** and **[[Retained Reasoning]]**.

## Appearances

- [[GPT-5.6]] — Programmatic Tool Calling (in-memory tool coordination, ZDR compatible); multi-agent beta; recommended interface for retained reasoning and compaction.
- [[How Two Settings Tripled Our ARC-AGI-3 Scores]] — OpenAI recommends Responses API over legacy Chat Completions for long agentic tasks.
- [[gpt-oss-safeguard]] — supports Responses API with low/medium/high reasoning effort.
- [[GPT-5.3]] — persistent WebSocket + Responses API changes cut per-request overhead 80% during Codex-Spark development.

## Notes

OpenAI positions the Responses API as the preferred interface for GPT-5.6+ agentic workloads. Benchmark harnesses built on older completions-style interfaces may not expose Responses API capabilities, creating score gaps that reflect harness design rather than raw model capability alone.

## Related

- [[Retained Reasoning]]
- [[Compaction]]
- [[OpenAI]]
- [[Agentic AI]]
- [[Evaluation and Benchmarks]]
