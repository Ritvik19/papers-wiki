# Papers Explained 469: MobileLLM-R1

Papers Explained 469: MobileLLM-R1

Papers Explained 469: MobileLLM-R1

There have been two prevailing assumptions about reasoning models:

Papers Explained 469: MobileLLM-R1

There have been two prevailing assumptions about reasoning models:

reasoning capabilities only emerge in sufficiently large models
such capabilities require training on massive datasets.

While the first assumption has already been challenged by recent sub-billion-parameter reasoning models such as Qwen3–0.6B and DeepSeek distilled variants, the second remains largely unquestioned. In this work, the necessity of scaling to extremely large corpora (>10T tokens) for reasoning emergence is revisited. By carefully curating and resampling open-source datasets that are identified as beneficial under designed metrics, strong reasoning abilities can emerge with far less data.

The models are available on HuggingFace.

How do LLMs gain reasoning capability?

LLMs can be fundamentally understood as context-conditioned pattern reconstruction systems, where the central objective is to model the conditional probability distribution of the next token given its preceding context. This perspective frames LLM training as the process of refining a predictive distribution over the vocabulary space: learning, from large-scale data, the statistical regularities that govern natural language.

From this lens, the transition from a general-purpose LLM to a reasoning-specialized model can be interpreted as a systematic shift in token probability mass. That is, reasoning ability emerges not from an entirely new modeling paradigm, but from a redistribution of probability towards reasoning-relevant continuations when presented with certain contexts.

In the pre-training stage, the model is first exposed to a diverse corpus that grounds it in human language and general world knowledge. During this stage, it also acquires basic mathematical and reasoning capabilities. It is crucial to (1) include both types of data and (2) train them jointly:

Web data provides fundamental linguistic grounding without divergence, while math data develops reasoning capacity. This stage establishes a robust linguistic and conceptual foundation, enabling coherent next-token prediction across a wide range of inputs.

In the subsequent mid-training stage, we strategically shift the data distribution towards reasoning-rich domains such as mathematics, coding, and structured problem solving. This induces a gradual reallocation of probability mass towards reasoning-oriented continuations — analogous to how specialized education shapes cognitive priors in humans.

Finally, supervised fine-tuning (SFT) serves to align the model with human-preferred behaviors, equipping it with instruction-following capabilities and extended sequence handling. This final stage ensures that the reasoning ability acquired during earlier phases is accessible, controllable, and usable in practical interaction settings.

Methodology

Model Architecture
Architecture specifications of MobileLLM-R1.
The model architecture is based on designs from MobileLLM and LLaMA3.2. The LLaMA3.2 tokenizer with a 128k subword vocabulary is adopted. QK-norm is incorporated to mitigate training instabilities in the self-attention block. Weight sharing between the input and output embeddings is adopted, following MobileLLM, to improve parameter efficiency.

Training Recipe
Training setup across different stages.
Pre-training phase: Models are initialized from scratch and optimized with Adam (β1,β2,ϵ) = (0.9,0.95,10−8) and weight decay 0.1. The learning rate employs a 2k-step warmup followed by linear decay to 0.1×the peak value.
Mid-training phase: Optimization continues with Adam, where the learning rate decays linearly to zero. Knowledge distillation is applied with the Llama-3.1–8B-Instruct model as the teacher, where the student is trained by minimizing the KL divergence between its output logits and the teacher’s logits.
Post-training phase: Adam is used with zero weight decay. The learning rate warmup ratio is set to 0.03 for general-purpose SFT and 0.1 for reasoning-specific SFT, followed by linear decay to zero.

Data

Pretraining
Pre-training datasets and mixture ratios for the two-stage curriculum.
A two-stage pretraining curriculum is designed with carefully curated data sources:

Phase 1 emphasizes broad coverage through large-scale web and educational corpora such as FineWeb-Edu, which provide linguistic and domain diversity. At the same time, the mixture is seeded with reasoning-rich corpora, including OpenWebMath, Arxiv, and StackExchange, to expose the model early to mathematical and scientific discourse.
In Phase 2, the weighting is deliberately shifted toward specialized reasoning datasets — such as FineMath, OpenWebMath, Algebraic Stack, and Facebook Natural Reasoning — while the proportion of generic sources is reduced.

