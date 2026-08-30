# Separating Signal From Noise in Coding Evaluations

**Source**: `raw/separating-signal-from-noise-coding-evaluations/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

OpenAI audited SWE-Bench Pro, the coding benchmark it had recommended as a replacement for SWE-bench Verified, and estimates that about 30% of its tasks are broken. Accurately measuring model capability matters for deployment and safety decisions, including those made under OpenAI's Preparedness Framework, so a benchmark that overstates or understates real coding ability is a problem beyond the benchmark itself. After OpenAI found that SWE-bench Verified had design and contamination issues (see [[Why We No Longer Evaluate SWE-bench Verified]]), it recommended the community switch to SWE-Bench Pro, built to test longer time horizons and more realistic coding tasks. On the 731-task public split, frontier models improved from a 23.3% to an 80.3% pass rate over eight months, a pace of progress fast enough to raise the same question that had prompted the earlier audit of Verified: how much of that improvement is genuine.

The audit used a datapoint analysis pipeline that reviewed model attempts, task metadata, and failure traces to flag likely evaluation flaws, followed by multiple passes from investigator agents and independent review by five experienced software engineers per flagged task, with disagreements escalated for further investigation. The automated pipeline flagged 200 tasks (27.4% of the set examined) as broken. The human annotation campaign identified 249 (34.1%). Issues fell into four categories: overly strict tests that enforce implementation details never specified in the prompt, invalidating functionally correct submissions; underspecified prompts that omit requirements the hidden tests enforce and that are not reasonably inferable; low-coverage tests that under-check the requested feature, letting incomplete fixes pass; and misleading prompts that point models toward the wrong behavior or contradict what the tests require. Combining both methods, OpenAI settled on an overall estimate of about 30% of SWE-Bench Pro tasks being broken, and retracted its earlier recommendation to adopt the benchmark, advising developers to examine results carefully.

The methodology started with an automated filter reviewing model instructions, attempts, and grading tests, which flagged 286 potentially broken tasks. Each was reviewed two ways: through Codex-based investigator agents with access to the task's repository and environment, distinguishing reasonable ambiguity that could be resolved by studying nearby code or conventions from true underspecification, followed by a researcher's final judgment; and through a human annotation campaign of experienced software engineers trained on the benchmark's goals, issue taxonomy, and edge cases, where each task was reviewed by five engineers who formed independent judgments before consulting the pipeline's analysis. Human reviewers were more likely than the investigator agents to mark tasks as broken, though "not broken" was never the most common human label on any flagged task, and human judgments overlapped with the agent-pipeline categories in 74% of cases. Humans selected low-coverage tests as the leading issue in 9.4% of the benchmark, compared with 4.1% from the agent pipeline, suggesting the agent-based approach was the more conservative of the two.

One concrete example: task OpenLibrary-77c16d5 asked a model to normalize table-of-contents entries and render them to Markdown, specifying single-space serialization in the prompt (for example `" | Chapter 1 | 1"`), but the hidden test assertions required double spaces (`"  | Chapter 1 | 1"`). A model that correctly followed the given prompt would fail the hidden test over a one-character discrepancy. OpenAI attributes many of these problems to how the underlying tasks were built: benchmarks sourced from open-source repository issues and pull requests were created for human collaboration through long maintainer-contributor back-and-forths, so problem descriptions, merged code, and tests do not always line up into clean, isolated evaluation tasks, and pull-request tests in particular are often written to validate one specific change rather than an implementation-agnostic standard. At the same time, evaluation flaws are easier to detect than before, since more capable models can inspect prompts, tests, patches, traces, and edge cases at much greater depth and scale than earlier audits could. OpenAI says it hopes the evaluation community will build new benchmarks authored by experienced software developers specifically to test model capability, preserving realism while allowing better human oversight, since eval results that are hard to trust or easy to game directly undermine the deployment and safety decisions that depend on them.

## Key Claims

- OpenAI estimates roughly 30% of SWE-Bench Pro tasks are broken, and has retracted its earlier recommendation that the community adopt the benchmark.
- On the 731-task public split of SWE-Bench Pro, frontier model pass rates rose from 23.3% to 80.3% over eight months.
- An automated pipeline flagged 200 of the examined tasks (27.4%) as broken; a human annotation campaign of five engineers per flagged task found 249 (34.1%) broken, with 74% overlap between the two methods' issue categories.
- Four issue categories account for the broken tasks: overly strict tests, underspecified prompts, low-coverage tests, and misleading prompts.
- Human reviewers flagged more tasks as broken than the automated investigator-agent pipeline, making the agent pipeline the more conservative of the two methods.
- One documented failure mode (OpenLibrary-77c16d5) shows a model correctly following the stated prompt but failing a hidden test over an unstated single-versus-double-space formatting difference.
- OpenAI plans to keep investing in benchmarks it authors privately, such as GDPval, rather than relying solely on benchmarks sourced from public open-source repositories.

## Figures

No article figures extracted; openai.com blocks direct HTML download so figures could not be downloaded, and WebFetch markdown does not preserve chart images.

## Entities

- [[OpenAI]]: ran the audit of SWE-Bench Pro and issues the resulting evaluation recommendations.

## Questions & Gaps

- The source does not say how many of the 731 public-split tasks the audit actually examined versus how the 200/249 broken-task counts map onto that total.
- It is not stated whether OpenAI or the SWE-Bench Pro maintainers plan to fix or remove the flagged tasks, or whether OpenAI will re-audit after any such fixes.
- The source does not clarify how this audit's findings affect comparisons of past model releases that already reported SWE-Bench Pro scores.

## Related

- [[OpenAI]]
- [[Evaluation and Benchmarks]]
- [[Code Models]]
- [[Why We No Longer Evaluate SWE-bench Verified]]: the earlier audit that led OpenAI to recommend SWE-Bench Pro in the first place.
