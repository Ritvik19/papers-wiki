# Papers Explained: 580 Nemotron 3 Ultra

Papers Explained: 580 Nemotron 3 Ultra

Papers Explained: 580 Nemotron 3 Ultra

Nemotron 3 Ultra is a 550B total and 55B active parameter Mixture-of-Experts Hybrid Mamba-Attention language model. It is pretrained on 20…

Papers Explained: 580 Nemotron 3 Ultra

Nemotron 3 Ultra is a 550B total and 55B active parameter Mixture-of-Experts Hybrid Mamba-Attention language model. It is pretrained on 20 trillion text tokens, then extended the context length to 1M tokens, and post-trained using Supervised Fine Tuning (SFT), Reinforcement Learning (RL), and Multi-teacher On-Policy Distillation (MOPD). It employs multiple key technologies: LatentMoE, Multi Token Prediction (MTP), NVFP4 pre-training, multi-environment RLVR, MOPD, and reasoning budget control.

The models and training data are available at HuggingFace.

Pretraining

Nemotron 3 Ultra layer pattern.

Nemotron 3 Ultra Architecture Dimensions.
Nemotron 3 Ultra uses the same hybrid Mamba-Attention Mixture-of-Experts architecture as Nemotron 3 Super, extended to 550B total parameters with 55B active parameters per token. It uses LatentMoE for MoE layers and native Multi-Token Prediction for inference acceleration with two heads during pre-training. It is trained using the same NVFP4 pretraining recipe as Nemotron 3 Super.

Long Context Extension

A long-context phase (LC-Phase) is added at the end of pretraining. In the LC-Phase, continuous pretraining is performed to equip the base model with long-context ability. Besides the long-context document QA data used in Nemotron 3 Super & Nano, further long-context SFT-style data is added into the blend. No RULER-style data was used in the blend. Overall, the long-context data constituted 46% and Phase 2 data constituted 54% in the blend. CPT was performed on 1,048,576 (1M) context length for 92% of the iterations, while training on 4,096 (4K) for the remaining 8% of the time in order to maintain the accuracy of the short benchmarks.

Pretraining Data

Code refresh

The raw source code data from GitHub is refreshed, adding 173B new tokens with a cut-off date of September 30, 2025.

Nemotron-Pretraining-Multiple-Choice and Nemotron-Pretraining-Generative

Large-scale, task-seeded synthetic Q&A data is generated from the training splits of many public datasets spanning a wide range of domains, including STEM, factual knowledge, commonsense reasoning, logical reasoning, math, code, reading comprehension, and multilingual QA. The resulting data is organized into two dataset families: Nemotron-Pretraining-Multiple-Choice, which contains synthetic questions with answer options and normalized correct answers, and Nemotron-Pretraining-Generative, which contains open-ended Q&A examples with free-form answers. For both formats, answer-enriched samples are generated that include task-relevant knowledge, reasoning, or explanatory context when appropriate. Formatting checks, schema validation, deduplication, and task-specific filtering are applied to improve data quality.

Nemotron-Pretraining-Fact-Seeking

This dataset contains fact-seeking questions generated from Finewiki. The questions are generated in two stages: extracting informative, factual statements from Finewiki articles, and prompting Qwen3–30B-A3B-Instruct-2507 with each statement and its original context to generate either a short-answer or multiple-choice question.

Nemotron-Pretraining-Moral-Scenarios

In the SFT data released for Nemotron 3 Super, multiple-choice questions about moral scenarios were included. These questions were constructed using situations and norms from Moral Stories and actions from Social Chemistry. A subset of these examples was sampled and a chain-of-thought version was created using Qwen3–235B-A22B-Thinking-2507.

Nemotron-Pretraining-Legal

Datasets extracted from HTML files:

Nemotron-Pretraining-Legal-California-Code-Of-Regulations: Excludes Title 6 and Title 24.
Nemotron-Pretraining-Legal-NYCourts-Judicial-Ethics-Opinions: New York Court Judicial Ethical Opinions.
Nemotron-Pretraining-Legal-eCFR: Code of Federal Regulations.

LLM-cleaned datasets:

