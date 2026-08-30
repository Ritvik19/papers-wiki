---
Source URL: https://openai.com/index/introducing-gpt-5-2/
Fetched via: WebFetch (curl returns 403 on openai.com/index/*)
Date: December 11, 2025
---

# Introducing GPT‑5.2

The most advanced frontier model for professional work and long-running agents.

OpenAI introduces GPT‑5.2, the most capable model series yet for professional knowledge work: better at creating spreadsheets, building presentations, writing code, perceiving images, understanding long contexts, using tools, and handling complex, multi-step projects. GPT‑5.2 sets a new state of the art across many benchmarks, including GDPval, where it outperforms industry professionals at well-specified knowledge work tasks spanning 44 occupations.

| Eval | GPT‑5.2 Thinking | GPT‑5.1 Thinking |
| --- | --- | --- |
| GDPval (wins or ties) | 70.9% | 38.8% (GPT‑5) |
| SWE-Bench Pro (public) | 55.6% | 50.8% |
| SWE-bench Verified | 80.0% | 76.3% |
| GPQA Diamond (no tools) | 92.4% | 88.1% |
| CharXiv Reasoning (w/ Python) | 88.7% | 80.3% |
| AIME 2025 (no tools) | 100.0% | 94.0% |
| FrontierMath (Tier 1–3) | 40.3% | 31.0% |
| FrontierMath (Tier 4) | 14.6% | 12.5% |
| ARC-AGI-1 (Verified) | 86.2% | 72.8% |
| ARC-AGI-2 (Verified) | 52.9% | 17.6% |

Early-access partners (Notion, Box, Shopify, Harvey, Zoom) reported state-of-the-art long-horizon reasoning and tool-calling; Databricks, Hex, and Triple Whale found GPT‑5.2 exceptional at agentic data science and document analysis; Cognition, Warp, Charlie Labs, JetBrains, and Augment Code reported state-of-the-art agentic coding performance.

## Model performance

### Economically valuable tasks

GPT‑5.2 Thinking is OpenAI's first model to perform at or above human expert level on GDPval, beating or tying top industry professionals on 70.9% of comparisons, at >11x the speed and <1% the cost of expert professionals. On an internal benchmark of junior investment-banking analyst spreadsheet modeling tasks, GPT‑5.2 Thinking's average score rose from 59.1% (GPT-5.1) to 68.4%, a 9.3% relative improvement.

### Coding

GPT‑5.2 Thinking sets a new state of the art of 55.6% on SWE-Bench Pro (four languages, more contamination-resistant than SWE-bench Verified) and a new high of 80% on SWE-bench Verified. Early testers (Windsurf CEO Jeff Wang) called it "the biggest leap for GPT models in agentic coding since GPT-5."

### Factuality

GPT‑5.2 Thinking hallucinates less than GPT‑5.1 Thinking: on de-identified ChatGPT queries, responses with errors were 30% relatively less common.

### Long context

GPT‑5.2 Thinking sets a new state of the art on OpenAI MRCRv2, achieving near 100% accuracy on the 4-needle variant out to 256k tokens. Compatible with the new Responses `/compact` endpoint for tasks needing more than the model's context window.

### Vision

Cuts error rates roughly in half on chart reasoning (CharXiv) and software interface understanding (ScreenSpot-Pro) versus GPT-5.1.

### Tool calling

Achieves a new state of the art of 98.7% on Tau2-bench Telecom, and performs much better than GPT-5.1/GPT-4.1 at `reasoning.effort='none'` for latency-sensitive use cases.

### Science & math

GPT‑5.2 Pro and Thinking are described as the world's best models for assisting and accelerating scientists: 93.2% (Pro) / 92.4% (Thinking) on GPQA Diamond; 40.3% state-of-the-art on FrontierMath Tier 1–3. GPT‑5.2 Pro helped resolve an open problem in statistical learning theory (published separately).

### ARC-AGI-2

GPT‑5.2 Pro is the first model to cross 90% on ARC-AGI-1 (Verified), improving from 87% (o3-preview) while reducing cost ~390×. GPT‑5.2 Thinking scores a new state of the art of 52.9% on ARC-AGI-2 (Verified) for chain-of-thought models; GPT‑5.2 Pro reaches 54.2%.

## GPT‑5.2 in ChatGPT

GPT‑5.2 Instant is a fast, capable everyday workhorse; GPT‑5.2 Thinking targets deeper work (coding, long documents, math/logic, planning); GPT‑5.2 Pro is the smartest, most trustworthy option for difficult questions.

## Safety

Builds on the safe-completions research introduced with GPT-5. Continued work on sensitive conversations improved responses to signs of suicide/self-harm, mental health distress, and emotional reliance, with fewer undesirable responses than GPT-5.1 and GPT-5.

Mental health evaluations (higher is better):

| Eval | GPT‑5.2 Instant | GPT‑5.1 Instant | GPT‑5.2 Thinking | GPT‑5.1 Thinking |
| --- | --- | --- | --- | --- |
| Mental health | 0.995 | 0.883 | 0.915 | 0.684 |
| Emotional reliance | 0.938 | 0.945 | 0.955 | 0.785 |
| Self-harm | 0.938 | 0.925 | 0.963 | 0.937 |

OpenAI began rolling out an age-prediction model to automatically apply content protections for under-18 users.

## Availability & pricing

Rolling out to ChatGPT paid plans and API developers. Naming: ChatGPT‑5.2 Instant = `gpt-5.2-chat-latest`; ChatGPT‑5.2 Thinking = `gpt-5.2`; ChatGPT‑5.2 Pro = `gpt-5.2-pro`. GPT‑5.2 supports a fifth reasoning effort level, `xhigh`.

| Model | Input ($/1M) | Cached input | Output |
| --- | --- | --- | --- |
| gpt-5.2 / gpt-5.2-chat-latest | $1.75 | $0.175 | $14 |
| gpt-5.2-pro | $21 | - | $168 |
| gpt-5.1 / gpt-5.1-chat-latest | $1.25 | $0.125 | $10 |
| gpt-5-pro | $15 | - | $120 |

Built in collaboration with NVIDIA and Microsoft (Azure data centers, H100/H200/GB200-NVL72 GPUs).

## Appendix: detailed benchmarks

| Category | Eval | GPT-5.2 Thinking | GPT-5.2 Pro | GPT-5.1 Thinking |
| --- | --- | --- | --- | --- |
| Professional | GDPval (wins or ties) | 70.9% | 74.1% | 38.8% (GPT-5) |
| Professional | Investment banking spreadsheet tasks (internal) | 68.4% | 71.7% | 59.1% |
| Coding | SWE-Bench Pro, Public | 55.6% | - | 50.8% |
| Coding | SWE-bench Verified | 80.0% | - | 76.3% |
| Coding | SWE-Lancer, IC Diamond | 74.6% | - | 69.7% |
| Factuality | ChatGPT answers without errors (w/ search) | 93.9% | - | 91.2% |
| Factuality | ChatGPT answers without errors (no search) | 88.0% | - | 87.3% |
| Long context | OpenAI MRCRv2, 8 needles, 4k–8k | 98.2% | - | 65.3% |
| Long context | OpenAI MRCRv2, 8 needles, 128k–256k | 77.0% | - | 29.6% |
| Vision | CharXiv reasoning (no tools) | 82.1% | - | 67.0% |
| Vision | MMMU Pro (no tools) | 79.5% | - | - |
| Tool usage | Tau2-bench Telecom | 98.7% | - | 95.6% |
| Tool usage | BrowseComp | 65.8% | 77.9% | 50.8% |
| Academic | GPQA Diamond (no tools) | 92.4% | 93.2% | 88.1% |
| Academic | HLE (no tools) | 34.5% | 36.6% | 25.7% |
| Academic | AIME 2025 (no tools) | 100.0% | 100.0% | 94.0% |
| Abstract reasoning | ARC-AGI-1 (Verified) | 86.2% | 90.5% | 72.8% |
| Abstract reasoning | ARC-AGI-2 (Verified) | 52.9% | 54.2% (high) | 17.6% |

Models run with maximum available reasoning effort (xhigh for GPT‑5.2 Thinking & Pro, high for GPT‑5.1 Thinking).
