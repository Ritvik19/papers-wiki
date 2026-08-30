# Papers Explained 352: Skywork-Math

Papers Explained 352: Skywork-Math

Papers Explained 352: Skywork-Math

This research investigates the underlying factors that potentially enhance the mathematical reasoning capabilities of large language models…

Papers Explained 352: Skywork-Math

This research investigates the underlying factors that potentially enhance the mathematical reasoning capabilities of large language models (LLMs). The data scaling law for math reasoning capabilities in modern LLMs is far from being saturated, highlighting how the model’s quality improves with increases in data quantity. The Skywork-Math model series is supervised fine-tuned (SFT) on common 7B LLMs using the proposed 2.5M-instance Skywork-MathQA dataset.

Method
Overview of the proposed two-stage method.
A two-stage SFT approach, in conjunction with two data synthesis pipelines, is employed to produce high-quality data.

In stage 1, base pre-trained models are fed with generated normal synthetic problems to produce an intermediate model.
In stage 2, to mitigate the diminishing returns in LLMs’ performance as the quantity of data increases, hard synthetic problems are generated and Skywork-Math models are developed.

To ensure the quality of data, GPT-4 is utilized to generate a 2.5M-instance synthetic Skywork-MathQA dataset.

Seed Problems: Publicly available high-quality mathematical datasets are adopted to generate the Skywork-MathQA dataset. To prevent data leakage in the testing phase, only the training sets from the following data sources are used: MATH, non-proving problems from OlympiadBench, mathematical problems from the AGIEval benchmark, and various problems in calculus, differential, statistics domains from SciBench and JEEBench.

The data synthesis process in the Skywork-MathQA dataset consists of two stages.

In stage 1, 2.1 million normal synthetic problems are generated.
In stage 2, 0.4 million hard synthetic problems are further generated.

The Skywork-Math models are instructed to use the prefix “\nThe answer is “ before generating answers in their responses.

Stage 1: Normal Synthetic Problems

To ensure diversity in synthetic data, three distinct methods are employed to augment the Skywork-MathQA dataset.

The first data augmentation method, MetaMathQA, comprises four specific approaches: three for query bootstrapping and one for response augmentation. For response augmentation, the corresponding query is left unchanged and GPT-4 is employed to refine its response. For query bootstrapping, the rephrasing method utilizes pre-defined prompts to generate more questions, followed by the few-shot Chain-of-Thought (COT) prompting to generate answers. Additionally, the FOBAR and self-verification methods deterministically convert the problem into a backward format to mimic backward reasoning, i.e., given the result and think backward to determine the unknown variable in the question. After transforming the questions, corresponding answers are generated with COT techniques using GPT-4.

The second data augmentation method is the Evol-Instruct approach, as implemented in WizardLM. Starting from the initial set of mathematical problems, Evol-Instruct iteratively rewrites them step by step into more complex queries. The maximum length of the evolutionary trajectory is set to five steps and the following five augmentation strategies are employed:

Rewrite the original problem to create a completely new problem of similar length and difficulty.
Add constraints and requirements to the original problem.
Increase the complexity of the original problem in both depth and breadth.
Replace general concepts with more specific ones.
Explicitly request additional steps in the reasoning process of the original question.

The third data augmentation method is question generation with self-correction, as practiced in Xwin. Specifically, GPT-4 is instructed to refine the input question and then verify it step-by-step to assess its logical and mathematical consistency. If the question is found to be imperfect, GPT-4 is instructed to modify it based on the verification results.

To improve the diversity of seed problems, the core-set approach is employed. This approach selects a representative subset of data that maximizes diversity while maintaining coverage of the original dataset’s key features. Data synthesis is first performed on the initial seed problems, and then the core-set approach is applied to obtain seed synthetic problems. Further data synthesis is performed on these seed synthesis problems to get the normal synthetic problems with 2.1 million instances.

Stage 2: Hard Synthetic Problems

As the quantity of data increases, empirically, the relationship between performance and data quantity begins to plateau. Motivated by the concept of curriculum learning, stage 2 in the data synthesis pipeline is specifically designed for models to focus on mastering the more challenging problems. In this stage, challenging problems, i.e., those categorized as Level 4 or Level 5 in the MATH dataset, are utilized to generate additional 0.4 million query-response pairs.

Evaluation
Summary of math reasoning performance of closed- and open-source LLM models in terms of accuracy (%).
Skywork-Math models achieved state-of-the-art performance on the MATH benchmark among LLMs smaller than 10B parameters using only Supervised Fine-Tuning (SFT). They even surpassed an early version of GPT-4. This suggests that strong math reasoning abilities can be developed during the SFT stage with a high-quality dataset like Skywork-MathQA.
Skywork-Math 7B models achieved accuracy comparable to 70B LLMs on the MATH benchmark, indicating that smaller models can achieve strong math reasoning with sufficient SFT. This highlights the effectiveness of the proposed two-stage data synthesis and model SFT pipeline.
Skywork-Math models achieved comparable performance on the GSM8K benchmark despite the training data not including GSM8K examples. This suggests that knowledge learned from solving competition-level math problems (MATH) can transfer to solving math word problems (GSM8K), especially since the easier problems in MATH have similar difficulty to GSM8K problems. This transfer learning is attributed to the similarity in difficulty between easier MATH problems and GSM8K problems.
The zero-shot top1 performance of Skywork-Math 7B model series.
Scaling Law: Increasing the size of the synthetic SFT dataset leads to improved performance on mathematical reasoning tasks.
Quantity over Specialized Pre-training: While a specialized pre-trained model (DeepSeekMath 7B) initially outperforms general-purpose models, increasing the size of the synthetic SFT dataset allows the general-purpose models to eventually surpass the specialized model’s performance. This suggests that large quantities of SFT data can compensate for specialized pre-training.
Impact of Problem Difficulty: Including more difficult problems in the synthetic dataset leads to significant performance gains, particularly when scaling from 2.1M to 2.5M examples. This highlights the importance of incorporating challenging problems to improve the model’s reasoning capabilities.

Paper

Skywork-Math: Data Scaling Laws for Mathematical Reasoning in Large Language Models — The Story Goes On 2407.08348

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on April 22, 2025.

Canonical link

Exported from Medium on May 4, 2026.