Mid-training
Mid-training datasets and mixture ratios.
For mid-training, a mixture is constructed that complements pre-training by targeting benchmarks and reasoning-intensive domains.

The first phase emphasizes coverage of general-purpose datasets (e.g., Dolmino DCLM baseline, FLAN, and peS2o) alongside curated knowledge sources such as Wiki and StackExchange.
In the second phase, the mixture is deliberately skewed toward math and coding corpora, particularly Dolmino Math, Nemotron-CC-Math, and Nemotron-Code, while reducing the weight of general-purpose datasets. A small but targeted set of benchmark-style datasets (e.g., GSM8K, ARC, OBQA) is also introduced to align training with downstream evaluation.

Post-training
Post-training data.
In the post-training stage, established post-training datasets are leveraged. Following standard practice, the model is first aligned with instructions through general supervised fine-tuning (SFT) and then reasoning-specific SFT is applied to extend the context length and promote a long chain-of-thought (CoT) reasoning style.

Final Results
Performance comparison of reasoning base models across multiple benchmarks.
MobileLLM-R1 consistently outperforms other fully open-source base models (OLMo, SmolLM) across all parameter scales.
At the 140M scale, MobileLLM-R1 dramatically surpasses SmolLM2–135M in GSM8K (16.3% vs. 1.8%) and HumanEval (15.9% vs. 0.0%).
MobileLLM-R1 achieves comparable or superior results to prior partially open-source base models (e.g., Qwen3–0.6B) despite being trained on substantially fewer tokens (4.2T for MobileLLM-R1 vs. 36T for Qwen3).
MobileLLM-R1–950M attains the highest HumanEval score (46.3%) among all sub-1B base models, significantly outperforming Qwen3–0.6B (30.5%).
Evaluation results of different reasoning models.
For post-trained models, MobileLLM-R1–360M achieves 5.1 points on LiveCodeBench, surpassing models with over 1B parameters (e.g., SmolLM2–1.7B, Gemma3–1B, LLaMA3.2–1B), indicating strong performance for its size in coding tasks.
MobileLLM-R1–950M demonstrates a substantial accuracy gain over Qwen3–0.6B on LiveCodeBench and matches the performance of much larger state-of-the-art models like DeepSeek-R1-Distill-Qwen-1.5B.
Across Math and AIME benchmarks, MobileLLM-R1 consistently outperforms other fully open-source models and achieves scores comparable to the partially open-source Qwen3 series.
Models with fewer than 150M parameters do not yield reliable MMLU scores, and models with fewer than 400M parameters do not produce reliable AIME scores.

Pre-training: Balance of Capabilities

Selecting Informative Datasets for Target Capability

To systematically assess which pre-training distributions most effectively support downstream reasoning behaviors, a leave-one-out (LOO) analysis is designed. Models are trained from scratch on the entire set of pre-selected high-quality datasets, excluding one dataset at a time. Negative log-likelihood on curated capability-probing datasets is then traced throughout training.
Hierarchical rejection sampling.
To derive a compact capability-probing datasets for each domain, a hierarchical rejection sampling pipeline that integrates multiple classifiers is employed. The objective is to construct a small yet representative target dataset for each capability, such that it can serve as a faithful proxy for reasoning performance while dramatically reducing overall volume during evaluation.

For each pretraining corpus in Table 3, the FineWeb-Edu classifier is first applied, retaining only those with classifier scores above 4. Next, each remaining sample is scored using the Ask-LLM paradigm. The evaluation prompt asks the model to judge whether a sample should be included in a reasoning-probing dataset, framed as a binary classification task (“1” for inclusion, “0” for exclusion). Rather than relying solely on the hard prediction, the probability assigned to “1” is recorded as a graded measure of the model’s confidence in the example’s reasoning relevance. The top 10% samples within each dataset are selected.

