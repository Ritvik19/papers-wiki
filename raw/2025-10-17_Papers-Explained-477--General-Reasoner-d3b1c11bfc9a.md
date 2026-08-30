# Papers Explained 477: General-Reasoner

Papers Explained 477: General-Reasoner

Papers Explained 477: General-Reasoner

Current works for LLM reasoning mainly focus on mathematical and coding domains, largely due to data abundance and the ease of answer…

Papers Explained 477: General-Reasoner

Current works for LLM reasoning mainly focus on mathematical and coding domains, largely due to data abundance and the ease of answer verification. This limits the applicability and generalization of such models to broader domains, where questions often have diverse answer representations, and data is more scarce.

General-Reasoner is a novel training paradigm designed to enhance LLM reasoning capabilities across diverse domains. Key contributions include: (1) constructing a large-scale, high-quality dataset of questions with verifiable answers curated by web crawling, covering a wide range of disciplines; and (2) developing a generative model-based answer verifier, which replaces traditional rule-based verification with the capability of chain-of-thought and context-awareness.

The project is available on GitHub.

General Reasoner

Diverse Verifiable Reasoning Tasks
Data creation pipeline.
WebInstruct dataset is used as the initial dataset, which comprises approximately 5 million naturally occurring, web-crawled instructions from high-quality resource websites like StackExchange and various educational portals. Despite WebInstruct’s suitability for general instruction tuning, the majority of its documents are not directly usable as reasoning tasks due to a lack of explicit verifiable answers or required reasoning processes.

To address this, entries are first traced back to their original web pages to re-crawl precise question-answer pairs. During this re-crawling, questions lacking clearly identifiable human-written answers on the original source websites, or those requiring membership or complex interaction to show answers, are removed. This careful selection aims to ensure retained entries are human-verified, enhancing the dataset’s reliability and correctness.

Next, Gemini-1.5-Pro is used to extract single-turn questions explicitly identified as having clearly verifiable short answers. This step yields an intermediate dataset of approximately 1 million verifiable reasoning questions across various disciplines.

Subsequently, Gemini-2.0-Flash is applied to annotate each question with metadata, including the answer type, subject category, and difficulty level. Recognizing the skewed ratio of mathematical tasks, mathematics problems labeled as easier than university-level are specifically filtered out to ensure a more balanced and challenging dataset distribution.

Additionally, acknowledging that web-crawled data inherently contains noise, such as questions that are either unsolvable or trivially easy, further rigorous filtering is implemented to refine the dataset quality. Specifically, Gemini-2.0-Flash generates eight candidate solutions for each question, allowing for the application of the following quality control criteria:

Questions for which all eight candidate solutions fail are excluded, effectively removing ambiguous or noisy questions likely arising from crawling errors or incomplete source content.
Overly simplistic questions for which all eight candidate solutions are correct are also excluded, ensuring the dataset maintains sufficient complexity and presents meaningful challenges for robust reasoning and generalization during RL training.

The Gemini-2.0-Flash generated solutions are also later utilized to train a proposed model-based verifier, which will be discussed in detail in the next section.

Eventually, the processed dataset contains approximately 230,000 reasoning questions. It spans diverse answer formats, including multiple-choice, numerical expressions, and matrices, as highlighted in Figure 3a. Figure 3b further illustrates the balanced domain distribution of the curated dataset, encompassing disciplines such as mathematics, physics, chemistry, finance, and various other humanities and social sciences fields. This rigorous data curation process ultimately produces a challenging but reliable dataset for training generalizable reasoning capabilities in large language models.

Model-Based Verifier for GRPO

Given a question-answer pair (q,a), a behavior policy πθold samples a group of G individual responses {oi}. The GRPO objective updates model parameters θ as follows:

Traditional reward models are trained through human feedback or preference assessment, returning scalar values based on the entire output to indicate overall quality. These models are suffering from being hacked by the policy model, and usually require the reward model to have a large parameter size to be effective and robust. In contrast, rule-based verifiers, widely used in mathematical reasoning due to simplicity, evaluate only the final answer, allowing models greater freedom to explore diverse reasoning paths. However, these rule-based approaches encounter several critical limitations when extending beyond mathematics:

Rigid Matching Criteria: Rule-based methods typically require exact matches or adherence to rigid structures, failing to recognize semantically equivalent answers that differ in representation.
Semantic Insensitivity: They are ineffective at interpreting answers that vary semantically, such as equivalent expressions or answers expressed in different units or formats.
Lack of Generality: Adapting rule-based verification to a wide range of disciplines and diverse answer formats can be difficult, limiting their applicability and scalability.

A compact generative model-based verifier is introduced, specifically trained to robustly assess answer equivalence across diverse domains. Ideally, LLMs like Gemini-2.0 could verify answer equivalence; however, such solutions are computationally expensive and impractical for large-scale RL training.

Instead, a dataset creation pipeline, specifically Gemini-2.0-generated candidate answers and verification annotations, is leveraged to train a compact 1.5B-parameter generative verifier model. This verifier, initialized from Qwen2.5-Math-1.5B, is fine-tuned to assess student-generated short answers (extracted from the response) against ground-truth references in a generative manner, whose inference process is formulated as:

Experiment Setup

The research follows the Zero RL setting, directly conducting reinforcement learning (RL) from base large language models without an intermediate supervised fine-tuning stage. Models are initialized using the base model from the Qwen2.5 family (7B and 14B) and the newer Qwen3 family (4B and 14B). The GRPO algorithm is applied. Reward scores during training are calculated as follows:

If the solution extraction fails (e.g., no boxed answer or summarization such as “the solution is:”), the reward is -0.5.
If the solution passes verification, the base reward is 1, with a length-based penalty applied to discourage excessively long generations:

penalty = -0.05× min(10, abs(len_of_ground_truth — len_of_answer))
Hyperparameter settings for General-Reasoner variants.
Evaluation
Accuracy comparison on general reasoning benchmarks.Math task accuracy across datasets.
General-Reasoner with Zero RL consistently outperforms both base and supervised fine-tuned models across the Qwen2.5 and Qwen3 backbones.
General-Reasoner achieves strong results on math-related benchmarks.
General-Reasoner-4B surpasses Qwen2.5–7B after Zero RL, demonstrating the efficiency and transferability of the training method across model scales.
General-Reasoner-Qw3–14B achieves performance comparable to GPT-4o on GPQA and TheoremQA, despite relying solely on Zero RL.
The model does not exhibit overthinking, with significantly shorter response lengths compared to methods like DeepScaleR.

Paper

General-Reasoner: Advancing LLM Reasoning Across All Domains 2505.14652

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on October 17, 2025.

Canonical link

Exported from Medium on May 4, 2026.
