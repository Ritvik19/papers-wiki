# Papers Explained 374: Sarvam-M

Papers Explained 374: Sarvam-M

Papers Explained 374: Sarvam-M

Sarvam-M (M stands for Mistral) is a finetuned Mistral Small 24B. It significantly improves on the base model with large relative…

Papers Explained 374: Sarvam-M

Sarvam-M (M stands for Mistral) is a finetuned Mistral Small 24B. It significantly improves on the base model with large relative increases: +20% average improvement on Indian language benchmarks, +21.6% on math benchmarks, and +17.6% on programming benchmarks.

Supervised finetuning

A large number of finetuning datasets, with completions from different models, are available on Hugging Face. In experiments in training with these datasets, inconsistent quality, large overlap amongst each other, significant content that is biased to specific countries, and very little high quality data for Indian languages are found. Thus, a pipeline is created to curate a finetuning set from scratch.

Curating Diverse Prompts

Over 11.5 million prompts were collected from selected Hugging Face finetuning datasets. Using min-hash and fuzzy algorithms, this was reduced to about 7 million prompts. These prompts, in various languages, were filtered to 5.2 million English prompts using simpler lang-detect models and Gemma 2 9B. Each prompt was then classified for quality, hardness, and categorized into 16 broad categories using Llama 3.3 70B.

Recognizing the need for a more refined sampling strategy, each prompt was embedded using the gte-Qwen2–7B model and clustered into 100,000 clusters. Semantic deduplication within each cluster was performed with a cosine similarity threshold of 0.8. Higher quality and more difficult prompts were prioritized, resulting in a set of 3.7 million samples with improved characteristics.
Category DistributionQuality DistributionDifficulty Distribution
These English prompts were partially translated into Indian languages, with about one-third used for completions in Indic languages. Specifically, 30% of coding, math, and reasoning prompts, and 50% of other prompts were translated. The translations included 28% in Hindi and 8% each in Bengali, Gujarati, Kannada, Malayalam, Marathi, Oriya, Punjabi, Tamil, and Telugu, covering the first language of over 70% of the Indian population. Three forms of Indian language representations were used: formal native script, code-mixed, and transliteration. The translations were done using Llama 3.1 8B models, with expert oversight, resulting in 50% in native script, and 25% each in code-mixed and romanized scripts.

Prompt Completions

Before creating prompt completions, various methods to measure the quality of generated completions are assessed. A seed corpus of 30K diverse prompts from a prompt bank is used, and completions are generated from four models: Llama 3.3 70B, Qwen 2.5 72B, Gemma 2 27B, and Gemini 1.5. Gemini 1.5 Pro then evaluates the quality of these 120K prompt responses by providing reasoning and a quality score between 0 and 9. This data is used to finetune Llama 3.3 70B to generate both reasoning and scores. This ‘generative scorer’ is found to be superior to classifier-based reward models that use log-prob to decide scores. However, the model showed a bias for low (0–2) and high (7–9) scores. To address this, a hybrid ‘real-value scorer’ is defined: the model generates reasoning and a score within a tag, but instead of using the generated score, the log-probs of that score token are used to compute a probability-weighted score across digits 0 through 9, resulting in a real-value score.
where p_i is the probability of digit i at the score token.
The real-valued scoring approach is used to compare three models: Llama 3.3 70B, Deepseek v3, and Deepseek R1. For outputs in formal Indic languages, Deepseek R1, with English thinking tokens and Indic language output in non-thinking tokens, generates the highest quality completions, averaging over 8 (on a 0 to 9 scale) across each of the 10 Indic languages. However, for code-mixed and romanized prompts, none of the models produce good results, so translation models trained internally on Llama 3.1 8B are used to convert formal Indic language outputs to these modified forms.

To further enhance Indic language skills, document and sentence-level translation pairs are added in various combinations of English, Indic language in native script, Indic language in romanized script, and colloquial Indic language with code-mixed scripts. The source text comes from Wikipedia and the BPCC dataset. Cross-lingual datasets are also generated where a prompt explicitly requests a response in a different language. Responses in English are prompted, and necessary transformations are made with the models. Vocalization data is also generated, converting input sentences with code-mixing, normalization, abbreviations, URLs, etc., to a spoken form in Indic language scripts.