Next, a domain-specific prompt is applied to Ask-LLM for each capability with specific emphasis on code, math, general knowledge or combined. Finally, semantic deduplication across corpora is performed, shrinking each dataset to a subset of roughly 10,000 examples. This yields the representative datasets DR. They are categorized into three domains according to their composition: Code ©, Math (M), and Knowledge (K).:

C= {StarCoder, StackExchange, Nemotron-Code, Cosmopedia, Natural Reasoning, pes2o}
M= {OpenWebMath, FineMath, Algebraic Stack, Nemotron-Math, Cosmopedia, Natural Reasoning, pes2o}
K= {FineWeb-Edu, Wikipedia, Arxiv, Cosmopedia, Nemotron-Science, Natural Reasoning, pes2o}
Leave-one-out analysis of pretraining data.
Excluding Fineweb-Edu results in the largest degradation across all capabilities, including knowledge, math, and code.
In contrast, domain-specific datasets primarily strengthen their respective domains.
An unexpected observation is that Starcoder benefits math more than OpenWeb-Math benefits code, a reversal of the commonly held view that mathematical data contributes disproportionately to coding ability.
Wikipedia appears to contribute little to math or code compared to web or domain-specific data, yet remains necessary as a structured and reliable source of factual knowledge.

Datamixing via Cross-Capability Self-Influence

Given a fixed training budget, the question arises: how should tokens be distributed across heterogeneous datasets to maximize downstream reasoning performance? Uniform sampling provides a natural baseline but ignores the varying marginal utility of different datasets. The key insight is that more informative datasets should receive proportionally larger sampling ratios. To operationalize this, an influence score is used, it measures how much a specific training example xi affects the loss on a target test example xtest. Mathematically, it’s approximated as:

θ* are the model parameters trained on dataset D.
L(x, θ) is the loss function.
Hθ* is the Hessian of the training loss at θ* (a square matrix of second-order partial derivatives of the training loss function with respect to the model’s parameters).

Directly computing the Hessian matrix Hθ* and its inverse is computationally prohibitive for large models, hence the authors leverage AutoMixer, which proposes an efficient approximation method that bypasses explicit Hessian inversion, making influence score calculation scalable.

For each training sample xi from a source dataset, its influence is computed on the validation loss of all three capability-probing datasets.

Self-influence: Occurs when training and validation samples originate from the same capability.
Cross-influence: Occurs when training and validation samples target different capabilities.

The checkpoints θC,t, θM,t, and θK,t are obtained by training separate models to convergence on the full training sets of domains C, M, and K, respectively, yielding domain-specialized parameters. A single checkpoint is insufficient to capture the full training dynamics. Therefore, influence scores are computed at T = 10 evenly spaced checkpoints. The joint influence of a sample xi is computed by summing its weighted influences across all checkpoints and capabilities, which is then used to assign a sampling weight (wg) to each source dataset g:

Ng is the token count of dataset g.
si is the length of sample xi.

Mid-training: Knowledge Compression

After the model has been exposed to broad knowledge during pretraining, the mid-training phase focuses on compressing this knowledge and maximizing performance on target tasks. The Dolmino dataset is augmented with additional mathematics and programming data, aiming to strengthen the model’s math and coding capabilities.

Given a training example xi from the mid-training dataset and a probe example xtest from capability probing dataset D_C,M,K, the influence score I(xi,xtest; θ) is calculated using the pretrained model θ. The data–model co-evolution proceeds iteratively through the following steps:

Sample-level Influence for Rejection Sampling: This step acts as a filtering mechanism. Only training examples that positively contribute to the target capabilities are retained, while neutral or detrimental samples are discarded.
Dataset-level Influence for Adaptive Data Mixing: Beyond individual sample filtering, influence scores are aggregated to the dataset level. This enables adaptive control of the mixing ratio among different mid-training datasets.
Train the Model on Curated Data and Repeat: The compressed dataset with the updated mix ratio is used for continued mid-training. The newly updated model then provides refined influence scores for the next stage of the process.
This iterative compression continues until no additional samples yield a positive influence score.

