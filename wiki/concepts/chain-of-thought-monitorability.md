# Chain of Thought Monitorability

**Type**: concept  
**Tags**: #concept

## Overview

**Chain-of-thought (CoT) monitorability** is the degree to which a reasoning model's visible step-by-step reasoning can be read by a human or an automated monitor to catch unsafe or misaligned behavior before it turns into an action. It is one layer of OpenAI's defense-in-depth safety approach, alongside safety training, behavioral testing, and agentic code review. Monitorability depends on the model's CoT staying legible and honest about what it is actually doing rather than being reshaped to look safe under evaluation.

## Appearances

- [[Chain of Thought Controllability]] — studies a specific threat to monitorability: whether a model can deliberately control properties of its own CoT (e.g. following instructions like "avoid this keyword" applied to its reasoning, not just its output) in ways that would let it evade a monitor. Across 13 frontier reasoning models tested with the open **CoT-Control** suite (13,000+ tasks built from GPQA, MMLU-Pro, HLE, BFCL, and SWE-Bench Verified), controllability scores stay low (0.1% to at most 15.4%), which the authors read as reassuring: current models cannot reliably reshape their own reasoning even when told they are being monitored.
- [[GPT-5.6]] — the preview system card reports CoT monitorability findings for GPT-5.6 Sol against GPT-5.5: similar overall monitorability with some per-environment regressions (Impossible Coding Tasks, Scruples) and improvements (Destructive Actions, Health Queries: Patient Opinion), generally attributed to differences in how the model verbalizes reasoning rather than a change in underlying behavior. It also reports higher CoT controllability than GPT-5.5 and GPT-5.4 Thinking on the CoT-Control suite (1.3% of long CoTs successfully controlled vs 0.4% and 0.7%), which OpenAI is monitoring as a leading indicator rather than treating as an immediate risk.
- [[A Framework for Frontier AI and the Dawning of a New Age]] — Demis Hassabis's policy proposal explicitly includes generating human-readable output tokens for reasoning as a mandated best practice under the Standards Body testing protocol.

## Notes

- Controllability tends to rise with model scale within an open-weight family (tapering off at larger sizes) but falls with longer reasoning and more RL post-training; one model (OLMo-3-7B-RL-Zero-Math) lost more than 10x its controllability over the course of RL training.
- OpenAI frames low CoT controllability as a feature rather than a limitation to fix: a model that cannot control its own CoT also cannot deliberately obfuscate it from a monitor. The company plans to report CoT controllability alongside CoT monitorability in future frontier system cards, starting with GPT-5.4 Thinking, and has committed not to apply optimization pressure directly to frontier models' CoTs.
- Monitorability can still degrade through other paths besides controllability, for example if training applies direct optimization pressure to CoT content, so OpenAI treats CoT-Control as a canary evaluation rather than a complete guarantee of monitorability.

## Related

- [[OpenAI]]
- [[Chain of Thought Controllability]]
- [[GPT-5.6]]
- [[Reasoning Models]]
- [[Safety and Alignment]]
- [[Preparedness Framework]]
- [[Standards Body for Frontier AI]]
