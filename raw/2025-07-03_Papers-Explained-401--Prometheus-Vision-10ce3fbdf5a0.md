# Papers Explained 401: Prometheus-Vision

Papers Explained 401: Prometheus-Vision

Papers Explained 401: Prometheus-Vision

Inspired by the approach of evaluating LMs with LMs, this work proposes to evaluate VLMs with VLMs. For this purpose, a new feedback…

Papers Explained 401: Prometheus-Vision

Inspired by the approach of evaluating LMs with LMs, this work proposes to evaluate VLMs with VLMs. For this purpose, a new feedback dataset called the Perception Collection is presented, encompassing 15K customized score rubrics that users might care about during assessment. Using the Perception Collection, Prometheus Vision is trained, the first open-source VLM evaluator model that can understand the user-defined score criteria during evaluation.

The project is available at GitHub.

Perception Collection

Each instance in the Perception Collection consists of five input components (image, instruction, response to evaluate, customized score rubric, reference answer) and two output components (language feedback and score decision).

Image: A real-world image that the user would provide to the VLM.
Instruction: A text instruction that the user would prompt the VLM. It is also related to the provided image.
Response to Evaluate: A text response that the VLM would generate based on the image and instruction. The evaluator VLM has to assess this response.
Customized Score Rubric: A detailed scoring criteria that the VLM should refer to for assessment. Fine-grained criteria are used in contrast to coarse-grained ones such as helpfulness, relevance, accuracy, and comprehensiveness. The rubric consists of (1) a description of the criteria and (2) a description of each scoring decision on a scale of 1 to 5.
Reference Answer: A reference answer that would achieve a score of 5. While this component could be hand-crafted by human annotators, in our experiments, GPT-4V is utilized.
Feedback: A rationale pinpointing what is good and bad about the response under assessment. Instead of directly providing a scoring decision, this component makes the judgment process more interpretable.
Score: An integer value on a scale of 1 to 5 that represents the quality of the response given the criteria mentioned in the score rubric.
The number of each component included in the Perception Collection.
While creating the Perception Collection, 5K real-world images sampled from MS COCO 2017 Challenge and the MMMU benchmark are utilized. Concretely, the augmentation process consists of 4 stages:

Step 1: Hand-Crafting Score Rubrics

Fifty examples of fine-grained score rubrics are initially written, designed to go beyond coarse-grained counterparts.
For these 50 images, an instruction and a corresponding rubric are created, specifically pinpointing the aspects to consider during assessment.

Step 2: Brainstorming Score Rubrics

GPT-4V is used to expand the number of score rubrics from 50 to 15,000.
This is achieved by using an arbitrary image from the 5,000-image pool and the initial 50 hand-crafted examples as demonstrations.
GPT-4V is prompted to generate three variants of score rubrics for each image.
To ensure quality, an additional prompting stage with GPT-4V is performed to inspect if the generated rubric aligns with the image. If not, GPT-4V is iteratively prompted again until three suitable candidates per image are acquired.

Step 3: Augmenting Instructions and Reference Answers related to the Score Rubric

The 15,000 generated score rubrics are then used to prompt GPT-4V to generate two novel instructions for each rubric.
This process results in a total of 30,000 instructions.
The method ensures a close tie between the instruction and the score rubric, as the instruction generation was conditioned on the rubric.

Step 4: Augmenting Training Instances

The final components i.e. the response to evaluate, feedback, and scoring decision are augmented.
Using the score rubric and instruction from previous stages, GPT-4V is prompted to write a response that would achieve a score of ‘i’ (where ‘i’ ranges from 1 to 5).
Crucially, measures were taken to ensure no length bias (i.e., longer responses not automatically receiving higher scores).
This stage yields a total of 150,000 responses and 150,000 feedback instances.
The instances are evenly distributed, with each score (1 through 5) having 30,000 instances.

Prometheus Vision

Using the Perception Collection, LLaVA-1.5 7B / 13B is employed as the backbone VLM for Prometheus Vision. For the language model component, vicuna-13b-v1.5 is utilized, and for the vision encoder, clip-vit-large-patch-14–336px is used. Both the language model and the vision encoder are frozen, focusing training solely on an MLP based alignment network. The training is conducted for one epoch.

