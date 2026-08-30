---
Source URL: https://openai.com/index/introducing-gpt-5-5/
Fetched via: WebFetch
Date: April 23, 2026 (updated April 24, 2026: GPT-5.5 and GPT-5.5 Pro added to the API)
---

# Introducing GPT-5.5

OpenAI released GPT-5.5 on April 23, 2026, rolling out to Plus, Pro, Business, and Enterprise users in ChatGPT and Codex; GPT-5.5 Pro rolled out to Pro, Business, and Enterprise ChatGPT users. API access followed a day later. GPT-5.5 matches GPT-5.4's per-token serving latency despite being a larger, more capable model, and uses fewer tokens to complete the same Codex tasks.

## Headline comparison table

| Eval | GPT‑5.5 | GPT‑5.4 | GPT‑5.5 Pro | GPT‑5.4 Pro | Claude Opus 4.7 | Gemini 3.1 Pro |
| --- | --- | --- | --- | --- | --- | --- |
| Terminal-Bench 2.0 | 82.7% | 75.1% | - | - | 69.4% | 68.5% |
| Expert-SWE (Internal) | 73.1% | 68.5% | - | - | - | - |
| GDPval (wins or ties) | 84.9% | 83.0% | 82.3% | 82.0% | 80.3% | 67.3% |
| OSWorld-Verified | 78.7% | 75.0% | - | - | 78.0% | - |
| Toolathlon | 55.6% | 54.6% | - | - | - | 48.8% |
| BrowseComp | 84.4% | 82.7% | 90.1% | 89.3% | 79.3% | 85.9% |
| FrontierMath Tier 1-3 | 51.7% | 47.6% | 52.4% | 50.0% | 43.8% | 36.9% |
| FrontierMath Tier 4 | 35.4% | 27.1% | 39.6% | 38.0% | 22.9% | 16.7% |
| CyberGym | 81.8% | 79.0% | - | - | 73.1% | - |

## Model capabilities

**Agentic coding**: On Terminal-Bench 2.0, GPT-5.5 reaches 82.7%. On SWE-Bench Pro it reaches 58.6% (labs have noted evidence of memorization on this eval). On Expert-SWE, an internal eval for long-horizon coding tasks with a median estimated human completion time of 20 hours, GPT-5.5 outperforms GPT-5.4. It improves on all three evals while using fewer tokens than GPT-5.4. Cursor CEO Michael Truell said GPT-5.5 "stays on task for significantly longer without stopping early."

**Knowledge work**: GPT-5.5 is better than GPT-5.4 at generating documents, spreadsheets, and slide presentations in Codex, and at operating computer interfaces via Codex's computer-use skills. More than 85% of OpenAI's own staff use Codex weekly across engineering, finance, communications, marketing, data science, and product management; cited internal use cases include analyzing speaking-request data (Comms), reviewing 24,771 K-1 tax forms totaling 71,637 pages (Finance, ~2 weeks faster than the prior year), and automating weekly business reports (Go-to-Market, saving 5-10 hours/week).

**Scientific research**: GPT-5.5 improves over GPT-5.4 on GeneBench (multi-stage genetics/quantitative-biology data analysis) and leads published scores on BixBench (bioinformatics data analysis). An internal version of GPT-5.5 with a custom harness found a new proof of a longstanding asymptotic fact about off-diagonal Ramsey numbers, later verified in Lean.

## Next-generation inference efficiency

GPT-5.5 was co-designed for, trained with, and served on NVIDIA GB200/GB300 NVL72 systems. Codex was used to analyze production traffic patterns and write custom heuristics for dynamic (rather than fixed-chunk) load partitioning across GPU cores, increasing token generation speed by over 20%.

## Cybersecurity and safety

OpenAI classifies GPT-5.5's biological/chemical and cybersecurity capabilities as **High** under the Preparedness Framework; it did not reach Critical cybersecurity capability, but testing showed a capability step up over GPT-5.4. OpenAI is deploying stricter cyber-risk classifiers than with GPT-5.2/5.4, expanding Trusted Access for Cyber (starting with Codex) for verified users meeting trust-signal requirements, and continuing to offer cyber-permissive models (e.g., GPT-5.4-Cyber) to organizations defending critical infrastructure under strict security requirements. GPT-5.5 went through the full safety/governance process: preparedness evaluations, domain-specific testing, new targeted biology/cybersecurity evaluations, and external expert red-teaming, detailed in the GPT-5.5 system card.

## Availability and pricing

- ChatGPT: GPT-5.5 Thinking for Plus/Pro/Business/Enterprise; GPT-5.5 Pro for Pro/Business/Enterprise.
- Codex: available on Plus, Pro, Business, Enterprise, Edu, and Go plans with a 400K context window; Fast mode generates tokens 1.5x faster for 2.5x the cost.
- API: gpt-5.5 at $5/1M input tokens, $30/1M output tokens, 1M context window; gpt-5.5-pro at $30/1M input, $180/1M output. Batch/Flex pricing at half standard rate; Priority processing at 2.5x standard rate.

## Full evaluation tables

