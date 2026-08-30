# Agentic Search

**Type**: concept  
**Tags**: #concept

## Overview

Agentic search is search performed as part of an agent loop: the model chooses queries, calls retrieval tools, reads results, refines the search strategy, and answers from gathered evidence. Unlike a fixed one-shot retriever, the [[Agent Harness]] shapes the tool interface, context delivery, stopping criteria, and evidence-reading workflow.

## Appearances

- [[Papers Explained: Is Grep All You Need]] - frames retrieval over conversational memory as an agentic search problem where grep, vector search, harness design, and file-based result delivery interact.

## Notes

The concept links retrieval quality to agent behavior. Better search is not just a better index; it is also a better loop for choosing queries, inspecting evidence, avoiding distractors, and managing [[Dynamic Context]].

## Related

- [[Agent Harness]]
- [[Dynamic Context]]
- [[Lexical Search]]
- [[Dense Retrieval]]
- [[Embedding and Retrieval]]
