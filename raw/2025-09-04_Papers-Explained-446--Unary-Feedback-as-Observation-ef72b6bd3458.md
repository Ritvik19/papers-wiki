# Papers Explained 446: Unary Feedback as Observation

Papers Explained 446: Unary Feedback as Observation

Papers Explained 446: Unary Feedback as Observation

Models trained with existing RL paradigms often lose their ability to solve problems across multiple turns and struggle to revise answers…

Papers Explained 446: Unary Feedback as Observation

Models trained with existing RL paradigms often lose their ability to solve problems across multiple turns and struggle to revise answers based on contextual feedback, leading to repetitive responses. Training models with multi-turn RL using only unary feedback (for example, “Let’s try again”) after wrong answers can improve both single-turn performance and multi-turn reasoning. Unary Feedback as Observation (UFO) for reinforcement learning uses minimal yet common unary user feedback during iterative problem solving.

The project is available on GitHub.

Single-Turn RL Leads to Collapsed Multi-Turn Reasoning
Single-turn RL causes LLMs to repeat the same answer across turns instead of revising based on feedback.
Models trained with single-turn RL are examined in multi-turn interaction settings. Specifically, in practical use cases such as tutoring or mathematical assistance, users typically offer minimal feedback (e.g., “try again”) and expect the model to adjust its reasoning accordingly. However, single-turn RL models are found to be effective solvers but poor revisers, consistently failing to incorporate feedback. A pre-trained model refines its answer across turns, while a single-turn RL model fails to revise, repeating its initial output. To quantify this behavior, effective answer is used as the metric, which is defined as a new answer that has not been given in the previous turns.

For off-the-shelf LLMs, models fine-tuned with various RL algorithms including PPO, GRPO, DAPO, and Dr. GRPO are selected.
Hugging Face model names used in the unique answer ratio evaluation.Comparison of effective (unique) answer ratio (%) before and after RL training.
All models exhibit a noticeable decline in the unique answer ratio after RL training, and the extent varies by method and model size.

Training Multi-Turn Reasoning Models with Unary Feedback

The process of multi-turn problem solving based on static single-turn datasets is modeled as a finite-horizon Markov Decision Process (MDP), defined by the tuple (S, A, P, 𝑅, 𝑇max).

S is the state space
A is the action space consisting of all possible answers
P is the transition function defined by the agent–environment interaction.
𝑅 is the reward function
𝑇max is the maximum number of interaction steps per episode.

At each turn 𝑡, the agent observes a state 𝑠𝑡 ∈S that encodes the original question 𝑞and the history of past attempts and feedbacks.

where 𝑎𝑘 denotes the 𝑘-th answer, and 𝑓𝑘 is a feedback token returned by the environment. The agent then generates an answer 𝑎𝑡 ∼𝜋𝜃(·|𝑠𝑡)and receives a scalar reward:

The episode ends when the agent provides a correct answer or reaches the maximum number of steps 𝑇max.

Unary Feedback as Observation (UFO)
The UFO framework for multi-turn training.
The key idea is to restrict 𝑓𝑘 in the observation to negative signals only. Specifically, when an answer 𝑎𝑘 is incorrect, the feedback is a generic signal such as TryAgain. When the agent produces a correct answer, the episode terminates immediately. Consequently, no explicit positive confirmation (e.g., Correct) is ever added to the state history. The agent thus only receives unary feedback and must learn to revise its answers based solely on a history of failed attempts. In practice, the prompt is constructed as a natural-language sequence concatenating all previous attempts and their feedback.

Reinforcement Learning with Unary Feedback

The agent is optimized using reinforcement learning to learn revision-aware and multi-turn policies. Proximal Policy Optimization (PPO) is adopted to train the policy 𝜋𝜃, which shows that a learned critic enables fine-grained value estimates and stabilizes optimization. At each episode, the agent interacts with a problem over multiple rounds. At each turn 𝑡, it observes input 𝑥𝑡, generates an answer 𝑎𝑡, and receives a binary reward 𝑟𝑡 ∈{0, 1}. The resulting trajectory is defined as:

where 𝑇 ⩽ 𝑇max is the number of turns before success or termination. The objective is to maximize the expected return:

PPO with a clipped surrogate objective is applied. For each training batch, the advantage 𝐴𝑡^ is estimated using a baseline value function and the policy is updated as:

The UFO design enables the policy to condition on the full history of failure signals, giving rise to context-sensitive behaviors such as error correction, elimination, and hypothesis refinement capabilities that are difficult to elicit through static supervision alone.

Reward Design for Adaptive Reasoning

Binary correctness signals offer a minimal form of supervision, but they could induce suboptimal behavior such as blind trial-and-error or repeated guesses. To encourage more efficient and reflective reasoning, a trajectory-level reward decay with repetition penalty is introduced. Reward decay encourages minimality by favoring trajectories that reach correct answers in fewer turns, thereby promoting concise and purposeful reasoning, while the repetition penalty promotes diversity by discouraging repetitive generations and encouraging the model to explore alternative strategies upon failure.

