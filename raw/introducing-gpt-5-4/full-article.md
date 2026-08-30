---
Source URL: https://openai.com/index/introducing-gpt-5-4/
Fetched via: WebFetch (curl returns 403 on openai.com/index/*)
Date: March 5, 2026
---

# Introducing GPT‑5.4

Designed for professional work.

GPT‑5.4 released in ChatGPT (as GPT‑5.4 Thinking), the API, and Codex: OpenAI's most capable and efficient frontier model for professional work at the time, plus GPT‑5.4 Pro for maximum performance on complex tasks. It brings together recent advances in reasoning, coding, and agentic workflows into a single model, incorporating the coding capabilities of GPT‑5.3‑Codex while improving work across tools, software environments, and professional tasks (spreadsheets, presentations, documents).

In ChatGPT, GPT‑5.4 Thinking provides an upfront plan of its thinking so users can adjust course mid-response, and improves deep web research for highly specific queries. In Codex and the API, GPT‑5.4 is the first general-purpose model with native, state-of-the-art computer-use capabilities, supports up to 1M tokens of context, and improves tool search across large tool ecosystems. It is OpenAI's most token-efficient reasoning model yet relative to GPT‑5.2.

| Eval | GPT‑5.4 | GPT‑5.3‑Codex | GPT‑5.2 |
| --- | --- | --- | --- |
| GDPval (wins or ties) | 83.0% | 70.9% | 70.9% |
| SWE-Bench Pro (Public) | 57.7% | 56.8% | 55.6% |
| OSWorld-Verified | 75.0% | 74.0%* | 47.3% |
| Toolathlon | 54.6% | 51.9% | 46.3% |
| BrowseComp | 82.7% | 77.3% | 65.8% |

*GPT‑5.3‑Codex achieves 74.0% with a newly introduced API parameter that preserves original image resolution (previously reported as 64.7%).

## Knowledge work

On GDPval (well-specified knowledge work across 44 occupations), GPT‑5.4 achieves a new state of the art, matching or exceeding industry professionals in 83.0% of comparisons versus 70.9% for GPT‑5.2. On an internal junior investment-banking analyst spreadsheet-modeling benchmark, GPT‑5.4 scores 87.3% versus 68.4% for GPT‑5.2. On presentation prompts, human raters preferred GPT‑5.4 output 68.0% of the time over GPT‑5.2. On a set of de-identified prompts where users flagged factual errors, GPT‑5.4's individual claims are 33% less likely to be false and full responses 18% less likely to contain any errors, relative to GPT‑5.2. Mercor's CEO reported GPT‑5.4 topping their APEX-Agents benchmark; Harvey's Head of Applied Research reported a 91% score on BigLaw Bench.

## Computer use and vision

GPT‑5.4 is OpenAI's first general-purpose model with native computer-use capabilities: writing code to operate computers via libraries like Playwright, and issuing mouse/keyboard commands from screenshots, with developer-steerable safety confirmation policies. On OSWorld-Verified, GPT‑5.4 achieves 75.0% (versus GPT‑5.2's 47.3%), surpassing human performance (72.4%). On WebArena-Verified, 67.3% (vs 65.4%). On Online-Mind2Web, 92.8% (vs ChatGPT Atlas Agent Mode's 70.9%).

Improved visual perception: MMMU-Pro 81.2% without tools (vs 79.5%); OmniDocBench error 0.109 (vs 0.140 for GPT‑5.2). New `original` image input detail level supports full-fidelity perception up to 10.24M total pixels or 6000px max dimension; `high` now supports up to 2.56M pixels or 2048px max dimension. Mainstay reported 95% first-attempt success (100% within three attempts) on ~30K HOA/property-tax portal computer-use evals, ~3x faster and ~70% fewer tokens than prior CUA models.

## Coding

Matches or outperforms GPT‑5.3‑Codex on SWE-Bench Pro while lower latency across reasoning efforts. `/fast` mode in Codex delivers up to 1.5x faster token velocity with the same intelligence. Released an experimental Codex skill, "Playwright (Interactive)," letting Codex visually debug web/Electron apps, including testing an app it's building as it builds it. Cursor's VP of Developer Education reported GPT‑5.4 as the leader on internal benchmarks, more natural and assertive, proactive at parallelizing work.

## Tool use

**Tool search**: instead of including all tool definitions upfront (which can add tens of thousands of tokens per request), GPT‑5.4 receives a lightweight tool list and can look up a tool's definition when needed. On 250 tasks from Scale's MCP Atlas benchmark (36 MCP servers), tool search reduced total token usage by 47% at the same accuracy.

**Agentic tool calling**: higher accuracy in fewer turns on Toolathlon versus GPT‑5.2. Further improvements at `reasoning.effort=None` for latency-sensitive use cases (Tau2-bench).

**Web search**: on BrowseComp, GPT‑5.4 leaps 17 percentage points over GPT‑5.2; GPT‑5.4 Pro sets a new state of the art of 89.3%. Zapier's CEO reported GPT‑5.4 xhigh as the new state of the art for multi-step tool use on their internal benchmarks.

## Steerability

GPT‑5.4 Thinking in ChatGPT outlines its work with a preamble for longer queries, and supports mid-response instruction adjustment without restarting. It can think longer on difficult tasks while maintaining stronger awareness of earlier conversation steps.

## Safety

GPT‑5.4 is treated as **High cyber capability** under the Preparedness Framework (same as GPT‑5.3‑Codex), deployed with an expanded cyber safety stack: monitoring systems, trusted access controls, asynchronous blocking for higher-risk requests on Zero Data Retention (ZDR) surfaces.

OpenAI introduced a new open-source evaluation, **CoT controllability**, measuring whether models can deliberately obfuscate their reasoning to evade monitoring, as part of ongoing chain-of-thought (CoT) monitorability research. GPT‑5.4 Thinking's ability to control its CoT is low, a positive property for safety: it suggests the model lacks the ability to hide its reasoning, so CoT monitoring remains an effective safety tool.

## Availability and pricing

Rolling out across ChatGPT and Codex; available in the API as `gpt-5.4` and `gpt-5.4-pro`. GPT‑5.4 Thinking replaces GPT‑5.2 Thinking for Plus, Team, and Pro users (GPT‑5.2 Thinking retired June 5, 2026). Includes experimental support in Codex for the 1M context window (2x usage rate beyond the standard 272K window).

| API model | Input price | Cached input price | Output price |
| --- | --- | --- | --- |
| gpt-5.2 | $1.75/M | $0.175/M | $14/M |
| gpt-5.4 | $2.50/M | $0.25/M | $15/M |
| gpt-5.2-pro | $21/M | - | $168/M |
| gpt-5.4-pro | $30/M | - | $180/M |

## Evaluations (selected)

| Category | Eval | GPT‑5.4 | GPT‑5.4 Pro | GPT‑5.3-Codex | GPT‑5.2 | GPT‑5.2 Pro |
| --- | --- | --- | --- | --- | --- | --- |
| Professional | GDPval | 83.0% | 82.0% | 70.9% | 70.9% | 74.1% |
| Professional | Investment Banking Modeling Tasks | 87.3% | 83.6% | 79.3% | 68.4% | 71.7% |
| Coding | SWE-Bench Pro (Public) | 57.7% | — | 56.8% | 55.6% | — |
| Coding | Terminal-Bench 2.0 | 75.1% | — | 77.3% | 62.2% | — |
| Computer use | OSWorld-Verified | 75.0% | — | 74.0% | 47.3% | — |
| Tool use | BrowseComp | 82.7% | 89.3% | 77.3% | 65.8% | 77.9% |
| Tool use | Toolathlon | 54.6% | — | 51.9% | 45.7% | — |
| Academic | GPQA Diamond | 92.8% | 94.4% | 92.6% | 92.4% | 93.2% |
| Academic | FrontierMath Tier 4 | 27.1% | 38.0% | — | 18.8% | 31.3% |
| Long context | OpenAI MRCR v2 8-needle 512K–1M | 36.6% | — | — | — | — |
| Abstract reasoning | ARC-AGI-1 (Verified) | 93.7% | 94.5% | — | 86.2% | 90.5% |
| Abstract reasoning | ARC-AGI-2 (Verified) | 73.3% | 83.3% | — | 52.9% | 54.2% (high) |