A fixed phrase ‘So the overall score is’ is included in between the feedback and the score, which is found to prevent degeneration during inference.

Evaluation

Evaluation Setup

Setup #1 (Human Correlation): Utilized 45 instances with hand-crafted rubrics. 9 human annotators provided scoring decisions and compared language feedback from GPT-4, GPT-4V, and Prometheus Vision (13B). Metrics included Pearson, Kendall-Tau, and Spearman correlation for scoring, and Pairwise Preference Win-rate for feedback.

Setup #2 (GPT-4V Correlation): Expanded to 3,560 instances with 1,085 fine-grained score rubrics. Compared the correlation of scoring decisions between GPT-4V (prompted three times) and other evaluator VLMs/LMs (prompted three times). Metrics included Pearson, Kendall-Tau, and Spearman correlation.

Correlation with Human Evaluators
Pearson Correlation between score decisions from human evaluators and score decisions.
Prometheus Vision 13B notably mirrors the high correlation of leading models like GPT-4V and GPT-4 on LLAVA-BENCH (0.639) and Perception Bench (0.870) with human evaluators, especially on instances with real-world images.
On the VISIT-BENCH, Prometheus Vision outperforms GPT-3.5-TURBO and PROMETHEUS 13B but is lower than GPT-4 and GPT-4V. This disparity is attributed to the VISIT-BENCH containing a higher proportion of text-rich images, which Prometheus Vision’s current architecture struggles with.
Future iterations of Prometheus Vision could improve by integrating new methods from recent architectural advancements and using text-rich datasets for training to alleviate limitations with text-rich images.
GPT-4 (LM Evaluator) shows a slightly higher correlation with human evaluators on the text-rich VISIT-BENCH, while GPT-4V (VLM Evaluator) excels on LLAVA-BENCH and Perception Bench, which include diverse real-world images.

Quality of Language Feedback
Pairwise comparison of the quality of the language feedback generated.
Prometheus Vision 13B is capable of generating feedback quality comparable to GPT-4.
Human annotators determined that Prometheus Vision’s feedback was better or as good as GPT-4V’s 57.78% of the time, and better or as good as GPT-4’s 45.93% of the time.
This indicates that Prometheus Vision could be utilized as an open-source critique model to assist human assessment.

Simulating GPT-4 Vision as a Judge

Visual Instruction Following Benchmarks:
Pearson, Kendall-Tau, Spearman correlation with scores sampled from GPT-4V across 3 inferences on visual instruction following benchmarks.
Prometheus Vision demonstrates a higher correlation with GPT-4V compared to its backbone model, LLAVA-V1.5, across all tested benchmarks and model sizes, indicating that training with Perception Collection enhances the VLM’s evaluation capabilities. Prometheus Vision 13B also exhibits higher correlation than LM evaluators GPT-3.5-Turbo and GPT-4 on LLAVA-BENCH and Perception Bench.

Visual Question Answering Benchmarks:
Pearson, Kendall-Tau, Spearman correlation with scores sampled from GPT-4V across 3 inferences on visual question answering benchmarks.
Prometheus Vision significantly outperforms other open-source models, including LLAVA-V1.5. However, its correlation is generally lower in VQA benchmarks compared to visual instruction following benchmarks, likely due to the Perception Collection training data involving longer responses while VQA answers are mostly short.

Captioning Benchmarks:
Pearson, Kendall-Tau, Spearman correlation with scores sampled from GPT-4V across 3 inferences on captioning benchmarks.
While most evaluators, including proprietary LMs, show low correlation, Prometheus Vision 13B surprisingly stands out with a correlation above 0.5 in COCO-Captions. This suggests Prometheus Vision can generalize to evaluate other visual-language tasks beyond its training data.

Paper

Prometheus-Vision: Vision-Language Model as a Judge for Fine-Grained Evaluation 2401.06591

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on July 3, 2025.

Canonical link

Exported from Medium on May 4, 2026.
