Source URL: https://huggingface.co/blog/huggingface/one-year-since-the-deepseek-moment-blog-3
Title: The Future of the Global Open-Source AI Ecosystem: From DeepSeek to AI+

# The Future of the Global Open-Source AI Ecosystem: From DeepSeek to AI+

Published February 3, 2026

Adina Yakefu, Irene Solaiman (Hugging Face)

Third and final post in Hugging Face's series on China's open source AI ecosystem since DeepSeek R1, examining the trajectories of prominent Chinese AI organizations and positing future directions for global open source.

## China's Organic Open Source AI Ecosystem

DeepSeek is the most-followed organization on Hugging Face; Qwen is fourth. The most popular papers on the Hub largely come from Chinese organizations (ByteDance, DeepSeek, Tencent, Qwen). The post profiles several organizational trajectories:

- **Alibaba/Qwen**: positioned open source as an ecosystem/infrastructure strategy rather than a single flagship model, expanding continuously across sizes/tasks/modalities. By mid-2025, Qwen had over 113k derivative models on Hugging Face and 200k+ repos tagging Qwen — more than Meta's Llama (27k) or DeepSeek (6k) — with Alibaba as an organization having nearly as many derivatives as Google and Meta combined.
- **Tencent**: moved from "borrowing to building" — initially integrating DeepSeek into consumer products via plug-in-style integration and internal validation, then from May 2025 accelerating its own open releases (Tencent Hunyuan/HY) in vision, video, and 3D, areas where it already had strength.
- **ByteDance**: follows an "AI application factory" approach, selectively open-sourcing high-value components (UI-TARS-1.5, Seed-Coder, the SuperGPQA dataset) while keeping competitive focus on its product entry points; its Doubao app surpassed 100M DAU in December 2025 despite a relatively low-profile open-source presence.
- **Baidu**: shifted after years of closed-model prioritization toward open release (e.g. the Ernie 4.5 series) alongside renewed investment in its PaddlePaddle framework and Kunlunxin AI chip (which announced an IPO Jan 1, 2026).

## The Normalcy of "DeepSeek Moments"

Moonshot, Z.ai, and MiniMax adjusted rapidly post-R1; Kimi K2, GLM-4.5, and MiniMax M2 all earned places on AI-World's open-model milestone rankings. Kimi K2's open-sourcing was itself widely called "another DeepSeek moment." Moonshot reportedly raised ~$500M by end of 2025 targeting AGI/agent commercialization, without (unlike Z.ai and MiniMax) announcing IPO plans. Application-first companies (Xiaohongshu, Bilibili, Xiaomi, Meituan) began training and releasing their own models once strong reasoning became cheaply available via open source, tuning models to their specific businesses rather than depending on external providers. Research institutions (BAAI, Shanghai AI Lab) redirected effort toward toolchains, evaluation systems, data platforms, and deployment infrastructure (FlagOpen, OpenDataLab, OpenCompass) rather than chasing single-model performance.

## Foundations for the Future

The post frames the defining shift as a full chain forming — models open-sourced and extended, deployments reused and scaled, hardware/software coordinated and swapped, governance embedded and audited — built atop years of accumulated infrastructure investment since 2017 (the "East Data, West Compute" national compute-hub strategy). China's total compute capacity is cited at ~1590 EFLOPS as of 2025, with intelligent (AI-specific) compute capacity reportedly growing ~43% year-over-year, and average data-center PUE falling to ~1.46. The post frames the August 2025 "AI+" action plan as a shift from the 2017 plan's foundation-building toward large-scale deployment and deep integration, distinct from an AGI-first pursuit, with R1 serving as the catalyst that activated already-built compute/energy/data infrastructure.

## Key Claims

- DeepSeek is the most-followed organization on Hugging Face overall; Qwen is fourth.
- By mid-2025, Qwen had over 113,000 derivative models on Hugging Face and 200,000+ repositories tagging it, more than Meta's Llama (27k) or DeepSeek (6k) individually; Alibaba's total derivatives nearly match Google's and Meta's combined.
- ByteDance's Doubao app surpassed 100 million daily active users in December 2025, despite the company's relatively low-profile open-source posture.
- China's total compute capacity is cited at ~1590 EFLOPS as of 2025, with AI-specific ("intelligent") compute capacity reportedly growing ~43% year-over-year and average data-center PUE improving to ~1.46.
- The August 2025 "AI+" action plan is framed as a shift from the 2017 "New Generation AI Development Plan"'s foundation-building toward large-scale deployment/integration, distinct from an AGI-maximalist strategy.
- Kimi K2's open-sourcing is described as "another DeepSeek moment," reportedly accompanying ~$500M in funding raised by Moonshot by end of 2025 (no IPO announced, unlike Z.ai and MiniMax).

## Figures

No figures were extracted for this ingest, per this batch's no-figure-download policy; a referenced Hugging Face PaperVerse Explorer screenshot is described inline above but not downloaded.

## Entities

- [[Hugging Face]] — publishes the series and supplies underlying Hub data (derivative counts, follower counts, paper upvotes).
- [[DeepSeek]] — most-followed org on Hugging Face per this post; central to the series' "DeepSeek Moment" framing.
- [[Qwen]] — profiled as having the largest derivative-model ecosystem on Hugging Face.
- [[Z.ai]] — one of the startups (with Moonshot, MiniMax) credited with rapid post-R1 open-source momentum.

## Questions & Gaps

- Compute-capacity and PUE figures are attributed to unnamed "sources in China" rather than a specific, checkable primary source.
- The post explicitly frames itself as forward-looking/speculative in its final section ("posit future directions"), so several claims about 2026 trajectory are stated as expectation rather than observed fact.

## Related

- [[One Year Since the "DeepSeek Moment"]] — first post in this series.
- [[Architectural Choices in China's Open-Source AI Ecosystem: Building Beyond DeepSeek]] — second post in this series.