Character Training

An increasingly important aspect of model alignment is ensuring a consistent character across responses, transforming it from a basic token predictor to an AI assistant.

The initial phase of character training focused on addressing political bias. To identify biased prompt-response pairs, Llama 3.3 70B with a customized prompt was employed to detect bias towards political entities, ideologies, geographical regions, cultural groups, nationalities, and races. Approximately 0.5% of the prompt-response pairs were flagged. For these identified prompts, responses were regenerated by either (a) using a debiased model — Perplexity R1 1776, or (b) adjusting the prompt to answer the question with a specific cultural tone.

While this process removes specific political and related biases, there was also a need for responses to be relevant to an Indian context. Prompt-response pairs requiring cultural relevance, geographical saliency, daily life and customs, or reflecting local educational or professional settings were identified using a custom prompt with Llama 3.3 70B. About 5% of the prompts were flagged for regeneration. These outputs were regenerated with a customized prompt to induce the desired bias.

Supervised Finetuning

Using the created dataset, the Mistral 3.1 24B model was finetuned. Initially, the vision encoder was removed. Training was conducted for a hybrid model in both ‘non-think’ and ‘think’ modes. In the ‘think’ mode, the model generates reasoning tokens within <think>…</think> tags in English before producing its final response in the target language.

Interestingly, simultaneous training for both think and non-think modes was ineffective. This indicated that to enhance the base model’s relatively lower performance on Indian languages, training needed to be prioritized in the non-think mode first, which contained a substantially higher proportion of Indian language tokens.

Based on these findings, a two-phase training approach was implemented: 2 epochs in non-think mode, followed by 2 epochs in think mode. Model merging techniques were also employed between and after these training phases.

Experiments included testing both Dare-Ties and Slerp algorithms with various checkpoint combinations. The most effective method proved to be merging the epoch 1 and epoch 2 checkpoints after each training phase using the Slerp algorithm. The resulting merged model demonstrated performance equal to or better than the constituent models across nearly all benchmarks evaluated.

Reinforcement Learning

Curriculum of Tasks

In initial experiments, batches of data from multiple tasks were combined into a single RLVR run. However, joint training led to several challenges:

Imbalanced learning: The model prioritized easier instances across tasks, while harder, more critical examples saw limited improvement.
Verification inefficiency: Verification time varied widely across datasets — some required significantly more time, bottlenecking the process. Additionally, coding tasks benefit from batched verification, which isn’t feasible when mixing samples from multiple datasets.
Sequence length mismatch: Different datasets required different maximum sequence lengths. A high sequence length setting (needed for some tasks) negatively impacted training efficiency and performance on tasks with shorter inputs.

Based on several ablation studies, a sequence is designed that alternates between reasoning and language tasks to foster balanced skill development:

Math Skills (GSM8K and MATH): Uses a multilingual approach with English, native Indian script, and romanized Indian script prompts (40% English, 40% native Indian, 20% romanized Indian, with 28% of Indian content in Hindi and 8% in each of the other nine languages). Fixed format responses were used for easier extraction, proving more effective than few-shot prompting, especially for Indian languages.
Advanced Mathematics (Big Math): Uses more challenging math problems, with responses generated within a LaTeX box for easy verification.
Instruction Following (Extended IFEval): Uses an expanded IFEval dataset with Indian language tasks and multi-turn interactions. A subset of constraints from the original IFEval paper was used, including “Numbered Bullets,” “Title,” and “Minimum Number of Highlighted Sections.” Sequencing these tasks early in the curriculum improved performance across benchmarks.
Code Understanding: Predicts code output given a snippet and input, requiring an exact match for verification. Uses the Synthetic-1 dataset and translates prompts into Indian languages.
Code Generation: Uses a high-quality subset of the PrimeIntellect dataset, requiring sandboxed code execution and flexible matching criteria (whitespace variations, numerical approximations). Focused on ‘stdin-stdout’ tasks.
Translation: Improves English-Indian language translation in both directions, rewarding higher chrF++ scores compared to a baseline.

