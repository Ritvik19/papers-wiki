# Why We No Longer Evaluate SWE-bench Verified

**Source**: `raw/why-we-no-longer-evaluate-swe-bench-verified/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

OpenAI stopped using SWE-bench Verified to evaluate frontier coding capability, because the benchmark is increasingly contaminated, and it recommends SWE-Bench Pro instead. Since SWE-bench Verified was first published in August 2024, it became a standard metric for autonomous software-engineering capability, reported in frontier model releases and used in OpenAI's Preparedness Framework to track capability over time. After initial rapid gains, progress on the benchmark slowed, improving from 74.9% to 80.9% over the six months before this analysis, which raised the question of whether the remaining failures reflect genuine model limitations or artifacts of the dataset itself.

OpenAI's analysis found two major issues. First, tests reject correct solutions: auditing a 27.6% subset of tasks that models often failed, at least 59.4% of the audited problems had flawed test cases that reject functionally correct submissions, despite improvements already made when the benchmark's curators created SWE-bench Verified from the original SWE-bench. Second, models are training on the solutions: SWE-bench problems are sourced from open-source repositories that many model providers train on, and all frontier models tested were able to reproduce the original human-written gold patch or verbatim problem-statement details for certain tasks, evidence of training-time exposure. Models that had seen a given problem during training were more likely to solve it, because they had extra information not available in the task description itself, which let them pass tests that were otherwise underspecified. Because of this, improvements on SWE-bench Verified no longer reliably reflect real-world software-development improvement, and increasingly reflect benchmark exposure at training time instead. OpenAI has stopped reporting SWE-bench Verified scores, recommends other developers do the same, and recommends SWE-Bench Pro as an interim replacement while it builds new, less-contaminated evaluations.

The original SWE-bench (2023) sources problems from resolved GitHub issues across 12 open-source Python repositories, paired with the corresponding pull request, and grades submissions with tests that fail before and pass after a correct fix, plus regression tests. Known issues with that original set included unit tests that were overly specific or misaligned with the stated task, task statements that were underspecified enough to admit multiple valid interpretations the tests only partially covered, and environment setup differences that could cause spurious failures. SWE-bench Verified (2024) addressed these by having expert engineers review 1,699 SWE-bench problems, three independent reviewers per problem, and filtering down to a curated set of 500. A later audit of 138 Verified problems that OpenAI's o3 model did not consistently solve across 64 independent runs, with each case reviewed by at least six engineers and re-verified by an additional team when flagged, found that 59.4% of those 138 problems had material issues in test design or problem description that made them extremely difficult or impossible to solve even for the most capable model or human. Of those, 35.5% had narrow test cases, strict tests enforcing implementation details never mentioned in the problem description (one example, `pylint-dev__pylint-4551`, has a hidden test that imports a specifically named function, `get_annotation`, which the problem description never mentions). 18.8% had wide test cases, checking additional functionality the problem description never specified (one example, `sympy__sympy-18199`, has a pull request that fixed three distinct issues while the task description covers only one, so models that correctly implement the described fix still fail tests covering the other two). The remaining 5.1% had miscellaneous issues that did not fit neatly into either category.

On contamination specifically, OpenAI first noticed signs in its own models: GPT-5.2 solved 31 tasks that had been identified as nearly impossible, and its chain of thought showed direct knowledge of unreleased or undocumented details, such as knowing that a specific `edit_only` parameter was introduced in a later Django version, information that comes from release notes rather than the problem text, in task `django__django-14725`. To assess contamination more broadly, OpenAI set up automated red-teaming in which GPT-5 probed GPT-5.2-Chat, Claude Opus 4.5, and Gemini 3 Flash Preview (all non-reasoning models) for contamination, given each task's ID, description, gold patch, and pull-request tests, with a judge model labeling contamination severity across turns and human review of the "strong" cases afterward. Strong contamination, including verbatim reproduction of exact gold-patch diffs, method names, comment text, and even punctuation, from only a short task-ID hint, turned up across all three model providers tested. OpenAI draws two broader lessons from this: benchmarks sourced from public material carry a contamination risk because training-data exposure can silently inflate scores, arguing for password-protected dataset hosting and strict canary-string filtering; and automated scoring is hard to get right in general, since a good test must fully verify correctness while staying agnostic to implementation details that do not matter and remaining robust to shortcut solutions, which in practice requires extensive human labeling to catch. OpenAI has switched to reporting results from the public split of SWE-Bench Pro, which its own contamination pipeline found suffers from contamination far less often and less severely (no model in that assessment produced a complete verbatim gold patch), though OpenAI notes it is "not perfect" (a later audit found about 30% of SWE-Bench Pro tasks broken, see [[Separating Signal From Noise in Coding Evaluations]]). OpenAI also plans to keep investing in originally, privately authored benchmarks such as GDPval, where tasks are written by domain experts and graded holistically by trained reviewers rather than sourced from public repositories.

## Key Claims

- OpenAI has stopped reporting SWE-bench Verified scores and recommends other developers do the same, citing contamination and test-design flaws.
- Auditing a 27.6% subset of frequently failed tasks, at least 59.4% had flawed test cases that reject functionally correct submissions.
- All frontier models tested could reproduce gold-patch or problem-statement details verbatim on certain tasks, indicating training-time exposure to the benchmark.
- A deeper audit of 138 hard SWE-bench Verified problems found 59.4% had material test or description issues: 35.5% narrow (overly strict) tests, 18.8% wide (underspecified) tests, and 5.1% other issues.
- GPT-5.2 solved 31 tasks flagged as nearly impossible, with chain-of-thought evidence of knowledge that could only come from sources outside the problem text.
- An automated red-teaming setup using GPT-5 as prober found strong contamination signals, including verbatim gold-patch reproduction, in GPT-5.2-Chat, Claude Opus 4.5, and Gemini 3 Flash Preview.
- OpenAI recommends SWE-Bench Pro as an interim replacement, while noting its own later audit found that benchmark is imperfect too (about 30% of its tasks broken).

## Figures

No article figures extracted; openai.com blocks direct HTML download so figures could not be downloaded, and WebFetch markdown does not preserve chart images.

## Entities

- [[OpenAI]]: conducted the contamination and test-quality audit and set the resulting evaluation policy change.

## Questions & Gaps

- The source does not state what fraction of the curated 500 SWE-bench Verified problems remain usable if the flawed ones identified across these audits were removed.
- It is not specified whether Anthropic, Google, or other providers whose models showed contamination signals have made any public response or changed their own evaluation practices as a result.
- The source does not describe how the automated red-teaming judge model itself was validated for accuracy in labeling contamination severity.

## Related

- [[OpenAI]]
- [[Evaluation and Benchmarks]]
- [[Code Models]]
- [[Separating Signal From Noise in Coding Evaluations]]: the later audit of SWE-Bench Pro, the benchmark recommended here as a replacement.
