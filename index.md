| Page | Summary | Tags |
| --- | --- | --- |
| [[Agent Harness]] | Product and infrastructure layer around an AI agent that manages prompts, tools, context, observability, and routing. | #concept |
| [[Agentic AI]] | Tool use, agents, web/search workflows, orchestration, and task-oriented LLM systems. | #topic |
| [[Arcee AI]] | AI company that builds efficient LLMs for enterprise; creators of the AFM dense model family and the Arcee Trinity sparse MoE family. | #entity |
| [[CoVe]] | Chain-of-Verification; inference-time hallucination mitigation via planning verification questions, answering them independently (draft absent from context), and revising the draft. Factored+Revise variant is best. | #concept |
| [[Extrinsic Hallucination]] | Model-generated content fabricated and ungrounded by world knowledge; root causes are pre-training noise and fine-tuning on unknown knowledge; mitigated by RAG, CoVe, ITI, factual fine-tuning. | #concept |
| [[Extrinsic Hallucinations in LLMs]] | Lilian Weng's July 2024 survey of extrinsic hallucination causes, detection (FActScore, SAFE, SelfCheckGPT, TruthfulQA), and mitigations (RARR, Self-RAG, CoVe, ITI, GopherCite, WebGPT, FLAME). | #summary |
| [[FActScore]] | Atomic-fact factuality metric: decomposes long-form generation into atomic facts, verifies each against Wikipedia via retrieval, reports average precision (Min et al. 2023). | #concept |
| [[FacTool]] | Multi-task factuality detection framework: extends atomic-fact checking to code generation, math problem solving, and scientific literature review using task-appropriate external tools (Chern et al. 2023). | #concept |
| [[Factual Nucleus Sampling]] | Decoding-time hallucination mitigation: dynamically decays nucleus probability p within each sentence (p_t = max(ω, p·λ^(t−1))) so later tokens (where factual entities appear) are sampled near-greedily. | #concept |
| [[FLAME]] | Factuality-Aware Alignment: SFT + DPO pipeline using FActScore as reward signal; shows RLHF degrades factuality because human raters prefer longer, more detailed answers (Lin et al. 2024). | #concept |
| [[GopherCite]] | DeepMind system that trains LLMs to produce cited responses via few-shot + context stuffing demonstrations + RL from human preferences; includes selective prediction ("I don't know") via RM threshold. | #concept |
| [[ITI]] | Inference-Time Intervention; reduces hallucination by probing attention heads for a truthfulness direction and shifting activations toward it at inference time; no fine-tuning required (Li et al. 2023). | #concept |
| [[RARR]] | Retrofit Attribution using Research and Revision; training-free retroactive RAG+editing framework that corrects unsupported claims and produces attribution reports (Gao et al. 2022). | #concept |
| [[RECITE]] | Recitation-Augmented Generation; treats Transformer parametric memory as a retrieval mechanism by prompting the model to recite relevant passages before answering; comparable to BM25 on common topics (Sun et al. 2023). | #concept |
| [[SAFE]] | Search-Augmented Factuality Evaluator; agentic multi-step search loop for atomic-fact verification; uses F1@K metric balancing factual precision and response recall (Wei et al. 2024). | #concept |
| [[Self-RAG]] | Self-Reflective RAG; trains a model to emit Retrieve / ISREL / ISSUP / ISUSE reflection tokens, adaptively retrieving and critiquing its own generation quality (Asai et al. 2024). | #concept |
| [[SelfCheckGPT]] | Black-box hallucination detection via consistency checking across multiple stochastic samples; no external knowledge base required; best with LLM-prompting consistency scorer (Manakul et al. 2023). | #concept |
| [[TruthfulQA]] | Adversarially constructed 817-question benchmark targeting common human misconceptions; larger models score *lower* (inverse scaling) because they better reproduce human falsehoods (Lin et al. 2021). | #concept |