### Coding
| Eval | GPT‑5.5 | GPT‑5.4 | GPT‑5.5 Pro | GPT‑5.4 Pro | Claude Opus 4.7 | Gemini 3.1 Pro |
| --- | --- | --- | --- | --- | --- | --- |
| SWE-Bench Pro (Public) | 58.6% | 57.7% | - | - | 64.3% | 54.2% |
| Terminal-Bench 2.0 | 82.7% | 75.1% | - | - | 69.4% | 68.5% |
| Expert-SWE (Internal) | 73.1% | 68.5% | - | - | - | - |

### Professional
| Eval | GPT‑5.5 | GPT‑5.4 | GPT‑5.5 Pro | GPT‑5.4 Pro | Claude Opus 4.7 | Gemini 3.1 Pro |
| --- | --- | --- | --- | --- | --- | --- |
| GDPval (wins or ties) | 84.9% | 83.0% | 82.3% | 82.0% | 80.3% | 67.3% |
| FinanceAgent v1.1 | 60.0% | 56.0% | - | 61.5% | 64.4% | 59.7% |
| Investment Banking Modeling Tasks (Internal) | 88.5% | 87.3% | 88.6% | 83.6% | - | - |
| OfficeQA Pro | 54.1% | 53.2% | - | - | 43.6% | 18.1% |

### Computer use and vision
| Eval | GPT‑5.5 | GPT‑5.4 | GPT‑5.5 Pro | GPT‑5.4 Pro | Claude Opus 4.7 | Gemini 3.1 Pro |
| --- | --- | --- | --- | --- | --- | --- |
| OSWorld-Verified | 78.7% | 75.0% | - | - | 78.0% | - |
| MMMU Pro (no tools) | 81.2% | 81.2% | - | - | - | 80.5% |
| MMMU Pro (with tools) | 83.2% | 82.1% | - | - | - | - |

### Tool use
| Eval | GPT‑5.5 | GPT‑5.4 | GPT‑5.5 Pro | GPT‑5.4 Pro | Claude Opus 4.7 | Gemini 3.1 Pro |
| --- | --- | --- | --- | --- | --- | --- |
| BrowseComp | 84.4% | 82.7% | 90.1% | 89.3% | 79.3% | 85.9% |
| MCP Atlas | 75.3% | 70.6% | - | - | 79.1% | 78.2% |
| Toolathlon | 55.6% | 54.6% | - | - | - | 48.8% |
| Tau2-bench Telecom (original prompts) | 98.0% | 92.8% | - | - | - | - |

### Academic
| Eval | GPT‑5.5 | GPT‑5.4 | GPT‑5.5 Pro | GPT‑5.4 Pro | Claude Opus 4.7 | Gemini 3.1 Pro |
| --- | --- | --- | --- | --- | --- | --- |
| GeneBench | 25.0% | 19.0% | 33.2% | 25.6% | - | - |
| FrontierMath Tier 1-3 | 51.7% | 47.6% | 52.4% | 50.0% | 43.8% | 36.9% |
| FrontierMath Tier 4 | 35.4% | 27.1% | 39.6% | 38.0% | 22.9% | 16.7% |
| BixBench | 80.5% | 74.0% | - | - | - | - |
| GPQA Diamond | 93.6% | 92.8% | - | 94.4% | 94.2% | 94.3% |
| Humanity's Last Exam (no tools) | 41.4% | 39.8% | 43.1% | 42.7% | 46.9% | 44.4% |
| Humanity's Last Exam (with tools) | 52.2% | 52.1% | 57.2% | 58.7% | 54.7% | 51.4% |

### Cybersecurity
| Eval | GPT‑5.5 | GPT‑5.4 | GPT‑5.5 Pro | GPT‑5.4 Pro | Claude Opus 4.7 | Gemini 3.1 Pro |
| --- | --- | --- | --- | --- | --- | --- |
| Capture-the-Flags challenge tasks (Internal) | 88.1% | 83.7% | - | - | - | - |
| CyberGym | 81.8% | 79.0% | - | - | 73.1% | - |

### Long context
| Eval | GPT‑5.5 | GPT‑5.4 |
| --- | --- | --- |
| Graphwalks BFS 256k f1 | 73.7% | 62.5% |
| Graphwalks BFS 1mil f1 | 45.4% | 9.4% |
| Graphwalks parents 256k f1 | 90.1% | 82.8% |
| Graphwalks parents 1mil f1 | 58.5% | 44.4% |
| OpenAI MRCR v2 8-needle 4K-8K | 98.1% | 97.3% |
| OpenAI MRCR v2 8-needle 128K-256K | 87.5% | 79.3% |
| OpenAI MRCR v2 8-needle 256K-512K | 81.5% | 57.5% |
| OpenAI MRCR v2 8-needle 512K-1M | 74.0% | 36.6% |

### Abstract reasoning
| Eval | GPT‑5.5 | GPT‑5.4 | GPT‑5.4 Pro | Claude Opus 4.7 | Gemini 3.1 Pro |
| --- | --- | --- | --- | --- | --- |
| ARC-AGI-1 (Verified) | 95.0% | 93.7% | 94.5% | 93.5% | 98.0% |
| ARC-AGI-2 (Verified) | 85.0% | 73.3% | 83.3% | 75.8% | 77.1% |

Evals of GPT were run with reasoning effort set to xhigh in a research environment, which may differ slightly from production ChatGPT output.
