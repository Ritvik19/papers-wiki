---
Source URL: https://openai.com/index/gpt-5-1-codex-max/
Fetched via: WebFetch (curl returns 403 on openai.com/index/*)
Date: November 19, 2025
---

# Building more with GPT‑5.1‑Codex‑Max

GPT‑5.1‑Codex‑Max is OpenAI's new frontier agentic coding model, available in Codex. It is built on an update to the foundational reasoning model, trained on agentic tasks across software engineering, math, research, and more. It is faster, more intelligent, and more token-efficient at every stage of the development cycle.

GPT‑5.1‑Codex‑Max is built for long-running, detailed work. It is the first model natively trained to operate across multiple context windows through a process called **compaction**, coherently working over millions of tokens in a single task. This unlocks project-scale refactors, deep debugging sessions, and multi-hour agent loops.

Available in Codex for use in the CLI, IDE extension, cloud, and code review; API access came later.

## Frontier coding capabilities

Trained on real-world software engineering tasks (PR creation, code review, frontend coding, Q&A). Outperforms previous models on many frontier coding evaluations. GPT‑5.1‑Codex‑Max is the first model trained to operate in Windows environments, and training now includes tasks designed to make it a better collaborator in the Codex CLI.

All evals were run with compaction enabled at Extra High reasoning effort; Terminal-Bench 2.0 ran with Codex CLI in the Laude Institute Harbor harness.

## Speed and cost

Significant improvements in token efficiency due to more effective reasoning. On SWE-bench Verified, GPT‑5.1‑Codex‑Max with 'medium' reasoning effort achieves better performance than GPT‑5.1‑Codex with the same effort while using 30% fewer thinking tokens. A new Extra High ('xhigh') reasoning effort was introduced for non-latency-sensitive tasks; 'medium' remains the recommended daily driver.

## Long-running tasks

Compaction enables the model to complete tasks that would previously fail due to context-window limits, such as complex refactors and long-running agent loops, by pruning history while preserving the most important context over long horizons. In Codex applications, the model automatically compacts its session when approaching the context window limit, giving it a fresh window, repeating until the task completes. In internal evaluations, GPT‑5.1‑Codex‑Max was observed working on tasks for more than 24 hours, persistently iterating on its implementation and fixing test failures.

## Building safe and trustworthy AI agents

GPT‑5.1‑Codex‑Max performs significantly better on evaluations requiring sustained, long-horizon reasoning, improving results on long-horizon coding and cybersecurity challenges. It does not reach High capability on Cybersecurity under the Preparedness Framework, but is the most capable cybersecurity model deployed to date; OpenAI is enhancing safeguards in the cyber domain and working to ensure defenders benefit from improved capabilities through programs like Aardvark.

Codex runs in a secure sandbox by default: file writes are limited to its workspace, and network access is disabled unless a developer turns it on. Enabling internet or web search can introduce prompt-injection risks from untrusted content. Developers are advised to review agent work rather than treat Codex as a replacement for human review.

## Availability

Available in Codex with ChatGPT Plus, Pro, Business, Edu, and Enterprise plans, replacing GPT‑5.1‑Codex as the default model in Codex surfaces. Recommended only for agentic coding tasks in Codex or Codex-like environments (unlike general-purpose GPT‑5.1).

## Appendix: model evaluations

| Eval | GPT‑5.1‑Codex (high) | GPT‑5.1‑Codex‑Max (xhigh) |
| --- | --- | --- |
| SWE-bench Verified (n=500) | 73.7% | 77.9% |
| SWE-Lancer IC SWE | 66.3% | 79.9% |
| Terminal-Bench 2.0 | 52.8% | 58.1% |

Internally, 95% of OpenAI engineers use Codex weekly, and these engineers ship roughly 70% more pull requests since adopting Codex.
