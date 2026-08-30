# Doom Loop

**Type**: concept  
**Tags**: #concept

## Overview

A **doom loop** is a repetitive degeneration failure mode in language models during inference: the model emits the same token span repeatedly until the context window is exhausted. It shows up most often in long reasoning traces on hard math or coding problems under greedy or low-temperature decoding.

## Appearances

- [[Antidoom]] — Liquid AI analysis of three mechanisms (overtrained-token fallback, prior-context reinforcement, greedy lock-in) and FTPO mitigation.
- [[Safety and Alignment]] — text degeneration and alignment risks.

## Notes

- Related to classic neural text degeneration (Holtzman et al. 2020) but tied specifically to reasoning-model loop lock-in.
- Antislop and FTPO treat the loop-starting token as the intervention point rather than rewriting the full trace.
- Liquid AI reports doom-loop rates of 10–23% on some checkpoints before FTPO, falling to about 1% after.

## Related

- [[Antidoom]] — source post and benchmarks.
- [[Final Token Preference Optimization]] — training fix scoped to loop-start tokens.
- [[Safety and Alignment]] — topic hub.
- [[Large Language Models]] — topic hub.
