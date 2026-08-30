---
Source URL: https://openai.com/index/introducing-gpt-5-3-codex-spark/
Fetched via: WebFetch (curl returns 403 on openai.com/index/*)
Date: February 12, 2026
---

# Introducing GPT‑5.3‑Codex‑Spark

An ultra-fast model for real-time coding in Codex.

OpenAI released a research preview of GPT‑5.3‑Codex‑Spark, a smaller version of GPT‑5.3‑Codex and the first model designed for real-time coding. Codex-Spark marks the first milestone in OpenAI's partnership with Cerebras (announced January 2026). It is optimized to feel near-instant on ultra-low-latency hardware, delivering more than 1000 tokens per second while remaining highly capable for real-world coding tasks. Shared as a research preview to ChatGPT Pro users while OpenAI and Cerebras ramp up datacenter capacity.

Frontier models had shown particular strength at long-running tasks (working autonomously for hours, days, or weeks). Codex-Spark is designed specifically for working with Codex in real time: making targeted edits, reshaping logic, refining interfaces, and seeing results immediately.

At launch: 128k context window, text-only, separate rate limits from standard usage.

## Speed and intelligence

Optimized for interactive work where latency matters as much as intelligence: minimal, targeted edits by default, no automatic test running unless requested.

## Coding

Strong performance on SWE-Bench Pro and Terminal-Bench 2.0 while accomplishing tasks in a fraction of the time compared to GPT‑5.3‑Codex. Duration estimated as the sum of output generation time, prefill time, tool execution time, and network overhead.

## Latency improvements for all models

Building Codex-Spark required reducing latency across the full request-response pipeline, not just model speed: streamlined response streaming, rewritten inference-stack pieces, reworked session initialization. Introduced a persistent WebSocket connection and Responses API optimizations that reduced overhead per client/server roundtrip by 80%, per-token overhead by 30%, and time-to-first-token by 50%. The WebSocket path is enabled for Codex-Spark by default and becomes the default for all models over time.

## Powered by Cerebras

Runs on Cerebras' Wafer Scale Engine 3, added to the same production serving stack as the rest of OpenAI's fleet. GPUs remain foundational for training and broad-usage inference; Cerebras complements this for workflows demanding extremely low latency.

## Availability

Rolling out as a research preview for ChatGPT Pro users in the Codex app, CLI, and VS Code extension, plus API access for a small set of design partners. Includes the same safety training as mainline models, including cyber-relevant training; evaluated as part of standard deployment process and determined not to have a plausible chance of reaching the Preparedness Framework threshold for high capability in cybersecurity or biology.
