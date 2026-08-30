# Papers Explained: GRAPE

Papers Explained: GRAPE

Papers Explained: GRAPE

GRAPE is a novel SFT framework that accounts for the unique characteristics of the target model. For each instruction, it gathers…

Papers Explained 503: GRAPE

GRAPE is a novel SFT framework that accounts for the unique characteristics of the target model. For each instruction, it gathers responses from various LLMs, and selects the one with the highest probability measured by the target model, indicating that it aligns most closely to the target model’s pretrained distribution; it then proceeds with standard SFT training.

Methodology
An overview of GRAPE.
The key idea is to find responses among a candidate pool for each instruction xi such that they align closely with the base model’s pretrained distribution πθ0.

GRAPE consists of two main steps, followed by standard SFT:

Response Collection: Collect a pool of high-quality candidate responses either from existing datasets or sampling from multiple LLMs.
Customization: For the target model to be fine-tuned πθ0 , find the response(s), for each instruction, that are closest to the pretrained distribution of πθ0.

Collecting Responses from Existing Resources

For instruction-tuning of language models, high-quality instructions are more difficult to collect than responses. Therefore, it is a common practice to reuse existing instruction-tuning prompts while generating diverse responses using various methods tailored to specific requirements. For instance, instructions from Flan, OpenOrca, ShareGPT, and the training splits of GSM-8K, MATH, and CodeContests are frequently reused in datasets like Olmo, Tulu, OpenHermes, OpenOrca, MetaMath, MathInstruct, UltraFeedback, and UltraInteract, whether for SFT or preference learning. The solutions are generated using different models or follow varying styles depending on the specific needs. This naturally leads to a situation where a single instruction with multiple responses becomes a readily available resource.

Responses for the i-th instruction are collected from various datasets to form Ri = {y^j_i : j = 1,…,J(i)}, where J(i) denotes the number of responses collected for the i-th instruction.

Customize Dataset For Models

The conditional probability of each response πθ0 (y^j_i|xi) is computed. Responses are ranked based on the conditional probability and those with the highest probability for each instruction are taken. Notably, GRAPE’s selection process requires only a forward pass through the candidates and does not require gradient computation.

Preliminary Experiments

UltraInteract-SFT contains approximately 80,800 unique instructions covering coding, math (chain-of-thought and program-aided) and logic reasoning domains. Each instruction is paired with varying numbers of different responses to contain a total > 280,000 training examples.

Responses are collected from a diverse set of models of various sizes across model families, including MIXTRAL-7X7B-INSTRUCT, CODESTRAL-22B, MISTRAL-SMALL, LLAMA-3.1–70B-INSTRUCT and LLAMA-3.1–405B-INSTRUCT, and QWEN2.5–72B-CHAT, resulting in approximately 10x additional responses per instruction. The responses are then filtered based on the answers to ensure their validity.

For each instruction, GRAPE is used to select the top-ranking responses, ensuring that the number of responses matches the original UltraInteract-SFT dataset for fair comparisons.

Base Models: LLAMA-3.1–8B, LLAMA-3.2–3B, MISTRAL-7B and QWEN2.5–7B.
Evaluation Benchmarks: HumanEval, MBPP, LeetCode, MATH, GSM-Plus, and TheoremQA
Baselines: The original dataset, responses from the strongest model (LLAMA3.1–405B-INSTRUCT), and an up-scaled dataset with three times the responses.
Result of synthetic experiment on UltraInteract-SFT.
Performance Summary: GRAPE consistently outperformed various baselines across benchmarks.
Improvement Over Strongest Model: GRAPE-selected solutions showed up to 13.8% absolute improvement over responses from LLAMA3.1–405B-INSTRUCT.
Importance of Customization: Customization for base models should be prioritized over identifying the highest-quality responses, verifying the central premise that in-distribution responses boost downstream performance.
Effect of Scaling Data: Adding more responses does not always lead to continuous improvement. GRAPE outperformed models trained with 3x responses by at least 3.6% and up to 17.3% absolute improvement, reinforcing the notion that alignment with the base model’s distribution is crucial.

Experiments

Overlapping instructions from TULU-3 and OLMO-2 models were collected and corresponding responses were gathered. Only the winning responses from the preference data were retained. A candidate pool was formed with instructions having at least two distinct responses, resulting in a dataset of 350.4k unique instructions and about 1.03 million total instruction-response pairs.

Evaluated on benchmarks like LeetCode, MATH, BigBench-Hard (BBH), MMLU, and AlpacaEval-V2 using zero-shot, 3-shot, and other methods as appropriate.
GRAPE on the Tulu-Olmo collection.
Models fine-tuned on responses selected by GRAPE outperformed strong baselines, including those trained on all available data.
GRAPE achieved better performance with roughly 1/6 of the training computation compared to TULU3–8B-SFT.
GRAPE outperformed state-of-the-art data-selection approaches like S2L, highlighting its effectiveness and efficiency.
GRAPE can leverage established datasets to customize a dataset for each base model, improving fine-tuning outcomes without synthesizing new data.
Consistent improvement across models reaffirmed GRAPE’s utility as an adaptive response selection mechanism for enhancing SFT performance.
GRAPE can optimize responses from a single generator, further boosting performance when applied to responses from a strong model.

Paper

The Best Instruction-Tuning Data are Those That Fit 2502.04194

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on December 17, 2025.

Canonical link

Exported from Medium on May 4, 2026.
