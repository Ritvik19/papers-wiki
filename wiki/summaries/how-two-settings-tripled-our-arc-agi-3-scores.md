# How Two Settings Tripled Our ARC-AGI-3 Scores

**Source**: `raw/how-two-settings-tripled-our-arc-agi-3-scores/full-article.md`  
**Ingested**: 2026-07-31  
**Tags**: #summary

## Summary

In a July 29, 2026 post, OpenAI researchers Ilan Bigio and Ted Sanders explain why GPT-5.6 Sol scored poorly on [[ARC-AGI-3]] under the benchmark's default harness and how two general-purpose [[Responses API]] settings raised performance nearly threefold. ARC-AGI-3 tests agents on 2D puzzle games where they must explore unfamiliar environments and infer rules without instructions; on the public leaderboard, no frontier model clears the first level under the standard setup.

With the official ARC-AGI-3 harness, GPT-5.6 Sol scored **13.3%** on the public task set (ARC Prize's verified leaderboard reports **7.8%** under its standardized "no harness" cross-provider setup). OpenAI traced the gap to two harness behaviors: **private reasoning is discarded after every action**, forcing the model to re-derive game rules each turn, and **rolling truncation** drops context once the transcript exceeds 175,000 characters. These choices made GPT-5.6 Sol look weak despite strong interactive-game results elsewhere (Pokémon FireRed vision-only, Slay the Spire 2 via Codex computer use, Baba Is You progress).

Reimplementing the harness on the Responses API with **[[Retained Reasoning]]** (passing `previous_response_id` so chain-of-thought persists across turns) and **[[Compaction]]** (summarizing old context instead of truncating) raised GPT-5.6 Sol to **38.3%** on the public set while using roughly **six times fewer output tokens** per game, clearing all six levels on the tested public game. OpenAI argues benchmark scores depend on harness design, not just the model, and recommends the Responses API with retained reasoning and compaction for long-running agentic work.

ARC Prize Foundation defended its verified methodology: identical observations, system prompts, and action limits for every model, with client-side state management through a standard completions-style interface to prevent provider-specific harness tuning. François Chollet distinguished custom benchmark-specific harnesses (off limits) from general-purpose API settings available to all developers (fair game), acknowledged ARC Prize's GPT-5.6 score disadvantaged OpenAI, and noted ongoing talks about folding server-side state management into future verified testing.

## Key Claims

- Official ARC-AGI-3 harness: GPT-5.6 Sol **13.3%** on public task set; GPT-5.5 **0.4%** in the same investigation.
- ARC Prize verified leaderboard: GPT-5.6 Sol **7.8%** (standardized cross-provider setup).
- Responses API + retained reasoning + compaction: GPT-5.6 Sol **38.3%**, ~**6× fewer output tokens**, all six levels cleared on tested public game.
- Default harness discards private reasoning after each action and truncates context past **175,000 characters**.
- Retained reasoning: chain-of-thought persists when developers pass `previous_response_id` across Responses API calls.
- Compaction: summarizes older context instead of dropping it, replacing rolling truncation.
- OpenAI recommends Responses API over legacy Chat Completions for long agentic tasks.
- ARC Prize uses a "no harness" verified setup to keep cross-lab comparisons fair; working with labs on future server-side state standards.

## Figures

No article figures extracted; openai.com blocks direct HTML download (curl 403). Benchmark score comparisons preserved above as markdown tables.

## Entities

- [[OpenAI]] — publisher of the analysis; GPT-5.6 Sol is the model under test.
- [[GPT-5.6]] — model whose ARC-AGI-3 scores vary dramatically by harness configuration.
- [[ARC-AGI-3]] — interactive puzzle-game benchmark central to the post.
- [[Retained Reasoning]] — Responses API feature preserving reasoning across turns.
- [[Compaction]] — Responses API feature summarizing old context instead of truncating.
- [[Responses API]] — recommended API surface for the configuration OpenAI describes.

## Questions & Gaps

- OpenAI's 38.3% uses provider-specific Responses API settings; ARC Prize leaderboard scores are not directly comparable without explicit harness attribution.
- Whether future ARC verified testing will adopt server-side state management (compaction, retained reasoning) remains unresolved.
- Third-party reports cite Claude Opus 5 at 30.2% with provider-appropriate settings; direct head-to-head under identical harnesses is not documented in this source.

## Related

- [[GPT-5.6]] — GA announcement reports official-harness ARC-AGI-3 scores for the full family.
- [[Evaluation and Benchmarks]] — harness-vs-model evaluation methodology.
- [[Reasoning Models]] — reasoning persistence across multi-step agentic tasks.
- [[Agent Harness]] — benchmark harness design as a first-class evaluation variable.
- [[Controlling Reasoning Effort in LLMs]] — related work on reasoning configuration at inference time.
