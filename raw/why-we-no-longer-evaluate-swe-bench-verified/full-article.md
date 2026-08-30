---
Source URL: https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/
Fetched via: WebFetch (curl returns 403 on openai.com/index/*)
Date: February 23, 2026
---

# Why SWE-bench Verified no longer measures frontier coding capabilities

SWE-bench Verified is increasingly contaminated. OpenAI recommends SWE-bench Pro instead.

Since SWE-bench Verified was first published in August 2024, it became a standard metric for autonomous software-engineering capability, reported in frontier model releases and used in OpenAI's Preparedness Framework capability tracking. After initial leaps, state-of-the-art progress slowed, improving from 74.9% to 80.9% over the last 6 months, raising the question of whether remaining failures reflect genuine model limitations or dataset artifacts.

A new analysis found two major issues indicating the benchmark is no longer suitable for measuring frontier progress at current performance levels:

1. **Tests reject correct solutions**: auditing a 27.6% subset of tasks models often failed, at least 59.4% of audited problems had flawed test cases that reject functionally correct submissions, despite improvements already made when creating SWE-bench Verified.
2. **Training on solutions**: SWE-bench problems are sourced from open-source repositories many model providers train on. All frontier models tested were able to reproduce the original human-written gold patch or verbatim problem-statement specifics for certain tasks, indicating training-time exposure. Models that had seen the problems during training were more likely to succeed, since they had extra information needed to pass underspecified tests.

Because of this, improvements on SWE-bench Verified no longer reflect meaningful real-world software-development improvement, increasingly reflecting benchmark exposure at training time instead. OpenAI has stopped reporting SWE-bench Verified scores and recommends other developers do the same, recommending SWE-Bench Pro in the interim while building new, uncontaminated evaluations.

## Background

The original SWE-bench (2023) sources problems from resolved GitHub issues in 12 open-source Python repositories, paired with the corresponding PR, graded by tests that fail before and pass after a correct fix (plus regression tests). Known issues: some unit tests were overly specific or misaligned with the task (rejecting correct fixes); many task statements were underspecified, admitting multiple valid interpretations that tests only partially covered; and environment setup differences could cause spurious test failures.

SWE-bench Verified (2024) addressed these by having expert engineers review 1,699 SWE-bench problems (three independent reviewers each) to filter to a curated set of 500 problems.

## Too narrow and too wide tests

An audit of 138 SWE-bench Verified problems that OpenAI o3 did not consistently solve over 64 independent runs (each case reviewed by at least six engineers, re-verified by an additional team when flagged) found that 59.4% of the 138 problems had material issues in test design and/or problem description, rendering them extremely difficult or impossible even for the most capable model or human to solve:

- 35.5% had **narrow test cases**: strict tests enforcing specific implementation details, invalidating functionally correct submissions (e.g. `pylint-dev__pylint-4551`, where hidden tests import a specifically named function, `get_annotation`, never mentioned in the problem description).
- 18.8% had **wide test cases**: tests checking additional functionality not specified in the problem description (e.g. `sympy__sympy-18199`, where the PR fixed three distinct issues but the task description covers only one, so models correctly implementing the described fix fail tests covering the other two).
- 5.1% had miscellaneous issues not well grouped by this taxonomy.

## Contamination

SWE-bench Verified and its source repositories are open and widely discussed, making contamination hard to avoid. OpenAI first noticed signs in its own models: GPT‑5.2 solved 31 tasks identified as nearly impossible, and its chain-of-thought showed direct knowledge of unreleased/undocumented details (e.g. knowing a specific `edit_only` parameter was introduced in a later Django version, from release notes rather than the problem text, in `django__django-14725`).

To assess contamination more broadly, an automated red-teaming setup tasked GPT‑5 with probing GPT‑5.2‑Chat, Claude Opus 4.5, and Gemini 3 Flash Preview (non-reasoning models) for contamination, given each task's ID, description, gold patch, and PR tests, with a judge model labeling contamination severity across turns and later human review of "strong" cases. Examples of strong contamination were found across all three model providers, including verbatim reproduction of exact gold-patch diffs, method names, comment text, and even punctuation, from only a short task-ID hint.

## Discussion

Two broader lessons: (1) benchmarks sourced from public material carry contamination risk since training-data exposure can silently inflate scores, arguing for password-protected dataset hosting and strict canary-string filtering; (2) automated scoring is hard to get right, since perfect tests must fully verify correctness while remaining agnostic to unimportant implementation details and robust to shortcut solutions, requiring extensive human labeling to catch.

OpenAI has switched to reporting results from the public split of SWE-Bench Pro, which its contamination pipeline found suffers from contamination far less often and less severely (no model produced a complete verbatim gold patch), though it is "not perfect" (see the later [[separating-signal-from-noise-coding-evaluations]] audit, which found ~30% of SWE-Bench Pro tasks broken). OpenAI plans to continue investing in original, privately authored benchmarks such as GDPval, where tasks are privately authored by domain experts and graded holistically by trained reviewers.
