---
Source URL: https://openai.com/index/gpt-5-system-card/
Fetched via: WebFetch (curl returns 403 on openai.com/index/*)
Date: August 7, 2025
---

# GPT‑5 System Card

GPT‑5 is a unified system with a smart and fast model that answers most questions, a deeper reasoning model for harder problems, and a real-time router that quickly decides which model to use based on conversation type, complexity, tool needs, and explicit intent (for example, if a user says "think hard about this" in the prompt). The router is continuously trained on real signals, including when users switch models, preference rates for responses, and measured correctness, improving over time. Once usage limits are reached, a mini version of each model handles remaining queries. In the near future, OpenAI plans to integrate these capabilities into a single model.

In this system card, the fast, high-throughput models are labeled gpt-5-main and gpt-5-main-mini, and the thinking models are gpt-5-thinking and gpt-5-thinking-mini. In the API, direct access is provided to the thinking model, its mini version, and an even smaller and faster nano version made for developers (gpt-5-thinking-nano). In ChatGPT, access to gpt-5-thinking is also provided using a setting that makes use of parallel test time compute, referred to as gpt-5-thinking-pro.

Model succession mapping:

| Previous model | GPT‑5 model |
| --- | --- |
| GPT‑4o | gpt-5-main |
| GPT‑4o‑mini | gpt-5-main-mini |
| OpenAI o3 | gpt-5-thinking |
| OpenAI o4-mini | gpt-5-thinking-mini |
| GPT‑4.1‑nano | gpt-5-thinking-nano |
| OpenAI o3 Pro | gpt-5-thinking-pro |

This system card focuses primarily on gpt-5-thinking and gpt-5-main, with evaluations for other models in the appendix. All GPT‑5 models feature safe-completions, OpenAI's approach to safety training to prevent disallowed content.

Similarly to ChatGPT agent, OpenAI decided to treat gpt-5-thinking as High capability in the Biological and Chemical domain under the Preparedness Framework, activating the associated safeguards. While there is no definitive evidence that this model could meaningfully help a novice create severe biological harm (OpenAI's defined threshold for High capability), OpenAI chose to take a precautionary approach.
