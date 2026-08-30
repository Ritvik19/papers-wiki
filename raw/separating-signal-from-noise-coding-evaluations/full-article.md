---
Source URL: https://openai.com/index/separating-signal-from-noise-coding-evaluations/
Fetched via: WebFetch (curl returns 403 on openai.com/index/*)
Date: July 8, 2026
---

# Separating signal from noise in coding evaluations

Through a detailed audit, OpenAI finds widespread task issues in SWE-Bench Pro and estimates that ~30% of the tasks are broken.

Accurately measuring model capability matters for sound deployment and safety decisions, including under OpenAI's Preparedness Framework. Following an earlier finding that SWE-bench Verified had fundamental design and contamination issues (see [[why-we-no-longer-evaluate-swe-bench-verified]]), OpenAI had recommended the community switch to SWE-Bench Pro, designed to test longer horizons and more realistic coding tasks. On the 731-task public split, frontier models improved from a 23.3% to 80.3% pass rate in eight months.

A similar audit of SWE-Bench Pro used a datapoint analysis pipeline reviewing model attempts, task metadata, and failure traces to flag likely evaluation flaws, followed by multiple investigator-agent passes and independent review by five experienced software engineers per flagged task (disagreements escalated for further investigation). The automated pipeline flagged 200 tasks (27.4%) as broken; the human annotation campaign identified 249 (34.1%).

Issues fell into four categories:
- **Overly strict tests** enforce specific implementation details not specified in the prompt, invalidating functionally correct submissions.
- **Underspecified prompts** omit requirements that hidden tests enforce and that are not reasonably inferable.
- **Low-coverage tests** under-check the requested feature, letting incomplete fixes pass.
- **Misleading prompts** point models toward the wrong behavior or contradict what tests require.

Overall, OpenAI estimates ~30% of SWE-bench Pro tasks are broken and advises model developers to carefully examine results, retracting its earlier recommendation to adopt SWE-Bench Pro.

## Methodology

An initial automated filter reviewing model instructions, attempts, and grading tests flagged 286 potentially broken tasks. These were reviewed via (1) Codex-based investigator agents with access to the task repository and environment, distinguishing reasonable ambiguity (resolvable by studying nearby code/conventions) from true underspecification, followed by a researcher's final judgment; and (2) a human annotation campaign with experienced software engineers trained on the benchmark's goals, issue taxonomy, and edge cases, each task reviewed by five engineers who formed independent judgments before consulting pipeline analysis, then assigned labels/severity with disagreements escalated.

Human reviewers were more likely than investigator agents to mark tasks as broken, though in no flagged task was "not broken" the most common human label; reviewers' judgments overlapped with agent-pipeline categories in 74% of cases. Humans selected low-coverage tests as the most common issue for 9.4% of the benchmark, versus 4.1% from the agent pipeline, suggesting the agent-plus-reviewer pipeline was conservative.

### Example failure mode (OpenLibrary-77c16d5)

A task normalizing table-of-contents entries and rendering to Markdown specified single-space serialization in the prompt (e.g. `" | Chapter 1 | 1"`) but the hidden test assertions required double spaces (`"  | Chapter 1 | 1"`). A model correctly following the given prompt would fail the hidden test on this one-character discrepancy.

## Discussion

Benchmarks sourced from open-source-repository issues/PRs were created for human collaboration through long maintainer-contributor back-and-forths, so problem descriptions, merged code, and tests do not always line up into clean, isolated evaluation tasks; PR tests in particular are often written to validate one specific change rather than an implementation-agnostic standard. At the same time, evaluation flaws are now easier to detect: as model capability improves, models themselves can inspect prompts, tests, patches, traces, and edge cases at much greater depth and scale.

OpenAI hopes the evaluation community will build new benchmarks authored by experienced software developers specifically to test model capability, preserving realism while allowing better human oversight. An eval should provide meaningful signal through benchmarks that are hard to game, easy to trust, and genuinely reflective of capability or alignment, since these results inform OpenAI's deployment and safety decisions.