Nemotron-Pretraining-Legal-Case-Law-Summary: 5.4M summaries from filtered Caselaw, using Qwen3–235B-A22B-Instruct-2507.

Reformatted datasets:

Nemotron-Pretraining-Legal-CaseHOLD: CaseHOLD dataset transformed to multiple-choice format.
Nemotron-Pretraining-Legal-Contract-NLI: For each NDA in ContractNLI, annotated hypotheses, answers, and evidence plus the source document.

Synthetic datasets:

Nemotron-Pretraining-Legal-Canadian-Case-Law-Outcome: Passages stating appeal outcomes, generated using Qwen3–235B-A22B-Instruct-2507.
Nemotron-Pretraining-Legal-Definition-Classification: Caselaw passages with/without defining language, used for term definition classification.
Nemotron-Pretraining-Legal-Diversity-Jurisdiction: Questions on complete diversity between parties, names, states, causes of action sampled from lists and rephrased for diversity.
Nemotron-Pretraining-Legal-Function-Of-Decision: Caselaw paragraphs classified into seven categories (facts, procedural history, issue, rule, analysis, conclusion, decree).
Nemotron-Pretraining-Legal-GlobalCit: Questions on global nationality laws, rephrased from GLOBALCIT dataset, each in three versions.
Nemotron-Pretraining-Legal-LegalBench-CUAD-v2: Contract clause type identification, cleaned and processed from CUAD dataset. For categories with low accuracy, longer prompts with instructions were used.
Nemotron-Pretraining-Legal-ToS-Clause-Understanding: Terms of service clause understanding questions, generated per clause using Qwen3–235B-A22B-Instruct-2507.
Nemotron-Pretraining-Legal-ToSDR-QA: Yes/No questions about contract sections from the ToSDR Terms of Service corpus, generated with Qwen3–235B-A22B-Instruct-2507.
Nemotron-Pretraining-Legal-eCFR-QA: DiverseQA-like questions from Code of Federal Regulations, each answer evaluated for correctness.

Data Mixture and Ordering

The data mixtures for both pretraining phases.

The data mixtures used to train Nemotron 3 Ultra are an adaptation of the data mixtures used to train Nemotron 3 Super and Nano and incorporate new and refreshed datasets. A two-phase curriculum is adopted, transitioning from a data mixture which biases dataset diversity (phase 1) to a data mixture which biases dataset quality (phase 2). This transition occurs after approximately 15 trillion tokens, corresponding to about 75% of pretraining.

Post Training
Overview of the post-training pipeline for Nemotron 3 Ultra.
Supervised Fine Tuning

SFT is performed in two stages. In Stage 1, training is conducted on packed sequences of length 294,912 tokens with a global batch size of 64 for 204,800 samples. In Stage 2, the packed sequence is extended to 515,000 tokens, augmenting the mixture with additional long-context data up to 512K tokens. Training is carried out with a global batch size of 64 for 19,200 samples. As in pre-training, the shared-weight MTP objective is retained during SFT, using two MTP layers with a per-token auxiliary-loss scaling factor of 0.1.

A length-aware best-fit packing strategy is adopted, which reads and interleaves all source files in a round-robin fashion, maintaining only a fixed-size pool of open sequences in memory, and retiring a sequence once its residual capacity falls below a small tolerance. Each incoming conversation is assigned to the partially filled sequence whose remaining capacity it most tightly fits, following a best-fit rule that minimizes padding overhead. Additionally, an in-pack deduplication constraint is enforced to prevent identical prompts from co-occurring within the same sequence.

SFT Data

Long context

512K long-context SFT data are prepared based on the synthetic data pipeline following Nemotron 3 Super.

Efficiency and Control

The SFT data include two components for reasoning efficiency and control. The first is training samples generated by GPT-OSS-120B in its medium-effort mode on prompts of math reasoning, STEM question answering and instruction following. These SFT data initiate Ultra’s medium-effort mode which is later optimized during the RLVR stage. The second component is training samples where the reasoning traces are truncated to random reasoning budgets while the responses remain the same.

Safety

