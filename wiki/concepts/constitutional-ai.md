# Constitutional AI

**Type**: concept  
**Tags**: #concept

## Overview

**Constitutional AI (CAI)** is Anthropic's alignment methodology for training AI systems to be **helpful, honest, and harmless** using explicit principles (a "constitution") rather than relying solely on human feedback labels. It underpins the Claude model family from the first **Introducing Claude** announcement (Mar 2023) and is referenced across safety evaluations, model cards, and the [[Responsible Scaling Policy]].

## Appearances

- [[Claude Models]] — HHH framing at launch; Constitutional AI cited in Claude 3 responsible-design section.
- [[Safety and Alignment]] — Core Anthropic alignment approach alongside RLHF and red-teaming.
- [[Anthropic]] — Company research pillar; public constitution and transparency docs.

## Notes

- CAI combines supervised revision and RL from AI feedback (RLAIF) guided by constitutional principles.
- Claude 3 models were tuned with Constitutional AI and showed reduced bias (BBQ) and fewer unnecessary refusals vs prior generations.
- Distinct from generic RLHF: emphasizes principle-guided self-critique and revision.

## Related

- [[Claude Models]]
- [[Anthropic]]
- [[Responsible Scaling Policy]]
- [[Safety and Alignment]]
- [[RLHF]]
