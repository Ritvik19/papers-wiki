# Lexical Search

**Type**: concept  
**Tags**: #concept

## Overview

Lexical search retrieves documents or passages by matching surface forms such as words, substrings, regular expressions, or sparse term weights. In [[Papers Explained: Is Grep All You Need]], the lexical baseline is grep-style regex search over conversation turns and extracted events, scored by match counts.

## Appearances

- [[Papers Explained: Is Grep All You Need]] - inline grep often outperforms vector retrieval on LongMemEval-style agent memory tasks, though results depend on harness and delivery format.

## Notes

Lexical search is high precision when the query vocabulary matches the evidence, but it can miss paraphrases and facts described in different words. Its strength in the source is not that it is universally smarter than [[Dense Retrieval]], but that simple, inspectable matches can be easier for an [[Agent Harness]] to expose and for an agent to use.

## Related

- [[Dense Retrieval]]
- [[Agentic Search]]
- [[Embedding and Retrieval]]
- [[Agent Harness]]