The 45K safety data blend from Nemotron 3 Super is retained, featuring prompts from diverse sources and synthetically generated responses based on a mapped response policy. The safety data blend is translated into six languages (German, Spanish, French, Japanese, Italian, and Chinese) using NVIDIA Riva Translate 4B v1.1. Translations were back-translated into English and compared to the original, filtering out examples with semantic similarity below 0.8, removing about 10–15% of examples per language. A balanced dataset is created using stratified sampling, resulting in a final safety blend of approximately 135K samples: 45K in English and 15K in each translated language.

Search Capabilities

Retaining search trajectories from the Nemotron 3 Super dataset, which uses seed prompts grounded in the Wikidata knowledge graph. These prompts are constructed through 4–8 hop random walks over factual relations and solved using the Tavily Search Engine, with MiniMax 2.1 as the teacher model.
Including a new search dataset from OpenResearcher , a public SFT dataset for long-horizon research agents, which synthesizes over 97K trajectories using gpt-oss-120b as the teacher model in an offline browser environment. This environment uses a local search index over 15M FineWeb documents and provides three structured browser tools: search, open, and find. The resulting trajectories capture long-horizon reasoning-action-observation loops for research questions, source gathering, evidence localization, and answer synthesis.
Collaborating with data vendors to curate challenging samples requiring 50–100 searches and collecting SFT trajectories in the BrowseComp harness. For these trajectories, MiniMax 2.5 and GLM 5.1 are used as teacher models.

Terminal Use Capabilities

A large-scale dataset of synthetic agentic trajectories is created, covering terminal tasks such as software engineering, data processing, file operations, and scientific computing. Seed instructions are sourced from publicly available datasets including OpenCodeReasoning, OpenMathReasoning, SWE-bench, SWE-Fixer-Train-110K, SWE-rebench, and SWE-smith. Tasks are assembled from existing math and coding SFT data in Nemotron-Cascade and synthetically generated using DeepSeek-V3.2 to cover a variety of terminal scenarios. DeepSeek-V3.2 acted as the agent within the Terminus-2 agent provided by the Harbor framework. Each trajectory involved multiple episodes where the model received a task prompt, interacted with a live terminal environment, issued commands, and incorporated feedback to progress towards task completion. This process helped the model learn practical tool use, adaptive planning, and error recovery behaviors. The final dataset includes approximately 370K multi-turn conversations, with a mix of reasoning and non-reasoning trajectories.

Conversational Tool Use Capabilities

Conversational tool-use data is scaled via a fully synthetic, six-stage generation pipeline including User and Environment simulation similar to the one used in Nemotron-3 Super.

Software Issue Resolution

A diverse dataset of synthetic agent trajectories are generated using two modeling paradigms: the reasoning-based Minimax-M2.5 and the instruction-based Qwen3-Coder-480B-A35B-Instruct. The issue statements are sourced from various publicly available datasets, including SWE-Gym, R2E-Gym, SWE-rebench, and SWE-rebench-V2. The trajectories are captured using OpenHands, SWE-agent, Mini-SWE-agent, and Opencode harnesses. To ensure quality, a heuristic analyzer filters the raw agent rollouts based on several criteria, such as submission integrity, disallowed git operations, edit-test loop anti-patterns, lost-in-exploration, tool-call hygiene, debug-artifact detection, and verification checks. This approach ensures the dataset supports generalization across different problem-solving methods and environments.

Math / Proof Data.

Nemotron-Cascade-2 math data, which includes problems from Nemotron-Cascade and Nemotron-Math-V2 is used. For non-proof math data, 1.8 million tool-calling samples and 1.9 million non-tool samples are collected, with responses generated by DeepSeek-V3.2 and DeepSeek-V3.2-Speciale, respectively. For mathematical natural language proof data, proof problems are sourced from the AOPS split of Nemotron-Math-Proofs-v1, and responses are generated by DeepSeek-V3.2-Speciale for proof generation, verification, and refinement.

Science

Science SFT data is prepared using the Nemotron Nano recipe, which integrates synthetic, real-world, and document-derived data from physics, chemistry, and biology. The data is diversified with NeMo Data Designer and filtered by an LLM judge for compliance and quality. Additionally, web-search and web-search-with-Python reasoning traces are generated using DeepSeek-V3.2, with the model accessing the Tavily search engine and a Python execution environment for the latter.