| [[Audio Models]] | Speech, audio, and audio-language representation models. | #topic |
| [[CISPO]] | Clipped Importance Sampling Weight Policy Optimization; GRPO variant from MiniMax-M1 using stop-gradient importance ratios to preserve pivotal fork-token gradients across multiple update steps. | #concept |
| [[Code Models]] | Code generation, coding benchmarks, compiler-oriented methods, and software-engineering agents. | #topic |
| [[Computer-use Agents]] | GUI-operating multimodal agents whose performance depends on realistic software environments, long-horizon interaction, and robust verification. | #concept |
| [[Computer Vision]] | Vision architectures, detection and segmentation methods, image generation, and representation-learning systems. | #topic |
| [[Contrastive Learning]] | Training paradigm that teaches embedding models to place similar items at smaller angles and dissimilar items farther apart; keeps cosine similarity useful in high-dimensional spaces. | #concept |
| [[Continuous Bag-of-Words]] | Word2Vec architecture predicting the center word from averaged context embeddings. | 2026-05-21 |
| [[Count-Based Vector Space Model]] | Unsupervised embeddings from co-occurrence matrix factorization (LSA, topic models, GloVe lineage). | 2026-05-21 |
| [[Cosine Similarity]] | Magnitude-invariant angle-based distance metric used as the default for embedding retrieval; degrades in very high dimensions due to vector orthogonality and concentration of measure. | #concept |
| [[Cosine Similarity in High-Dimensional Embedding Spaces]] | Google AI Mode answer on whether cosine similarity becomes irrelevant as embedding dimensionality grows; covers curse of dimensionality, floor effects, contrastive training, and DIEM alternatives. | #summary |
| [[Curse of Dimensionality]] | Phenomenon causing distance concentration, vector orthogonality, and sparse data in high-dimensional spaces; drives failures of cosine similarity and nearest-neighbor search. | #concept |
| [[DatologyAI]] | Data curation company specializing in large-scale pretraining datasets; curated training data for Arcee AFM and Arcee Trinity. | #entity |
| [[Context Anxiety]] | Cursor-coined model behavior where filling the context window triggers refusals and hedging on task scope. | #concept |
| [[Context Rot]] | Degradation in language-model performance as input or transcript length grows, including from accumulated tool-call failures. | #concept |
| [[A Visual Guide to Attention Variants in Modern LLMs]] | Sebastian Raschka's Ahead of AI visual reference on MHA, GQA, MLA, SWA, DSA, gated attention, and hybrid stacks with LLM architecture gallery. | #summary |
| [[Beyond Standard LLMs]] | Sebastian Raschka's Ahead of AI survey of linear attention hybrids (Gated DeltaNet, Qwen3-Next, Kimi Linear), text diffusion LLMs, code world models, and small recursive transformers. | #summary |
| [[Components of A Coding Agent]] | Sebastian Raschka's Ahead of AI reference on six coding-harness components—repo context, prompt caching, tools, context reduction, session memory, and subagents—with Mini Coding Agent. | #summary |
| [[Understanding the 4 Main Approaches to LLM Evaluation (From Scratch)]] | Sebastian Raschka's Ahead of AI overview of MMLU, verifiers, LM Arena leaderboards, and LLM-as-a-judge evaluation with from-scratch Python code. | #summary |
| [[Understanding and Coding the KV Cache in LLMs from Scratch]] | Sebastian Raschka's Ahead of AI tutorial on KV cache concepts, O(n²)→O(n) decode savings, and from-scratch PyTorch implementation on the GPT model from his LLM book. | #summary |
| [[Coding Harness]] | Task-specific agent harness for software engineering: structured tools, repo context, prompt prefix caching, session memory, and bounded subagents. | #concept |
| [[Continually Improving Our Agent Harness]] | Cursor article on harness engineering for coding agents: dynamic context, evals, tool reliability, per-model customization, and multi-agent orchestration. | #summary #topic |
| [[Introducing Cursor Router]] | Cursor Teams/Enterprise intelligent model router: cache-aware per-request classification, three Auto modes, ~30–60% cost savings at frontier quality. | #summary |
| [[Composer: Building a fast frontier model with RL]] | #summary | Cursor's Oct 2025 Composer (1) launch: MoE coding agent, Cursor Bench, MXFP8 async RL at scale, harness-unified sandboxes; ~4× faster than peers on internal eval. | 2026-05-19 |
| [[CUA-World]] | Benchmark-and-training collection of 10K-plus computer-use tasks across 200 software applications and three operating systems. | #entity |
| [[CursorBench]] | Cursor's internal coding-agent eval suite, built from real engineering sessions to overcome contamination and over-specification in public benchmarks. | #entity |
| [[DAPO]] | Decoupled Clip and Dynamic Sampling Policy Optimization; four practical GRPO improvements (clip higher, dynamic sampling, token-level loss, overlong reward shaping) achieving 50% AIME 2024 with Qwen-2.5-32B. | #concept |
| [[DIEM]] | Dimension Insensitive Euclidean Metric; a proposed alternative to cosine similarity designed to remain discriminative in high-dimensional embedding spaces. | #concept |
| [[Document AI]] | Document understanding, OCR, layout parsing, tables, charts, and screenshot-based representation learning. | #topic |
| [[Distillation Regimes Compared]] | Comparison of classical representation-level KD, teacher-completion SFT distillation, and on-policy distillation. | #summary #concept |
| [[Dr. GRPO]] | De-biased GRPO variant removing std from advantage and normalizing loss by fixed constant; eliminates response-length bias and question-difficulty bias. | #concept |
| [[Dynamic Context]] | Context an agent retrieves on demand at runtime through harness-exposed tools, replacing pre-packed static context. | #concept |
| [[Embedding and Retrieval]] | Embedding models, dense retrieval, reranking, RAG evaluation, and representation-learning methods. | #topic |
| [[Encoder-Only Language Models]] | Timeline and synthesis of encoder-only language models from BERT through modern long-context, retrieval, and multilingual encoder systems. | #summary #topic |
| [[Efficient Encoder Models]] | Comparison page for compact, mobile, and adaptive BERT-family encoders such as DistilBERT, TinyBERT, ALBERT, MobileBERT, and FastBERT. | #summary #topic |
| [[Evaluation and Benchmarks]] | Benchmarks, evaluation methods, judge models, hallucination studies, and robustness analyses. | #topic |
| [[Explainable AI (XAI): A Survey of Recent Methods, Applications and Frameworks]] | AI Summer XAI survey: CAM, Grad-CAM, LRP, LIME, TCAV, saliency/plot/text explanations, autonomous driving and medical applications, InterpretML/iNNvestigate. | #summary |
| [[Exploration Strategies in Deep Reinforcement Learning]] | Lilian Weng's 2020 survey of deep RL exploration: count-based (pseudo-counts, SimHash), prediction-based (ICM, VIME, RND, disagreement), memory-based (NGU, Agent57, Go-Explore, EC), and option/skill discovery (VIC, VALOR); covers hard-exploration and noisy-TV problems. | #summary |
| [[Unravel Policy Gradients and REINFORCE]] | AI Summer 2018 RL primer: policy-based vs value-based, policy search, log-π gradient, REINFORCE/CartPole code, Karpathy Pong; high-variance → actor-critic cliffhanger. | #summary |
| [[The Idea behind Actor-Critics and How A2C and A3C Improve Them]] | AI Summer 2018: actor/critic split, advantage A2C, parallel A3C workers, synchronous multi-env A2C; bridge to PPO/TRPO. | #summary |
| [[Trust Region and Proximal Policy Optimization (TRPO and PPO)]] | AI Summer 2019: KL trust-region TRPO, PPO-Clip surrogate, importance ratios; ancestor of LLM GRPO clipping. | #summary |
| [[Proximal Policy Optimization]] | PPO-Clip policy optimizer: clipped importance ratio stabilizes policy-gradient updates; base for GRPO. | #concept |
| [[Trust Region Policy Optimization]] | KL-constrained policy improvement solved with conjugate gradient; motivated PPO. | #concept |
| [[Advantage Actor-Critic]] | Actor-critic with advantage baseline A(s,a)=Q−V; synchronous parallel-env rollout pattern. | #concept |
| [[Asynchronous Advantage Actor-Critic]] | DeepMind 2016 parallel async actor-critic with global shared network (A3C). | #concept |
| [[Curriculum for Reinforcement Learning]] | Lilian Weng's 2020 survey of six curriculum paradigms for RL: task-specific, teacher-guided (TSCL, ALP-GMM), self-play (asymmetric self-play), automatic goal generation (Goal GAN), skill-based (CARML), and curriculum through distillation (Progressive Neural Networks, Mix-and-Match). | #summary |
| [[Teacher-Student Curriculum Learning]] | TSCL framework (Matiisen et al. 2017): teacher RL agent selects subtasks for student agent as an N-armed bandit; rewards student's learning progress; uniform task sampling is a surprisingly strong baseline. | #concept |
| [[ALP-GMM]] | Absolute Learning Progress Gaussian Mixture Model (Portelas et al. 2019): teacher-student curriculum for continuous task parameter spaces; GMM over ALP scores (reward difference between nearby tasks) with ε-greedy sampling. | #concept |
| [[Asymmetric Self-Play]] | Sukhbaatar et al. 2017 self-play curriculum: Alice sets states for Bob to reproduce; Alice's reward grows with Bob's difficulty; all tasks guaranteed solvable because Alice demonstrates them first. | #concept |
| [[Goal GAN]] | Generative Goal Learning (Florensa et al. 2018): GAN-based curriculum where generator proposes goals of intermediate difficulty (GOID) and discriminator classifies whether goal is achievable; extended by Setter-Judge-Solver framework. | #concept |
| [[Automatic Domain Randomization]] | OpenAI ADR (2019): grows a distribution of RL environments with increasing complexity by widening parameter ranges when policy performance exceeds a threshold; Rubik's cube curriculum. | #concept |
| [[Progressive Neural Networks]] | Rusu et al. 2016: curriculum through distillation via frozen sequential column expansion; lateral connections allow positive transfer; tested on multi-task Atari. | #concept |
| [[CARML]] | Jabri et al. 2019: variational EM skill-discovery framework for meta-RL; E-step organizes trajectories into latent skill space; M-step trains policy with skills as task distribution; operates on pixel observations. | #concept |
| [[GloVe]] | Global Vectors: log co-occurrence factorization combining count statistics with linear word-vector structure (Pennington et al., 2014). | 2026-05-21 |
| [[GMPO]] | Geometric Mean Policy Optimization; GRPO variant using geometric mean aggregation of token-level losses for reduced variance, plug-and-play replacement for GRPO. | #concept |
| [[Hierarchical Softmax]] | Binary-tree softmax reducing Word2Vec training cost from O(V) to O(log V) per sample (Morin & Bengio, 2005). | 2026-05-21 |
| [[GRPO]] | Group Relative Policy Optimization; default RL optimizer for reasoning model training; uses group-relative advantage estimation instead of a learned critic/value model. | #concept |
| [[GRPO++: Tricks for Making RL Actually Work]] | Comprehensive survey (Cameron R. Wolfe) of practical improvements to vanilla GRPO for reasoning model training: DAPO, Dr. GRPO, TIS, GSPO, GMPO, CISPO. | #summary |
| [[Agent57]] | First deep RL agent to outperform the human benchmark on all 57 Atari games; extends Never Give Up with a population of policies and a UCB meta-controller. | #concept |
| [[GSPO]] | Group Sequence Policy Optimization; GRPO variant with sequence-level importance ratios; used to train Qwen 3; naturally stabilizes MoE routing. | #concept |
| [[k-Nearest Neighbors]] | Non-parametric classifier that assigns a test item the majority label of its k closest training items by some distance metric; used with NCD in training-free gzip text classification. | #concept |
| [[Keep Rate]] | Online quality metric tracking the fraction of agent-proposed code changes that survive in the user's codebase after fixed time intervals. | #concept |
| [[Jeffrey Pennington]] | Lead author of GloVe (Global Vectors for Word Representation, EMNLP 2014). | 2026-05-21 |
| [[KL Regularization]] | Constraint technique for keeping policy or teacher-guided updates within a stable divergence budget. | #concept |
| [[Kolmogorov Complexity]] | Theoretical measure of information content as the length of the shortest program generating an object; uncomputable in practice but approximated by NCD via real compressors. | #concept |
| [[Large Language Models]] | Language-model architectures, training recipes, and model-family releases across the Papers Explained corpus. | #topic |
| [[Long Context]] | Long-context training, retrieval over long inputs, compression, and context-window robustness. | #topic |
| [[LoRA Without Regret]] | Empirical study by John Schulman & Thinking Machines Lab characterising the low-regret regime where LoRA matches full fine-tuning for both SFT and RL post-training; applies to all layers especially MLP/MoE. | #summary |
| [[Inkling]] | Thinking Machines 975B/41B-active open MoE: encoder-free multimodal, relative attention, controllable thinking effort, Tinker fine-tuning. | #summary |
| [[Inkling-Small]] | 276B/12B-active efficient Inkling family member; on-policy distillation from Inkling; strong reasoning/agentic at lower cost. | #summary |
| [[Mixture of Experts]] | Mixture-of-experts architectures and sparse routing methods for scaling model capacity efficiently. | #topic |
| [[Model Compression and Efficiency]] | Small models, quantization, parameter-efficient fine-tuning, long-context efficiency, and deployment-oriented architectures. | #topic |
| [[Model Distillation]] | Transfer of behavior or capability from a teacher model into a student model. | #concept |
| [[Muon Optimizer]] | Modern deep learning optimizer offering improved training efficiency and stability; used to train Arcee Trinity Large. | #concept |
| [[Multilingual Models]] | Multilingual, cross-lingual, translation, and region-specific model work. | #topic |
| [[Nathan Lambert]] | Author of the open RLHF textbook; RLHF researcher and educator (rlhfbook.com). | #entity |
| [[Intrinsic Curiosity Module (ICM)]] | Self-supervised exploration bonus using an inverse-dynamics-learned feature space and forward prediction error; excludes uncontrollable environment factors to partially mitigate the noisy-TV problem. | #concept |
| [[Negative Sampling]] | Word2Vec training objective: sigmoid classifiers on true vs noise context pairs (Mikolov et al., 2013). | 2026-05-21 |
| [[Never Give Up (NGU)]] | Combines a short-term episodic novelty module (IDF embeddings + k-NN kernel) with a long-term RND life-long module for two-timescale exploration bonuses. | #concept |
| [[Noisy-TV Problem]] | Failure mode of curiosity-driven RL where an agent fixates on irreducible environmental noise that gives permanent high intrinsic reward without learning progress. | #concept |
| [[Normalized Compression Distance]] | Computable approximation of Kolmogorov-based information distance using compression length; drives the gzip+kNN training-free text classifier. | #concept |
| [[NVFP4]] | #concept | NVIDIA 4-bit float format for Blackwell training/inference; used by Inkling and Nemotron open checkpoints. | 2026-07-21 |
| [[On SFT RL and On-Policy Distillation]] | Synthesis of Will Brown's argument that SFT, RL, OPD, and self-distillation differ by compounding, teacher-family match, and gradient density/bias/concentration. | #summary #topic |
| [[On-Policy Distillation]] | Student-rollout distillation using dense token-level guidance from a same-family teacher. | #concept |
| [[On-Policy Self-Distillation]] | Self-distillation setup where a privileged-context version of the student teaches its on-policy rollouts. | #concept |
| [[Random Network Distillation (RND)]] | Exploration bonus using prediction error of a trained network against a fixed random target; novel states yield higher error; works best in non-episodic setting with normalised rewards. | #concept |
| [[SFT, RL, and On-Policy Distillation Visual Notes]] | Visual synthesis of SFT, RL, and OPD as different update geometries, with saved X article figures on KL, MOPD, and entropy collapse. | #summary #topic |
| [[Paper Explained 144 - Granite Code Models]] | This paper introduces a series of decoder-only code models (3B, 8B, 20B, 34B) for code generative tasks, trained with code written in 116 programming languages, suitable for... | #summary #topic |
| [[Paper Explained 268 - PaliGemma2]] | PaliGemma 2 is an upgrade of PaliGemma by replacing its language model component with the more recent and more capable language models from the Gemma 2 family, while utilizing the... | #summary #topic |
| [[Paper Explained 316 - NuminaMath]] | The NuminaMath dataset is a comprehensive collection of 860k pairs of competition math problems and solutions. Problems range from high-school-level to advanced-competition-level... | #summary #topic |
| [[Papers Explained - AceCoder]] | AceCoder leverages automated large-scale test-case synthesis to enhance code model training. A pipeline is designed that generates extensive (question, test-cases) pairs from... | #summary #topic |
| [[Papers Explained - Advancing Search Augmented Language Models]] | This article describes Perplexity’s post-training pipeline for developing state-of-the-art web search agents based on open-source models. Training frontier web search agents... | #summary #topic |
| [[Papers Explained - An Introduction to Vision-Language Modeling]] | The development of Vision-Language Models (VLMs), aims to connect vision to language and enable applications such as visual assistants and generative models that produce images... | #summary #topic |
| [[Papers Explained - Apriel-1.5-OpenReasoner]] | Domains that have produced fewer completions than intended get αd > 1 and are up-weighted, while over-represented domains are down-weighted. If a domain has no completions yet, αd... | #summary #topic |
| [[Papers Explained - Beyond Web]] | Recent advances in LLM pretraining show that simply scaling web data leads to diminishing returns, pushing researchers to use synthetic data. | #summary #topic |
| [[Papers Explained - Composer 2]] | Several potential open-source base models were evaluated, including GLM-5, Kimi K2.5, and DeepSeek V3.2. Three base model evaluations contributed to the selection of Kimi K2.5: | #summary #topic |
| [[Papers Explained - EfficientNetV2]] | EfficientNetV2 is a new family of convolutional networks having faster training speed and better parameter efficiency than previous models, developed using a combination of... | #summary #topic |
| [[Papers Explained - EvolLM]] | EvoLM is a model suite that enables systematic and transparent analysis of large language models’ training dynamics across pre-training, continued pre-training, supervised... | #summary #topic |
| [[Papers Explained - Extracting alignment data in open models]] | This work hypothesizes that since the chat template is exclusively introduced in post-training, if the model is prompted with the template, it will generate alignment data. | #summary #topic |
| [[Papers Explained - FinePhrase]] | FinePhrase is a 486B-token synthetic pretraining dataset created after 90 systematic experiments, over 1 trillion generated tokens, and 12.7 GPU-years to find the best “recipe”... | #summary #topic |
| [[Papers Explained - GGUF]] | GGUF (GGML Unified Format) is a binary file format designed for storing and loading large language models (LLMs), specifically for inference, primarily within the GGML ecosystem... | #summary #topic |
| [[Papers Explained - GLIDE]] | GLIDE explores diffusion models for the problem of text-conditional image synthesis and compares two different guidance strategies: CLIP guidance and classifier-free guidance. It... | #summary #topic |
| [[Papers Explained - GloVe 2024]] | This report details the creation and evaluation of new 2024 English GloVe (Global Vectors for Word Representation) models. The original 2014 GloVe models, while useful, lacked... | #summary #topic |
| [[Papers Explained - GRAPE]] | GRAPE is a novel SFT framework that accounts for the unique characteristics of the target model. For each instruction, it gathers responses from various LLMs, and selects the one... | #summary #topic |
| [[Gym-Anything]] | Framework for turning arbitrary software into audited computer-use environments and scaling them into the CUA-World benchmark. | #summary #topic |
| [[Papers Explained - How2Everything]] | Candidate documents are sourced from the DCLM web corpus. Because tutorial-style documents tend to have a high density of explicitly ordered, imperative steps, the document pool... | #summary #topic |
| [[Papers Explained - Likelihood-Based Reward Designs for General LLM Reasoning]] | This work systematically compares variants of likelihood-based rewards with standard baselines, testing performance both on standard mathematical reasoning benchmarks and on... | #summary #topic |
| [[Papers Explained - Mistral 7B]] | Mistral 7B is an LLM engineered for superior performance and efficiency. It leverages grouped-query attention (GQA) for faster inference, coupled with sliding window attention... | #summary #topic |
| [[Papers Explained - Nemotron 3 Super]] | Nemotron 3 Super is a 120B (active 12B) parameter hybrid Mamba-Attention Mixture-of-Experts model, pre-trained in NVFP4. It leverages LatentMoE, a new Mixture-of-Experts... | #summary #topic |
| [[Papers Explained - OpenAI Privacy Filter]] | OpenAI Privacy Filter is a bidirectional token-classification model for personally identifiable information (PII) detection and redaction in text. It is designed for... | #summary #topic |
| [[Papers Explained - Probabilistic Diffusion Models]] | Diffusion models are a class of powerful generative models used to generate high-quality samples and perform tasks like image denoising, inpainting, super-resolution, and image... | #summary #topic |
| [[Papers Explained - Sarvam 30B and Sarvam 105B]] | Sarvam 30B and Sarvam 105B are reasoning models trained from scratch on large-scale, high-quality datasets curated in-house across every stage of training: pre-training... | #summary #topic |
| [[Papers Explained - SelfCite]] | SelfCite is a novel self-supervised approach that aligns LLMs to generate high-quality, fine-grained, sentence-level citations for the statements in their generated responses.... | #summary #topic |
| [[Papers Explained - The Art of Asking]] | Current synthetic data pipelines focus on improving the mapping from prompts to completions (P(y\|x)), assuming the input prompt distribution (P(x)) remains constant. | #summary #topic |
| [[Papers Explained 01 - Transformer]] | Most competitive neural sequence transduction models have an encoder-decoder structure. Here, the encoder maps an input sequence of symbol representations (x1, …, xn) to a... | #summary #topic |
| [[Papers Explained 02 - BERT]] | During pre-training, the model is trained on unlabeled data over different pre-training tasks. | #summary #topic |
| [[Papers Explained 03 - RoBERTa]] | RoBERTa presents a replication study of BERT pretraining that carefully measures the impact of many key hyperparameters and training data size. It is found that BERT was... | #summary #topic |
| [[Papers Explained 04 - Sentence BERT]] | BERT and RoBERTa require that both sentences are fed into the network, which causes a massive computational overhead: Finding the most similar pair in a collection of 10,000... | #summary #topic |
| [[Papers Explained 05 - Tiny BERT]] | Knowledge Distillation aims to transfer the knowledge of a large teacher network T to a small student network S. Let fT and fS represent the behavior functions of teacher and... | #summary #topic |
| [[Papers Explained 06 - Distil BERT]] | Knowledge distillation is a compression technique in which a compact model (the student) is trained to reproduce the behaviour of a larger model, (the teacher) or an ensemble of... | #summary #topic |
| [[Papers Explained 07 - ALBERT]] | ALBERT presents certain parameter reduction techniques to lower memory consumption and increase the training speed of BERT | #summary #topic |
| [[Papers Explained 08 - DeBERTa]] | DeBERTa (Decoding-enhanced BERT with disentangled attention) improves the BERT and RoBERTa models using two novel techniques. | #summary #topic |
| [[Papers Explained 09 - BART]] | BART is a denoising autoencoder built with a sequence-to-sequence model that is applicable to a very wide range of end tasks. Pretraining has two stages (1) text is corrupted with... | #summary #topic |
| [[Papers Explained 10 - Layout LM]] | LayoutLM is a Neural Network that jointly models interactions between text and layout information across scanned document images, thus is beneficial for a great number of... | #summary #topic |
| [[Papers Explained 100 - CLIP]] | CLIP is pre-trained on a large dataset of 400M (image, text) pairs from the internet, instead of relying on fixed sets of predetermined object categories. The model learns... | #summary #topic |
| [[Papers Explained 101 - Vicuna]] | Vicuna-13B is an open-source chatbot trained by fine-tuning LLaMA on user-shared conversations collected from ShareGPT, capable of generating more detailed and well-structured... | #summary #topic |
| [[Papers Explained 102 - LLaVA 1]] | LLaVA (Large Language and Vision Assistant) is an end-to-end trained large multimodal model that connects a vision encoder (CLIP) and an LLM (Vicuna) for general purpose visual... | #summary #topic |
| [[Papers Explained 103 - LLaVA 1.5]] | LLaVA 1.5 is a 13B model that uses 12M publicly available data along with simple modifications to LLaVA, namely, using CLIP-ViT-L-336px with an MLP projection and adding... | #summary #topic |
| [[Papers Explained 104 - MoE-LLaVA]] | MoE-LLaVA is a MoE-based sparse LVLM architecture that incorporates a mixture of experts and learnable routers. It consists of multiple sparse paths where each token is dispatched... | #summary #topic |
| [[Papers Explained 105 - Gemini 1.5 Pro]] | Gemini 1.5 Pro marks a significant milestone in the evolution of multi-modal mixture-of-experts models, pushing the boundaries of compute efficiency, reasoning, and long-context... | #summary #topic |
| [[Papers Explained 106 - Gemma]] | Gemma are a family of lightweight (2B and 7B), state-of-the art open language models built from the research and technology used to create Gemini models. Unlike Gemini, these... | #summary #topic |
| [[Papers Explained 107 - LLaVA 1.6]] | LLaVA 1.6 is an advancement LLaVA 1.5 featuring enhanced reasoning, OCR, and world knowledge capabilities, surpassing its predecessor and other models in several benchmarks. | #summary #topic |
| [[Papers Explained 108 - Aya Dataset]] | This work contributes four key resources: the Aya Annotation Platform, the Aya Dataset, the Aya Collection, and the Aya Evaluation Suite. | #summary #topic |
| [[Papers Explained 109 - Aya 101]] | Aya 101 is a massively multilingual generative language model that follows instructions in 101 languages of which over 50% are considered as lower-resourced. It outperforms mT0... | #summary #topic |
| [[Papers Explained 11 - Layout LM v2]] | LayoutLMv2 architecture is proposed with new pre-training tasks to model the interaction among text, layout, and image in a single multi-modal framework. | #summary #topic |
| [[Papers Explained 110 - Nomic Embed]] | Nomic-embed-text is a fully open-source English text embedding model with a large context length of 8192. It surpasses existing models like OpenAI’s Ada-002 and... | #summary #topic |
| [[Papers Explained 111 - H2O Danube 1.8B]] | H2O-Danube-1.8B is a new open-source pre-trained foundation model with 1.8 billion parameters, developed by H2O.ai. | #summary #topic |
| [[Papers Explained 112 - Self Instruct]] | Self-Instruct is a framework for improving the instruction-following capabilities of pretrained language models by bootstrapping off their own generations. It provides an almost... | #summary #topic |
| [[Papers Explained 113 - mT5]] | mT5 is a multilingual variant of the T5 model pre-trained on a dataset covering 101 languages (mC4), achieving state-of-the-art performance on multilingual benchmarks. This paper... | #summary #topic |
| [[Papers Explained 114 - Phi-1]] | Phi-1 is a transformer based 1.3B LLM for code, trained using a selection of “textbook quality” data from the web (6B tokens) and synthetically generated textbooks and exercises... | #summary #topic |
| [[Papers Explained 115 - Phi-1.5]] | Phi-1.5 follows the phi-1 approach, focusing this time on common sense reasoning in natural language, and creating a new 1.3 billion parameter model, with performance on natural... | #summary #topic |
| [[Papers Explained 116 - Phi-2]] | Phi-2 is a 2.7B parameter model that follows the phi approach, trained on 1.4T tokens from multiple passes on a mixture of Synthetic and Web datasets for NLP and coding.It is... | #summary #topic |
| [[Papers Explained 117 - MM1]] | MM1 is a family of multimodal models up to 30B parameters, consisting of both dense models and mixture-of-experts variants, that are SOTA in pre-training metrics and achieve... | #summary #topic |
| [[Papers Explained 118 - WRAP]] | WRAP (Web Rephrase Augmented Pre-training) uses instruction-tuned models to paraphrase noisy web documents into synthetic training data, improving pre-training efficiency and out-of-distribution performance. | #summary #topic |
| [[Papers Explained 119 - DBRX]] | DBRX is an open, general-purpose Large Language Model (LLM) created by Databricks. It sets a new state-of-the-art surpassing existing models like GPT-3.5 and is competitive with... | #summary #topic |
| [[Papers Explained 12 - LiLT]] | All the bounding box coordinates are normalised and discretized to integers in the range [0, 1000], and four embedding layers are used to generate x-axis, y-axis, height and width... | #summary #topic |
| [[Papers Explained 120 - BloombergGPT]] | BloombergGPT is a 50 billion parameter language model that supports a wide range of tasks within the financial industry. | #summary #topic |
| [[Papers Explained 121 - Pythia]] | Pythia is a suite of 16 LLMs all trained on public data seen in the exact same order and ranging in size from 70M to 12B parameters, with public access provided to 154 checkpoints... | #summary #topic |
| [[Papers Explained 122 - Sparse Transformer]] | Sparse Transformers introduce sparse factorizations of the attention matrix to reduce the time and memory consumption to O(n√ n) in terms of sequence lengths. It also introduces: | #summary #topic |
| [[Papers Explained 123 - WebGPT]] | WebGPT is GPT-3 fine-tuned to answer long-form questions using a text-based web browsing environment (allowing the model to search and navigate the web) using imitation learning... | #summary #topic |
| [[Papers Explained 124 - CodeGemma]] | CodeGemma is a collection of open code models built on top of Gemma by further training on more than 500 billion tokens of code, capable of a variety of code and natural language... | #summary #topic |
| [[Papers Explained 125 - CodeGen]] | CodeGen is a 16.1B parameter LLM trained for program synthesis using input-output examples and natural language descriptions. | #summary #topic |
| [[Papers Explained 126 - CodeGen2]] | CodeGen2 proposes an approach to make the training of LLMs for program synthesis more efficient by unifying key components of model architectures, learning methods, infill... | #summary #topic |
| [[Papers Explained 127 - WizardLM]] | Wizard LM shows an avenue for creating large amounts of instruction data with varying levels of complexity using LLM instead of humans. Starting with an initial set of... | #summary #topic |
| [[Papers Explained 128 - WizardCoder]] | WizardCoder empowers Code LLMs (specifically StarCoder) with complex instruction fine-tuning, by adapting the Evol-Instruct method to the domain of code. It surpasses all other... | #summary #topic |
| [[Papers Explained 129 - WizardMath]] | WizardMath enhances the mathematical reasoning abilities of Llama-2, by applying the proposed Reinforcement Learning from Evol-Instruct Feedback (RLEIF) method to the domain of... | #summary #topic |
| [[Papers Explained 13 - Layout LM v3]] | The word Embeddings are initialized with a word embedding matrix from a pre-trained model RoBERTa. | #summary #topic |
| [[Papers Explained 130 - Phi-3]] | phi-3-mini is a 3.8B language model trained on 3.3T tokens data which is a scaled-up version of the one used for phi-2, composed of heavily filtered web data and synthetic data.It... | #summary #topic |
| [[Papers Explained 131 - Hawk, Griffin]] | This work presents the Real-Gated Linear Recurrent Unit (RG-LRU) layer, a novel gated linear recurrent layer, around which a new recurrent block is designed to replace Multi Query... | #summary #topic |
| [[Papers Explained 132 - RecurrentGemma]] | RecurrentGemma-2B is an open model based on the Griffin architecture. It uses a combination of linear recurrences and local attention instead of global attention. | #summary #topic |
| [[Papers Explained 133 - Rho-1]] | The study analyzes token-level training dynamics of language models, revealing distinct loss patterns for different tokens. RHO-1 leverages these insights and employs Selective... | #summary #topic |
| [[Papers Explained 134 - Open ELM]] | OpenELM is an open language model by Apple with not only open source model weights and inference code but the complete framework for training and evaluation of the language model. | #summary #topic |
| [[Papers Explained 135 - DSPy]] | The DSPy programming model first translates string-based prompting techniques, including complex and task-dependent ones like Chain of Thought and ReAct into declarative modules... | #summary #topic |
| [[Papers Explained 136 - LLMLingua]] | LLMLingua is a coarse-to-fine prompt compression method that involves a budget controller to maintain semantic integrity under high compression ratios, a token-level iterative... | #summary #topic |
| [[Papers Explained 137 - LongLLMLingua]] | LongLLMLingua is a framework designed for prompt compression in long context scenarios. It addresses three main challenges associated with LLMs in long context scenarios: higher... | #summary #topic |
| [[Papers Explained 138 - LLMLingua-2]] | LLMLingua-2 focuses on task-agnostic prompt compression for better generalizability and efficiency in LLMs. It proposes a data distillation procedure to derive knowledge from an... | #summary #topic |
| [[Papers Explained 139 - Gorilla]] | Data is collected from various sources, specifically HuggingFace’s Model Hub, PyTorch Hub, and TensorFlow Hub Models. These sources contain a large number of machine learning... | #summary #topic |
| [[Papers Explained 14 - RCNN]] | The first generates category-independent region proposals. These proposals define the set of candidate detections available to our detector. | #summary #topic |
| [[Papers Explained 140 - Toolformer]] | Toolformer is a model trained to decide which APIs to call, when to call them, what arguments to pass, and how to best incorporate the results into future token prediction. This... | #summary #topic |
| [[Papers Explained 141 - Tool LLM]] | Open-source LLMs struggle with tasks that require interaction with external tools or APIs, to address this limitation, this paper introduces Tool Bench, an instruction-tuning... | #summary #topic |
| [[Papers Explained 142 - Gemini 1.5 Flash]] | Gemini 1.5 Flash is a more lightweight variant designed for efficiency with minimal regression in quality. It is a transformer decoder model with the same 2M+ context and... | #summary #topic |
| [[Papers Explained 143 - Chameleon]] | Chameleon is a family of early-fusion token-based mixed-modal models capable of reasoning over and generating interleaved image-text documents, setting a new bar for open... | #summary #topic |
| [[Papers Explained 145 - LoRA]] | Low-Rank Adaptation or LoRA freezes the pretrained model weights and injects trainable rank decomposition matrices into each layer of the Transformer architecture, greatly... | #summary #topic |
| [[Papers Explained 146 - QLoRA]] | QLoRA is an efficient finetuning approach that reduces memory usage for fine-tuning hplarge models on a single GPU while preserving full 16-bit fine tuning task performance by... | #summary #topic |
| [[Papers Explained 147 - LongLoRA]] | LongLoRA is an efficient fine-tuning approach that extends the context sizes of pre-trained LLMs, with limited computation cost. | #summary #topic |
| [[Papers Explained 148 - Direct Preference Optimization]] | Supervised Fine-Tuning (SFT): This phase starts with fine-tuning a pre-trained Language Model (LM) on high-quality data relevant to the downstream tasks. The goal is to obtain a... | #summary #topic |
| [[Papers Explained 149 - RLHF Workflow]] | This work presents the workflow of Online Iterative Reinforcement Learning from Human Feedback (RLHF) and discusses the theoretical insights and algorithmic principles behind... | #summary #topic |
| [[Papers Explained 15 - Fast RCNN]] | Training is a multi-stage pipeline: R-CNN first finetunes a ConvNet on object proposals using log loss. Then, it fits SVMs to ConvNet features. These SVMs act as object detectors... | #summary #topic |
| [[Papers Explained 150 - MarianMT]] | Marian is a robust and self-contained Neural Machine Translation system. It is entirely implemented in C++ and features a built-in automatic differentiation engine using dynamic... | #summary #topic |
| [[Papers Explained 151 - Aya 23]] | Aya 23 is a family of multilingual language models that can serve 23 languages. It is an improvement over the previous model, Aya 101, which covered 101 languages but had... | #summary #topic |
| [[Papers Explained 152 - SigLip]] | This paper proposes a simple pairwise Sigmoid loss for Language-Image Pre-training (SigLIP). Unlike standard contrastive learning with softmax normalization, the sigmoid loss... | #summary #topic |
| [[Papers Explained 153 - CTRL]] | CTRL is a 1.63 billion-parameter conditional transformer language model, trained to condition on control codes that govern style, content, and task-specific behavior. | #summary #topic |
| [[Papers Explained 154 - BLIP]] | BLIP is a new VLP framework which transfers flexibly to both vision-language understanding and generation tasks. BLIP effectively utilizes the noisy web data by bootstrapping the... | #summary #topic |
| [[Papers Explained 155 - BLIP 2]] | BLIP-2 is a generic and efficient pretraining strategy that bootstraps vision-language pre-training from off-the-shelf frozen pre-trained image encoders and frozen large language... | #summary #topic |
| [[Papers Explained 156 - InstructBLIP]] | This paper conducts a systematic and comprehensive study on vision-language instruction tuning based on the pretrained BLIP-2 models. 26 publicly available datasets, covering a... | #summary #topic |
| [[Papers Explained 157 - Gemma 2]] | Gemma 2 is a new addition to the Gemma family with several technical modifications, including interleaving local-global attentions and group-query attention. The model is trained... | #summary #topic |
| [[Papers Explained 158 - XLM]] | XLM is a transformer-based model, built by Meta. It extends the approach of generative pretraining to multiple languages and shows the effectiveness of cross-lingual pretraining. | #summary #topic |
| [[Papers Explained 159 - XLM Roberta]] | XLM-RoBERTa combines RoBERTa techniques with XLM, excluding translation language modelling. Instead, it focuses on masked language modelling in sentences from a single language.... | #summary #topic |
| [[Papers Explained 16 - Faster RCNN]] | Faster R-CNN, is composed of two modules. The first module is a deep fully convolutional network that proposes regions, and the second module is the Fast R-CNN detector that uses... | #summary #topic |
| [[Papers Explained 160 - Orca]] | A 13B LLM that learns to imitate the reasoning process of SOTA LLMs, utilizing rich signals from GPT-4 including explanation traces; step-by-step thought processes; and other... | #summary #topic |
| [[Papers Explained 161 - Orca 2]] | Orca 2 continues exploring how improved training signals can enhance smaller LMs’ reasoning abilities. It aims to teach the model various reasoning techniques (step-by-step... | #summary #topic |
| [[Papers Explained 162 - PEGASUS]] | PEGASUS (Pre-training with Extracted Gap-sentences for Abstractive SUmmarization Sequence-to-sequence models) utilizes the same encoder-decoder model architecture as BART. For... | #summary #topic |
| [[Papers Explained 163 - Orca Math]] | Orca-Math is a 7B-sized language model (SLM) based on the Mistral-7B. It achieves an accuracy rate of 86.81% on the GSM8k dataset without requiring multiple model calls... | #summary #topic |
| [[Papers Explained 164 - Orca 3 (Agent Instruct)]] | The study focuses on using synthetic data for post-training, specifically creating data by powerful models to teach a new skill or behavior to another model, referred to as... | #summary #topic |
| [[Papers Explained 165 - Reformer]] | Reformer by Google Research is designed with new methods to reduce memory usage and computation time. As a result, this model can handle much longer sentences compared to... | #summary #topic |
| [[Papers Explained 166 - Command Models]] | Command R is a 35B LLM designed for production-scale AI in enterprises. It is a scalable generative model that balances efficiency with accuracy, enabling companies to move beyond... | #summary #topic |
| [[Papers Explained 167 - Monte Carlo Tree Self-refine]] | Monte Carlo Tree Self-refine combines LLMs with Monte Carlo Tree Search (MCTS) to improve performance in complex mathematical reasoning tasks. | #summary #topic |
| [[Papers Explained 168 - NV-Embed]] | NV-Embed proposes a latent attention layer to obtain pooled embeddings and removes causal attention mask during contrastive training to significantly enhance the performance of... | #summary #topic |
| [[Papers Explained 169 - mBART]] | mBART is a sequence-to-sequence denoising auto-encoder pre-trained on large-scale monolingual corpora in many languages using the BART objective. | #summary #topic |
| [[Papers Explained 17 - Mask RCNN]] | Faster R-CNN consists of two stages. The first stage, called a Region Proposal Network (RPN), proposes candidate object bounding boxes. The second stage, which is in essence Fast... | #summary #topic |
| [[Papers Explained 170 - Prometheus]] | A 13B fully open source evaluation LLM trained on Feedback Collection curated using GPT-4 (in this work). | #summary #topic |
| [[Papers Explained 171 - Prometheus 2]] | This Work curates Preference Collection, a fine-grained pairwise ranking feedback dataset that builds on the Feedback Collection. | #summary #topic |
| [[Papers Explained 172 - E5-V]] | E5-V leverages Multimodal Large Language Models Via prompts to effectively bridge the modality gap between different types of inputs, demonstrating strong performance in... | #summary #topic |
| [[Papers Explained 173 - ELECTRA]] | Efficiently Learning an Encoder that Classifies Token Replacements Accurately (ELECTRA), a unique transformer model jointly developed by Stanford University and Google, employs a... | #summary #topic |
| [[Papers Explained 174 - FineWeb]] | FineWeb is a large-scale dataset for pretraining LLMs, consisting of 15T tokens and 44TB of disk space. It was created by combining 96 CommonCrawl snapshots and is designed to... | #summary #topic |
| [[Papers Explained 175 - Cosmopedia]] | Cosmopedia aims to reproduce the training data used for Phi-1.5. It is a dataset of synthetic textbooks, blog posts, stories, posts, and WikiHow articles generated by... | #summary #topic |
| [[Papers Explained 176 - Smol LM]] | SmolLM is a series of state-of-the-art small language models available in three sizes: 135M, 360M, and 1.7B parameters. These models are built on a meticulously curated... | #summary #topic |
| [[Papers Explained 177 - WebSight]] | Despite VLMs have made significant progress in various tasks, converting website screenshots into functional HTML code has been minimally explored due to the lack of a suitable... | #summary #topic |
| [[Papers Explained 178 - Docmatix]] | Docmatix is a large-scale dataset for Document Visual Question Answering (DocVQA) that is hundreds of times larger than previously available datasets. The dataset contains 2.4... | #summary #topic |
| [[Papers Explained 179 - Obelics, Idefics]] | This work curates Obelics, an openly-accessible web-scale dataset consisting of 141M multimodal English web documents containing 353M associated images and 115B tokens. Obelics... | #summary #topic |
| [[Papers Explained 18 - TableNet]] | If convolutional filters utilized to detect tables, can be reinforced by column detecting filters, this should significantly improve the performance of the model. TableNet model... | #summary #topic |
| [[Papers Explained 180 - Idefics 2]] | Idefics2 is a family of general multimodal model that takes in arbitrary sequences of text and images and generates text responses. | #summary #topic |
| [[Papers Explained 181 - Claude]] | The Claude 3 model family, announced by Anthropic, introduces three advanced models: Claude 3 Haiku, Claude 3 Sonnet, and Claude 3 Opus. Each successive model offers increasingly... | #summary #topic |
| [[Papers Explained 182 - DeBERTa V3]] | DeBERTa enhances BERT with Disentangled Attention (DA) and an improved mask decoder. Unlike BERT, which uses a single vector for content and position, DA employs separate vectors... | #summary #topic |
| [[Papers Explained 183 - Magpie]] | Magpie is a self-synthesis method for generating large-scale alignment data. It is based on the observation that aligned LLMs like Llama-3-Instruct because of their... | #summary #topic |
| [[Papers Explained 184 - Instruction Pretraining]] | Instead of directly pre-training on raw corpora, Instruction Pre-Training augments each text from the raw corpora with a set of instruction-response pairs generated by an... | #summary #topic |
| [[Papers Explained 185 - GPT-4o]] | GPT-4o is an autoregressive omni model, which accepts as input any combination of text, audio, image, and video and generates any combination of text, audio, and image outputs.... | #summary #topic |
| [[Papers Explained 186 - Grok]] | Grok is a 314B Mixture-of-Experts model, with 25% of the weights active on a given token, modeled after the Hitchhiker’s Guide to the Galaxy, hence designed to answer questions... | #summary #topic |
| [[Papers Explained 187a - Llama 3]] | Llama 3 is a new set of foundation models, designed for multilinguality, coding, reasoning, and tool usage. The largest model boasts 405B parameters and a 128K token context... | #summary #topic |
| [[Papers Explained 187b - Llama 3.1]] | Llama 3 is a new set of foundation models, designed for multilinguality, coding, reasoning, and tool usage. The largest model boasts 405B parameters and a 128K token context... | #summary #topic |
| [[Papers Explained 187c - Llama 3.1 — Multimodal Experiments]] | Llama 3 is a new set of foundation models, designed for multilinguality, coding, reasoning, and tool usage. The largest model boasts 405B parameters and a 128K token context... | #summary #topic |
| [[Papers Explained 187d - Llama 3.2]] | Llama 3 is a new set of foundation models, designed for multilinguality, coding, reasoning, and tool usage. | #summary #topic |
| [[Papers Explained 187e - Quantized Llama 3.2, Llama 3.3]] | Llama 3 is a new set of foundation models, designed for multilinguality, coding, reasoning, and tool usage. | #summary #topic |
| [[Papers Explained 188 - Hermes 3]] | The models are available at [HuggingFace](https://huggingface.co/collections/NousResearch/hermes-3-66bd6c01399b14b08fe335ea). | #summary #topic |
| [[Papers Explained 189 - Proofread]] | Proofread is a novel feature in Gboard that uses a server-side Large Language Model (LLM) to provide seamless sentence-level and paragraph-level corrections with a single tap... | #summary #topic |
| [[Papers Explained 19 - Dit]] | DiT is a self-supervised pre-trained Document Image Transformer model using large-scale unlabeled text images for Document AI tasks. We leverage DiT as the backbone network in a... | #summary #topic |
| [[Papers Explained 190 - BLIP-3 (xGen-MM)]] | xGen-MultiModal (xGen-MM) also known as BLIP-3, expands the Salesforce xGen initiative on foundation AI models. It is a framework for developing Large Multimodal Models consisting... | #summary #topic |
| [[Papers Explained 192 - Phi-3.5]] | Phi-3.5 is a family of lightweight, state-of-the-art open models built upon datasets used for Phi-3 — synthetic data and filtered publicly available documents — with a focus on... | #summary #topic |
| [[Papers Explained 193 - BERTopic]] | BERTopic generates document embedding with pre-trained transformer-based language models, clusters these embeddings, and finally, generates topic representations with the... | #summary #topic |
| [[Papers Explained 194 - PaLI]] | At its core, PaLI has a text encoder decoder Transformer.To include vision as input, the text encoder is fed with a sequence of visual “tokens”: output patch features of a Vision... | #summary #topic |
| [[Papers Explained 195 - PaLI-X]] | This work focuses on scaling a Vision-Language model to achieve outstanding performance on a wide variety of benchmarks. | #summary #topic |
| [[Papers Explained 196 - PaLI-3]] | PaLI-3 is a 5B vision language model that outperforms larger models on various benchmarks. It uses a multilingual contrastive vision model scaled to 2B parameters, obtained using... | #summary #topic |
| [[Papers Explained 197 - Pali Gemma]] | PaliGemma is an open model that continues the line of PaLI vision-language models by combining the SigLIP-So400m vision encoder with the Gemma-2B language model. | #summary #topic |
| [[Papers Explained 198 - ColPali]] | ColPali leverages the document understanding capabilities of recent Vision Language Models to produce high-quality contextualized embeddings solely from images of document pages. | #summary #topic |
| [[Papers Explained 199 - CvT]] | Convolutional vision Transformer (CvT) improves Vision Transformer (ViT) in performance and efficiency by introducing convolutions into ViT to yield the best of both designs.... | #summary #topic |
| [[Papers Explained 20 - Donut]] | Donut is an end-to-end (i.e., self-contained) VDU model for general understanding of document images. The architecture of Donut is quite simple, which consists of a Transformer... | #summary #topic |
| [[Papers Explained 200 - SimCLR]] | SimCLR is a simple framework for contrastive learning of visual representations. The key components of the framework and findings are: | #summary #topic |
| [[Papers Explained 201 - SimCLRv2]] | The study proposes a semi-supervised learning framework that combines Unsupervised or self-supervised pre training (SimCLRv2) to learn general visual representations, Supervised... | #summary #topic |
| [[Papers Explained 202 - SynCLR]] | SynCLR (Synthetic Contrastive Learning) leverages generative models to redefine the granularity of visual classes for improving visual representations. | #summary #topic |
| [[Papers Explained 203 - Gecko]] | Gecko is a versatile text embedding model trained on a variety of tasks including document retrieval, semantic similarity, and classification. It leverages knowledge distillation... | #summary #topic |
| [[Papers Explained 204 - Matryoshka Adaptor]] | Matryoshka-Adaptor is a framework designed to customize LLM embeddings for improved computational efficiency and cost-effectiveness. The framework achieves substantial... | #summary #topic |
| [[Papers Explained 205 - LeViT]] | LeViT is a hybrid neural network for fast inference image classification. LeViT significantly outperforms existing convnets and vision transformers with respect to the... | #summary #topic |
| [[Papers Explained 206 - Nemotron-4 15B]] | Nemotron-4 15B is a large multilingual language model trained on 8T text tokens by Nvidia.It exhibits high downstream accuracies across a wide range of English, code, and... | #summary #topic |
| [[Papers Explained 207 - Nemotron-4 340B]] | A family of 340B models including a base model, instruct model and a reward model, aimed to benefit in various research studies and commercial applications, especially for... | #summary #topic |
| [[Papers Explained 208 - Minitron]] | The study investigates whether pruning an existing Large Language Model (LLM) and re-training it with a fraction of the original training data can be a suitable alternative to... | #summary #topic |
| [[Papers Explained 209 - Minitron Approach in Practice]] | This work presents a comprehensive report on compressing the Llama 3.1 8B and Mistral NeMo 12B models to 4B and 8B parameters, respectively, using the Minitron Approach. | #summary #topic |
| [[Papers Explained 21 - Feature Pyramid Network]] | Feature pyramids are a basic component in recognition systems for detecting objects at different scales. But recent deep learning object detectors have avoided pyramid... | #summary #topic |
| [[Papers Explained 210 - MaxViT]] | Max ViT introduces an efficient and scalable attention model called multi-axis attention, consisting of two aspects: blocked local and dilated global attention. These design... | #summary #topic |
| [[Papers Explained 211 - o1]] | OpenAI o1 is a large language model trained with reinforcement learning to perform complex reasoning. o1 thinks before it answers — it can produce a long internal chain of thought... | #summary #topic |
| [[Papers Explained 212 - DataGemma]] | The models are available at [HuggingFace](https://huggingface.co/collections/google/datagemma-release-66df7636084d2b150a4e6643/). | #summary #topic |
| [[Papers Explained 213 - Florence]] | While existing vision foundation models such as CLIP focus mainly on mapping images and textual representations to a cross-modal shared representation, Florence, expands the... | #summary #topic |
| [[Papers Explained 214 - Florence-2]] | While existing large vision models excel in transfer learning, they struggle to perform a diversity of tasks with simple instructions, Florence-2 was designed to take text-prompt... | #summary #topic |
| [[Papers Explained 215 - Swin Transformer V2]] | Swin Transformer v2 explores large-scale models in computer vision, addressing challenges like training stability, resolution gaps, and labeled data scarcity. It introduces... | #summary #topic |
| [[Papers Explained 216 - MobileLLM]] | Mobile LLM leverages deep and thin architectures, embedding sharing, and grouped-query attention mechanisms to establish a strong baseline network, which achieves a remarkable... | #summary #topic |
| [[Papers Explained 217 - H2O Danube 3]] | H2O-Danube3 is a series of small language models that can be efficiently run on modern smartphones and other edge devices. The models are trained on high-quality Web data and... | #summary #topic |
| [[Papers Explained 218 - Idefics 3]] | This paper can be seen as a tutorial for building a VLM. It begins by providing a comprehensive overview of the current state-of-the-art approaches, highlighting the strengths and... | #summary #topic |
| [[Papers Explained 219 - Pixtral]] | Pixtral is a 12B parameter natively multimodal vision-language model based on Mistral Nemo. It is trained with interleaved image and text data demonstrating strong performance on... | #summary #topic |
| [[Papers Explained 22 - Focal Loss for Dense Object Detection (RetinaNet)]] | The highest accuracy object detectors to date are based on a two-stage approach popularized by R-CNN, where a classifier is applied to a sparse set of candidate object locations. | #summary #topic |
| [[Papers Explained 220 - EfficientFormer]] | Efficient Former is a family of models optimized for inference speed. The paper revisits the design principles of ViT and its variants through latency analysis and identifies... | #summary #topic |
| [[Papers Explained 221 - Reader-LM]] | reader-lm-0.5b and reader-lm-1.5b are two SLMs specifically trained to generate clean markdown directly from noisy raw HTML. Both models are multilingual and support a context... | #summary #topic |
| [[Papers Explained 222 - Apple Intelligence Foundation Language Models]] | Apple Foundation Models are developed as part of Apple Intelligence, a personal intelligence system integrated into iOS 18, iPadOS 18, and macOS Sequoia. The AFM models are... | #summary #topic |
| [[Papers Explained 223 - LLM Compiler]] | LLM Compiler models are initialized with the weights of Code Llama and then trained for 401 billion tokens on a compiler centric dataset composed mostly of compiler intermediate... | #summary #topic |
| [[Papers Explained 224 - CriticGPT]] | RLHF is fundamentally limited by the capacity of humans to correctly evaluate model output. To improve human evaluation ability and overcome that limitation this work trains... | #summary #topic |
| [[Papers Explained 225 - FastViT]] | FastViT is a hybrid vision transformer architecture featuring a novel token mixing operator called RepMixer, which significantly improves model efficiency, achieving faster... | #summary #topic |
| [[Papers Explained 226 - RewardBench]] | RewardBench is a benchmark dataset and code-base for evaluating RMs. The dataset consists of prompt-win-lose trios spanning chat, reasoning, and safety, and is designed to... | #summary #topic |
| [[Papers Explained 227 - RAGAS]] | Evaluating RAG architectures is challenging because there are several dimensions to consider: the ability of the retrieval system to identify relevant and focused context... | #summary #topic |
| [[Papers Explained 228 - Direct Judgement Preference Optimization]] | This study investigates the idea of learning from both positive and negative data with preference optimization to enhance the evaluation capabilities of LLM judges across an array... | #summary #topic |
| [[Papers Explained 229 - Efficient ViT]] | It applies a single self-attention layer Φ^A_i for spatial mixing, which is sandwiched between FFN layers Φ^F_i . The computation can be formulated as: | #summary #topic |
| [[Papers Explained 23 - Structural LM]] | Taking advantage of existing pretrained language models and to adapt to document image understanding tasks, Structural LM uses the BERT architecture as the backbone. | #summary #topic |
| [[Papers Explained 230 - MAmmoTH]] | MAmmoTH is a series of open-source LLMs specifically tailored for general math problem-solving, trained on MathInstruct, a meticulously curated instruction tuning dataset compiled... | #summary #topic |
| [[Papers Explained 231 - MAmmoTH2]] | This work proposes a method to efficiently harvest 10M naturally existing instruction data from the pre-training web corpus to enhance LLMs’ reasoning abilities. The approach... | #summary #topic |
| [[Papers Explained 232 - MobileNetV4]] | An optimized neural architecture search (NAS) recipe is also introduced, which improves MNv4 search effectiveness. To further boost accuracy, a novel distillation technique is... | #summary #topic |
| [[Papers Explained 234 - SoViT]] | This paper introduces advanced methods for inferring compute-optimal model shapes, such as width and depth, challenging the prevailing approach of blindly scaling up vision models... | #summary #topic |
| [[Papers Explained 235 - CogVLM]] | Unlike existing methods that employ shallow alignment techniques — where image features are simply mapped into the input space of a language model — CogVLM innovates by... | #summary #topic |
| [[Papers Explained 236 - CogVLM2]] | The CogVLM2 family is a new generation of visual language models for image and video understanding. The family includes three models: CogVLM2, CogVLM2-Video, and GLM-4V. | #summary #topic |
| [[Papers Explained 237 - OWL ViT]] | OWL ViT (Vision Transformer for Open-World Localization) proposes a strong recipe for transferring image-text models to open-vocabulary object detection. | #summary #topic |
| [[Papers Explained 238 - Segment Anything Model]] | The Segment Anything (SA) project aims to build a foundation model for segmentation by introducing three interconnected components: a promptable segmentation task, a segmentation... | #summary #topic |
| [[Papers Explained 239 - SAM 2]] | Segment Anything Model 2 (SAM 2) is a foundation model designed to solve promptable visual segmentation in images and videos. The model is a simple transformer architecture with... | #summary #topic |
| [[Papers Explained 24 - ERNIE Layout]] | Given a document, ERNIE-Layout rearranges the token sequence with the layout knowledge and extracts visual features from the visual encoder. The textual and layout embeddings are... | #summary #topic |
| [[Papers Explained 240 - NVLM]] | NVLM 1.0 is a family of multimodal large language models (LLMs) rivaling proprietary and open-access models. Notably, NVLM 1.0 shows improved text-only performance over its LLM... | #summary #topic |
| [[Papers Explained 241 - Pixmo and Molmo]] | Molmo (Multimodal Open Language Model) utilizes PixMo (Pixels for Molmo), a high-quality dataset of detailed image captions collected from human annotators describing images... | #summary #topic |
| [[Papers Explained 242 - STORM]] | STORM is a writing system for the Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking. | #summary #topic |
| [[Papers Explained 243 - ShieldGemma]] | ShieldGemma is a comprehensive suite of LLM-based safety content moderation models ranging from 2B to 27B built upon Gemma2. These models provide robust, state-of-the-art... | #summary #topic |
| [[Papers Explained 244 - Gemma APS]] | This work focuses on the task of abstractive proposition segmentation: transforming text into simple, self-contained, well-formed sentences. | #summary #topic |
| [[Papers Explained 245 - Layout Parser]] | LayoutParser is an open-source library designed to streamline the application of deep learning (DL) in document image analysis (DIA) research and applications. | #summary #topic |
| [[Papers Explained 246 - BROS]] | The main Transformer structure of BROS is the same as BERT. BROS (BERT Relying On Spatiality) encodes relative positions of texts in 2D space and learns from unlabeled documents... | #summary #topic |
| [[Papers Explained 247 - Layout Reader]] | LayoutReader captures the text and layout information for reading order prediction using the seq2seq model. It performs almost perfectly in reading order detection and... | #summary #topic |
| [[Papers Explained 248 - LMDX]] | Firstly an OCR is used on the document image to obtain words and line segments, along with their corresponding spatial positions (bounding boxes) on the document. | #summary #topic |
| [[Papers Explained 249 - DINO]] | This paper investigates whether self-supervised learning enhances Vision Transformer performance compared to convolutional networks, finding that self-supervised ViT features... | #summary #topic |
| [[Papers Explained 25 - Vision Transformers]] | Inspired by the Transformer scaling successes in NLP, the idea is to apply a standard Transformer directly to images, with the fewest possible modifications. To do so, we split an... | #summary #topic |
| [[Papers Explained 250 - DINO v2]] | Recommended Reading [Papers Explained 249: DINO](https://ritvik19.medium.com/papers-explained-249-dino-f7e2c7f438ab) | #summary #topic |
| [[Papers Explained 251 - H2OVL-Mississippi]] | H2O VL Mississippi is a collection of smaller vision-language models, including H2OVL-Mississippi-0.8B and H2OVL-Mississippi-2B. These models were designed for efficiency and... | #summary #topic |
| [[Papers Explained 252 - Nemotron-Mini-Hindi]] | Nemotron-Mini-Hindi is a 4B bilingual SLM supporting both Hindi and English, based on Nemotron-Mini 4B. | #summary #topic |
| [[Papers Explained 253 - SPADE]] | Information Extraction (IE) for semistructured document images is often approached as a sequence tagging problem by classifying each recognized input token into one of the IOB... | #summary #topic |
| [[Papers Explained 254 - Pix2Struct]] | Pix2Struct, a pretrained image-to-text model for purely visual language understanding, which can be finetuned on tasks containing visually-situated language. Pix2Struct is... | #summary #topic |
| [[Papers Explained 255 - Matcha]] | Matcha (Math reasoning and Chart derendering pretraining) propose several pre-training tasks that cover plot deconstruction and numerical reasoning, starting from Pix2Struct to... | #summary #topic |
| [[Papers Explained 256 - DePlot]] | This paper presents the first few(one)- shot solution to visual language reasoning. It proposes to decompose visual language reasoning into two steps: (1) plot-to-text... | #summary #topic |
| [[Papers Explained 257 - Nougat]] | Nougat (Neural Optical Understanding for Academic Documents) is a Visual Transformer model that performs an Optical Character Recognition (OCR) task for processing scientific... | #summary #topic |
| [[Papers Explained 258 - GeoLayoutLM]] | Visual information extraction (VIE) is divided into two tasks: semantic entity recognition (SER) and relation extraction (RE). Most of the existing models learn the geometric... | #summary #topic |
| [[Papers Explained 259 - OmniParser]] | VLMs struggle to effectively interact with user interfaces due to the lack of robust screen parsing techniques. These techniques are crucial for: | #summary #topic |
| [[Papers Explained 26 - Swin Transformer]] | Swin Transformer constructs a hierarchical representation by starting from small-sized patches and gradually merging neighboring patches in deeper Transformer layers. | #summary #topic |
| [[Papers Explained 260 - GSM-Symbolic]] | This research investigates the true mathematical reasoning abilities of LLMs by addressing concerns about the reliability of existing benchmarks like GSM8K. The authors introduce... | #summary #topic |
| [[Papers Explained 261 - MM-1.5]] | Recommended Reading [Papers Explained 117: MM1](https://ritvik19.medium.com/papers-explained-117-mm1-c579142bcdc0/) | #summary #topic |
| [[Papers Explained 262 - PromptWizard]] | Prompt Wizard is a novel framework that uses LLMs to iteratively synthesize and refine prompts tailored to specific tasks. | #summary #topic |
| [[Papers Explained 263 - Jina Embeddings v1]] | Jina Embeddings are a set of sentence embedding models ranging from 35M to 6B parameters that translate textual inputs into numerical representations, capturing the semantics of... | #summary #topic |
| [[Papers Explained 264 - Jina Embeddings v2]] | The current open-source text embedding models struggle to represent lengthy documents and often resort to truncation, requiring splitting documents into smaller paragraphs for... | #summary #topic |
| [[Papers Explained 265 - Jina Bilingual Embeddings]] | This paper presents a novel suite of state-of-the-art bilingual text embedding models that are designed to support English and another target language. These models are capable of... | #summary #topic |
| [[Papers Explained 266 - Jina Embeddings v3]] | Recommended Reading [Papers Explained 265: Jina Bilingual Embeddings](https://ritvik19.medium.com/papers-explained-265-jina-bilingual-embeddings-39960d6f7a7c) | #summary #topic |
| [[Papers Explained 267 - Jina Reranker]] | Jina Reranker is a neural reranking model designed to tackle this critical issue of relevancy. It enhances search and RAG system by reordering retrieved documents in a manner that... | #summary #topic |
| [[Papers Explained 269 - Eagle]] | This work systematically investigates the mixture-of-vision-encoders design space for improved MLLM perception and leads to several interesting new findings: | #summary #topic |
| [[Papers Explained 27 - BEiT]] | The images have two views of representations in our method, namely, image patch, and visual tokens. The two types serve as input and output representations during pre-training... | #summary #topic |
| [[Papers Explained 270 - OLMoE]] | OLMoE is a sparse Mixture-of-Experts based Language Model with 7B parameters, out of which only 1B parameters are active per input token, making it more cost-effective than dense... | #summary #topic |
| [[Papers Explained 271 - Spreadsheet LLM]] | where S ∈ Rm,n denotes the spreadsheet, T ∈ R1 denotes the text representation of a cell, and i, j, m, n respectively represent the row and column in- dex of the cell and the row... | #summary #topic |
| [[Papers Explained 272 - RAFT]] | Retrieval Augmented Fine Tuning (RAFT) is a training method designed to enhance the performance of LLMs for “open-book” in-domain question answering tasks. Given a context and a... | #summary #topic |
| [[Papers Explained 273 - LongCite]] | Given a long context D and a query q, the LLM is required to return a response A, which consists of n statements s_1, . . . , s_n, and each statement s_i cites a list of snippets... | #summary #topic |
| [[Papers Explained 274 - Thought Preference Optimization]] | Starting with a typical instruction-tuned LLM that outputs a response directly after the user instruction and assuming that there is no provided labeled thought data that can be... | #summary #topic |
| [[Papers Explained 275 - Self-Consistency Preference Optimization]] | Self-consistency is a method applied at inference time based on multiple sampling in order to find the most consistent answer. Self-consistency preference optimization (SCPO)... | #summary #topic |
| [[Papers Explained 276 - Self-Taught Evaluators]] | This paper presents an approach that aims to improve evaluators without human annotations, using synthetic training data only. | #summary #topic |
| [[Papers Explained 277 - ModernBERT]] | The models are available at [HuggingFace](https://huggingface.co/collections/answerdotai/modernbert-67627ad707a4acbf33c41deb). | #summary #topic |
| [[Papers Explained 278 - Phi-4]] | Phi-4 is a 14B parameter model that advances the performance of small language models by introducing innovative synthetic data generation methods for reasoning-focused tasks. This... | #summary #topic |
| [[Papers Explained 279 - LearnLM Tutor]] | LearnLM-Tutor is a text-based conversational AI tutor, built upon Gemini 1.0 and fine-tuned for 1:1 educational interactions, evaluated with seven pedagogical benchmarks... | #summary #topic |
| [[Papers Explained 28 - Masked AutoEncoder]] | The appetite for data has been successfully addressed in natural language processing (NLP) by self-supervised pretraining. The solutions, based on autoregressive language modeling... | #summary #topic |
| [[Papers Explained 280 - LearnLM]] | LearnLM is designed to enhance Gemini’s learning capabilities and is trained using pedagogical instruction following. This involves providing the model with system-level... | #summary #topic |
| [[Papers Explained 281 - Tulu]] | This paper explores the instruction-tuning of language models using various open-source datasets. | #summary #topic |
| [[Papers Explained 282 - Tulu V2]] | Since the release of TÜLU, open resources for instruction tuning have developed quickly, from better base models to new finetuning techniques. This has resulted in TÜLU 2. | #summary #topic |
| [[Papers Explained 283 - Tulu V3]] | The [models](https://huggingface.co/collections/allenai/tulu-3-models-673b8e0dc3512e30e7dc54f5) and... | #summary #topic |
| [[Papers Explained 284 - OLMo 2]] | A decoder-only transformer architecture is adopted, delivering 7B and 13B parameter variants. The architecture is very similar to the first iteration of OLMo with several changes... | #summary #topic |
| [[Papers Explained 285 - OpenScholar]] | OpenScholar is a specialized retrieval-augmented language model that answers scientific queries by identifying relevant passages from 45 million open-access papers and... | #summary #topic |
| [[Papers Explained 286 - NuNER]] | NuNER is a compact language representation model specialized in the Named Entity Recognition (NER) task. It can be fine-tuned to solve downstream NER problems in a data-efficient... | #summary #topic |
| [[Papers Explained 287 - NuExtract]] | NuExtract is a lightweight text-to-JSON LLM, that allows extraction of arbitrarily complex information from text and turns it into structured data. This model can be directly used... | #summary #topic |
| [[Papers Explained 288 - STaR]] | Self-Taught Reasoner (STaR) is a technique to iteratively leverage a small number of rationale examples and a large dataset without rationales, to boot- strap the ability to... | #summary #topic |
| [[Papers Explained 289 - V-STaR]] | Verification for Self-Taught Reasoners (V-STaR) utilizes both the correct and incorrect solutions generated during the self-improvement process to train a verifier using DPO that... | #summary #topic |
| [[Papers Explained 29 - ConvMixer]] | ConvMixer is similar to the Vision Transformer (and MLP-Mixer) in many respects: it directly operates on patches, it maintains an equal-resolution-and-size representation... | #summary #topic |
| [[Papers Explained 290 - rStar-Math]] | rStar-Math demonstrates that small language models (SLMs) can rival or even surpass the math reasoning capability of OpenAI o1, without distillation from superior models. | #summary #topic |
| [[Papers Explained 291 - Multiagent Debate]] | Multiagent Debate is a complementary approach to improve language responses where multiple language model instances propose and debate their individual responses and reasoning... | #summary #topic |
| [[Papers Explained 292 - Multiagent Finetuning]] | Multiagent Fine Tuning is a complementary approach towards self-improvement where finetuning is applied to a multiagent society of language models. A group of language models, all... | #summary #topic |
| [[Papers Explained 293 - TLDR]] | TLDR generation is a new form of extreme summarization, for scientific papers which involves high source compression and requires expert background knowledge and understanding of... | #summary #topic |
| [[Papers Explained 294 - Multi-LLM Text Summarization]] | Each LLM is prompted once, and their summaries are gathered. A single evaluation step then selects the best final summary. | #summary #topic |
| [[Papers Explained 295 - ReaderLM v2]] | ReaderLM’s second generation is a 1.5B parameter language model that converts raw HTML into beautifully formatted markdown or JSON with superior accuracy and improved longer... | #summary #topic |
| [[Papers Explained 296 - MAmmoTH-VL]] | To achieve both scale and diversity while maintaining accessibility for open-source initiatives, data is sourced from 153 publicly available multimodal instruction datasets. The... | #summary #topic |
| [[Papers Explained 297 - Maya]] | Maya is an open-source Multimodal Multilingual model to address the significant gaps remaining in the ability of current VLMs to handle low-resource languages and varied cultural... | #summary #topic |
| [[Papers Explained 298 - Llava-Mini]] | LLaVA-Mini is a unified large multimodal model that can support the understanding of images, high-resolution images, and videos in an efficient manner. | #summary #topic |
| [[Papers Explained 299 - Red Pajama]] | In the first iteration of the RedPajama datasets, the primary goal is to recreate the training data documented in the LLaMA technical report. To this end, the descriptions of the... | #summary #topic |
| [[Papers Explained 30 - DocFormer]] | Joint Multi-Modal: VL-BERT, LayoutLMv2, VisualBERT, MMBT]: In this type of architecture, vision and text are concatenated into one long sequence which makes transformers... | #summary #topic |
| [[Papers Explained 300 - Shiksha]] | Contextual Understanding: Models often struggle to grasp the context of a sentence, leading to incorrect translations. | #summary #topic |
| [[Papers Explained 301 - ReST]] | Reinforced Self-Training (ReST) is a simple algorithm for aligning LLMs with human preferences inspired by growing batch reinforcement learning (RL). Given an initial LLM policy... | #summary #topic |
| [[Papers Explained 302 - ReST^EM]] | ReST-EM is a simple self-training method based on expectation-maximization. It involves (1) generating samples from the model and filtering them using binary feedback, (2)... | #summary #topic |
| [[Papers Explained 303 - Reward rAnked FineTuning (RAFT)]] | Generative foundation models can inherit implicit biases from their extensive unsupervised training data, leading to suboptimal samples, skewed outcomes, and unfairness.... | #summary #topic |
| [[Papers Explained 304 - Constrained Generative Policy Optimization (Mixture of Judges)]] | RLHF has limitations in multi-task learning (MTL) due to challenges of extreme multi-objective optimization (i.e., trade-off of multiple and/or sometimes conflicting objectives)... | #summary #topic |
| [[Papers Explained 305 - Hyperfitting]] | Hyperfitting is conceptually straightforward and consists of fine-tuning a pre-trained model on a small set of samples until the model achieves a near-zero training loss. This is... | #summary #topic |
| [[Papers Explained 306 - Critique Fine-Tuning]] | Critique Fine-Tuning (CFT) is a strategy where models learn to critique noisy responses rather than simply imitate correct ones. Inspired by human learning processes that... | #summary #topic |
| [[Papers Explained 307 - Diverse Preference Optimization]] | Diverse Preference Optimization (DivPO) is an online optimization method which learns to generate much more diverse responses than standard pipelines, while maintaining the... | #summary #topic |
| [[Papers Explained 308 - SFT Memorizes, RL Generalizes]] | This paper studies the comparative effect of SFT and RL on generalization and memorization, focusing on text-based and visual environments. It shows that: | #summary #topic |
| [[Papers Explained 31 - Single Shot MultiBox Detector]] | The SSD approach is based on a feed-forward convolutional network that produces a fixed-size collection of bounding boxes and scores for the presence of object class instances in... | #summary #topic |
| [[Papers Explained 310 - SmolLM2]] | SmolLM2 is a 1.7B parameter language model overtrained on ~11 trillion tokens of data using a multi-stage training process that mixes web text with specialized math, code, and... | #summary #topic |
| [[Papers Explained 312 - It’s All in The MASK]] | This paper introduces ModernBERT-Large-Instruct, a 0.4B-parameter encoder model that leverages its masked language modeling (MLM) head for generative classification. This model... | #summary #topic |
| [[Papers Explained 313 - Document Screenshot Embedding]] | Document Screenshot Embedding (DSE) is a novel retrieval paradigm that regards document screenshots as a unified input format. DSE does not require any content extraction... | #summary #topic |
| [[Papers Explained 314 - vdr Embeddings]] | The models and datasets are available at [HuggingFace](https://huggingface.co/collections/llamaindex/visual-document-retrieval-678151d19d2758f78ce910e1). | #summary #topic |
| [[Papers Explained 315 - mmE5]] | broad scope ensures that the generated data covers diverse tasks and modalities, making it applicable to various downstream scenarios. | #summary #topic |
| [[Papers Explained 317 - Competitive Programming with Large Reasoning Models]] | This paper explores how reinforcement learning significantly improves large language models’ (LLMs) performance on complex coding and reasoning tasks, specifically within the... | #summary #topic |
| [[Papers Explained 318 - Autoregressive Image Models (AIM)]] | Autoregressive Image Models (AIM) are a collection of vision models pre-trained with an autoregressive objective. These models are inspired by their textual counterparts, i.e.... | #summary #topic |
| [[Papers Explained 319 - Autoregressive Image Models V2 (AIM V2)]] | Autoregressive Image Models V2 (AIM V2) extends the Autoregressive Image Models (AIM) framework to a multimodal setting, i.e., images and text. This is achieved by pairing the... | #summary #topic |
| [[Papers Explained 32 - ColD Fusion]] | Improving a pretrained model has the potential to improve every model finetuned on it. However, pretraining is often computationally expensive, so practitioners rarely seek to... | #summary #topic |
| [[Papers Explained 320 - SigLIP 2]] | In addition to training a set of models and adapting each model separately to different resolutions while distorting the aspect ratio, variants which process images while largely... | #summary #topic |
| [[Papers Explained 321 - Persona Hub]] | This work proposes a novel persona-driven data synthesis methodology that leverages various perspectives within a LLM to create diverse synthetic data. | #summary #topic |
| [[Papers Explained 322 - Phi 4 Mini, Phi 4 Multimodal]] | A 3.8B parameter language model excelling in math and coding, utilizing high-quality web and synthetic data, and featuring a 200K token vocabulary and group query attention. | #summary #topic |
| [[Papers Explained 323 - SysGen]] | SysGen is a pipeline for generating system messages with better aligned assistant responses. This is achieved from the supervised fine-tuning dataset without system messages.... | #summary #topic |
| [[Papers Explained 324 - Thinking Preference Optimization]] | Thinking Preference Optimization (ThinkPO) utilizes readily available or easily obtainable short CoT reasoning responses as rejected answers and long CoT responses as chosen... | #summary #topic |
| [[Papers Explained 325 - Selective Self-to-Supervised Fine-Tuning (S3FT)]] | S3FT (Self-Supervised Self-Training Fine-Tuning) aims to fine-tune large language models (LLMs) for specific tasks while minimizing the degradation of their general capabilities... | #summary #topic |
| [[Papers Explained 326 - olmOCR]] | olmOCR is an open-source Python toolkit for processing PDFs into clean, linearized plain text in natural reading order while preserving structured content like sections, tables... | #summary #topic |
| [[Papers Explained 327 - NeoBERT]] | NeoBERT is a next-generation encoder that redefines the capabilities of bidirectional models by integrating state-of-the-art advancements in architecture, modern data, and... | #summary #topic |
| [[Papers Explained 328 - LIMO]] | LIMO demonstrates unprecedented performance and efficiency in mathematical reasoning. With merely 817 curated training samples, LIMO improves the performance of previous strong... | #summary #topic |
| [[Papers Explained 329 - Gemma 3]] | Gemma 3 is a multimodal addition to the Gemma family, ranging in scale from 1 to 27 billion parameters. This version introduces vision understanding abilities, a wider coverage of... | #summary #topic |
| [[Papers Explained 33 - ELMo]] | Pre-trained word representations should ideally model both: complex characteristics of word use (e.g., syntax and semantics), and how these uses vary across linguistic contexts... | #summary #topic |
| [[Papers Explained 330 - Gemini Embedding]] | Gemini Embedding leverages the power of Gemini to produce highly generalizable embeddings for text spanning numerous languages and textual modalities. | #summary #topic |
| [[Papers Explained 331 - MAmmoTH-VL 2]] | The project is available on [GitHub](https://tiger-ai-lab.github.io/VisualWebInstruct/). | #summary #topic |
| [[Papers Explained 332 - Aya Vision]] | The models are available on [HuggingFace](https://huggingface.co/collections/CohereLabs/cohere-labs-aya-vision-67c4ccd395ca064308ee1484/). | #summary #topic |
| [[Papers Explained 333 - SmolDocling]] | SmolDocling is a 256M parameter vision-language model Based on Hugging Face’s SmolVLM designed for end-to-end document conversion. It processes entire pages by generating DocTags... | #summary #topic |
| [[Papers Explained 334 - Kimi k1.5]] | Kimi k1.5 multi-modal LLM trained with RL, including its RL training techniques, multi-modal data recipes, and infrastructure optimization. | #summary #topic |
| [[Papers Explained 335 - Transformers without Normalization]] | This work demonstrates that Transformers without normalization can achieve the same or better performance using a remarkably simple technique. Dynamic Tanh (DyT), an element-wise... | #summary #topic |
| [[Papers Explained 336 - Rethinking Compute-Optimal Test-Time Scaling]] | What is the optimal approach to scale test-time computation across different policy models, PRMs, and problem difficulty levels? | #summary #topic |
| [[Papers Explained 337 - Logic-RL]] | This study explores the potential of rule-based reinforcement learning (RL) in large reasoning models. Synthetic logic puzzles are used as training data due to their controllable... | #summary #topic |
| [[Papers Explained 338 - Large-Scale Data Selection for Instruction Tuning]] | This work presents a systematic study of how well data selection methods scale, It finds that: | #summary #topic |
| [[Papers Explained 339 - Code Guided Synthetic data generation system (CoSyn)]] | Given a text query q about an image type, the goal is to create a synthetic multimodal dataset Dq = (I,T), where I is the image, and T is the textual instruction-tuning data... | #summary #topic |
| [[Papers Explained 34 - TransformerXL]] | The Transformer XL architecture is an extension of the original Transformer model for sequence-to-sequence tasks such as machine translation. The main difference between the two... | #summary #topic |
| [[Papers Explained 340 - CHASE]] | CHallenging AI with Synthetic Evaluations (CHASE) is a unified framework to synthetically generate challenging problems using LLMs without human involvement. For a given task, the... | #summary #topic |
| [[Papers Explained 341 - U-Net]] | Each blue box corresponds to a multi-channel feature map. The number of channels is denoted on top of the box. The x-y-size is provided at the lower left edge of the box. White... | #summary #topic |
| [[Papers Explained 342 - U-ViT]] | U-ViT is a simple and general ViT-based architecture for image generation with diffusion models, characterized by treating all inputs including the time, condition and noisy image... | #summary #topic |
| [[Papers Explained 343 - LSNet]] | Token mixing aims to generate a feature representation (yi) for each token (xi) based on its contextual region (N(xi)). This process involves two key steps: | #summary #topic |
| [[Papers Explained 344 - What do Vision Transformers Learn]] | This study addresses the obstacles to performing visualizations in ViTs and analyzes the mechanism of various ViT variants, including DeiT, CoaT, ConViT, PiT, Swin, and Twin, to... | #summary #topic |
| [[Papers Explained 345 - ConvNets Match Vision Transformers at Scale]] | To address this gap, the study evaluates NFNet models, a pure convolutional architecture, by pre-training on a dataset and observing a scaling law between validation loss and... | #summary #topic |
| [[Papers Explained 346 - SmolVLM]] | SmolVLM is a family of small, efficient multimodal models designed for resource-constrained devices, achieving high performance despite limited size. SmolVLM excels in both image... | #summary #topic |
| [[Papers Explained 347 - Command A]] | Command A is an agent-optimized and multilingual-capable model, with support for 23 languages of global business: English, French, Spanish, Italian, German, Portuguese, Japanese... | #summary #topic |
| [[Papers Explained 348 - ReaderLM-v2]] | A 1.5B language model specialized for efficient web content extraction, transforming HTML into clean Markdown or JSON formats, It utilizes a novel three-stage data synthesis... | #summary #topic |
| [[Papers Explained 349 - ReSearch]] | In original GRPO, the loss is calculated by all the generated tokens in the whole rollout. In ReSearch, the rollout contains retrieval results, which are not generated by the... | #summary #topic |
| [[Papers Explained 35 - XLNet]] | XLNet proposes a new method for pretraining language models that combines ideas from AR and AE objectives while avoiding their limitations and can improve their performance on a... | #summary #topic |
| [[Papers Explained 350 - GPT 4.5]] | OpenAI GPT-4.5 is the largest and most knowledgeable model yet. Building on GPT-4o, GPT-4.5 scales pre-training further and is designed to be more general-purpose than powerful... | #summary #topic |
| [[Papers Explained 351 - MathFusion]] | MathFusion is a novel framework that enhances mathematical reasoning through cross-problem instruction synthesis. MathFusion implements this through three fusion strategies: | #summary #topic |
| [[Papers Explained 352 - Skywork-Math]] | This research investigates the underlying factors that potentially enhance the mathematical reasoning capabilities of large language models (LLMs). The data scaling law for math... | #summary #topic |
| [[Papers Explained 353 - s1]] | This work curates a small dataset s1K of 1,000 questions paired with reasoning traces relying on three criteria validated through ablations: difficulty, diversity, and quality. | #summary #topic |
| [[Papers Explained 354 - Does RL Incentivize Reasoning Capacity in LLMs Beyond the Base Model]] | It is widely believed that RLVR enables LLMs to continuously self-improve, thus acquiring novel reasoning abilities that exceed corresponding base models’ capacity. | #summary #topic |
| [[Papers Explained 355 - OpenMath Nemotron]] | This paper presents a winning submission to the AI Mathematical Olympiad — Progress Prize 2 (AIMO-2) competition. | #summary #topic |
| [[Papers Explained 356 - CLIMB]] | Despite the success of pre-training, optimizing data mixtures for both general and domain-specific tasks remains a challenge: | #summary #topic |
| [[Papers Explained 357 - Long-To-Short LLM Reasoning With Model Merging]] | This work presents a comprehensive empirical study on model merging for L2S reasoning, exploring diverse methodologies, including task-vector-based, SVD-based, and... | #summary #topic |
| [[Papers Explained 358 - Phi-4-Reasoning]] | Phi-4-reasoning is a 14-billion parameter reasoning model that achieves strong performance on complex reasoning tasks. It is trained via supervised fine-tuning of Phi-4 on a... | #summary #topic |
| [[Papers Explained 359 - Phi-4-Mini-Reasoning]] | This paper presents a systematic training recipe for SLMs that consists of four steps: | #summary #topic |
| [[Papers Explained 36 - MobileBERT]] | MobileBERT is as deep as BERTLARGE, but each building block is made much smaller, the hidden dimension of each building block is only 128. On the other hand, we introduce two... | #summary #topic |
| [[Papers Explained 360 - Nemotron CrossThink]] | Nemotron-Crossthink is a framework that systematically incorporates multi-domain corpora, including both synthetic and real-world question-answer pairs, into RL training to... | #summary #topic |
| [[Papers Explained 361 - OpenCodeReasoning]] | OpenCodeReasoning is a publicly available synthetic dataset for code reasoning, comprising 736,712 Python code solutions with accompanying reasoning traces, spanning 28,904 unique... | #summary #topic |
| [[Papers Explained 362 - Llama-Nemotron]] | Llama-Nemotron is an open family of heterogeneous reasoning models available in Nano (8B), Super (49B), and Ultra (253B) sizes, designed for exceptional reasoning capabilities and... | #summary #topic |
| [[Papers Explained 363 - UltraLong]] | This work introduces an efficient training recipe for building ultra-long context LLMs from aligned instruct models, pushing the boundaries of context lengths from 128K to 1M, 2M... | #summary #topic |
| [[Papers Explained 364 - OmniMath]] | OmniMath is a comprehensive and challenging benchmark specifically designed to assess LLMs’ mathematical reasoning at the Olympiad level. Unlike existing Olympiad-related... | #summary #topic |
| [[Papers Explained 365 - DeepMath]] | DeepMath-103K is a new dataset designed for advancing mathematical reasoning research. It comprises 103,000 mathematical problems with a focus on higher difficulty levels (3–10)... | #summary #topic |
| [[Papers Explained 366 - Math Shepherd]] | Given a problem p in the testing set, N candidate solutions are sampled from a generator. These candidates are then scored using a reward model, and the highest-scoring solution... | #summary #topic |
| [[Papers Explained 367 - Gemini Models]] | Gemini 2.0 Flash is a new, more powerful large language model (LLM) building upon the success of its predecessor, Gemini 1.5 Flash. It boasts enhanced performance, faster response... | #summary #topic |
| [[Papers Explained 368 - ThinkPRM]] | ThinkPRM, a long CoT verifier fine-tuned on orders of magnitude fewer process labels than those required by discriminative PRMs. | #summary #topic |
| [[Papers Explained 369 - RM-R1]] | Starting from any off-the-shelf instruction-tuned model (e.g., Qwen-2.5–14b-instruct), high-quality reasoning traces are synthesized and RM-R1 is distilled on the synthesized... | #summary #topic |
| [[Papers Explained 37 - FastBERT]] | FastBERT is a novel speed-tunable language transformer with adaptive inference time. | #summary #topic |
| [[Papers Explained 370 - Test Time Reinforcement Learning (TTRL)]] | Test-Time Reinforcement Learning (TTRL) is a method for training LLMs using RL on unlabeled data. TTRL enables self-evolution of LLMs by utilizing the priors in the pre-trained... | #summary #topic |
| [[Papers Explained 371 - ReasonIR]] | The project is available at [GitHub](https://github.com/facebookresearch/ReasonIR/). | #summary #topic |
| [[Papers Explained 372 - QALIGN]] | QLAIGN is a test-time alignment method that uses Markov Chain Monte Carlo (MCMC) sampling to generate a sequence of increasingly aligned text samples, guided by a reward model. It... | #summary #topic |
| [[Papers Explained 373 - One-Shot RLVR]] | Experiments are run on Qwen2.5-Math-1.5B, Qwen2.5-Math-7B, Llama-3.2–3B-Instruct, and DeepSeek-R1-Distill-Qwen-1.5B. | #summary #topic |
| [[Papers Explained 374 - Sarvam-M]] | Sarvam-M (M stands for Mistral) is a finetuned Mistral Small 24B. It significantly improves on the base model with large relative increases: +20% average improvement on Indian... | #summary #topic |
| [[Papers Explained 375 - Absolute Zero]] | The Absolute Zero paradigm is a novel approach to training models that eliminates the need for human-curated data. It relies on self-play and experience, aided by an environment... | #summary #topic |
| [[Papers Explained 376 - REFINE-AF]] | This paper explores the use of open-source small LLMs (LLaMA 2–7B, LLaMA 2–13B, and Mistral 7B) within a semi-automated framework to generate instruction datasets for fine-tuning... | #summary #topic |
| [[Papers Explained 378 - Eagle 2]] | Eagle 2 is a family of performant vision-language models. It addresses VLM post-training from a data-centric perspective, detailing the process of building a post-training data... | #summary #topic |
| [[Papers Explained 379 - Eagle 2.5]] | Following the architecture of LLaVA, an MLP projection layer is employed to align vision embeddings from SigLIP with the LLM representation space. The Qwen2.5 series models are... | #summary #topic |
| [[Papers Explained 38 - Longformer]] | The original Transformer model has a self-attention component with O(n²) time and memory complexity where n is the input sequence length. To address this challenge, we sparsify... | #summary #topic |
| [[Papers Explained 380 - Self-Evolved Preference Optimization (SPHERE)]] | The first stage of SPHERE constructs structured reasoning trajectories by using a base SLM to explore diverse problem-solving paths. Given a policy π and a dataset D with... | #summary #topic |
| [[Papers Explained 381 - AceReason-Nemotron]] | The models are available at [HuggingFace](https://huggingface.co/nvidia/AceReason-Nemotron-14B/). | #summary #topic |
| [[Papers Explained 381 - KL Divergence VS MSE for Knowledge Distillation]] | Typically, KD uses the Kullback-Leibler (KL) divergence loss between the softened probability distributions of the teacher and student models, with the temperature scaling... | #summary #topic |
| [[Papers Explained 383 - Perception Encoder]] | There are two objectives: first, to enhance the scalability and data efficiency of contrastive training; and second, to create a unified model effective on both image and video. | #summary #topic |
| [[Papers Explained 384 - PerceptionLM]] | Perception Language Model (PLM) is an open and reproducible framework for transparent research in image and video understanding, addressing the limitations of closed-source... | #summary #topic |
| [[Papers Explained 385 - J1]] | J1 is a reinforcement learning approach for training LLM-as-a-Judge models that converts both verifiable and non-verifiable prompts into judgment tasks with verifiable rewards to... | #summary #topic |
| [[Papers Explained 386 - ProRL]] | This work challenges the idea that RL only amplifies existing outputs and demonstrates that prolonged RL training (ProRL) can uncover novel reasoning strategies not accessible to... | #summary #topic |
| [[Papers Explained 387 - Sarvam-Translate]] | Sarvam-Translate is trained by fine-tuning Gemma3–4B-IT. It supports 22 Indian languages — Hindi, Bengali, Marathi, Telugu, Tamil, Gujarati, Urdu, Kannada, Odia, Malayalam... | #summary #topic |
| [[Papers Explained 388 - Magistral]] | Magistral is Mistral AI’s first reasoning model, designed for domain-specific, transparent, and multilingual reasoning. It comes in two versions: | #summary #topic |
| [[Papers Explained 389 - short-m@k]] | Llama-3.3-Nemotron-Super-49B-v1: a reasoning RL-enhanced version of Llama-3.3–70B | #summary #topic |
| [[Papers Explained 39 - DeiT]] | DeiT is a competitive convolution-free transformer trained on Imagenet only. It introduces a teacher-student strategy specific to transformers. It relies on a distillation token... | #summary #topic |
| [[Papers Explained 390 - Perplexity-based Importance Refinement (PIR)]] | PIR (Perplexity-based Importance Refinement) is a framework that quantitatively evaluates the importance of each reasoning step based on its impact on answer prediction confidence. | #summary #topic |
| [[Papers Explained 391 - Adaptive Reasoning Model]] | Adaptive Reasoning Model (ARM) is a reasoning model capable of adaptively selecting appropriate reasoning formats based on the task at hand. These formats include three efficient... | #summary #topic |
| [[Papers Explained 392 - Hard Negative Mining for Domain-Specific Retrieval]] | This paper addresses the challenge of retrieving accurate, domain-specific information in enterprise search systems, by dynamically selecting semantically challenging but... | #summary #topic |
| [[Papers Explained 393 - Gemini 2.5]] | The pre-training dataset is a large-scale, diverse collection of data encompassing a wide range of domains and modalities, which includes publicly available web-documents, code... | #summary #topic |
| [[Papers Explained 394 - OpenThoughts]] | The first step in the data generation pipeline is finding questions for each data domain. Question sourcing techniques can be broadly categorized into three types: | #summary #topic |
| [[Papers Explained 395 - AceReason-Nemotron 1.1]] | AceReason-Nemotron-1.1 7B is a reasoning model developed by leveraging the synergy between supervised fine-tuning (SFT) and reinforcement learning (RL). | #summary #topic |
| [[Papers Explained 396 - rStar-Coder]] | rStar-Coder significantly improves LLM code reasoning capabilities by constructing a large-scale, verified dataset of 418K competition-level code problems, 580K long-reasoning... | #summary #topic |
| [[Papers Explained 397 - SweEval]] | SweEval is a benchmark simulating real-world scenarios with variations in tone (positive or negative) and context (formal or informal). The prompts explicitly instruct the model... | #summary #topic |
| [[Papers Explained 398 - Evaluation is all you need]] | This study reveals that the benchmark evaluation results of reasoning models are subject to significant fluctuations caused by various factors. Subtle differences in evaluation... | #summary #topic |
| [[Papers Explained 399 - RewardAnything]] | The standard practice of collecting task-specific preference data and retraining reward models is resource-intensive, often producing biased rewards, and limits practical... | #summary #topic |
| [[Papers Explained 40 - MobileViT]] | MobileViT is a light-weight and general-purpose vision transformer for mobile devices. MobileViT presents a different perspective for the global processing of information with... | #summary #topic |
| [[Papers Explained 400 - Reward Reasoning Model]] | Reward Reasoning Models (RRMs) are specifically designed to execute a deliberate reasoning process before generating final rewards. Through chain-of-thought reasoning, RRMs... | #summary #topic |
| [[Papers Explained 401 - Prometheus-Vision]] | Inspired by the approach of evaluating LMs with LMs, this work proposes to evaluate VLMs with VLMs. For this purpose, a new feedback dataset called the Perception Collection is... | #summary #topic |
| [[Papers Explained 402 - MVTamperBench]] | MVTamperBench is a benchmark that systematically evaluates MLLM robustness against five prevalent tampering techniques: rotation, masking, substitution, repetition, and dropping... | #summary #topic |
| [[Papers Explained 403 - Crosslingual Reasoning through Test-Time Scaling]] | This work investigates how much test-time compute can improve multilingual reasoning abilities of English-centric RLMs. Research questions include: | #summary #topic |
| [[Papers Explained 404 - Pangea]] | Pangea is a multilingual multimodal LLM trained on PangeaIns, a diverse 6M instruction dataset spanning 39 languages. PangeaIns features high-quality English instructions... | #summary #topic |
| [[Papers Explained 405 - Universal Tokenizer]] | The experiments include 62 typologically and lexicographically diverse languages, broken up into three geographically motivated clusters: | #summary #topic |
| [[Papers Explained 406 - Answer Matching]] | This paper argues that multiple-choice benchmarks, traditionally used for evaluating language models, suffer from a critical flaw: they allow models to exploit discriminative... | #summary #topic |
| [[Papers Explained 407 - Should We Still Pretrain Encoders with Masked Language Modeling]] | While encoder pretraining has traditionally relied on Masked Language Modeling (MLM), recent evidence suggests that decoder models pretrained with Causal Language Modeling (CLM)... | #summary #topic |
| [[Papers Explained 408 - Encoder-Decoder Gemma]] | This paper studies a novel problem: adapting pre-trained decoder-only LLMs to encoder-decoder, with the goal of leveraging the strengths of both approaches to achieve a more... | #summary #topic |
| [[Papers Explained 409 - Jina Embeddings v4]] | Jina Embeddings v4 is a 3.8 billion parameter multimodal embedding model that unifies text and image representations through a novel architecture supporting both single-vector and... | #summary #topic |
| [[Papers Explained 41 - LAMBERT]] | We inject the layout information into the model in two ways. Firstly, we modify the input embeddings of the original RoBERTa model by adding the layout term. We also experiment... | #summary #topic |
| [[Papers Explained 410 - Big Math]] | Big-Math is a dataset of over 250,000 high-quality math questions with verifiable answers, purposefully made for reinforcement learning (RL). To create Big-Math, openly available... | #summary #topic |
| [[Papers Explained 411 - Constitutional AI]] | This study experiments with methods for training a harmless AI assistant through self-improvement, without any human labels identifying harmful outputs. The only human oversight... | #summary #topic |
| [[Papers Explained 412 - Claude Research]] | Claude Research is a multi-agent system that searches across the web, Google Workspace, and any integrations to accomplish complex tasks. The Research feature involves an agent... | #summary #topic |
| [[Papers Explained 413 - Reinforcement Learning with Reference Probability Reward (RLPR)]] | Reinforcement learning from verifiable reward (RLVR) is a general post-training paradigm in which a rule-based verifier assigns a scalar reward score to each generated response.... | #summary #topic |
| [[Papers Explained 414 - Out-of-distribution Math Problems Evaluation with 3 Generalization Axes…]] | OMEGA (Out-of-distribution Math Problems Evaluation with 3 Generalization Axes) is a controlled yet diverse benchmark designed to evaluate three axes of out-of-distribution... | #summary #topic |
| [[Papers Explained 415 - Gemini 2.5 Pro Capable of Winning Gold at IMO 2025]] | This paper presents a novel methodology based on pipeline design and prompt engineering with the Gemini 2.5 Pro model, solving 5 out of the 6 problems of IMO 2025. | #summary #topic |
| [[Papers Explained 416 - LongWriter-Zero]] | To train policies for ultra-long-form generation, the Group Relative Policy Optimization (GRPO) algorithm is adopted for RL training on the Qwen2.5–32B base model. Training... | #summary #topic |
| [[Papers Explained 417 - Kimi-Researcher]] | Kimi-Researcher is an autonomous agent that excels at multi-turn search and reasoning. It performs an average of 23 reasoning steps and explores over 200 URLs per task. Built on... | #summary #topic |
| [[Papers Explained 418 - TabArena]] | TabArena is the first continuously maintained living tabular benchmarking system. A representative collection of datasets and well-implemented models are manually curated, a... | #summary #topic |
| [[Papers Explained 419 - The Ladder of Reasoning]] | This paper conducts a detailed analysis of model performance on the AIME24 dataset to understand how reasoning capabilities evolve. A ladder-like structure in problem difficulty... | #summary #topic |
| [[Papers Explained 42 - UDOP]] | Universal Document Processing (UDOP) is a foundation Document AI model which unifies text, image, and layout modalities together with varied task formats, including document... | #summary #topic |
| [[Papers Explained 420 - Fast Math R1 14B]] | This model ranked 4th on the public leaderboard and 8th on the private leaderboard of the second edition of AI Mathematical Olympiad (AIMO). It utilizes a practical and effective... | #summary #topic |
| [[Papers Explained 421 - AdaptiVocab]] | AdaptiVocab is an end-to-end approach for vocabulary adaptation, designed to enhance LLM efficiency in low- resource domains. | #summary #topic |
| [[Papers Explained 422 - MDocAgent]] | MDocAgent (A Multi-Modal Multi-Agent Framework for Document Understanding) is a novel RAG and multi-agent framework that leverages both text and image. The system employs five... | #summary #topic |
| [[Papers Explained 423 - Reasoning or Memorization]] | This study centers on four representative checkpoints: Qwen2.5–7B, Qwen2.5–7B-Instruct, Qwen2.5-Math-7B, and Qwen2.5-Math-7B-Instruct. For a controlled comparison, Llama3.1–8B and... | #summary #topic |
| [[Papers Explained 424 - One Token to Fool LLM-as-a-Judge]] | Reinforcement Learning with Verifiable Rewards (RLVR) focuses on a reference-based setting, where the reward signal is provided by either a rule-based function or a generative... | #summary #topic |
| [[Papers Explained 425 - ReCode]] | LLMs struggle to adapt to frequent API updates due to reliance on outdated knowledge. ReCode (rule-based Reinforcement learning for Code Update) is a novel framework that mimics... | #summary #topic |
| [[Papers Explained 426 - Arcee Foundation Models]] | Arcee Foundation Models is a new family of generative AI models built from the ground up for enterprise reality. Combined with built-in support for function calling and agentic... | #summary #topic |
| [[Papers Explained 427 - Paper2Poster]] | Given a scientific paper composed of interleaved text, figures, and tables, the goal is to automatically generate a single-page academic poster that faithfully conveys the paper’s... | #summary #topic |
| [[Papers Explained 428 - gpt-oss]] | OpenAI’s open-weight language models, including gpt-oss-120b and gpt-oss-20b are designed for reasoning, agentic tasks. They are trained on the harmony response format and offer... | #summary #topic |
| [[Papers Explained 429 - GPT-5]] | GPT‑5 shows particular improvements in complex front‑end generation and debugging larger repositories. | #summary #topic |
| [[Papers Explained 43 - GPT]] | GPT demonstrates that large gains on Natural language understanding tasks can be realized by generative pre-training of a language model on a diverse corpus of unlabeled text... | #summary #topic |
| [[Papers Explained 430 - Safe-Completions]] | Large Language Models used in ChatGPT have traditionally been trained to learn a refusal boundary: depending on the user’s intent, the model is taught to either fully comply or... | #summary #topic |
| [[Papers Explained 431 - Anatomy of a Machine Learning Ecosystem]] | This work analyzes 1.86 million models on Hugging Face. The study of model family trees — networks that connect fine-tuned models to their base or parent — reveals sprawling... | #summary #topic |
| [[Papers Explained 433 - Aryabhata 1.0]] | Aryabhata 1.0 is a 7B parameter math reasoning model optimized for the Indian Joint Entrance Examination (JEE). It achieves an accuracy of 86.0% on the January session and 90.2%... | #summary #topic |
| [[Papers Explained 434 - Voxtral]] | Voxtral Mini and Voxtral Small are multimodal audio chat models trained to comprehend both spoken audio and text documents. These models were pretrained on a large-scale corpus of... | #summary #topic |
| [[Papers Explained 435 - MegaScience]] | The open-source community has primarily focused on mathematics and coding while neglecting the scientific domain, largely due to the absence of open, large-scale, high-quality... | #summary #topic |
| [[Papers Explained 436 - CoT-Self-Instruct]] | CoT-Self-Instruct is a synthetic data generation method that instructs LLMs to first reason and plan via Chain-of-Thought (CoT) based on the given seed tasks, and then to generate... | #summary #topic |
| [[Papers Explained 437 - Vision-Guided Chunking]] | Traditional document chunking methods, such as fixed-size or sliding-window approaches, suffer from several fundamental limitations: | #summary #topic |
| [[Papers Explained 438 - MiroMind-M1]] | The project is available on [GitHub](https://github.com/MiroMindAsia/MiroMind-M1). | #summary #topic |
| [[Papers Explained 439 - Reinforcement Learning with Calibration Rewards (RLCR)]] | RLCR (Reinforcement Learning with Calibration Rewards) is an approach to training reasoning models that jointly improves accuracy and calibrated confidence estimation. During... | #summary #topic |
| [[Papers Explained 44 - T5]] | T5 explores the landscape of transfer learning techniques for NLP by introducing a unified framework that converts all text-based language problems into a text-to-text format. | #summary #topic |
| [[Papers Explained 440 - OpenCodeReasoning-II]] | The dataset is available on [HuggingFace](https://huggingface.co/datasets/nvidia/OpenCodeReasoning-2/). | #summary #topic |
| [[Papers Explained 441 - Multi-Domain Reasoning via Reinforcement Learning]] | This study investigates multi-domain reasoning within the RLVR framework, addressing the gap in understanding the interplay among different reasoning skills under reinforcement... | #summary #topic |
| [[Papers Explained 442 - Examining Citation Relationships using LLMs]] | This paper addresses the challenge of ensuring the trustworthiness and interpretability of LLMs when applied to document-based tasks such as summarization, question answering, and... | #summary #topic |
| [[Papers Explained 443 - Hermes 4]] | Hermes 4 is a family of hybrid reasoning models that combine structured, multi-step reasoning with broad instruction-following ability. This paper describes the challenges... | #summary #topic |
| [[Papers Explained 444 - POLARIS]] | POLARIS is a post-training recipe focused on calibrated data difficulty, enhanced data diversity, inference-time length scaling, and efficient training, designed to scale... | #summary #topic |
| [[Papers Explained 445 - Context Rot]] | LLMs are typically presumed to process context uniformly. However, in practice, this assumption does not hold. Model performance varies significantly as input length changes, even... | #summary #topic |
| [[Papers Explained 446 - Unary Feedback as Observation]] | For off-the-shelf LLMs, models fine-tuned with various RL algorithms including PPO, GRPO, DAPO, and Dr. GRPO are selected. | #summary #topic |
| [[Papers Explained 447 - ULMFiT]] | Universal Language Model Fine-tuning (ULMFiT) is an effective transfer learning method that can be applied to any task in NLP. The paper further introduces techniques that are key... | #summary #topic |
| [[Papers Explained 448 - Sparsely-Gated Mixture-of-Experts Layer]] | Computation is saved based on the sparsity of the output of G(x). Wherever G(x)i = 0, Ei(x) need not be computed. If the number of experts is very large, the branching factor can... | #summary #topic |
| [[Papers Explained 449 - Switch Transformers]] | The core idea behind Switch Transformers is to maximize the number of parameters while keeping the FLOPs per example constant. To achieve this, Switch Transformers employ a... | #summary #topic |
| [[Papers Explained 45 - Codex]] | Codex is a GPT language model finetuned on publicly available code from GitHub. A distinct production version of Codex powers GitHub Copilot. | #summary #topic |
| [[Papers Explained 450 - GLaM]] | GLaM (Generalist Language Model) is a family of language models that utilizes a sparsely activated mixture-of-experts architecture to scale model capacity while reducing training... | #summary #topic |
| [[Papers Explained 451 - Kimi K2]] | The base and instruct models are available at [HuggingFace](https://huggingface.co/collections/moonshotai/kimi-k2-6871243b990f2af5ba60617d). | #summary #topic |
| [[Papers Explained 452 - Apriel-Nemotron-15B-Thinker]] | Apriel-Nemotron-15B-Thinker is a 15B parameter model in the ServiceNow Apriel SLM series. It is trained in a four stage training pipeline including | #summary #topic |
| [[Papers Explained 453 - Nemotron-H]] | To ensure that technical pages in Common Crawl retain their mathematical content, the recipe and code base from OpenWebMath are leveraged. It is also found essential to apply this... | #summary #topic |
| [[Papers Explained 454 - Nemotron Nano 2]] | Nemotron-Nano-9B-v2 is a hybrid Mamba-Transformer language model designed to increase throughput for reasoning workloads while achieving state-of-the-art accuracy compared to... | #summary #topic |
| [[Papers Explained 455 - Shepherd]] | Shepherd is a language model specifically tuned to critique model responses and suggest refinements. At the core of the approach is a high quality feedback dataset, which is... | #summary #topic |
| [[Papers Explained 456 - Deep Think with Confidence (DeepConf)]] | Deep Think with Confidence (DeepConf) is a simple yet powerful method that enhances both reasoning efficiency and performance at test time. DeepConf leverages model-internal... | #summary #topic |
| [[Papers Explained 457 - Hallucination Tax of Reinforcement Finetuning]] | To teach models to reason about their uncertainty and knowledge boundary by leveraging inference-time compute. | #summary #topic |
| [[Papers Explained 458 - Kimi-VL]] | The architecture of Kimi-VL consists of three parts: a native-resolution vision encoder (MoonViT), an MLP projector, and an MoE language model. | #summary #topic |
| [[Papers Explained 459 - FineWeb2]] | FineWeb2 is a new 20TB (5B document) multilingual dataset covering over 1000 languages. It was created using a new pre-training dataset curation pipeline based on FineWeb that can... | #summary #topic |
| [[Papers Explained 46 - FLAN]] | This paper explores a simple method for improving the zero-shot learning abilities of language models, and shows that instruction tuning (finetuning language models on a... | #summary #topic |
| [[Papers Explained 460 - rStar2-Agent]] | rStar2-Agent is a 14B math reasoning model trained with agentic reinforcement learning to achieve frontier-level performance. | #summary #topic |
| [[Papers Explained 461 - LLM-JEPA]] | LLM pretraining, finetuning, and evaluation rely on input-space reconstruction and generative capabilities. Yet, it has been observed in vision that embedding-space training... | #summary #topic |
| [[Papers Explained 462 - Smol2Operator]] | Graphical User Interface (GUI) automation is one of the most challenging frontiers in computer vision. Developing models that see and interact with user interfaces enables AI... | #summary #topic |
| [[Papers Explained 463 - FineVision]] | FineVision is a new multimodal dataset with 24 million samples. It is created by collecting over 200 datasets containing 17M images, 89M question-answer turns, and 10B answer... | #summary #topic |
| [[Papers Explained 464 - AggLM]] | This work proposes to learn aggregation as an explicit reasoning skill. Given a set of candidate solutions, an aggregator model called AggLM is trained to review, reconcile, and... | #summary #topic |
| [[Papers Explained 465 - EmbeddingGemma]] | EmbeddingGemma is an encoder-only transformer model adapted from a pretrained 300M decoder-only Gemma 3 model. The Gemma 3 model is adapted into an encoder-decoder model following... | #summary #topic |
| [[Papers Explained 466 - Jina Code Embeddings]] | jina-code-embeddings is a novel code embedding model suite designed to retrieve code from natural language queries, perform technical question-answering, and identify semantically... | #summary #topic |
| [[Papers Explained 467 - Mix Data or Merge Models]] | Extensive experiments are conducted with diverse data mixtures to create a pool of model candidates. From this pool, the best-performing checkpoints are merged using four... | #summary #topic |
| [[Papers Explained 468 - NaturalThoughts]] | This study examines different data selection strategies along two axes: diversity and difficulty. | #summary #topic |
| [[Papers Explained 469 - MobileLLM-R1]] | While the first assumption has already been challenged by recent sub-billion-parameter reasoning models such as Qwen3–0.6B and DeepSeek distilled variants, the second remains... | #summary #topic |
| [[Papers Explained 47 - Gopher]] | This paper presents an analysis of Transformer-based language model performance across a wide range of model scales — from models with tens of millions of parameters up to a 280... | #summary #topic |
| [[Papers Explained 470 - VaultGemma]] | VaultGemma 1B is a 1 billion parameter model within the Gemma family, fully trained with differential privacy (DP) on the same data mixture used for the Gemma 2 series. VaultGemma... | #summary #topic |
| [[Papers Explained 471 - mmBERT]] | mmBERT is an encoder-only language model pretrained on 3T tokens of multilingual text in over 1800 languages using an architecture inspired from ModernBERT. To build mmBERT... | #summary #topic |
| [[Papers Explained 473 - Fathom-DeepResearch]] | The first is Fathom-Search-4B, a DeepSearch model trained from Qwen3–4B and optimized for evidence-based investigation through live web search and targeted webpage querying. Its... | #summary #topic |
| [[Papers Explained 473 - FusioN]] | Generating high-quality text with modern LLMs has traditionally focused on selecting the best output from a set of diverse candidates (Best-of-N). This approach discards valuable... | #summary #topic |
| [[Papers Explained 474 - Jina Reranker v3]] | jina-reranker-v3 is a 0.6B parameter multilingual document reranker that introduces a novel last but not late interaction. | #summary #topic |
| [[Papers Explained 475 - ModernVBERT]] | A central aspect of the study is the impact of causal and bidirectional attention masks, extending previous work on textual representations to the vision modality. | #summary #topic |
| [[Papers Explained 476 - Klear-Reasoner]] | Klear-Reasoner is a reasoning model with long reasoning capabilities that achieves high performance across multiple benchmarks. | #summary #topic |
| [[Papers Explained 477 - General-Reasoner]] | Current works for LLM reasoning mainly focus on mathematical and coding domains, largely due to data abundance and the ease of answer verification. This limits the applicability... | #summary #topic |
| [[Papers Explained 478 - Apriel-1.5–15B-Thinker]] | Apriel-1.5–15B-Thinker is a 15-billion parameter open-weights multi-modal reasoning model. Starting from Pixtral-12B, a progressive three-stage methodology is applied: | #summary #topic |
| [[Papers Explained 479 - olmOCR]] | The data and models are available at [HuggingFace](https://huggingface.co/collections/allenai/olmocr). | #summary #topic |
| [[Papers Explained 48 - InstructGPT]] | We start with a pretrained language model, a distribution of prompts on which we want our model to produce aligned outputs and a team of trained human labelers. We then apply the... | #summary #topic |
| [[Papers Explained 480 - olmOCR 2]] | olmOCR 2 is a specialized, 7B vision language model (VLM) trained using reinforcement learning with verifiable rewards (RLVR), where the rewards are a diverse set of binary unit... | #summary #topic |
| [[Papers Explained 481 - DeepSeek-OCR]] | DeepSeek-OCR is an initial investigation into the feasibility of compressing long contexts via optical 2D mapping. It consists of two components: DeepEncoder and... | #summary #topic |
| [[Papers Explained 482 - Agent Foundation Models (Chain-of-Agents)]] | The [models](https://huggingface.co/collections/PersonalAILab/afm-models-689200e11d0b21a67c015ba8) and... | #summary #topic |
| [[Papers Explained 483 - PANNs]] | In computer vision and natural language processing, systems pretrained on large-scale datasets have generalized well to several tasks. However, there is limited research on... | #summary #topic |
| [[Papers Explained 484 - wav2vec]] | Wav2vec is an unsupervised pre-training method for speech recognition that learns representations of raw audio using a multi-layer convolutional neural network. | #summary #topic |
| [[Papers Explained 485 - wav2vec 2.0]] | This research shows for the first time that learning powerful representations from speech audio alone followed by fine-tuning on transcribed speech can outperform the best... | #summary #topic |
| [[Papers Explained 487 - CLAP]] | Contrastive Language-Audio Pretraining (CLAP) learns to connect language and audio by using two encoders and a contrastive learning to bring audio and text descriptions into a... | #summary #topic |
| [[Papers Explained 488 - Reasoning Vectors]] | The core idea involves comparing two models that share an identical architecture, initialization, and pre-training history, sourced from a public repository. | #summary #topic |
| [[Papers Explained 489 - LIMI]] | Agency is defined as the emergent capacity of AI systems to function as autonomous agents — actively discovering problems, formulating hypotheses, and executing solutions through... | #summary #topic |
| [[Papers Explained 489 - UserLM]] | To evaluate LM performance in realistic settings, prior work simulated users in multi-turn conversations, often prompting an LLM originally trained to be a helpful assistant to... | #summary #topic |
| [[Papers Explained 49 - Chinchilla]] | This paper investigated the optimal model size and number of tokens for training a transformer LLM within a given compute budget and discovered that current LLMs are not... | #summary #topic |
| [[Papers Explained 490 - A single character can make or break your LLM evals]] | A diverse set of instruction-tuned open-source language models from the Llama, Gemma, and Qwen families is chosen. Specifically, two model sizes are considered, approximately 8B... | #summary #topic |
| [[Papers Explained 492 - AutoL2S]] | AutoL2S aims to distill reasoning capabilities from reasoning-capable LLMs, enabling the model to learn effective reasoning patterns while reducing the length of reasoning paths... | #summary #topic |
| [[Papers Explained 493 - gpt oss safeguard]] | gpt-oss-safeguard-120b and gpt-oss-safeguard-20b are two open-weight reasoning models post-trained from the gpt-oss models. These models are trained to reason from a provided... | #summary #topic |
| [[Papers Explained 494 - Model Interpolation for Efficient Reasoning]] | This paper observes that model interpolation follows a three-stage evolutionary paradigm with distinct behaviors on the reasoning trajectory. These dynamics provide a principled... | #summary #topic |
| [[Papers Explained 495 - What Characterizes Effective Reasoning]] | This study investigates the characteristics of effective chain-of-thought (CoT) reasoning in large reasoning models. It challenges the notion that longer CoTs and increased review... | #summary #topic |
| [[Papers Explained 496 - Treasure Hunt]] | Large general-purpose models are trained for many tasks, but work best on high-frequency use cases. After training, it is hard to adapt a model to perform well on specific use... | #summary #topic |
| [[Papers Explained 497 - AI-Augmented Textbook (Learn Your Way)]] | Textbooks are a cornerstone of education, but they have a fundamental limitation: they are a one-size-fits-all medium. This work presents an approach for transforming and... | #summary #topic |
| [[Papers Explained 498 - Command A Translate]] | Command A Translate is a machine translation model built off Cohere’s Command A trained via direct preference optimization. The model is extended and participates at WMT with a... | #summary #topic |
| [[Papers Explained 499 - Souper Model (Soup Of Category Experts)]] | Soup Of Category Experts (SoCE) is a principled approach for model souping that utilizes benchmark composition to identify optimal model candidates and applies non-uniform... | #summary #topic |
| [[Papers Explained 50 - PaLM]] | Pathways Language Model (PaLM) is a 540-billion parameter, densely activated, Transformer language model. It is trained on 6144 TPU v4 chips using Pathways, a new ML system that... | #summary #topic |
| [[Papers Explained 500 - P1]] | P1 is a family of open-source physics reasoning models developed to advance physics research by creating LLMs with exceptional physics reasoning capabilities, particularly in... | #summary #topic |
| [[Papers Explained 501 - Reasoning Gym]] | Reasoning Gym (RG) is a library of reasoning environments for reinforcement learning with verifiable rewards. It provides over 100 data generators and verifiers spanning multiple... | #summary #topic |
| [[Papers Explained 504 - Who Reasons in LLMs]] | This work introduces Stethoscope for Networks (SfN), a suite of diagnostic tools designed to probe and analyze the internal behaviors of LLMs. Using SfN, both circumstantial and... | #summary #topic |
| [[Papers Explained 505 - Rnj-1]] | Rnj-1, named in homage to Ramanujan and pronounced “range-1,” is a pair of base and instruction-tuned large language models developed by Essential. These models are part of the... | #summary #topic |
| [[Papers Explained 506 - Nemotron 3 Nano]] | Nemotron 3 Nano 30B-A3B is a Mixture-of-Experts hybrid Mamba-Transformer language model, pretrained on 25 trillion text tokens, including more than 3 trillion new unique tokens... | #summary #topic |
| [[Papers Explained 507 - T5Gemma 2]] | T5Gemma 2 basic building block follows Gemma 3: grouped-query attention with QK-norm, pre- and post-norm with RMSNorm, RoPE for positional encoding, and interleaved local and... | #summary #topic |
| [[Papers Explained 508 - On the Interplay of Pre-Training, Mid-Training, and RL on Reasoning Language…]] | This work develops a fully controlled experimental framework that isolates the causal contributions of pre-training, mid-training, and RL-based post-training. The approach employs... | #summary #topic |
| [[Papers Explained 509 - FACTS Leaderboard]] | The FACTS Leaderboard is an online leaderboard suite and associated set of benchmarks that comprehensively evaluates the ability of language models to generate factually accurate... | #summary #topic |
| [[Papers Explained 51 - OPT]] | Open Pre-trained Transformers (OPT) comprise a suite of decoder-only pre-trained transformers with parameter ranges from 125M to 175B, intended to be fully and responsibly shared... | #summary #topic |
| [[Papers Explained 510 - OEIS Sequence Benchmark]] | The project is available at [GitHub](https://github.com/ceodspspectrum/oeis-sequence-benchmark/). | #summary #topic |
| [[Papers Explained 511 - HelpSteer]] | HelpSteer is a multi-attribute help-fulness dataset annotated for the various aspects that make responses helpful like correctness, coherence, complexity, and verbosity in... | #summary #topic |
| [[Papers Explained 512 - HelpSteer2]] | HelpSteer2 is an open-source helpfulness preference dataset of about 10k response pairs, designed for training reward models that align LLMs with human preferences, despite being... | #summary #topic |
| [[Papers Explained 513 - Help Steer 2 Preference]] | For each task, annotators are provided a prompt and two responses. They first annotate each response on a Likert-5 scale along several dimensions (helpfulness, correctness and... | #summary #topic |
| [[Papers Explained 514 - HelpSteer 3]] | Prompts are drawn from ShareGPT for Coding and Multilingual prompts (as in HelpSteer2) and WildChat for General and STEM prompts (approx. 1M prompts), chosen to reduce overlap... | #summary #topic |
| [[Papers Explained 515 - Help Steer 3 Preference]] | HelpSteer3-Preference is a high-quality, human-annotated preference dataset comprising of over 40,000 samples spanning diverse tasks relating to STEM, coding and multilingual... | #summary #topic |
| [[Papers Explained 516 - SteerLM]] | SteerLM is a supervised fine-tuning method that empowers end-users to control responses during inference. It conditions responses to conform to an explicitly defined... | #summary #topic |
| [[Papers Explained 517 - Nemotron-Math]] | Nemotron-Math is a large-scale mathematical reasoning dataset containing 7.5M solution traces across high, medium, and low reasoning modes. Each mode is available both with and... | #summary #topic |
| [[Papers Explained 518 - Nemotron Cascade]] | This work proposes cascaded domain-wise reinforcement learning (Cascade RL) to develop general-purpose reasoning models, Nemotron-Cascade, capable of operating in both instruct... | #summary #topic |
| [[Papers Explained 519 - Nemotron-Parse 1.1]] | The vision encoder, denoted as ℰ, is initialized from RADIO which follows a ViT-H/16 architecture (657M parameters), and maps an image I ∈R3×𝐻×𝑊 to a latent representation Z ∈R𝑁... | #summary #topic |
| [[Papers Explained 52 - BLOOM]] | BLOOM is a 176B-parameter open-access decoder-only transformer model, collaboratively developed by hundreds of researchers, aiming to democratize advanced LLM technology. | #summary #topic |
| [[Papers Explained 520 - Nemotron 3]] | The Nemotron 3 family of models utilize a hybrid Mamba-Transformer MoE architecture. | #summary #topic |
| [[Papers Explained 521 - Nemotron Nano V2 VL]] | Nemotron Nano V2 VL builds on Nemotron Nano V2, a hybrid Mamba-Transformer LLM and is designed for strong real-world document understanding, long video comprehension, and... | #summary #topic |
| [[Papers Explained 522 - ToolOrchestra]] | ToolOrchestra is a method for training small orchestrators that coordinate intelligent tools. It explicitly uses reinforcement learning with outcome-, efficiency-, and... | #summary #topic |
| [[Papers Explained 523 - Meta CLIP]] | This work intends to reveal CLIP’s data curation approach and, in pursuit of making it open to the community, introduce Metadata-Curated Language-Image Pre-training (MetaCLIP).... | #summary #topic |
| [[Papers Explained 524 - Meta CLIP 2]] | Although CLIP is successfully trained on billion-scale image-text pairs from the English world, scaling CLIP’s training further to learning from the worldwide web data is still... | #summary #topic |
| [[Papers Explained 525 - NaturalReasoning]] | NaturalReasoning is a comprehensive dataset of 2.8 million diverse, challenging reasoning questions with reference answers, backtranslated from pretraining corpora across domains... | #summary #topic |
| [[Papers Explained 526 - Ministral 3]] | The models are available at [HuggingFace](https://huggingface.co/collections/mistralai/ministral-3). | #summary #topic |
| [[Papers Explained 527 - TranslateGemma]] | The models are available on [HuggingFace](https://huggingface.co/collections/google/translategemma). | #summary #topic |
| [[Papers Explained 528 - FlexOlmo]] | FlexOlmo is a new class of language models that employs a mixture-of-experts (MoE) architecture where each expert is trained independently on closed datasets and later integrated... | #summary #topic |
| [[Papers Explained 529 - DR Tulu]] | The datasets and models are available at [HuggingFace](https://huggingface.co/collections/rl-research/dr-tulu). | #summary #topic |
| [[Papers Explained 53 - Galactica]] | Galactica is an LLM specializing in scientific knowledge, surpasses existing models on a variety of scientific tasks, excelling in technical knowledge probes like LaTeX equations... | #summary #topic |
| [[Papers Explained 530 - BroRL]] | Existing methods like ProRL plateau in performance after thousands of training steps, showing diminishing returns. BroRL (Broaden exploration) aims to overcome this by broadening... | #summary #topic |
| [[Papers Explained 531 - OctoThinker]] | This work investigates how mid-training strategies shape RL dynamics, focusing on two representative model families: Qwen and Llama. The study reveals that | #summary #topic |
| [[Papers Explained 532 - Jina-VLM]] | Jina-VLM is a 2.4B parameter vision-language model that achieves state-of-the-art multilingual visual question answering among open 2B-scale VLMs. The model couples a SigLIP2... | #summary #topic |
| [[Papers Explained 533 - OpenVision 3]] | OpenVision 3 is a family of advanced vision encoders that learn a single, unified visual representation that can serve both image understanding and image generation. | #summary #topic |
| [[Papers Explained 534 - PubMed-OCR]] | PubMed-OCR is an OCR-centric corpus of scientific articles derived from PubMed Central Open Access PDFs. Each page image is annotated with Google Cloud Vision and released in a... | #summary #topic |
| [[Papers Explained 535 - LongMagpie]] | LongMagpie is a self-synthesis framework that automatically generates large-scale long-context instruction data. The key insight is that aligned long-context LLMs, when presented... | #summary #topic |
| [[Papers Explained 536 - DeepSeek-OCR 2]] | DeepSeek-OCR 2 inherits the overall architecture of DeepSeek-OCR, which consists of an encoder and a decoder. The encoder discretizes images into visual tokens, while the decoder... | #summary #topic |
| [[Papers Explained 537 - ScaleRL]] | This research presents the first large-scale systematic study, amounting to more than 400,000 GPU-hours, that defines a principled framework for analyzing and predicting RL... | #summary #topic |
| [[Papers Explained 538 - Code World Model]] | Code World Model (CWM) is a 32-billion-parameter dense, decoder-only LLM trained with a context size of up to 131 k tokens. | #summary #topic |
| [[Papers Explained 539 - Golden Goose]] | Given a source text S, an LLM is prompted to identify a contiguous span t of important reasoning steps. This span t is used to construct a masked context Smask by replacing t in S... | #summary #topic |
| [[Papers Explained 54 - ChatGPT]] | ChatGPT is an interactive model designed to engage in conversations. Its conversational format allows ChatGPT to respond to subsequent queries, acknowledge errors, question... | #summary #topic |
| [[Papers Explained 540 - Bespoke MiniChart 7B]] | Bespoke-MiniChart-7B is a 7B open chart understanding model that sets a new state-of-the-art in chart question answering for models of its size and matches larger models like... | #summary #topic |
| [[Papers Explained 541 - Phi 4 Reasoning Vision 15B]] | Phi-4-reasoning-vision-15B is a compact open-weight multimodal reasoning model that balances reasoning power, efficiency, and training data needs. The model was trained with 200... | #summary #topic |
| [[Papers Explained 542 - Composition RL]] | Composition-RL is a simple yet useful approach for better utilizing limited verifiable prompts targeting pass-rate-1 prompts, by automatically composing multiple problems into a... | #summary #topic |
| [[Papers Explained 543 - Dr. SCI]] | Exploration-Expanding SFT, which broadens the model’s reasoning pattern coverage prior to RL | #summary #topic |
| [[Papers Explained 544 - GEPA]] | GEPA (Genetic-Pareto) is a prompt optimizer that thoroughly incorporates natural language reflection to learn high-level rules from trial and error. | #summary #topic |
| [[Papers Explained 545 - MiniCheck]] | MiniCheck is an efficient, small fact-checking system designed to verify sentences against grounding documents in tasks like retrieval-augmented generation, summarization, and... | #summary #topic |
| [[Papers Explained 546 - Tiny Aya]] | Tiny Aya is a family of efficient, open-weight multilingual language models centered on balanced performance across 70+ languages, especially underrepresented ones, using just... | #summary #topic |
| [[Papers Explained 547 - Terminal-Bench]] | Terminal-Bench 2.0 is a carefully curated hard benchmark composed of 89 tasks in computer terminal environments. These tasks are inspired by problems from real workflows. Each... | #summary #topic |
| [[Papers Explained 548 - CHIMERA]] | CHIMERA is a compact synthetic reasoning dataset comprising 9K samples designed to support generalizable reasoning across domains. It is constructed with three key properties: | #summary #topic |
| [[Papers Explained 549 - TinyLoRA]] | TinyLoRA is an extra low-rank variant of LoRA that scales adapter size down arbitrarily, even to a single trained parameter, enabling extremely parameter-efficient reinforcement... | #summary #topic |
| [[Papers Explained 55 - LLaMA]] | LLaMA is a collection of foundation language models ranging from 7B to 65B parameters, trained on trillions of tokens using publicly available datasets exclusively. | #summary #topic |
| [[Papers Explained 550 - PPLX Embedding]] | Two bidirectional diffusion language models are trained via continued pretraining of existing autoregressive decoder-only backbones. Considering the state-of-the-art performance... | #summary #topic |
| [[Papers Explained 551 - QED Nano]] | QED-Nano is a compact 4B model post-trained to write Olympiad-level mathematical proofs and operates entirely in natural language, with no reliance on Lean or external tools. The... | #summary #topic |
| [[Papers Explained 552 - Nemotron Cascade 2]] | Nemotron-Cascade 2 is an open 30B MoE model with 3B activated parameters that delivers mathematical and coding reasoning performance approaches that of frontier open models. | #summary #topic |
| [[Papers Explained 553 - Rubrics as Rewards]] | Explicit Aggregation involves computing the reward as follows: each criterion is independently evaluated using an LLM-as-judge, and the final normalized reward is computed as: | #summary #topic |
| [[Papers Explained 554 - Jina Embeddings v5 Text]] | The paper introduces jina-embeddings-v5-text, a family of compact text embedding models trained with a novel regimen that combines model distillation and task-specific contrastive... | #summary #topic |
| [[Papers Explained 555 - IH Challenge]] | The dataset is available at [HuggingFace](https://huggingface.co/datasets/openai/ih-challenge). | #summary #topic |
| [[Papers Explained 56 - Alpaca]] | Alpaca is fine-tuned from Meta’s LLaMA 7B model. The Alpaca model is trained on 52K instruction-following demonstrations generated in the style of self-instruct using... | #summary #topic |
| [[Papers Explained 57 - LIMA]] | Large language models are trained in two stages: (1) unsupervised pretraining from raw text, to learn general-purpose representations, and (2) large-scale instruction tuning and... | #summary #topic |
| [[Papers Explained 58 - PaLM 2]] | PaLM 2 is the successor of PaLM. It’s more compute efficient and is pre-trained on a more multilingual & during mixture of data spanning across hundreds of languages and domains.... | #summary #topic |
| [[Papers Explained 59 - Falcon]] | As larger models require pretraining on trillions of tokens, it is unclear how scalable is curation of “high-quality” corpora, such as social media conversations, books, or... | #summary #topic |
| [[Papers Explained 60 - Llama 2]] | Llama 2 is a collection of pretrained and fine-tuned large language models (LLMs) ranging in scale from 7 billion to 70 billion parameters. Their fine-tuned LLMs, called Llama... | #summary #topic |
| [[Papers Explained 61 - Humpback]] | Instruction back translation is a scalable method to build a high-quality instruction following language model by automatically labeling human written text with corresponding... | #summary #topic |
| [[Papers Explained 62 - Code Llama]] | Code Llama is a family of large language models for code based on Llama 2 providing state-of-the-art performance among open models, infilling capabilities, support for large input... | #summary #topic |
| [[Papers Explained 63 - LLaMA 2 Long]] | LLaMA 2 Long is a series of long-context LLMs built through continual pretraining from LLAMA 2 with longer training sequences that support effective context windows of up to... | #summary #topic |
| [[Papers Explained 65 - GPT-2]] | GPT-2 demonstrates that language models begin to learn various language processing tasks without any explicit supervision. GPT-2 is trained on a new dataset of millions of web... | #summary #topic |
| [[Papers Explained 66 - GPT-3]] | GPT-3 is an autoregressive language model with 175 billion parameters, 10x more than any previous non-sparse language model. It demonstrates that scaling up language models... | #summary #topic |
| [[Papers Explained 67 - GPT-4]] | GPT-4 is a large-scale, multimodal Transformer based model pre-trained to predict the next token in a document, which can accept image and text inputs and produce text outputs. | #summary #topic |
| [[Papers Explained 68 - GPT-4V]] | GPT-4 with vision (GPT-4V) enables users to instruct GPT-4 to analyze image inputs provided by the user. Incorporating additional modalities (such as image inputs) into LLMs is a... | #summary #topic |
| [[Papers Explained 69 - Llemma]] | Llemma is an LLM for mathematics. Formed by continued pretraining of Code Llama on Proof-Pile-2, a mixture of scientific papers, web data containing mathematics, and mathematical... | #summary #topic |
| [[Papers Explained 70 - CodeFusion]] | Auto-regressive models for code generation have a limitation: they do not easily allow reconsidering earlier tokens generated. CodeFusion is a 75M pre-trained diffusion code... | #summary #topic |
| [[Papers Explained 71 - Zephyr]] | Zephyr is 7B LLM that utilizes distilled Direct Preference Optimization (dDPO) that significantly improves intent alignment and AI Feedback (AIF) preference data to achieve... | #summary #topic |
| [[Papers Explained 72 - UniLM]] | UNIfied pre-trained Language Model (UNILM)is pre-trained using three types of language modeling tasks: unidirectional, bidirectional, and sequence-to-sequence prediction, by... | #summary #topic |
| [[Papers Explained 73 - UniLMv2]] | UniLMv2 introduces a novel training procedure, PMLM, which enables efficient learning of inter-relations between corrupted tokens and context via autoencoding, as well as... | #summary #topic |
| [[Papers Explained 74 - T0]] | T0 is a fine tuned encoder-decoder model on a multitask mixture covering a wide variety of tasks. The model attains strong zero-shot performance on several standard datasets... | #summary #topic |
| [[Papers Explained 75 - Flan T5, Flan PaLM]] | This paper explores instruction fine tuning with a particular focus on (1) scaling the number of tasks, (2) scaling the model size, and (3) fine tuning on chain-of-thought data. | #summary #topic |
| [[Papers Explained 76 - LaMDA]] | Language Models for Dialog Applications (LaMDA) is a family of Transformer based natural language models specialized for dialog, which have up to 137B parameters and are... | #summary #topic |
| [[Papers Explained 77 - Cascade RCNN]] | In Cascade R-CNN, bounding box regression is framed as a cascaded regression problem, relying on a cascade of specialized regressors. | #summary #topic |
| [[Papers Explained 78 - GPT-NeoX-20B]] | GPT-NeoX-20B is an autoregressive language model trained on the Pile, and the largest dense autoregressive model that had publicly available weights at the time of submission. | #summary #topic |
| [[Papers Explained 79 - DETR]] | DEtection TRansformer or DETR streamlines the detection pipeline, effectively removing the need for many hand-designed components like a non-maximum suppression procedure or... | #summary #topic |
| [[Papers Explained 80 - Gemini 1.0]] | Gemini is a family of highly capable multi-modal models developed at Google, trained jointly across image, audio, video, and text data for the purpose of building a model with... | #summary #topic |
| [[Papers Explained 81 - An In-depth Look at Gemini’s Language Abilities]] | A third-party, objective comparison of the abilities of the OpenAI GPT and Google Gemini models with reproducible code and fully transparent results. Code and data for... | #summary #topic |
| [[Papers Explained 82 - Flamingo]] | Flamingo is a family of visual language models (VLMs) that take as input visual data interleaved with text and produce free-form text as output. | #summary #topic |
| [[Papers Explained 83 - Are Emergent Abilities of Large Language Models a Mirage]] | Large language models are claimed to demonstrate certain emergent abilities which are not present at smaller scales. These emergent abilities are intriguing because of their... | #summary #topic |
| [[Papers Explained 84 - NF Net]] | NF Net is an improved class of Normalizer-Free ResNets that achieves competitive test accuracies with batch-normalized networks, offers faster training times, and introduces an... | #summary #topic |
| [[Papers Explained 85 - Scaling Data-Constrained Language Models]] | Extrapolating the current trend of scaling language models i.e. increasing both parameter count and training dataset size suggests that training dataset size may soon be limited... | #summary #topic |
| [[Papers Explained 86 - Dense Passage Retriever]] | This paper shows that retrieval can be practically implemented using dense representations alone, where embeddings are learned from a small number of questions and passages by a... | #summary #topic |
| [[Papers Explained 87 - DocLLM]] | DocLLM is a lightweight extension to traditional large language models (LLMs) for reasoning over visual documents, taking into account only textual semantics and spatial layout... | #summary #topic |
| [[Papers Explained 88 - ColBERT]] | ColBERT is a novel ranking model that adapts deep LMs (in particular, BERT) for efficient retrieval. It introduces a late interaction architecture that independently encodes the... | #summary #topic |
| [[Papers Explained 89 - ColBERTv2]] | Late interaction models produce multi-vector representations at the granularity of each token and decompose relevance modeling into scalable token-level computations. This... | #summary #topic |
| [[Papers Explained 90 - E5]] | E5 (EmbEddings from bidirEctional Encoder rEpresentations) is a family of state-of-the-art text embeddings trained in a contrastive manner with weak supervision signals from a... | #summary #topic |
| [[Papers Explained 91 - E5 Mistral-7B]] | This paper introduces a novel and simple method for obtaining high-quality text embeddings using only synthetic data and less than 1k training steps. It leverages proprietary LLMs... | #summary #topic |
| [[Papers Explained 92 - ConvNeXt]] | The starting point is a ResNet-50 model. It is first trained using similar training techniques employed for training vision Transformers, resulting in much improved results... | #summary #topic |
| [[Papers Explained 93 - TinyLlama]] | TinyLlama is a compact 1.1B language model built upon the architecture and tokenizer of Llama 2, pre-trained on around 1 trillion tokens for approximately 3 epochs, leveraging... | #summary #topic |
| [[Papers Explained 94 - ConvNeXt V2]] | The ConvNeXt model demonstrated strong results but struggles when combined with self-supervised learning (MAE). ConvNeXt V2 addresses this by incorporating a fully convolutional... | #summary #topic |
| [[Papers Explained 95 - Mixtral 8x7B]] | Mixtral 8x7B is a Sparse Mixture of Experts (SMoE) language model trained with multilingual data using a context size of 32k tokens. The paper also presents Mixtral 8x7B —... | #summary #topic |
| [[Papers Explained 96 - Matryoshka Representation Learning]] | Matryoshka Representation Learning (MRL) encodes information at different granularities and allows a flexible representation that can adapt to multiple downstream tasks with... | #summary #topic |
| [[Papers Explained 97 - Dolma]] | Dolma (Data for Open Language Models’ Appetite) is an open corpus of three trillion tokens designed to support language model pretraining research, sourced from a diverse mix of... | #summary #topic |
| [[Papers Explained 98 - OLMo]] | The entire framework, including the [code](https://github.com/allenai/OLMo), [model](https://huggingface.co/allenai/OLMo-7B), and... | #summary #topic |
| [[Papers Explained 99 - BLOOMZ, mT0]] | The study applies Multitask prompted fine tuning to the pretrained multilingual BLOOM and mT5 model families to produce finetuned variants called BLOOMZ and mT0. | #summary #topic |
| [[Papers Explained: Arcee Trinity]] | Sparse MoE language model family (Nano 6B/1B active, Mini 26B/3B active, Large 400B/13B active) with gated attention, depth-scaled sandwich norm, sigmoid routing, and SMEBU load balancing; trained on 10–17T tokens. | #summary |
| [[Papers Explained: Text Classification with Gzip]] | Training-free gzip+kNN text classifier using Normalized Compression Distance; competitive with non-pretrained deep models in-distribution and outperforms BERT on OOD and low-resource datasets. | #summary |
| [[Papers Explained Corpus]] | Master topic for the locally ingested Papers Explained Medium export corpus. | #topic |
| [[Papers Explained Review 01 - Convolutional Neural Networks]] | [Gradient-Based Learning Applied to Document Recognition](https://ieeexplore.ieee.org/document/726791) | #summary #topic |
| [[Papers Explained Review 02 - Layout Transformers]] | [LayoutLM: Pre-training of Text and Layout for Document Image Understanding](https://arxiv.org/abs/1912.13318) | #summary #topic |
| [[Papers Explained Review 03 - RCNNs]] | [Rich feature hierarchies for accurate object detection and semantic segmentation](https://arxiv.org/abs/1311.2524) | #summary #topic |
| [[Papers Explained Review 04 - Tabular Deep Learning]] | Neural networks are not as prominent when dealing with machine learning problems with structured data. This can be easily seen by the fact that the top teams in many online... | #summary #topic |
| [[Papers Explained Review 05 - Generative Adversarial Networks]] | Generative Adversarial Networks (GANs) are a class of machine learning models that consist of two components: a generator and a discriminator. | #summary #topic |
| [[Papers Explained Review 06 - Parameter Efficient FineTuning]] | [LoRA](https://ritvik19.medium.com/papers-explained-review-06-parameter-efficient-finetuning-6934fafa74e5#05fa) (Jun 2021) | #summary #topic |
| [[Papers Explained Review 06 - Position Encodings]] | Unlike traditional neural networks that utilise recurrence or convolution to process sequential data, transformers lack an inherent mechanism to recognize the order of input... | #summary #topic |
| [[Papers Explained Review 07 - Convolution Layers]] | Convolutional layers consist of a set of learnable filters, also known as kernels or feature detectors. Each filter is a small matrix, typically square, with weights initialized... | #summary #topic |
| [[Papers Explained Review 08 - Recurrent Layers]] | Input Propagation: At each time step t, the input vector X(t) is fed into the Input Layer. The hidden state H(t-1) from the previous time step t-1 is also passed into the Hidden... | #summary #topic |
| [[Papers Explained Review 09 - Attention Layers]] | Scaled Dot-Product Attention is a mechanism designed to enhance model focus on relevant parts of input data by dynamically adjusting the input values’ weights. This process... | #summary #topic |
| [[Papers Explained Review 10 - Normalization Layers]] | Batch Normalization was first discussed in the paper [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate... | #summary #topic |
| [[Papers Explained Review 11 - Auto Encoders]] | Autoencoders are a type of neural network architecture used for unsupervised learning and dimensionality reduction. They are primarily designed to learn efficient representations... | #summary #topic |
| [[Papers Explained Review 12 - LLMs for Maths]] | [WizardMath: Empowering Mathematical Reasoning for Large Language Models via Reinforced Evol-Instruct](https://arxiv.org/abs/2308.09583) | #summary #topic |
| [[Papers Explained Review 13 - Model Merging]] | Model merging techniques offer a powerful way to combine multiple fine-tuned models, leveraging their strengths to enhance performance without additional training. This article... | #summary #topic |
| [[Papers Explainedv377 - Fathom-R1]] | Fathom-R1–14B is a 14-billion-parameter reasoning language model derived from Deepseek-R1-Distilled-Qwen-14B, fine-tuned for mathematical reasoning by Fractal. | #summary #topic |
| [[Policy Gradient]] | Optimization lens for updating a policy from estimated reward-correlated probability changes. | #concept |
| [[Post-Training]] | Multi-stage training after pretraining: SFT, preference alignment (RLHF/DPO), and verifier-driven RL (RLVR). | #concept |
| [[Direct Preference Optimization]] | Preference alignment via closed-form KL-constrained objective; avoids explicit RL loop. | #concept |
| [[Doom Loop]] | #concept | Repetitive degeneration failure mode where reasoning models lock into repeated spans until context fills. | 2026-07-12 |
| [[Reasoning Models]] | Math, coding, scientific, and general reasoning methods, including training-time and test-time reasoning strategies. | #topic |
| [[Reinforcement Learning]] | On-policy reward-driven training regime whose improvements can compound through student rollouts. | #concept |
| [[Reinforcement Learning Topic]] | Reinforcement-learning and preference-optimization papers that train models from reward, verifier, or preference signals. | #topic |
| [[Reinforcement Learning: An Introduction]] | Sutton & Barto (2nd ed.): canonical RL textbook—MDPs, bandits, TD/Q-learning, function approximation, policy gradients, deep RL. | #summary |
| [[Richard S. Sutton]] | Co-author of *Reinforcement Learning: An Introduction*; pioneered TD learning and policy gradient methods. | #entity |
| [[Andrew G. Barto]] | Co-author of *Reinforcement Learning: An Introduction*; foundational RL and neuroscience connections. | #entity |
| [[Markov Decision Process]] | Standard RL formalism: states, actions, rewards, transitions, policies, and value functions. | #concept |
| [[Temporal-Difference Learning]] | Bootstrapped RL methods (TD, Sarsa, Q-learning) that update from successor estimates. | #concept |
| [[Q-learning]] | Off-policy TD control algorithm learning optimal action-values via max over next-state actions. | #concept |
| [[Actor-Critic Methods]] | Policy gradient with a value-function critic for lower-variance updates; lineage of PPO-style LLM RL. | #concept |
| [[Contextual Bandits]] | Bandits with per-round context features; bridge to full MDP control. | #concept |
| [[Deadly Triad]] | Instability when combining function approximation, bootstrapping, and off-policy learning. | #concept |
| [[Dynamic Programming]] | RL planning with a known model: policy iteration, value iteration, Bellman backups. | #concept |
| [[Dyna]] | Integrates learned models with TD updates for planning from simulated experience. | #concept |
| [[Eligibility Traces]] | Backward-view TD(λ) credit assignment unifying TD and Monte Carlo. | #concept |
| [[Expected Sarsa]] | On-policy TD control using the expectation over next actions instead of a single sample. | #concept |
| [[Exploration-Exploitation Tradeoff]] | Balancing trying new actions vs repeating what has worked; core RL dilemma. | #concept |
| [[Function Approximation in RL]] | Parameterized value/policy estimates for large state spaces; tile coding to deep nets. | #concept |
| [[Importance Sampling]] | Off-policy correction via behavior/target policy probability ratios. | #concept |
| [[Monte Carlo Methods]] | RL learning from complete episode returns without bootstrapping. | #concept |
| [[Multi-Armed Bandits]] | Stateless RL: k actions, stochastic rewards, exploration algorithms (ε-greedy, UCB). | #concept |
| [[n-Step Methods]] | TD methods using n-step returns between one-step TD and full Monte Carlo. | #concept |
| [[Off-Policy Learning]] | Learn a target policy from data collected under a different behavior policy. | #concept |
| [[On-Policy Learning]] | Train on data from the policy being improved (Sarsa, on-policy actor–critic). | #concept |
| [[Options]] | Temporally extended actions for hierarchical RL and temporal abstraction. | #concept |
| [[Policy Iteration]] | DP loop alternating policy evaluation and greedy improvement. | #concept |
| [[REINFORCE]] | Monte Carlo policy gradient: update log-probs weighted by return. | #concept |
| [[Sarsa]] | On-policy TD control using the actual next action in the TD target. | #concept |
| [[Value Iteration]] | DP algorithm iterating Bellman optimality backups until convergence. | #concept |
| [[Reinforcement Learning from Human Feedback]] | Nathan Lambert's open RLHF textbook: post-training pipeline, algorithms, data, over-optimization, RLVR, evaluation. | #summary |
| [[RLHF]] | Align LMs to human preferences via reward modeling and RL or direct preference optimization. | #concept |
| [[Reinforcement Learning with Verifiable Rewards]] | Post-training with programmatic verifiers (math, code, IF checks) instead of learned preference RMs. | #concept |
| [[RL Environments]] | Interactive task scaffolds for LLM reinforcement learning, covering tools, tasks, reward wiring, and episode control. | #concept |
| [[RL Environments in the LLM Era]] | Survey of six LLM RL environment frameworks, comparing deployment, reward architecture, task coupling, and scaling. | #summary #topic |
| [[Safety and Alignment]] | Safety, privacy, alignment, refusal behavior, constitutional AI, and guardrail techniques. | #topic |
| [[SMEBU]] | Soft-clamped Momentum Expert Bias Updates; MoE load-balancing strategy used in Arcee Trinity Large combining tanh soft-clamping and a momentum buffer for stable expert bias updates. | #concept |
| [[Self-Distilled Fine-Tuning]] | Self-distillation approach that uses privileged demonstrations to guide the model's own training signal. | #concept |
| [[Self-Summarization]] | RL-trained agent behavior: compress a long trajectory into a useful summary when context fills, then continue working. | #concept |
| [[Supervised Fine-Tuning]] | Post-training on fixed example completions from humans, datasets, or teacher models. | #concept |
| [[Synthetic Data]] | Synthetic-data generation, filtering, rephrasing, instruction data, and dataset-construction methods. | #topic |
| [[Tomas Mikolov]] | Researcher behind Word2Vec, skip-gram/CBOW, and negative sampling (Google, 2013). | 2026-05-21 |
| [[Tool Call Reliability]] | Per-tool, per-model error classification and anomaly detection used to keep agent harnesses stable in production. | #concept |
| [[Truncated Importance Sampling]] | Algorithmic fix for the sampler-learner engine gap in LLM RL training; scales policy gradient by a capped importance ratio π_learner/π_sampler. | #concept |
| [[Verifier-Bounded Learning]] | Training regime whose ceiling is set by what a verifier can grade rather than what a teacher can demonstrate. | #concept |
| [[Vision Language Models]] | Multimodal and vision-language systems that connect image, video, document, and text understanding. | #topic |
| [[gzip Predicts Data-dependent Scaling Laws]] | #summary | Shows that neural scaling laws depend on training data complexity, measured by gzip compressibility, challenging the universality of Chinchilla's compute-optimal ratios. | 2026-05-12 |
| [[Scaling Laws, Carefully]] | #summary | Lilian Weng Jun 2026 survey: Kaplan vs Chinchilla reconciliation, data-limited scaling, fitting pitfalls. | 2026-07-12 |
| [[Scaling Laws]] | #concept | Power-law relationships between model loss, parameter count, token count, and compute; the Chinchilla form and its data-dependent extensions. | 2026-05-12 |
| [[Data-Constrained Scaling Laws]] | #concept | Muennighoff effective-data decay and Lovelace capacity-ratio overfitting penalty for repeated tokens. | 2026-07-12 |
| [[IsoFLOP Profiles]] | #concept | Chinchilla Method 2: compute-optimal model size at fixed FLOP budget via parabolic fits. | 2026-07-12 |
| [[Probabilistic Context-Free Grammars]] | #concept | Grammars with probabilistic production rules used to generate synthetic datasets with controlled syntactic complexity. | 2026-05-12 |
| [[Papers Explained: Is Grep All You Need]] | Compares grep and vector retrieval on LongMemEval-style agent memory tasks, showing that harness design and tool-result delivery reshape retrieval accuracy. | #summary |
| [[Lexical Search]] | Surface-form retrieval using words, substrings, regular expressions, or sparse term weights; grep is the source's lexical baseline. | #concept |
| [[Dense Retrieval]] | Embedding-based retrieval using vector similarity, approximate nearest neighbors, and often reranking. | #concept |
| [[Agentic Search]] | Search performed inside an agent loop where the model chooses queries, calls tools, reads evidence, and refines its strategy. | #concept |
| [[Antidoom]] | #summary | Liquid AI blog on doom-loop failure modes and Final Token Preference Optimization; LFM2.5 and Qwen3.5 results. | 2026-07-12 |
| [[LongMemEval]] | Multi-session conversational-memory benchmark used to evaluate long-term memory retrieval under oracle and distractor sessions. | #entity |
| [[Papers Explained: IFBench]] | Introduces IFBench, a benchmark and IF-RLVR training setup for generalizing to unseen verifiable instruction-following constraints. | #summary |
| [[IFBench]] | Benchmark for precise instruction following under unseen Python-verifiable output constraints, with single-turn and multi-turn settings. | #entity |
| [[Verifiable Instruction Following]] | Instruction-following setup where explicit output constraints are paired with deterministic checkers for evaluation or verifier-reward training. | #concept |
| [[Papers Explained: Reward Hacking in Rubric-Based RL]] | Analyzes how rubric-reward RL can exploit verifier errors and optimize explicit criteria while degrading rubric-free holistic quality. | #summary |
| [[Rubric-Based Reinforcement Learning]] | RL setup where rewards are produced from prompt-specific rubrics judged by LLM or other verifiers. | #concept |
| [[Reward Hacking]] | Failure mode where measured reward improves while intended behavior or quality degrades. | #concept |
| [[Verifier Exploitation]] | Policy behavior that takes advantage of systematic false positives or blind spots in the training verifier. | #concept |
| [[Self-Internalization Gap]] | Verifier-free diagnostic comparing prompt-only and rubric-conditioned policy likelihoods to estimate rubric internalization. | #concept |
| [[Papers Explained: EMO]] | EMO pretrains mixture-of-experts models for document-level modularity, preserving quality when using small expert subsets. | #summary #topic |
| [[EMO]] | MoE pretraining method that constrains tokens in a document to route within a shared expert pool. | #concept |
| [[Inference Engineering]] | #summary | Comprehensive practitioner's guide (259 pp.) by Philip Kiely on serving generative AI models in production: hardware, software, quantization, speculation, caching, parallelism, disaggregation, and multi-modal inference. | 2026-05-18 |
| [[Inkling]] | #summary | Thinking Machines Lab open multimodal MoE (975B/41B active, 1M context, 45T tokens); Tinker fine-tuning base with controllable thinking effort. | 2026-07-21 |
| [[Introducing Composer 1.5]] | #summary | Cursor post on Composer 1.5: 20× RL on same base, adaptive thinking tokens, RL-trained self-summarization, Terminal-Bench 2.0 via Harbor. | 2026-05-19 |
| [[Introducing Composer 2]] | #summary | Cursor launch post for Composer 2: CursorBench / Terminal-Bench / SWE-bench scorecard, continued pretraining + long-horizon RL, fast-tier pricing. | 2026-06-06 |
| [[Introducing Composer 2.5]] | #summary | Cursor research post on Composer 2.5: targeted textual feedback for RL credit assignment, 25× synthetic coding tasks, sharded Muon + dual-mesh HSDP, and Kimi K2.5 base. | 2026-05-19 |
| [[Speculative Decoding]] | #concept | Inference optimization generating multiple draft tokens per forward pass; covers draft-target, Medusa, EAGLE, and n-gram speculation. | 2026-05-18 |
| [[Short Convolution]] | #concept | Local 1D convolution (SConv) over recent hidden states; used in Inkling after K/V projections and on residual branches. | 2026-07-21 |
| [[KV Cache]] | #concept | Precomputed attention keys/values reused across the autoregressive decode loop; prefix caching, offloading, and cache-aware routing. | 2026-05-18 |
| [[Disaggregated Serving]] | #concept | Separating prefill and decode phases onto independent GPU workers for independent optimization and scaling. | 2026-05-18 |
| [[GPU Inference Hardware]] | #concept | NVIDIA GPU architecture generations (Hopper, Blackwell, Rubin), compute/memory specs, and multi-GPU topology for inference. | 2026-05-18 |
| [[Inference Engine]] | #concept | Specialized serving software (vLLM, SGLang, TensorRT-LLM) handling batching, scheduling, KV cache, and hardware-specific optimizations. | 2026-05-18 |
| [[Baseten]] | #entity | Inference platform company powering production inference for AI-native products; publisher of Inference Engineering. | 2026-05-18 |
| [[Philip Kiely]] | #entity | Author of Inference Engineering; VP of AI at Baseten. | 2026-05-18 |
| [[Deep Learning]] | #summary | Goodfellow, Bengio & Courville (2016): canonical 801-page textbook—math foundations, CNNs, RNNs, optimization, regularization, representation learning, generative models. | 2026-05-20 |
| [[Ian Goodfellow]] | #entity | Lead author of *Deep Learning*; GANs and adversarial ML researcher. | 2026-05-20 |
| [[Yoshua Bengio]] | #entity | Co-author of *Deep Learning*; Turing laureate, deep learning and representation learning pioneer. | 2026-05-20 |
| [[Aaron Courville]] | #entity | Co-author of *Deep Learning*; probabilistic models and vision researcher. | 2026-05-20 |
| [[Back-Propagation]] | #concept | Reverse-mode AD via chain rule on computational graphs; core training algorithm for neural nets. | 2026-05-20 |
| [[Feedforward Neural Networks]] | #concept | Multilayer perceptrons: stacked affine layers + nonlinearities; universal deep learning building block. | 2026-05-20 |
| [[Convolutional Neural Networks]] | #concept | Spatial networks with local filters, weight sharing, and pooling; standard for vision. | 2026-05-20 |
| [[Recurrent Neural Networks]] | #concept | Sequence models with hidden state; LSTM/GRU and encoder–decoder architectures. | 2026-05-20 |
| [[Representation Learning]] | #concept | Learning useful features from data; deep learning as multi-layer representation learning. | 2026-05-20 |
| [[Dropout]] | #concept | Training-time random unit dropout for regularization; ensemble interpretation. | 2026-05-20 |
| [[Stochastic Gradient Descent]] | #concept | Minibatch-based gradient optimization for scalable deep learning training. | 2026-05-20 |
| [[Gradient Descent]] | #concept | Iterative optimization via negative gradients; core loop with back-propagation. | 2026-05-20 |
| [[Momentum]] | #concept | Velocity accumulation in gradient descent; dampens oscillations, speeds convergence. | 2026-05-20 |
| [[Adam]] | #concept | Adaptive moment optimizer combining momentum and per-parameter learning rates. | 2026-05-20 |
| [[Batch Normalization]] | #concept | Minibatch input standardization with learnable scale/shift; stabilizes deep training. | 2026-05-20 |
| [[Layer Normalization]] | #concept | Per-sample activation standardization over channels and spatial dims; transformer default. | 2026-06-06 |
| [[Group Normalization]] | #concept | Channel-group spatial normalization; batch-independent CNN alternative to BN. | 2026-06-06 |
| [[Instance Normalization]] | #concept | Per-sample per-channel spatial normalization; style transfer and generative models. | 2026-06-06 |
| [[Synchronized Batch Normalization]] | #concept | Distributed BN with global mean/variance across all GPUs/workers. | 2026-06-06 |
| [[Weight Normalization]] | #concept | Weight reparameterization w=(g/‖v‖)v decoupling magnitude from direction. | 2026-06-06 |
| [[Weight Standardization]] | #concept | Per-filter weight mean/std before convolution; pairs with GN in BiT. | 2026-06-06 |
| [[Adaptive Instance Normalization]] | #concept | Style-conditioned IN aligning content moments to reference image statistics (AdaIN). | 2026-06-06 |
| [[SPADE]] | #concept | Segmentation-conditioned spatially varying γ, β for semantic image synthesis. | 2026-06-06 |
| [[Weight Initialization]] | #concept | Starting parameter schemes (Xavier, He) preserving activation/gradient variance across layers. | 2026-05-20 |
| [[Weight Decay]] | #concept | L2 parameter penalty for regularization; encourages smaller weights. | 2026-05-20 |
| [[Early Stopping]] | #concept | Halt training when validation loss plateaus; implicit regularization. | 2026-05-20 |
| [[Data Augmentation]] | #concept | Label-preserving input transforms to expand effective training data. | 2026-05-20 |
| [[Adversarial Training]] | #concept | Train on perturbations that maximize loss to improve robustness. | 2026-05-20 |
| [[Overfitting]] | #concept | Model memorizes training data and fails to generalize; combated via regularization. | 2026-05-20 |
| [[Bias-Variance Tradeoff]] | #concept | Decomposition of generalization error into bias, variance, and noise. | 2026-05-20 |
| [[Maximum Likelihood Estimation]] | #concept | Fit parameters to maximize observed-data probability; links to cross-entropy loss. | 2026-05-20 |
| [[Cross-Entropy Loss]] | #concept | Classification objective equivalent to negative log-likelihood under softmax. | 2026-05-20 |
| [[Skip-Gram]] | Word2Vec architecture predicting context words from a target word in a sliding window. | 2026-05-21 |
| [[Softmax]] | #concept | Maps logits to a probability distribution over classes. | 2026-05-20 |
| [[Activation Functions]] | #concept | Nonlinearities (ReLU, sigmoid, tanh) enabling neural nets to approximate complex functions. | 2026-05-20 |
| [[Pooling]] | #concept | CNN downsampling (max/avg) for translation robustness and receptive field growth. | 2026-05-20 |
| [[LSTM]] | #concept | Gated RNN architecture with memory cells for long-term dependencies. | 2026-05-20 |
| [[GRU]] | #concept | Simplified gated RNN combining LSTM gates with fewer parameters. | 2026-05-20 |
| [[Encoder-Decoder Architecture]] | #concept | Sequence-to-sequence model compressing input then generating output steps. | 2026-05-20 |
| [[Vanishing Gradients]] | #concept | Shrinking back-propagated gradients in deep/RNN stacks; mitigated by gates and ReLU. | 2026-05-20 |
| [[Computational Graphs]] | #concept | DAG representation of differentiable programs for automatic differentiation. | 2026-05-20 |
| [[KL Divergence]] | #concept | Asymmetric measure of distribution difference; used in VI, distillation, RL regularization. | 2026-05-20 |
| [[Bayesian Statistics]] | #concept | Prior + likelihood + posterior framework for uncertainty-aware learning. | 2026-05-20 |
| [[Principal Component Analysis]] | #concept | Linear dimensionality reduction via orthogonal variance-maximizing directions. | 2026-05-20 |
| [[Autoencoders]] | #concept | Encoder–decoder networks learning compressed representations via reconstruction. | 2026-05-20 |
| [[Denoising Autoencoders]] | #concept | Reconstruct clean inputs from corrupted versions; learn robust manifold structure. | 2026-05-20 |
| [[Transfer Learning]] | #concept | Reuse pretrained representations or weights on a target task with limited data. | 2026-05-20 |
| [[Distributed Representations]] | #concept | Concepts encoded as patterns across many units; core advantage of deep learning. | 2026-05-20 |
| [[Greedy Layer-Wise Pretraining]] | #concept | Train deep nets layer-by-layer then fine-tune; historical pretraining strategy. | 2026-05-20 |
| [[Directed Graphical Models]] | #concept | Bayesian networks factoring joints into conditional DAG products. | 2026-05-20 |
| [[Undirected Graphical Models]] | #concept | Markov random fields with energy-based joint distributions. | 2026-05-20 |
| [[Partition Function]] | #concept | Normalizing constant Z for energy-based models; often intractable to compute. | 2026-05-20 |
| [[Markov Chain Monte Carlo]] | #concept | Sample-based approximate inference via Markov chains at target stationary distribution. | 2026-05-20 |
| [[Gibbs Sampling]] | #concept | MCMC by cycling conditional samples; used in RBM training. | 2026-05-20 |
| [[Contrastive Divergence]] | #concept | Approximate log-likelihood gradient for undirected models via short MCMC chains. | 2026-05-20 |
| [[Variational Inference]] | #concept | Optimize tractable distribution to approximate intractable posterior (minimize KL). | 2026-05-20 |
| [[Expectation Maximization]] | #concept | Alternate E-step (latent inference) and M-step (parameter update) for incomplete data. | 2026-05-20 |
| [[Restricted Boltzmann Machine]] | #concept | Bipartite undirected visible–hidden model; building block for deep belief nets. | 2026-05-20 |
| [[Deep Belief Networks]] | #concept | Stack of RBMs trained greedily; early deep generative pretraining architecture. | 2026-05-20 |
| [[Deep Boltzmann Machine]] | #concept | Multi-layer undirected generative model; harder to train than DBNs. | 2026-05-20 |
| [[Generative Adversarial Networks]] | #concept | Generator vs discriminator minimax game for implicit sample generation. | 2026-05-20 |
| [[Noise-Contrastive Estimation]] | #concept | Learn unnormalized models by discriminating data from noise; avoids partition function. | 2026-05-20 |
| [[Hyperparameter Tuning]] | #concept | Validation-driven selection of learning rate, capacity, and regularization settings. | 2026-05-20 |
| [[Singular Value Decomposition]] | #concept | Matrix factorization generalizing eigendecomposition; underpins PCA and low-rank methods. | 2026-05-20 |
| [[Entropy]] | #concept | Shannon information measure; foundation for cross-entropy and KL divergence. | 2026-05-20 |
| [[Model Capacity]] | #concept | Ability of a model class to fit diverse functions; linked to over/underfitting. | 2026-05-20 |
| [[Unsupervised Learning]] | #concept | Learning structure from unlabeled data (representations, density, clusters). | 2026-05-20 |
| [[Semi-Supervised Learning]] | #concept | Combine small labeled set with large unlabeled data via structural assumptions. | 2026-05-20 |
| [[Multi-Task Learning]] | #concept | Joint training on related tasks with shared representations as regularizer. | 2026-05-20 |
| [[Parameter Sharing]] | #concept | Reuse weights across positions (conv filters, tied embeddings). | 2026-05-20 |
| [[Bagging]] | #concept | Bootstrap ensemble of models; related to dropout interpretation. | 2026-05-20 |
| [[Second-Order Optimization]] | #concept | Curvature-aware methods (Newton, L-BFGS) for faster local convergence. | 2026-05-20 |
| [[Learning Word Embedding]] | #summary | Lilian Weng (2017): Word2Vec skip-gram/CBOW, softmax approximations (hierarchical softmax, NCE, negative sampling), GloVe, training heuristics, GoT gensim demo. | 2026-05-21 |
| [[Lilian Weng]] | ML researcher and educator; author of lilianweng.github.io technical posts including word embeddings (2017). | 2026-05-21 |
| [[Liquid AI]] | #entity | LFM foundation model family; Antidoom doom-loop research and FTPO training method. | 2026-07-12 |
| [[Word Embedding]] | Dense low-dimensional vectors representing words; capture similarity and analogy structure. | 2026-05-21 |
| [[Word2Vec]] | Shallow neural models (skip-gram, CBOW) for learning static word embeddings at scale. | 2026-05-21 |
| [[Learning Rate Schedule]] | #concept | Time-varying step sizes (decay, warm-up, cosine) for stable training. | 2026-05-20 |
| [[Curriculum Learning]] | #concept | Ordered presentation of examples from easy to hard. | 2026-05-20 |
| [[Convolution]] | #concept | Shared-filter operation on grids; core of CNNs. | 2026-05-20 |
| [[Bidirectional RNN]] | #concept | Forward+backward RNN for full-sequence context per position. | 2026-05-20 |
| [[Recursive Neural Networks]] | #concept | Tree-structured recurrent composition for parses and hierarchies. | 2026-05-20 |
| [[Echo State Networks]] | #concept | Fixed random reservoir with trained linear readout. | 2026-05-20 |
| [[ECHO Algorithm]] | #concept | Verifier-free RL that applies next-token CE to environment tokens alongside policy learning (implicit world model). | 2026-07-21 |
| [[Independent Component Analysis]] | #concept | Linear separation of non-Gaussian independent sources. | 2026-05-20 |
| [[Sparse Coding]] | #concept | Sparse linear codes over a learned dictionary. | 2026-05-20 |
| [[Contractive Autoencoders]] | #concept | Jacobian penalty for locally invariant representations. | 2026-05-20 |
| [[Variational Autoencoders]] | #concept | Latent generative model trained via variational lower bound. | 2026-05-20 |
| [[Score Matching]] | #concept | Match log-density gradients without partition function. | 2026-05-20 |
| [[Denoising Score Matching]] | #concept | Learn scores from corrupted samples; precursor to diffusion models. | 2026-05-20 |
| [[Pseudolikelihood]] | #concept | Product of conditionals for tractable MRF learning. | 2026-05-20 |
| [[MAP Inference]] | #concept | Most probable latent assignment; sparse coding connection. | 2026-05-20 |
| [[Boltzmann Machines]] | #concept | Fully connected energy-based undirected models. | 2026-05-20 |
| [[Generative Stochastic Networks]] | #concept | Learned Markov transitions with data as stationary distribution. | 2026-05-20 |
| [[Domain Adaptation]] | #concept | Transfer across distribution shift between source and target domains. | 2026-05-20 |
| [[RMSProp]] | #concept | Per-parameter adaptive scaling via running RMS of squared gradients. | 2026-05-20 |
| [[Log-Sum-Exp Trick]] | #concept | Numerically stable computation of log-partition and softmax denominators. | 2026-05-20 |
| [[Object Detection for Dummies Part 1]] | #summary | Lilian Weng (2017): image gradients, HOG, Felzenszwalb segmentation, Selective Search. | 2026-05-21 |
| [[Object Detection for Dummies Part 2]] | #summary | Lilian Weng (2017): AlexNet/VGG/ResNet, mAP/IoU, DPM, Overfeat. | 2026-05-21 |
| [[Object Detection for Dummies Part 3]] | #summary | Lilian Weng (2017): R-CNN through Mask R-CNN, bbox regression, NMS, RoIAlign. | 2026-05-21 |
| [[Object Detection Part 4]] | #summary | Lilian Weng (2018): one-stage detectors YOLO, SSD, RetinaNet, focal loss. | 2026-05-21 |
| [[Image Gradient]] | #concept | Per-pixel intensity change vector; basis for HOG and edge operators. | 2026-05-21 |
| [[Histogram of Oriented Gradients]] | #concept | Block-normalized orientation histogram features for object recognition. | 2026-05-21 |
| [[Felzenszwalb Segmentation]] | #concept | Graph-based image segmentation merging by edge weight predicate. | 2026-05-21 |
| [[Final Token Preference Optimization]] | #concept | DPO variant scoped to the single token that starts a doom loop (Liquid AI FTPO). | 2026-07-12 |
| [[Selective Search]] | #concept | Hierarchical region proposals from merged superpixels. | 2026-05-21 |
| [[Region Proposal]] | #concept | Candidate windows for object detection before classification. | 2026-05-21 |
| [[Mean Average Precision]] | #concept | Detection metric: mean of per-class AP under precision-recall curves. | 2026-05-21 |
| [[Intersection over Union]] | #concept | Box overlap ratio for matching detections to ground truth. | 2026-05-21 |
| [[Deformable Parts Model]] | #concept | Part-based latent SVM detector with deformable spatial model. | 2026-05-21 |
| [[Overfeat]] | #concept | Integrated CNN for sliding-window classification and bbox regression. | 2026-05-21 |
| [[R-CNN]] | #concept | Region-based CNN with per-RoI features and class SVMs. | 2026-05-21 |
| [[Fast R-CNN]] | #concept | Shared conv features + RoI pooling + joint cls/reg loss. | 2026-05-21 |
| [[Faster R-CNN]] | #concept | RPN + Fast R-CNN on shared feature map. | 2026-05-21 |
| [[Mask R-CNN]] | #concept | Faster R-CNN + per-RoI mask head and RoIAlign. | 2026-05-21 |
| [[RoI Pooling]] | #concept | Max-pool arbitrary RoI regions to fixed grid on feature map. | 2026-05-21 |
| [[RoIAlign]] | #concept | Bilinear RoI sampling without coordinate quantization. | 2026-05-21 |
| [[Region Proposal Network]] | #concept | Learned anchor-based proposals in Faster R-CNN. | 2026-05-21 |
| [[Bounding Box Regression]] | #concept | Refine box centers/scales with learned offsets. | 2026-05-21 |
| [[Non-Maximum Suppression]] | #concept | Suppress overlapping duplicate detections by score. | 2026-05-21 |
| [[Hard Negative Mining]] | #concept | Retrain on hard false-positive background regions. | 2026-05-21 |
| [[Smooth L1 Loss]] | #concept | Huber loss for robust bbox regression in Fast/Faster R-CNN. | 2026-05-21 |
| [[Two-Stage Object Detector]] | #concept | Sparse proposals then per-region classification (R-CNN family). | 2026-05-21 |
| [[One-Stage Object Detector]] | #concept | Dense single-pass prediction (YOLO, SSD, RetinaNet). | 2026-05-21 |
| [[YOLO]] | #concept | Grid-based real-time one-stage detector family. | 2026-05-21 |
| [[SSD Object Detection]] | #concept | Multi-scale anchor detection on conv feature pyramid. | 2026-05-21 |
| [[RetinaNet]] | #concept | FPN + focal loss one-stage detector. | 2026-05-21 |
| [[Pedro Felzenszwalb]] | Graph segmentation and DPM researcher. | 2026-05-21 |
| [[Ross Girshick]] | R-CNN family lead; DPM-as-CNN. | 2026-05-21 |
| [[Kaiming He]] | ResNet, Mask R-CNN, RoIAlign. | 2026-05-21 |
| [[Shaoqing Ren]] | Faster R-CNN co-author. | 2026-05-21 |
| [[Pierre Sermanet]] | Overfeat lead author. | 2026-05-21 |
| [[Joseph Redmon]] | YOLO family author. | 2026-05-21 |
| [[Reward Hacking in Reinforcement Learning]] | #summary | Lilian Weng (2024): Comprehensive synthesis of reward hacking taxonomy, scaling laws, RLHF-specific exploits (U-Sophistry, sycophancy, grader biases), in-context reward hacking (ICRH), and mitigations. | 2026-05-21 |
| [[In-Context Reward Hacking]] | #concept | Spontaneous alignment failure occurring at test-time inside iterative refinement loops without any parameter updates. | 2026-05-21 |
| [[U-Sophistry]] | #concept | Unintended sophistry where RLHF-trained models optimize human approval by cherry-picking evidence or generating unreadably complex code. | 2026-05-21 |
| [[Sycophancy]] | #concept | AI tendency to agree with stated human user beliefs and flattery, reinforced during human preference training. | 2026-05-21 |
| [[Decoupled Approval]] | #concept | Multi-agent safety mechanism querying human feedback on independently sampled state-action pairs rather than full trajectories to prevent feedback corruption. | 2026-05-21 |
| [[SEAL Framework]] | #concept | Quantitative evaluation methodology introduced by Revel et al. (2024) to analyze how training datasets influence behavioral alignment and identify spoiler features. | 2026-05-21 |
| [[Contrastive Representation Learning]] | #summary | Lilian Weng (2021): Comprehensive synthesis of contrastive training objectives (InfoNCE, triplet loss), vision architectures (SimCLR, BYOL, MoCo, CLIP), and text models (SimCSE, whitening). | 2026-05-21 |
| [[Triplet Loss]] | #concept | Anchor-positive-negative margin optimization objective that forces positive pairs closer than negative pairs by at least a specified margin. | 2026-05-21 |
| [[InfoNCE Loss]] | #concept | Categorical cross-entropy objective based on Noise Contrastive Estimation that maximizes the mutual information lower bound between representation views. | 2026-05-21 |
| [[SimCLR]] | #concept | Self-supervised visual representation pipeline maximizing agreement between differently augmented views via NT-Xent loss on a projection head. | 2026-05-21 |
| [[MoCo]] | #concept | Self-supervised visual representation framework treating contrastive learning as dynamic dictionary lookup over a FIFO queue with a momentum key encoder. | 2026-05-21 |
| [[Targeted Textual Feedback]] | #concept | Localized RL training technique inserting short textual hints in-context to define a teacher distribution for on-policy distillation. | 2026-05-21 |
| [[TabFM]] | #summary | Google Research zero-shot tabular foundation model: ICL over full tables, SCM pre-training, TabArena Elo leader. | 2026-07-12 |
| [[Tabular In-Context Learning]] | #concept | Tabular prediction as single-prompt ICL without per-dataset training (TabPFN, TabICL, TabFM). | 2026-07-12 |
| [[Cursor]] | #entity | AI-native code editor and coding-agent product creators of the Composer model family and research on agent harness design and large-scale RL. | 2026-05-21 |
| [[Mini Coding Agent]] | #entity | Sebastian Raschka's minimal pure-Python coding agent illustrating six harness components from scratch. | 2026-06-07 |
| [[OpenClaw]] | #entity | Local general-purpose agent platform; coding is one workload among multi-channel long-lived agents. | 2026-06-07 |
| [[Sebastian Raschka]] | #entity | ML educator, Ahead of AI author, and creator of from-scratch LLM/reasoning-model books and Mini Coding Agent. | 2026-06-07 |
| [[Moonshot AI]] | #entity | AI research company behind the Kimi large language model family, including the open Kimi K2.5 base model used in Composer. | 2026-05-21 |
| [[Thinking Machines Lab]] | #entity | AI research organization focused on fine-tuning and post-training efficiency, publisher of the Connectionism research blog. | 2026-05-21 |
| [[Tinker]] | #entity | Thinking Machines Lab managed fine-tuning / post-training platform; primary customization surface for Inkling. | 2026-07-21 |
| [[Papers Explained: OLMo 3]] | #summary | AllenAI's third generation of fully-open 7B and 32B models, covering Base, Think (via SFT + DPO + RLVR with OlmoRL), Instruct, and RL-Zero. | 2026-05-21 |
| [[AllenAI]] | #entity | Independent non-profit research institute conducting high-impact AI research and engineering, creator of OLMo, Dolma, and olmOCR. | 2026-05-21 |
| [[DeepSeek]] | #entity | AI research organization and company known for models like DeepSeek-R1, and algorithmic innovations like MLA, DeepSeekMoE, and GRPO. | 2026-05-21 |
| [[Cameron R. Wolfe]] | #entity | AI researcher and writer of the "Deep Learning Focus" technical newsletter on reinforcement learning and optimization. | 2026-05-21 |
| [[Self-Supervised Representation Learning]] | #summary | Lilian Weng (2019): Comprehensive survey of self-supervised pretext tasks across vision, video, and robotic control modalities. | 2026-05-21 |
| [[Exemplar-CNN]] | #concept | Self-supervised patch classification task learning representations invariant to rotations, scaling, and color shifts. | 2026-05-21 |
| [[Jigsaw Puzzle Pretext Task]] | #concept | Pretext task solving shuffled 3x3 patch permutations while avoiding lens chromatic aberration shortcuts. | 2026-05-21 |
| [[Context Encoder]] | #concept | Generative inpainting network trained to reconstruct missing image regions using combined L2 and adversarial losses. | 2026-05-21 |
| [[Split-Brain Autoencoder]] | #concept | Disjoint sub-network architecture trained to perform cross-channel color/structure predictions without capacity loss. | 2026-05-21 |
| [[Contrastive Predictive Coding]] | #concept | Sequence representation framework optimizing InfoNCE loss to maximize the mutual information lower bound. | 2026-05-21 |
| [[Grasp2Vec]] | #concept | Object-centric robotic metric learning utilizing N-Pair contrastive loss to subtract scene changes. | 2026-05-21 |
| [[Time-Contrastive Networks]] | #concept | Viewpoint-invariant robotic metric representations learned from multi-view video tracking with triplet loss. | 2026-05-21 |
| [[Reinforcement Learning with Imagined Goals]] | #concept | Goal-conditioned control policies operating in β-VAE latent metric representation spaces. | 2026-05-21 |
| [[Yann LeCun]] | #entity | Pioneer in self-supervised learning; deep learning and CNN advocate. | 2026-05-21 |
| [[DeepMind]] | #entity | AI research laboratory known for CPC, TCN, RIG, and structural biology models. | 2026-05-21 |
| [[How to Train Really Large Models on Many GPUs?]] | #summary | Lilian Weng (2021): Master survey of distributed deep learning techniques across training parallelism paradigms, MoE gating, and memory-saving designs. | 2026-05-21 |
| [[Data Parallelism]] | #concept | Distributed training paradigm that replicates the model across devices and partitions the mini-batch data to average gradients. | 2026-05-21 |
| [[Model Parallelism]] | #concept | Vertical layer-wise partitioning of neural networks across multiple devices to train models exceeding single-node memory. | 2026-05-21 |
| [[Pipeline Parallelism]] | #concept | Microbatch-based sequential layer sharding executing overlapping forward/backward steps to minimize idle processor bubbles. | 2026-05-21 |
| [[Tensor Parallelism]] | #concept | Horizontal intra-layer sharding of transformer attention and MLP matrices using inline collective communication sums. | 2026-05-21 |
| [[Activation Recomputation]] | #concept | Memory reduction technique that discards intermediate activations and recalculates them on-the-fly during the backward pass to achieve sublinear scaling. | 2026-05-21 |
| [[Mixed Precision Training]] | #concept | Numerical optimization training in half-precision (FP16/BF16) stabilized by full-precision master weights, loss scaling, and high-precision accumulation. | 2026-05-21 |
| [[ZeRO]] | #concept | Zero Redundancy Optimizer sharding optimizer states, gradients, and model parameters across data-parallel processes to eliminate memory redundancies. | 2026-05-21 |
| [[Mixture of Experts]] | #concept | Sparse architecture routing input tokens dynamically to a subset of specialized expert networks using gated neural routers. | 2026-05-21 |
| [[DeepSpeed]] | #entity | Microsoft's open-source deep learning optimization library implementing ZeRO, CPU offloading, and 3D parallelism. | 2026-05-21 |
| [[Megatron-LM]] | #entity | NVIDIA's large-scale training library specializing in horizontal Tensor Parallelism and interleaved pipeline schedules. | 2026-05-21 |
| [[GPipe]] | #entity | Google's synchronous Pipeline Parallelism framework that divides mini-batches into synchronous microbatches. | 2026-05-21 |
| [[Microsoft]] | #entity | Global technology corporation behind DeepSpeed and ZeRO, and pioneer of synthetic-data-driven small language models. | 2026-05-21 |
| [[Learning with not Enough Data Part 1: Semi-Supervised Learning]] | #summary | Lilian Weng (2021): SSL survey — consistency regularization, pseudo labeling, MixMatch/FixMatch, self-supervised pre-training baselines. | 2026-05-22 |
| [[Learning with not Enough Data Part 2: Active Learning]] | #summary | Lilian Weng (2022): budgeted labeling — uncertainty/diversity acquisition, MC dropout, BALD, BADGE, core-sets, VAAL/MAL. | 2026-05-22 |
| [[Learning with not Enough Data Part 3: Data Generation]] | #summary | Lilian Weng (2022): augmentation + LM synthesis (EDA, UDG, LAMBADA), affinity/diversity metrics, noisy-label training. | 2026-05-22 |
| [[Active Learning]] | #concept | Select unlabeled samples to label under budget via uncertainty, diversity, or model-change acquisition. | 2026-05-22 |
| [[Consistency Regularization]] | #concept | Penalize prediction change under valid perturbations; core SSL unsupervised loss. | 2026-05-22 |
| [[FixMatch]] | #concept | Weak-augment pseudo label + strong-augment consistency SSL (Sohn et al. 2020). | 2026-05-22 |
| [[MixMatch]] | #concept | SSL combining consistency, entropy minimization, and MixUp (Berthelot et al. 2019). | 2026-05-22 |
| [[Mean Teacher]] | #concept | EMA teacher weights for consistency targets in semi-supervised learning. | 2026-05-22 |
| [[Unsupervised Data Augmentation]] | #concept | UDA consistency training with RandAugment, sharpening, confidence masking (Xie et al. 2020). | 2026-05-22 |
| [[Noisy Student]] | #concept | Large-scale self-training with noisy student and soft pseudo labels (Xie et al. 2020). | 2026-05-22 |
| [[MC Dropout]] | #concept | Test-time dropout ensemble for epistemic uncertainty (Gal & Ghahramani 2016). | 2026-05-22 |
| [[BALD]] | #concept | Bayesian Active Learning by Disagreement; maximize information gain about weights. | 2026-05-22 |
| [[BADGE]] | #concept | Batch active learning via diverse gradient embeddings (Ash et al. 2020). | 2026-05-22 |
| [[Core-Set Active Learning]] | #concept | $k$-center geometric sample selection for active learning (Sener & Savarese 2018). | 2026-05-22 |
| [[Easy Data Augmentation]] | #concept | EDA lexical text augmentation (synonym replace, insert, swap, delete). | 2026-05-22 |
| [[Unsupervised Data Generation]] | #concept | UDG few-shot LM synthesis of inputs given labels + noisy label annealing. | 2026-05-22 |
| [[LAMBADA Data Generation]] | #concept | Class-conditioned LM fine-tuning for synthetic training text (Anaby-Tavor et al. 2019). | 2026-05-22 |
| [[Co-teaching]] | #concept | Dual-network mutual small-loss training robust to noisy labels (Han et al. 2018). | 2026-05-22 |
| [[DivideMix]] | #concept | GMM clean/noisy split + dual-network SSL for learning with noisy labels (Li et al. 2020). | 2026-05-22 |
| [[Meta Pseudo Labels]] | #concept | Meta-learn teacher pseudo labels via student performance on labeled data (Pham et al. 2021). | 2026-05-22 |
| [[Generalized Cross Entropy]] | #concept | Robust loss interpolating CCE and MAE for noisy labels (Zhang & Sabuncu 2018). | 2026-05-22 |
| [[Virtual Adversarial Training]] | #concept | Adversarial input perturbations for consistency without labels (Miyato et al. 2018). | 2026-05-22 |
| [[VAAL]] | #concept | Variational adversarial active learning in latent space (Sinha et al. 2019). | 2026-05-22 |
| [[MAL]] | #concept | Minimax active learning: VAAL diversity + entropy uncertainty (Ebrahimi et al. 2021). | 2026-05-22 |
| [[CEAL]] | #concept | Cost-effective AL: uncertain samples to humans + confident pseudo labels (Yang et al. 2016). | 2026-05-22 |
| [[Contrastive Active Learning]] | #concept | Acquire points with similar features but diverging predictions vs labeled neighbors (Margatina et al. 2021). | 2026-05-22 |
| [[Suggestive Annotation]] | #concept | Two-step hybrid AL: ensemble uncertainty then greedy max-cover diversity (Yang et al. 2017). | 2026-05-22 |
| [[LAMBADA Data Generation]] | #concept | Class-conditioned LM fine-tuning for synthetic text augmentation (Anaby-Tavor et al. 2019). | 2026-05-22 |
| [[2020-08-06-nas]] | #summary | Lilian Weng (2020): Neural Architecture Search survey decomposing AutoML structures into search spaces, search algorithms, and evaluation strategies. | 2026-05-22 |
| [[Neural Architecture Search]] | #concept | Automate neural network design via three pillars: search space, search algorithm, and child model evaluation strategy. | 2026-05-22 |
| [[ENAS]] | #concept | Efficient Neural Architecture Search using an over-parameterized supergraph and shared weights across sampled child subgraphs. | 2026-05-22 |
| [[DARTS]] | #concept | Differentiable Architecture Search mapping discrete stochastics to continuous variables via continuous relaxation and bilevel optimization. | 2026-05-22 |
| [[AutoML-Zero]] | #concept | Discover entire machine learning algorithms from scratch using regularized neuroevolution over basic mathematical primitives. | 2026-05-22 |
| [[2024-02-05-human-data-quality]] | #summary | Lilian Weng (2024): Master survey on high-quality human data SFT/RLHF engineering, prescriptive/descriptive aggregation, and training dynamic diagnostics. | 2026-05-22 |
| [[Majority Voting]] | #concept | Simple baseline consensus aggregation method that assigns a sample's label based on the most frequent response among a pool of annotators. | 2026-05-22 |
| [[MACE]] | #concept | Multi-Annotator Competence Estimation: generative graphical model using expectation-maximization to estimate latent annotator competence and identify spammers. | 2026-05-22 |
| [[Disagreement Deconvolution]] | #concept | Probabilistic aggregation framework that filters stochastic rater inconsistency noise to recover stable demographic belief distributions. | 2026-05-22 |
| [[Jury Learning]] | #concept | Interactive descriptive learning framework modeling demographic-dependent predictions using Deep & Cross Networks (DCN) and custom simulated juror panels. | 2026-05-22 |
| [[Influence Functions in DL]] | #concept | Closed-form robust statistics approximation tracing model predictions and test loss back to the gradient impact of individual training instances. | 2026-05-22 |
| [[Data Maps]] | #concept | Dataset cartography framework segmenting training samples into easy, ambiguous, and hard-to-learn regions based on epoch-by-epoch confidence and variability. | 2026-05-22 |
| [[Area Under the Margin]] | #concept | Scale-free logit margin ranking metric that leverages SGD tension with noisy label memorization to cleanly prune mislabeled training instances. | 2026-05-22 |
| [[What are Diffusion Models?]] | #summary | Lilian Weng (2021): Master survey on the mathematical foundations, accelerated sampling regimes, and scalable backbones of diffusion generative models. | 2026-05-22 |
| [[Denoising Diffusion Probabilistic Models]] | #concept | Markovian forward/reverse trajectories adding Gaussian noise and learning optimized simplified MSE noise prediction. | 2026-05-22 |
| [[Denoising Diffusion Implicit Models]] | #concept | Non-Markovian deterministic trajectory sampling enabling high-fidelity generation with up to 50x fewer inference steps. | 2026-05-22 |
| [[Classifier-Free Guidance]] | #concept | Steering conditional diffusion models by linearly interpolating between joint conditional and unconditional noise predictions. | 2026-05-22 |
| [[Latent Diffusion Models]] | #concept | Operating diffusion inside a perceptually compressed latent space to reduce training costs while preserving visual details. | 2026-05-22 |
| [[Consistency Models]] | #concept | Trajectory self-consistency functions mapping any point along a continuous probability flow ODE directly to the origin for single-step synthesis. | 2026-05-22 |
| [[Diffusion Transformer]] | #concept | Scalable generative backbone swapping traditional convolutional U-Nets for patchified vision transformers using AdaLN modulation. | 2026-05-22 |
| [[Diffusion Models for Video Generation]] | #summary | Lilian Weng (2024): Comprehensive overview of video generation diffusion architectures, temporal layers, and zero-shot adaptations. | 2026-05-22 |
| [[v-parameterization]] | #concept | Trigonometric parameterization of the DDIM update step in angular coordinates, preventing color-shift artifacts. | 2026-05-22 |
| [[space-time-u-net]] | #concept | Space-Time U-Net (STUNet) performing downsampling and upsampling over spatial and temporal dimensions concurrently. | 2026-05-22 |
| [[pseudo-3d-convolution]] | #concept | Factored spatial-only and temporal-only convolutional layer stack initialized to identity. | 2026-05-22 |
| [[cross-frame-attention]] | #concept | Attention variants that anchor frame queries to a reference frame (e.g., first frame or preceding frame) to enforce temporal visual consistency. | 2026-05-22 |
| [[reconstruction-guidance]] | #concept | Auxiliary MSE gradient guidance steering clean predictions to respect boundary or downsampled conditional constraints. | 2026-05-22 |
| [[Best Deep CNN Architectures and Their Principles: from AlexNet to EfficientNet]] | #summary | AI Summer survey of ImageNet CNN evolution: AlexNet through EfficientNet, compound scaling, BiT, Noisy Student, Meta Pseudo Labels. | 2026-06-06 |
| [[AlexNet]] | #concept | 2012 ImageNet CNN; first large-scale GPU-trained conv net with ReLU, max-pool, dropout. | 2026-06-06 |
| [[VGG]] | #concept | 2014 deep CNN using stacked 3×3 convolutions; depth-as-scaling paradigm. | 2026-06-06 |
| [[Vision Transformer]] | #concept | Dosovitskiy et al. 2020: image patches as transformer encoder tokens; needs large-scale pretraining to beat CNNs. | 2026-06-06 |
| [[Inception Network]] | #concept | GoogLeNet multi-branch modules with 1×1 bottleneck convs for multi-scale width scaling. | 2026-06-06 |
| [[ResNet]] | #concept | 2015 residual CNN with identity skip connections enabling 100+ layer stacks. | 2026-06-06 |
| [[DenseNet]] | #concept | 2017 densely connected CNN with feature concatenation and compact parameter count. | 2026-06-06 |
| [[EfficientNet]] | #concept | NAS-derived CNN family scaled via compound depth/width/resolution coefficients. | 2026-06-06 |
| [[Compound Scaling]] | #concept | Joint CNN depth, width, and resolution scaling under a FLOPs constraint (Tan & Le 2019). | 2026-06-06 |
| [[Big Transfer]] | #concept | Large-scale ResNet pretraining (BiT) with group norm on JFT-300M for transfer learning. | 2026-06-06 |
| [[Skip Connections]] | #concept | Layer shortcuts (add or concat) that ease training of deep networks; core ResNet/DenseNet mechanism. | 2026-06-06 |
| [[Understanding the Receptive Field of Deep Convolutional Networks]] | #summary | AI Summer survey of CNN receptive fields: biological motivation, Araujo closed-form RF, dilation/pooling growth, skip paths, and Luo effective RF. | 2026-06-06 |
| [[Receptive Field]] | #concept | Input region influencing a CNN unit's output; composes across conv, pooling, and dilation layers. | 2026-06-06 |
| [[Effective Receptive Field]] | #concept | Gradient-weighted subset of theoretical RF where input pixels materially affect output (Luo et al.). | 2026-06-06 |
| [[Dilated Convolution]] | #concept | Atrous conv with spaced kernel weights; exponential RF growth without resolution loss. | 2026-06-06 |
| [[The Theory behind Latent Variable Models: Formulating a Variational Autoencoder]] | #summary | AI Summer VAE theory: discriminative vs generative, latent-variable framework, ELBO, amortized VI, reparameterization, conv MNIST VAE. | 2026-06-06 |
| [[Latent Variable Models]] | #concept | Generative models with unobserved \(z\): prior, likelihood, joint, marginal, posterior; generation vs inference. | 2026-06-06 |
| [[ELBO]] | #concept | Evidence Lower Bound on log marginal likelihood; VAE training objective via variational inference. | 2026-06-06 |
| [[GANs in Computer Vision: Semantic Image Synthesis and Learning a Generative Model from a Single Image]] | #summary | AI Summer GAN series pt.6 (finale): GauGAN/SPADE semantic synthesis, SinGAN single-image pyramid GANs. | 2026-06-06 |
| [[GauGAN]] | #concept | SPADE-based semantic image synthesis from segmentation maps; multi-scale D from Pix2PixHD (Park et al. 2019). | 2026-06-06 |
| [[SinGAN]] | #concept | Multi-scale patch-GAN pyramid trained on one image; harmonization, editing (Shaham et al. ICCV 2019). | 2026-06-06 |
| [[GANs in Computer Vision: Self-Supervised Adversarial Training and High-Resolution Image Synthesis with Style Incorporation]] | #summary | AI Summer GAN series pt.5: rotation self-supervised GAN, StyleGAN/AdaIN, BN vs IN, disentanglement metrics. | 2026-06-06 |
| [[StyleGAN]] | #concept | Style-based generator: mapping network W, per-layer AdaIN, noise injection, truncation (Karras et al. 2019). | 2026-06-06 |
| [[Self-Supervised GAN]] | #concept | Auxiliary rotation loss on D to prevent forgetting in unconditional ImageNet GANs (Chen et al. 2019). | 2026-06-06 |
| [[GANs in Computer Vision: 2K Image and Video Synthesis, and Large-Scale Class-Conditional Image Generation]] | #summary | AI Summer GAN series pt.4: Pix2PixHD 2K synthesis, vid2vid temporal video GAN, BigGAN ImageNet scaling. | 2026-06-06 |
| [[Pix2PixHD]] | #concept | 2K multi-scale semantic synthesis: global G1 + local G2, image-pyramid PatchGAN D (Wang et al. 2017). | 2026-06-06 |
| [[Video-to-Video Synthesis]] | #concept | Temporally coherent 2K video GAN: flow warping, occlusion masks, dual image/video D (vid2vid 2018). | 2026-06-06 |
| [[BigGAN]] | #concept | Large-scale class-conditional ImageNet GAN: batch 2048, spectral norm, hinge loss, truncation trick (2018). | 2026-06-06 |
| [[GANs in Computer Vision: Improved Training with Wasserstein Distance, Game Theory Control, and Progressively Growing Schemes]] | #summary | AI Summer GAN series pt.3: WGAN/WGAN-GP, BEGAN equilibrium control, Progressive GAN megapixel synthesis. | 2026-06-06 |
| [[Wasserstein GAN]] | #concept | Earth Mover distance critic; weight clipping; n_critic training; reduces mode collapse (Arjovsky et al. 2017). | 2026-06-06 |
| [[BEGAN]] | #concept | Autoencoder D; Wasserstein distance on reconstruction errors; adaptive k_t balance (Berthelot et al. 2017). | 2026-06-06 |
| [[Progressive GAN]] | #concept | Coarse-to-fine resolution growing; smooth α transitions; first 1024×1024 GAN faces (Karras et al. 2017). | 2026-06-06 |
| [[GANs in Computer Vision: Conditional Image Synthesis and 3D Object Generation]] | #summary | AI Summer GAN series pt.2: AC-GAN, 3D-VAE-GAN, PacGAN, Pix2Pix, CycleGAN; paired/unpaired image translation. | 2026-06-06 |
| [[AC-GAN]] | #concept | Auxiliary classifier GAN: D reconstructs class labels; 128×128 ImageNet synthesis, MS-SSIM diversity (Odena et al. 2017). | 2026-06-06 |
| [[3D-GAN]] | #concept | Volumetric DCGAN for 3D shape synthesis; 3D-VAE-GAN for single-view RGB→voxel reconstruction (Wu et al. 2016). | 2026-06-06 |
| [[PacGAN]] | #concept | Packed-sample discriminator for mode-collapse detection via product-distribution hypothesis testing (Lin et al. 2018). | 2026-06-06 |
| [[Pix2Pix]] | #concept | Paired image-to-image translation: U-Net G, PatchGAN D, L1 + adversarial loss (Isola et al. 2017). | 2026-06-06 |
| [[CycleGAN]] | #concept | Unpaired domain translation via bidirectional generators and cycle-consistency loss (Zhu et al. 2017). | 2026-06-06 |
| [[GANs in Computer Vision: Introduction to Generative Learning]] | #summary | AI Summer GAN series pt.1: vanilla/cGAN/DCGAN/InfoGAN, mode collapse, Improved GAN tricks, PyTorch training loops, MNIST/CIFAR demos. | 2026-06-06 |
| [[Mode Collapse]] | #concept | GAN failure mode: generator diversity collapses to few or identical outputs; unstable gradients. | 2026-06-06 |
| [[DCGAN]] | #concept | Convolutional GAN baseline: strided conv D, transpose conv G, batch norm, ReLU/LeakyReLU design rules (Radford et al. 2015). | 2026-06-06 |
| [[InfoGAN]] | #concept | Mutual-information maximization for unsupervised disentangled latent codes in GANs (Chen et al. 2016). | 2026-06-06 |
| [[Feature Matching]] | #concept | Improved GAN objective: match D intermediate feature statistics (L2) to stabilize training. | 2026-06-06 |
| [[Inception Score]] | #concept | GAN image-quality metric via pretrained Inception classifier confidence and batch diversity. | 2026-06-06 |
| [[How to Generate Images using Autoencoders]] | #summary | AI Summer autoencoder/VAE primer: latent bottleneck, reparameterization, BCE+KL loss, MNIST demo, generative vs discriminative framing. | 2026-06-06 |
| [[Sergios Karagiannakos]] | #entity | AI Summer author of early generative-model tutorials (autoencoders, regularization, optimization). | 2026-06-06 |
| [[How Positional Embeddings Work in Self-Attention (Code in PyTorch)]] | #summary | AI Summer PE tutorial: encodings vs embeddings, absolute/relative 1D PE, 2D vision PE, PyTorch implementations. | 2026-06-06 |
| [[Positional Embeddings]] | #concept | Trainable position vectors inside MHSA; absolute index or relative distance buckets; 2D factorization for vision. | 2026-06-06 |
| [[Relative Position Embedding]] | #concept | Distance-based attention PE (Shaw / Music Transformer); Inkling uses relative attention instead of RoPE. | 2026-07-21 |
| [[Why Multi-Head Self Attention Works: Math, Intuitions and 10+1 Hidden Insights]] | #summary | AI Summer deep-dive: two-matmul attention, 11 research insights (asymmetry, head pruning, rank collapse, fast weights, efficient attention). | 2026-06-06 |
| [[Rank Collapse]] | #concept | Pure self-attention degenerates to rank-1 with depth; mitigated by skip connections and MLP (Dong et al.). | 2026-06-06 |
| [[An Overview of Classifier-Free Guidance for Diffusion Models]] | #summary | AI Summer CFG survey pt.1: classifier guidance, CFG derivation, Imagen thresholding, CADS, limited-interval CFG, spatial CFG, U-Net attention. | 2026-06-06 |
| [[An Overview of Classifier-Free Diffusion Guidance: Impaired Model Guidance with a Bad Version of Itself (Part 2)]] | #summary | AI Summer CFG pt.2: SAG, PAG, autoguidance, ICG, SIMS, SEG — impaired-model negatives without conditioning dropout. | 2026-06-06 |
| [[Tim Kaiser]] | #entity | AI Summer co-author of the 2024 two-part classifier-free guidance survey with Nikolas Adaloglou. | 2026-06-06 |
| [[Autoguidance]] | #concept | CFG with impaired checkpoint/smaller model as negative; both models conditional (Karras et al. 2024). | 2026-06-06 |
| [[Perturbed Attention Guidance]] | #concept | Training-free CFG alternative: identity self-attention maps as negative perturbation (PAG, Ahn et al. 2024). | 2026-06-06 |
| [[How Diffusion Models Work: The Math from Scratch]] | #summary | AI Summer DDPM tutorial: forward/reverse diffusion, ELBO, noise prediction, U-Net, CFG, latent/cascade scaling, score-based SDEs. | 2026-06-06 |
| [[Score-Based Generative Models]] | #concept | Score matching, NCSN multi-scale noise, Langevin dynamics, SDE unification with DDPM. | 2026-06-06 |
| [[Best Graph Neural Network Architectures: GCN, GAT, MPNN and More]] | #summary | AI Summer GNN architecture survey: spectral GCN, MPNN, GAT, GraphSAGE, PinSAGE, TGN; node/edge/graph tasks. | 2026-06-06 |
| [[Graph Attention Networks]] | #concept | GAT: learned softmax attention over graph neighbors; multi-head; replaces fixed GCN coefficients. | 2026-06-06 |
| [[Message Passing Neural Networks]] | #concept | MPNN framework: message \(f_e\), aggregate, update \(f_v\); unifies spatial GNNs. | 2026-06-06 |
| [[GraphSAGE]] | #concept | Sample-and-aggregate inductive GNN; learnable neighborhood aggregators for large graphs. | 2026-06-06 |
| [[How Graph Neural Networks (GNN) Work: Introduction to Graph Convolutions from Scratch]] | #summary | AI Summer GNN primer: structure/signal decomposition, Laplacian math, spectral Chebyshev GCN, 1-hop PyTorch GCN, MUTAG training. | 2026-06-06 |
| [[Graph Neural Networks]] | #concept | Neural networks on graph-structured data via neighborhood aggregation; inductive graph vs transductive node classification. | 2026-06-06 |
| [[Graph Convolutional Networks]] | #concept | GCN layers via normalized Laplacian multiplication; Kipf-Welling 1-hop and Defferrard Chebyshev spectral filters. | 2026-06-06 |
| [[Graph Laplacian]] | #concept | \(L = D - A\) graph operator; normalized form with self-loops stabilizes GCN training; eigenvalues encode connectivity. | 2026-06-06 |
| [[Grokking Self-Supervised (Representation) Learning: How It Works in Computer Vision and Why]] | #summary | AI Summer SSL tutorial: contrastive CV workflow, augmentations, SimCLR/BYOL/DINO, mode collapse, EMA teachers. | 2026-06-06 |
| [[Grok Models]] | #summary | xAI/SpaceXAI Grok timeline Nov 2023–Jul 2026: Grok-1 through Grok 4.5 (Cursor co-training), code/voice/imagine APIs; Colossus/GB300 training. | 2026-07-10 |
| [[xAI]] | #entity | Elon Musk AI lab; Grok on 𝕏, Colossus cluster, xAI API (text, voice, imagine, agent tools). | 2026-06-11 |
| [[BYOL]] | #concept | Bootstrap Your Own Latent: negative-free SSL with EMA teacher, predictor MLP, and BN implicit contrast. | 2026-06-06 |
| [[In-layer Normalization Techniques for Training Very Deep Neural Networks]] | #summary | AI Summer survey of BN, LN, IN, GN, SyncBN, weight norm/WS, AdaIN, SPADE; axis aggregation and task mapping. | 2026-06-06 |
| [[How the Vision Transformer (ViT) Works in 10 Minutes: An Image Is Worth 16×16 Words]] | #summary | AI Summer ViT primer: patch tokenization, JFT-scale pretraining requirement, attention distance vs conv RF, PyTorch ViT code. | 2026-06-06 |
| [[How Transformers Work in Deep Learning and NLP: An Intuitive Introduction]] | #summary | AI Summer transformer tutorial: tokenization, positional encoding, scaled dot-product attention, multi-head, encoder/decoder, masked and cross-attention. | 2026-06-06 |
| [[Positional Encoding]] | #concept | Fixed position signals (sinusoidal in original Transformer) added to embeddings; distinct from trainable [[Positional Embeddings]]. | 2026-06-06 |
| [[Multi-Head Attention]] | #concept | Parallel attention heads in different subspaces; concatenated and projected in transformer blocks. | 2026-06-06 |
| [[How Attention Works in Deep Learning: Understanding the Attention Mechanism in Sequence Models]] | #summary | AI Summer attention primer: seq2seq bottleneck, Bahdanau attention, soft/hard/global/local taxonomy, self-attention, and applications beyond NLP. | 2026-06-06 |
| [[Attention Mechanism]] | #concept | Dynamic input weighting for sequences; solves encoder–decoder bottleneck via learned alignments and memory-through-time weights. | 2026-06-06 |
| [[Self-Attention]] | #concept | Intra-sequence attention connecting all tokens; core transformer building block with \(O(n^2)\) cost. | 2026-06-06 |
| [[Recurrent Neural Networks: Building GRU Cells VS LSTM Cells in PyTorch]] | #summary | AI Summer GRU tutorial: reset/update gates, LSTM-vs-GRU tradeoffs, when RNNs beat transformers. | 2026-06-06 |
| [[Recurrent Neural Networks: Building a Custom LSTM Cell]] | #summary | AI Summer LSTM tutorial: RNN unrolling, BPTT, gate equations, custom PyTorch cell, bidirectional stacking, RNN vs CNN receptive field. | 2026-06-06 |
| [[Backpropagation Through Time]] | #concept | Train RNNs by unrolling across timesteps and summing shared-weight gradients. | 2026-06-06 |
| [[Nikolas Adaloglou]] | #entity | AI Summer author of CNN architecture, receptive-field, LSTM/GRU, attention, and transformer tutorials (2020–2021). | 2026-06-06 |
| [[Sasha Rush Explains Targeted On-Policy Self-Distillation]] | #summary | Sasha Rush's impromptu video lecture to Dwarkesh Patel on sequence KD, on-policy distillation, and targeted on-policy self-distillation as used for Cursor Composer 2.5. | 2026-06-04 |
| [[Sasha Rush]] | #entity | ML researcher (Cornell); explained Cursor's targeted self-distillation method in a video posted by Dwarkesh Patel. | 2026-06-04 |
| [[Dwarkesh Patel]] | #entity | Podcast host and interviewer; recorded Sasha Rush's lecture on targeted on-policy self-distillation. | 2026-06-04 |
| [[Explainable AI]] | #concept | Methods making ML decisions understandable; visual saliency, textual rationales, numerical concept testing. | 2026-06-06 |
| [[Grad-CAM]] | #concept | Gradient-weighted CNN class activation maps; backprops class score to final conv layer. | 2026-06-06 |
| [[LIME]] | #concept | Local interpretable model-agnostic explanations via simple surrogate models. | 2026-06-06 |
| [[Class Activation Mapping]] | #concept | CNN saliency via GAP-layer class weights on conv feature maps (CAM, Zhou et al. 2016). | 2026-06-06 |
| [[Layer-Wise Relevance Propagation]] | #concept | Backward relevance decomposition assigning pixel-level contribution scores. | 2026-06-06 |
| [[Concept Activation Vectors]] | #concept | TCAV concept sensitivity testing via binary classifiers in hidden activation space. | 2026-06-06 |
| [[Ilias Papastratis]] | #entity | AI Summer author of the 2021 XAI survey on interpretability methods and frameworks. | 2026-06-06 |
| [[Advancing Search-Augmented Language Models]] | #summary | Perplexity SFT→GRPO pipeline for web search agents: verifiable QA, rubric RL, gated rewards, Qwen3.5 results. | 2026-06-06 |
| [[pplx-embed: State-of-the-Art Embedding Models for Web-Scale Retrieval]] | #summary | pplx-embed-v1/context-v1 release: diffusion Qwen3 encoders, INT8/binary embeddings, MTEB/ConTEB/PPLX benchmarks. | 2026-06-06 |
| [[Accelerating Sonar Through Speculation]] | #summary | Perplexity speculative decoding for Sonar: draft-target, EAGLE, MTP, FlashInfer scheduling. | 2026-06-06 |
| [[RL Training For Math Reasoning]] | #summary | Perplexity GRPO math-reasoning infra: NeMo/vLLM, log-prob alignment, SFT warmup, collapse modes. | 2026-06-06 |
| [[Perplexity AI]] | #entity | AI company: Sonar LLMs, pplx-embed retrieval, search-agent research. | 2026-06-06 |
| [[Sonar]] | #entity | Perplexity LLM family accelerated via speculative decoding in production. | 2026-06-06 |
| [[pplx-embed]] | #entity | Perplexity multilingual embedding models for web-scale dense retrieval. | 2026-06-06 |
| [[Multi-Token Prediction]] | #concept | Auxiliary heads forecasting future tokens; MTP draft models for speculative decoding. | 2026-06-06 |
| [[FlashInfer]] | #concept | Customizable GPU attention engine used in Perplexity's inference runtime. | 2026-06-06 |
| [[Cohere]] | #entity | Enterprise AI company: Command, Embed, Rerank, Transcribe, Aya research, North platform. | 2026-06-06 |
| [[Introducing North Mini Code]] | #summary | Cohere's first open agentic coding MoE (30B/3B); Apache 2.0; harness-robust SFT + async CISPO RLVR. | 2026-06-09 |
| [[North Mini Code]] | #entity | Cohere open developer coding model: 30B/3B MoE, 256K context, multi-harness agentic training. | 2026-06-09 |
| [[OpenCode]] | #entity | Open-source coding-agent harness with fine-grained typed tools (edit, grep, task, etc.). | 2026-06-09 |
| [[Introducing Command A+]] | #summary | Cohere 218B-A25B MoE open flagship: reasoning, multimodal, 48 languages, sovereign deployment, speculative decoding. | 2026-06-06 |
| [[Command A Reasoning: Enterprise-grade Control for AI Agents]] | #summary | Cohere reasoning model for enterprise agents: BFCL, Tau-bench, Deep Research multi-agent, North. | 2026-06-06 |
| [[Introducing Command A Vision: Multimodal AI built for business]] | #summary | Cohere enterprise multimodal Command A Vision for charts, PDFs, and document understanding. | 2026-06-06 |
| [[Introducing Command A: Max performance, minimal compute]] | #summary | Cohere 111B Command A: two-GPU enterprise LLM, 23 languages, RAG and tool use vs GPT-4o/DeepSeek-V3. | 2026-06-06 |
| [[Command A Translate: Secure Translation for Global Enterprises]] | #summary | Cohere enterprise MT model built on Command A with DPO; WMT and long-context translation benchmarks. | 2026-06-06 |
| [[Introducing Command R+: A Scalable LLM Built for Business]] | #summary | Cohere 104B Command R+: RAG with citations, tool use, multilingual; Azure launch. | 2026-06-06 |
| [[Command R: Retrieval-Augmented Generation at Production Scale]] | #summary | Original Command R launch: 35B RAG-optimized LLM for production-scale enterprise AI. | 2026-06-06 |
| [[Introducing Command R7B: Fast and efficient generative AI]] | #summary | Cohere 7B compact R-series model: 128K context, RAG, BFCL tool use, commodity-GPU deployment. | 2026-06-06 |
| [[Introducing Command R7B Arabic]] | #summary | Arabic/English MENA specialization of Command R7B for enterprise RAG and agents. | 2026-06-06 |
| [[Introducing Cohere Transcribe]] | #summary | Cohere 2B Conformer ASR; 5.42% avg WER on Open ASR Leaderboard; 14 languages; Apache 2.0. | 2026-06-06 |
| [[C4AI Launches Aya, an LLM Covering More Than 100 Languages]] | #summary | Original Aya open-science launch: 513M-example collection, 114 languages, 3000+ collaborators. | 2026-06-06 |
| [[C4AI Launches Aya 23, 8B and 35B Parameter Open Weights Release]] | #summary | Cohere Labs Aya 23 8B/35B open weights covering 23 languages. | 2026-06-06 |
| [[Aya Expanse: Connecting our world]] | #summary | Aya Expanse 8B/32B multilingual LLMs: data arbitrage, preference training, model merging. | 2026-06-06 |
| [[Aya Vision: Expanding the worlds AI can see]] | #summary | Cohere Labs multilingual multimodal Aya Vision open-weights models. | 2026-06-06 |
| [[Cohere Labs Launches Tiny Aya]] | #summary | Official Tiny Aya blog: efficient open multilingual models for 70+ languages. | 2026-06-06 |
| [[Mistral AI]] | #entity | French AI company: Mistral, Mixtral, Codestral, Devstral, Pixtral, Magistral, Voxtral, OCR. | 2026-06-06 |
| [[Mistral 7B]] | #summary | Mistral 7.3B Apache 2.0 launch: GQA, sliding-window attention, beats Llama 2 13B. | 2026-06-06 |
| [[Au Large (Mistral Large)]] | #summary | Feb 2024 Mistral flagship: 32K context, multilingual, function calling, Azure. | 2026-06-06 |
| [[Large Enough (Mistral Large 2)]] | #summary | Mistral Large 2 (123B): 128K context, code/reasoning, multilingual, tool use. | 2026-06-06 |
| [[Mistral NeMo]] | #summary | 12B Mistral–NVIDIA model: Tekken tokenizer, 128K context, FP8, Apache 2.0. | 2026-06-06 |
| [[Mistral Small 3]] | #summary | 24B Apache 2.0 latency model; rivals Llama 3.3 70B at 3× speed. | 2026-06-06 |
| [[Mistral Small 3.1]] | #summary | Small 3 upgrade: multimodal, 128K context, beats GPT-4o Mini class. | 2026-06-06 |
| [[Mistral Saba]] | #summary | 24B Arabic/South Asian regional language model for Middle East enterprise. | 2026-06-06 |
| [[Mixtral of experts]] | #summary | Mixtral 8x7B SMoE: 46.7B total, 12.9B active; Apache 2.0; beats Llama 2 70B. | 2026-06-06 |
| [[Cheaper, Better, Faster, Stronger]] | #summary | Mixtral 8x22B: 141B total, 39B active; 64K context; Apache 2.0. | 2026-06-06 |
| [[Medium is the new large.]] | #summary | Mistral Medium 3: frontier performance at ~8× lower cost than Claude Sonnet 3.7. | 2026-06-06 |
| [[Introducing Mistral 3]] | #summary | Ministral 3 (3B/8B/14B) + Mistral Large 3 (675B MoE); all Apache 2.0. | 2026-06-06 |
| [[Introducing Mistral Small 4]] | #summary | Unified instruct/reasoning/multimodal MoE; configurable reasoning effort. | 2026-06-06 |
| [[Un Ministral, des Ministraux]] | #summary | Ministral 3B/8B edge models; 128K context; outperforms Mistral 7B. | 2026-06-06 |
| [[Codestral]] | #summary | Mistral 22B code model: 80+ languages, 32K context, FIM, RepoBench. | 2026-06-06 |
| [[Codestral Mamba]] | #summary | 7.3B Mamba code model; linear-time inference; Apache 2.0. | 2026-06-06 |
| [[Codestral 25.01]] | #summary | Upgraded Codestral: 256K context, 2× faster, SOTA FIM in weight class. | 2026-06-06 |
| [[Codestral Embed]] | #summary | Code-specialized embedding model for RAG and semantic code search. | 2026-06-06 |
| [[Announcing Codestral 25.08 and the Complete Mistral Coding Stack for Enterprise]] | #summary | Enterprise coding stack: Codestral + Embed + Devstral + Mistral Code IDE. | 2026-06-06 |
| [[Devstral]] | #summary | Agentic coding LLM; 46.8% SWE-Bench Verified; Apache 2.0. | 2026-06-06 |
| [[Upgrading agentic coding capabilities with the new Devstral models]] | #summary | Devstral Small 1.1 (53.6%) and Devstral Medium (61.6%) on SWE-Bench. | 2026-06-06 |
| [[Introducing: Devstral 2 and Mistral Vibe CLI.]] | #summary | Devstral 2 (123B, 72.2% SWE-Bench) + open-source Vibe CLI agent. | 2026-06-06 |
| [[Leanstral: Open-Source foundation for trustworthy vibe-coding]] | #summary | Lean 4 proof assistant agent; sparse 120B-A6B; FLTEval benchmark. | 2026-06-06 |
| [[MathΣtral]] | #summary | 7B STEM model from Mistral 7B; 56.6% MATH; majority voting to 74.59%. | 2026-06-06 |
| [[Announcing Pixtral 12B]] | #summary | 12B multimodal on Mistral NeMo; 400M vision encoder; Apache 2.0 (deprecated). | 2026-06-06 |
| [[Pixtral Large]] | #summary | 124B multimodal on Mistral Large 2; frontier VLM (deprecated). | 2026-06-06 |
| [[Mistral OCR]] | #summary | OCR API: documents, tables, equations; multilingual; RAG-ready markdown output. | 2026-06-06 |
| [[Introducing Mistral OCR 3]] | #summary | OCR 3: handwriting, forms, HTML tables; Document AI Playground. | 2026-06-06 |
| [[Magistral]] | #summary | First Mistral reasoning model: Small (24B open) + Medium; multilingual CoT. | 2026-06-06 |
| [[Voxtral]] | #summary | 24B/3B speech understanding: transcription, Q&A, function calling. | 2026-06-06 |
| [[Voxtral transcribes at the speed of sound.]] | #summary | Voxtral Transcribe 2 + Realtime: diarization, sub-200ms latency. | 2026-06-06 |
| [[Speaking of Voxtral]] | #summary | Voxtral TTS: 4B flow-matching; 9 languages; custom voice from 3s prompt. | 2026-06-06 |
| [[Gemini 3]] | #summary | Nov 2025 Gemini 3 Pro launch: reasoning, 1M context, Antigravity, generative UI, Deep Think. | 2026-06-06 |
| [[Gemini 3 Flash]] | #summary | Dec 2025 Flash tier: frontier speed, $0.50/$3 per M tokens, SWE-bench 78%, default in app/Search. | 2026-06-06 |
| [[Gemini Deep Research]] | #summary | Autonomous research agent via Interactions API; 46.4% HLE, DeepSearchQA benchmark. | 2026-06-06 |
| [[Agentic Vision in Gemini 3 Flash]] | #summary | Think-Act-Observe vision loop with code execution; 5–10% benchmark boost. | 2026-06-06 |
| [[Gemini 3 Deep Think]] | #summary | Specialized parallel reasoning: 84.6% ARC-AGI-2, 48.4% HLE, science/engineering focus. | 2026-06-06 |
| [[Google DeepMind]] | #entity | Google's AI research lab; Gemini, Nano Banana image models, AlphaFold. | 2026-06-06 |
| [[Google Research]] | #entity | Google Research blog brand; TabFM tabular foundation model and other applied ML releases. | 2026-07-12 |
| [[Nano Banana Pro]] | #summary | Gemini 3 Pro Image: high-fidelity generation, Search grounding, SynthID, 2K/4K. | 2026-06-06 |
| [[How Nano Banana Got Its Name]] | #summary | LMArena codename origin from PM Naina Raisinghani; Gemini 2.5 Flash Image brand. | 2026-06-06 |
| [[Nano Banana 2]] | #summary | Gemini 3.1 Flash Image (Feb 26 2026): Flash speed, 512px tier, web search grounding. | 2026-06-06 |
| [[Gemini 3.1 Pro]] | #summary | Google Feb 2026 reasoning upgrade: 77.1% ARC-AGI-2; preview in API, Antigravity, Vertex, Gemini app, NotebookLM. | 2026-06-06 |
| [[Gemini 3.1 Flash Lite]] | #summary | Google Mar 2026 cost tier: $0.25/$1.50 per M tokens, 1432 Arena Elo, high-volume workloads. | 2026-06-06 |
| [[Gemini 3.1 Flash Live]] | #summary | Google Mar 2026 real-time voice: ComplexFuncBench 90.8%, Search Live 200+ countries, SynthID. | 2026-06-06 |
| [[Gemini 3.1 Flash TTS]] | #summary | Google Apr 2026 TTS: audio tags, 70+ languages, Elo 1211 on TTS Arena, SynthID. | 2026-06-06 |
| [[Gemma 4]] | #summary | Google Apr 2026 open models: E2B/E4B/26B MoE/31B Dense, Gemini 3 stack, 140+ languages, vision+audio, agentic. | 2026-06-06 |
| [[Gemma 4 Multi-Token Prediction]] | #summary | Google May 2026 MTP drafters for Gemma 4: speculative decoding, KV cache sharing, up to 3× speedup. | 2026-06-06 |
| [[Gemma 4 12B]] | #summary | Google Jun 2026 encoder-free multimodal 12B: 16GB VRAM, native audio, near 26B MoE performance. | 2026-06-06 |
| [[Gemma 4 QAT]] | #summary | Google Jun 2026 QAT checkpoints: Q4_0 + mobile format, E2B under 1GB, MTP-compatible. | 2026-06-06 |
| [[Gemma 4 MTP Overview]] | #summary | Google ai.google.dev MTP architecture doc: shared embeddings, target activations, clustered LM head, MoE batching caveat. | 2026-07-12 |
| [[Gemma 4 MTP Transformers Guide]] | #summary | Google Hugging Face MTP tutorial: target + assistant models, `generate(assistant_model=...)`, heuristic draft scheduling. | 2026-07-12 |
| [[Gemma 4 Technical Report]] | #summary | arXiv:2607.02770 Gemma 4 technical report: architecture, thinking mode, QAT, MTP drafter §2.6, benchmarks. | 2026-07-12 |
| [[Gemma 4 MTP Explained in 5 Minutes]] | #summary | Jackson MZ Medium explainer: Gemma 4 MTP vs EAGLE/DeepSeek V3; stateless drafter KV design. | 2026-07-12 |
| [[Gemma4 Assistant Docs]] | #summary | HF Transformers `Gemma4AssistantForCausalLM` docs: shared KV, cross-attention, centroid LM head. | 2026-07-12 |
| [[A Visual Guide to Gemma 4]] | #summary | Maarten Grootendorst illustrated Gemma 4 architecture + MTP section (Substack, Apr 2026). | 2026-07-12 |
| [[Maarten Grootendorst]] | #entity | Google DeepMind; BERTopic creator; Gemma 4 visual guide author and core contributor. | 2026-07-12 |
| [[DiffusionGemma]] | #summary | Google Jun 2026 experimental open text-diffusion MoE: 4× local GPU decode, 256-token parallel canvas, Apache 2.0. | 2026-06-11 |
| [[Gemini 3.5 Flash]] | #summary | Google I/O 2026: frontier agentic/coding Flash model; Terminal-Bench 2.1 76.2%, 4× frontier speed; Antigravity subagents, Gemini Spark. | 2026-06-06 |
| [[Introducing Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber]] | #summary | Google Jul 2026: 3.6 Flash workhorse, 3.5 Flash-Lite throughput tier, 3.5 Flash Cyber in CodeMender. | 2026-07-22 |
| [[CodeMender]] | #entity | Google multi-agent code-security system using Gemini 3.5 Flash Cyber; limited pilot for governments/trusted partners. | 2026-07-22 |
| [[Gemini Omni Flash]] | #summary | Google I/O 2026: video from any input; conversational editing; physics reasoning; SynthID; Avatars. | 2026-06-06 |
| [[T5Gemma 2]] | #summary | Google Dec 2025 encoder-decoder from Gemma 3: tied embeddings, merged attention, multimodal, 128K context. | 2026-06-06 |
| [[FunctionGemma]] | #summary | Google Dec 2025 Gemma 3 270M function-calling specialist for edge agents; 58%→85% after fine-tuning. | 2026-06-06 |
| [[Claude Models]] | #summary | Anthropic Claude timeline Mar 2023–Jun 2026: Opus/Sonnet/Haiku through Fable 5 / Mythos 5 and Sonnet 5; computer use, extended thinking, Claude Code. | 2026-07-12 |
| [[Anthropic]] | #entity | AI safety company; Constitutional AI; Claude model family and platform. | 2026-06-06 |
| [[Project Glasswing]] | #concept | Anthropic-led cyberdefense initiative deploying Mythos-class models to vetted partners. | 2026-06-09 |
| [[Claude Fable Safeguards]] | #concept | Domain-routing safeguards releasing Mythos-class Fable 5 broadly; cyber/bio queries → Opus 4.8. | 2026-06-09 |
| [[Cyber Verification Program]] | #concept | Anthropic opt-in program for reduced cyber guardrails on vetted security research orgs. | 2026-07-12 |
| [[OpenAI]] | #entity | AI research and product company; GPT model family, ChatGPT, Codex; Preparedness Framework system cards. | 2026-07-10 |
| [[GPT-5]] | #summary | Aug 2025 OpenAI flagship: unified router across gpt-5-main and gpt-5-thinking; safe-completions training. | 2026-07-10 |
| [[GPT-5.1]] | #summary | Nov 2025: warmer default tone, adaptive Instant reasoning, personality presets; GPT-5.1-Codex-Max. | 2026-07-10 |
| [[GPT-5.2]] | #summary | Dec 2025: GDPval-focused knowledge-work gains; GPT-5.2-Codex agentic coding update. | 2026-07-10 |
| [[GPT-5.3]] | #summary | Feb-Mar 2026: GPT-5.3-Codex family, GPT-5.3-Codex-Spark, GPT-5.3 Instant. | 2026-07-10 |
| [[GPT-5.4]] | #summary | Mar 2026: first general-purpose OpenAI model with High cybersecurity mitigations. | 2026-07-10 |
| [[GPT-5.5]] | #summary | Apr 2026: GB200/GB300-co-designed inference; High Bio/Chem and Cyber; GPT-5.5 Instant. | 2026-07-10 |
| [[How Two Settings Tripled Our ARC-AGI-3 Scores]] | #summary | OpenAI: retained reasoning + compaction on Responses API raised GPT-5.6 Sol ARC-AGI-3 from 13.3% to 38.3%. | 2026-07-31 |
| [[GPT-5.6]] | #summary | Jul 2026 GA: Sol/Terra/Luna family, ChatGPT Work, updated safety card; Luna/Terra price cuts Jul 30. | 2026-07-31 |
| [[GPT-Live]] | #summary | OpenAI full-duplex voice models GPT-Live-1 and GPT-Live-1 mini; continuous listen-and-respond conversation. | 2026-07-10 |
| [[Sora 2]] | #summary | OpenAI video and audio generation model with synchronized dialogue and sound effects; social Sora app. | 2026-07-10 |
| [[ChatGPT Images 2.0]] | #summary | OpenAI ChatGPT image-generation update: improved text rendering, editing consistency, prompt adherence. | 2026-07-10 |
| [[OpenAI Privacy Filter]] | #summary | Official OpenAI page for the bidirectional token-classification PII detection and redaction model. | 2026-07-10 |
| [[gpt-oss-safeguard]] | #summary | Open-weight safety-reasoning models fine-tuned from gpt-oss; classify content against a supplied policy at inference time. | 2026-07-10 |
| [[Instruction Hierarchy Challenge]] | #summary | OpenAI benchmark and dataset testing whether models follow system > developer > user > tool instruction priority. | 2026-07-10 |
| [[Model Disproves Discrete Geometry Conjecture]] | #summary | OpenAI research post: GPT-5 contributed to disproving a discrete-geometry conjecture. | 2026-07-10 |
| [[New Result in Theoretical Physics]] | #summary | OpenAI research post on a GPT-5-assisted theoretical-physics result. | 2026-07-10 |
| [[Where the Goblins Came From]] | #summary | OpenAI research post on reward-signal generalization producing reward hacking. | 2026-07-10 |
| [[Ten Advances in Mathematics and Theoretical Computer Science]] | #summary | OpenAI announcement: internal Astra model proofs for ten open math/TCS problems; Lean certificates; ~$2k inference cost. | 2026-08-01 |
| [[How the Ideas Came Together]] | #summary | Proof-discovery narratives for the ten Astra math results; AI-reconstructed reasoning paths. | 2026-08-01 |
| [[Astra]] | #entity | Internal OpenAI reasoning model previewed to regulators; generated the ten math/TCS proofs. | 2026-08-01 |
| [[Separating Signal From Noise in Coding Evaluations]] | #summary | OpenAI audit finding about 30% of SWE-Bench Pro's public-split tasks broken; contamination and grading-noise fixes. | 2026-07-10 |
| [[Why We No Longer Evaluate SWE-bench Verified]] | #summary | OpenAI stopped reporting SWE-bench Verified after finding flawed tests and cross-provider training contamination. | 2026-07-10 |
| [[Chain of Thought Controllability]] | #summary | OpenAI research post on reasoning models trained to keep chain-of-thought in a target language or format. | 2026-07-10 |
| [[IndQA]] | #summary | OpenAI benchmark for model quality across Indian languages and culturally grounded knowledge. | 2026-07-10 |
| [[Instruction Hierarchy]] | #concept | OpenAI training scheme resolving instruction conflicts in system > developer > user > tool priority order. | 2026-07-10 |
| [[Preparedness Framework]] | #concept | OpenAI risk-assessment framework covering Biological/Chemical, Cybersecurity, and AI Self-Improvement categories. | 2026-07-10 |
| [[GDPval]] | #concept | OpenAI benchmark of real-world economically valuable tasks graded holistically by domain experts. | 2026-07-10 |
| [[Chain of Thought Monitorability]] | #concept | Using a model's visible reasoning trace as a safety-monitoring signal to catch misbehavior before the final answer. | 2026-07-10 |
| [[Full-Duplex Voice]] | #concept | Continuous-listening voice models that decide in the moment whether to respond or keep listening. | 2026-07-10 |
| [[A Foundation Model for Entity Recognition]] | #summary | NuMind Nov 2023 BERT-size NER foundation model: LLM 80k-concept C4 labels, 6× data efficiency, MIT weights. | 2026-06-12 |
| [[NuExtract: A Foundation Model for Structured Extraction]] | #summary | NuMind Jun 2024 text-to-JSON NuExtract 1.0 (0.5B–7B): GPT-4o-class zero-shot at 100× smaller; Llama 3 synthetic C4 data. | 2026-06-12 |
| [[NuExtract 1.5 — Multilingual, Infinite context, still small, and better than GPT-4o!]] | #summary | NuMind Oct 2024 Phi-3.5 extraction: multilingual C4, continuation infinite context, beats GPT-4o English zero-shot. | 2026-06-12 |
| [[NuExtract 2.0: Outclassing Frontier LLMs in Information Extraction]] | #summary | NuMind Jul 2025 VLM extraction 2B–8B + PRO: vision, typed templates, ICL; +9 F-Score vs GPT-4.1. | 2026-06-12 |
| [[NuExtract3: The Reasoning Open-Source OCR & Structured Extraction LLM]] | #summary | NuMind May 2026 Qwen3.5-4B VLM: unified JSON + Markdown OCR, SFT+RL toggleable reasoning, 20 field types. | 2026-06-12 |
| [[NuMind]] | #entity | French extraction specialist; NuExtract/NuNER open models and nuextract.ai platform. | 2026-06-12 |
| [[NuExtract]] | #entity | NuMind document-to-JSON (and v3 OCR) model family from 1.0 through 3.0. | 2026-06-12 |
| [[Structured Extraction]] | #concept | Hierarchical template/schema filling from documents; NuExtract core task. | 2026-06-12 |
| [[Task-Specific Foundation Models]] | #concept | Small task-specialized models from corpus + LLM labels + fine-tune; NuMind recipe. | 2026-06-12 |
| [[Papers Explained 574: Jina Embeddings v5 Omni]] | #summary | GELATO omni embeddings: locked Qwen vision/audio towers on Jina v5 Text; sub-5B SOTA four-modality score. | 2026-06-13 |
| [[Papers Explained 575: Gemini Embedding 2]] | #summary | Google native Gemini multimodal embedder (3072-d, MRL); leads retrieval and native-audio vs ASR. | 2026-06-13 |
| [[Papers Explained 576: Aryabhata 2]] | #summary | PhysicsWallah 20B JEE/NEET STEM model; GRPO on 1.25M verified questions; 88.95% in-distribution. | 2026-06-13 |
| [[Papers Explained 577: MAI-Thinking-1]] | #summary | Microsoft 35B-active/1T MoE from-scratch reasoning; specialist RL climbs + self-distillation. | 2026-06-13 |
| [[Papers Explained 579: Policy-Aware Rubric Reward (POW3R)]] | #summary | Dynamic rubric-criterion reweighting for RLVR; 24/30 metric wins vs static rubric rewards. | 2026-06-13 |
| [[Papers Explained 580: Nemotron 3 Ultra]] | #summary | NVIDIA 550B/55B-active Hybrid Mamba-MoE; 20T pre-train, 1M context, RLVR + MOPD teachers. | 2026-06-13 |
| [[Papers Explained 581: Rubric-Guided Self-Distillation]] | #summary | Verifier-free rubric-conditioned self-distillation; matches GRPO without train-time judge calls. | 2026-06-21 |
| [[Papers Explained 582: Mellum]] | #summary | JetBrains 4B IDE code completion; project-context FIM + DPO on 4T permissive tokens. | 2026-06-21 |
| [[Papers Explained 583: Mellum 2]] | #summary | JetBrains 12B/2.5B-active MoE coding agent; SFT + multi-domain RLVR with MTP speculative decoding. | 2026-06-21 |
| [[Papers Explained 584: VibeThinker-1.5B]] | #summary | Spectrum-to-Signal SFT diversity + MGPO; AIME25 74.4 at 1.5B from Qwen2.5-Math base. | 2026-06-21 |
| [[Papers Explained 585: VibeThinker-3B]] | #summary | Scaled SSP at 3B; AIME26 97.1, LiveCodeBench v6 80.2, LeetCode OOD 96.1% first-attempt. | 2026-06-21 |
| [[JetBrains]] | #entity | IDE tools company; Mellum open-weight code completion and agentic coding models. | 2026-06-21 |
| [[Mellum]] | #entity | JetBrains code model family: 4B FIM completion and 12B MoE agentic successor. | 2026-06-21 |
| [[VibeThinker]] | #entity | Compact reasoning models (1.5B/3B) trained with Spectrum-to-Signal + MGPO. | 2026-06-21 |
| [[RubricHub]] | #entity | Medical/science rubric-graded generation benchmark and training corpus. | 2026-06-21 |
| [[Rubric-Guided Self-Distillation]] | #concept | Rubric-conditioned frozen teacher distills into unconditioned student; no train-time judges. | 2026-06-21 |
| [[Spectrum-to-Signal Principle]] | #concept | SFT maximizes solution diversity (Pass@K); RL amplifies correct signal (Pass@1). | 2026-06-21 |
| [[Jina AI]] | #entity | Embedding/search company; jina-embeddings-v5-omni and GELATO. | 2026-06-13 |
| [[PhysicsWallah]] | #entity | Indian ed-tech; Aryabhata 2 STEM reasoning model. | 2026-06-13 |
| [[NVIDIA]] | #entity | GPU and Nemotron model family; Nemotron 3 Ultra technical report. | 2026-06-13 |
| [[Ettin Suite: SoTA Paired Encoders and Decoders]] | #summary | JHU CLSP encoder/decoder twins at 6 matched sizes, identical data/recipe; encoders beat ModernBERT, decoders beat Llama 3.2/SmolLM2. | 2026-07-10 |
| [[Introducing the Ettin Reranker Family]] | #summary | Six Sentence Transformers CrossEncoder rerankers distilled from mxbai-rerank-large-v2 onto Ettin encoder backbones; SoTA at size, up to 2.3x faster via unpadded FA2. | 2026-07-10 |
| [[Introducing RTEB: A New Standard for Retrieval Evaluation]] | #summary | MTEB/MongoDB paired open+private retrieval benchmark to catch models overfit to public leaderboards. | 2026-07-10 |
| [[Granite Embedding Multilingual R2]] | #summary | IBM 97M/311M ModernBERT-based multilingual embedders, 32K context, Matryoshka on the 311M; +9.4 pt gain over multilingual-e5-small at sub-100M. | 2026-07-10 |
| [[Build a Domain-Specific Embedding Model in Under a Day]] | #summary | NVIDIA nemotron-embed CLI: synthetic QA generation + hard-negative mining + contrastive fine-tune, no manual labels, ~10% NDCG@10 gain. | 2026-07-10 |
| [[Hugging Face]] | #entity | Open-source AI platform; Hub, transformers, Sentence Transformers, and the huggingface.co/blog technical blog. | 2026-07-10 |
| [[IBM]] | #entity | Enterprise AI research org; Granite dense/MoE language and embedding model family. | 2026-07-10 |
| [[Gemma 3n fully available in the open-source ecosystem!]] | #summary | Google's on-device natively multimodal Gemma (image/text/audio/video); MatFormer nested sub-models, Per-Layer Embeddings, MobileNet-V5 vision encoder. | 2026-07-10 |
| [[nanoVLM: The simplest repository to train your VLM in pure PyTorch]] | #summary | Hugging Face minimal from-scratch VLM training codebase; SigLIP + SmolLM2, trained on Colab-friendly hardware. | 2026-07-10 |
| [[SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data]] | #summary | 450M open VLA for robotics; SmolVLM2 backbone + flow-matching action expert; async inference stack. | 2026-07-10 |
| [[Welcome the NVIDIA Llama Nemotron Nano VLM to Hugging Face Hub]] | #summary | 8B document-intelligence VLM; Llama-3.1-8B + C-RADIOv2-VLM-H; leads OCRBench v2. | 2026-07-10 |
| [[Granite 4.0 3B Vision: Compact Multimodal Intelligence for Enterprise Documents]] | #summary | IBM LoRA-adapter VLM on Granite 4.0 Micro; ChartNet dataset, DeepStack injection; table/chart/KVP extraction. | 2026-07-10 |
| [[DeepSeek-V4: A Million-Token Context That Agents Can Actually Use]] | #summary | 1.6T/49B-active + 284B/13B-active MoE; CSA/HCA hybrid attention, 1M context at ~2% GQA's KV cache; agent-focused post-training (DSML, DSec). | 2026-07-10 |
| [[Welcome Llama 4 Maverick & Scout on Hugging Face]] | #summary | Meta's ~400B/17B-active Maverick and ~109B/17B-active Scout; natively multimodal MoE; iRoPE (NoPE + chunked RoPE) gives 1M/10M context. | 2026-07-10 |
| [[GLM-5.2: Built for Long-Horizon Tasks]] | #summary | Z.ai 753B flagship; IndexShare-shared DSA indexer (2.9x FLOPs cut at 1M ctx), +20% MTP acceptance length, critic-based PPO, anti-reward-hacking module. | 2026-07-10 |
| [[Granite 4.1 LLMs: How They're Built]] | #summary | IBM dense 3B/8B/30B; 5-phase pretrain to 512K context, LLM-as-Judge SFT, 4-stage GRPO+DAPO RL; 8B dense matches a 32B-A9B MoE predecessor. | 2026-07-10 |
| [[Granite 4.0 Nano: Just How Small Can You Go?]] | #summary | IBM sub-1B/1B edge models, hybrid-SSM and traditional-transformer variants, for on-device and llama.cpp deployment. | 2026-07-10 |
| [[StarCoder2 and The Stack v2]] | #summary | BigCode 3B/7B/15B open code LLMs on The Stack v2 (~900B tokens, 600+ languages); GQA, FIM, sliding-window attention. | 2026-07-10 |
| [[StarCoder2-Instruct: Fully Transparent and Permissive Self-Alignment for Code Generation]] | #summary | Fully self-aligned instruction tuning, no human/proprietary-LLM data; 72.6 HumanEval, beats CodeLlama-70B-Instruct. | 2026-07-10 |
| [[Meta]] | #entity | Developer of the Llama open-weight model family; Llama 4 shifted to MoE + native multimodality. | 2026-07-10 |
| [[Z.ai]] | #entity | GLM model family developer (formerly Zhipu AI); GLM-5.2 flagship long-horizon agentic coding model. | 2026-07-10 |
| [[Open-R1: A Fully Open Reproduction of DeepSeek-R1]] | #summary | Hugging Face's project to reconstruct DeepSeek-R1's missing training data and RL pipeline in the open. | 2026-07-10 |
| [[Open R1: Update #1]] | #summary | MATH-500 reproduction across R1-Distill models; GRPO lands in TRL 0.14; vLLM streaming-request throughput fixes. | 2026-07-10 |
| [[Open R1: Update #2]] | #summary | OpenR1-Math-220k dataset (800k R1 traces, Math-Verify + LLM-judge filtering); OpenR1-Qwen-7B near-matches R1-Distill-7B. | 2026-07-10 |
| [[Open R1: Update #3]] | #summary | CodeForces-CoTs dataset, IOI 2024 contest eval, OlympicCoder models; exposes a code-verifiability crisis in public test cases. | 2026-07-10 |
| [[Open R1: Update #4]] | #summary | DeepSeek-V3-0324 base-model refresh (MIT license, capability deltas) plus open-model usage/safety guidance. | 2026-07-10 |
| [[Mini-R1: Reproduce Deepseek R1 "Aha Moment", a RL Tutorial]] | #summary | Small-scale GRPO reproduction of R1's self-reflective reasoning shift on the Countdown Game, Qwen2.5-3B-Instruct. | 2026-07-10 |
| [[DeepMath: A Lightweight Math Reasoning Agent With Smolagents]] | #summary | Intel's GRPO-trained Qwen3-4B Thinking agent offloading arithmetic to a sandboxed Python executor via smolagents. | 2026-07-10 |
| [[Kimina-Prover: Applying Test-Time RL Search on Large Formal Reasoning Models]] | #summary | Numina/Kimi Lean 4 theorem prover; TTRL Search + error-fixing reach 92.2% pass rate on miniF2F. | 2026-07-10 |
| [[Kimina-Prover-RL]] | #summary | Open-source, Verl-compatible DrGRPO pipeline reproducing Kimina-Prover's methodology at 0.6B-1.7B scale. | 2026-07-10 |
| [[Putting RL Back in RLHF]] | #summary | Cohere's RLOO (critic-free, leave-one-out baseline) shipped as TRL's RLOO Trainer; 50-70% less VRAM, 2-3x faster than PPO. | 2026-07-10 |
| [[Keep the Tokens Flowing: Lessons From 16 Open-Source RL Libraries]] | #summary | Survey of 16 async RL libraries across orchestration, buffers, weight sync, staleness, LoRA, and MoE parallelism, informing TRL's async trainer. | 2026-07-10 |
| [[OpenEnv in Practice: Evaluating Tool-Using Agents in Real-World Environments]] | #summary | Meta/HF/Turing OpenEnv framework; Calendar Gym shows agents drop from ~90% to ~40% success under ambiguous phrasing. | 2026-07-10 |
| [[PipelineRL]] | #summary | ServiceNow's inflight-weight-update RL trainer decoupling inference throughput from on-policy data freshness. | 2026-07-10 |
| [[Apriel-H1: The Surprising Key to Distilling Efficient Reasoning Models]] | #summary | ServiceNow distills a 15B reasoning model into a Mamba hybrid (2.1x throughput); SFT reasoning traces, not pretraining data, preserve quality. | 2026-07-10 |
| [[ServiceNow]] | #entity | Enterprise platform company; SLAM Lab builds PipelineRL and Apriel-H1 efficient reasoning research. | 2026-07-10 |
| [[Turing]] | #entity | AI data/evaluation company; contributed the Calendar Gym environment to Meta/Hugging Face's OpenEnv. | 2026-07-10 |
| [[Numina]] | #entity | AI-for-math research group (AI-MO); NuminaMath and the Kimina-Prover Lean 4 theorem-prover family. | 2026-07-10 |
| [[Intel]] | #entity | Intel AI Software Group; DeepMath GRPO-trained math reasoning agent. | 2026-07-10 |
| [[Profiling in PyTorch (Part 1): A Beginner's Guide to torch.profiler]] | #summary | Introduces `torch.profiler` table/trace reading via a minimal matmul-add example; overhead-bound vs. compute-bound regimes, `torch.compile`'s addmm fusion. | 2026-07-10 |
| [[Profiling in PyTorch (Part 2): From nn.Linear to a Fused MLP]] | #summary | Profiles `nn.Linear`'s fused addmm epilogue and a GeGLU MLP; `torch.compile` fuses GeLU+multiply into one Triton kernel, matched by a hand-tuned Liger kernel. | 2026-07-10 |
| [[Profiling in PyTorch (Part 3): Attention Is All You Profile]] | #summary | Profiles SDPA's math/efficient/flash/cuDNN backends; math is 3.7x slower on 20 kernels, flash's low occupancy is by design, cuDNN moves cost to the CPU. | 2026-07-10 |
| [[Tricks From OpenAI gpt-oss You Can Use With Transformers]] | #summary | `transformers` upgrades for gpt-oss: Hub-downloaded kernels, MXFP4 quantization, Tensor/Expert Parallelism, sliding-window KV cache, faster model loading. | 2026-07-10 |
| [[Native-Speed vLLM Transformers Modeling Backend]] | #summary | `torch.fx`-based runtime layer fusion makes the `transformers` vLLM backend match native throughput on dense and 235B MoE Qwen3 models. | 2026-07-10 |
| [[Efficient MultiModal Data Pipeline]] | #summary | nanoVLM rewrites multimodal batching as a knapsack-packing problem, cutting ~60% padding waste and balancing per-batch image counts. | 2026-07-10 |
| [[Prefill and Decode for Concurrent Requests - Optimizing LLM Performance]] | #summary | TNG's production analysis of prefill/decode scheduling; chunked prefill lifts total throughput +50% over prefill-first continuous batching. | 2026-07-10 |
| [[TNG Technology Consulting]] | #entity | German IT consultancy self-hosting a 24-H100 LLM inference cluster; publishes an LLM-serving-performance blog series. | 2026-07-10 |
| [[Beyond LoRA: Can You Beat the Most Popular Fine-Tuning Technique?]] | #summary | HF PEFT team benchmarks 40+ PEFT methods on equal footing; LoRA sits on the Pareto frontier but OFT strictly dominates it on image-gen. | 2026-07-10 |
| [[Differential Transformer V2]] | #summary | Microsoft's DIFF V2 doubles only query heads (not KV), dropping per-head RMSNorm; matches FlashAttention speed, lower loss and fewer spikes at scale. | 2026-07-10 |
| [[Introducing SynthID Text]] | #summary | Google DeepMind + HF text watermarking via tournament sampling; ships in `transformers` v4.46.0 as a `generate()` config. | 2026-07-10 |
| [[Introducing the Synthetic Data Generator - Build Datasets with Natural Language]] | #summary | No-code Argilla/`distilabel` tool: prompt to classification/chat dataset to AutoTrain model in three steps. | 2026-07-10 |
| [[Neural Super Sampling Is Here!]] | #summary | Arm's mobile temporal upscaling model; 50% GPU workload cut, 540p→1080p in 4ms; ships via two Unreal Engine plugins. | 2026-07-10 |
| [[Open-Source DeepResearch - Freeing Our Search Agents]] | #summary | HF's 24h open reproduction of OpenAI Deep Research via a `smolagents` code agent; 55.15% on GAIA vs. 33% for the same setup in JSON. | 2026-07-10 |
| [[Harness, Scaffold, and the AI Agent Terms Worth Getting Right]] | #summary | HF glossary formalizing agent/harness/scaffold/policy/rollout/reward/rubric vocabulary post-ICLR 2026. | 2026-07-10 |
| [[AprielGuard: A Guardrail for Safety and Adversarial Robustness in Modern LLM Systems]] | #summary | ServiceNow's 8B unified safety+adversarial guardrail across prompts, chats, and agentic workflows; reasoning and fast modes. | 2026-07-10 |
| [[Nemotron 3.5 Content Safety: Customizable Multimodal Safety for Global Enterprise AI]] | #summary | NVIDIA's 4B Gemma-3-based multimodal/multilingual safety classifier with custom-policy enforcement and THINK-mode reasoning traces. | 2026-07-10 |
| [[NVIDIA Cosmos Reason 2 Brings Advanced Reasoning to Physical AI]] | #summary | 2B/8B open reasoning VLM for physical AI; 256K context, OCR/trajectory output; #1 on Physical AI Bench. | 2026-07-10 |
| [[Arm]] | #entity | Semiconductor/mobile-GPU design company; develops Neural Accelerators (NX) and Neural Super Sampling. | 2026-07-10 |
| [[Data for Agents]] | #summary | NVIDIA Nemotron essay: agentic AI needs open (synthetic) data; introduces the Post-Training v3 Prompt Atlas and Nemotron-Personas. | 2026-07-10 |
| [[Introducing NVIDIA Nemotron 3 Nano Omni: Long-Context Multimodal Intelligence for Documents, Audio and Video Agents]] | #summary | Hybrid Mamba-Transformer-MoE + C-RADIOv4-H + Parakeet-TDT omni model; leads document/video/audio benchmarks, 9.2x system efficiency. | 2026-07-10 |
| [[The Open Evaluation Standard: Benchmarking NVIDIA Nemotron 3 Nano with NeMo Evaluator]] | #summary | NVIDIA publishes the exact NeMo Evaluator YAML config + artifacts behind Nemotron 3 Nano's model-card benchmark numbers. | 2026-07-10 |
| [[Nemotron-Personas-India: Synthesized Data for Sovereign AI]] | #summary | 21M-persona synthetic Indic dataset (7.7B tokens, CC BY 4.0) via NeMo Data Designer, grounded in 2011 Census distributions. | 2026-07-10 |
| [[NVIDIA Releases 6 Million Multi-Lingual Reasoning Dataset]] | #summary | Nemotron Post-Training Dataset v2 translates English reasoning data into 5 languages; co-launches Nemotron Nano 2 9B. | 2026-07-10 |
| [[State of Open Source on Hugging Face: Spring 2026]] | #summary | HF's ecosystem retrospective: China overtakes US in downloads (41%), Qwen's 113k+ derivatives, robotics now the top dataset category. | 2026-07-10 |
| [[One Year Since the "DeepSeek Moment"]] | #summary | First of 3: how R1's MIT license lowered technical/adoption/psychological barriers, triggering China's open-source surge. | 2026-07-10 |
| [[Architectural Choices in China's Open-Source AI Ecosystem: Building Beyond DeepSeek]] | #summary | Second of 3: MoE-as-default, Apache 2.0 licensing, and the shift to domestic-hardware-first training/serving (Ascend, Cambricon, Kunlun). | 2026-07-10 |
| [[The Future of the Global Open-Source AI Ecosystem: From DeepSeek to AI+]] | #summary | Third of 3: Alibaba/Tencent/ByteDance/Baidu trajectories; China's "AI+" plan and ~1590 EFLOPS compute buildout. | 2026-07-10 |
| [[Inkling]] | #summary | Thinking Machines 975B/41B-active open MoE: encoder-free multimodal, relative attention, controllable thinking effort, Tinker fine-tuning. | 2026-07-31 |
| [[Inkling-Small]] | #summary | 276B/12B-active efficient Inkling family member; on-policy distillation from Inkling; strong reasoning/agentic at lower cost. | 2026-07-31 |
| [[Tinker]] | #entity | Thinking Machines fine-tuning, distillation, and RL platform for open-weights models. | 2026-07-31 |
| [[Relative Attention]] | #concept | Inkling's learned position bias replacing RoPE; pairs with SWA-heavy hybrid attention. | 2026-07-31 |
| [[Controllable Thinking Effort]] | #concept | Runtime `reasoning_effort` knob trading tokens for performance on Inkling-family models. | 2026-07-31 |
| [[Controlling Reasoning Effort in LLMs]] | #summary | Sebastian Raschka survey of reasoning-effort modes: RLVR recap, think tokens, effort-conditioned SFT/RLVR, six open-weight recipes. | 2026-07-21 |
| [[Harness Engineering for Self-Improvement]] | #summary | Lilian Weng survey of harness design patterns, self-improving harness loops, and evolutionary program search for RSI. | 2026-07-21 |
| [[Uncensor any LLM with abliteration]] | #summary | Maxime Labonne tutorial on refusal-direction ablation, weight orthogonalization, and DPO healing of abliterated models. | 2026-07-21 |
| [[Reasoning Effort]] | #concept | Low/med/high or continuous effort labels; system-prompt control and token-penalty RLVR for reasoning models. | 2026-07-21 |
| [[Think Tokens]] | #concept | `<think>` delimiters mark reasoning traces; format reward during RLVR, not reasoning ability itself. | 2026-07-21 |
| [[Thinking Mode Fusion]] | #concept | Qwen3 mixed SFT on thinking/non-thinking examples; empty thinking-block prefill as hard switch. | 2026-07-21 |
| [[Reasoning Budget]] | #concept | Hard inference-time cap on thinking tokens; budget-aware SFT and Toggle RL training. | 2026-07-21 |
| [[Recursive Self-Improvement]] | #concept | AI improving training/deployment machinery (harnesses), not only model weights; Good/Yudkowsky framing. | 2026-07-21 |
| [[Self-Improving Harness]] | #concept | Harness that edits its own prompts/tools/workflow via propose-evaluate-accept loops with regression guards. | 2026-07-21 |
| [[Agentic Context Engineering]] | #concept | ACE generator/reflector/curator playbook; extends to MCE and Meta-Harness meta-optimization. | 2026-07-21 |
| [[Evolutionary Program Search]] | #concept | STOP, AlphaEvolve, DGM, ADAS, AFlow as code-space evolutionary search over agents and harnesses. | 2026-07-21 |
| [[Abliteration]] | #concept | Remove refusal by ablating a residual-stream direction without retraining; fragility of safety fine-tuning. | 2026-07-21 |
| [[Refusal Direction]] | #concept | Mean-difference vector in residual activations mediating LLM refusal (Arditi et al. 2024). | 2026-07-21 |
| [[Weight Orthogonalization]] | #concept | Permanent weight edit blocking writes along the refusal direction (`W_E`, `W_O`, `W_out`). | 2026-07-21 |
| [[Maxime Labonne]] | #entity | HF ML educator; abliteration tutorial, LLM Course, model merging, NeuralDaredevil-8B. | 2026-07-21 |
| [[Unsloth Origins and Mission]] | #summary | Unsloth founding story: YC backing, 30× speed claims, Triton kernels, PyTorch Ecosystem. | 2026-07-22 |
| [[Unsloth Model Support 2024]] | #summary | 2024 model launches: Mistral, Gemma, Llama 3 family, Phi-3, HF TRL integration. | 2026-07-22 |
| [[Unsloth Model Support 2025]] | #summary | 2025 launches: DeepSeek R1/V3, Qwen3, Gemma 3/3n, Llama 4, GPT-OSS, GRPO. | 2026-07-22 |
| [[Unsloth Model Support 2026]] | #summary | 2026 docs: Qwen3.5/3.6, Gemma 4, DiffusionGemma, DeepSeek V4, GLM-5.2. | 2026-07-22 |
| [[Unsloth Model Bug Fixes]] | #summary | Day-zero upstream fixes: Gemma BOS/EOS, RoPE float32, softcapping, chat templates. | 2026-07-22 |
| [[Unsloth Dynamic Quantization]] | #summary | Dynamic 4-bit, R1 1.58-bit, Dynamic 2.0 GGUF selective-layer quantization. | 2026-07-22 |
| [[Unsloth Quantization-Aware Training]] | #summary | Fake-quant QAT workflows; Gemma 4 QAT; TorchAO/ExecuTorch export. | 2026-07-22 |
| [[Unsloth Long Context Training]] | #summary | Async checkpointing, Flex Attention, attention sinks, 500K Tiled MLP training. | 2026-07-22 |
| [[Unsloth Training Efficiency and Kernels]] | #summary | Gradient-accum fix, sample packing, faster MoE, NVIDIA collab, CPT. | 2026-07-22 |
| [[Unsloth Reinforcement Learning]] | #summary | GRPO/GSPO, memory-efficient RL, FP8 RL, VLM-RL, GPT-OSS reward hacking. | 2026-07-22 |
| [[Unsloth Specialized Model Training]] | #summary | TTS (Orpheus/CSM/Whisper), embeddings, DeepSeek-OCR fine-tuning. | 2026-07-22 |
| [[Unsloth Studio and Deployment]] | #summary | Studio UI, OpenAI-compatible API, Docker training images. | 2026-07-22 |
| [[Unsloth]] | #entity | Open-source LLM fine-tuning library; Triton kernels, QLoRA, GRPO, Studio. | 2026-07-22 |
| [[Daniel Han]] | #entity | Co-founder of Unsloth; kernel engineering lead. | 2026-07-22 |
| [[Michael Han]] | #entity | Co-founder of Unsloth; product and notebooks. | 2026-07-22 |
| [[PyTorch]] | #entity | Meta DL framework; Unsloth ecosystem partner, Flex Attention integration. | 2026-07-22 |
| [[Y Combinator]] | #entity | Startup accelerator that backed Unsloth. | 2026-07-22 |
| [[Zhipu AI]] | #entity | Stub cross-ref to Z.ai / GLM model family. | 2026-07-22 |
| [[Unsloth Gradient Checkpointing]] | #concept | Async checkpointing overlapping recompute with backward pass. | 2026-07-22 |
| [[Quantization-Aware Training]] | #concept | Fake-quant training for deployable INT4/FP8 weights. | 2026-07-22 |
| [[Flex Attention]] | #concept | PyTorch block-sparse attention API for custom masks. | 2026-07-22 |
| [[Attention Sinks]] | #concept | Sink tokens stabilizing sliding-window long-context attention. | 2026-07-22 |
| [[Cut Cross Entropy]] | #concept | Apple vocab-sliced CE avoiding full logits materialization. | 2026-07-22 |
| [[Gradient Accumulation]] | #concept | Micro-batch gradient scaling; Unsloth fixed HF loss bug. | 2026-07-22 |
| [[Sample Packing]] | #concept | Padding-free multi-sequence batches with block-diagonal masks. | 2026-07-22 |
| [[Tiled MLP]] | #concept | Sequence-sharded MLP for extreme long-context training memory. | 2026-07-22 |
| [[Continued Pretraining]] | #concept | Domain-adaptive pretrain from base checkpoints before SFT. | 2026-07-22 |
| [[DeepSeek V4]] | #concept | Stub cross-ref to DeepSeek-V4 HF blog and Unsloth docs. | 2026-07-22 |
| [[Llama 4 Release]] | #concept | Stub cross-ref to Welcome Llama 4 Maverick & Scout page. | 2026-07-22 |
| [[GLM-5.2 Blog]] | #concept | Stub cross-ref to GLM-5.2: Built for Long-Horizon Tasks. | 2026-07-22 |
| [[Diffusion Gemma]] | #concept | Stub cross-ref to DiffusionGemma summary page. | 2026-07-22 |
| [[Gemma 3n]] | #concept | Stub cross-ref to Gemma 3n open-source ecosystem post. | 2026-07-22 |
| [[Llama 3.3]] | #concept | Meta Llama 3.3 70B; Cut Cross Entropy integration. | 2026-07-22 |
| [[GGUF]] | #concept | Quantized weight format for llama.cpp/Ollama export. | 2026-07-22 |
| [[Embedding Models]] | #concept | Bi-encoders and rerankers; Unsloth SentenceTransformers QLoRA. | 2026-07-22 |
| [[Sentence Transformers]] | #concept | Embedding/reranker framework integrated with Unsloth. | 2026-07-22 |
| [[Docker]] | #concept | Containerized Unsloth CUDA training environments. | 2026-07-22 |
| [[vLLM]] | #concept | High-throughput LLM inference engine; Unsloth serving integration. | 2026-07-22 |
| [[Papers Explained 586: Gemma 4]] | #summary | Google natively multimodal family (E2B, E4B, 12B, 31B, 26B-A4B); PLE in flash, p-RoPE, encoder-free 12B, speculative MTP drafter. | 2026-08-23 |
| [[Per-Layer Embedding]] | #concept | Flash-resident layer-wise embedding vectors with learned gating to anchor token identity in deep LLMs. | 2026-08-23 |
| [[p-RoPE]] | #concept | Partial rotary position embedding (p=0.25 on global layers) cutting global KV cache by 37.5%. | 2026-08-23 |
| [[Papers Explained 587: OpenThoughts Agent]] | #summary | OpenThoughts 100K open agent data curation pipeline, 100+ ablations (sourcing, difficulty filtering, teacher selection), OpenThinker-Agent-v1 (44.8% on 7 benchmarks). | 2026-08-23 |
| [[OpenThoughts]] | #entity | Open-science research initiative for open data curation pipelines, datasets, and recipes for reasoning and agentic models. | 2026-08-23 |
| [[Agentic Data Curation]] | #concept | Empirical recipes for sourcing, filtering, instruction-rewriting, and RL training for tool-using language agents. | 2026-08-23 |
| [[Papers Explained 588: LLM-as-a-Verifier]] | #summary | Logprob-expectation continuous verification, Probabilistic Pivot Tournament (O(Nk)), and VOC progress metric. | 2026-08-23 |
| [[LLM-as-a-Verifier]] | #concept | Framework computing continuous trajectory rewards via logit expectations over score tokens. | 2026-08-23 |
| [[Probabilistic Pivot Tournament]] | #concept | Budget-efficient candidate selection via Hamiltonian ring passes and empirical pivot rounds. | 2026-08-23 |
| [[Value-Order Correlation]] | #concept | Spearman rank correlation between trajectory step index and verifier score. | 2026-08-23 |
| [[Papers Explained 589: Weak-to-Strong On-Policy Distillation]] | #summary | Weak-to-strong on-policy distillation dynamics, reverse-KL mode seeking, and error correction. | 2026-08-23 |
| [[Weak-to-Strong Distillation]] | #concept | Capability transfer from frontier teacher models to compact students via on-policy alignment. | 2026-08-23 |
| [[Papers Explained 590: Nemotron 3 Nano Omni]] | #summary | NVIDIA 3.2B native omni model for text, document vision, video, and real-time full-duplex speech. | 2026-08-23 |
| [[Nemotron 3 Nano Omni]] | #concept | NVIDIA compact omni-multimodal foundation model for edge text, vision, and speech. | 2026-08-23 |
| [[Papers Explained 591: Generalized Knowledge Distillation]] | #summary | GKD unified on-policy distillation framework, student rollouts, and generalized divergence metrics. | 2026-08-23 |
| [[Generalized Knowledge Distillation]] | #concept | Unified on-policy sequence distillation framework with customizable divergences. | 2026-08-23 |
| [[Papers Explained 592: Self-Distilled Reasoner]] | #summary | On-Policy Self-Distillation (OPSD), privileged teacher conditioning, and per-token KL clipping. | 2026-08-23 |
| [[Per-Token Pointwise Divergence Clipping]] | #concept | Clipping token-level divergence to stabilize on-policy self-distillation against stylistic spikes. | 2026-08-23 |
| [[Papers Explained 593: Self-Distillation Fine-Tuning]] | #summary | SDFT on-policy in-context teacher distillation preventing catastrophic forgetting in continual learning. | 2026-08-23 |
| [[Catastrophic Forgetting]] | #concept | Loss of pre-existing capabilities during sequential task fine-tuning. | 2026-08-23 |
| [[Continual Learning]] | #concept | Sequential model adaptation and cumulative skill acquisition without forgetting. | 2026-08-23 |
| [[Papers Explained 594: Teacher-Routed Exploration via Forward KL (TREK)]] | #summary | TREK teacher-routed exploration, Forward KL proposal learning, and reachability restoration. | 2026-08-23 |
| [[TREK]] | #concept | Teacher-routed exploration framework restoring policy reachability via Forward KL. | 2026-08-23 |
| [[Papers Explained 595: Unsupervised On-Policy Self-Distillation]] | #summary | U-OPSD label-free on-policy self-distillation via thinking-mode consensus and pseudo-labeling. | 2026-08-23 |
| [[Unsupervised On-Policy Self-Distillation]] | #concept | Label-free self-distillation distilling thinking-mode reasoning without external teachers. | 2026-08-23 |
| [[Papers Explained 596: Shieldstral]] | #summary | Mistral AI multimodal safety guardrail, contrastive sample curation, and low false-refusal moderation. | 2026-08-23 |
| [[Shieldstral]] | #concept | Mistral AI open-weights multimodal safety and content moderation model. | 2026-08-23 |
| [[Papers Explained 597: Leanstral]] | #summary | Mistral AI technical report on Leanstral 1.5, LeanGym environments, CISPO RL, and MiniF2F/PutnamBench SOTA. | 2026-08-23 |
| [[Papers Explained 598: Compress & Distil]] | #summary | Reasoning trace compression for efficient knowledge distillation and token reduction. | 2026-08-23 |
| [[Compress-Distill]] | #concept | Condensing verbose reasoning chains for efficient student knowledge distillation. | 2026-08-23 |
| [[Papers Explained 599: Sparse Upcycling]] | #summary | Google Research technique initializing sparse MoE models from dense checkpoints. | 2026-08-23 |
| [[Sparse Upcycling]] | #concept | Transforming dense checkpoints into sparse MoE architectures to reuse pretraining compute. | 2026-08-23 |
| [[Papers Explained 600: Rubric Dropout]] | #summary | Rubric Dropout regularization (30-50%) mitigating reward hacking in rubric-based RL. | 2026-08-23 |
| [[Rubric Dropout]] | #concept | Regularization masking random rubric criteria during RL to eliminate proxy judge gaming. | 2026-08-23 |
| [[Papers Explained: Attention with Linear Biases (ALiBi)]] | #summary | ALiBi linear attention biases enabling seamless zero-shot context length extrapolation. | 2026-08-23 |
| [[ALiBi]] | #concept | Attention with Linear Biases for zero-shot context length extrapolation in transformers. | 2026-08-23 |
| [[Papers Explained: CLRS and CLRS-Text Benchmark]] | #summary | DeepMind algorithmic reasoning benchmark covering 30+ classical algorithms and CLRS-Text. | 2026-08-23 |
| [[CLRS Benchmark]] | #entity | Algorithmic reasoning benchmark evaluating multi-step execution across classical algorithms. | 2026-08-23 |
| [[Papers Explained: Is One Layer Enough?]] | #summary | Systematic study of layer-wise reasoning contribution, Layer-Adaptive Learning Rate (LALR), and Layer-Selective Training. | 2026-08-23 |
| [[Layer-Adaptive Learning Rate]] | #concept | Depth-proportional learning rate scaling accelerating post-training convergence. | 2026-08-23 |
| [[Layer-Selective Training]] | #concept | Freezing early layers to cut post-training memory/compute by 50% without performance loss. | 2026-08-23 |
| [[Papers Explained: Kimi K2.5]] | #summary | Moonshot AI frontier multimodal MoE, Zero-Vision SFT, and Parallel Agent RL (PARL). | 2026-08-23 |
| [[Kimi K2.5]] | #concept | Moonshot AI frontier multimodal MoE model with agent swarm PARL training. | 2026-08-23 |
| [[Papers Explained: Kimi K3]] | #summary | Moonshot AI Kimi K3 with multi-teacher on-policy distillation and agentic sandboxes. | 2026-08-23 |
| [[Kimi K3]] | #concept | Moonshot AI reasoning and agentic model trained with multi-teacher distillation. | 2026-08-23 |
| [[Papers Explained: Low-Rank Training in Transformer LMs]] | #summary | Empirical study of low-rank pretraining, gradient rank dynamics, and rank annealing. | 2026-08-23 |
| [[Low-Rank Training]] | #concept | Factorized low-rank matrix training and rank annealing for transformer pretraining. | 2026-08-23 |
| [[Papers Explained: No Position Encoding (NoPE)]] | #summary | Demonstrating that causal masking implicitly encodes position, enabling robust length extrapolation without positional embeddings. | 2026-08-23 |
| [[NoPE]] | #concept | Causal transformer architecture without explicit positional encodings. | 2026-08-23 |
| [[Papers Explained: Passive Skill Distillation]] | #summary | Passive Skill Distillation transferring procedural tool skills from offline traces with 10x compute savings. | 2026-08-23 |
| [[Passive Skill Distillation]] | #concept | Distilling procedural and tool skills from passive logs without online rollouts. | 2026-08-23 |
| [[Papers Explained: Position Encodings in Transformers]] | #summary | Foundational survey covering Sinusoidal, Learned Absolute, and Shaw Relative Positional Encodings. | 2026-08-23 |
| [[Papers Explained: Rotary Position Embedding (RoPE)]] | #summary | Foundational paper on Rotary Position Embedding (RoPE), complex rotation geometry, and relative distance decay. | 2026-08-23 |
| [[RoPE]] | #concept | Rotary Position Embedding rotating Query/Key vectors in 2D complex subspaces. | 2026-08-23 |
| [[Papers Explained: Self-Optimization via Asymmetric RL (SOAR)]] | #summary | SOAR asymmetric bi-level RL self-optimization and automated curriculum generation for reasoning. | 2026-08-23 |
| [[SOAR]] | #concept | Asymmetric reinforcement learning self-optimization framework with automated curriculum. | 2026-08-23 |
| [[Papers Explained: Subproblem Curriculum Reinforcement Learning (SCRL)]] | #summary | SCRL subproblem DAG decomposition and progress-aware milestone rewards for long-horizon RL. | 2026-08-23 |
| [[SCRL]] | #concept | Subproblem curriculum reinforcement learning for complex multi-step reasoning. | 2026-08-23 |
| [[Papers Explained: TinyGSM]] | #summary | Microsoft 1.3B model scoring 81.5% on GSM8K via programmatic synthetic data curation. | 2026-08-23 |
| [[TinyGSM]] | #concept | Small language model achieving high mathematical reasoning via synthetic data. | 2026-08-23 |
| [[Papers Explained: TinyStories]] | #summary | Microsoft landmark study on linguistic emergence in tiny language models (1M-33M) via synthetic data. | 2026-08-23 |
| [[TinyStories]] | #concept | Synthetic dataset and framework demonstrating linguistic emergence in tiny transformers. | 2026-08-23 |
| [[Papers Explained: Unsupervised Process Reward Models]] | #summary | uPRM training step-level process reward models without human annotations via joint multi-trajectory scoring. | 2026-08-23 |
| [[Unsupervised Process Reward Models]] | #concept | Unsupervised process reward modeling for step-level reasoning verification. | 2026-08-23 |
| [[Papers Explained: Yet another RoPE extensioN method (YaRN)]] | #summary | YaRN compute-efficient RoPE context window extension via NTK-by-parts and attention temperature scaling. | 2026-08-23 |
| [[YaRN]] | #concept | Context window extension for RoPE combining NTK-by-parts interpolation and temperature scaling. | 2026-08-23 |
| [[Jianlin Su]] | #entity | AI researcher and mathematician, creator of Rotary Position Embedding (RoPE). | 2026-08-23 |
| [[Process Reward Models]] | #concept | Verifiers assigning step-by-step credit to intermediate reasoning tokens. | 2026-08-23 |
| [[Weak-to-Strong Generalization]] | #concept | Alignment and distillation paradigm transferring capabilities between asymmetric models. | 2026-08-23 |
| [[A Framework for Frontier AI and the Dawning of a New Age]] | #summary | Demis Hassabis's essay proposing a FINRA-style public-private Standards Body for frontier AI testing, pre-release review, and safety protocols. | 2026-08-23 |
| [[Demis Hassabis]] | #entity | CEO and co-founder of Google DeepMind, Nobel laureate in Chemistry (2024), and AI safety governance advocate. | 2026-08-23 |
| [[Standards Body for Frontier AI]] | #concept | FINRA-style public-private self-regulatory organization (SRO) for frontier model testing, held-out benchmarks, and coordinated development slowdowns. | 2026-08-23 |
| [[Financial Industry Regulatory Authority]] | #entity | Non-governmental self-regulatory organization (FINRA) regulating US financial markets; blueprint for frontier AI Standards Body. | 2026-08-23 |
| [[A Single Question to Track Progress from o3 to GPT-5.6 and Beyond]] | #summary | Sébastien Bubeck's essay tracking AI reasoning progression from o3 to GPT-5.6-pro via self-contracted gradient flows and long-horizon test-time compute. | 2026-08-23 |
| [[Sebastien Bubeck]] | #entity | AI researcher and mathematician at OpenAI, former VP AI at Microsoft, known for convex optimization, bandit theory, and empirical LLM evaluations. | 2026-08-23 |
| [[Self-Contracted Curves]] | #concept | Curves where distance to future points decreases monotonically; mathematical framework for convex gradient flow trajectories and arc length bounds. | 2026-08-23 |
| [[Gradient Flow on Convex Functions]] | #concept | Continuous-time gradient dynamics on convex potentials generating rectifiable self-contracted solution trajectories. | 2026-08-23 |
| [[Implications of Large-Scale Test-Time Compute]] | #summary | Noam Brown's essay analyzing why benchmark performance is a function of test-time compute, deceptive scalar grids, and compute-budgeted safety evaluations. | 2026-08-23 |
| [[Noam Brown]] | #entity | OpenAI researcher and pioneer in multi-agent game theory, search at test time, and reasoning models (Libratus, Pluribus, Cicero, o1, o3). | 2026-08-23 |
| [[AI Security Institute]] | #entity | UK state-backed frontier AI evaluation institute developing long-horizon, token-scaled cyber evaluations ("The Last Ones"). | 2026-08-23 |
| [[Zvi Mowshowitz]] | #entity | AI safety researcher, writer (Don't Worry About the Vase), and commentator on frontier model safety and governance. | 2026-08-23 |
| [[Test-Time Compute]] | #concept | Dynamic allocation of inference-time computation (extended chains, parallel sampling, MCTS, scaffolding) as an orthogonal scaling axis to pre-training. | 2026-08-23 |
| [[Inference-Budget Safety Evaluation]] | #concept | Safety evaluation methodology projecting misuse capabilities across low to state-actor ($10M+) compute budgets with explicit uncertainty bounds. | 2026-08-23 |
| [[ARC-AGI-2]] | #entity | Abstraction and reasoning benchmark evaluating grid puzzle generalization with cost-conditioned leaderboards. | 2026-08-23 |
| [[Andrej Karpathy]] | #entity | AI researcher and educator known for neural network education, nanoGPT, and autonomous autoresearch scaling experiments. | 2026-08-23 |
| [[What Even Is a Kernel?]] | #summary | Adam Mainz's visual guide to GPU kernel launches, eager-mode memory traffic, and `torch.compile` fusion. | 2026-08-23 |
| [[Two Speeds of a GPU]] | #summary | Adam Mainz's guide to GPU compute vs memory bandwidth ceilings, arithmetic intensity, and the Roofline Model. | 2026-08-23 |
| [[Adam Mainz]] | #entity | AI/ML performance engineer (ex-Meta, Google PyTorch TPU) authoring systems guides on GPU execution and compilation. | 2026-08-23 |
| [[GPU Kernel]] | #concept | Parallel function launched by host CPU and executed across hardware threads/warps on GPU device memory. | 2026-08-23 |
| [[Kernel Fusion]] | #concept | Compiler optimization combining adjacent operators into a single kernel to eliminate intermediate global memory round-trips. | 2026-08-23 |
| [[Torch Compile]] | #concept | PyTorch 2.x JIT graph compiler using TorchDynamo, AOTAutograd, and TorchInductor for automated kernel fusion and Triton codegen. | 2026-08-23 |
| [[Arithmetic Intensity]] | #concept | Ratio of total arithmetic operations (FLOPs) to memory bytes transferred across the memory bus (FLOPs/byte). | 2026-08-23 |
| [[Roofline Model]] | #concept | Visual performance model bounding attainable throughput by memory bandwidth and peak compute ceilings. | 2026-08-23 |
| [[How Claude Watermarks AI-Generated Text]] | #summary | Sebastian Raschka's video lecture on token sampling, secret-key PRNG seeding, tournament sampling, watermark detection, and evasion. | 2026-08-23 |
| [[Text Watermarking]] | #concept | Embedding imperceptible statistical or cryptographic signals in LLM token sampling for post-hoc machine provenance verification. | 2026-08-23 |
| [[Tournament Sampling]] | #concept | Keyed tournament decoding algorithm enabling lightweight, LLM-free post-hoc watermark detection on arbitrary text. | 2026-08-23 |
| [[Papers Explained: SFT Conflicts, RL Coexists]] | #summary | Analysis of multi-task reasoning in SFT vs RL, parameter sparsity, gradient orthogonality, and Parallel-RL merging. | 2026-08-30 |
| [[Parallel-RL]] | #concept | Distributed RL framework merging independently trained task parameter updates without interference. | 2026-08-30 |
| [[Task Coexistence]] | #concept | Multi-task RL property where optimizing one capability preserves and improves untrained capabilities. | 2026-08-30 |
| [[RL's Razor]] | #concept | Principle that on-policy RL implicitly minimizes divergence from initial policy, inducing sparse minimal updates. | 2026-08-30 |
| [[Gradient Interference]] | #concept | Multi-task gradient inner product; norm-limited in SFT and variance-limited via zero-sum advantage filtering in RL. | 2026-08-30 |
| [[Papers Explained: On-policy Distillation with Verifiable Reward]] | #summary | Parameter-free ReLU gating mechanism unifying on-policy distillation with verifiable rewards and GRPD. | 2026-08-30 |
| [[OPDVR]] | #concept | On-policy Distillation with Verifiable Reward using ReLU-gated token log-probability ratios. | 2026-08-30 |
| [[GRPD]] | #concept | Group Relative Policy Distillation combining GRPO advantages with gated token distillation. | 2026-08-30 |
| [[LeapLabTHU]] | #entity | Tsinghua University LEAP Lab led by Gao Huang, researching efficient post-training and reasoning architectures. | 2026-08-30 |
| [[Papers Explained: SycophancyEval]] | #summary | Benchmark and empirical study of sycophancy in LLMs across feedback, challenge, QA, and preference data. | 2026-08-30 |
| [[SycophancyEval]] | #entity | Evaluation suite measuring feedback, challenge, answer, and mimicry sycophancy in large language models. | 2026-08-30 |
| [[Papers Explained: SycoBench-600]] | #summary | Controlled 600-instance MCQ benchmark measuring social-pressure sycophancy and correction selectivity in LLMs. | 2026-08-30 |
| [[SycoBench-600]] | #entity | Diagnostic multiple-choice benchmark evaluating pressure-robust accuracy and correction selectivity under social perturbations. | 2026-08-30 |
| [[Correction Selectivity]] | #concept | Metric quantifying an assistant's capacity to accept legitimate corrections while rejecting deceptive suggestions. | 2026-08-30 |
| [[Pressure-Robust Accuracy]] | #concept | Multi-turn accuracy metric requiring consistent correctness across all misleading conversational perturbations. | 2026-08-30 |
| [[Papers Explained: SYCON (SYcophantic CONformity) Bench]] | #summary | Multi-turn free-form benchmark evaluating sycophantic conformity, Turn-of-Flip, and Number-of-Flip. | 2026-08-30 |
| [[SYCON Bench]] | #entity | Multi-turn conversational benchmark evaluating temporal sycophantic conformity across debate, unethical queries, and false presuppositions. | 2026-08-30 |
| [[Turn-of-Flip]] | #concept | Multi-turn metrics (ToF and NoF) measuring the latency of stance capitulation and stance volatility in dialogues. | 2026-08-30 |
| [[URIAL]] | #concept | In-context alignment methodology unlocking interactive multi-turn capabilities in base LLMs without fine-tuning. | 2026-08-30 |
| [[Papers Explained: Who Flips?]] | #summary | Controlled two-stage protocol measuring Answer Flip Rate under counterarguments, Self-Attribution Delta, and MAXFLIP. | 2026-08-30 |
| [[Answer Flip Rate]] | #concept | Metric measuring the conditional probability of retracting naturally correct answers under argument-only challenges. | 2026-08-30 |
| [[Self-Attribution Bias]] | #concept | Empirical increase in flip rate (Self-Attribution Delta) when misleading counterarguments are attributed to the model itself. | 2026-08-30 |
| [[Coercion Success Rate]] | #concept | Metric measuring model compliance in generating plausible rationales for objectively incorrect options across domains. | 2026-08-30 |
| [[MAXFLIP]] | #concept | Adversarial multi-model evaluation protocol selecting the most persuasive cross-model counterargument per question. | 2026-08-30 |
