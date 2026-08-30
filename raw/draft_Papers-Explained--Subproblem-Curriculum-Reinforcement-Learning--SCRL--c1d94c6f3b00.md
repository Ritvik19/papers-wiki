# Papers Explained: Subproblem Curriculum Reinforcement Learning (SCRL)

Papers Explained: Subproblem Curriculum Reinforcement Learning (SCRL)

Papers Explained: Subproblem Curriculum Reinforcement Learning (SCRL)

Subproblem Curriculum Reinforcement Learning (SCRL) is a curriculum reinforcement learning framework built on verifiable subproblems…

Papers Explained: Subproblem Curriculum Reinforcement Learning (SCRL)

Subproblem Curriculum Reinforcement Learning (SCRL) is a curriculum reinforcement learning framework built on verifiable subproblems derived from reasoning chains. Given a reference solution, SCRL derives a series of verifiable subproblems and constructs a subproblem curriculum, with the final subproblem fixed as the original problem. This converts partial progress on hard problems into verifiable learning signals.

Method

Overview of SCRL.

SCRL has three steps:

Given a reference solution, an external LLM derives K verifiable subproblems from the reasoning chain and constructs the subproblem curriculum.
The policy answers all K subproblems in one on-policy rollout. Each subproblem answer is then verified, and progress-aware correction is applied to obtain progress-aware subproblem rewards. Subproblem-level normalization computes an advantage for each subproblem position, which is then used for token-level credit assignment.
To reduce prompt mismatch, SCRL uses mixed-group training, jointly optimizing curriculum rollouts and original-problem rollouts in the same update.

The main guidelines for building subproblems are:

Increasing difficulty: Subproblems are ordered from easier to harder, with the final subproblem fixed as the original problem: s(1) ≺ s(2) ≺ · · · ≺ s(K) = x.
Linked but self-contained: Earlier subproblems provide useful intermediate results for later ones, while each subproblem remains a complete standalone question.
Verifiable answers: Each subproblem has an objectively checkable answer for independent verification.
System Message:
You are a math curriculum designer for RL training. Generate exactly 4 progressive subproblems q1, q2, q3, q4.

Hard constraints:
1. q4 must be equivalent to the original final question and same grading target.
2. Difficulty strictly increases: q1 < q2 < q3 < q4.
3. q2/q3 should be naturally informed by q1/q2, but each question must be self-contained.
4. Each question must have a single clean numerical-expression ground_truth.
5. Avoid open-ended proof/explanation-only questions.
6. Use reference_solution to design the progressive dependency and correctness.
Output JSON only.

User Message:
Given the original problem and final answer, generate JSON with schema:
{
"question_1": {"statement": "...", "ground_truth": "..."},
"question_2": {"statement": "...", "ground_truth": "..."},
"question_3": {"statement": "...", "ground_truth": "..."},
"question_4": {"statement": "...", "ground_truth": "..."}
}
Original Problem: {{problem}}
Original Final Answer: {{final_answer}}
Reference Solution: {{reference_solution}}
Let x denote the original problem. The curriculum prompt tK (x) is defined as the prompt that presents all K subproblems s(1), . . . , s(K) simultaneously and asks the model to solve them in order. Thus, x corresponds to the original-problem rollout, while tK (x) corresponds to the curriculum rollout.
<|im_start|>system
Please reason step by step, and put your final answer within \boxed{}.<|im_end|>
<|im_start|>user
Problem Statement: {Original Problem}
Problem1: {Subproblem1}
Problem2: {Subproblem2}
Problem3: {Subproblem3}
Problem4: {Subproblem4}
This task has 4 problems.
Please solve Problem 1 to Problem 4 in order.
Output MUST contain exactly 4 blocks in this order:
<p1></p1>
<p2></p2>
<p3></p3>
<p4></p4>
For each block <pN>...</pN>, include reasoning and end with final answer in \boxed{answer}.<|im_end|>
<|im_start|>assistant<|im_start|>system
Please reason step by step, and put your final answer within \boxed{}.<|im_end|>
<|im_start|>user
{USER_PROMPT}<|im_end|>
<|im_start|>assistant
Progress-Aware Subproblem Rewards

