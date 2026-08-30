# Responsible Scaling Policy

**Type**: concept  
**Tags**: #concept

## Overview

Anthropic's **Responsible Scaling Policy (RSP)** is a framework that ties deployment safeguards to model **AI Safety Levels (ASL)** based on assessed catastrophic-risk capability. **ASL-2** applies when models pose limited CBRN or autonomy risk; **ASL-3** adds stronger classifiers and restrictions when frontier capabilities increase. Claude 3 launched at **ASL-2**; **Claude Sonnet 4.5** (Sep 2025) was released under **ASL-3** protections.

## Appearances

- [[Claude Models]] — ASL-2 (Claude 3 family); ASL-3 (Sonnet 4.5+); ASL-2 (Haiku 4.5); cyber safeguards on Opus 4.7.
- [[Anthropic]] — Governance framework for frontier model deployment.
- [[Safety and Alignment]] — Capability-triggered safety tiers and red-teaming requirements.

## Notes

- ASL thresholds are evaluated against autonomy, cyber, and CBRN misuse potential—not just benchmark scores.
- Sonnet 4.5 ASL-3 includes CBRN-related input/output classifiers with fallback to lower-risk models on false positives.
- Opus 4.7 introduces automated cyber-misuse detection blocks ahead of broader Mythos-class releases.
- **Claude Fable 5** (Jun 2026) releases Mythos-class capability under [[Claude Fable Safeguards]] with cyber/biology domain routing to Opus 4.8; **Claude Mythos 5** remains in trusted-access programs ([[Project Glasswing]]).

## Related

- [[Claude Models]]
- [[Anthropic]]
- [[Constitutional AI]]
- [[Preparedness Framework]]
- [[Standards Body for Frontier AI]]
- [[Safety and Alignment]]
