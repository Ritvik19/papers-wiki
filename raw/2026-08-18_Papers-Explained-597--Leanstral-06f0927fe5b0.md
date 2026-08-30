# Papers Explained 597: Leanstral

Papers Explained 597: Leanstral

Papers Explained 597: Leanstral

Leanstral is a series of generalist code-agent models for Lean 4 with 119B total and only 6B active parameters. Rather than a specialized…

Papers Explained 597: Leanstral

Leanstral is a series of generalist code-agent models for Lean 4 with 119B total and only 6B active parameters. Rather than a specialized prover scaffold, Leanstral operates directly within the open-sourced Mistral Vibe code-agent harness and uses no test-time-scaling method beyond context compaction. Beyond competition mathematics, Leanstral resolves issues in real repositories spanning graduate-level mathematics, mathematical finance, and code verification.

Data

Lean data is collected for three stages of training: mid-training, supervised fine-tuning, and reinforcement learning.

For mid-training, the process starts from the Mistral Small 4 checkpoint and continues training on 6.5B Lean-specific tokens after deduplication, plus general code-agent data and other sources for instruction following and alignment. The Lean tokens include traces of generalist models attempting individual theorem-proving tasks as well as realistic proof-engineering issues in repositories.

For SFT, a Lean-code-agent-heavy mixture is used in which 50% of the trainable tokens come from Lean code-agent traces. The data is filtered for correctness, formatting, and style. Behaviors that are especially harmful for long-horizon proof engineering are also filtered, such as declaring success without compilation feedback, refusing difficult but feasible tasks, or hallucinating constraints that are not present in the repository.

For RL, a mixture of LeanGym PR data (50%), LeanGym single-theorem data (20%), and prove-or-disprove multiturn data (30%) is used.

Single-Theorem Competition Mathematics Data: A variety of self-contained competition mathematics theorem statements in Lean are sourced, and the SFT checkpoint is used to filter out the easy fraction of the data. This is used with the LeanGym Single Theorem and Prove-or-Disprove Multi-turn RL environments.

LeanGym PR Data: In addition to competition data, real Lean repositories are also used. The LeanGym pipeline extracts tasks from pull requests of permissively licensed Lean 4 GitHub repositories:

Collect raw PRs from such repositories.
For each commit, build the repository in a container at the base commit.
Find altered theorems and definitions via metaprogramming and omit their proofs or bodies.
Apply the full PR patch and verify its correctness via SafeVerify. Discard the failed PRs.
Rewrite the task description so it contains the full context of the PR.

Environments

Leanstral is trained on two types of environments:

The multiturn environment allows the model to prove or refute given theorems and Lean feedback between attempts
The LeanGym environment is a code-agent environment: the agent interacts with a repository, receives tool outputs, edits files, and decides how to proceed.

Prove-or-Disprove Multiturn Environment

The model is given a Lean theorem statement (with the proof body replaced by sorry), all required imports, and instructions to either prove or refute the theorem.
The statement problems are mostly self-contained; little context outside the imports and statement is required.
The model must attempt a proof of the theorem or of its negation.
After an attempt, if it doesn’t compile, uses the wrong or extra axioms, or proves the incorrect statement, feedback from the Lean compiler is provided and the model tries again.
The process is multiturn, continuing until the model either succeeds, reaches a turn limit, or exceeds its context length. If none of these result in success, the attempt is marked as a failure.
Partial reward: Given when the response is properly formatted with both a “thinking block” and a code block answer, following the original problem’s setting, and providing a single Lean proof without any lemmas.
Full reward: The proof must compile in the Lean Interact verifier and rely only on standard Lean axioms (verified with #print axioms). native decide is strictly forbidden due to inconsistency risks.
Special safeguards: “set options” are discouraged, and the system checks (via Lean metaprogramming) to ensure no code follows the proof.

LeanGym Environment

Designed for training Lean code agents to perform a wide range of Lean proof engineering tasks, beyond just proving single theorems.
The agent can interact with a Lean repository. It is given access to both bash and the Lean language server (lean-lsp-mcp).
All PR changes are applied via a startup patch, but bodies of modified proofs/definitions are replaced with sorry.
The goal is to fill in the correct content so target theorems are verified.
Inputs are a list of theorems and definitions that need completion. The environment controls the agent within a sandbox.
The verification of the agent’s work is done by a modified SafeVerify tool at the end of each episode.
If the working session (trajectory) becomes longer than the model’s context window, previous work is summarized (compacted).
For Leanstral 1.5, the original instructions are always preserved at the start, helping the model stay on target (prevents “objective drift”).
For self-contained tasks (like competition problems), a minimal Lean project with the theorem, imports, and config is set up.
The agent must fill in the proof and can write additional lemmas and even new Lean files if needed.

Training

After mid-training and SFT, Leanstral is trained with reinforcement learning from verifiable Lean feedback. The RL follows CISPO, using a truncated importance-weighted policy-gradient objective to reduce the effect of trainer-generator mismatch on long code-agent trajectories.

where Ti denotes the interleaved tool calls and tool responses in the trajectory, and c is a finite truncation threshold. Gradients are stopped through ¯ρi,t.

Evaluation

miniF2F Benchmark: Leanstral 1.5, with pass@4 and a 2M token limit per trajectory, saturates the benchmark, achieving a perfect MiniF2F-valid score (244/244) and nearly perfect test score (242/244). The two unsolved problems were both solved within additional attempt
PutnamBench leaderboard.
PutnamBench: Leanstral 1.5 solves 587 out of 672 problems using pass@8 with a 4M token limit, outperforming other open-source systems by being the only agent using a general coding-agent scaffold rather than a specialized prover workflow.
FATE benchmark.
FATE Benchmark: Leanstral 1.5 achieves 100% on undergraduate-level (FATE-M) problems with only 2 attempts per problem, state-of-the-art performance of 87% on graduate-level (FATE-H), and 34% on expert/PhD-level (FATE-X) using pass@8.
ArXivLean Benchmark: Leanstral 1.5 matches or outperforms major AI models at a much lower inference cost, solving 17.1% of problems, aligning with GPT-5.5 xhigh but at less than half the inference cost. The top leaderboard spot is held by Aleph Prover at 34.2%
FLTEval results.
FLTEval Benchmark: On real Lean software engineering tasks, Leanstral 1.5 (pass@8) achieves 43.2%, a significant improvement over the previous Leanstral 1.0 (31.0%) and outperforms Claude Opus 4.6 (pass@1) while operating at less than 1/7th the cost.

Paper

Leanstral

That’s a wrap!

If you enjoyed this breakdown, follow for more. I publish new paper explanations most weekdays.

More papers in this series, organized by lab and topic, are in the start here guide.

What paper should I cover next? Let me know in the responses.

By Ritvik Rastogi on August 18, 2026.

Canonical link

Exported from Medium on August 22, 2026.
