# Papers Explained: Sarvam 30B and Sarvam 105B

Papers Explained: Sarvam 30B and Sarvam 105B

Papers Explained: Sarvam 30B and Sarvam 105B

Sarvam 30B and Sarvam 105B are reasoning models trained from scratch on large-scale, high-quality datasets curated in-house across every…

Papers Explained: Sarvam 30B and Sarvam 105B

Sarvam 30B and Sarvam 105B are reasoning models trained from scratch on large-scale, high-quality datasets curated in-house across every stage of training: pre-training, supervised fine-tuning, and reinforcement learning conducted entirely in India.

Architecture

Both models share a common architectural principle: high-capacity reasoning with efficient training and deployment. At the core is a Mixture-of-Experts (MoE) Transformer backbone that uses sparse expert routing to scale parameter count without increasing the compute required per token, while keeping inference costs practical. The architecture supports long-context inputs through rotary positional embeddings, RMSNorm-based stabilization, and attention designs optimized for efficient KV-cache usage during inference.

While the two models share the same design philosophy, they differ in scale and attention mechanism. Sarvam 30B uses Grouped Query Attention (GQA) to reduce KV-cache memory while maintaining strong performance. Sarvam 105B extends the architecture with greater depth and Multi-head Latent Attention (MLA), a compressed attention formulation that further reduces memory requirements for long-context inference.

Both models use sparse expert feedforward layers with 128 experts, but differ in expert capacity and routing configuration. This allows the larger model to scale to higher total parameters while keeping active compute bounded.

Training

Pre-training

The models were trained, with 16T tokens for the 30B and 12T tokens for the 105B. The pre-training data spans code, general web data, specialized knowledge corpora, mathematics, and multilingual content. After multiple ablations, the final training mixture was balanced to emphasize reasoning, factual grounding, and software capabilities. Significant investment was made in synthetic data generation pipelines across all categories. The multilingual corpus allocates a substantial portion of the training budget to the 10 most-spoken Indian languages.

Pre-training was conducted in three phases, covering long-horizon pre-training, mid-training, and a long-context extension phase. Sigmoid-based routing scores were used rather than traditional softmax gating, which improves expert load balancing and reduces routing collapse during training. An expert-bias term stabilizes routing dynamics and encourages more uniform expert utilization across training steps.

Supervised Finetuning

During supervised fine-tuning, the model is trained on a large corpus of high-quality prompts curated for difficulty, quality, and domain diversity. Prompts are sourced from open datasets and labeled using custom models to identify domains and analyze distribution coverage. To address gaps in underrepresented or low-difficulty areas, additional prompts are synthetically generated based on the pre-training domain mixture.

The dataset also includes extensive agentic traces generated from both simulated environments and real-world repositories, enabling the model to learn tool interaction, environment reasoning, and multi-step decision making.

For safety fine-tuning, a dataset covering both standard and India-specific risk scenarios was developed. This effort was guided by a unified taxonomy and an internal model specification inspired by public frontier model constitutions.

Reinforcement Learning

The reinforcement learning stage uses a large and diverse prompt distribution spanning mathematics, coding, STEM reasoning, web search, and tool usage across both single-turn and multi-turn environments. Rewards are derived from a combination of verifiable signals, such as correctness checks and execution results, and rubric-based evaluations that assess instruction adherence, formatting, response structure, and overall quality. To maintain an effective learning curriculum, prompts are pre-filtered using open-source models and early checkpoints to remove tasks that are either trivially solvable or consistently unsolved. During training, an adaptive sampling mechanism dynamically allocates rollouts based on an information-gain metric derived from the current pass rate of each prompt.

The RL system is implemented with an asynchronous GRPO architecture that decouples generation, reward computation, and policy updates, enabling efficient large-scale training while maintaining high GPU utilization. Trajectory staleness is controlled by limiting the age of sampled trajectories relative to policy updates, balancing throughput with training stability. The system omits KL-divergence regularization against a reference model, avoiding the optimization conflict between reward maximization and policy anchoring. Policy optimization instead uses a custom group-relative objective inspired by CISPO, which improves stability over standard clipped surrogate methods.

Evaluation