Chat

Seed prompts are drawn from open conversational datasets like LMArena and WildChat. For each prompt, multiple candidate responses are generated using GLM-5, and the highest-quality response is selected using Nemotron-GenRM. To extend these into multi-turn conversations, a simulated user, guided by hand-crafted conversation strategies, interacts with the system. These strategies include building on prior content, asking for clarification, challenging assumptions, reframing tasks, or applying answers to new contexts to create diverse and realistic dialogues. To ensure robustness, some examples include suboptimal responses in earlier turns. The model is trained only on the final assistant response to produce high-quality outputs while being resilient to imperfect previous turns.

Code

Coding problems are collected from platforms like Codeforces, AtCoder, AIZU, and CodeChef. Strict deduplication and aggressive filtering are applied to enhance data quality and balance problem difficulties. The teacher model chosen is GPT-OSS-120B due to its strong reasoning ability and verbosity. Rejection sampling is applied to the reasoning traces, resulting in a final dataset of 1.2 million Python reasoning traces, 1.0 million C++14 reasoning traces, and 1.3 million Python tool-calling reasoning traces for competitive coding.

CUDA

A large-scale synthetic CUDA dataset with approximately 100K samples for kernel generation, repair, and optimization is created using a synthetic data generation pipeline involving DeepSeek-R1 and GPT-OSS-120B, with seed questions sourced from popular open-source libraries, NVIDIA library API surfaces, and Backend-Bench.

Two types of samples are generated: PyTorch-reference-to-CUDA-kernel samples and natural-language-specification-to-CUDA-kernel samples, each accompanied by reasoning. Multiple candidate kernels are produced for each seed item through LLM-based synthetic generation and rejection sampling. These candidates are validated in an internal CUDA evaluation environment using compilation checks, numerical correctness tests, and runtime benchmarking. Invalid, non-compiling, or incorrect candidates are rejected, and the best-performing kernel based on runtime benchmarks was retained.

Additionally, repair and optimization data are collected from an internal CUDA agent. Repair samples included a PyTorch reference, a faulty CUDA C++ kernel, the corresponding error message, and a corrected CUDA C++ kernel. Optimization samples included a PyTorch reference, a slow CUDA C++ kernel, an Nsight Compute log, and an optimized CUDA C++ kernel.

Beyond direct CUDA C++ kernel generation, CUDA-X library data is generated using publicly available documentation and official code samples. This included PyTorch references, aligned natural-language specifications, corresponding CUDA-X library implementations, and reasoning. The covered libraries included Thrust, CUB, cuBLAS, cuDNN, cuSPARSE, cuRAND, and cuSOLVER.

RTL

ACE-RTL raining data, which includes three main RTL task categories: specification-to-RTL generation, code editing, and code debugging is used. ACE-RTL is based on the seed RTL corpus from ScaleRTL, with designs sourced from open-source RTL repositories and processed through deduplication, filtering, and syntax validation. For specification-to-RTL tasks, DeepSeek-R1 and GPT-OSS-120B synthesize natural-language specifications paired with corresponding golden RTL implementations from the seed designs. For editing and debugging tasks, the original seed RTL serves as the golden implementation, while simplified or buggy variants are generated as inputs, with specifications describing required feature extensions or diagnostic information. The final dataset, after additional filtering and evaluation, contains around 1.2 million training samples.

Multilingual

The multilingual post-training data combines sentence-level parallel corpora and synthetic translations of English SFT examples in math, code, and science. Due to data quality issues in line-by-line translation pipeline, a new end-to-end translation pipeline is introduced, which processes full JSON objects. This pipeline, requiring strong long-context capabilities, uses the DeepSeek-V3–0324 model. Post-translation, heuristic format checking ensures JSON conformity, followed by data filtration and light-weight post-editing as per the Nemotron Super-V3 recipe. For Nemotron Ultra-V3, synthetic data for Hindi, Japanese, Korean, and Brazilian Portuguese is created using this new pipeline, while existing multilingual synthetic data from Super-V3 is reused for other languages.

Reinforcement Learning

