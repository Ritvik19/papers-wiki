# Papers Explained: Passive Skill Distillation

Papers Explained: Passive Skill Distillation

Papers Explained: Passive Skill Distillation

While reasoning modes in language models perform better on multi-step agentic tasks, they are expensive due to redundant output tokens…

Papers Explained: Passive Skill Distillation

While reasoning modes in language models perform better on multi-step agentic tasks, they are expensive due to redundant output tokens spent reiterating procedures. This work shows that by analyzing a small set of example trajectories and compiling these into a compact natural-language skill for use in non-reasoning models, most of the reasoning advantage (55%–100%+ on tested benchmarks) can be achieved with far fewer output tokens (2.7–6× less) and without repeated reasoning.

Passive Skill Distillation

Let M expose a reasoning mode Mr and a non-reasoning mode Mnr. A benchmark supplies tasks T = Ttrain ∪ Ttest (disjoint), an environment loop (or simulated user), and terminal rewards. The input to distillation is a trajectory corpus D collected once on Ttrain: per-step observations, actions and tool calls, visible outputs, and rewards.

Collect a training corpus: For each domain, the model is rolled out on the training split: 50 ALFWorld canonical tasks, 50 SSB-Verified tasks, 50 τ2-telecom tasks, and 35 τ2-retail training tasks.
Distill with a coding agent: A coding agent A (an LLM with file-system and code-execution tools; here Claude Code with Claude Sonnet 5) is opened in the directory containing the corpus and receives a fixed natural-language instruction P producing a skill σ = A(D, P). The agent compares failing and succeeding trajectories (and, when available, contrasts no-think failures with think successes on the same tasks), computing corpus-level statistics: failure-mode frequencies, action loops, win/loss contrasts, and reading individual episodes where the statistics point.
Deploy: The skill is appended verbatim to the non-reasoning model’s system prompt: πσ(·) = Mnr(· | sys ⊕ σ). Nothing else: harness, decoding, tools, changes between the no-think and skill conditions.

Experimental Setup

Benchmarks:

ALFWorld: text-based embodied household tasks (ReAct-style agent, admissible commands, max. 40 steps); held-out random-50 split; win rate.
SSB-Verified: a verified subset of SpreadsheetBench, real-world spreadsheet manipulation against live workbooks; held out 50 tasks; modification accuracy.
τ2-bench telecom and retail: conversational customer service agents with tool use and a simulated user in a dual-control environment; held-out test splits of 40 tasks; pass rate.

Models:

GPT-5.4-mini with reasoning_effort ∈ {none, medium}
Qwen3.6–27B with enable_thinking ∈ {false, true}
Skills are produced once per domain per model by Claude Sonnet 5 via Claude Code.

Results
Main results.
Injecting distilled skills recovers 55%–100%+ of the reasoning gap across four benchmarks, sometimes even outperforming the original reasoning model, while using 2.9–4.5× fewer tokens.
Ablation: distillation source.
Skills distilled solely from non-reasoning traces are “competitive everywhere” and recover the majority of the reasoning benefit, making the full amortization process viable without running the high-cost reasoning model.

Paper

Reason Wide, Not Deep: Amortizing the Reasoning Premium into Distilled Skills 2608.07885

That’s a wrap!

If you enjoyed this breakdown, follow for more. I publish new paper explanations most weekdays.

More papers in this series, organized by lab and topic, are in the start here guide.

What paper should I cover next? Let me know in the responses.

View original.

Exported from Medium on August 22, 2026.
