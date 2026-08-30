# Compaction

**Type**: concept  
**Tags**: #concept

## Overview

**Compaction** is an OpenAI [[Responses API]] feature that summarizes older conversation context instead of truncating or dropping it when transcripts grow long. It replaces rolling truncation strategies that discard the oldest messages once a character limit is reached.

## Appearances

- [[How Two Settings Tripled Our ARC-AGI-3 Scores]] — replacing ARC-AGI-3 harness rolling truncation (past 175k characters) with compaction, alongside retained reasoning, improved GPT-5.6 Sol scores and cut output tokens ~6×.
- [[GPT-5.1]] — GPT-5.1-Codex-Max uses compaction for reasoning across multiple context windows.

## Notes

Compaction preserves strategic context for long-running agentic tasks while managing context window limits. ARC Prize has discussed compaction with OpenAI as part of evaluating how server-side state management might enter verified benchmark testing.

## Related

- [[Retained Reasoning]]
- [[Responses API]]
- [[Long Context]]
- [[ARC-AGI-3]]