A unified RLVR training stage is conducted spanning all available environments, targeting terminal usage, office and productivity workflows, software engineering, search, general tool-calling, math, code, STEM, safety, chat, instruction following, long-context QA, inductive and transductive reasoning, structured outputs, and general model usability. The RL training data is refreshed using recent collections and reward profiling is performed prior to training. The training procedure largely follows the asynchronous GRPO algorithm with the stability optimizations proposed in Nemotron 3 Super. To support training across a large and diverse set of environments, a global batch size of 8192 is used, with each sample generating 16 rollouts. Training begins with a maximum generation length of 48K tokens, which is later increased to 64K tokens.

MOPD

Two-iteration MOPD training pipeline for Nemotron 3 Ultra.

Mixed-environment RLVR provides broad capability improvements across a wide range of domains. However, as the number of environments continues to grow, each domain contributes only a relatively small number of samples to any given training batch. To fully unlock performance and push the frontier in each capability area, more than ten specialized teacher models are trained, each optimized through its own domain-specific training pipeline. During MOPD, the student model (obtained from RLVR) generates rollouts across all domains and receives dense reward signals from the corresponding teacher models.

MOPD is performed over multiple iterative cycles: after obtaining an MOPD-trained checkpoint, new rounds of teacher training are branched out, initialized from the updated student model, and the resulting improvements are subsequently merged back into the next MOPD stage. This iterative co-evolution between student and teachers enables continuous capability improvement and progressively stronger specialization across domains.

The goal is to train a single student policy (𝜋𝜃) by learning from multiple teacher policies ({𝜋𝑇𝑖} 𝑖 = 1 … 𝑁), where each teacher is an expert on a certain domain.

The student is trained to imitate the teacher on the student’s own generated data (as opposed to the teacher’s data).

For each text generation prompt 𝑞 (sampled from teacher 𝑖’s dataset 𝐷𝑖), the student generates a completion 𝑦 = (𝑦1,…,𝑦𝐻). The core objective is for the student’s policy to match the teacher’s, at each token on sequences generated by the student itself:

Where 𝜆𝑖 balances the importance of each domain 𝑖

Software Engineering Teacher

The SWE teacher was trained through a three-stage pipeline. Initially, Supervised Fine-Tuning (SFT) was applied to the Ultra base model using a blend of agentic data. Next, PivotRL was run on single-step agentic environments. In the final end-to-end SWE-RL stage, the model interacted with a code repository over multiple turns, issuing tool and bash commands to produce a patch, after which a verifier ran hidden tests and assigned a binary reward used in GRPO. Adjustments were made to address issues with the final reward, including masking the loss on unfinished trajectories and penalizing malformed reasoning and tool calls. To prevent the agent from cheating by reading the gold patch, two leak channels were closed: the in-container repository was rewritten to look like a fresh clone, and a runtime command filter was installed to block network-based history recovery. The end-to-end RL was conducted with a generation length of 192K and a maximum of 200 agent turns.

Office & Workplace Task Teacher

A specialized teacher was trained for tasks measured by the GDPval benchmark. GDPval tasks are structured as professional work assignments that capture economically productive tasks typically performed by human professionals. The model receives a prompt, often with supporting reference files, and must produce deliverables such as spreadsheets, documents, reports, music/audio files, or other artifacts.

The office and workplace task teacher was initialized from a Nemotron 3 Ultra checkpoint that completed the general SFT post-training phase. A training distribution was constructed from AfterQuery (AQ) tasks that share important latent structures with GDPval, including file-grounded reasoning, professional deliverables, multi-step analysis, and judged final outputs. For each AQ task, a strong model generated multiple full trajectory rollouts. These rollouts were used in two stages: first, light SFT was performed directly on the student Ultra model to transfer workflow priors for GDPval-like tasks; second, pivot RL was conducted in the MOPD stage, distilling the SFT-trained teacher into the student Ultra model using pivots derived from the strong model’s AQ rollouts.

Search Teacher

