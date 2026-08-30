# Papers Explained 439: Reinforcement Learning with Calibration Rewards (RLCR)

Papers Explained 439: Reinforcement Learning with Calibration Rewards (RLCR)

Papers Explained 439: Reinforcement Learning with Calibration Rewards (RLCR)

RLCR (Reinforcement Learning with Calibration Rewards) is an approach to training reasoning models that jointly improves accuracy and…

Papers Explained 439: Reinforcement Learning with Calibration Rewards (RLCR)

RLCR (Reinforcement Learning with Calibration Rewards) is an approach to training reasoning models that jointly improves accuracy and calibrated confidence estimation. During RLCR, LLMs generate both predictions and numerical confidence estimates after reasoning. They are trained to optimize a reward function that augments a binary correctness score with a Brier score — a scoring rule for confidence estimates that incentivizes calibrated prediction.

Scoring Rule

A scoring rule, denoted as S, is a function S : R × {0, 1} → R that maps a confidence estimate (q) and an outcome (o) to a scalar score. This is specifically in the context of modeling binary outcomes (e.g., the confidence that an answer is correct).

A scoring rule is considered “proper” if its expected value is minimized when the confidence scores (q) match the true outcome probability (p(a)). Mathematically:

Ea∼p(a) S(p(a), a) ≤ Ea∼p(a) S(q, a) for any q.

This means that the best score is achieved when the predictor’s confidence accurately reflects the true probability of the outcome.

Examples of Proper Scoring Rules:

Logarithmic Score (Log-loss): S(q, a) = a log q + (1 − a) log(1 − q)
Brier Score: S(q, a) = (a − q)2
Spherical Score: S(q, a) = q / √(q2 + (1 − q)2)

All these scoring rules share the property that they are maximized when the confidence (q) matches the true probability (p(a = 1)).

Method

The main idea behind the approach is to train language models via reinforcement learning with a reward that incentivizes both correctness and calibration, by combining a standard correctness reward with a reward based on the Brier score. In this approach, models are first prompted to produce reasoning chains that produce both answers and confidence estimates. They are then trained to optimize:

Intuitively, this reward incentivizes correctness but penalizes models when they output incorrect answers with high confidence or correct answers with low confidence.

Experiment Setup

GRPO is used as the base RL algorithm with modifications:

KL regularization is not used
The standard deviation division in the advantage is removed, which might help with learning on examples where there are extreme miscalibrations.
The BNPO loss function is used, which aggregates token level losses using the number of active tokens in the local training batch.

RL is initialised from the base model specifically, the Qwen2.5–7B base model

For HotPotQA, a maximum response length of 1536 is used while for Math, 4096 is used. The Long RLCR system prompt is used for HotPot and the Simple RLCR prompt for Math (the long version did not provide additional benefit on Math). The Simple Generation prompt is used for RLVR.

Long RLCR system prompt:
A conversation between User and Assistant. 
The user asks a question, and the Assistant solves it. 
The assistant first thinks about the reasoning process in the mind, provides the user with the final answer, then analyzes its confidence about the solution and then provides the user with its confidence level. 
The confidence level is a number between 0 and 1 (inclusive)
enclosed within <confidence> </confidence> tags. 
The final answer is enclosed between <answer> </answer> tags. 
The analysis about confidence and uncertainty is enclosed within <analysis> </analysis> tags. 
The assistant should reason about its confidence in the solution and its uncertainty in the solution within these tags. 
Here are some guidelines for the analysis: 
1. Your task is to point out things where the model could be wrong in its thinking, or things where there might be ambiguity in the solution steps, or in the reasoning process itself.
2. You should not suggest ways of fixing the response, your job is only to reason about uncertainties.
3. For some questions, the response might be correct. In these cases, It is also okay to have only a small number of uncertainties and then explicitly say that I am unable to spot more uncertainties.
4. Uncertainties might be different from errors. For example, uncertainties may arise from ambiguities in the question, or from the application of a particular lemma/proof.
5. If there are alternate potential approaches that may lead to different answers, you should mention them.
6. List out plausible uncertainties, do not make generic statements, be as specific about uncertainties as possible.
7. Enclose this uncertainty analysis within <analysis> </analysis> tags.
The final format that must be followed is : 
<think> reasoning process here </think> 
<answer> final answer here </answer> 
<analysis> analysis about confidence and uncertainty here </analysis> 
<confidence> confidence level here (number between 0 and 1) </confidence> )
Simple RLCR prompt:
A conversation between User and Assistant. 
The user asks a question, and the Assistant solves it. 
The Assistant first thinks about the reasoning process in the mind, provides the user with the final answer, then analyzes its confidence about the solution and provides the user with its confidence level. 
The confidence level is a number between 0 and 1 (inclusive) enclosed within <confidence> </confidence> tags. 
The final answer is enclosed between <answer> </answer> tags. 
The analysis about confidence and uncertainty is enclosed within <analysis> </analysis> tags. 
The Assistant should reason about its confidence in the solution and its uncertainty in the solution within these tags. 
The final format that must be followed is: 
<think> reasoning process here </think>
<answer> final answer here </answer>
<analysis> analysis about confidence and uncertainty here </analysis>
<confidence> confidence level here (number between 0 and 1) </confidence>
Simple Generation prompt
A conversation between User and Assistant. 
The user asks a question, and the Assistant solves it. 
The assistant first thinks about the reasoning process in the mind and analyzes its confidence about the solution and then provides the user with the final answer as well as its confidence level. 
The confidence level is a number between 0 and 1 (inclusive) enclosed within <confidence> </confidence> tags. 
The final answer is enclosed between <answer> </answer> tags. 
The final format that must be followed is : 
<think> reasoning process here </think>
<answer> final answer here </answer> 
<confidence> confidence level here (number between 0 and 1) </confidence>.
The optimisation function is augmented with a simple format reward that encourages models to enclose CoTs within the right tags to enable easier verification and more structured outputs.

