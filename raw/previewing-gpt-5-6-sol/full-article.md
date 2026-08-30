---
Source URL: https://openai.com/index/previewing-gpt-5-6-sol/
Fetched via: WebFetch (curl returns 403 on openai.com/index/*)
Date: June 26, 2026
---

# Previewing GPT‑5.6 Sol: a next-generation model

A limited preview of the GPT‑5.6 series: **Sol** (flagship), **Terra** (balanced, everyday work), and **Luna** (fast, affordable). Terra has competitive performance to GPT‑5.5 while being 2x cheaper; Luna brings strong capability at OpenAI's lowest cost. This introduces a new naming system: the number identifies the generation, while Sol/Terra/Luna identify durable capability tiers that can advance on their own cadence.

GPT‑5.6 Sol launches with OpenAI's most robust safety stack to date: strengthened protections for higher-risk activity, sensitive cyber requests, and repeated misuse, with multiple weeks of pressure-testing against real-world attacks.

As part of ongoing engagement with the U.S. government, OpenAI previewed plans and capabilities ahead of launch. At the government's request, the release starts with a limited preview for a small group of trusted partners (shared with the government) before broader release, while OpenAI works with the Administration on a cyber Executive Order framework and repeatable process for future releases. OpenAI states it does not believe this kind of government access process should become the long-term default.

## Capabilities

GPT‑5.6 introduces a new `max` reasoning effort and a new `ultra` mode that uses subagents to accelerate complex work beyond a single agent.

- **Coding**: sets a new state of the art on Terminal-Bench 2.1.
- **Biology**: on GeneBench v1 (long-horizon genomics/quantitative-biology analyses), stronger results than GPT‑5.5 using fewer tokens.
- **Cybersecurity**: OpenAI's most capable model yet for cybersecurity, shifting the performance-efficiency frontier for long-horizon security tasks (vulnerability research, exploitation). On ExploitBench, competitive with Mythos Preview using ~1/3 the output tokens. On ExploitGym (a UC Berkeley benchmark built with OpenAI and other frontier labs), Sol/Terra/Luna all show strong improvements in cyber capability as reasoning increases.

## Stronger cyber capabilities with stronger safeguards

Safeguards are configured to each model's capability, designed to hold up to real-world adversarial pressure while preserving legitimate work (code review, vulnerability research, patch development, debugging, security education, defensive testing). GPT‑5.6 Sol is better at helping find and fix vulnerabilities than at reliably carrying out end-to-end attacks.

GPT‑5.6 Sol does **not** cross the Cyber Critical threshold under the Preparedness Framework. In evaluations involving Chromium and Firefox, it identified bugs and exploitation primitives but did not autonomously produce a functional full-chain exploit under the conditions tested. OpenAI pairs the model's step change in capability with stronger safeguards and phased release given that benchmark thresholds cannot capture every real-world use.

## A layered safeguard stack

Layered safeguards vary by model: protections trained into the model (refusing prohibited cyber assistance, including disguised intent/jailbreaks), real-time cyber/biology misuse classifiers during generation (which can pause generation for larger-model review on higher-risk cases), account-level review across conversations, differentiated access, monitoring, and enforcement. During the preview, some legitimate dual-use security work may be blocked or delayed as OpenAI tunes the safeguards.

## Improving robustness with automated red-teaming

OpenAI dedicated over 700,000 A100-equivalent GPU hours to automated red-teaming aimed at finding universal jailbreaks (attacks generalizing across many prompts/contexts), complemented by third-party human expert red-teaming continuing through the preview period. Maintains a rapid-response process to reproduce, assess, prioritize, and remediate newly discovered jailbreaks.

## Availability and pricing

Initially available through the API and Codex to a select group of trusted partners/organizations, with broader ChatGPT/Codex/API availability planned soon.

Pricing per 1M tokens: Sol $5 input / $30 output; Terra $2.50 input / $15 output; Luna $1 input / $6 output. Introduces more predictable prompt caching (explicit cache breakpoints, 30-minute minimum cache life); cache writes billed at 1.25x the uncached input rate for GPT‑5.6+ models, cache reads keep the 90% cached-input discount. GPT‑5.6 Sol launching on Cerebras at up to 750 tokens/second in July 2026, initially limited to select customers.
