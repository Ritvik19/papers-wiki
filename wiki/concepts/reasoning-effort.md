# Reasoning Effort

**Type**: concept  
**Tags**: #concept

## Overview

**Reasoning effort** is a user- or system-controlled setting that tells a [[Reasoning Models|reasoning model]] how much intermediate computation (typically tokens in the thinking trace) to spend before answering. Effort appears in product UIs ([[GPT-5.6]], Codex) and open models ([[Papers Explained 428 - gpt-oss]], Inkling) as ordinal labels (`low`/`medium`/`high`) or continuous values (0–1).

## Appearances

- [[Controlling Reasoning Effort in LLMs]] — comprehensive survey of training recipes (effort-conditioned SFT, token-penalty RLVR) and six open-weight implementations.
- [[GPT-5.6]] — Luna/Terra/Sol model family with multiple effort tiers per size; GA system card reports performance curves across effort levels rather than single scores; `max` and `ultra` modes for demanding tasks.
- [[A Single Question to Track Progress from o3 to GPT-5.6 and Beyond]] — long-horizon test-time compute (80–88 minutes per proof) enables GPT-5.6-pro to autonomously beat 35-year published mathematical SOTA.
- [[Implications of Large-Scale Test-Time Compute]] — [[Noam Brown]] analyzes how explicit effort budgets and token-allocation curves reveal true frontier capability scaling.
- [[Papers Explained 428 - gpt-oss]] — effort inserted into system message via chat template.
- [[Inkling]] — continuous effort via system message + per-token cost in RL; transformers `reasoning_effort` levels; see also [[Controllable Thinking Effort]].

## Notes

Training typically pairs effort labels in prompts with target trace lengths (SFT) or adjusts per-token cost in RLVR: $R(e) = R_\text{task} - \lambda(e)\,N_\text{tokens}$. At inference, effort is often a system-prompt field. Effort correlates with token usage and accuracy but shows diminishing returns. Model size and effort are separate scaling axes.

Automatic effort selection (GPT-5 Auto) was tried and removed; [[Harness Engineering for Self-Improvement]] discusses future harness/router-based inference.

## Related

- [[Test-Time Compute]]
- [[Think Tokens]]
- [[Thinking Mode Fusion]]
- [[Reasoning Budget]]
- [[Controllable Thinking Effort]]
- [[Reasoning Models]]
- [[Reinforcement Learning with Verifiable Rewards]]
- [[Inkling]]
- [[Implications of Large-Scale Test-Time Compute]]
