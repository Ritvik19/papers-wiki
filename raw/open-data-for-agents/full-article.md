Source URL: https://huggingface.co/blog/nvidia/open-data-for-agents
Title: Data for Agents

# Data for Agents

Published July 8, 2026

Will Jennings, Jane Polak Scowcroft, Annie Surla, Yev Meyer, Rebecca Kao, Leanna Chraghchian, Chris Alexiuk, Michelle Xu, Dhruv Nathawani (NVIDIA)

An NVIDIA Nemotron team essay arguing that agentic AI needs open data, and that synthetic data is the mechanism for scaling it. The core claim: an agent that cannot recover from a broken API call or an unfamiliar workflow "is not really an agent, it is an autocompleter with tools" — closing that gap is fundamentally a data problem (software-engineering traces, tool-use failures, multi-step reasoning, retrieval, safety, user simulation, workflow execution, physical-world interaction), which is where NVIDIA Nemotron's open data products sit.

## Why Open Data, Not Just Open Weights

NVIDIA notes nearly 145 ICML papers cite Nemotron models/datasets, with synthetic data playing a role across that ecosystem: Nemotron-CC uses synthetics to enhance Common Crawl for pretraining; Nemotron-CC-Math uses synthetic math questions to improve reasoning; Nemotron Pretraining spans general, code, math, and synthetic data across trillions of tokens. The argument is that open weights are only part of reproducibility — datasets, curation choices, training recipes, and evaluation methods behind a model matter too, especially for agents, since inspectable/explainable agent behavior requires understanding the data that shaped tool calls, workflow execution, and retrieval.

## The "Secret" Problem and Synthetic Data as a Solution

Citing NVIDIA VP of Applied Deep Learning Research Bryan Catanzaro's observation that "every company is built around a secret" (a workflow, corpus, or customer pattern competitors lack), the post frames synthetic data as a way for teams to preserve useful signal without exposing the underlying proprietary source. The concern raised: if every model learns from the same narrow data pool, models converge and feel the same, but the most useful data typically sits inside organizations unwilling or unable to publish it directly. Openly released synthetic data is offered as a way to build a richer shared data layer without forcing anyone to be first to give away their edge.

## Nemotron Post-Training v3 Prompt Atlas

To make the composition of Nemotron's post-training data (over 10 trillion pretraining tokens plus millions of post-training samples) explorable, the team built the Nemotron Post-Training v3 Prompt Atlas: an interactive visual map where each point is a prompt sample drawn from the Nemotron v3 post-training collection, volume-sampled to reflect the data mixture's true proportions. Color overlays and filters let users reorganize the map by dataset, pipeline stage, domain, or tool use; since semantically similar prompts cluster together, users can zoom into a region (coding, safety, math, agentic behavior), inspect representative examples, and use that to curate data, build evals, or understand model behavior.

## Nemotron-Personas and Local Data Quality

The post argues data quality is often local rather than universal — e.g. a toxicity classifier trained on English internet data can miss hostility in Korean or Japanese, where aggression is often encoded via politeness level rather than vocabulary. Nemotron-Personas is presented as an attempt to address this: locally grounded synthetic personas mirroring official regional demographic/geographic statistics, built with NeMo Data Designer, intended to let developers test whether their systems reflect the users, languages, regions, and occupations they claim to serve (not to recreate real people). Privasis, a derivative dataset built on Nemotron-Personas-USA, layers privacy-preserving synthetic records across medical, financial, legal, and social contexts. As of this post, NVIDIA had launched its tenth country in the Nemotron-Personas collection (at VivaTech Paris the prior month), collectively representing more than 2.4 billion people.

## Ground Truths (Synthetic Data as Part of a System)

The post introduces "synthetic thresholds": points where data can no longer be treated as purely real, since real workflows, human feedback, model-generated traces, simulated users, and synthetic labels increasingly intertwine. Its position is not to treat synthetic data as fake or harmless, but to document what was generated, what was grounded, what was reviewed, and what the data is meant to test. Quality requirements differ by data type: reasoning data needs harder problems and cleaner traces; persona data needs distributional fidelity and local review; agentic workflows need task diversity, failure coverage, and recovery paths. The piece closes by framing the scarce resource in AI as trust between organizations rather than tokens, with openly released synthetic data as one of the few tools for building that trust.

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
