# OpenAI

**Type**: org  
**Tags**: #entity

## Overview

**OpenAI** is an AI research and product company (founded 2015) best known for the **GPT** model family, **ChatGPT**, and **Codex**. It ships models through ChatGPT (Plus/Pro/Business/Enterprise/Edu/Go tiers), the Codex coding agent, and an API platform (Responses and Chat Completions), and publishes a **Preparedness Framework** system card alongside most model releases covering Biological/Chemical, Cybersecurity, and AI Self-Improvement risk categories.

## Appearances

### GPT-5.x model family (official blog + system cards)

- [[GPT-5]] — Aug 2025 launch; unified router across `gpt-5-main` and `gpt-5-thinking`; safe-completions training.
- [[GPT-5.1]] — Nov 2025; warmer tone, adaptive reasoning in Instant, personality presets; GPT-5.1-Codex-Max.
- [[GPT-5.2]] — Dec 2025; GDPval-focused knowledge work gains; GPT-5.2-Codex.
- [[GPT-5.3]] — Feb-Mar 2026; GPT-5.3-Codex family, GPT-5.3-Codex-Spark, GPT-5.3 Instant.
- [[GPT-5.4]] — Mar 2026; first general-purpose model with High cybersecurity mitigations.
- [[GPT-5.5]] — Apr 2026; GB200/GB300-co-designed inference; High Bio/Chem and Cyber; GPT-5.5 Instant.
- [[GPT-5.6]] — Jul 2026 GA (preview Jun 26); Sol/Terra/Luna family; ChatGPT Work launch; first release with High designations for smaller family members alongside the flagship.
- [[GPT-6 Astra]] — Sep 2026 GA; internal [[Astra]] codename; first OpenAI model at Critical cyber under Preparedness Framework; succeeds Sol as flagship.
- [[How Two Settings Tripled Our ARC-AGI-3 Scores]] — Jul 2026 harness analysis: retained reasoning + compaction on Responses API.

### Products

- [[GPT-Live]] — full-duplex voice models (GPT-Live-1, GPT-Live-1 mini).
- [[Sora 2]] — video/audio generation model with cameo likeness controls and C2PA provenance.
- [[ChatGPT Images 2.0]] — April 2026 image generation update.
- [[OpenAI Privacy Filter]] — on-device filter that removes personal information from prompts before they reach a model.

### Safety and policy

- [[gpt-oss-safeguard]] — open-weight safety classifier reasoning models (120b/20b) for developer-authored policies.
- [[Instruction Hierarchy Challenge]] — public red-teaming challenge and dataset release for instruction-hierarchy bypasses.

### Coverage on other platforms

- [[Tricks From OpenAI gpt-oss You Can Use With Transformers]] — Hugging Face's engineering writeup on the `transformers` library upgrades (kernels, MXFP4, parallelism) built to ship gpt-oss.

### Research and evaluation methodology

- [[Ten Advances in Mathematics and Theoretical Computer Science]], [[How the Ideas Came Together]] — Aug 2026: internal [[Astra]] model proofs for ten open math/TCS problems; shipped as [[GPT-6 Astra]] Sep 2026.
- [[A Single Question to Track Progress from o3 to GPT-5.6 and Beyond]] — Jul 2026: [[Sebastien Bubeck]]'s analysis of o3 through GPT-5.6-pro one-shot mathematical proofs on self-contracted gradient flows.
- [[Implications of Large-Scale Test-Time Compute]] — Jun 2026: [[Noam Brown]]'s essay analyzing why benchmark performance is a function of test-time compute and advocating for 2D capability curves and compute-budgeted safety evaluations.
- [[Model Disproves Discrete Geometry Conjecture]], [[New Result in Theoretical Physics]], [[Where the Goblins Came From]] — model-assisted research results.
- [[Separating Signal From Noise in Coding Evaluations]], [[Why We No Longer Evaluate SWE-bench Verified]], [[Chain of Thought Controllability]] — internal evaluation-methodology posts.
- [[IndQA]] — Hindi/Indic-language benchmark.

## Notes

- Official primary sources: 39 posts at `openai.com/index/*` (blocked to `curl`, fetched via WebFetch markdown) plus system cards at `deploymentsafety.openai.com/*` (fetched via `curl`); GPT-5.6 GA announcement, ARC-AGI-3 harness post, and GA system card added 2026-07-31.
- [[Papers Explained 429 - GPT-5]], [[Papers Explained 493 - gpt oss safeguard]], [[Papers Explained 555 - IH Challenge]], and [[Papers Explained - OpenAI Privacy Filter]] are complementary Medium coverage; the pages above are the official-source complement, not a replacement.
- GPT-5.x version numbering mixes Thinking/Instant/Pro/mini/nano variants and, from GPT-5.3 onward, dedicated Codex-branded coding models; each version page merges the announcement with its system card(s).

## Related

- [[GPT-5]] — first entry in the GPT-5.x lineage.
- [[GPT-5.6]] — latest entry in the GPT-5.x lineage.
- [[Sebastien Bubeck]] — AI researcher and mathematician at OpenAI.
- [[Noam Brown]] — AI researcher at OpenAI specializing in reasoning search and test-time compute.
- [[A Single Question to Track Progress from o3 to GPT-5.6 and Beyond]] — evaluation of mathematical reasoning from o3 to GPT-5.6.
- [[Implications of Large-Scale Test-Time Compute]] — test-time compute scaling and safety evaluation framework.
- [[Preparedness Framework]] — the risk framework behind every system card.
- [[Instruction Hierarchy]] — core safety-training concept spanning the GPT-5.x line.
- [[Large Language Models]]
- [[Reasoning Models]]
- [[Agentic AI]]
- [[Safety and Alignment]]
- [[Papers Explained 429 - GPT-5]]
