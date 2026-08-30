# Open-R1: A Fully Open Reproduction of DeepSeek-R1

**Source**: `raw/open-r1/full-article.html` (500 KB), `raw/open-r1/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

Hugging Face's announcement of the Open-R1 project, launched days after DeepSeek released R1. DeepSeek-R1 matched or beat OpenAI's o1 on reasoning tasks and shipped a technical report describing the recipe: a 671B MoE base model (DeepSeek-V3, trained for roughly $5.5M using Multi-Token Prediction, Multi-Head Latent Attention, and heavy hardware optimization), then two RL-trained variants. DeepSeek-R1-Zero skipped SFT entirely and trained purely with Group Relative Policy Optimization (GRPO) against a rule-based reward for answer accuracy and output structure; it learned to decompose problems and verify its own outputs but produced hard-to-read responses. DeepSeek-R1 added a "cold start" SFT phase on curated examples for readability, followed by further RL and rejection sampling with both preference-based and verifiable rewards.

What DeepSeek released was only the model weights, not the training code or datasets. Open-R1 set out to reconstruct the missing pieces in three steps: distill a high-quality reasoning dataset from R1 to reproduce the R1-Distill models, replicate the pure-RL pipeline behind R1-Zero with new large-scale math/reasoning/code datasets, and demonstrate the full base-to-SFT-to-RL pipeline. The project explicitly planned to extend past math into code and other verifiable domains like medicine, and to publish reproducible datasets, training recipes, and negative results along the way. This post is the project's opening announcement rather than a report of results; those come in the update posts (see [[Open R1: Update #1]] through [[Open R1: Update #4]]).

## Key Claims

- DeepSeek-V3 (671B MoE base model) was reported to cost ~$5.5M to train, competitive with Sonnet 3.5 and GPT-4o.
- DeepSeek-R1-Zero used pure GRPO with rule-based reward (accuracy + format), no SFT; it developed step-decomposition and self-verification but produced low-readability outputs.
- DeepSeek-R1 added a cold-start SFT phase plus further RL/rejection-sampling with both human-preference and verifiable rewards to fix readability while retaining reasoning quality.
- DeepSeek released only model weights; no training code or datasets, prompting the Open-R1 reproduction effort.
- Open-R1's three-step plan: (1) distill R1-Distill-equivalent models, (2) reproduce the pure-RL R1-Zero pipeline with new datasets, (3) show a full base -> SFT -> RL pipeline works end to end.

## Figures

No figures were extracted for this ingest; the post's architecture/plan-of-attack diagrams are described inline above but not downloaded, per this batch's no-figure-download policy.

## Entities

- [[Hugging Face]] — publishes the post and hosts the open-r1 org/repo.
- [[DeepSeek]] — creator of DeepSeek-R1/R1-Zero/V3, the model being reproduced.

## Questions & Gaps

- The post does not give a concrete timeline or compute budget for Open-R1's own reproduction effort.
- No detail yet on how "verifiable" rewards will be defined for domains beyond math (e.g. medicine).

## Related

- [[Open R1: Update #1]] — first progress report: evaluation reproduction, GRPO landing in TRL, synthetic-data-generation throughput tuning.
- [[Open R1: Update #2]] — OpenR1-Math-220k dataset construction and community GRPO experiments.
- [[Open R1: Update #3]] — CodeForces-CoTs dataset, IOI benchmark, OlympicCoder models.
- [[Open R1: Update #4]] — DeepSeek-V3-0324 model update coverage and open-model safety discussion.
- [[Mini-R1: Reproduce Deepseek R1 "Aha Moment", a RL Tutorial]] — community GRPO reproduction using the Countdown Game, referenced as inspiration.
- [[GRPO]]
- [[Reasoning Models]]
- [[Reinforcement Learning Topic]]
