Source URL: https://huggingface.co/blog/nvidia/nvidia-cosmos-reason-2-brings-advanced-reasoning
Title: NVIDIA Cosmos Reason 2 Brings Advanced Reasoning To Physical AI

# NVIDIA Cosmos Reason 2 Brings Advanced Reasoning To Physical AI

Published January 5, 2026

Tsung-Yi Lin, Debraj Sinha (NVIDIA)

NVIDIA released Cosmos Reason 2, the latest advancement in open, reasoning vision language models for physical AI. Cosmos Reason 2 surpasses its previous version in accuracy and tops the Physical AI Bench and Physical Reasoning leaderboards as the #1 open model for visual understanding.

## Cosmos Reason 2: Reasoning VLM for Physical AI

Vision-language models have rapidly improved at object and pattern recognition in images, but they still struggle with tasks humans find natural: planning several steps ahead, handling uncertainty, adapting to new situations. Cosmos Reason is designed to close this gap by giving robots and AI agents stronger common sense and reasoning for solving complex problems step by step.

Cosmos Reason 2 is an open reasoning vision-language model that enables robots and AI agents to see, understand, plan, and act in the physical world. It uses common sense, physics, and prior knowledge to recognize how objects move across space and time, handle complex tasks, adapt to new situations, and solve problems step by step.

### Key Highlights

- Improved spatio-temporal understanding and timestamp precision.
- Flexible deployment from edge to cloud with 2B and 8B parameter model sizes.
- Expanded spatial understanding and visual perception: 2D/3D point localization, bounding box coordinates, trajectory data, and OCR support.
- Long-context understanding up to 256K input tokens, up from 16K in Cosmos Reason 1.
- Adaptable to multiple use cases via Cosmos Cookbook recipes.

## Popular Use Cases

**Video analytics AI agents.** Extract insights from large volumes of video data. Cosmos Reason 2 adds OCR support and 2D/3D point localization/mark understanding on top of Cosmos Reason 1's capabilities. Example: understanding text embedded in a video to determine road conditions during a rainstorm. Developers can jump-start development using the NVIDIA video search and summarization (VSS) blueprint with Cosmos Reason as the VLM; Salesforce uses this combination (with Agentforce and Cobalt robots) for workplace safety and compliance analysis.

**Data annotation and critique.** Automates high-quality annotation and critique of large, diverse training datasets by providing timestamps and detailed descriptions for real or synthetic training videos. Uber is exploring Cosmos Reason 2 for accurate, searchable video captions for autonomous vehicle training data. A co-authored fine-tuning/evaluation recipe (Reason 2 for AV Video Captioning and VQA) on annotated AV videos reported:

| Metric | Before | After | Change |
|---|---|---|---|
| BLEU | 0.113 | 0.125 | +10.6% |
| MCQ-based VQA | 80.18% | 80.85% | +0.67 pp |
| LingoQA | 63.2% | 77.0% | +13.8% |

**Robot planning and reasoning.** Acts as the "brain" for deliberate, methodical decision-making in a robot vision-language-action (VLA) model, now providing trajectory coordinates in addition to next-step determination (e.g. JSON output specifying the steps and gripper trajectory to move an object into a basket). Encord natively supports Cosmos Reason 2 in its Data Agent library and AI data platform for VLA robotics use cases. Hitachi, Milestone, and VAST Data use Cosmos Reason for robotics, autonomous driving, and traffic/workplace-safety video analytics.

(Note: figure/example images referenced in the article — road-condition OCR example, AV captioning prompt example, robot gripper trajectory JSON example — were not extracted.)

Cosmos Reason 2 can be tried on build.nvidia.com with sample prompts for bounding boxes and robot trajectories, or via uploaded videos/images. Models (2B and 8B) are downloadable on Hugging Face, with cloud availability planned for AWS, Google Cloud, and Microsoft Azure.

## Other Models in the Cosmos Family

- **Cosmos Predict 2.5**: generative model predicting future states of the physical world as video from text/image/video input; leads Physical AI Bench for quality, accuracy, and consistency; up to 30 seconds of physically/temporally consistent output per generation; pre-trained on 200 million clips; available as 2B and 14B pre-trained models plus 2B post-trained variants for multiview, action conditioning, and autonomous vehicle training.
- **Cosmos Transfer 2.5**: lightest multicontrol model for video-to-world style transfer, scaling a single simulation or spatial video across environments/lighting conditions, used with NVIDIA Isaac Sim or Omniverse NuRec for sim-to-real transformation.
- **NVIDIA GR00T N1.6**: open reasoning VLA model for humanoid robots with full-body control, using Cosmos Reason for contextual reasoning.
