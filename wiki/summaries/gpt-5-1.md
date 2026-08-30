# GPT-5.1

**Source**: `raw/gpt-5-1/full-article.md`, `raw/gpt-5-system-card-addendum-gpt-5-1/full-article.md`, `raw/gpt-5-1-codex-max/full-article.md`, `raw/gpt-5-1-codex-max-system-card/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

OpenAI shipped GPT-5.1 on November 12, 2025 as an upgrade to both halves of the GPT-5 router: GPT-5.1 Instant and GPT-5.1 Thinking. Instant is described as warmer and more conversational by default, with better instruction following, for example more reliably honoring a constraint like "respond in six words." For the first time, Instant gained adaptive reasoning: it can decide on its own when a question is hard enough to warrant thinking before responding, which shows up as gains on math and coding evaluations such as AIME 2025 and Codeforces. Thinking adapts its reasoning time more precisely to each question, running roughly twice as fast on the easiest tasks and twice as slow on the hardest compared to GPT-5 Thinking at the same "Standard" setting, with clearer responses that use less jargon. OpenAI named the release 5.1 rather than 6 specifically to signal an iterative improvement within the GPT-5 generation, with the same naming pattern expected for future updates. Rollout went to paid ChatGPT tiers first, then free and logged-out users; Instant shipped in the API as `gpt-5.1-chat-latest` and Thinking as `gpt-5.1`, both with adaptive reasoning on by default.

The system card addendum for GPT-5.1 reuses the safety mitigations described for GPT-5 and adds updated baseline safety metrics for the new versions. It extends the evaluation set introduced in GPT-5's sensitive-conversations addendum to cover mental health signals such as isolated delusions, psychosis, or mania, and to cover emotional reliance, meaning unhealthy emotional dependence or attachment to ChatGPT.

A week later, on November 19, 2025, OpenAI released GPT-5.1-Codex-Max, a frontier agentic coding model built on an updated reasoning model and trained specifically for long-running, multi-hour coding work. Its headline feature is compaction: the first OpenAI model natively trained to work across multiple context windows by pruning history while preserving what matters, letting it work coherently over millions of tokens in a single task and, in internal evaluations, keep iterating on a task for more than 24 hours. On SWE-bench Verified it reached 77.9% at "xhigh" reasoning effort versus 73.7% for GPT-5.1-Codex at "high," while using 30% fewer thinking tokens than GPT-5.1-Codex at the same "medium" effort level. It is also the first OpenAI model trained to operate in Windows environments. Internally, OpenAI reports 95% of its engineers use Codex weekly and ship roughly 70% more pull requests since adopting it.

The Codex-Max system card evaluates the model under the Preparedness Framework as very capable in cybersecurity, the most capable cybersecurity model OpenAI had deployed at that point, but stops short of the High capability threshold. It keeps the High designation for biology carried over from GPT-5, and does not reach High capability on AI self-improvement. Codex itself runs in a sandbox by default, with file writes restricted to its workspace and network access off unless a developer enables it.

## Key Claims

- GPT-5.1 Instant gains adaptive reasoning, deciding on its own when to think before answering; GPT-5.1 Thinking adapts its reasoning time per question, running about 2x faster on easy tasks and 2x slower on hard ones versus GPT-5 Thinking at Standard setting.
- API names: `gpt-5.1-chat-latest` (Instant), `gpt-5.1` (Thinking), both with adaptive reasoning by default.
- New tone presets: Professional, Candid, and Quirky added alongside updated Default, Friendly, and Efficient; Cynical and Nerdy unchanged.
- GPT-5.1-Codex-Max introduces compaction, letting the model work across multiple context windows over millions of tokens in one task; observed running on tasks for more than 24 hours in internal evaluations.
- SWE-bench Verified: 77.9% (Codex-Max, xhigh) vs 73.7% (Codex, high); SWE-Lancer IC SWE: 79.9% vs 66.3%; Terminal-Bench 2.0: 58.1% vs 52.8%.
- Codex-Max uses 30% fewer thinking tokens than GPT-5.1-Codex at matched "medium" reasoning effort.
- 95% of OpenAI engineers use Codex weekly; those engineers ship roughly 70% more pull requests since adopting it.
- Codex-Max does not reach High cybersecurity capability under the Preparedness Framework but is described as the most capable cybersecurity model OpenAI had deployed to date; it keeps the High biology designation from GPT-5 and does not reach High on AI self-improvement.
- GPT-5.1 system card addendum adds mental health (delusions, psychosis, mania) and emotional reliance to its baseline safety evaluation set, building on GPT-5's sensitive-conversations addendum.

## Benchmarks

| Eval | GPT-5.1-Codex (high) | GPT-5.1-Codex-Max (xhigh) |
| --- | --- | --- |
| SWE-bench Verified (n=500) | 73.7% | 77.9% |
| SWE-Lancer IC SWE | 66.3% | 79.9% |
| Terminal-Bench 2.0 | 52.8% | 58.1% |

## Preparedness Framework / Safety

The GPT-5.1 system card addendum states that comprehensive safety mitigations are largely unchanged from the GPT-5 System Card. Its main addition is coverage: baseline safety evaluations were expanded to include mental health signals (isolated delusions, psychosis, mania) and emotional reliance (unhealthy dependence or attachment to ChatGPT), continuing the direction set by GPT-5's sensitive-conversations addendum.

GPT-5.1-Codex-Max's system card places the model as very capable in cybersecurity without crossing the High threshold under the Preparedness Framework, while noting OpenAI expects models to cross that threshold in the near future given the pace of improvement. It retains the High Biological and Chemical capability designation used for GPT-5 and applies the same safeguard suite. It does not reach High capability on AI self-improvement. At the product level, Codex runs sandboxed by default (workspace-limited file writes, network access off unless explicitly enabled), and OpenAI flags that turning on internet access or web search introduces prompt-injection risk from untrusted content, recommending developers review agent output rather than treat Codex as a substitute for human review.

## Figures

No article figures extracted; openai.com blocks direct HTML download so figures could not be downloaded, and WebFetch markdown does not preserve chart images. Benchmark data is preserved above as markdown tables instead.

## Entities

- [[OpenAI]] — publisher of GPT-5.1, its system card addendum, GPT-5.1-Codex-Max, and its system card.

## Questions & Gaps

- The GPT-5.1 announcement does not give a precise numeric breakdown of the adaptive-reasoning accuracy gains on AIME 2025 or Codeforces for Instant, only that both improved.
- Pricing for GPT-5.1-Codex-Max was not stated in the announcement; API access is noted as arriving later than the Codex-surface launch.
- The mental health and emotional reliance evaluation sets introduced in the GPT-5.1 addendum are described qualitatively, without published baseline scores in this source.

## Related

- [[OpenAI]]
- [[GPT-5]]
- [[GPT-5.2]]
- [[Large Language Models]]
- [[Reasoning Models]]
- [[Code Models]]
- [[Agentic AI]]
- [[Long Context]]
- [[Safety and Alignment]]
- [[Preparedness Framework]]
