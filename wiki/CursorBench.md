# CursorBench

#entity

CursorBench is Cursor's internal evaluation suite for coding agents, built from real engineering sessions inside the Cursor team rather than from public benchmarks. It was first introduced as **Cursor Bench** in [[Composer: Building a fast frontier model with RL]] (Oct 2025) as real agent requests from Cursor engineers plus hand-curated optimal solutions, measuring correctness, adherence to codebase abstractions, and software engineering practices. It is used both to compare model and harness variants over time and to drive training, and it is the offline backbone of the measurement stack described in [[Continually Improving Our Agent Harness]].

## What It Measures

[[Papers Explained - Composer 2]] gives the most concrete description in the corpus. CursorBench was introduced because Cursor observed that public coding benchmarks loosely correlate with real-world utility for four reasons: domain mismatch, prompt over-specification, data contamination and overfitting, and narrow evaluation scope. CursorBench addresses these by using underspecified tasks pulled from real coding sessions, evaluating code quality, execution efficiency, and interactive behavior, and refreshing tasks regularly to track evolving workflows. It is supplemented by targeted evaluations covering ambiguous prompts, instruction following, unnecessary edits, code quality, and interruption handling.

Reported numbers from [[Introducing Composer 2]] and [[Papers Explained - Composer 2]]: Composer 1 scores 38.0%, Composer 1.5 scores 44.2%, Composer 2 reaches 61.3% (the Medium article labels this CursorBench-3; the Mar 2026 blog post tabulates the same scores without a version suffix). Composer 2 sits on a Pareto frontier of cost versus accuracy on this suite while remaining competitive in token efficiency. The benchmark is positioned as the canonical internal accuracy signal that Cursor releases the most public detail on.

[[Introducing Composer 1.5]] also references an internal benchmark of real-world coding problems (scaling curves in figure assets) but does not name CursorBench explicitly; that post's public eval is [[Papers Explained 547 - Terminal-Bench|Terminal-Bench 2.0]] instead.

## Role In The Harness Loop

[[Continually Improving Our Agent Harness]] places CursorBench alongside public benchmarks as the fast, standardized offline read on quality. Harness changes that look promising on CursorBench still go to online A/B tests where additional signals — [[Keep Rate]] of agent-proposed code, LLM-judged user-response semantics, latency, token efficiency, tool-call counts, cache-hit rate — decide whether the variant ships.

## Training-data contamination (Grok 4.5)

The Jul 2026 [[Grok Models#Grok 4.5 (Jul 2026)|Grok 4.5]] Cursor announcement discloses that an earlier snapshot of the Cursor codebase was **accidentally included** in Grok 4.5 training data, giving the model an advantage on CursorBench. The exact impact is unclear. That data has been removed for future models, and Cursor is working on a larger CursorBench update — which is why CursorBench was excluded from Grok 4.5's public benchmark chart. This is a notable honesty disclosure for an internal eval that also drives training.

## Related

- [[Composer: Building a fast frontier model with RL]]
- [[Introducing Composer 1.5]]
- [[Introducing Composer 2]]
- [[Continually Improving Our Agent Harness]]
- [[Agent Harness]]
- [[Papers Explained - Composer 2]]
- [[Evaluation and Benchmarks]]
- [[Code Models]]
- [[Keep Rate]]
- [[Grok Models#Grok 4.5 (Jul 2026)]] — training-data contamination disclosure
- [[Papers Explained 547 - Terminal-Bench]]
