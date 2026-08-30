# Papers Explained 539: Golden Goose

Papers Explained 539: Golden Goose

Papers Explained 539: Golden Goose

Golden Goose is a simple trick to synthesize unlimited RLVR tasks from unverifiable internet text by constructing a multiple-choice…

Papers Explained 539: Golden Goose

Golden Goose is a simple trick to synthesize unlimited RLVR tasks from unverifiable internet text by constructing a multiple-choice question-answering version of the fill-in-the-middle task. Given a source text, an LLM is prompted to identify and mask key reasoning steps, then generate a set of diverse, plausible distractors. This enables the leveraging of reasoning-rich unverifiable corpora typically excluded from prior RLVR data construction to synthesize GooseReason-0.7M, a large-scale RLVR dataset with over 0.7 million tasks spanning mathematics, programming, and general scientific domains.

Method

Data Synthesis Pipeline
The Golden Goose pipeline.
Given a source text S, an LLM is prompted to identify a contiguous span t of important reasoning steps. This span t is used to construct a masked context Smask by replacing t in S with a special token [MASK]. Treating t as the ground-truth answer, the LLM then generates a set of diverse distractors D= {d1, d2, . . . , dk }that are plausible and similar in style to t, yet incorrect in the context of Smask. Finally, a multiple-choice question Q = (Smask, {t}∪D) is formulated.

If the source text S is noisy, such as cybersecurity-related scrapes from FineWeb, the LLM is first prompted to extract or summarize S into a coherent, educationally valuable S′. Smask and D are then constructed based on S′. If S contains no suitable passage, the LLM is instructed to return an empty string.

The student model is provided with Smask and tasked with selecting the option that best fills the [MASK] from the candidate set {t}∪D, presented in randomized order. Verification during RL simply checks if the prediction matches the ground-truth option.

To ensure data quality, the strongest LLM available at the time of the experiment, GPT-5, is used. Additionally, difficulty-based filtering is employed to remove easy problems on which the student model consistently succeeds across all 16 rollouts.

Source Corpora

Reasoning Domain:

AoPS-Instruct: Extracted around 600k question-answer pairs from the Art of Problem Solving (AoPS) forum, featuring Olympiad-level math problems and community-driven solutions. The forum’s unstructured and noisy nature results in varied and occasionally incomplete solutions, including theorem-proving problems that are difficult to verify with existing RLVR pipelines.
rStar-Coder: Curated and cleaned 37.7K expert-written problems with oracle solutions from competitive programming platforms. They synthesized new problems using an input-output test case synthesis pipeline, but only 380K out of 1,656K synthesized questions obtained test cases. The synthetic sft split contains questions and teacher model’s solutions without test cases, which are leveraged to synthesize verifiable coding questions with Golden Goose.
MegaScience: Extracted 650k question-answer pairs from nearly 12k university-level scientific textbooks across various subjects. Solutions in domains like chemistry involve specialized formulas, while questions in medicine or economics require multi-paragraph discussions, challenging to validate under the current RLVR pipeline.

From these sources, over 0.7 million novel RLVR tasks were synthesized using the Golden Goose pipeline. GooseReason-0.7M retains around 70% effectiveness ratio, substantially supplementing existing RLVR datasets for further scaling RL training.

Cybersecurity Domain: Primus released pre-training data for their cybersecurity LLM, Llama-Primus-Instruct, consisting of:

Primus-Seed: Data crawled from reputable sources like MITRE, Wikipedia, cybersecurity company websites, and manually collected cyber threat intelligence.
Primus-FineWeb: Constructed by filtering cybersecurity-related text from FineWeb using Primus-Seed as positive samples.

Golden Goose synthesized approximately 180K RLVR tasks for the cybersecurity domain from raw internet text, despite the noisy nature of web scrapes.

Design Choice

Multiple-Choice v.s. Open-ended

An alternative to the multiple-choice formulation is to construct RLVR tasks as open-ended fill-in-the-mask problems, where the model is tasked with predicting the masked content and an LLM-as-judge verifies the prediction against the ground-truth. However, beyond the computational overhead of hosting a powerful judge model during RL training, reasoning models, particularly those heavily tuned with RL, exhibit a strong tendency to solve the problem from scratch and completely ignore the task requirement of generating the infill.

Number of Distractors

Ablating the effect of the number of distractors reveals that with too few options (e.g., 3), the majority of problems in GooseReason-Math become overly easy, where the model tends to rely on an elimination strategy. Increasing the number of distractors raises the task difficulty, as this elimination strategy becomes less effective under a fixed output length. When using 9 options, over 70% of the problems fall into a medium-difficulty regime with both successful and failed model rollouts, effective for RL training.

Experiment

The effect of GooseReason-0.7M is evaluated across two representative scenarios for scaling up RL training of LLMs. The first scenario is a data-saturation scenario, where the model has already saturated on a strong RLVR data blend. The second scenario is a compute-constrained scenario, where RL training starts from scratch under a fixed training budget, making the choice of RL data crucial.

The RL recipe in ProRLv2, a variant of the GRPO algorithm designed to maintain stable policy optimization over prolonged training, is adopted. Specifically, it employs the clipped GRPO objective with a decoupled advantage normalization strategy from REINFORCE++ consisting of a group-wise mean subtraction followed by batch-level standardization.

Data-saturation experiment

Starting from ProRL-1.5B-v2, a strong RLVR-ed model, based on R1-Distill-Qwen-1.5B, already trained with >20K H100 GPU hours on 136K diverse RLVR tasks (math, coding, STEM, logic, instructions) Continued RL is compared with:

Original ProRL data only.
ProRL data + GooseReason-0.7M.
Comparison of continued RL training on ProRL-1.5B-v2 using the original ProRL data, adding GooseReason-0.7M, or using RLVE.
Continued RL on ProRL data alone yields only marginal gains over 1,100 H100 GPU hours.
Adding GooseReason-0.7M yields robust, continuous improvements:
Math: +2.71% vs. +0.63% (ProRL-only).
Coding: +2.12% vs. +0.95%.
STEM: +3.48% vs. +0.13% (largest margin, addressing STEM data scarcity).
Despite GooseReason being MCQ-formatted, gains transfer to non-MCQ benchmarks, indicating generalizable reasoning skills.

Compute-efficient scaling from scratch

Trained Qwen-4B-Instruct from scratch for only 200 RL steps under a fixed compute budget, comparing:

ProRL data only.
ProRL data + GooseReason-0.7M (joint training).
Comparison of RL training from scratch on Qwen-4B-Instruct under a fixed compute budget with ProRL data only versus joint training with GooseReason-0.7M.
Under the same 200-step budget:
Joint training with GooseReason-0.7M consistently achieves higher performance at each step than ProRL-only training.
Demonstrates that GooseReason enables more compute-efficient RL scaling from scratch.

Paper

Golden Goose: A Simple Trick to Synthesize Unlimited RLVR Tasks from Unverifiable Internet Text 2601.22975

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on February 12, 2026.

Canonical link

Exported from Medium on May 4, 2026.