Curriculum Progress: For a curriculum rollout oi ∼ πθ(· | tK (x)), verifying the K extracted subproblem answers gives a raw reward vector 

ri = (r(1)i , . . . , r(K)i ) ∈ {0, 1}K.

If the response does not follow the required format, ri is set to 0. The curriculum progress ki ∈ {0, 1, . . . , K} is defined as the maximum number of consecutively solved subproblems from the beginning.

The curriculum progress ki tracks the current policy’s capability boundary on the hard problem, and also identifies the intermediate progress actually achieved by the rollout.

Progress Aware Correction: Directly rewarding each subproblem independently may credit later subproblems despite earlier failures, creating a potential reward-hacking shortcut. Rewards are therefore aligned with curriculum progress by keeping only the consecutively solved prefix.

Subproblem-level normalization: Given G curriculum rollouts oi for i = 1, . . . , G, the final subproblem rewards at each subproblem position j are normalized across the rollout group. Thus, the subproblem-level advantage A(j)i measures the relative success of rollout i at subproblem position j within the rollout group, independent of rewards at other subproblem positions.

Token-level credit assignment: After computing the subproblem-level advantages, these are assigned back to the tokens of the corresponding subproblem answers. Using the structured response format, subi(t) is defined as j if token oi,t lies between and ; then Ai,t = A(subi(t)) gives the token-level advantage. Tokens outside all answer spans receive zero advantage, and if the response does not follow the required format, all tokens in that response receive zero advantage. This converts subproblem-level progress into token-level learning signals for the corresponding answer spans.

Experiment Setup

Qwen3–4B-Base, Qwen3–14B-Base and Llama3.2–3B-Instruct serve as the base policies. Subproblems are generated with the DeepSeek-V3.2 API with K = 4. The training set hard_1024 is used, a subset of 1,024 problems randomly selected from the high-difficulty competition mathematics dataset.
Hyperparameter settings for SCRL.
The models are evaluated on seven widely used mathematical reasoning benchmarks: OlympiadBench, Minerva, MATH-500, AIME 2024, AIME 2025, AMC, and IMO-Bench.

The method is compared against the following competitive baselines: SFT, GRPO, DAPO, QuestA, and NuRL.

Evaluation
Main Results on mathematical reasoning benchmarks.
SCRL consistently outperforms vanilla GRPO and other competitive baselines such as DAPO, QuestA, and NuRL across all tested models (Llama3.2–3B, Qwen3–4B, Qwen3–14B) and benchmarks, with the most notable improvement on Qwen3–4B: 35.0% average vs. 32.0% (QuestA) and 30.9% (GRPO).
SCRL also shows significant gains on challenging benchmarks (e.g., AIME’25: 15.3% vs. 11.7% for QuestA).
Ratio of solvable problems during training of Qwen3–4B-Base.
SCRL’s curriculum training enhances not only performance on curriculum-format rollouts but also transfers to improved direct hard-problem solving capability, as tracked by the ratio of solvable problems during training.
Effect of subproblem generator quality on Qwen3–4B-Base.
SCRL’s performance advantage is robust even when using weaker or less curated subproblems, though higher-quality subproblems (e.g., generated by DeepSeek-V3.2) can still boost gains further.
Ablation on credit assignment. Here “corr” denotes progress-aware correction.
Effective curriculum training in SCRL relies on subproblem-level normalization with progress-aware correction, which enables better credit assignment and, in turn, better performance compared to strategies that lack either component.

Paper

From Reasoning Chains to Verifiable Subproblems: Curriculum Reinforcement Learning Enables Credit Assignment for LLM Reasoning 2605.22074

That’s a wrap!

If you enjoyed this breakdown, follow for more. I publish new paper explanations most weekdays.

More papers in this series, organized by lab and topic, are in the start here guide.

What paper should I cover next? Let me know in the responses.

View original.

Exported from Medium on August 22, 2026.
