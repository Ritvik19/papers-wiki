# Lilian Weng

**Type**: person  
**Tags**: #entity

## Overview

Lilian Weng is an ML researcher and technical writer known for long-form explanatory posts on deep learning, reinforcement learning, agents, and NLP at [lilianweng.github.io](https://lilianweng.github.io). Her articles bridge research papers and implementable intuition with diagrams and worked examples.

## Appearances

- [[Learning Word Embedding]] — *Learning Word Embedding* (Oct 15, 2017, ~18 min read): comprehensive Word2Vec/GloVe tutorial with architecture figures, loss derivations, Game of Thrones gensim walkthrough, and 11 primary references.
- [[Object Detection for Dummies Part 1]] — gradients, HOG, Felzenszwalb segmentation, Selective Search (Oct 29, 2017).
- [[Object Detection for Dummies Part 2]] — AlexNet/VGG/ResNet, mAP/IoU, DPM, Overfeat (Dec 15, 2017).
- [[Object Detection for Dummies Part 3]] — R-CNN through Mask R-CNN family (Dec 31, 2017).
- [[Object Detection Part 4]] — YOLO, SSD, RetinaNet one-stage detectors (Dec 27, 2018).
- [[Self-Supervised Representation Learning]] — *Self-Supervised Representation Learning* (Nov 10, 2019, ~33 min read): A unified, highly detailed survey of self-supervised pretext tasks across computer vision, video dynamics, and robotic visual control.
- [[Contrastive Representation Learning]] — *Contrastive Representation Learning* (May 31, 2021, ~28 min read): A comprehensive synthesis of deep metric learning loss functions, unsupervised visual representation pipelines (SimCLR, MoCo, Barlow Twins, BYOL, SwAV, CLIP), and natural language sentence representation alignment approaches (SimCSE, whitening).
- [[How to Train Really Large Models on Many GPUs?]] — *How to Train Really Large Models on Many GPUs?* (Sep 25, 2021): An exhaustive, master survey of distributed deep learning techniques across training parallelism paradigms (Data, Model, Pipeline, Tensor), sparse scaling Mixture-of-Experts routing strategies, and memory-saving designs (Activation Recomputation, Mixed Precision, ZeRO optimizer partitioning).
- [[Reward Hacking in Reinforcement Learning]] — *Reward Hacking in Reinforcement Learning* (Nov 28, 2024): comprehensive synthesis of reward hacking taxonomy, scaling laws, RLHF-specific exploits (U-Sophistry, sycophancy, grader biases), in-context reward hacking (ICRH), and mitigations.
- [[Extrinsic Hallucinations in LLMs]] — *Extrinsic Hallucinations in LLMs* (Jul 7, 2024): comprehensive synthesis of causes (pre-training noise, fine-tuning new knowledge), detection methods (FActScore, SAFE, SelfCheckGPT, TruthfulQA, calibration), and mitigations (RAG+editing, Self-RAG, CoVe, ITI, factual nucleus sampling, GopherCite, WebGPT, FLAME).
- [[Learning with not Enough Data Part 1: Semi-Supervised Learning]] — *Learning with not Enough Data Part 1* (Dec 5, 2021, ~26 min): SSL survey — consistency regularization (Π-model, Mean Teacher, UDA), pseudo labeling (Noisy Student, Meta Pseudo Labels), MixMatch/FixMatch, and self-supervised pre-training baselines.
- [[Learning with not Enough Data Part 2: Active Learning]] — *Part 2* (Feb 20, 2022, ~22 min): budgeted labeling — uncertainty/diversity/model-change acquisition, MC dropout, BALD, BADGE, core-sets, VAAL/MAL, hybrid CEAL.
- [[Learning with not Enough Data Part 3: Data Generation]] — *Part 3* (Apr 15, 2022, ~28 min): augmentation (EDA, RandAugment, Mixup) and LM synthesis (GPT-3 annotator, LAMBADA, UDG), affinity/diversity metrics, noisy-label robust training (Co-teaching, GCE).
- [[2020-08-06-nas]] — *Neural Architecture Search* (Aug 6, 2020, ~30 min read): A master survey decomposing AutoML neural structures into search spaces (sequential, cell, hierarchical), search algorithms (RL, evolutionary, surrogate, continuous gradients), and evaluation strategies (proxies, hypernetwork weights, supergraph weight-sharing).
- [[2024-02-05-human-data-quality]] — *Thinking about High-Quality Human Data* (Feb 5, 2024): master survey on crowdsourcing paradigms, label aggregation methodologies ([[Majority Voting]], [[MACE]], [[Disagreement Deconvolution]], [[Jury Learning]]), and deep learning training dynamics diagnostics ([[Influence Functions in DL]], [[Data Maps]], [[Area Under the Margin]]).
- [[What are Diffusion Models?]] — *What are Diffusion Models?* (Jul 11, 2021): An exhaustive, master survey of the mathematical foundations (DDPM, score networks, stochastic differential equations), acceleration samplers (DDIM, progressive distillation, Consistency Models), and scalable backbones (LDM, DiT, ControlNet).
- [[Diffusion Models for Video Generation]] — *Diffusion Models for Video Generation* (Apr 12, 2024): An exhaustive, master survey mapping the three key paradigms of video diffusion: video generation from scratch ($\mathbf{v}$-parameterization, STUNet, DiT/Sora), adapting 2D image models (Make-A-Video, Tune-A-Video, Video LDM, SVD, Lumiere), and training-free adaptation (Text2Video-Zero, ControlVideo).
- [[Exploration Strategies in Deep Reinforcement Learning]] — *Exploration Strategies in Deep Reinforcement Learning* (Jun 7, 2020): comprehensive survey of exploration methods in deep RL, covering classic strategies (ε-greedy, UCB, Thompson sampling), count-based methods (pseudo-counts, SimHash), prediction-based methods (ICM, VIME, RND, disagreement), memory-based methods (NGU, Agent57, Go-Explore, Episodic Curiosity), and option/skill discovery (VIC, VALOR).
- [[Curriculum for Reinforcement Learning]] — *Curriculum for Reinforcement Learning* (Jan 29, 2020): comprehensive survey of curriculum learning for RL across six paradigms: task-specific curriculum, teacher-guided curriculum (TSCL, ALP-GMM), curriculum through self-play (asymmetric self-play), automatic goal generation (Goal GAN, Setter-Judge-Solver), skill-based curriculum (CARML), and curriculum through distillation (Progressive Neural Networks, Mix-and-Match).
- [[Scaling Laws, Carefully]] — *Scaling Laws, Carefully* (Jun 24, 2026, ~25 min): survey from Amari/Hestness/Rosenfeld through Kaplan vs. Chinchilla reconciliation (Pearce & Song), data-limited extensions (Muennighoff, Lovelace), and Besiroglu replication pitfalls; includes interactive toy simulation.
- [[Harness Engineering for Self-Improvement]] — *Harness Engineering for Self-Improvement* (Jul 4, 2026, ~31 min): RSI via harness design—workflow patterns, ACE/MCE/Meta-Harness, self-improving and evolutionary harness search, future bottlenecks (evaluators, reward hacking, scientific taste).

## Notes

The word-embedding post is a standard reference in the NLP education stack alongside Chris McCormick's Word2Vec tutorial and Sebastian Ruder's embedding survey (both cited in the article). It predates transformers but remains accurate for static embedding methods.

**Object Detection for Dummies** (4 parts, 2017–2018): classical vision (HOG, selective search) → CNN/DPM/Overfeat → R-CNN family → YOLO/SSD/RetinaNet. Pedagogical series with worked math, Python demos, and architecture diagrams—complements [[Papers Explained 14 - RCNN]] through [[Papers Explained 31 - Single Shot MultiBox Detector]] paper pages.

**Self-Supervised Representation Learning** (2019): An extensive survey cataloging early geometric pretext tasks (rotation, relative patch location, Jigsaw Puzzles, feature counting), generative reconstruction (Context Encoders, Split-Brain Autoencoders, BiGAN), contrastive latent representations (CPC, InfoNCE), and viewpoint-invariant metrics for robotic control (TCN, Grasp2Vec, RIG). Discusses mathematical formulations and the constant challenge of model shortcut exploitation (e.g. chromatic aberration).

**Contrastive Representation Learning** (2021): An exhaustive survey bridging self-supervised vision architectures and NLP sentence alignment. Synthesizes the development from early metric losses (Triplet) to massive joint multimodal networks (CLIP). Reflects her unique ability to distill complex mathematical formulations (such as mutual information bounds of InfoNCE and importance-sampling estimators for debiased contrastive objectives) alongside empirical PyTorch/Numpy pseudo-code.

**Reward Hacking in RL** (2024): Transition from classical RL shaping limitations (Ng 1999) and specification gaming (Krakovna 2020) to modern LLM-centric exploits (Wen 2024, Sharma 2023) and test-time ICRH loops (Pan 2024). Represents her deep interest and call to research in practical mitigations for AI Safety.

**Extrinsic Hallucinations in LLMs** (Jul 2024): Comprehensive synthesis of the hallucination problem in LLMs — narrowed to extrinsic (world-knowledge-grounded) hallucination. Covers root causes (pre-training noise, fine-tuning on unknown knowledge), detection methods (FActScore, SAFE's agentic F1@K, SelfCheckGPT, TruthfulQA, calibration curves, indirect query), and a rich catalog of mitigations (RAG+editing via RARR/FAVA, adaptive retrieval via Self-RAG/RECITE/RR, inference-time steering via CoVe/ITI/factual nucleus sampling, and factuality fine-tuning via GopherCite/WebGPT/FLAME). Complements the Reward Hacking post as a companion safety-focused survey.

**How to Train Really Large Models on Many GPUs?** (2021): A fundamental systems engineering reference compiling high-level architectures and rigorous mathematical equations for modern large-scale training pipelines. Captures the detailed transition from naive vertical model sharding to complex asynchronous 1F1B schedules (PipeDream-2BW) and horizontal matrix sharding (Megatron-LM). Serves as a vital design map for modern foundation model pretraining.

**Learning with not Enough Data** (2021–2022, 3 parts): A coherent trilogy on scarce labeled data — Part 1 semi-supervised learning (consistency + pseudo labels + FixMatch), Part 2 active learning (deep acquisition functions), Part 3 data generation and noise-robust training. Bridges classical SSL/AL literature with the LM few-shot synthesis era.

### Trilogy comparison: when to use which strategy

| | Part 1: SSL | Part 2: Active Learning | Part 3: Data Generation |
|---|-------------|-------------------------|-------------------------|
| **Summary** | [[Learning with not Enough Data Part 1: Semi-Supervised Learning]] | [[Learning with not Enough Data Part 2: Active Learning]] | [[Learning with not Enough Data Part 3: Data Generation]] |
| **Extra cost** | None (no new labels) | Human labeling budget $B$ | Compute for aug/synthesis; optional human QA |
| **Uses $\mathcal{U}$** | Yes — all unlabeled data in loss | Yes — but only labels top-$b$ each round | Yes — aug perturbs; synthesis creates new points |
| **Label source** | Pseudo labels + consistency | Human oracle on selected batches | Augmentation preserves $y$; LM generates $(x,y)$ |
| **Best when** | Large $\mathcal{U}$, labels scarce but free to use unlabeled pool | Labels expensive, can query oracle (medical, expert) | Need more diversity or volume; have strong LM/aug pipeline |
| **Key methods** | [[FixMatch]], [[Mean Teacher]], [[UDA]], [[Noisy Student]] | [[BALD]], [[BADGE]], [[VAAL]], [[MAL]], [[CEAL]] | [[Easy Data Augmentation]], [[UDG]], [[Co-teaching]], [[Generalized Cross Entropy]] |
| **Main risk** | Confirmation bias on pseudo labels | Batch redundancy; miscalibrated uncertainty | Noisy synthetic labels; distribution shift |
| **Combines with** | Self-supervised pretrain (SimCLRv2) | [[CEAL]] + pseudo labels; GPT-3 + AL relabel | [[Semi-Supervised Learning]] on generated data; [[Active Learning]] for QA |

**Decision flow (from Weng's framing):**

1. **Large unlabeled pool, zero labeling budget** → Part 1 SSL or pre-train + fine-tune
2. **Can pay for some labels, need best ROI** → Part 2 AL (hybrid: [[BADGE]], [[MAL]], [[CEAL]])
3. **Need more training points or label throughput** → Part 3 generation (aug cheap; LM synthesis when pretrained model available)
4. **All three**: e.g. GPT-3 labels + AL human fixup + SSL on remaining unlabeled ([[CEAL]] pattern; Wang et al. 2021 GPT-3 pipeline)

**Neural Architecture Search** (2020): An exhaustive master survey bridging classical heavy optimization (Zoph & Le 2017) with modern one-shot/differentiable methods. Synthesizes how AutoML transitioned from high-compute random/evolutionary graphs to parameter-sharing supergraphs ([[ENAS]]), continuous relaxation ([[DARTS]]), memory-efficient binarization (ProxylessNAS), and evolutionary program synthesis from mathematical primitives ([[AutoML-Zero]]). Represents her unique ability to dissect massive research areas into elegant, structured frameworks.

**Curriculum for Reinforcement Learning** (2020): A structured taxonomy of curriculum approaches applied to RL, organized into six paradigms. Key insight: mixing easy tasks throughout training (combined strategy) beats pure sequential curricula; uniformly sampling all tasks is a surprisingly strong baseline for teacher-guided methods. Covers three curriculum automation mechanisms: teacher RL agents (TSCL, ALP-GMM), adversarial goal generation (Goal GAN, Setter-Judge-Solver), and skill discovery (CARML). Two distillation-based methods—Progressive Neural Networks and Mix-and-Match—realize curriculum as model expansion sequences that avoid catastrophic forgetting. Companion post to [[Exploration Strategies in Deep Reinforcement Learning]].

**Thinking about High-Quality Human Data** (2024): An extensive survey on the role of human annotations in SFT and RLHF. Deconstructs data quality control into two interfaces: rater operations and training dynamics. Under rater operations, she distinguishes prescriptive paradigms (single ground-truth, spammers filtered via [[MACE]] or aggregated via [[Majority Voting]]) from descriptive paradigms (retaining demographic diversity via [[Disagreement Deconvolution]] and [[Jury Learning]]'s DCN panels). Under training dynamics, she shows how SGD tension with noisy labels yields diagnostic profiles like [[Influence Functions in DL]], cartographic confidence/variability segmentation in [[Data Maps]], and low logit margins in [[Area Under the Margin]] (AUM) which can be calibrated using known noisy threshold samples.

**What are Diffusion Models?** (2021): A master reference unifying variational and score-based diffusion theories. It details the transition from high-latency Markovian sampling to deterministic implicit samplers, and establishes mathematical guidance paradigms (Classifier-Free Guidance) and structural scaling laws (Diffusion Transformers).

**Scaling Laws, Carefully** (2026): A pretraining-focused survey that treats scaling laws as a fitting and extrapolation problem, not just a power-law slogan. Walks Kaplan ($N_\text{opt} \propto C^{0.73}$) vs. Chinchilla ($C^{0.5}$), explains Pearce & Song's embedding-parameter reconciliation, then covers data repetition (Hernandez double descent, Muennighoff exponential token decay, Lovelace capacity-ratio penalty) and Besiroglu's Chinchilla Method 3 replication. Complements [[gzip Predicts Data-dependent Scaling Laws]] on the data-dependence axis.

**Diffusion Models for Video Generation** (2024): An exhaustive survey deconstructing the video generation landscape into three distinct methodologies. Under *from scratch modeling*, she catalogs $\mathbf{v}$-parameterization (trigonometric DDIM rotations preventing color shift), reconstruction guidance conditional formulations (autoregressive extension, temporal interpolation, SSR cascades), STUNet downsampling/upsampling architectures, and Spacetime Patch DiT structures (Sora). Under *image model adaptation*, she analyzes spatial freezing + temporal layer insertion (Video LDM, SVD, Lumiere) alongside the critical SVD data curation pipeline (aesthetic, optical flow, and OCR filtering). Finally, under *training-free zero-shot adaptation*, she deconstructs deterministic DDIM inversion camera dynamics warping (Text2Video-Zero) and spatiotemporal anchoring cross-frame attention blocks (Tune-A-Video, ControlVideo).

## Related

- [[Word Embedding]]
- [[Word2Vec]]
- [[Learning Word Embedding]]
- [[Object Detection for Dummies Part 1]]
- [[Object Detection for Dummies Part 2]]
- [[Object Detection for Dummies Part 3]]
- [[Object Detection Part 4]]
- [[Self-Supervised Representation Learning]]
- [[Contrastive Representation Learning]]
- [[Contrastive Learning]]
- [[How to Train Really Large Models on Many GPUs?]]
- [[Data Parallelism]]
- [[Model Parallelism]]
- [[Pipeline Parallelism]]
- [[Tensor Parallelism]]
- [[Activation Recomputation]]
- [[Mixed Precision Training]]
- [[ZeRO]]
- [[Mixture of Experts]]
- [[Reward Hacking in Reinforcement Learning]]
- [[Reward Hacking]]
- [[In-Context Reward Hacking]]
- [[Safety and Alignment]]
- [[Learning with not Enough Data Part 1: Semi-Supervised Learning]]
- [[Learning with not Enough Data Part 2: Active Learning]]
- [[Learning with not Enough Data Part 3: Data Generation]]
- [[Semi-Supervised Learning]]
- [[Active Learning]]
- [[FixMatch]]
- [[VAAL]]
- [[MAL]]
- [[CEAL]]
- [[BALD]]
- [[BADGE]]
- [[Unsupervised Data Generation]]
- [[Extrinsic Hallucinations in LLMs]]
- [[Extrinsic Hallucination]]
- [[FActScore]]
- [[SAFE]]
- [[SelfCheckGPT]]
- [[TruthfulQA]]
- [[Self-RAG]]
- [[CoVe]]
- [[ITI]]
- [[2020-08-06-nas]]
- [[Neural Architecture Search]]
- [[ENAS]]
- [[DARTS]]
- [[AutoML-Zero]]
- [[2024-02-05-human-data-quality]]
- [[Majority Voting]]
- [[MACE]]
- [[Disagreement Deconvolution]]
- [[Jury Learning]]
- [[Influence Functions in DL]]
- [[Data Maps]]
- [[Area Under the Margin]]
- [[What are Diffusion Models?]]
- [[Denoising Diffusion Probabilistic Models]]
- [[Denoising Diffusion Implicit Models]]
- [[Classifier-Free Guidance]]
- [[Latent Diffusion Models]]
- [[Consistency Models]]
- [[Diffusion Transformer]]
- [[Diffusion Models for Video Generation]]
- [[v-parameterization]]
- [[space-time-u-net]]
- [[pseudo-3d-convolution]]
- [[cross-frame-attention]]
- [[reconstruction-guidance]]
- [[Exploration Strategies in Deep Reinforcement Learning]]
- [[Intrinsic Curiosity Module (ICM)]]
- [[Random Network Distillation (RND)]]
- [[Never Give Up (NGU)]]
- [[Agent57]]
- [[Noisy-TV Problem]]
- [[Curriculum for Reinforcement Learning]]
- [[Curriculum Learning]]
- [[Teacher-Student Curriculum Learning]]
- [[ALP-GMM]]
- [[Asymmetric Self-Play]]
- [[Goal GAN]]
- [[Automatic Domain Randomization]]
- [[Progressive Neural Networks]]
- [[CARML]]
- [[Scaling Laws, Carefully]]
- [[Scaling Laws]]
- [[IsoFLOP Profiles]]
- [[Data-Constrained Scaling Laws]]
- [[Harness Engineering for Self-Improvement]]
- [[Recursive Self-Improvement]]
- [[Self-Improving Harness]]
- [[Agentic Context Engineering]]
- [[Evolutionary Program Search]]
