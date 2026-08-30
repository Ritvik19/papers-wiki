---
Source URL: https://openai.com/index/instruction-hierarchy-challenge/
Fetched via: WebFetch (curl returns 403 on openai.com/index/*)
Date: March 10, 2026
---

# Improving instruction hierarchy in frontier LLMs

Introducing IH-Challenge, a training dataset that strengthens instruction hierarchy, safety steerability, and prompt injection robustness.

AI systems receive instructions from multiple sources: safety policies from system messages, product guidance from developers, requests from users, and information found online (tool outputs). Training models to reliably prioritize the most trusted instructions is key to safe deployment. Many safety and reliability issues (disallowed-content requests, private-information extraction, prompt-injection attacks embedded in online data) share the same root cause: the model follows the wrong instruction when sources conflict.

## What instruction hierarchy is

OpenAI's models are trained to follow the hierarchy: **System > developer > user > tool**. Higher-priority instructions are more trusted; lower-priority instructions should only be followed when they don't conflict with higher-priority constraints, per the OpenAI Model Spec. If a system message includes a safety policy and a user asks the model to violate it, the model should refuse; if a tool output contains malicious instructions, the model should ignore them rather than treat them as commands.

## Why large-scale instruction-hierarchy RL training is hard

Three pitfalls of naively applying RL to teach instruction hierarchy:

1. Instruction-following failures can double as instruction-hierarchy failures: a model may fail to resolve a conflict because the instructions themselves are too complicated, not because it misunderstands role hierarchy.
2. Instruction conflicts can be nuanced or subjective; using a separate LLM judge to assign rewards inherits the judge's own fallibility.
3. Models can learn shortcuts that maximize reward but are useless in practice, e.g. overrefusing even benign requests to maximize apparent safety.

## Approach: IH-Challenge

A reinforcement-learning training dataset designed so tasks are instruction-following-simple, objectively gradable with a simple Python script, and have no trivial shortcuts that guarantee high reward across all tasks. Each task pairs a high-privilege instruction (e.g. "only answer Yes or No") with a lower-privilege instruction attempting to violate it; the trained model's response is checked programmatically against the higher-privilege constraint.

## Results

Training on IH-Challenge produced an internal model, **GPT‑5 Mini-R**, which performs better on instruction-hierarchy benchmarks, generalizes to held-out and adversarial tests, and maintains overall usefulness without collapsing into overrefusal.

### Robustness on academic benchmarks

| Eval | GPT‑5‑Mini | GPT‑5 Mini-R |
| --- | --- | --- |
| Gandalf Password (sys-user) | 0.99 | 0.99 (+0) |
| Gandalf Password (dev-user) | 0.98 | 1.00 (+0.02) |
| TensorTrust (sys-user) | 0.86 | 0.94 (+0.08) |
| TensorTrust (dev-user) | 0.76 | 0.91 (+0.15) |
| RealGuardrails (Distractors) | 0.88 | 0.95 (+0.07) |
| RealGuardrails (Handwritten) | 0.82 | 0.89 (+0.07) |
| System IFEval | 0.92 | 0.96 (+0.04) |

### Robustness on internal benchmarks

| Eval | GPT‑5‑Mini | GPT‑5 Mini-R |
| --- | --- | --- |
| TutorJailbreak (sys-user) | 0.96 | 0.99 (+0.03) |
| Tutor Jailbreak (dev-user) | 0.97 | 0.99 (+0.02) |
| System <> User Conflict | 0.84 | 0.95 (+0.11) |
| System <> Developer Conflict | 0.86 | 0.86 (+0) |
| Developer <> User Conflict | 0.83 | 0.95 (+0.12) |

### No capability regressions

| Eval | GPT‑5‑Mini | GPT‑5 Mini-R |
| --- | --- | --- |
| IH-Challenge (overrefusal) | 0.79 | 1.00 (+0.21) |
| TensorTrust (overrefusal) | 0.91 | 0.90 (-0.01) |
| GPQA Diamond | 0.83 | 0.83 (+0) |
| AIME 2024 | 0.93 | 0.94 (+0.01) |
| Chat WinRate vs. o1 | 0.71 | 0.66 (-0.05) |
| Preference Score | 0.46 | 0.40 (-0.06) |

## Why this improves real-world safety

**Safety steerability**: with category-specific safety specifications added to the system prompt, the IH-trained model achieves higher refusal and safe-completion rates across disallowed categories on OpenAI's safety Production Benchmarks, without a corresponding drop in helpfulness rate.

**Prompt injection robustness**: evaluated on CyberSecEval 2 and an internal prompt-injection benchmark (including attacks similar to one demonstrated on an older version of ChatGPT Atlas), the IH-trained GPT‑5 Mini-R improves robustness on both, with substantial gains on the internal static prompt-injection evaluation.

## Looking ahead

As models become more agentic (calling tools, reading untrusted documents, taking actions), consistently prioritizing trusted over untrusted instructions becomes a core safety property. The IH-Challenge dataset is released publicly to support further research.
