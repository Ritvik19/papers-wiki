# Papers Explained: Kimi K2.5

Papers Explained: Kimi K2.5

Papers Explained: Kimi K2.5

Kimi K2.5 is an open-source multimodal agentic model, which emphasizes the joint optimization of text and vision so that two modalities…

Papers Explained: Kimi K2.5

Kimi K2.5 is an open-source multimodal agentic model, which emphasizes the joint optimization of text and vision so that two modalities enhance each other. This includes a series of techniques such as joint text-vision pre-training, zero-vision SFT, and joint text-vision reinforcement learning.

The model is available on HuggingFace.

Joint Optimization of Text and Vision

Kimi K2.5 is a native multimodal model built upon Kimi K2 through large-scale joint pre-training on approximately 15 trillion mixed visual and text tokens. Ablation studies were conducted varying the vision ratio and vision injection timing while keeping the total vision and text token budgets fixed. The vision ratio has minimal impact on final multimodal performance. In fact, early fusion with a lower vision ratio yields better results given a fixed total vision-text token budget. This motivates a native multimodal pre-training strategy: rather than aggressive vision-heavy training concentrated at the end, a moderate vision ratio integrated early in the training process allows the model to naturally develop balanced multimodal representations while benefiting from extended co-optimization of both modalities.

Zero-Vision SFT

Pretrained VLMs do not naturally perform vision-based tool-calling, which poses a cold-start problem for multimodal RL. A novel approach, zero-vision SFT, uses only text SFT data to activate the visual, agentic capabilities during post-training. In this approach, all image manipulations are proxied through programmatic operations in IPython, effectively serving as a generalization of traditional vision tool-use. This “zero-vision” activation enables diverse reasoning behaviors, including pixel-level operations such as object size estimation via binarization and counting, and generalizes to visually grounded tasks such as object localization, counting, and OCR.

Joint Multimodal Reinforcement Learning

Following the zero-vision SFT, the model requires further refinement to reliably incorporate visual inputs into reasoning. Text-initiated activation alone exhibits notable failure modes: visual inputs are sometimes ignored, and images may not be attended to when necessary.

Visual grounding and counting: Accurate localization and enumeration of objects within images;
Chart and document understanding: Interpretation of structured visual information and text extraction;
Vision-critical STEM problems: Mathematical and scientific questions filtered to require visual inputs.

Outcome-based RL on these tasks improves both basic visual capabilities and more complex agentic behaviors. Extracting these trajectories for rejection-sampling fine-tuning (RFT) enables a self-improving data pipeline, allowing subsequent joint RL stages to leverage richer multimodal reasoning traces.

To investigate potential trade-offs between visual and textual performance, text-only benchmarks were evaluated before and after visual RL. Surprisingly, outcome-based visual RL produced measurable improvements in textual tasks, including MMLU-Pro (84.7% → 86.4%), GPQA-Diamond (84.3% → 86.4%), and LongBench v2 (56.7% → 58.9%). Analysis suggests that visual RL enhances calibration in areas requiring structured information extraction, reducing uncertainty on queries that resemble visually grounded reasoning (e.g., counting, OCR). These findings indicate that visual RL can contribute to cross-modal generalization, improving textual reasoning without observable degradation of language capabilities.

Motivated by the finding that robust visual capabilities can emerge from zero-vision SFT and vision RL further enhances general text abilities, a joint multimodal RL paradigm is adopted during Kimi K2.5’s post-training. RL domains are organized not by input modality but by abilities: knowledge, reasoning, coding, agentic, etc. These domain experts jointly learn from both pure-text and multimodal queries, while the Generative Reward Model (GRM) similarly optimizes across heterogeneous traces without modality barriers.

Agent Swarm and Parallel Agent Reinforcement Learning (PARL)

Instead of executing a task as a reasoning chain or relying on pre-specified parallelization heuristics, K2.5 initiates an Agent Swarm through dynamic task decomposition, subagent instantiation, and parallel subtask scheduling. Importantly, parallelism is not presumed to be inherently advantageous; decisions regarding whether, when, and how to parallelize are explicitly learned through environmental feedback and RL-driven exploration.

