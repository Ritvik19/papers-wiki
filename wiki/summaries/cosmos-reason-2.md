# NVIDIA Cosmos Reason 2 Brings Advanced Reasoning to Physical AI

**Source**: `raw/cosmos-reason-2/full-article.md`, `raw/cosmos-reason-2/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

An NVIDIA post announcing Cosmos Reason 2, the second generation of its open reasoning vision-language model for "physical AI": robots and agents that need to plan, adapt, and act in the physical world rather than just recognize objects in a still frame. The post frames the gap Cosmos Reason targets as one of common sense and multi-step reasoning: VLMs have become strong at recognition tasks but still struggle with planning several steps ahead, handling uncertainty, and adapting to novel situations, which the model addresses by combining physics/common-sense priors with step-by-step reasoning over video. Cosmos Reason 2 ships in 2B and 8B parameter sizes for edge-to-cloud deployment flexibility, extends context from Cosmos Reason 1's 16K tokens to 256K, and adds OCR, 2D/3D point localization, bounding-box output, and trajectory-coordinate output to its existing spatio-temporal understanding, topping the Physical AI Bench and Physical Reasoning leaderboards as the #1 open model for visual understanding at time of release.

Three use-case categories are highlighted with production partners. For video-analytics agents (extracting insights from large video volumes), the new OCR support lets the model read embedded text (e.g. determining road conditions during a rainstorm from visible signage), and NVIDIA's video search/summarization (VSS) blueprint pairs it as the underlying VLM; Salesforce uses this combination with Agentforce and Cobalt robots for workplace-safety and compliance analysis. For data annotation and critique (auto-generating timestamped, detailed descriptions of training video), Uber is exploring Cosmos Reason 2 for autonomous-vehicle training-data captioning; a co-authored fine-tuning/evaluation recipe on annotated AV video reports a 10.6% BLEU improvement (0.113→0.125), a 0.67-point MCQ-VQA gain (80.18%→80.85%), and a 13.8% LingoQA improvement (63.2%→77.0%) after domain-specific fine-tuning. For robot planning and reasoning, the model now outputs trajectory coordinates alongside next-step decisions (demonstrated via a JSON output specifying a gripper's path to move an object into a basket), with Encord adding native Cosmos Reason 2 support to its data-agent library for VLA robotics workflows; Hitachi, Milestone, and VAST Data are cited as production users across robotics, autonomous driving, and traffic/workplace-safety video analytics.

The models are downloadable from Hugging Face (2B and 8B), tryable directly on build.nvidia.com with sample prompts for bounding boxes and robot trajectories, and planned for availability on AWS, Google Cloud, and Microsoft Azure. Cosmos Reason 2 sits within NVIDIA's broader Cosmos family alongside Cosmos Predict 2.5 (a generative world-simulation model producing up to 30 seconds of physically consistent video from text/image/video input, pretrained on 200 million clips) and Cosmos Transfer 2.5 (a video-to-world style-transfer model for sim-to-real workflows with Isaac Sim/Omniverse NuRec); GR00T N1.6, NVIDIA's humanoid-robot VLA model, uses Cosmos Reason for its contextual reasoning.

## Key Claims

- Cosmos Reason 2 ships in 2B and 8B parameter sizes, extends context to 256K tokens (up from 16K in Cosmos Reason 1), and adds OCR, 2D/3D point localization, bounding-box coordinates, and trajectory output to its spatio-temporal reasoning capabilities.
- It tops both the Physical AI Bench and Physical Reasoning leaderboards as the #1 open model for visual understanding, per NVIDIA's own reporting.
- Uber-co-authored AV video-captioning fine-tuning recipe on Cosmos Reason 2-8B reports: BLEU 0.113→0.125 (+10.6%), MCQ-VQA 80.18%→80.85% (+0.67pp), LingoQA 63.2%→77.0% (+13.8%).
- New trajectory-coordinate output lets the model act as a VLA-style planning "brain," producing structured (JSON) step-by-step robot action plans, integrated natively by Encord for robotics data workflows.
- OCR support enables reading embedded text in video for analytics use cases (e.g. road-condition determination from visible signage), used with NVIDIA's VSS blueprint by Salesforce for workplace-safety analysis via Agentforce and Cobalt robots.
- Named production/design partners: Salesforce (video analytics/compliance), Uber (AV training-data captioning), Encord (robotics data platform), Hitachi, Milestone, and VAST Data (robotics, autonomous driving, traffic/safety analytics).
- Models are available on Hugging Face now; cloud availability on AWS, Google Cloud, and Microsoft Azure is described as forthcoming rather than live at publication.

## Figures

No figures were extracted for this ingest, per this batch's no-figure-download policy; referenced example imagery (road-condition OCR example, AV-captioning prompt example, robot-gripper trajectory JSON example) is described inline above but not downloaded.

## Entities

- [[NVIDIA]] — develops Cosmos Reason 2 and the broader Cosmos model family (Predict 2.5, Transfer 2.5, GR00T N1.6).
- [[Hugging Face]] — hosts the 2B and 8B model checkpoints and the blog post.

## Questions & Gaps

- No quantitative Physical AI Bench / Physical Reasoning leaderboard scores are given in the post itself, only the qualitative #1 ranking claim; exact margins over other open models are unclear without checking the leaderboard directly.
- The three headline use-case results (Salesforce, Uber, Encord/Hitachi/Milestone/VAST) are described at different levels of quantitative detail: only the Uber AV-captioning case includes hard benchmark numbers, while the others are described qualitatively.

## Related

- [[Nemotron 3.5 Content Safety: Customizable Multimodal Safety for Global Enterprise AI]] — contemporaneous NVIDIA model release from the same blog, in the safety rather than physical-AI domain.
- [[Welcome the NVIDIA Llama Nemotron Nano VLM to Hugging Face Hub]]
