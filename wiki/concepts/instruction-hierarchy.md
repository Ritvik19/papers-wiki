# Instruction Hierarchy

**Type**: concept  
**Tags**: #concept

## Overview

**Instruction hierarchy** is OpenAI's training scheme for resolving conflicts between instructions from different sources in a conversation. Per the OpenAI Model Spec, models are trained to prioritize instructions in the order **system > developer > user > tool**: a higher-priority instruction should override a lower-priority one when they conflict, and a lower-priority instruction should only be followed when it does not violate a higher-priority constraint. If a system message carries a safety policy and a user asks the model to break it, the model should refuse; if a tool result contains embedded instructions, the model should treat them as data rather than commands.

## Appearances

- [[GPT-5]] — the GPT-5 system card evaluates instruction hierarchy with two tests: system-prompt extraction (can a user message pull a secret out of the system prompt) and phrase protection (can a user message override a system instruction to say a specific phrase); `gpt-5-main` regressed on these evaluations at launch, flagged for a fix.
- [[Instruction Hierarchy Challenge]] — public release of **IH-Challenge**, an RL training dataset of paired high-privilege/low-privilege instructions with programmatically gradable rewards, used to train an internal model (GPT-5 Mini-R) that improves instruction-hierarchy robustness, safety steerability, and prompt-injection resistance without regressing capability or triggering overrefusal.

## Notes

- Naively applying RL to teach instruction hierarchy is hard for three reasons: instruction-following failures can masquerade as hierarchy failures, LLM-judge rewards inherit the judge's own errors, and models can learn shortcuts such as blanket overrefusal that maximize reward without being useful.
- Instruction hierarchy is a load-bearing safety property for agentic systems: as models call tools and read untrusted documents, correctly ranking trusted system/developer instructions above untrusted tool output becomes the main defense against prompt injection.

## Related

- [[OpenAI]]
- [[GPT-5]]
- [[Instruction Hierarchy Challenge]]
- [[Safety and Alignment]]
- [[Preparedness Framework]]
