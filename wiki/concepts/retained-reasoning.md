# Retained Reasoning

**Type**: concept  
**Tags**: #concept

## Overview

**Retained reasoning** is an OpenAI [[Responses API]] behavior where a model's private chain-of-thought persists across turns when developers pass `previous_response_id` from a prior response, rather than discarding reasoning after each API call. It is the default persistence mode for GPT-5.6-class models built on the Responses API and is used inside ChatGPT and Codex.

## Appearances

- [[How Two Settings Tripled Our ARC-AGI-3 Scores]] — enabling retained reasoning (with compaction) raised GPT-5.6 Sol's ARC-AGI-3 score from 13.3% to 38.3%.
- [[Responses API]] — API surface where reasoning continuity is configured.

## Notes

Benchmark harnesses that discard private reasoning after every action can substantially understate model performance on long-horizon interactive tasks. ARC Prize co-founder François Chollet considers general-purpose API settings available to all developers fair game for reporting, distinct from harnesses custom-built for a specific benchmark.

## Related

- [[Compaction]]
- [[Responses API]]
- [[Reasoning Models]]
- [[Chain of Thought Monitorability]]
- [[ARC-AGI-3]]