Search-based agents often deal with long and noisy interaction histories due to verbose, redundant, or partially relevant retrieved documents. Without explicit context management, these models can exhaust their context window before completing complex queries that require iterative refinement and evidence aggregation. Nemotron 3 Super was trained on search data without explicit context-management supervision. In contrast, Nemotron 3 Ultra was trained with a search-specialized teacher using supervised fine-tuning (SFT) on trajectories that included context-management behavior. The training data exposed the model to strategies for managing a finite context budget, such as discard-all resets and summary-based compression. The focus was primarily on discard-all context management, where earlier search observations are removed once the interaction history exceeds the context budget, allowing the model to handle longer effective contexts than its official context length.

Terminal-use Teacher

This involves using expert trajectories for tasks designed to challenge the model in long timeout settings, where tasks can run for up to one hour. The model is iteratively improved using PivotRL, with re-profiling steps introduced when accuracy saturates.

Conversational Tool-use Teacher

This uses the same data and recipe from Nemotron 3 Super to train the model on conversational tool-use data through PivotRL. For Nemotron 3 Ultra, the data is expanded to include tasks requiring sequential and dependent multi-step actions to prevent premature termination in conversational agent settings.

Model Usability Teacher

Nemotron 3 Super is trained to include three new targets: document extraction, citation formatting, and freeform text formatting. For structured schema formatting, an improved dataset covering JSON, YAML, XML, TOML, and CSV is created, and structured output tasks are increased to six categories: direct extraction, translation, multistep-related, multistep-unrelated, schema-only, and error correction. Document extraction training involves using varied structured extraction tools with distractors to handle deeply nested fields. Citation formatting training teaches the model to use multiple inline citation formats. Freeform text formatting training involves following diverse markdown styling instructions. All seed data was created using Nemo Data Designer with openai/gpt-oss-120b, and environments are implemented through Nemo-Gym.

Agentic Safety Teacher

A dataset is created with realistic tasks from various enterprise domains, where benign user requests require the model to call a read tool that returns content containing hidden adversarial instructions. These instructions target a sensitive write tool, making attack compliance observable from the tool-call trace. The dataset includes four attack categories: unauthorized actions, data modification, denial of service, and data exfiltration. An automated red-teaming loop is used to generate challenging attacks, with Nemotron 3 Super as the attacker model and Nemotron 3 Nano as the defender. A deterministic verifier marks an injection as resisted if the agent does not invoke the attacker’s target tool with the target arguments. This teacher provides verifiable supervision for completing the user’s intended task while ignoring untrusted instructions from the environment.

Chat Teacher

As policy models grow larger and more capable, they increasingly exploit weaknesses in the reward model during Reinforcement Learning from Human Feedback (RLHF), especially when the reward model is smaller or less capable. Generative Reward Models (GenRM) with reasoning capabilities help mitigate such reward hacking behaviors, but substantial failure cases still exist. To address this, both model capacity and training data are scaled up, resulting in the development of an Ultra-based GenRM.

The GenRM is trained to evaluate pairs of candidate responses given a conversational context. When user-defined principles are provided, the model’s judgment is conditioned on those principles; otherwise, it evaluates responses based on general helpfulness and quality criteria. The GenRM is trained on top of the Ultra SFT model and follows the RLVR method used in Nemotron 3 Super, assigning rewards to predict individual scores for two responses and a ranking score. When multiple principles are presented, GenRM predicts the triplet for each principle and then provides an overall judgment. During RLHF, only the overall scores are used as reward signals.

Chat teacher training involves multiple RLHF iterations. After each iteration, the policy model is evaluated on internal chat benchmarks, weaknesses are identified, and targeted data is curated to address them. A principle-following GenRM makes this process more flexible by adapting to different principles during training and evaluation, enabling targeted improvements across cycles without retraining the reward model itself.

Instruction-following and Factuality Teacher

Training combined instruction-following, abstention-focused, and RLHF environments. Instruction-following environments included scenarios like strict format compliance, mid-conversation instruction changes, and long-horizon conversational coherence, evaluated programmatically or via LLM-as-a-judge. Abstention training encouraged the model to abstain when uncertain, dynamically calibrating the abstention reward to balance accuracy and reduce hallucinations. RLHF data was incorporated to prevent behavioral collapse and overfitting, maintaining response quality, helpfulness, and alignment with human preferences while enhancing robustness in instruction-following and factuality tasks.

Competitive Coding Teacher