Sarvam 105B
Sarvam 105B: All Benchmarks.
Sarvam 105B matches or outperforms most comparable open and closed-source frontier models across knowledge, reasoning, and agentic benchmarks.
On Indian language benchmarks, it significantly outperforms all evaluated models.
Demonstrates strong, balanced performance in mathematics, coding, knowledge, and instruction following:
Math500: 98.6, matching top models in the comparison.
LiveCodeBench v6: 71.7, outperforming most competitors on real-world coding tasks.
MMLU: 90.6 and MMLU Pro: 81.7, competitive with frontier-class systems on knowledge tasks.
IF Eval: 84.8, indicating well-rounded instruction-following and general capability.
Strong multi-step and complex reasoning, including effective tool integration:
AIME 25: 88.3 Pass@1, improving to 96.7 with tool use, showing that external tools significantly boost performance.
GPQA Diamond: 78.7 and HMMT: 85.8, outperforming several comparable models.
Beyond AIME: 69.1, leading or matching the comparison set on deeper, harder reasoning tasks.
Optimized for tool use, long-horizon reasoning, and environment interaction:
BrowseComp: 49.5, outperforming several competitors on web-search-driven tasks.
Tau2 (avg.): 68.3, the highest score among compared models, indicating strong long-horizon agentic reasoning and task completion.

Sarvam 30B
Sarvam 30B:All Benchmark.
Sarvam 30B shows strong core language modeling performance, especially in math, coding, and knowledge:
Math: 97.0 on Math500, matching or exceeding several larger models.
Coding: 92.1 on HumanEval, 92.7 on MBPP, 70.0 on LiveCodeBench v6, outperforming many similarly sized models on practical coding tasks.
Knowledge: 85.1 on MMLU and 80.0 on MMLU Pro, competitive with leading open models.
Strong multi-step reasoning and complex problem-solving:
AIME 25: 88.3 Pass@1, improving to 96.7 with tool use, showing effective integration of reasoning with external tools.
GPQA Diamond: 66.5, indicating strong performance on difficult scientific/graduate-level questions.
HMMT Feb 2025: 73.3; HMMT Nov 2025: 74.2, strong on challenging math competitions.
Beyond AIME: 58.3, competitive with larger models.
Native tool-calling and agentic workflows (planning, retrieval, multi-step execution) are well supported:
BrowseComp: 35.5, outperforming several comparable models on web-search-driven tasks.
Tau2 (avg.): 45.7, indicating reliable performance over extended, interactive tasks.
SWE-Bench Verified: performance is competitive within its class, though the benchmark remains challenging for all models.

Indian Language Performance

To evaluate Indian language capabilities, a new benchmark was developed using a pairwise comparison framework with an LLM-as-judge protocol.
Sarvam 105B Indic Win Rate.
In pairwise chat comparisons against large open-source models, Sarvam 105B wins the majority of cases:

Qwen3-Next-80B-A3B: 87.30% Sarvam wins vs 12.70% competitor wins/ties
GLM-4.5-Air: 91.70% vs 8.30%
GPT-OSS-120B: 91.20% vs 8.80%

In technical domains (STEM, mathematics, coding), Sarvam 105B still wins strongly:

Qwen3-Next-80B-A3B: 84.50% vs 15.50%
GLM-4.5-Air: 87.40% vs 12.60%
GPT-OSS-120B: 81.30% vs 18.70%

Overall, Sarvam 105B wins on average:

~90% of comparisons across all benchmarked dimensions.
~84% on STEM, mathematics, and coding.
Sarvam 30B Indic Win Rate.
Sarvam 30B outperforms a range of 20–32B open-source models in chat:

GPT-OSS-20B: 90.60% vs 9.40%
Nemotron-3-Nano-30B: 97.10% vs 2.90%
Qwen3–30B-A3B: 81.60% vs 18.40%
Gemma-3–27B-IT: 70% vs 30%
Mistral-3.2–24B: 97.80% vs 2.20%
GLM-4.7-Flash: 91.50% vs 8.50%
OLMo-3.1–32B-Think: 93.40% vs 6.60%

In technical domains, Sarvam 30B also leads:

GPT-OSS-20B: 80.80% vs 19.20%
Nemotron-3-Nano-30B: 90.90% vs 9.10%
Qwen3–30B-A3B: 83.50% vs 16.50%
Gemma-3–27B-IT: 80.30% vs 19.70%
Mistral-3.2–24B: 93.80% vs 6.20%
GLM-4.7-Flash: 85.60% vs 14.40%
OLMo-3.1–32B-Think: 93.40% vs 6.60%

Overall, Sarvam 30B wins on average:

~89% of comparisons across all benchmarked dimensions.
~87% on STEM, mathematics, and coding.

Tokenizer Efficiency

Sarvam tokenizer outperforms other open-source tokenizers in encoding Indic text, as measured by fertility (average tokens per word).
It is particularly more efficient for low-resource languages such as Odia, Santali, and Manipuri (Meitei).

Paper

Open-Sourcing Sarvam 30B and 105B

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

View original.

Exported from Medium on May 4, 2026.
