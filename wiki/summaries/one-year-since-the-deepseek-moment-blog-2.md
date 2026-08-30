# Architectural Choices in China's Open-Source AI Ecosystem: Building Beyond DeepSeek

**Source**: `raw/one-year-since-the-deepseek-moment-blog-2/full-article.html`, `raw/one-year-since-the-deepseek-moment-blog-2/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

Second post in Hugging Face's three-part series on China's open-source AI ecosystem since DeepSeek R1 (following [[One Year Since the "DeepSeek Moment"]]), focused on the architectural and hardware choices Chinese companies made as openness became the norm. In the past year, leading Chinese models (Kimi K2, MiniMax M2, Qwen3, and R1 itself) almost unanimously adopted Mixture-of-Experts architectures, which the post frames as a natural fit for China's real-world constraints: MoE dynamically activates different numbers of experts by task complexity rather than requiring every inference to consume full resources. The overall 2025 direction was less about maximal performance and more about sustainable operation, flexible deployment, and continuous evolution.

Starting February 2025, open-source activity expanded beyond text into multimodal and agentic directions in parallel (any-to-any models, text-to-image, image-to-video, text-to-video, TTS, 3D, and agents), with the community pushing full engineering assets (inference deployment, datasets/evaluation, toolchains, workflows) rather than just weights. Models in the 0.5B-30B range proved easiest to run locally and integrate into workflows (Qwen 1.5-0.5B has the most derivative models in the Qwen series), with large MoE models (100B-700B) increasingly used as capability ceilings or "teacher models" distilled down into many smaller practical models. After R1, Apache 2.0 became close to the default license choice for Chinese open models, lowering production-adoption friction versus bespoke licenses.

The most significant shift was model releases increasingly aligning with inference frameworks, quantization formats, serving engines, and edge runtimes targeting domestic hardware. DeepSeek-V3.2-Exp shipped with day-zero, reproducible inference support on Huawei Ascend and Cambricon chips, not just cloud demos. On training: Ant Group's Ling models used optimized training on domestic chips to approach near-H800 performance while cutting 1-trillion-token training cost by about 20%; Baidu's Qianfan-VL was trained on a cluster of 5,000+ Baidu Kunlun P800 accelerators; by early 2026 Zhipu's GLM-Image and China Telecom's TeleChat3 were both announced as trained entirely on domestic chips, marking domestic compute's move from inference-only into training. On serving: Moonshot AI open-sourced its Mooncake serving system (with prefill/decode separation), Baidu's FastDeploy 2.0 emphasized extreme quantization and cluster-level optimization, and Alibaba pursued full-stack integration across models, inference frameworks, quantization, and cloud deployment. The post also notes a countervailing signal of reported compute constraints inside China (e.g. Zhipu AI reportedly restricting usage amid a computing crunch).

## Key Claims

- Leading Chinese open models (Kimi K2, MiniMax M2, Qwen3, R1 itself) have almost unanimously converged on Mixture-of-Experts architectures as a cost/capability tradeoff suited to China's compute constraints.
- Apache 2.0 became close to the default open-source license choice among Chinese labs after R1, reducing production-adoption friction relative to bespoke licenses.
- DeepSeek-V3.2-Exp shipped with day-zero, reproducible inference support on Huawei Ascend and Cambricon chips (not just cloud demos).
- Ant Group's Ling models, trained with optimized techniques on domestic chips, approached near-H800 performance and cut 1-trillion-token training cost by ~20%; Baidu's Qianfan-VL was trained on 5,000+ Kunlun P800 accelerators.
- By early 2026, Zhipu's GLM-Image and China Telecom's TeleChat3 were both announced as trained entirely on domestic chips, domestic hardware moving from inference-only into the training pipeline.
- Moonshot AI open-sourced its Mooncake serving system (with prefill/decode separation); Baidu's FastDeploy 2.0 and Alibaba's Qwen full-stack integration are cited as parallel serving/infrastructure open-sourcing efforts.
- The post flags a countervailing signal: reported compute constraints inside China (e.g. Zhipu AI reportedly restricting usage amid a compute crunch) even as the broader hardware-first trend accelerates.

## Figures

No figures were extracted for this ingest, per this batch's no-figure-download policy; referenced charts (license-permissiveness trend graph, Chinese Open Source Heatmap-derived charts) are described inline above but not downloaded.

## Entities

- [[Hugging Face]] — publishes the series.
- [[DeepSeek]] — R1's MoE architecture and its day-zero domestic-hardware support (V3.2-Exp) are discussed as a throughline.
- [[NVIDIA]] — referenced as the incumbent hardware baseline domestic Chinese chips (Huawei Ascend, Cambricon, Baidu Kunlun) are being compared against, and as the subject of ongoing U.S. export-control questions (H200 sales) mentioned as an open question for China's response.

## Questions & Gaps

- The post raises but does not resolve how China will respond to U.S. hardware export controls (e.g. NVIDIA H200 sales) as an open strategic question.
- No independent verification is given for vendor-reported efficiency claims (e.g. Ant Group's ~20% training-cost reduction, near-H800 performance parity), which are presented as company-disclosed figures.

## Related

- [[One Year Since the "DeepSeek Moment"]] — first post in this series.
- [[The Future of the Global Open-Source AI Ecosystem: From DeepSeek to AI+]] — third and final post in this series.
