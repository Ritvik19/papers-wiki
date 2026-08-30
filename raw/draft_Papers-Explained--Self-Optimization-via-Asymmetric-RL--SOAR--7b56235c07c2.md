# Papers Explained: Self-Optimization via Asymmetric RL (SOAR)

Papers Explained: Self-Optimization via Asymmetric RL (SOAR)

Papers Explained: Self-Optimization via Asymmetric RL (SOAR)

Self-Optimization via Asymmetric RL (SOAR) is an asymmetric self-play framework where a pretrained LLM acts as both teacher and student…

Papers Explained: Self-Optimization via Asymmetric RL (SOAR)

Self-Optimization via Asymmetric RL (SOAR) is an asymmetric self-play framework where a pretrained LLM acts as both teacher and student: the teacher proposes synthetic problems, and is rewarded when the student improves on a subset of hard problems, thus generating a self-guided curriculum.

Method

The framework adopts the teacher-student setup of asymmetric self-play, to “kickstart” learning on datasets where the initial success rate is too low for successful training. Two copies of the same model are instantiated: a teacher πTϕ and a student πSθ. At step zero, θ = ϕ = θbase.

The teacher’s role is to generate synthetic problems that provide the student with the necessary gradient signal to escape the performance plateau. Intuitively, while the teacher may be unable to solve a difficult problem directly, it may still possess the knowledge to generate easier problems that provide a non-zero reward to the student and shift its policy towards progress on the original problem.

This problem is formulated as a bilevel optimization problem. The objective is to generate a small synthetic dataset X = {(qi, ai)}n i=1 of question-answer pairs such that training πS θ on X with RL improves performance on the target domain:

where RL-update describes the RL training procedure of the student on X , yielding parameters θ′(X ), and R denotes the updated student’s performance on Dtrain.

This objective is instantiated as a nested meta-RL loop:

Outer RL loop: Train the teacher with RLOO to generate question-answer pairs.
Inner RL loop: Train the student with standard RLVR (also RLOO) on teacher-generated problems. The subsequent performance improvement of the student on Dtrain is the black-box reward signal for the teacher.

Automatic verification of synthetic question well-posedness or answer correctness is not assumed. Instead, the teacher generates both the question and answer, treating the question utility as an emergent property of the teacher’s reward signal. Critically, the teacher’s objective is grounded in measured student progress on Dtrain. SOAR only rewards a synthetic question-answer pair if training on it improves student performance on ground-truth problems. The teacher is not shown the hard problems during training, but rather discovers useful stepping stones purely from this student improvement signal.
The SOAR meta-RL Loop.
Outer Loop: Teacher Training

Let g denote the RLOO group size and n the size of the generated dataset X. At each iteration, g · n rollouts y₁, …, y₍g·n₎ are sampled from πT_ϕ, subdivided into g datasets of n items each: X₁ = {y₁, …, yₙ}, …, Xg = {y[g(n−1)+1], …, ygn}. Each rollout yi is parsed into yi = (qi, ai).

Each dataset Xk receives a reward. At each outer-loop iteration, a set of reward questions QR is subsampled from the original training set Dtrain. The student is trained on each dataset Xk for a fixed number of steps, resulting in trained student πS_θ′_k. The dataset-level reward R(Xk) is then the average greedy success of πS_θ′_k on QR relative to the success of a baseline student model πS_θ:

Here, πS_θ is the initial student when starting the inner loop. The initial student accuracy is subtracted so that teacher rewards are normalized across outer-loop steps, which is necessary for the student promotion mechanism.

To mitigate reward variance, rewards are averaged over r parallel student trainings per dataset. This averaged reward is assigned to each rollout in Xk to update the teacher.

Inner Loop: Student Training

The student πSθ trains on the teacher-generated dataset Xk using RLOO for 10 steps (batch size 8), long enough to induce measurable movement while minimizing computational cost. After each inner loop, the student reverts to the baseline policy for the next iteration. A promotion mechanism is introduced to accumulate student improvement and useful questions across inner loops. A rolling moving average of teacher rewards ¯Rt is tracked; when it exceeds a fixed threshold τ, the baseline student πSθ is updated to the student trained on the best Xk. Subsequent rewards measure improvement relative to this new baseline. The accumulated datasets that led to student promotions are denoted as Dbest; these constitute the Promotion Questions (PQ) that are evaluated in the experiments.

Experiment Setup

The experiments mainly use Llama-3.2–3B-Instruct, with ablations extending to Llama-3.1–8B-Instruct. The teacher and student are initialized from the base model and SOAR is trained on MATH and HARP, keeping OlympiadBench held-out.

For each dataset, 128 samples per problem are drawn with the target model, retaining those with a 0/128 success rate. These subsets are referred to as fail@128 datasets; 128 serves as a practical but stringent threshold at which, empirically, direct training yields only marginal improvement. Each is randomly split 50–50 into training and test sets. Given the low baseline pass rates on fail@128 problems, this larger test set is necessary to distinguish performance gains from stochastic variance.

200 outer-loop steps are allocated based on compute constraints. Each outer-loop iteration samples n = 64 problems (X) from the teacher, and 64 reward questions (QR) from the fail@128 train set (Dtrain). The student baseline is promoted when the 3-step moving average of teacher rewards exceeds τ = 0.01.

SOAR is assessed in two ways:

Promoted Student (PS): The model with the best validation performance across multiple training promotions is selected (typically after training with 128, 192, or 256 synthetic questions), and its test set accuracy is measured to gauge direct performance gains from SOAR.
Promotion Questions (PQ): A new base student is trained using standard RLOO on a combination of the “Promotion Questions” (Dbest) and the fail@128 train set. This setup evaluates the value of the synthetic questions independently of the PS model’s training trajectory.

Baselines Compared:

Hard-Only: Models trained only on the real fail@128 train set (group size 32), and also with a larger group size of 128 on MATH, to separate meta-RL loop effects from extra compute.
Intrinsic Teacher (Intrinsic-T): Trained similarly to SOAR, but the reward signal is replaced with a “learnability objective” (moderate difficulty questions), not grounded in data. Students are evaluated by training on 128 problems sampled from this teacher plus the fail@128 set, per the PQ protocol.
SeRL: A self-play baseline where the curriculum evolves from a seed set (MATH and HARP fail@128 sets) using self-rewards and diversity/learnability filters, trained with Llama-3.2–3B-Instruct.
Upper Bound: Student trained on the full MATH train split (6750 problems) plus fail@128, serving as an upper-bound for performance if all human-curated stepping stones are available.

Evaluation
Performance on MATH/HARP fail@128 (improvement over Hard-Only).
Meta-RL-generated synthetic questions (PQ) outperform other curriculum methods.
PQ yields higher test performance increases (up to +9.3% pass@32 on MATH and +4.2% on HARP) compared to Hard-Only or Intrinsic-T baselines, especially at higher k (number of solution attempts)
Transfer performance to OlympiadBench fail@128 subset (improvement over Hard-Only).
Synthetic questions derived from meta-RL (PQ-MATH, PQ-HARP, Intrinsic-T) robustly transfer to OOD datasets (OlympiadBench), indicating that the induced reasoning pathways generalize effectively beyond the target training distribution

Paper

Teaching Models to Teach Themselves: Reasoning at the Edge of Learnability 2601.18778

That’s a wrap!

If you enjoyed this breakdown, follow for more. I publish new paper explanations most weekdays.

More papers in this series, organized by lab and topic, are in the start here guide.

What paper should I cover next? Let me know in the responses.

View original.

Exported from Medium on August 22, 2026.
