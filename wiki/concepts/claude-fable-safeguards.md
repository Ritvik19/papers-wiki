# Claude Fable Safeguards

**Type**: concept  
**Tags**: #concept

## Overview

**Claude Fable safeguards** are Anthropic's mechanism for releasing Mythos-class capability to general users while limiting dual-use risk in cybersecurity and biology. **Claude Fable 5** shares the same underlying weights as **Claude Mythos 5**, but queries in high-risk domains are automatically routed to **Claude Opus 4.8** instead of exposing full Mythos-level performance.

## Appearances

- [[Claude Models]] — Fable 5 / Mythos 5 joint launch (June 2026); safeguards enable GA of Mythos-class general capability.
- [[Safety and Alignment]] — dual-use routing and conservative classifier tuning.

## Notes

- Safeguards are tuned conservatively at launch; Anthropic reports they trigger in <5% of sessions on average but can catch benign requests (false positives).
- Mythos 5 without these domain blocks is available only through trusted-access programs (e.g., [[Project Glasswing]] for cyberdefense).
- Mythos 5 usage requires 30-day data retention for safety monitoring.

## Related

- [[Responsible Scaling Policy]] — Anthropic's ASL deployment framework.
- [[Constitutional AI]] — broader alignment methodology.
- [[Anthropic]] — model provider.
- [[Project Glasswing]] — trusted-access cyberdefense deployment channel.