The PARL framework adopts a decoupled architecture comprising a trainable orchestrator and frozen subagents instantiated from fixed intermediate policy checkpoints. This design deliberately avoids end-to-end co-optimization to circumvent two fundamental challenges: credit assignment ambiguity and training instability. In this multi-agent setting, outcome-based rewards are inherently sparse and noisy; a correct final answer does not guarantee flawless subagent execution, just as a failure does not imply universal subagent error. By freezing the subagents and treating their outputs as environmental observations rather than differentiable decision points, high-level coordination logic is disentangled from low-level execution proficiency, leading to more robust convergence. To improve efficiency, the orchestrator is first trained using small-size subagents before transitioning to larger models.

Training a reliable parallel orchestrator is challenging due to the delayed, sparse, and non-stationary feedback inherent in independent subagent execution. To address this, the PARL reward is defined as:

The performance reward rperf evaluates the overall success and quality of the solution y for a given task x.
The reward rparallel is introduced to mitigate serial collapse a local optimum where the orchestrator defaults to single agent execution. By incentivizing subagent instantiation, this term encourages the exploration of concurrent scheduling spaces.
The rfinish reward focuses on the successful completion of assigned subtasks. It is used to prevent spurious parallelism, a reward-hacking behavior in which the orchestrator increases parallel metrics dramatically by spawning many subagents without meaningful task decomposition.

To ensure the final policy optimizes for the primary objective, the hyperparameters λ1 and λ2 are annealed to zero over the course of training.

Model Architecture

The foundation of Kimi K2.5 is Kimi K2, a trillion-parameter mixture-of-experts (MoE) transformer model pre-trained on 15 trillion high-quality text tokens. Kimi K2 employs the token-efficient MuonClip optimizer with QK-Clip for training stability. The model comprises 1.04 trillion total parameters with 32 billion activated parameters, utilizing 384 experts with 8 activated per token (sparsity of 48).

The multimodal architecture of Kimi K2.5 consists of three components: a three-dimensional native-resolution vision encoder (MoonViT-3D), an MLP projector, and the Kimi K2 MoE language model.

Initialized from SigLIP-SO-400M, MoonViT incorporates the patch packing strategy from NaViT, where single images are divided into patches, flattened, and sequentially concatenated into 1D sequences, thereby enabling efficient simultaneous training on images at varying resolutions.

To maximize the transfer of image understanding capabilities to video, MoonViT-3D is introduced with a unified architecture, fully shared parameters, and a consistent embedding space. By generalizing the “patch n’ pack“ philosophy to the temporal dimension, up to four consecutive frames are treated as a spatiotemporal volume: 2D patches from these frames are jointly flattened and packed into a single 1D sequence, allowing the identical attention mechanism to operate seamlessly across both space and time. While the extra temporal attention improves understanding on high-speed motions and visual effects, the sharing maximizes knowledge generalization from static images to dynamic videos, achieving strong video understanding performance without requiring specialized video modules or architectural bifurcation. Prior to the MLP projector, lightweight temporal pooling aggregates patches within each temporal chunk, yielding 4× temporal compression to significantly extend feasible video length.
Overview of training stages.
Pre-training Pipeline

Kimi K2.5’s pre-training builds upon the Kimi K2 language model checkpoint and processes approximately 15T tokens across three stages:

Standalone ViT training to establish a robust native-resolution visual encoder.
Joint pre-training to simultaneously enhance language and multimodal capabilities.
Mid-training on high-quality data and long-context activation to refine capabilities and extend context windows.

The MoonViT-3D is continual pre-trained from SigLIP on image-text and video-text pairs, where the text components consist of a variety of targets: image alt texts, synthetic captions of images and videos, grounding bboxes, and OCR texts. This continual pre-training does not include a contrastive loss, but incorporates solely cross-entropy loss Lcaption for caption generation conditioned on input images and videos.

A two-stage alignment strategy is adopted:

The MoonViT-3D is updated to align it with Moonlight-16B-A3B via the caption loss, consuming about 1T token. This stage allows MoonViT-3D to primarily understand high-resolution images and videos.
Only the MLP projector is updated to bridge the ViT with the 1T LLM for smoother joint pre-training.

The joint pre-training stage continues from a near-end Kimi K2 checkpoint over an additional 15T vision-text tokens at 4K sequence length. The data recipe extends Kimi K2’s pre-training distribution by introducing unique tokens, adjusting data proportions with increased weight on coding-related content, and controlling maximum epochs per data source. The third stage performs long-context activation with integrated higher-quality mid-training data, sequentially extending context length via YaRN interpolation.

