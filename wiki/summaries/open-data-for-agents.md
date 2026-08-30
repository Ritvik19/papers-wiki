# Data for Agents

**Source**: `raw/open-data-for-agents/full-article.html`, `raw/open-data-for-agents/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

An NVIDIA Nemotron team essay arguing that agentic AI needs open data, and that synthetic data is the mechanism for scaling it. The core claim: an agent that cannot recover from a broken API call or an unfamiliar workflow "is not really an agent, it is an autocompleter with tools." Closing that gap is fundamentally a data problem (software-engineering traces, tool-use failures, multi-step reasoning, retrieval, safety, user simulation, workflow execution, physical-world interaction), which is where NVIDIA Nemotron's open data products sit. NVIDIA notes nearly 145 ICML papers cite Nemotron models/datasets, with synthetic data playing a role throughout that ecosystem (Nemotron-CC enhancing Common Crawl for pretraining, Nemotron-CC-Math adding synthetic math questions, Nemotron Pretraining spanning trillions of tokens across general/code/math/synthetic data). The argument is that open weights are only part of reproducibility; datasets, curation choices, training recipes, and evaluation methods matter too, especially for agents, since inspectable/explainable agent behavior requires understanding the data that shaped tool calls, workflow execution, and retrieval.

Citing NVIDIA VP of Applied Deep Learning Research Bryan Catanzaro's observation that "every company is built around a secret" (a workflow, corpus, or customer pattern competitors lack), the post frames synthetic data as a way for teams to preserve useful signal without exposing the underlying proprietary source, building a richer shared data layer without forcing anyone to be first to give away their edge. It highlights the Nemotron Post-Training v3 Prompt Atlas, an interactive visual map (over 10 trillion pretraining tokens plus millions of post-training samples, volume-sampled to reflect true mixture proportions) letting users filter by dataset, pipeline stage, domain, or tool use and zoom into semantically clustered regions (coding, safety, math, agentic behavior) to curate data or understand model behavior.

The post also covers Nemotron-Personas, locally grounded synthetic personas built with NeMo Data Designer that mirror official regional demographic/geographic statistics, motivated by the observation that data quality is often local rather than universal (e.g. a toxicity classifier trained on English internet data can miss hostility in Korean or Japanese, where aggression is encoded via politeness level rather than vocabulary). As of this post, the Nemotron-Personas collection had reached its tenth country, collectively representing more than 2.4 billion people; Privasis, a derivative built on Nemotron-Personas-USA, layers privacy-preserving synthetic records across medical, financial, legal, and social contexts. The essay closes on "synthetic thresholds": the idea that real workflows, human feedback, model-generated traces, simulated users, and synthetic labels increasingly intertwine, so the goal is not to pretend synthetic data is fake or harmless but to document what was generated, grounded, reviewed, and meant to test. It frames trust between organizations, not tokens, as AI's scarce resource, with openly released synthetic data as one of the few tools for building it.

## Key Claims

- Nearly 145 ICML papers cite Nemotron models and datasets, per NVIDIA's count.
- The Nemotron Post-Training v3 Prompt Atlas is an interactive, volume-sampled visual map of the Nemotron v3 post-training prompt mixture, filterable by dataset, pipeline stage, domain, and tool use.
- The Nemotron-Personas collection had reached its tenth country as of this post (launched at VivaTech Paris the prior month), collectively representing more than 2.4 billion people.
- Privasis, built on Nemotron-Personas-USA, layers privacy-preserving synthetic records across medical, financial, legal, and social domains.
- The post frames data-quality requirements as domain-specific ("more craft than formula"): reasoning needs harder problems/cleaner traces, personas need distributional fidelity/local review, agentic workflows need task diversity/failure coverage/recovery paths.

## Figures

No figures were extracted for this ingest, per this batch's no-figure-download policy; a referenced Nemotron Post-Training v3 Prompt Atlas screenshot is described inline above but not downloaded.

## Entities

- [[NVIDIA]] — publishes the Nemotron open-data ecosystem (Nemotron-CC, Nemotron-CC-Math, Nemotron Pretraining, Nemotron-Personas, Privasis, Prompt Atlas) discussed throughout.
- [[Hugging Face]] — hosts the datasets, the Prompt Atlas Space, and the blog post.

## Questions & Gaps

- The essay is argumentative/reflective rather than empirical; it does not present benchmark results showing synthetic Nemotron data measurably improves agent robustness or tool-use recovery.
- "Synthetic thresholds" is introduced as a framing concept but not given a precise operational definition or measurement method.

## Related

- [[Nemotron-Personas-India: Synthesized Data for Sovereign AI]] — one of the country-specific Nemotron-Personas releases discussed in this post.
- [[NVIDIA Releases 6 Million Multi-Lingual Reasoning Dataset]] — another Nemotron open-data release in the same ecosystem.
- [[The Open Evaluation Standard: Benchmarking NVIDIA Nemotron 3 Nano with NeMo Evaluator]]