Post-Training

Datasets

Tülu-3-SFT is a large, curated collection of prompts and instruction-answer pairs designed for post-training language models across skills such as reasoning, coding, and math. It combines publicly available datasets with synthetically generated data. tulu-3-sft-olmo-2-mixture-0225, which is a latest filtered version of the Tulu-3 dataset, is used.

OpenMathReasoning is a large-scale dataset for training models in complex mathematical reasoning. It contains 3.2M long chain-of-thought (CoT) solutions for 306K unique mathematical problems, helping models improve problem-solving skills in mathematics.

OpenScienceReasoning-2 is a synthetic dataset spanning multiple scientific domains. It contains 803k general-purpose reasoning data, including STEM, law, economics, and humanities, featuring both multiple-choice and open-ended questions, designed to enhance scientific reasoning capabilities.

OpenCodeReasoning-2 is a large-scale dataset for programming reasoning. It contains 1.4M Python and 1.1M C++ samples, covering nearly 35K unique competitive programming problems. It is intended to improve code completion abilities in models.

Ablations
Ablation studies on post-training stages.
Instruction-following supervision provides a strong foundation for reasoning. Models that are first trained with Tulu-SFT data consistently outperform those that start directly from reasoning data. This demonstrates that high-quality instruction-following supervision provides alignment signals making subsequent reasoning adaptation more effective.

Domain-specific data improves performance in its own domain. OpenMathReasoning,OpenScienceReasoning-2, and OpenCodeReasoning-2 improve performance on math, code, and knowledge-intensive benchmarks (e.g., MMLU), respectively. These effects are highly consistent, showing that specialized datasets provide targeted benefits.

Scientific reasoning data generalizes across domains. Beyond its impact on MMLU, adding science data also improves performance on math and coding tasks compared to using only math and coding data. This suggests that scientific reasoning provides broadly useful structures that transfer across different forms of symbolic problem-solving.

Introducing math or coding data tends to reduce performance on MMLU. This is hypothesized to be due to limited model capacity: when the model is pushed to absorb new symbolic reasoning skills through exposure to math and coding data, it partially forgets factual knowledge that is important for knowledge-intensive evaluation. This forgetting effect is especially pronounced in smaller models.

Compared to models trained with Tulu and reasoning data jointly in a single stage, a two-stage setup of first training on Tulu, then on reasoning data delivers overall stronger results especially on math and general reasoning benchmarks.

Whether to Use RL or Not

To assess the impact of reinforcement learning (RL) on small reasoning models, an ablation study is performed by applying an RL stage to both the base model and the final model, i.e., fine-tuned with SFT data. The base model is finetuned for 100 steps on the TULU3 dataset (1% of total data) as a cold start, solely to learn the correct output format. Subsequently, both the base and SFT models undergo GRPO training on the NuminaMath-TIR dataset.
Accuracy and sequence length during RL fine-tuning on MobileLLM-R1 base model and final model after SFT.
Small models can also benefit from RL-based fine-tuning when they are well-pretrained on a suitable corpus. Results show that MobileLLM-R1–950M-base achieves evident improvements in reasoning accuracy as the average length gradually increases.

Supervised fine-tuning (SFT) data distilled from large models consistently yields higher performance than directly applying RL to small models, corroborating prior findings. For instance, the final GSM8K accuracy of RL-optimized MobileLLM-R1–950M-base is 57.0, compared to 74.0 for the SFT-trained MobileLLM-R1–950M.

For high-performing small models fully fine-tuned on SFT data, additional RL does not observe a significant performance improvement. This suggests that SFT provides more structured and reliable supervision than the noisy self-exploration signal accessible to small models, which often lack the capacity to further refine their reasoning policies beyond the distilled demonstrations.

Paper

MobileLLM-R1: Exploring the Limits of Sub-Billion Language Model Reasoners with Open Training Recipes 2509.24945

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on October 7, 2025.

Canonical link

Exported from Medium on May 4, 2026.