The Kimi K2.5 pre-training text corpus comprises curated, high-quality data spanning four primary domains: Web Text, Code, Mathematics, and Knowledge. For each domain, rigorous correctness and quality validation were performed, and targeted data experiments were designed to ensure the curated dataset achieved both high diversity and effectiveness. Code-centric data was upweighted, significantly expanding:

Repository-level code supporting cross-file reasoning and architectural understanding
Issues, code reviews and commit histories from the internet capturing real-world development patterns
Code-related documents retrieved from PDF and webtext corpora

The multimodal pre-training corpus includes seven categories: caption, interleaving, OCR, knowledge, perception, video, and agent data.

Caption data provides fundamental modality alignment, with strict limits on synthetic captions to mitigate hallucination.
Image-text interleaving data from books, web pages, and tutorials enables multi-image comprehension and longer context learning.
OCR data spans multilingual text, dense layouts, and multi- page documents.
Knowledge data incorporates academic materials processed via layout parsers to develop visual reasoning capabilities.

Furthermore, a specialized multimodal problem-solving corpus is curated to improve reasoning within STEM domains.

This data is aggregated through targeted retrieval and web crawling; for informational content lacking explicit query formats, in-context learning is employed to automatically reformulate raw materials into structured academic problems spanning K-12 to university levels. To bridge the modality gap between visual layouts and code data, extensive image-code paired data is incorporated. This includes a diverse array of code formats such as HTML, React, and SVG, among others paired with their corresponding rendered screenshots, enabling the model to align abstract structural logic with concrete visual geometry.

For agentic and temporal understanding, GUI screenshots and action trajectories are collected across desktop, mobile, and web environments, including human-annotated demonstrations. Video data from diverse sources enables both hour-long video comprehension and fine-grained spatio-temporal perception. Additionally, grounding data is incorporated to enhance fine-grained visual localization, including perception annotations (bounding boxes) and point-based references. A new contour-level segmentation task is introduced for pixel-level perception learning. All data undergoes rigorous filtering, deduplication, and quality control to ensure high diversity and effectiveness.

Post Training

Supervised Fine Tuning

K2.5 was developed by synthesizing high-quality candidate responses from K2, K2 Thinking and a suite of proprietary in-house expert models. The data generation strategy employs specialized pipelines tailored to specific domains, integrating human annotation with advanced prompt engineering and multi-stage verification. This methodology produced a large-scale instruction-tuning dataset featuring diverse prompts and intricate reasoning trajectories.

Reinforcement Learning

For each problem x sampled from a dataset D, K responses {y1, . . . , yK } are generated using the previous policy πold. The model πθ is optimized with respect to the following objective:

This loss function departs from the policy optimization algorithm used in K1.5 by introducing a token-level clipping mechanism designed to mitigate the off-policy divergence amplified by discrepancies between training and inference frameworks. The mechanism functions as a simple gradient masking scheme: policy gradients are computed normally for tokens with log-ratios within the interval [α, β ], while gradients for tokens falling outside this range are zeroed out. Notably, a key distinction from standard PPO clipping is that the method relies strictly on the log-ratio to explicitly bound off-policy drift, regardless of the sign of the advantages. This approach aligns with recent strategies proposed to stabilize large-scale RL training. Empirically, this mechanism is essential for maintaining training stability in complex domains requiring long-horizon, multi-step tool-use reasoning. The MuonClip optimizer is employed to minimize this objective.

A rule-based outcome reward is applied for tasks with verifiable solutions, such as reasoning and agentic tasks. To optimize resource consumption, a budget-control reward is incorporated, aimed at enhancing token efficiency. For general-purpose tasks, Generative Reward Models (GRMs) are employed to provide granular evaluations aligned with Kimi’s internal value criteria.

In addition, for visual tasks, task-specific reward functions are designed to provide fine-grained supervision.

For visual grounding and point localization tasks, an F1-based reward with soft matching is employed: grounding tasks derive soft matches from Intersection over Union (IoU), and point tasks derive soft matches from Gaussian-weighted distances under optimal matching.
For polygon segmentation tasks, the predicted polygon is rasterized into a binary mask, and the segmentation IoU against the ground-truth mask is computed to assign the reward.
For OCR tasks, normalized edit distance is adopted to quantify character-level alignment between predictions and ground-truth.
For counting tasks, rewards are assigned based on the absolute difference between predictions and ground-truth.
Furthermore, complex visual puzzle problems are synthesized and an LLM verifier (Kimi K2) is utilized to provide feedback.

