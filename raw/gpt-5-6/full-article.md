---
Source URL: https://openai.com/index/gpt-5-6/
Fetched via: WebFetch (curl returns 403 on openai.com/index/*)
Date published: July 9, 2026
Update: July 30, 2026 — Luna price cut 80%, Terra 20%
---

# GPT‑5.6: Frontier intelligence that scales with your ambition

We're launching the GPT‑5.6 family of models for general availability following our limited preview: our new flagship, Sol, alongside Terra, a balanced model for everyday work, and Luna, our most cost-efficient model.

GPT‑5.6 Sol sets a new standard for both intelligence and efficiency, achieving state-of-the-art results across coding, knowledge work, cybersecurity, and science while outperforming previous and competing frontier models with fewer tokens and at lower estimated cost. We also introduce `ultra`, our highest-capability setting, coordinating multiple agents across parallel workstreams to finish complex tasks faster.

## Key capability claims

- **Agents' Last Exam**: GPT‑5.6 Sol sets a new high of 53.6 (max reasoning), eclipsing Claude Fable 5 (adaptive reasoning) by 13.1 points. At medium reasoning, beats Fable 5 by 11.4 points at ~¼ estimated cost.
- **Artificial Analysis Intelligence Index v4.1**: GPT‑5.6 Sol with max reasoning within one point of Fable 5 while completing tasks in 61% less time at ~half estimated cost.
- **Artificial Analysis Coding Agent Index v1.1**: GPT‑5.6 Sol with max reasoning SOTA at 80 (2.8 points above Fable 5), using <½ output tokens, <½ time, ~⅓ cost.
- **Terminal-Bench 2.1**: 88.8% (Sol), 91.9% (Sol Ultra); new SOTA.
- **BrowseComp**: 90.4% (Sol), 92.2% (Sol Ultra).
- **OSWorld 2.0**: 62.6% (Sol); surpasses Opus 4.8 while using 85% fewer output tokens.
- **ExploitBench**: 73.5% vs GPT‑5.5's 47.9% at comparable token budget.
- **ExploitGym**: 33.7% (6-hour cap) vs GPT‑5.5's 15.1% (2-hour cap).
- **GeneBench Pro**: 28.7% vs GPT‑5.5's 12% with fewer tokens.
- **RSI Index**: 57.9% vs GPT‑5.5's 41.7%.

## API and product features

- **ChatGPT Work**: new product combining ChatGPT and Codex for non-coding knowledge work; connects to Slack, Gmail, Google Drive, calendars, CRMs.
- **Responses API**: Programmatic Tool Calling (in-memory tool coordination, ZDR compatible); multi-agent beta for concurrent subagents.
- **Reasoning**: `max` effort level; `ultra` mode (4 agents default in API); `reasoning.mode: "pro"` for highest quality.
- **Prompt caching**: explicit cache breakpoints, 30-minute minimum cache life; cache writes at 1.25× uncached input rate for GPT‑5.6+.

## Safety (GA)

- Most robust safety system to date; ~700,000 A100-equivalent GPU hours automated red-teaming before GA.
- Cyber safeguards block roughly **10× more** potentially harmful activity vs prior models.
- Option to retry prompts on lower-capability models when safeguards create friction.
- All three models High in Bio/Chem and Cyber; below High in AI Self-Improvement; none reach Cyber Critical.
- Updated system card at deploymentsafety.openai.com/gpt-5-6.

## Availability and pricing

GA rollout July 9, 2026 across ChatGPT, Codex, and OpenAI API.

| Model | Input ($/1M) | Output ($/1M) | Notes |
| --- | --- | --- | --- |
| Sol | $5 | $30 | Flagship |
| Terra | $2.50 → **$2.00** (Jul 30) | $15 → **$12.00** (Jul 30) | Competitive with GPT‑5.5 |
| Luna | $1 → **$0.20** (Jul 30) | $6 → **$1.20** (Jul 30) | Fastest, most affordable |

- Chat: Plus/Pro/Business/Enterprise get Sol at medium+ effort; Pro/Enterprise get Sol Pro.
- ChatGPT Work and Codex: Free/Go get Terra; Plus+ can choose Sol/Terra/Luna; `max` for all with access; `ultra` for Pro/Enterprise (ChatGPT Work) or Plus+ (Codex).

## Benchmark tables (from announcement)

### Professional
| Eval | Sol | Terra | Luna | GPT‑5.5 | Fable 5 |
| --- | --- | --- | --- | --- | --- |
| Agents' Last Exam | 52.7% | 50.4% | 50.3% | 46.9% | 40.5% |
| GDPval-AA v2 | 1747.8 Elo | 1593 | 1591.8 | 1493.7 | 1759.6 |
| AA Intelligence Index v4.1 | 58.9 | 55 | 51.2 | 54.8 | 59.9 |

### Coding
| Eval | Sol | Sol Ultra | Terra | Luna | GPT‑5.5 |
| --- | --- | --- | --- | --- | --- |
| AA Coding Agent Index v1.1 | 80 | — | 77.4 | 74.6 | 76.4 |
| SWE-Bench Pro | 64.6% | — | 63.4% | 62.7% | 59.4% |
| Terminal-Bench 2.1 | 88.8% | 91.9% | 87.4% | 84.7% | 85.6% |
| DeepSWE v1.1 | 72.7% | — | 69.6% | 67.2% | 67% |

### Cybersecurity
| Eval | Sol | Sol Ultra | Terra | Luna | GPT‑5.5 |
| --- | --- | --- | --- | --- | --- |
| Capture-the-Flag | 96.7% | — | 91.8% | 85.2% | 88.1% |
| SEC-Bench Pro | 71.2% | 74.3% | 57.7% | 48.9% | 45.8% |
| ExploitBench | 73.5% | — | 52.9% | 33.2% | 47.9% |
| ExploitGym | 33.7% | — | 23.2% | 12.4% | 15.1% |

### Abstract reasoning
| Eval | Sol | Terra | Luna | GPT‑5.5 |
| --- | --- | --- | --- | --- |
| ARC-AGI-3 (official harness) | 7.78% | 0.8% | 0.18% | 0.43% |

Footnote: ARC-AGI-3 scores use official scoring approach; see [[How Two Settings Tripled Our ARC-AGI-3 Scores]] for harness-configuration analysis.
