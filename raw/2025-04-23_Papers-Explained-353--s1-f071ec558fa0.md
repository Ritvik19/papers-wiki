# Papers Explained 353: s1

Papers Explained 353: s1

Papers Explained 353: s1

This work curates a small dataset s1K of 1,000 questions paired with reasoning traces relying on three criteria validated through…

Papers Explained 353: s1

This work curates a small dataset s1K of 1,000 questions paired with reasoning traces relying on three criteria validated through ablations: difficulty, diversity, and quality. Second, budget forcing is developed to control test-time compute by forcefully terminating the model’s thinking process or lengthening it by appending “Wait” multiple times to the model’s generation when it tries to end. This can lead the model to double-check its answer, often fixing incorrect reasoning steps.

The project is available on GitHub.

Reasoning data curation to create s1K

Initial collection of 59K samples

An initial 59,029 questions are collected from 16 sources, following three guiding principles. Datasets should be high-quality; samples are always inspected and datasets with, e.g., poor formatting are ignored. Datasets should be challenging and require significant reasoning effort. Datasets should stem from various fields to cover different reasoning tasks.
Composition of full 59K questions.
All samples are decontaminated against evaluation questions (MATH500, GPQA Diamond, AIME24) using 8-grams and the data is deduplicated.

Final selection of 1K samples

Three stages of filtering are used to arrive at a minimal set of 1,000 samples based on three guiding data principles: Quality, Difficulty, and Diversity.

First, any questions where API errors occurred are removed, reducing the dataset to 54,116 samples. Next, low-quality examples containing string patterns with formatting issues, such as ASCII art diagrams, non-existent image references, or inconsistent question numbering are filtered out, reducing the dataset to 51,581 examples. From this pool, 384 samples are identified for the final 1,000 samples from datasets perceived as high-quality and not in need of further filtering.

For difficulty, two indicators are used: model performance and reasoning trace length. Two models, Qwen2.5–7B-Instruct and Qwen2.5–32B-Instruct, are evaluated on each question, with correctness assessed by Claude 3.5 Sonnet comparing each attempt against the reference solution. The token length of each reasoning trace is measured using the Qwen2.5 tokenizer to indicate problem difficulty, assuming that more difficult problems require more thinking tokens. Questions that either Qwen2.5–7B-Instruct or Qwen2.5–32B-Instruct can solve correctly are removed, as they may be too easy, bringing the total samples down to 24,496.

To quantify diversity, questions are classified into domains using Claude 3.5 Sonnet based on the Mathematics Subject Classification (MSC) system from the American Mathematical Society. To select the final examples from the pool of 24,496 questions, one domain is chosen uniformly at random. Then, one problem from this domain is sampled according to a distribution that favors longer reasoning traces. This process is repeated until 1,000 total samples spanning 50 domains are obtained.
Summary of s1K dataset.
Some distilled generations are incorrect, which is allowed as the focus is on capturing the reasoning process rather than entirely correct solutions. 53.6% are deemed correct in s1K and 63.0% in the follow-up s1K-1.1.

Test Time Scaling

Test-time scaling methods are classified into 1) Sequential, where later computations depend on earlier ones (e.g., a long reasoning trace), and 2) Parallel, where computations run in- dependently (e.g., majority voting). The focus is on sequential scaling. New sequential scaling methods and ways to benchmark them are proposed.

A maximum token count is enforced by simply appending the end-of-thinking token delimiter and optionally “Final Answer:” to early exit the thinking stage and make the model provide its current best answer. To enforce a minimum, the generation of the end-of-thinking token delimiter is suppressed and optionally the string “Wait” is appended to the model’s current reasoning trace to encourage the model to reflect on its current generation.
Budget forcing with s1–32B.
Supervised finetuning is performed on Qwen2.5–32B-Instruct using s1K to obtain the model s1–32B.

Evaluation

The resulting model, s1–32B, achieves strong performance on the reasoning benchmarks, comparable to much larger models trained on significantly more data.
It demonstrates that carefully curated training data can significantly improve sample efficiency. s1–32B is the most sample-efficient open data reasoning model.
Test-time scaling with s1–32B.Sequential and parallel test-time scaling.
Budget forcing enables effective test-time scaling, allowing for improved performance with increased compute.
However, excessive suppression of the end-of-thinking token can lead to repetitive loops and diminishing returns.
Sequential scaling via budget forcing is more effective than parallel scaling (majority voting).

s1.1

Seven days after the release of s1, s1.1 is released. Traces for the 1,000 samples in s1K are regenerated using DeepSeek r1 to create s1K-1.1. The same training procedure is used to train the model s1.1. Other updates since the launch include the release of o3, LIMO, and AIME 2025. s1.1 performs significantly better than s1. Distilling from Claude 3.7 led to worse performance than from r1.

Paper

s1: Simple test-time scaling https://arxiv.org/abs/2501.19393

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on April 23, 2025.

Canonical link

Exported from Medium on May 4, 2026.
