# Papers Explained 576: Aryabhata 2

Papers Explained 576: Aryabhata 2

Papers Explained 576: Aryabhata 2

Aryabhata 2 is a 20B-parameter open-source language model developed by PhysicsWallah for advanced STEM reasoning in competitive exams like…

Papers Explained 576: Aryabhata 2

Aryabhata 2 is a 20B-parameter open-source language model developed by PhysicsWallah for advanced STEM reasoning in competitive exams like JEE and NEET, post-trained from GPT-OSS-20B using reinforcement learning on a rigorously cleaned and verified curriculum of Physics, Chemistry, Mathematics, and Reasoning questions.

Data Preparation

The raw dataset comes from PhysicsWallah’s internal question banks, covering Physics, Chemistry, Mathematics, and General Reasoning, mirroring the question types in Indian competitive exams like JEE and NEET.

Initial size: 1.78 million questions.
After cleaning and verification: 1.25 million high-quality questions.
Decontamination: Ensures the dataset does not include overlap with evaluation/benchmark sets and only includes materials up to mid-2024
Dataset distribution across different stages of the preprocessing pipeline.
Cleaning Pipeline

HTML artifact removal: Deletes all questions with tags, as these need visual data not handled by a text-only model.
LaTeX validation: All math expressions are rendered using pdflatex; failures are discarded, ensuring syntactically valid math.
Completeness check: Qwen3–30B-A3B-Thinking-2507 classifies and removes incomplete/ill-posed questions.
Domain filtering: Non-STEM questions are dropped using Qwen3–30B-A3B-Thinking-2507 .
About 24% of original questions are filtered out through these stages

Answer Verification

Since RL depends on reward signals, incorrect answer keys can harm training.

Policy model: GPT-OSS-120B generates chain-of-thought (CoT) solutions.
Judge model: Qwen3–30B-A3B-Thinking-2507 checks if the solution’s final answer matches the official key. 

Multi-pass Verification:

Single-sample: For each question, generate one CoT; if judge says correct, accept. ~80% accepted here.
Four-sample: For the unresolved 20%, generate four CoTs; accept if any are correct. +8%.
Sixteen-sample: For the rest, generate sixteen CoTs; accept if any are correct. +4%.

If any valid solution is possible, the pair is kept.

Curriculum Construction

Each question is sampled with four independent model generations to estimate empirical difficulty:

Trivial: Solved correctly all 4 times.
Learnable: Solved correctly 1–3 times.
Challenging: Solved zero times.

Trivial questions are largely omitted from later RL phases, except some for format alignment. Chemistry questions are upsampled due to initial underperformance

Reinforcement Learning Framework

Some key changes are made to the standard GRPO objective:

No KL-regularization/reference model: To save GPU memory.
DAPO-style clipped objective: Uses a clipped, asymmetric policy-ratio objective function.
No variance normalization: Only mean reward is removed from advantages, not divided by stdev.
Truncation masking: Masks outputs that ‘hit’ max length, avoiding incomplete answer training.
Multiplicative reward composition: Final reward combines correctness and format via multiplication.

Reward Shaping
R = Raccuracy × Rformat
Accuracy Reward:

String match: Case-insensitive, whitespace-trimmed comparison.
Numeric match: ∣a−b∣≤max(0.01⋅max(∣a∣,∣b∣),0.01) to tolerate rounding.
Symbolic match: Uses math-verify; fallback to numeric.
MCQs: If label doesn’t match but text does, partial reward (0.5).

Format Reward: 

Considers answer length and the ratio of answer to total output. Let c_tot be the total number of output characters, c_sol be the number of characters in the final-answer segment, then:

Format Reward is 

where

Intuitively, Slen rewards sufficiently detailed final answers by increasing the score with solution length, while Sratio encourages a balanced allocation between reasoning and answer segments.

Training Phases

Phase 1: Format Alignment (300 steps, group size 8):

Early phase using a format-mixed dataset (with more chemistry), aligns the model to the desired answer structure before increasing difficulty.

Phase 2: Prolonged RL (5,000 steps, group size 8→16):

Increases question difficulty adaptively; group size grows as RL proceeds.
Rewards monitored — if accuracy reward > 0.7 for 20+ steps, sampling increases in difficulty.
Checkpoint merging (EMA-based) used for stability when reward plateaus.

Phase 3: Broadened RL (700 steps, group size 64→128):

Focuses on broad exploration/generalization by sampling larger groups, allowing the model to discover new reasoning strategies.
Training hyperparameters across the three reinforcement learning phases.
Evaluation
In-distribution Pass@1 (4-sample mean, %) overall accuracy.In-distribution accuracy-token trade-off.
Aryabhata 2 achieved the highest open-source accuracy (Pass@1 average 88.95), outperforming GPT-OSS-120B (88.28) and Qwen3–30B-A3B (88.55).
Aryabhata 2 was significantly more token-efficient achieving substantially higher accuracy per 1K tokens than all other open-weight models
Out-of-distribution Pass@1 (4-sample mean, %) accuracy.Out-of-distribution accuracy-token trade-off.
Aryabhata 2 averaged 87.64 on OOD benchmarks surpassing Nemotron 3 Nano 30B (83.48) but trailing proprietary and larger models (e.g., GPT-OSS-120B at 89.50, Qwen3–30B-A3B at 89.42).
Demonstrated particular strength on harder Olympiad-style tests (notably +27.08 on HMMT compared to Qwen3–30B-A3B). Achieved superior token-efficiency (39.58 Acc./1K tokens) compared to all open-weight baselines.

Paper

Aryabhata 2: Scaling Reinforcement Learning for Advanced STEM Reasoning 2605.28829

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

View original.

Exported from Medium on June 13, 2026.
