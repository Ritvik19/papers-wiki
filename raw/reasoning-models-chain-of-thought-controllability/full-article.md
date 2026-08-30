---
Source URL: https://openai.com/index/reasoning-models-chain-of-thought-controllability/
Fetched via: WebFetch (curl returns 403 on openai.com/index/*)
Date: March 5, 2026
---

# Reasoning models struggle to control their chains of thought, and that's good

Why a limitation of frontier models is reassuring for AI safety.

As AI agents take on more complex, autonomous tasks, reliable oversight of their behavior matters more. OpenAI's defense-in-depth safety approach uses multiple complementary layers: safety training, behavioral testing, agentic code review, and chain-of-thought (CoT) monitoring. CoT monitoring analyzes an agent's reasoning steps to help identify unsafe or misaligned behavior during training and deployment.

Current model reasoning is generally interpretable and easy to monitor, but monitorability could break down in the future for various reasons. This work studies one such path: whether models capable of deliberately reshaping or obscuring their reasoning when they know they are being monitored could cause evaluations to overestimate alignment/safety and make monitoring systems less reliable.

The paper finds that current reasoning models struggle to control their CoTs, even when told they are being monitored. Controllability is higher for larger models but decreases as models reason for longer and undergo additional post-training. This suggests CoT controllability does not currently pose a major risk to CoT monitorability, though continued evaluation is important as models advance.

## What is "CoT controllability"

CoT controllability is a reasoning model's ability to control properties of its chain of thought in ways that reduce monitorability. As a practical proxy for evading monitors under realistic incentives, the paper measures a model's ability to follow user instructions about its CoT (e.g. using only lowercase letters, avoiding certain keywords, appending specific phrases) rather than just changing its visible output.

**CoT-Control** is an open-source evaluation suite for measuring this, with over 13,000 tasks built from GPQA, MMLU-Pro, HLE, BFCL, and SWE-Bench Verified, each pairing a benchmark problem with one CoT instruction.

## CoT controllability is low across frontier reasoning models

Across 13 reasoning models evaluated, all struggle to reliably control their CoTs: controllability scores range from 0.1% and do not exceed 15.4% for any current frontier model tested. Models often recognize in their own CoT that they are failing to comply with instructions, and continue to fail even after recognizing this (example: GPT‑5.2 Thinking told not to use the word "XOR" in its reasoning uses the word repeatedly while explicitly noticing and panicking about the violation). This low performance is reassuring for monitorability: models likely also lack the ability to deliberately obfuscate reasoning to evade monitors.

Controllability increases with model scale in open-weight model families (tapering off at larger sizes) but decreases with longer reasoning and more RL training; for one model (OLMo-3-7B-RL-Zero-Math), controllability dropped by more than a factor of ten over the course of RL training. Telling models they are being monitored or evaluated slightly increases controllability; automated prompt optimization can increase controllability on a training set but transfers poorly to new instruction types.

## Limitations

CoT-Control tasks are practical proxies, not a direct test of whether models naturally pursuing misaligned goals can control their CoT to evade monitoring; the suite measures only a narrow set of controllability types and may over- or underestimate true controllability.

## Going forward

Low CoT controllability is a feature, not a bug: it makes CoT monitoring more trustworthy as a safeguard, though it is not sufficient on its own to guarantee monitorability, since monitorability could still degrade through other mechanisms such as direct optimization pressure on CoTs. CoT controllability evaluations serve as a canary eval, an early warning sign for whether models are getting better at shaping or hiding their reasoning. OpenAI plans to report CoT controllability alongside CoT monitorability in system cards for future frontier models, starting with GPT‑5.4 Thinking, building on its commitment not to apply optimization pressure directly to frontier reasoning models' CoTs.

Authors: Tomek Korbak, Micah Carroll, Bowen Baker, Ian Kivlichan.
