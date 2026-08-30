# LongMemEval

**Type**: concept  
**Tags**: #entity

## Overview

LongMemEval is a benchmark for evaluating long-term memory over multi-session conversations. Tasks include questions that require finding oracle sessions amid distractor sessions and reasoning over knowledge updates, user preferences, assistant outputs, and temporal facts.

## Appearances

- [[Papers Explained 445 - Context Rot]] - uses LongMemEval to compare focused prompts against full long-context prompts containing irrelevant conversation history.
- [[Papers Explained: Is Grep All You Need]] - provides the 116-question subset used to compare grep and vector retrieval across agent harnesses.

## Notes

The source uses LongMemEval as a stress test for agentic memory retrieval rather than only for raw long-context reading. This makes it especially relevant to [[Long Context]], [[Dynamic Context]], and [[Evaluation and Benchmarks]].

## Related

- [[Evaluation and Benchmarks]]
- [[Long Context]]
- [[Agentic Search]]
- [[Agent Harness]]
