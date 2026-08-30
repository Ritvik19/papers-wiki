# Think Tokens

**Type**: concept  
**Tags**: #concept

## Overview

**Think tokens** (often rendered as `<think>` and `</think>`) are delimiter tokens that mark where a [[Reasoning Models|reasoning model]]'s intermediate trace begins and ends. They separate the thinking block from the final user-visible answer in training pipelines and UIs.

## Appearances

- [[Controlling Reasoning Effort in LLMs]] — explains that think tokens are cosmetic with respect to reasoning ability; format reward encourages their use during RLVR.

## Notes

Think tokens do not create reasoning capability; models trained without them can reach similar benchmark performance. The literal strings are arbitrary—any delimiter pair works. In DeepSeek-R1, format reward is added to accuracy: $R_\text{total} = R_\text{accuracy} + R_\text{format}$.

## Related

- [[Reasoning Effort]]
- [[Thinking Mode Fusion]]
- [[Reinforcement Learning with Verifiable Rewards]]
