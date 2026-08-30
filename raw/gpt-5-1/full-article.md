---
Source URL: https://openai.com/index/gpt-5-1/
Fetched via: WebFetch (curl returns 403 on openai.com/index/*)
Date: November 12, 2025
---

# GPT‑5.1: A smarter, more conversational ChatGPT

OpenAI is upgrading the GPT‑5 series with:

- **GPT‑5.1 Instant**: the most-used model, now warmer, more intelligent, and better at following instructions.
- **GPT‑5.1 Thinking**: the advanced reasoning model, now easier to understand and faster on simple tasks, more persistent on complex ones.

## GPT‑5.1 Instant

GPT‑5.1 Instant is now warmer by default and more conversational, often surprising testers with its playfulness while remaining clear and useful. Instruction following has also improved, so the model more reliably answers the question actually asked (e.g. following a "respond with six words" constraint).

For the first time, GPT‑5.1 Instant can use adaptive reasoning to decide when to think before responding to more challenging questions, improving accuracy while still responding quickly. This shows up in significant improvements on math and coding evaluations like AIME 2025 and Codeforces.

## GPT‑5.1 Thinking

GPT‑5.1 Thinking adapts its thinking time more precisely to the question, spending more time on complex problems and responding more quickly to simpler ones. On a representative distribution of ChatGPT tasks, GPT‑5.1 Thinking is roughly twice as fast on the fastest tasks and twice as slow on the slowest tasks compared to GPT‑5 Thinking (thinking time set to Standard for both).

GPT‑5.1 Thinking's responses are also clearer, with less jargon and fewer undefined terms, and its default tone is warmer and more empathetic.

## Rollout, routing, and naming

GPT‑5.1 Auto continues to route each query to the model best suited for it. GPT‑5.1 Instant and Thinking began rolling out to paid (Pro, Plus, Go, Business) users first, then free and logged-out users. Enterprise and Edu plans got a seven-day early-access toggle (off by default), after which GPT‑5.1 became the sole default model. GPT‑5.1 Instant is available in the API as `gpt-5.1-chat-latest`; GPT‑5.1 Thinking is released as GPT‑5.1 in the API, both with adaptive reasoning. GPT‑5 (Instant and Thinking) remained available under the legacy models dropdown for paid subscribers for three months.

This update is called GPT‑5.1 (not GPT‑6) to reflect meaningful improvements while remaining within the GPT‑5 generation; future iterative upgrades follow the same pattern.

## Making ChatGPT uniquely yours

Alongside the model upgrade, tone/style customization was refined. Default, Friendly (formerly Listener), and Efficient (formerly Robot) presets were updated, and Professional, Candid, and Quirky were added. These settings apply across all models. Cynical (formerly Cynic) and Nerdy (formerly Nerd) remained available unchanged.

OpenAI also began experimenting with finer-grained tuning of ChatGPT's characteristics directly from personalization settings, including conciseness, warmth, scannability, and emoji frequency, with ChatGPT able to proactively offer to update these preferences mid-conversation. Personalization updates now take effect across all chats immediately, including ongoing conversations (previously, changes only applied to new conversations). The updated GPT‑5.1 models are also better at adhering to custom instructions.
