# One Year Since the "DeepSeek Moment"

**Source**: `raw/one-year-since-the-deepseek-moment/full-article.md`, `raw/one-year-since-the-deepseek-moment/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

First of a three-part Hugging Face series (Adina Yakefu, Irene Solaiman) examining China's open-source AI community's advancements in the year since January 2025's "DeepSeek Moment" (the release of DeepSeek's R1 model) and its reverberations across the ecosystem. This post covers strategic changes and the explosion of new open models and open-source players; the second post covers architectural/hardware choices ([[Architectural Choices in China's Open-Source AI Ecosystem: Building Beyond DeepSeek]]); the third analyzes organizational trajectories and the future of the global open-source ecosystem ([[The Future of the Global Open-Source AI Ecosystem: From DeepSeek to AI+]]).

Before R1, China's AI industry was largely centered on closed models, with open models mostly confined to research or niche privacy-sensitive uses. R1 lowered the barrier to advanced AI capability and demonstrated that rapid progress was possible with limited resources through open source and fast iteration, aligning with China's 2017 "AI+" strategy of combining AI with industry early while building compute capacity long-term. The post frames R1's significance as lowering three barriers rather than simply being the most capable model: a technical barrier (openly sharing reasoning paths and post-training methods turned advanced reasoning into a downloadable, distillable, fine-tunable asset), an adoption barrier (the MIT license made it straightforward to use, modify, and redistribute, shifting community discussion from "which model scores higher" to "how do we deploy it"), and a psychological barrier (shifting the question from "can we do this?" to "how do we do this well?").

Since R1, competition shifted from model-to-model comparisons toward system-level capabilities, and the number of Chinese organizations releasing state-of-the-art models skyrocketed: Baidu went from zero Hugging Face releases in 2024 to over 100 in 2025, ByteDance and Tencent each grew releases 8-9x, and Moonshot's Kimi K2 release was itself widely called "another DeepSeek moment." The post frames this convergence as alignment under shared technical, economic, and regulatory constraints (compute, cost, compliance) rather than explicit coordination. Globally, sentiment toward open source has grown, especially in the U.S.; DeepSeek has been heavily adopted in Southeast Asia and Africa for multilingual and cost reasons, while Western organizations often still seek non-Chinese alternatives (gpt-oss, AI2's Olmo, Llama 4, Mistral Large 3) even as some major Western releases build directly on Chinese models: Deep Cogito's Cogito v2.1, cited as a leading U.S. open-weight model, is itself a fine-tune of DeepSeek-V3.

## Key Claims

- DeepSeek R1 (Jan 2025, MIT license) became the most-liked model on Hugging Face of all time, ending U.S. dominance of the top-liked-models list.
- Baidu went from zero open releases on Hugging Face in 2024 to over 100 in 2025; ByteDance and Tencent each increased releases 8-9x over the same period.
- Downloads for newly created (<1 year old) Chinese-developed models have surpassed those of any other country, including the U.S.
- Deep Cogito's Cogito v2.1 (Nov 2025), cited as a leading U.S. open-weight model, is itself a fine-tuned version of DeepSeek-V3, illustrating cross-pollination even amid a "seek non-Chinese alternatives" framing in parts of the Western market.
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
