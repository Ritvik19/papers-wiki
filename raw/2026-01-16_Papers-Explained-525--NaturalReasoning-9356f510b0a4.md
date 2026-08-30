# Papers Explained 525: NaturalReasoning

Papers Explained 525: NaturalReasoning

Papers Explained 525: NaturalReasoning

NaturalReasoning is a comprehensive dataset of 2.8 million diverse, challenging reasoning questions with reference answers, backtranslated…

Papers Explained 525: NaturalReasoning

NaturalReasoning is a comprehensive dataset of 2.8 million diverse, challenging reasoning questions with reference answers, backtranslated from pretraining corpora across domains such as Mathematics, Physics, Computer Science, Economics & Business, and Social Sciences; it bridges the gap between narrow, easily verifiable tasks and broader open-ended reasoning (including theorem proving), is created solely with pretraining data and LLMs without extra human annotation

The dataset is available at HuggingFace.

Data Collection

An overview of the data creation approach of NaturalReasoning.

Given a document d from the pretraining corpora DCLM-baseline and FineMath, an LLM is prompted to rate the content in d along multiple axes: Problem Completeness, Problem Complexity and Technical Depth, Technical Correctness and Accuracy, Thinking and Reasoning.

For documents which are identified with a high degree of reasoning, an LLM is further prompted to compose a self-contained and challenging reasoning question ‘q’ based on the content in ‘d’. This approach allows for the synthesis of more novel questions not directly contained in pretraining corpora, unlike existing work which extracts questions appearing in the document. Then, the LLM is prompted to verify whether a correct reference answer ‘a’ to the synthesized question ‘q’ can be derived from ‘d’ and, if possible, include it as a reference answer. Finally, for every question, an additional response is generated with a relatively strong open-source model (Llama-3–70B-Instruct).

A similarity threshold of 0.55 is applied to filter out closely related variations, ensuring that questions with the same core reasoning task but different prompts are not redundantly included. Questions that are similar to popular reasoning benchmarks including MATH, GPQA, MMLU-Pro and MMLU-Stem are filtered out. A standard 13-gram decontamination method is used to identify and remove 0.026% items from the dataset.

Data Analysis
Comparison of four large publicly available reasoning datasets with NaturalReasoning.
Key Statistics:

Domain Diversity: Unlike datasets focused primarily on math (OpenMathInstruct-2, NuminaMath, MetaMathQA), NaturalReasoning covers a wider range of domains, including Physics, Chemistry, Computer Science, and Law.
Size: With 2.8 million unique questions, it’s larger than OpenMathInstruct-2, NuminaMath, and MetaMathQA, but smaller than WebInstruct (13M).
Question Length: NaturalReasoning questions average 55 words, significantly longer than other datasets, indicating richer context and multi-step reasoning requirements.

Quality:

Automatic Evaluation: Three strong LLMs (DeepSeek-R1-Distill-Qwen-32B, Qwen2.5–72B-Instruct, Llama-3–70B-Instruct) independently scored questions on a 0–10 scale. NaturalReasoning boasts the highest fraction of high-quality questions (93%) compared to other datasets.
Human Evaluation: Two expert annotators independently rated 100 randomly selected questions from each dataset. NaturalReasoning achieved the top mean score (6.45).

Difficulty:

Response Length Proxy: Llama3.3–70B-Instruct generated responses for randomly selected questions. NaturalReasoning exhibited the longest median response length (434 words), suggesting more intricate and reasoning-demanding questions.

Diversity:

Embedding Clustering: NaturalReasoning demonstrates a more diverse and dense representation of non-mathematical topics compared to WebInstruct, which is primarily skewed towards math.
Classifier Categorization: NaturalReasoning complements WebInstruct with better coverage on non-Math topics like Physics, Computer Science, and Social Science.

Reference Answers:

Availability: 81.68% of NaturalReasoning questions have reference answers derivable from pretraining data.
Length Distribution: Single-word answers (10.7%), short answers (2–9 words, 20.0%), and long answers (≥10 words, 50.9%) are prevalent.
Utility: Reference answers are valuable for filtering training data in knowledge distillation and enabling reinforcement learning with verifiable rewards (RLVR).

Steeper Scaling with Challenging and Diverse questions

Llama3.1‑8B‑Base and Qwen2.5‑7B were Supervised finetuned on NaturalReasoning and comparison datasets for 3 epochs.
Scaling results for Llama3.1–8B-Base model.
NaturalReasoning is more sample‑efficient than other datasets

Models trained on NaturalReasoning reach higher performance with fewer examples than those trained on other reasoning datasets.
With only 1.5M NaturalReasoning examples, Llama3.1‑8B‑Base surpasses Llama3.1‑8B‑Instruct, which was tuned with substantially more instruction‑following data.
Competing datasets (e.g., OpenMathInstruct‑2, WebInstruct) do not surpass Llama3.1‑8B‑Instruct even at 2.8M examples.

