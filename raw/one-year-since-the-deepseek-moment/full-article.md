Source URL: https://huggingface.co/blog/huggingface/one-year-since-the-deepseek-moment
Title: One Year Since the "DeepSeek Moment"

# One Year Since the "DeepSeek Moment"

Published January 20, 2026

Adina Yakefu, Irene Solaiman (Hugging Face)

First of a three-part series examining China's open source AI community's advancements in the year since January 2025's "DeepSeek Moment" (the release of DeepSeek's R1 model) and its reverberations across the entire ecosystem. This first post addresses strategic changes and the explosion of new open models and open source players; the second covers architectural and hardware choices; the third analyzes prominent organizations' trajectories and the future of the global open source ecosystem.

## The Seeds of China's Organic Open Source AI Ecosystem

Before R1, China's AI industry was still largely centered on closed models; open models existed but were mostly confined to research communities or niche scenarios like privacy-sensitive applications, and were not the default choice for most companies given tight compute resources. DeepSeek's R1 lowered the barrier to advanced AI capabilities and offered a pattern to follow, giving Chinese AI development something valuable: time. It showed rapid progress was possible even with limited resources through open source and fast iteration, aligning with China's 2017 "AI+" strategy of combining AI with industry early while building compute capacity long-term.

## DeepSeek R1: A Turning Point

R1 was the first open Chinese model to enter global mainstream rankings and quickly became the most-liked model on Hugging Face of all time. Its significance lay less in raw capability than in lowering three barriers:

- **Technical barrier**: by openly sharing reasoning paths and post-training methods, R1 turned advanced reasoning from a closed-API capability into a downloadable, distillable, fine-tunable engineering asset, reducing the need to train massive models from scratch for strong reasoning.
- **Adoption barrier**: released under the MIT license, R1 was straightforward to use, modify, and redistribute; companies that had relied on closed models began bringing it directly into production, and community discussion shifted from "which model scores higher" to "how do we deploy it, reduce cost, integrate it."
- **Psychological barrier**: the question shifted from "can we do this?" to "how do we do this well?", changing decision-making across many companies and giving the Chinese AI community a rare moment of sustained global attention.

## From DeepSeek to AI+: Strategic Realignment

Since R1's release, competition shifted from model-to-model comparisons toward system-level capabilities. The number of Chinese organizations releasing state-of-the-art models and repositories skyrocketed: Baidu went from zero Hugging Face releases in 2024 to over 100 in 2025; ByteDance and Tencent each increased releases 8-9x; Moonshot's open release of Kimi K2 was widely called "another DeepSeek moment." Zhipu AI's GLM and Alibaba's Qwen expanded from publishing weights to building full engineering systems and ecosystem interfaces. Downloads for newly created (<1 year old) Chinese models have surpassed any other country, including the U.S. The post frames this less as coordinated collaboration and more as alignment under shared technical, economic, and regulatory constraints around compute, cost, and compliance.

## Global Reception and Response

Positive sentiment toward open source has increased worldwide, especially in the U.S., alongside recognition of open source's role in global competitiveness. DeepSeek has been heavily adopted in Southeast Asia and Africa, where multilingual support, open-weight availability, and cost considerations favor enterprise use. Western organizations often still seek non-Chinese models for commercial deployment (OpenAI's gpt-oss, AI2's Olmo, Meta's Llama 4, Mistral's Mistral Large 3), yet major Western releases sometimes build directly on Chinese models — Deep Cogito's Cogito v2.1 (Nov 2025), described as a leading U.S. open-weight model, is a fine-tuned version of DeepSeek-V3. The American Truly Open Model (ATOM) project cites DeepSeek's momentum as a motivator for U.S.-led open-weight efforts, while also noting heavy early adoption of OpenAI's gpt-oss.

## Key Claims

- DeepSeek R1 (Jan 2025, MIT license) became the most-liked model on Hugging Face of all time, ending U.S. dominance of the top-liked-models list.
- Baidu went from zero open releases on Hugging Face in 2024 to over 100 in 2025; ByteDance and Tencent each increased releases 8-9x over the same period.
- Downloads for newly created (<1 year old) Chinese-developed models have surpassed those of any other country, including the U.S.
- Deep Cogito's Cogito v2.1 (Nov 2025), cited as a leading U.S. open-weight model, is itself a fine-tuned version of DeepSeek-V3 — illustrating cross-pollination even amid a "seek non-Chinese alternatives" framing in parts of the Western market.
- The post frames the described convergence among Chinese AI organizations as alignment under shared constraints (compute, cost, compliance) rather than explicit coordination.

## Figures

No figures were extracted for this ingest, per this batch's no-figure-download policy; referenced charts (Hugging Face Repository Growth of Chinese Companies, Top Newly Created Models by Week, Chinese Open Source Heatmap) are described inline above but not downloaded.

## Entities

- [[Hugging Face]] — publishes the three-part series and supplies the underlying Hub download/repository data.
- [[DeepSeek]] — R1's release is the "DeepSeek Moment" the series analyzes.

## Questions & Gaps

- The post's claim of "alignment under constraint, not coordination" among Chinese AI labs is asserted rather than empirically distinguished from actual coordination.
- No head-to-head reproducibility or benchmark comparison is given for R1 against contemporaneous closed models; the analysis is about ecosystem/adoption dynamics rather than model capability.

## Related

- [[Architectural Choices in China's Open-Source AI Ecosystem: Building Beyond DeepSeek]] — second post in this series.
- [[The Future of the Global Open-Source AI Ecosystem: From DeepSeek to AI+]] — third and final post in this series.
- [[State of Open Source on Hugging Face: Spring 2026]] — later HF ecosystem report citing this series.
