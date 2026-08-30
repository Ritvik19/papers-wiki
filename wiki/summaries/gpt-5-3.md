# GPT-5.3

**Source**: `raw/introducing-gpt-5-3-codex/full-article.md`, `raw/gpt-5-3-codex-system-card/full-article.md`, `raw/introducing-gpt-5-3-codex-spark/full-article.md`, `raw/gpt-5-3-instant/full-article.md`, `raw/gpt-5-3-instant-system-card/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

Unlike the other versions in this lineage, GPT-5.3 has no separate general-purpose "Thinking" announcement in this batch of sources; it shipped instead as three distinct releases, a coding model, a lightweight coding variant, and an update to the everyday chat model. OpenAI introduced GPT-5.3-Codex on February 5, 2026 as its most capable agentic coding model to date, combining the frontier coding performance of GPT-5.2-Codex with the reasoning and professional knowledge-work capabilities of GPT-5.2 in a single model that runs about 25% faster. It set new highs on SWE-Bench Pro and Terminal-Bench 2.0 while using fewer tokens than any prior model, matched GPT-5.2 on GDPval, and showed far stronger computer-use capability than earlier GPT models on OSWorld-Verified, where human performance is around 72%. OpenAI describes GPT-5.3-Codex as the first model that was instrumental in creating itself: the Codex team used early versions of the model to debug its own training run, manage its own deployment, and diagnose evaluation results during development.

GPT-5.3-Codex is also the first OpenAI model classified as High capability for cybersecurity under the Preparedness Framework, and the first directly trained to identify software vulnerabilities. OpenAI states it has no definitive evidence the model can automate cyberattacks end to end, but is applying its most comprehensive cybersecurity safety stack to date: safety training, automated monitoring, trusted access for advanced capabilities, and enforcement pipelines that include threat intelligence. Some elevated-cyber-risk requests can be routed automatically from GPT-5.3-Codex down to GPT-5.2. Alongside the model, OpenAI launched a Trusted Access for Cyber pilot, expanded the private beta of its Aardvark security-research agent, and committed $10M in API credits toward cyber defense.

A week later, on February 12, 2026, OpenAI released GPT-5.3-Codex-Spark as a research preview: a smaller version of GPT-5.3-Codex built for real-time coding rather than long-running autonomous work, delivering more than 1,000 tokens per second on Cerebras Wafer Scale Engine 3 hardware as the first product of OpenAI's partnership with Cerebras (announced January 2026). At launch it supports a 128k context window and text only, with separate rate limits from standard usage. Building Codex-Spark also drove latency work that benefits every model: a persistent WebSocket connection and Responses API changes cut per-request overhead by 80%, per-token overhead by 30%, and time-to-first-token by 50%. OpenAI evaluated Codex-Spark as part of its standard deployment process and determined it does not have a plausible chance of reaching the Preparedness Framework's High threshold for cybersecurity or biology.

Separately, on March 3, 2026, OpenAI updated ChatGPT's everyday chat model to GPT-5.3 Instant, aimed at conversational quality rather than raw benchmark scores: fewer unnecessary refusals and moralizing preambles, better-synthesized web search results, a more focused conversational tone, and measurable factuality gains. On an internal higher-stakes evaluation (medicine, law, finance), hallucination rates dropped 26.8% with web use and 19.7% without, relative to GPT-5.2 Instant; on a separate evaluation built from user-flagged factual errors, hallucinations fell 22.5% with web use and 9.6% without. The system card for GPT-5.3 Instant states its safety mitigation approach is largely the same as GPT-5.2 Instant's.

## Key Claims

- GPT-5.3-Codex is 25% faster than GPT-5.2-Codex while combining GPT-5.2-Codex's coding strength with GPT-5.2's reasoning and professional knowledge-work capability.
- SWE-Bench Pro (public) 56.8%, Terminal-Bench 2.0 77.3%, OSWorld-Verified 64.7%, GDPval 70.9% (matching GPT-5.2), Cybersecurity Capture-the-Flag challenges 77.6% at xhigh reasoning effort.
- GPT-5.3-Codex is the first OpenAI model rated High capability for cybersecurity under the Preparedness Framework, and the first trained directly to identify software vulnerabilities.
- OpenAI can automatically route elevated-cyber-risk requests from GPT-5.3-Codex to GPT-5.2, and committed $10M in API credits to cyber defense on top of a $1M Cybersecurity Grant Program launched in 2023.
- GPT-5.3-Codex-Spark delivers more than 1,000 tokens per second on Cerebras hardware, the first release from OpenAI's Cerebras partnership; it does not reach the High threshold for cybersecurity or biology.
- Codex-Spark infrastructure work cut per-roundtrip overhead by 80%, per-token overhead by 30%, and time-to-first-token by 50%, benefits that roll out to all models over time.
- GPT-5.3 Instant reduces hallucinations 26.8% (with web) / 19.7% (without) on a higher-stakes internal evaluation, and 22.5% / 9.6% on a user-feedback-based evaluation, versus GPT-5.2 Instant.
- GPT-5.3 Instant is available as `gpt-5.3-chat-latest` in the API; GPT-5.2 Instant retired from ChatGPT's Legacy Models on June 3, 2026.
- GPT-5.3-Codex is described as the first model instrumental in creating itself, used by OpenAI's own Codex team to debug and manage its training and deployment.

## Benchmarks

| Eval | GPT-5.3-Codex (xhigh) | GPT-5.2-Codex (xhigh) | GPT-5.2 (xhigh) |
| --- | --- | --- | --- |
| SWE-Bench Pro (Public) | 56.8% | 56.4% | 55.6% |
| Terminal-Bench 2.0 | 77.3% | 64.0% | 62.2% |
| OSWorld-Verified | 64.7% | 38.2% | 37.9% |
| GDPval (wins or ties) | 70.9% | - | 70.9% (high) |
| Cybersecurity Capture the Flag Challenges | 77.6% | 67.4% | 67.7% |
| SWE-Lancer IC Diamond | 81.4% | 76.0% | 74.6% |

## Preparedness Framework / Safety

GPT-5.3-Codex's system card marks the first time OpenAI treated a model as High capability in the Cybersecurity domain under the Preparedness Framework, activating the associated safeguards. OpenAI is explicit that it lacks definitive evidence the model actually reaches that threshold, but is taking a precautionary approach because it cannot rule out the possibility. The safeguards rely on a layered safety stack designed to impede and disrupt threat actors while working to make the same capabilities available to legitimate cyber defenders, backed by the new Trusted Access for Cyber pilot and expanded Aardvark security-research agent beta. The model keeps the High biology designation used across the GPT-5 family and does not reach High capability on AI self-improvement.

GPT-5.3-Codex-Spark went through the same safety training as mainline models, including cyber-relevant training, and was evaluated as part of the standard deployment process; OpenAI determined it does not have a plausible chance of reaching the Preparedness Framework's High threshold for cybersecurity or biology, consistent with its role as a smaller, faster, more narrowly scoped model. The GPT-5.3 Instant system card states its safety mitigation approach is largely unchanged from GPT-5.2 Instant's, with no new risk designation introduced in this source.

## Figures

No article figures extracted; openai.com blocks direct HTML download so figures could not be downloaded, and WebFetch markdown does not preserve chart images. Benchmark data is preserved above as markdown tables instead.

## Entities

- [[OpenAI]] — publisher of GPT-5.3-Codex, its system card, GPT-5.3-Codex-Spark, GPT-5.3 Instant, and its system card.

## Questions & Gaps

- None of the five sources for this page announce a general-purpose "GPT-5.3 Thinking" model; the GPT-5.4 Thinking system card later confirms this explicitly, noting its own baseline comparison is GPT-5.2 Thinking rather than a nonexistent GPT-5.3 Thinking.
- GPT-5.3-Codex-Spark's pricing is not stated; it is described as a research preview with API access limited to "a small set of design partners."
- The GPT-5.3-Codex system card is short and does not give the specific evaluation names or scores behind its High cybersecurity designation beyond what the main announcement's benchmark table shows.

## Related

- [[OpenAI]]
- [[GPT-5.2]]
- [[GPT-5.4]]
- [[Large Language Models]]
- [[Reasoning Models]]
- [[Code Models]]
- [[Agentic AI]]
- [[Evaluation and Benchmarks]]
- [[Preparedness Framework]]
