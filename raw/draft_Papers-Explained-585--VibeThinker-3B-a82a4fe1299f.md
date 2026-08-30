# Papers Explained 585: VibeThinker-3B

Papers Explained 585: VibeThinker-3B

Papers Explained 585: VibeThinker-3B

VibeThinker-3B is a compact dense model with 3B parameters, developed to investigate how far verifiable reasoning can be pushed within a…

Papers Explained 585: VibeThinker-3B

VibeThinker-3B is a compact dense model with 3B parameters, developed to investigate how far verifiable reasoning can be pushed within a strictly small-model regime. Building upon the Spectrum-to-Signal post-training paradigm, the model is systematically enhanced through an optimized pipeline that includes curriculum-based supervised fine-tuning, multi-domain reinforcement learning, and offline self-distillation.

Method
Overall training pipeline of VibeThinker-3B.
VibeThinker-3B is developed through a staged post-training pipeline built upon Qwen2.5-Coder-3B base. The overall post-training framework continues the Spectrum-to-Signal Principle (SSP) introduced in VibeThinker-1.5B. The data construction and overall training pipeline are comprehensively optimized.

First, in the Supervised Fine-Tuning (SFT) stage, the rigorous data synthesis and filtering pipeline is upgraded, thereby supporting the introduction of a two-stage curriculum learning strategy. This enables the model to transition smoothly from broad capability coverage to deep, long-horizon reasoning.

Subsequently, in the Reinforcement Learning (RL) stage, MGPO is applied to multi-domain reasoning tasks utilizing a significantly expanded context window; furthermore, in the mathematical RL phase, a Long2Short stage is introduced to optimize reasoning efficiency without compromising accuracy.

Following the completion of the core reasoning RL, the pipeline immediately proceeds to an Offline Self-Distillation phase to backfeed the newly elicited capabilities, and finally concludes with an Instruct RL stage to further reinforce the model’s strict adherence to complex, multi-step instructions.

Supervised Fine-tuning

Data Construction

An automated data synthesis pipeline is introduced during the SFT phase to broaden the coverage of training queries. Only queries with reliable supervision signals from existing datasets are selected as seed queries: mathematical queries must possess explicit and credible final answers or solving rationales, while competitive programming queries must be equipped with reliable unit tests or executable evaluation rules. Based on these high-confidence seed samples, queries are rewritten and expanded across multiple dimensions, such as concept composition, problem-solving skeletons, constraints, and evaluation objectives, yielding derivative queries that encompass a wider array of knowledge configurations and reasoning patterns. For the initially filtered synthetic queries, multiple independent samplings are performed using strong teacher models, and pseudo-labels are generated via majority voting, establishing the foundation for subsequent distillation and training.

Strong teacher models are employed to sample multiple candidate reasoning traces for each query, retaining the complete intermediate reasoning steps rather than only a single standard solution. This design inherits the Spectrum-to-Signal paradigm, as the model learns various decomposition methods, derivation paths, and verification strategies, thereby improving exploration diversity during subsequent on-policy sampling.

Samples containing anomalous repetitive segments, templated degeneration patterns, or n-gram overlaps with evaluation sets are discarded to remove low-quality generations and benchmark contamination. Capable LLMs are utilized to assess query quality, filtering out samples with incomplete descriptions, unreasonable conditions, invalid logic, or an inability to effectively assess target knowledge points.

At the distilled response level, reasoning traces are screened through a combination of answer verification, code sandbox execution, and LLM majority voting. Traces with incorrect final answers, failed execution results, or evidently invalid reasoning steps are filtered out.

Training Process

VibeThinker-3B adopts a curriculum-based two-stage SFT procedure. The first stage focuses on broad capability coverage and behavioral cold start. The entire quality-filtered reasoning dataset is utilized for training to maximize the diversity of task types and reasoning.

Initialized from the final checkpoint of the first stage, the second stage continues training on a hard-reasoning subset generated through a joint length-difficulty filtration. Samples with reasoning traces shorter than 5K tokens are discarded. Using VibeThinker-1.5B as a reference model, 8 independent rollouts are performed per query, filtering out relatively easy problems that yield an error rate below 0.75.

Retaining the exact hyperparameter configuration from the first stage, this phase undergoes an additional 2 epochs of training on the hard-sample subset.

Intermediate checkpoints are periodically saved during training and evaluated for their Pass@K performance on domain-specific probing sets. For each domain, the checkpoint that produces more valid solutions is selected as the corresponding specialist model, rather than simply choosing the checkpoint with the lowest validation loss or the highest Pass@1. These domain specialist models are then merged at the parameter level to obtain a unified SFT model.

Reinforcement Learning

