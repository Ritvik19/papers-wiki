# ARC-AGI-3

**Type**: entity  
**Tags**: #entity

## Overview

**ARC-AGI-3** is the third-generation benchmark from ARC Prize, testing agents on interactive 2D puzzle games where they must explore unfamiliar environments and infer rules without instructions. It succeeded ARC-AGI-2 as the harder contested abstraction-and-reasoning test as frontier models approach saturation on earlier ARC benchmarks.

## Appearances

- [[How Two Settings Tripled Our ARC-AGI-3 Scores]] — OpenAI analysis of harness effects on GPT-5.6 Sol scores (7.8–13.3% official vs 38.3% with retained reasoning + compaction).
- [[GPT-5.6]] — official-harness scores: Sol 7.78%, Terra 0.8%, Luna 0.18%.

## Notes

ARC Prize verified testing uses a standardized "no harness" setup: identical observations, system prompts, and action limits for every model, with client-side conversation state via a completions-style interface. This prevents provider-specific harness tuning but may not expose capabilities available through modern APIs (e.g. server-side reasoning persistence, compaction). ARC Prize is working with OpenAI and other labs on how server-side state management might enter verified testing fairly.

## Related

- [[Evaluation and Benchmarks]]
- [[Reasoning Models]]
- [[Retained Reasoning]]
- [[Compaction]]
- [[Responses API]]
