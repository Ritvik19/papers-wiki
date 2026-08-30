# Extended Thinking

**Type**: concept  
**Tags**: #concept

## Overview

**Extended thinking** (also **hybrid reasoning**) is Anthropic's approach where a single model can respond instantly or spend additional compute on visible, step-by-step reasoning before answering. Introduced with **Claude 3.7 Sonnet** (Feb 2025), it differs from separate "reasoning-only" model SKUs: users toggle thinking mode and control thinking token budgets via API (up to 128K tokens on 3.7; effort levels on later Opus models).

## Appearances

- [[Claude Models]] — Claude 3.7 Sonnet launch; extended to Claude 4 Opus/Sonnet; adaptive thinking + effort on Opus 4.6+.
- [[Reasoning Models]] — Hybrid reasoning as an alternative to dedicated o-series / Deep Think style models.
- [[Claude Code]] — Extended thinking improves coding, planning, and agentic tool use.

## Notes

- Thinking tokens are billed as output tokens on Claude 3.7+.
- **Adaptive thinking** (Opus 4.6): model decides when deeper reasoning helps.
- **Effort** parameter (Opus 4.5+): low/medium/high/max (and `xhigh` on 4.7) trades latency and cost vs quality.
- Anthropic optimized reasoning for real-world business tasks over competition math, per the 3.7 launch post.

## Related

- [[Claude Models]]
- [[Anthropic]]
- [[Reasoning Models]]
- [[Claude Code]]
