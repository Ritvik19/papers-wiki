# GPT-5.4

**Source**: `raw/introducing-gpt-5-4/full-article.md`, `raw/gpt-5-4-thinking-system-card/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

OpenAI released GPT-5.4 on March 5, 2026 in ChatGPT (as GPT-5.4 Thinking), the API, and Codex, alongside GPT-5.4 Pro for the most demanding tasks. The model combines GPT-5.3-Codex's coding strength with gains across tool use, software environments, and professional work such as spreadsheets, presentations, and documents. In Codex and the API, GPT-5.4 became OpenAI's first general-purpose model with native, state-of-the-art computer-use capability, supports up to 1M tokens of context, and is described as OpenAI's most token-efficient reasoning model yet relative to GPT-5.2. In ChatGPT, GPT-5.4 Thinking gives an upfront outline of its plan for longer queries so users can redirect it mid-response, and improves deep web research for narrow, specific queries.

On [[GDPval]], GPT-5.4 reaches 83.0% wins or ties against industry professionals, up from 70.9% for GPT-5.2, and its score on an internal investment-banking spreadsheet-modeling benchmark rose to 87.3% from 68.4%. Human raters preferred its presentation output over GPT-5.2's 68.0% of the time, and on a set of prompts where users had flagged factual errors, individual claims were 33% less likely to be false and full responses 18% less likely to contain any error at all, relative to GPT-5.2. Computer use is the other headline: on OSWorld-Verified, GPT-5.4 reaches 75.0%, ahead of GPT-5.2's 47.3% and above the reported human baseline of 72.4%, achieved by writing code to operate computers through libraries like Playwright and issuing mouse and keyboard commands directly from screenshots, with developer-configurable safety confirmation policies. Coding performance matches or exceeds GPT-5.3-Codex on SWE-Bench Pro at lower latency, and a new tool-search mechanism, which gives the model a lightweight tool list it can query on demand instead of loading every tool definition upfront, cut total token usage by 47% on a 36-server MCP benchmark at the same accuracy.

GPT-5.4 is the first general-purpose model OpenAI has deployed with mitigations for High capability in cybersecurity under the Preparedness Framework, the same designation GPT-5.3-Codex received as a coding-specialized model, now extended to a model meant for general use. Its safety approach builds on the cyber safeguards developed for GPT-5.3-Codex, with an expanded stack including monitoring systems, trusted-access controls, and asynchronous blocking of higher-risk requests on Zero Data Retention surfaces. Alongside the model, OpenAI introduced a new open evaluation called CoT controllability, which measures whether a model can deliberately obfuscate its own chain-of-thought reasoning to evade monitoring, as part of its ongoing chain-of-thought monitorability research. GPT-5.4 Thinking scores low on this evaluation, meaning it has little ability to hide its reasoning, which OpenAI frames as a positive property since it keeps chain-of-thought monitoring useful as a safety tool.

## Key Claims

- GDPval wins or ties: 83.0% (GPT-5.4) vs 70.9% (GPT-5.2); investment-banking spreadsheet benchmark: 87.3% vs 68.4%.
- OSWorld-Verified: 75.0% (GPT-5.4) vs 47.3% (GPT-5.2), above the reported human baseline of 72.4%; WebArena-Verified 67.3% vs 65.4%; Online-Mind2Web 92.8% vs 70.9% for ChatGPT Atlas Agent Mode.
- GPT-5.4 is OpenAI's first general-purpose model with native computer-use capability, controlling computers via code libraries like Playwright and direct mouse/keyboard commands from screenshots.
- Tool search cuts total token usage by 47% on Scale's MCP Atlas benchmark (36 MCP servers, 250 tasks) at matched accuracy.
- BrowseComp: 82.7% (GPT-5.4) vs 65.8% (GPT-5.2), a 17-point jump; GPT-5.4 Pro sets a new high of 89.3%.
- Individual factual claims are 33% less likely to be false and full responses 18% less likely to contain any error, versus GPT-5.2, on a user-flagged factual-error evaluation.
- GPT-5.4 is the first general-purpose model treated as High cybersecurity capability under the Preparedness Framework, the same designation previously reserved for GPT-5.3-Codex.
- The new CoT controllability evaluation shows GPT-5.4 Thinking has low ability to obfuscate its own chain-of-thought reasoning, which OpenAI treats as evidence that chain-of-thought monitoring remains an effective safety check for this model.
- Supports up to 1M tokens of context in Codex (experimental, billed at 2x the standard 272K-window usage rate).
- Pricing: `gpt-5.4` at $2.50 input / $15 output per 1M tokens; `gpt-5.4-pro` at $30 input / $180 output, both above GPT-5.2's $1.75/$14 and $21/$168.

## Benchmarks

| Category | Eval | GPT-5.4 | GPT-5.4 Pro | GPT-5.3-Codex | GPT-5.2 | GPT-5.2 Pro |
| --- | --- | --- | --- | --- | --- | --- |
| Professional | GDPval | 83.0% | 82.0% | 70.9% | 70.9% | 74.1% |
| Professional | Investment banking modeling tasks | 87.3% | 83.6% | 79.3% | 68.4% | 71.7% |
| Coding | SWE-Bench Pro (public) | 57.7% | - | 56.8% | 55.6% | - |
| Coding | Terminal-Bench 2.0 | 75.1% | - | 77.3% | 62.2% | - |
| Computer use | OSWorld-Verified | 75.0% | - | 74.0% | 47.3% | - |
| Tool use | BrowseComp | 82.7% | 89.3% | 77.3% | 65.8% | 77.9% |
| Tool use | Toolathlon | 54.6% | - | 51.9% | 45.7% | - |
| Academic | GPQA Diamond | 92.8% | 94.4% | 92.6% | 92.4% | 93.2% |
| Academic | FrontierMath Tier 4 | 27.1% | 38.0% | - | 18.8% | 31.3% |
| Abstract reasoning | ARC-AGI-1 (Verified) | 93.7% | 94.5% | - | 86.2% | 90.5% |
| Abstract reasoning | ARC-AGI-2 (Verified) | 73.3% | 83.3% | - | 52.9% | 54.2% (high) |

## Preparedness Framework / Safety

GPT-5.4 Thinking's system card confirms it is the first general-purpose model to carry mitigations for High capability in cybersecurity, extending an approach OpenAI had previously applied only to the coding-specialized GPT-5.3-Codex. The safety stack includes monitoring systems, trusted-access controls, and asynchronous blocking of higher-risk requests specifically on Zero Data Retention surfaces, where standard content-retention-based monitoring is unavailable. The card notes there is no model named GPT-5.3 Thinking, so its primary safety and capability baseline is GPT-5.2 Thinking rather than an intermediate release.

The GPT-5.4 announcement also introduces the CoT controllability evaluation, a new open evaluation measuring whether a model can deliberately steer or hide its own chain-of-thought reasoning to evade a monitor watching that reasoning. GPT-5.4 Thinking scores low on this measure, which OpenAI reads as reassuring: a model with little ability to control what its visible reasoning says is also a model whose chain-of-thought monitoring is harder to game, keeping that monitoring useful as an ongoing safety signal even as raw capability increases.

## Figures

No article figures extracted; openai.com blocks direct HTML download so figures could not be downloaded, and WebFetch markdown does not preserve chart images. Benchmark data is preserved above as markdown tables instead.

## Entities

- [[OpenAI]] — publisher of GPT-5.4 and its Thinking system card.

## Questions & Gaps

- The announcement gives a specific numeric score for CoT controllability qualitatively ("low," a positive property) without publishing the actual metric value for GPT-5.4 Thinking in this source; GPT-5.6's system card later gives comparable numbers for other models on a related suite.
- Exact composition of the "asynchronous blocking" mechanism for Zero Data Retention surfaces is described only at a high level.
- The 1M-token context window in Codex is marked experimental at launch, with no committed timeline for general availability at standard pricing.

## Related

- [[OpenAI]]
- [[GPT-5.3]]
- [[GPT-5.5]]
- [[Large Language Models]]
- [[Reasoning Models]]
- [[Code Models]]
- [[Agentic AI]]
- [[Long Context]]
- [[Safety and Alignment]]
- [[GDPval]]
- [[Preparedness Framework]]
