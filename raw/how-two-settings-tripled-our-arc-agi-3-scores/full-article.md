---
Source URL: https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores/
Fetched via: WebFetch (curl returns 403 on openai.com/index/*); content reconstructed from OpenAI post via secondary reporting (Office Chai, The Decoder) cross-checked against GPT-5.6 GA announcement footnote
Date published: July 29, 2026
Authors: Ilan Bigio, Ted Sanders (per Office Chai)
---

# How enabling two settings tripled our scores on the ARC-AGI-3 benchmark

OpenAI published an analysis showing that GPT-5.6 Sol's score on ARC-AGI-3 nearly tripled once the company swapped the benchmark's default harness for two settings it already uses inside ChatGPT and Codex.

## Scores

| Configuration | GPT-5.6 Sol (public task set) | Notes |
| --- | --- | --- |
| Official ARC-AGI-3 harness | 13.3% | Reasoning discarded after each action; rolling truncation past 175k chars |
| ARC Prize verified leaderboard (no harness) | 7.8% | Standardized cross-provider setup |
| OpenAI Responses API + retained reasoning + compaction | **38.3%** | ~6× fewer output tokens per game; cleared all 6 levels on tested public game |

For comparison: GPT-5.5 scored 0.4% on ARC-AGI-3 in the same investigation. Claude Opus 5 reportedly reached 30.2% with provider-appropriate settings (per third-party reporting).

## What was going wrong

ARC-AGI-3 is a benchmark of 2D puzzle games where an agent must explore an unfamiliar environment and infer rules without instructions. On the public leaderboard, no frontier model gets past the first level under the default harness.

OpenAI researchers identified two harness limitations in ARC's generic test setup:

1. **Reasoning discarded after every action** — the model had to re-derive game rules from scratch each turn. It could see a log of past moves and short notes, but not the private thinking that produced those moves.
2. **Rolling truncation** — once conversation exceeded 175,000 characters, oldest context was dropped, so the model lost earlier observations.

This combination made GPT-5.6 Sol look weak on ARC-AGI-3 despite strong performance on other interactive tasks (Pokémon FireRed vision-only, Slay the Spire 2 via Codex computer use, Baba Is You progress).

## The fix

GPT-5.6 Sol was built through OpenAI's Responses API, where reasoning persists across turns when developers pass `previous_response_id`. OpenAI reimplemented the ARC-AGI-3 harness with:

- **Retained reasoning** — preserve chain-of-thought across turns instead of discarding after each action.
- **Compaction** — summarize older context instead of truncating it outright.

With both enabled, the model spent less time re-deriving rules and retained strategies across the run.

## OpenAI's broader argument

Benchmark results reflect harness design as much as underlying model capability. OpenAI recommends developers use the Responses API (not legacy Chat Completions), retain reasoning across turns, and enable compaction for long-running agentic tasks.

## ARC Prize response

ARC Prize Foundation defended its verified "no harness" setup: every model receives the same observations, system prompt, and action limits; conversation state is managed client-side through a standard completions-style interface rather than provider-specific session management. Goal: prevent harness tuning around a specific model and keep cross-lab comparisons fair.

François Chollet (ARC Prize co-founder) distinguished harnesses custom-made for a benchmark (off limits) from general-purpose API settings available to all API users (fair game). He acknowledged ARC Prize's GPT-5.6 Sol score put OpenAI at a disadvantage and noted ongoing discussions with OpenAI about compaction and server-side state management for future verified testing.

ARC Prize said it is working with OpenAI and other labs on how server-side state management might be folded into verified testing without giving any provider an edge.
