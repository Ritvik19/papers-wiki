# State of Open Source on Hugging Face: Spring 2026

**Source**: [HF Blog](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026) ([raw](/raw/state-of-os-hf-spring-2026/full-article.md))
**Published**: March 17, 2026
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

A Hugging Face team retrospective (Avijit Ghosh, Lucie-Aimée Kaffee, Yacine Jernite, Irene Solaiman) examining how the open-source AI ecosystem shifted across competition, geography, technical trends, and emerging sub-communities over the prior year, following up on a mid-2025 analysis. It draws on Hugging Face Hub activity data plus outside analyses (Data Provenance Initiative, Interconnects, OpenRouter/a16z, MIT/Linux Foundation, ATOM Project, Longpre et al.'s "Economies of Open Intelligence") to argue open source AI is best understood as a collection of overlapping sub-ecosystems rather than one uniform market.

## Growth and concentration

Hugging Face grew to 13 million users, over 2 million public models, and more than 500,000 public datasets in 2025, with the platform's activity nearly doubling. Despite this growth, activity remains highly concentrated: about half of all models have fewer than 200 total downloads, while the top 200 most-downloaded models (0.01% of models) account for 49.6% of all downloads.

## Competition and adoption

Over 30% of the Fortune 500 now maintain verified Hugging Face accounts. Thinking Machines built its Tinker model options entirely on open weights; both open and closed models are supported side by side in popular IDEs like VS Code and Cursor. Big Tech companies continue expanding their Hub presence, with NVIDIA identified as the strongest contributor by repository-growth trend.

## Geography

China surpassed the U.S. in both monthly and overall Hugging Face downloads over the past year, with Chinese models accounting for a plurality (41%) of downloads. Industry's share of overall development fell from roughly 70% before 2022 to about 37% in 2025, while independent/unaffiliated developers rose from 17% to 39% over the same period, at times exceeding half of total usage: largely individuals and small collectives quantizing, adapting, and redistributing base models. The post points to its own three-part "DeepSeek Moment" retrospective series ([[One Year Since the "DeepSeek Moment"]], [[Architectural Choices in China's Open-Source AI Ecosystem: Building Beyond DeepSeek]], [[The Future of the Global Open-Source AI Ecosystem: From DeepSeek to AI+]]) for deeper coverage of China's ecosystem. Baidu went from zero Hub releases in 2024 to over 100 in 2025; ByteDance and Tencent each grew releases 8-9x. National sovereignty initiatives are also covered: South Korea's National Sovereign AI Initiative (LG AI Research, SK Telecom, Naver Cloud, NC AI, Upstage) had three models trend simultaneously on the Hub in February 2026, and in March 2026 South Korea partnered with U.S. startup Reflection AI on a data center deal.

## Model popularity and papers

The most-liked models on the Hub shifted in one year from predominantly U.S.-developed (Meta's Llama family) to an international mix topped by China's DeepSeek-R1. The most-upvoted papers on the Hub skew toward large organizations from the U.S. and China, with Chinese Big Tech companies (especially ByteDance) contributing a high volume of highly-upvoted work.

## Derivative models and adoption

Alibaba has more derivative models on the Hub than Google and Meta combined; the Qwen family alone has over 113,000 derivative models, rising past 200,000 when counting all models that merely tag Qwen. Smaller models are downloaded and deployed at much higher rates than very large systems: per the ATOM Project's Relative Adoption Metric, median top-10 models in the 1-9B range are downloaded only about 4x more than models above 100B, once controlling for the sheer number of small-model releases. Mean engagement duration for an open model is about 6 weeks, rewarding organizations (like DeepSeek, via V3/R1/V3.2) that ship frequent follow-on releases. The mean size of downloaded open models rose from 827M parameters (2023) to 20.8B (2025), driven by quantization and MoE architectures, while the median barely moved (326M to 406M), indicating heavy-tail usage by high-end users pulling up the mean while typical small-model usage stayed stable.

## Compute, hardware, and sub-communities

Most models remain optimized for NVIDIA GPUs, but AMD support is expanding (e.g. Stability AI's dual-platform collections); Hugging Face launched the Kernel Hub in 2025 to serve optimized kernels for both. Chinese open models increasingly ship with explicit support for domestic chips, and Alibaba has invested in inference-focused chip architectures for Chinese data centers. Robotics is flagged as one of the fastest-growing Hub sub-communities: robotics datasets grew from 1,145 (2024) to 26,991 (2025), jumping from rank 44 to the single largest dataset category on the Hub (ahead of text generation's ~5,000 datasets), aided by Hugging Face's acquisition of Pollen Robotics and continued LeRobot growth (GitHub stars nearly tripled over the year). AI-for-science is highlighted as another active area (protein folding, molecular dynamics, drug discovery), though the post notes current focus remains weighted toward literature discovery over direct experimentation.

## Key Claims

- Hugging Face reached 13M users, 2M+ public models, and 500k+ public datasets in 2025, with the top 200 most-downloaded models (0.01%) accounting for 49.6% of all downloads.
- China overtook the U.S. in Hugging Face download share in 2025, reaching a 41% plurality of downloads; Baidu went from 0 to 100+ Hub releases year-over-year, and ByteDance/Tencent each grew releases 8-9x.
- Independent/unaffiliated developers' share of Hub downloads rose from 17% (pre-2022) to 39% (2025), even as industry's share fell from ~70% to ~37%.
- Qwen alone has 113,000+ derivative models on the Hub (200,000+ counting all Qwen-tagged models), more than Meta's Llama or DeepSeek individually, and Alibaba's total derivatives nearly match Google's and Meta's combined.
- Robotics datasets grew 23x year-over-year (1,145 to 26,991), becoming the single largest dataset category on the Hub within three years, ahead of text generation (~5,000 datasets).
- Mean engagement duration for an open model release is roughly 6 weeks, and mean downloaded-model size grew from 827M to 20.8B parameters (2023 to 2025) while the median grew only from 326M to 406M.

## Figures

No figures were extracted for this ingest, per this batch's no-figure-download policy; the post's many referenced charts (repository growth, geographic downloads, derivative-model counts, robotics dataset growth, etc., largely sourced from Hugging Face, AI World, and Longpre et al.) are described inline above but not downloaded.

## Entities

- [[Hugging Face]] — publishes the report and supplies the underlying Hub activity data throughout.
- [[NVIDIA]] — identified as the strongest Big Tech contributor to Hub repository growth.
- [[Qwen]] — identified as having the largest derivative-model ecosystem on the Hub.
- [[DeepSeek]] — R1 is cited as the top most-liked Hub model, displacing Meta's Llama family from that position over the year covered.

## Questions & Gaps

- Several figures (e.g. China's 41% download plurality, the 4x adoption gap between small and large models) are drawn from third-party analyses (ATOM Project, Longpre et al.) cited but not independently re-derived in this post.
- The post's "Looking Forward" section is explicitly speculative about 2026 trends (e.g. whether Western open efforts like GPT-OSS, OLMo, and Gemma can match Qwen/DeepSeek's adoption momentum) rather than a factual claim.

## Related

- [[One Year Since the "DeepSeek Moment"]], [[Architectural Choices in China's Open-Source AI Ecosystem: Building Beyond DeepSeek]], [[The Future of the Global Open-Source AI Ecosystem: From DeepSeek to AI+]] — the three-part series this report points to for deeper coverage of China's open-source AI ecosystem.
