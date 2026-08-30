# Thinking Mode Fusion

**Type**: concept  
**Tags**: #concept

## Overview

**Thinking Mode Fusion** is a post-training stage (introduced in Qwen3) where a single checkpoint learns both thinking and non-thinking behaviors via supervised fine-tuning on mixed examples, then reinforced in general RL.

## Appearances

- [[Controlling Reasoning Effort in LLMs]] — Qwen3 recipe: `/think` examples with full traces vs. `/no_think` with empty `<think></think>` plus short answers.

## Notes

Thinking is default; `/think` can be omitted. At inference, `enable_thinking=False` prefills an empty thinking block as a **hard** switch (tokenizer-level), while `/no_think` is a softer SFT flag. This binary on/off is a simplified version of multi-level [[Reasoning Effort]].

## Related

- [[Think Tokens]]
- [[Reasoning Effort]]
- [[Qwen]]
- [[Reasoning Models]]
