# Claude Fable Safeguards

**Type**: concept  
**Tags**: #concept

## Overview

**Claude Fable safeguards** are Anthropic's mechanism for releasing Mythos-class capability to general users while limiting dual-use risk in cybersecurity and biology. **Claude Fable 5** and **Claude Fable 5.1** share weights with their Mythos counterparts, but high-risk queries are routed to Opus models instead of exposing full Mythos-level performance.

## Appearances

- [[Claude Models]] — Fable 5 / Mythos 5 (June 2026); Fable 5.1 / Mythos 5.1 (September 2026) with refined cyber safeguards.
- [[Safety and Alignment]] — dual-use routing and conservative classifier tuning.

## Notes

- **Fable 5.1 (Sep 2026)**: cyber safeguards block **60% fewer false positives** than Fable 5 launch safeguards; **vulnerability discovery** allowed on Fable but exploit generation, penetration testing, and binary vuln scanning still route to Opus.
- Biology R&D on Fable still routes to Opus; advanced biology via [[Life Sciences Verification Program]] on Mythos 5.1.
- Mythos without domain blocks available through trusted-access programs ([[Project Glasswing]], [[Cyber Verification Program]], LSVP).

## Related

- [[Responsible Scaling Policy]] — Anthropic's ASL deployment framework.
- [[Constitutional AI]] — broader alignment methodology.
- [[Anthropic]] — model provider.
- [[Project Glasswing]] — trusted-access cyberdefense deployment channel.