Formally, reward decay promotes early success by assigning exponentially diminishing rewards to correct answers produced at later turns.

where 𝛾 ∈(0, 1)is a decay factor that favors solving the problem in fewer turns.

Repetition penalty is defined based on the number of effective answers — i.e., responses that have not been submitted previously in the same episode. Let 𝑇 denote the number of turns in the episode, and 𝐸(𝜏)be the number of effective answers in the trajectory 𝜏. A normalized penalty term is defined:

The trajectory-level reward for RL training is defined as:

where 𝜆 > 0 is a tunable penalty weight, and 𝐸(𝜏)/𝑇 measures answer diversity. The penalty is maximized when all answers are identical, and vanishes when all are distinct.

To ensure syntactic validity and improve training stability, a small penalty 𝜂 < 0 is applied for each invalid output across turns. This penalty is applied when the model produces malformed or missing answers.

Experiment Setup

Major experiments are conducted on the MATH subset of the MetaMathQA dataset (MMQ-Math), where data are augmented from the MATH training sets. Six widely-used datasets are selected to evaluate training generalization.

MMQ-Math requires multi-step symbolic and numerical reasoning to solve complex math word problems.
TheoremQA evaluates formal mathematics understanding through questions about theorem statements and proofs.
HotPotQA tests multi-hop factual reasoning across Wikipedia passages
ConcurrentQA focuses on temporal and causal reasoning in concurrent event settings.
MMLU assesses general-knowledge proficiency across 57 academic subjects,
MMLU-Pro covers more specialized expert domains.

Qwen-2.5–3B-Instruct is trained with PPO for 200 optimization steps. Each batch samples 𝑃=8 prompts, with 𝑁=16 rollouts per prompt. During training, the maximum number of turns per episode, 𝑇max, is set to 1, 5, and 10, respectively. For the validation phase, 𝑇max is fixed at 5 turns.

Results

Multi-turn RL Unlocks Higher Upper Bound of LLM Reasoning

Multi-turn training consistently outperforms single-turn baseline, achieving up to 14% higher success rate with comparable inference cost
Performance comparison when evaluating with 5 turns after training with different maximum turns (1, 5, and 10).
Larger training budgets (𝑇max = 10 and 𝑇max = 5) yield enhanced performance, delivering more than a 6% relative improvement over single-turn training at their peak.
Validation performance (Succ@k) of models trained with different roll-out turns under varying inferencetime turn budgets.
Models trained under multi-turn conditions show superior Succ@𝑘 performance across varied inference-time interaction budgets, even at the lowest inference budget (𝑘= 1).
5-turn success rate (%) across different tasks and training settings.
Applying 5-turn UFO on top of task-specific RL consistently improves performance across all domains, enhancing multi-turn reasoning and generalization to out-of-domain tasks.
On MMQ-Math, 5-turn UFO raises performance from 52.3% to 88.5%.
UFO provides gains in cross-task generalization: +8.8 points on TheoremQA, +7.1 points on HotPotQA, and +2.3 points on ConcurrentQA when trained on MMQ-Math.
Training on HotPotQA with UFO improves downstream performance on TheoremQA (+0.9), MMLU (+5.1), and ConcurrentQA (+0.2).
In the general knowledge domain, UFO recovers and surpasses original accuracy on MMLU, reaching 85.2%, and boosts performance on MMLU-Pro from 48.3% to 60.9%.

Multi-turn Setting Enables LRMs to Revise From Feedback
Comparison of success rate with multi-turn setting.
Providing explicit feedback during multi-turn training leads to an over 8% peak performance improvement.
Multi-turn training, even with feedback prompts only during training, can intrinsically enhance model reasoning capabilities.
Validation under different verbal feedback prompts.
The effectiveness of the approach is preserved across a range of prompt formulations, indicating practical applicability.

Reward Shaping Encourages Efficient Problem Solving
Comparison of reward shaping strategies.
Exponential reward decay reduces the mean number of actions by approximately 10% without significantly affecting overall success rates. This suggests it encourages more profound self-reflection and systematic thinking.
The model learns to be more deliberate and efficient, minimizing redundant interactions when trained with exponential decay.
The percentage of non-repetitive answers increases from 80% to 90% during training, indicating improved model performance in generating diverse responses and reducing duplicate answers.
Proportion of effective answers over training.
Reducing duplicate answers is important because high repetition rates lead to higher penalties and lower overall rewards.

Paper

A Simple “Try Again” Can Elicit Multi-Turn LLM Reasoning 2507.14295

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on September 4, 2025.

Canonical link

Exported from Medium on May 4, 2026.
