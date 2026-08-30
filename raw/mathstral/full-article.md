# MathΣtral

**Source URL**: https://mistral.ai/news/mathstral/
**Published**: July 16, 2024
**Author**: Mistral AI team

We're contributing Mathstral to the science community to bolster efforts in advanced mathematical problems requiring complex, multi-step logical reasoning. The Mathstral release is part of our broader effort to support academic projects—it was produced in the context of our collaboration withProject Numina.

Akin to Isaac Newton in his time, Mathstral stands on the shoulders of Mistral 7B and specializes in STEM subjects. It achieves state-of-the-art reasoning capacities in its size category across various industry-standard benchmarks. In particular, it achieves 56.6% on MATH and 63.47% on MMLU, with the following MMLU performance difference by subject between Mathstral 7B and Mistral 7B.

![Mathstral 7B breakdown by subject](/_astro/996b99d1-b61b-46ce-b1eb-4ff4e981aeb4_Z2fuvn2.webp?dpl=6a22ec9594e7d400080f6dd3)

Mathstral is another example of the excellent performance/speed tradeoffs achieved when building models for specific purposes – a development philosophy we actively promote in la Plateforme, particularly with its newfine-tuning capabilities.

![Mathstral 7B detailed benchmarks](/_astro/d2d77e13-903b-4b86-a0fb-771b0c7c9b15_Z1RncBc.webp?dpl=6a22ec9594e7d400080f6dd3)

Mathstral can achieve significantly better results with more inference-time computation: Mathstral 7B scores68.37%on MATH with majority voting and74.59%with a strong reward model among 64 candidates.

Mathstral is an instructed model – use it or fine-tune it as such, referring to our documentation. Weights are hosted onHuggingFace. You can try Mathstral now withmistral-inferenceand adapt it withmistral-finetune.

We thank ProfessorPaul Bourdonfor curating the GRE Math Subject Test problems used in our evaluation.