The following methods are evaluated:

Base: The base pre-trained model.
RLVR: Initialized from the base model and trained using Rcorrectness with <think> and <answer> tags. During evaluation, the model is also asked to verbalize confidence.
RLVR + BCE Classifier: A confidence classifier trained on outputs from the RLVR model. Specifically, given a dataset of problems, solution CoTs (from RLVR), and correctness labels (x,y, y≡y∗), we train a classifier fθ(x,y) to predict the model’s confidence score using the binary cross-entropy (BCE) loss. The classifier is initialized from Qwen2.5–7B Base and is thus highly expressive.
RLVR + Brier Classifier: Instead of using binary cross-entropy (BCE) loss, mean squared error (MSE) is used which allows more direct optimization of the Brier score.
RLVR + Probe: Given the final-layer embedding ϕ(x,y) of the RLVR model, a linear probe is trained to predict confidence scores.
Answer Probability: The outputs are generated using RLVR, the tokens enclosed within the <answer> tags are extracted, and their average probability is computed.
RLCR: Initialized from the base model and trained using R_RLCR.

Evaluation

Hotpot QA

To evaluate and improve models’ uncertainty reasoning, particularly under varying information completeness, used a modified HotPotQA distractor dataset (HotPotQA-Modified) with multi-hop questions and varying information completeness (by removing 0, 1, or both relevant paragraphs). Trained models on 20,000 examples from the modified HotPotQA dataset. Evaluated correctness using exact string match.
Accuracy and calibration metrics for models trained on HotpotQA.
RL-trained models (RLCR and RLVR) outperformed off-the-shelf models in multi-hop accuracy on the original HotPotQA distractor dataset.
RLCR achieved accuracy comparable to RLVR, confirming that the calibration term does not negatively impact performance.
The base model, RLVR, and the Answer Probability baseline exhibited high overconfidence and poor calibration on the in-distribution dataset.
RLCR and classifier methods showed significantly better calibration, with RLCR slightly outperforming classifiers.
RL training on HotPotQA did not improve out-of-distribution (OOD) reasoning accuracy, as the base model’s accuracy closely matched RL-trained models on OOD tasks.
RLVR negatively impacted calibration on out-of-distribution tasks compared to the base model.
RLCR achieved substantial gains in calibration metrics across all baselines on out-of-distribution tasks, while maintaining or slightly improving task accuracy.

The better calibration generalization of RLCR is hypothesized to be due to:

Uncertainty reasoning in chain-of-thought, allowing reflection on confidence.
Robust learning from non-stationary RL training dynamics.
Leveraging shared internal representations for solution generation and calibration.

Math

Used Big-Math, a large, curated training dataset containing over 250,000 math problems, including questions from benchmarks like Math and GSM8K. Problems were filtered to retain those with LLaMA-8B solve rates between 0–70% and numerical answers, resulting in a final training set of 15,000 problems.

Correctness was computed using math-verify, a robust expression evaluation system.

To enhance the quality of uncertainty analyses, a variant model was trained with a lightweight Supervised Fine-Tuning (SFT) warmup phase before RL.
Accuracy and calibration metrics for models trained on BigMath.
Accuracy on Math Benchmarks: All RL methods significantly improved accuracy over the base model on Math benchmarks (averaged over GSM8K, Math, and Big-Math).
Calibration on Math Benchmarks: SFT+RLCR achieved the best calibration on Math benchmarks, slightly surpassing classifiers, while base and RLVR models remained poorly calibrated.
Out-of-Distribution (O.O.D.) Accuracy: On O.O.D. datasets (TriviaQA, SimpleQA, CommonsenseQA, GPQA, HotPotQA), the accuracies of RLCR and RLVR were marginally better than the base model.
SFT+RLCR O.O.D. Accuracy Drop: The accuracy of the SFT+RLCR model dropped significantly in O.O.D. settings, possibly due to catastrophic forgetting induced by the SFT warmup.
O.O.D. Calibration: Despite the O.O.D. accuracy drop, SFT+RLCR achieved the strongest calibration in O.O.D. settings.
RLCR Trade-off in O.O.D.: RLCR offered a stronger trade-off in O.O.D. settings, maintaining accuracy while matching or outperforming all baselines on calibration.
Uncertainty Analysis Quality: Direct application of RL to the base model improved calibrated reward, but the uncertainty analyses remained qualitatively generic, often lacking reasoning tied to specific solution steps

Paper

Beyond Binary Rewards: Training LMs to Reason About Their Uncertainty 2507.16806

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on August 26, 2025.

Canonical link

Exported from Medium on May 4, 2026.
