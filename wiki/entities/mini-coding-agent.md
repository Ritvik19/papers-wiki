# Mini Coding Agent

**Type**: tool  
**Tags**: #entity

## Overview

**Mini Coding Agent** is [[Sebastian Raschka]]'s minimal, from-scratch coding agent implemented in pure Python (no external dependencies). The repository at https://github.com/rasbt/mini-coding-agent annotates six [[Coding Harness]] components in code: workspace context, prompt prefix and cache-oriented packaging, structured tools with validation and approval, context clipping and transcript reduction, JSON session store with working memory, and bounded subagent delegation.

## Appearances

- [[Components of A Coding Agent]] — primary reference; article walks through all six components with figures and code-comment mapping.

## Notes

- Demonstrates tool-call approval UI and path sandboxing in a terminal setting, contrasted with polished products like [[Claude Code]] and Codex CLI.
- Subagent implementation runs synchronously in the minimal version; production agents add parallelism and richer sandbox inheritance.

## Related

- [[Sebastian Raschka]]
- [[Components of A Coding Agent]]
- [[Coding Harness]]
- [[Agent Harness]]
- [[Claude Code]]