OpenMathInstruct‑2 excels in math but fails to generalize

OpenMathInstruct‑2 achieves the best MATH scores across all data sizes, improving from 50.83 (500K) to 59.25 (2.8M), confirming strong math‑reasoning supervision.
However, its performance on GPQA and MMLU‑Pro is weaker and does not improve meaningfully with more data:
GPQA accuracy hovers around 25.60–31.77 and plateaus/oscillates.
MMLU‑Pro accuracy fluctuates (e.g., 32.16 → 34.03 → 34.30 → 31.99) without clear gains.

Some datasets show diminishing or inconsistent returns with more data

WebInstruct’s GPQA performance peaks at 500K (29.02), drops at 1.5M (25.37), and only slightly recovers at 2.8M (26.12), indicating non‑monotonic scaling.
OpenMathInstruct‑2’s GPQA scores also fluctuate with data size rather than steadily improving.
Implication: Simply increasing dataset size does not guarantee better reasoning; data composition, quality, and diversity are more critical than volume.

Eliciting Long Chain-of-Thought

One thousand questions were randomly sampled from NaturalReasoning. DeepSeek-R1 was prompted on these questions, generating one long Chain-of-Thought (CoT) response per question. These responses ranged in length from 745 to 14.6K tokens, with an average length of 4,430 tokens. Llama-3.3–70B-Instruct was supervised fine-tuned on these DeepSeek-R1 responses. For comparison, Llama-3.3–70B-Instruct was also fine-tuned on two strong, heavily curated datasets (s1K-1.1 and LIMO). Responses for these datasets were also generated with DeepSeek-R1.
Pass@1 of Llama-3.3–70B-Instruct after distilling DeepSeek-R1 responses.
Quality of NaturalReasoning vs curated datasets (1K scale)

A random 1K subset of NaturalReasoning yields performance that matches or slightly exceeds that obtained from the curated s1K-1.1 and LIMO datasets after distillation.
This parity indicates that NaturalReasoning questions are diverse, challenging, and consistently high quality, even without heavy manual curation.

Data efficiency vs DeepSeek-R1-Distill-Llama-70B

Fine-tuning Llama-3.3–70B-Instruct on 100K randomly sampled NaturalReasoning questions brings its performance close to DeepSeek-R1-Distill-Llama-70B, which was trained on 800K examples.
With only one-eighth the data, the NaturalReasoning-trained model outperforms DeepSeek-R1-Distill-Llama-70B on GPQA-Diamond and MMLU-Pro, and is only slightly worse on MATH-500.
This demonstrates both the scalability and intrinsic quality of NaturalReasoning for long-CoT distillation.

Unsupervised Self-Training

GPQA-Diamond was used as the test set and the remaining GPQA questions served as seeds to retrieve similar questions from NaturalReasoning, forming a 15,000-question training set called SelfTrain-15k. Two unsupervised self-training methods were used:

Rejection-based sampling Fine-Tuning (RFT): sample 32 responses per question, score them, and fine-tune on the highest-scoring response.
Direct Preference Optimization (DPO): sample 32 responses, then form training pairs from the highest vs lowest-scoring responses.

External reward models

Qwen2.5-Math-RM-72B
INF-ORM-Llama3.1–70B

Self-consistency:

Select “best” response by most frequent final answer (extracted as \boxed{X}); choose “worst” response randomly.
Filter out responses without a clearly extractable final answer.

Self-scoring:

The model is prompted with (question, candidate response) and asked to judge if the response is valid.
Reward = log-probability difference between “yes” and “no” judgments.

Self-scoring with filtering:

For RFT: discard the top-ranked response if its self-score < 0.
For DPO: discard a preference pair if the preferred response has self-score < 0.
Unsupervised self-training results.
Self-training improves over baseline

Baseline Llama3.1–8B-Instruct: 40.81 average across GPQA-Diamond and MMLU-Pro.
Almost all self-training variants (RFT and DPO, with external or self-reward) improve over this baseline, showing that fine-tuning on high-quality model-generated responses is effective.

Self-reward is competitive with or better than external rewards

External reward models (e.g., INF-ORM-Llama3.1–70B) improve over baseline, but:
Self-score-filtered RFT and DPO achieve the best GPQA-Diamond score (35.02).
Self-score-filtered DPO achieves the highest overall average (43.67).
This shows self-reward mechanisms can match or surpass external reward models for guiding self-training.

Benefit of self-score filtering

Filtering low-confidence responses (self-score < 0) further boosts performance:
RFT: self-score-filtered average 42.54 vs unfiltered self-scoring 42.35.
DPO: self-score-filtered average 43.67 vs unfiltered self-scoring 43.22.
Indicates that removing low-confidence (noisy) responses improves training data quality and strengthens self-training.

Paper

NaturalReasoning: Reasoning in the Wild with 2.8M Challenging Questions 2502.13124

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on January 16, 2026.

Canonical link

Exported from Medium on May 4, 2026.
