# Papers Explained 593: Self-Distillation Fine-Tuning

Papers Explained 593: Self-Distillation Fine-Tuning

Papers Explained 593: Self-Distillation Fine-Tuning

Self-Distillation Fine-Tuning (SDFT) is a simple method that enables on-policy learning directly from demonstrations. SDFT leverages…

Papers Explained 593: Self-Distillation Fine-Tuning

Self-Distillation Fine-Tuning (SDFT) is a simple method that enables on-policy learning directly from demonstrations. SDFT leverages in-context learning by using a demonstration-conditioned model as its own teacher, generating on-policy training signals that preserve prior capabilities while acquiring new skills.

Method

Given a foundation model with policy π, the teacher is constructed by conditioning it on expert demonstrations: π(·|x, c), where x is the task prompt and c is a demonstration. The student is simply the base model without this conditioning, πθ (·|x). To construct the teacher for a given prompt x, the model is conditioned on both the prompt and a demonstration using the following simple prompt.
<Question>This is an example for a response to the question:<Demonstration>Now answer with a response of your own, including the thinking process:
This prompt is sufficient to prevent the policy from outputting c verbatim and instead elicits a response that reflects the model’s understanding of the intent behind the demonstration, leveraging its in-context learning capabilities.

For every prompt x, our algorithm, SDFT, samples responses from the student policy y ∼ πθ (·|x) and minimizes the reverse Kullback-Leibler (KL) divergence between the student and the teacher distributions:

The objective is decomposed into a token-level loss, and the gradient is taken with respect to the student parameters θ while treating the teacher distribution as fixed. This results in the following gradient estimator:

Where V is the token vocabulary. A critical component of SDFT is the parameterization of the teacher model used to compute the likelihood ratios. While the teacher is always conditioned on the demonstrations c, its weights can be defined in multiple ways. An exponential moving average (EMA) of the student parameters is used for the teacher.

Experimental Setting

The method is evaluated in two settings that reflect common forms of post-training adaptation: Skill Learning and Knowledge Acquisition.

In Skill Learning, the focus is on determining whether a pretrained LLM with broad capabilities can acquire a new, narrowly defined skill without degrading its existing abilities. The chosen experimental tasks are ones the models had not been explicitly fine-tuned on, unlike Math or Coding, to demonstrate the benefits of continual learning. The method is tested on three domains:

Science Q&A, involving undergraduate-level scientific reasoning and using the Chemistry L-3 subset of SciKnowEval.
Tool Use, which requires mapping a tool-API specification and user request to the correct tool call, utilizing ToolAlpaca.
Medical, centered on clinical reasoning questions, with training data from stage 1 of the HuatuoGPT-o1 pipeline and evaluation from stage 2.

In Knowledge Acquisition, the objective shifts: the model must integrate genuinely new factual content not present in its pretraining data. For this purpose, a corpus of Wikipedia articles describing natural disasters that occurred in 2025 (after the training knowledge cutoff) is constructed, totaling approximately 200K tokens. Question–answer pairs are generated about these articles, yielding an SFT dataset roughly five times larger than the source corpus. These questions are designed to probe factual content.

For each task, evaluation is conducted along two primary axes.:

In-Distribution Accuracy measures accuracy on held-out test data for the newly introduced task. For Knowledge Acquisition, two variants are used: (1) All details correct (Strict Accuracy), and (2) The answer contains correct information and no incorrect statements (Lenient Accuracy).
Previous Capabilities assesses performance on a suite of established benchmarks that probe general reasoning and world knowledge: HellaSwag, TruthfulQA, MMLU, IFEval, Winogrande, and HumanEval. The average performance across these datasets is reported as a measure of catastrophic forgetting.

In the Knowledge Acquisition setting, a third metric is included:

Out-of-Distribution Accuracy. This refers to “indirect” questions whose answers depend on the injected knowledge but do not directly reference it (e.g., “Which countries required international humanitarian aid in 2025?”). This metric measures whether the new information has been properly integrated into the model’s internal memory rather than memorized in a narrow form.

Evaluation
Performance trade-offs between new task accuracy and retention of prior capabilities.SDFT effectively integrates new factual knowledge, thus achieving better accuracy both in- and out-of-distribution.
On-policy SDFT achieves higher accuracy on new tasks than SFT, benefitting both in-distribution and out-of-distribution generalization.
The table reports the exact new-task accuracy and average prior-task performance for each method across all Skill Learning tasks.
In both single-task and multi-task continual learning, only SDFT improves performance on new tasks without significant loss on prior tasks, while SFT suffers heavy forgetting.
SDFT allows for stable, incremental learning of multiple skills without oscillatory losses, supporting true cumulative/continual learning.

Paper

Self-Distillation Enables Continual Learning 2601.19897

That’s a wrap!

If you enjoyed this breakdown, follow for more. I publish new paper explanations most weekdays.

More papers in this series, organized by lab and topic, are in the start here guide.

What paper should I cover next? Let me know in the responses.

By Ritvik Rastogi on August 12, 2026.

Canonical link

Exported from Medium on August 22, 2026.