Kimi K2 leverages a self-critique rubric reward for open-ended generation, and K2.5 extends this line of work by systematically deploying Generative Reward Models (GRMs) across a broad range of agentic behaviors and multimodal trajectories. Rather than limiting reward modeling to conversational outputs, GRMs are applied on top of verified reward signals in diverse environments, including chat assistants, coding agents, search agents, and artifact-generating agents. To mitigate reward hacking and overfitting to a single preference signal, multiple alternative GRM rubrics tailored to different task contexts are employed.

Imposing a problem-dependent budget effectively constrains inference-time compute, incentivizing the model to generate more concise chain of thought reasoning patterns without unnecessary token expansion. However, a length-overfitting phenomenon is observed: models trained under rigid budget constraints often fail to generalize to higher compute scales. Consequently, they cannot effectively leverage additional inference-time tokens to solve complex problems, instead defaulting to truncated reasoning patterns.

To this end, Toggle is proposed, a training heuristic that alternates between inference-time scaling and budget-constrained optimization: for learning iteration t, the reward function is defined by:

Phase 0 (budget limited phase): The model is trained to solve the problem within a task-dependent token budget. To prevent a premature sacrifice of quality for efficiency, this constraint is conditionally applied: it is only enforced when the model’s mean accuracy for a given problem exceeds the threshold λ .
Phase 1 (standard scaling phase): The model generates responses up to the maximum token limit, encouraging the model to leverage computation for better inference-time scaling.

The problem-dependent budget is estimated from the ρ-th percentile of token lengths among the subset of correct responses:

Evaluation
Performance comparison of Kimi K2.5 against open-source and proprietary models.
Reasoning & General: Kimi K2.5 delivers highly competitive performance, often matching or outperforming proprietary models on STEM benchmarks (e.g., 96.1% on AIME 2025, outperforming Claude Opus 4.5 and Gemini 3 Pro), and demonstrates deep reasoning, instruction following, and long-context abilities.
Coding & Software Engineering: The model excels in realistic coding and maintenance tasks (e.g., 76.8% on SWE-Bench Verified, 85.0% on LiveCodeBench v6), showing strong, robust, and adaptable software engineering skills. It also performs well in security-focused tasks (41.3% on CyberGym).
Agentic Capabilities: Kimi K2.5 sets new state-of-the-art results on complex search and multi-step agentic tasks, significantly outperforming both proprietary and open-source competitors on benchmarks like BrowseComp (up to 74.9% with context management), WideSearch, and DeepSearchQA.
Image Understanding: The system exhibits superior multimodal reasoning, world knowledge, and perception (e.g., 78.5% on MMMU-Pro, 92.3% on OCRBench, and 92.6% on InfoVQA), consistently outperforming competitors, particularly with tool augmentation on challenging perception tasks.
Video Understanding: Kimi K2.5 achieves best-in-class results on video benchmarks, setting new global SOTA for long-video understanding (75.9% on LVBench, 79.8% on LongVideoBench, 86.6% on VideoMMMU).
Computer Use: Demonstrates state-of-the-art ability in GUI-based computer interaction with 63.3% on OSWorld-Verified and 58.9% on WebArena, outperforming several strong open-source and proprietary baselines and closing the gap with the current leader, Claude Opus 4.5.
Performance comparison of Kimi K2.5 Agent Swarm against single-agent and proprietary baselines on agentic search benchmarks.
Agent Swarm achieves substantial performance improvements over single-agent and proprietary systems.
Agent Swarm provides substantial execution time reductions on WideSearch, yielding 3×–4.5× faster completion compared to single agents, especially as task complexity increases.
Agent Swarm’s dynamic allocation of subagents supports scalable, efficient orchestration, preventing linear growth in completion time as task difficulty increases.
The proactive context management strategy of Agent Swarm (context sharding) outperforms reactive truncation (e.g., Discard-all), preserving structural information and achieving higher accuracy with fewer steps.

Paper

Kimi K2.5: Visual Agentic Intelligence 2602.02276

That’s a wrap!

If you enjoyed this breakdown, follow for more. I publish new paper explanations most weekdays.

More papers in this series, organized by lab and topic, are in the start here guide.

What paper should I cover next? Let me know in the responses.

View original.

Exported from Medium on August 22, 2026.