Group Relative Policy Optimization (GRPO) is adopted. For each RLVR task, a prompt sampling approach targeting a pass-through rate of approximately 20% on the model being trained is implemented.

Reward Engineering

For most RLVR tasks, a straightforward binary reward system was employed, classifying responses as either correct or incorrect.

The Code Generation reward consisted of two components:

the fraction of test cases that successfully passed code execution
a bonus reward applied when all test cases passed.

For Translation tasks, a ‘relative reward score’ was developed with the following structure:

a score of 0.5 if the chrF++ metric exceeded the pre-RLVR baseline by a specified lower threshold,
a score of 1.0 if the chrF++ metric either exceeded the baseline by a higher threshold or surpassed a predefined global chrF++ threshold.

Evaluation

Sarvam-M demonstrates superior or highly competitive performance across diverse benchmarks.
Sarvam-M excels in Indian language tasks, programming, mathematical reasoning, and multilingual capabilities.
Sarvam-M outperforms other models on Indic-focused benchmarks, particularly IndicGenBench, MILU-EN, and MILU-IN.
Sarvam-M leads on regionally adapted general knowledge evaluations like MMLU-IN and ARC-C-IN, and achieves the highest overall score on ARC-C.
Sarvam-M achieves the highest scores on HumanEval, MBPP, and LivecodeBench in programming benchmarks.
Sarvam-M achieves the highest performance on GSM-8K-IN, GSM-8K-IN-R, and maintains competitive scores on GSM-8K and the MATH benchmark in mathematical reasoning tasks.

Indic Vibe Check

To evaluate user engagement with the model, “Indic Vibe Check” was developed. This benchmark helps understand the model’s effectiveness in various conversational contexts, avoiding over-optimization for standard benchmarks. Based on Anthropic’s Economic Index, tasks were created from individual entries and Gemini-1.5-Pro was prompted to generate realistic user chat queries. A streamlined prompt engineering method was used to create scenarios in 11 languages, reflecting global usage patterns. After rigorous quality control to remove substandard or erroneous prompts, a dataset of about 3,000 diverse conversational scenarios was compiled.

Failed Experiments

Tokenizer Extension

To decrease the fertility scores of Indian languages and improve inference throughput, the vocabulary of Mistral Small was extended with additional Indian language tokens. This approach resulted in a significant drop in the model’s knowledge base and persisted even after extensive SFT.

RL with LLM-Based Rewards

Using LLM-based verification as a reward signal in RLVR for programming tasks did not yield consistent performance improvements. A key limitation was the non-deterministic nature of these evaluations, which introduced instability in reward attribution.

Tokenizer Transplant

Soft distillation from larger models requires identical vocabularies between teacher and student models. Since the student model (Mistral Small) and potential teachers (Llama 3.3 70B, Deepseek R1, etc.) use different vocabularies, a transplantation approach was used:

For tokens existing in both vocabularies, the original embeddings from the student model were directly copied to preserve exact representations.
For tokens unique to the teacher model, k-nearest neighbors among common tokens between teacher and student were identified. Then, the student’s embeddings of these neighbors were used to approximate new token embeddings through barycentric interpolation.
For special cases like byte tokens, fallback logic such as prefix matching was implemented before resorting to approximation methods.

The merged embeddings maintained the student’s embedding dimension while expanding to accommodate the teacher’s vocabulary, effectively transplanting the teacher’s tokenization capabilities while preserving the student’s semantic representation space.

With aligned vocabularies, the student was fine-tuned to learn the log-probability distribution of the teacher using its top-20 logits. A combination of cross-entropy and Kullback-Leibler divergence losses was employed for optimization. Though the student model rapidly learned to mimic the teacher distribution, it required longer training and more data to recover performance lost due to vocabulary changes. This process did not outperform a simple SFT procedure.

Paper

Sarvam — M: ‍Explorations in Post Training and Inferencing Optimizations for a Hybrid Indic LLM

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on May 27, 2025.

Canonical link

Exported from Medium on May 4, 2026.
