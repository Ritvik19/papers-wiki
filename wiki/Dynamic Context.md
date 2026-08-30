# Dynamic Context

#concept

Dynamic context is the part of an agent's context window that the agent retrieves on demand at runtime, rather than receiving it pre-packed at session start. The [[Agent Harness]] exposes affordances such as semantic code search, file readers, terminal session readers, past-conversation lookups, and tool registries; the model decides when and what to pull in. The technique trades the predictability of static context for the ability to grow context with the task and to avoid spending tokens on material the agent does not actually need.

## Why It Replaced Static Context

[[Continually Improving Our Agent Harness]] traces the shift from late-2024 harnesses that loaded the folder layout, semantically retrieved snippets, and compressed user attachments at the start of each session toward today's harnesses that keep only a small static base (operating system, git status, current and recently viewed files). Two pressures drove the change. First, models got better at choosing their own context, so guardrails like rewriting too-short file reads or capping per-turn tool calls became net-negative overhead. Second, [[Papers Explained 445 - Context Rot]] showed that long context degrades performance non-uniformly, so spending tokens defensively up front actively harmed quality.

Dynamic context inverts the budget: instead of paying token cost for context that may or may not be useful, the agent pays a tool-call cost only when context is needed, and the harness optimizes those tool calls for latency, cache, and reliability. This is also why [[Tool Call Reliability]] becomes load-bearing for dynamic-context harnesses — every dynamic affordance is a tool the agent might call, and a single failed call wastes tokens and induces [[Context Rot]].

[[Papers Explained: Is Grep All You Need]] adds a retrieval-specific version of the same lesson. When memory-search results are appended inline, they compete directly with prompts and conversation history in the context window. When results are written to files, the model must explicitly inspect them, which changes the balance between [[Lexical Search]] and [[Dense Retrieval]] and makes harness ergonomics part of the retrieval result.

## Related

- [[Agent Harness]]
- [[Continually Improving Our Agent Harness]]
- [[Papers Explained: Is Grep All You Need]]
- [[Long Context]]
- [[Papers Explained 445 - Context Rot]]
- [[Tool Call Reliability]]
- [[Context Rot]]
- [[Agentic AI]]
- [[Code Models]]
