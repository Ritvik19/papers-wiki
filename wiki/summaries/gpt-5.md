# GPT-5

**Source**: `raw/introducing-gpt-5/full-article.md`, `raw/gpt-5-system-card/full-article.md`, `raw/gpt-5-system-card-addendum-gpt-5-codex/full-article.md`, `raw/gpt-5-system-card-sensitive-conversations/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

OpenAI released GPT-5 on August 7, 2025 as a unified system rather than a single model. A fast, efficient model (`gpt-5-main`) answers most questions, a deeper reasoning model (`gpt-5-thinking`) handles harder problems, and a real-time router decides which one to use based on conversation type, complexity, tool needs, and explicit cues such as a user writing "think hard about this." The router is trained continuously on signals including when users switch models by hand, response preference rates, and measured correctness. GPT-5 became the default model in ChatGPT, replacing GPT-4o, o3, o4-mini, GPT-4.1, and GPT-4.5 for signed-in users, with Pro subscribers getting unlimited access plus GPT-5 pro, a variant that uses scaled parallel test-time compute for the hardest tasks. In the API, developers get direct access to the thinking model, a mini version, and a nano version.

On benchmarks, GPT-5 set new highs at launch: 94.6% on AIME 2025 without tools, 74.9% on SWE-bench Verified, 88% on Aider Polyglot, 84.2% on MMMU, and 46.2% on HealthBench Hard, with GPT-5 pro reaching 88.4% on GPQA without tools. OpenAI also reported gains outside raw benchmark scores. With web search enabled, GPT-5's responses were about 45% less likely to contain a factual error than GPT-4o's, and GPT-5 thinking's responses were about 80% less likely to contain an error than o3's. A CharXiv test that stripped images from a multimodal benchmark found o3 still answered confidently about nonexistent images 86.7% of the time, versus 9% for GPT-5, and deception rates on real ChatGPT traffic dropped from 4.8% (o3) to 2.1% (GPT-5 reasoning). Sycophantic replies in targeted evaluations fell from 14.5% to under 6%.

The GPT-5 system card describes the same router architecture and adds a mapping from the model's predecessors: GPT-4o becomes `gpt-5-main`, o3 becomes `gpt-5-thinking`, o4-mini becomes `gpt-5-thinking-mini`, and o3 Pro becomes `gpt-5-thinking-pro`. Its central safety claim is a shift away from binary refusal training toward **safe completions**, which trains the model to give the most helpful response available within safety limits rather than a flat refusal, including partial or high-level answers for dual-use topics like virology. Two addenda followed. The September 15, 2025 addendum covers GPT-5-Codex, a version of GPT-5 tuned for agentic coding in Codex through reinforcement learning on real-world coding tasks, paired with sandboxing and prompt-injection defenses at the product level. The October 27, 2025 addendum covers a October 3 update to ChatGPT's default model (GPT-5 Instant) built with more than 170 mental health experts to better recognize and respond to signs of distress, cutting responses that fell short of the desired behavior by 65 to 80%.

Under the Preparedness Framework, OpenAI treated `gpt-5-thinking` as High capability in the Biological and Chemical domain, the same designation given to ChatGPT agent before it, after 5,000 hours of red-teaming with partners including CAISI and the UK AI Security Institute. OpenAI states there is no definitive evidence the model could meaningfully help a novice cause severe biological harm, but chose to activate the associated safeguards anyway as a precaution: threat modeling, safe-completions training, always-on classifiers and reasoning monitors, and enforcement pipelines.

## Key Claims

- Unified system: `gpt-5-main` / `gpt-5-main-mini` (fast) and `gpt-5-thinking` / `gpt-5-thinking-mini` / `gpt-5-thinking-nano` (reasoning), with `gpt-5-thinking-pro` for parallel test-time compute, routed by a continuously trained real-time router.
- 94.6% on AIME 2025 (no tools), 74.9% on SWE-bench Verified (n=477 fixed subset), 88% on Aider Polyglot, 84.2% on MMMU, 46.2% on HealthBench Hard, 88.4% on GPQA without tools (GPT-5 pro).
- GPT-5 thinking uses 50 to 80% fewer output tokens than o3 while scoring better across visual reasoning, agentic coding, and graduate-level science problems.
- Hallucinations down roughly 45% versus GPT-4o (with search) and roughly 80% versus o3 (when thinking); "GPT-5 thinking" shows about six times fewer hallucinations than o3 on LongFact and FActScore.
- Sycophantic replies dropped from 14.5% to under 6% in targeted evaluations after the earlier 2025 GPT-4o sycophancy incident.
- Safe-completions training replaces binary refusal for dual-use requests, aiming to answer helpfully within safety limits instead of refusing outright.
- `gpt-5-thinking` is rated High capability in Biological and Chemical risk under the Preparedness Framework, backed by 5,000 hours of red-teaming with CAISI and UK AISI.
- GPT-5-Codex (Sept 2025 addendum) adds RL-trained agentic coding behavior plus sandboxing and prompt-injection defenses for Codex CLI, IDE, web, GitHub, and mobile use.
- The sensitive-conversations addendum (Oct 2025) reports a 65 to 80% reduction in ChatGPT responses that fell short of desired behavior around mental and emotional distress, after work with 170+ mental health experts.
- Trained on Microsoft Azure AI supercomputers.

## Benchmarks

| Eval | GPT-5 | Note |
| --- | --- | --- |
| AIME 2025 (no tools) | 94.6% | New SOTA at launch |
| SWE-bench Verified | 74.9% | Fixed n=477 subset |
| Aider Polyglot | 88% | Real-world coding |
| MMMU | 84.2% | Multimodal understanding |
| HealthBench Hard | 46.2% | Physician-defined criteria |
| GPQA (no tools) | 88.4% | GPT-5 pro, extended reasoning |
| CharXiv (images removed) confident-but-wrong rate | 9% vs 86.7% for o3 | Honesty about missing inputs |
| Deception rate on production-like traffic | 2.1% vs 4.8% for o3 | GPT-5 reasoning |
| Sycophantic replies (targeted eval) | <6% vs 14.5% pre-fix | GPT-4o baseline |

## Preparedness Framework / Safety

`gpt-5-thinking` is designated High capability in the Biological and Chemical risk category, matching the designation OpenAI had already given ChatGPT agent. OpenAI is explicit that it has no definitive evidence the model clears its own threshold for meaningfully helping a novice cause severe biological harm, but activated the full safeguard suite anyway: threat modeling, safe-completions training, always-on classifiers, reasoning monitors, and enforcement pipelines, developed alongside 5,000 hours of red-teaming with CAISI and the UK AI Security Institute.

The core safety-training change across GPT-5 is safe completions, which replaces the older refuse-or-comply pattern. Instead of a hard refusal on an ambiguous or dual-use prompt, the model is trained to answer at whatever level of detail stays within safety limits, and to explain its reasoning transparently when it does decline, offering safer alternatives where possible.

The GPT-5-Codex addendum adds model-level mitigations (safety training specific to harmful coding tasks and prompt injection) and product-level mitigations (agent sandboxing, configurable network access) for the coding agent surface. The sensitive-conversations addendum documents an October 2025 update to ChatGPT's default model that improved recognition of and response to signs of mental and emotional distress, developed with more than 170 mental health experts, cutting undesired responses by 65 to 80% relative to the original August 2025 version of GPT-5 Instant.

## Figures

No article figures extracted; openai.com blocks direct HTML download so figures could not be downloaded, and WebFetch markdown does not preserve chart images. Benchmark data is preserved above as markdown tables instead.

## Entities

- [[OpenAI]] — publisher of GPT-5, its system card, and both addenda.
- [[Microsoft]] — GPT-5 was trained on Microsoft Azure AI supercomputers.

## Questions & Gaps

- The system card does not give GPT-5-Codex its own benchmark numbers; the addendum focuses on safety measures rather than capability evaluation.
- Exact router training data and decision logic are not disclosed beyond the general description of signals used (model switches, preference rates, correctness).
- The sensitive-conversations addendum reports percentage reductions in undesired responses but does not give absolute rates or sample sizes.

## Related

- [[OpenAI]]
- [[GPT-5.1]]
- [[Large Language Models]]
- [[Reasoning Models]]
- [[Code Models]]
- [[Safety and Alignment]]
- [[Evaluation and Benchmarks]]
- [[Instruction Hierarchy]]
- [[Preparedness Framework]]
- [[Papers Explained 429 - GPT-5]]