Additional Competitive Coding RL is conducted on top of the General Reasoning Teacher using coding data from the Nemotron-Cascade, which includes coding prompts from various competitive programming platforms with strong test cases for reward verification. Prompts that the General Reasoning Teacher solves correctly in all 8 of 8 rollouts are filtered out, resulting in a final set of 3.5K samples. This Competitive Coding RL approach yields a +2.4 improvement over the General Reasoning Teacher on LiveCodeBench v6.

STEM Teacher

This teacher focuses on the general reasoning capabilities on a wide range of subjects including math, code, natural sciences, humanities, sociology, and tool use for these domains. Starting from the student model, additional stages of SFT and RL are performed on selected datasets.

Science Reasoning Data:

The dataset includes STEM and non-STEM domains, derived from existing problems in several sources, including Nemotron Nano SFT, curated chemistry datasets, Multi-subject-RLVR, and proprietary datasets.
Problems were filtered to remove the easiest ones, and solution traces were generated using DeepSeek-V4-Pro, with more traces for difficult problems.
Correctness was graded by gpt-oss-120b, and additional traces were generated for problems with long correct-solution lengths.
A held-out set of 3,000 problems was reserved for RL evaluation.

Coding Reasoning Data:

The dataset comprises approximately 14K problems from international programming competitions over the past decade, including diverse contest styles and difficulty levels.
An additional 4K difficult problems from OpenCodeReasoning were included.
For each problem, 10 candidate solutions were generated with DeepSeek-V4, and non-compiling solutions were filtered out.

Mathematical Chain-of-Thought (COT) and Tool-Integrated Reasoning (TIR) Data:

The dataset includes 95,164 unique math problems, filtered from the Nemotron math data pipeline.
Both COT and TIR solution trajectories were generated using DeepSeek-V4-Pro and validated against reference answers using gpt-oss-120b.
The final pool contains 545,431 examples, split between COT and TIR.

Mathematical Proof Data:

A dedicated dataset for theorem-proving and verification-style reasoning, drawn from the AoPS AoP section of the Nemotron math data collection.
Proof-oriented traces were generated using DeepSeek-V4-Pro, following DeepSeekMath-V2 methodology.
The final validated pool contains 82,737 samples, including proof, verification, and meta-verification responses.

SFT Data Blending:

The final SFT mixture consists of 40B generated tokens, with contributions from science reasoning (58.75%), mathematical reasoning (23.63%), competitive coding (10.13%), and general-domain SFT (7.50%).
Examples were downsampled or upsampled to meet token budgets, and training examples were packed to a maximum sequence length of 294,912 tokens.

Reinforcement Learning:

Post-SFT, the model showed strong performance in math, code, and natural sciences.
The RL stage focused on non-STEM domains, using a smaller number of prompts per batch and a smaller global batch size.
Training generalized well, improving performance across all domains.

MOPD Warmup

One key finding from the MOPD trials is that teacher models trained with substantially different training pipelines cannot be effectively combined through a straightforward MOPD merge, resulting in suboptimal performance. To mitigate the distribution mismatch between teacher and student models, a brief warmup stage before MOPD is introduced. Specifically, the student undergoes a very light SFT on data drawn from the teacher’s training distribution. Since the warmup stage is intentionally limited in scale, it induces minimal regression on unrelated domains, and any residual degradation is subsequently recovered through MOPD training.

Evaluation

Evaluation suite for Nemotron 3 Ultra.

Nemotron 3 Ultra remains competitive with leading open models, outperforming or matching much larger models on several benchmarks.
On the held-out PinchBench and ProfBench benchmarks, Nemotron 3 Ultra scored 90.0 and 56.0, respectively, both close to or matching the top results, indicating strong generalization to unseen agentic tasks.
It demonstrates chain-of-thought reasoning and tool-integrated reasoning, achieving a score of 570.0 on IOI 2025 (top-3-human-level performance) and 92.3 on IMOAnswerBench with tools.
It supports context windows up to 1 million tokens, showing robust long-context understanding and retrieval abilities. On AA-Omniscience, it achieved the highest non-hallucination score (78.7), indicating high reliability and low hallucination rates.

Paper

Nemotron 3 Ultra: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

View original.

Exported from Medium on June 13, 2026.