In VibeThinker-3B, the core MGPO formulation is kept unchanged.

Multi-domain Reasoning RL

MGPO is applied to multi-domain verifiable reasoning tasks, including mathematics, code, and STEM reasoning. These domains share the same policy optimization framework, but use different reward sources and verification mechanisms: mathematical tasks mainly rely on final-answer verification, code tasks rely on sandbox execution and test cases, and STEM tasks combine answer matching with option verification.

Training starts with Math RL, which strengthens the model’s long-horizon symbolic derivation, complex condition composition, and multi-step search capabilities. It then smoothly transitions to Code RL, focusing on improving the rigor of executable logic, boundary-case handling, and program constraint satisfaction. STEM RL is conducted to generalize the underlying logical reasoning ability to multidisciplinary scientific scenarios, enhancing knowledge utilization and cross-domain reasoning. The checkpoint obtained after each RL stage is preserved and used in the subsequent offline self-distillation phase, where high-quality reasoning trajectories elicited at different stages are collected to further consolidate the model’s overall reasoning capability.

For all domains, the training sets comprise data with reliable supervision signals and have undergone strict benchmark decontamination. Additionally, before training commences, samples yielding an accuracy of exactly 0.0 or 1.0 as evaluated by the starting checkpoint of each respective phase are filtered out.

VibeThinker-3B adopts a ‘from accuracy to efficiency’ two-stage reinforcement learning strategy. In the first stage, the model is optimized for accuracy using standard MGPO, allowing it to fully unfold its reasoning process and explore diverse solution paths. Subsequently, a Long2Short stage in Math RL is introduced, extending the optimization objective from pure accuracy improvement to token-efficiency optimization.

Rewards are redistributed only among correct trajectories in each prompt group according to response length, increasing the rewards of shorter correct responses and decreasing those of longer correct responses. After obtaining the binary correctness reward ri, for the correct set C = {i | ri = 1}, a brevity score si = 1/Li is defined, where Li denotes the response length, and a centered length-aware reward shift is applied:

where ¯s is the mean brevity score over correct trajectories and λ, set to 0.2, controls the maximum redistribution magnitude.

Offline Self-Distillation

The checkpoints from the Math, Code, and STEM RL stages, together with data filtering, are used to extract offline trajectories that contain high-quality reasoning patterns. These trajectories are then distilled back into a unified student model through supervised fine-tuning, enabling more stable integration of multi-domain reasoning capabilities.

After obtaining verified teacher trajectories, a learning potential score is introduced to estimate the distillation value of each correct trace for the student model. Specifically, for an input q and a verified teacher trajectory y, the length-normalized negative log-likelihood under the student model is computed.

A higher score indicates that the trace, although successfully generated and verified by the teacher, is not yet well modeled by the student, and therefore carries higher distillation value.

Instruct RL

Instruct RL is applied to convert the reasoning-enhanced checkpoint into a more reliable user-facing model. Training is conducted on a mixed instruction dataset containing format-sensitive prompts, long-context instructions, and general alignment examples. For samples with explicit constraints, rewards are computed by rule-based validators that check format, ordering, item count, keyword constraints, and task completion. For open-ended prompts, rubric-based reward models are used to evaluate helpfulness, coherence, instruction adherence, and redundancy.

Evaluation
Performance of VibeThinker-3B on Core Benchmarks.
VibeThinker-3B significantly outperforms or matches other small and mid-sized models (<14B) on mathematics (e.g., 94.3 on AIME26, 93.8 on BruMO25, 76.4 on IMO-AnswerBench), and achieves top results on coding (80.2 on LiveCodeBench v6) and instruction following without losing controllability (93.4 on IFEval, 74.5 on IFBench).
Compared to much larger reasoning models (up to over 500B parameters), VibeThinker-3B holds its own on competition mathematics and coding, though it lags on knowledge-heavy tasks like GPQA-Diamond, a gap consistent with limits to what small models can recall as direct knowledge.
Performance of VibeThinker-3B on Core Benchmarks.
VibeThinker-3B enters the leading cluster on competition mathematics with scores like 97.1 (AIME26), 99.2 (BruMO25), and 80.6 (IMO-AnswerBench) matching or surpassing larger state-of-the-art model.
OOD Generalization Test: LeetCode Weekly & Biweekly Contests (Apr 25–May 31, 2026).
For OOD performance on recent LeetCode contests the model achieved a 96.1% first-attempt acceptance rate (123/128), outperforming or rivaling most contemporary large models, confirming strong generalization beyond benchmark datasets.

Paper

VibeThinker-3B: Exploring the Frontier of Verifiable Reasoning in Small Language Models 2606.16140

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

View original.

Exported from Medium on June 21, 2026.
