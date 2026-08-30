Source URL: https://huggingface.co/blog/huggingface/one-year-since-the-deepseek-moment-blog-2
Title: Architectural Choices in China's Open-Source AI Ecosystem: Building Beyond DeepSeek

# Architectural Choices in China's Open-Source AI Ecosystem: Building Beyond DeepSeek

Published January 27, 2026

Adina Yakefu, Irene Solaiman (Hugging Face)

Second post in a three-part Hugging Face series on China's open source AI ecosystem since DeepSeek R1's January 2025 release, this time focused on the architectural and hardware choices Chinese companies made as openness became the norm.

## Mixture of Experts as the Default Choice

In the past year, leading Chinese models (Kimi K2, MiniMax M2, Qwen3) almost unanimously adopted Mixture-of-Experts architectures; R1 itself was an MoE model, proving strong reasoning could be open, reproducible, and engineered in practice. Under China's real-world constraints (controlling cost while maintaining capability, ensuring models could be trained/deployed/adopted broadly), MoE emerged as a natural fit: it dynamically activates different numbers of experts by task complexity rather than requiring every inference to consume full resources or assuming uniform deployment hardware. The overall 2025 direction for Chinese open models was less about maximal performance and more about sustainable operation, flexible deployment, and continuous evolution.

## The Rush for Supremacy by Modality

Starting February 2025, open-source activity expanded beyond text into multimodal and agentic directions in parallel: any-to-any models, text-to-image, image-to-video, text-to-video, TTS, 3D, and agents. What the community pushed was not just weights but full engineering assets: inference deployment, datasets/evaluation, toolchains, workflows, edge-to-cloud coordination. StepFun released high-performing multimodal models across audio, video, and image generation/editing (its speech-to-speech Step-Audio-R1.1 reportedly beats proprietary models); Tencent's Hunyuan Video and Hunyuan 3D reflected the same shift beyond text-centric models.

## Big Preferences for Small Models

Models in the 0.5B-30B range were easier to run locally, fine-tune, and integrate into business/agent workflows — Qwen 1.5-0.5B has the most derivative models in the Qwen series. Leading players often used large MoE models (100B-700B) as capability ceilings or "teacher models," then distilled capability down into many smaller models, producing a structure of a few very large models atop many practical smaller ones.

## More Permissive Open Source Licenses

After R1, Apache 2.0 became close to the default license choice for Chinese open models, lowering friction around using, modifying, and deploying models in production compared to prescriptive/tailored licenses that add unfamiliarity and legal-review friction.

## From Model-First to Hardware-First

Model releases increasingly aligned with inference frameworks, quantization formats, serving engines, and edge runtimes targeting domestic hardware. DeepSeek-V3.2-Exp shipped with day-zero support on Huawei Ascend and Cambricon chips as reproducible inference pipelines released alongside the weights, not just cloud demos. On the training side: Ant Group's Ling models used optimized training on domestic AI chips to approach near-NVIDIA-H800 performance, cutting the cost of training 1 trillion tokens by about 20%; Baidu's Qianfan-VL models were documented as trained on a cluster of 5,000+ Baidu Kunlun P800 accelerators; by early 2026, Zhipu's GLM-Image and China Telecom's TeleChat3 were both announced as trained entirely on domestic chips, showing domestic compute moving from inference-only into training. On serving/infrastructure: Moonshot AI open-sourced its Mooncake serving system with prefill/decoding separation support; Baidu's FastDeploy 2.0 emphasized extreme quantization and cluster-level optimization; Alibaba's Qwen ecosystem pursued full-stack integration across models, inference frameworks, quantization, and cloud deployment. The post also notes reported compute constraints inside China (e.g. Zhipu AI reportedly restricting usage amid a computing crunch) as a countervailing pressure.

## Key Claims

- Leading Chinese open models (Kimi K2, MiniMax M2, Qwen3, R1 itself) have almost unanimously converged on Mixture-of-Experts architectures as a cost/capability tradeoff suited to China's compute constraints.
- Apache 2.0 became close to the default open-source license choice among Chinese labs after R1, reducing production-adoption friction relative to bespoke licenses.
- DeepSeek-V3.2-Exp shipped with day-zero, reproducible inference support on Huawei Ascend and Cambricon chips (not just cloud demos).
- Ant Group's Ling models, trained with optimized techniques on domestic chips, approached near-H800 performance and cut 1-trillion-token training cost by ~20%; Baidu's Qianfan-VL was trained on 5,000+ Kunlun P800 accelerators.
- By early 2026, Zhipu's GLM-Image and China Telecom's TeleChat3 were both announced as trained entirely on domestic chips — domestic hardware moving from inference-only into the training pipeline.
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
