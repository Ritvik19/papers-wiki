# Papers Explained 588: LLM-as-a-Verifier

Papers Explained 588: LLM-as-a-Verifier

Papers Explained 588: LLM-as-a-Verifier

LLM-as-a-Verifier is a general-purpose verification framework that provides fine grained feedback for agentic tasks without requiring…

Papers Explained 588: LLM-as-a-Verifier

LLM-as-a-Verifier is a general-purpose verification framework that provides fine grained feedback for agentic tasks without requiring additional training. Unlike standard LM judges that prompt LLMs to produce discrete scores for candidate solutions, LLM-as-a-Verifier computes the expectation over the distribution of scoring token logits to generate continuous scores.

The project is available at GitHub.

Methodology

By definition, a judge is one who forms an overall opinion and assigns a decision, whereas a verifier is one who confirms the truth or correctness of something and requires more detailed evaluations

Let 𝑉score = {𝑣1, . . . , 𝑣𝐺} denote an ordered set of tokens representing discrete score levels. Given a task prompt 𝑥, a language model 𝑝𝜃, a criterion 𝑐, and two candidate trajectories 𝜏𝑖 and 𝜏𝑗 , scoring prompts are constructed and their conditional distributions 𝑝𝜃(𝑣 | 𝑥, 𝑐, 𝜏𝑖) and 𝑝𝜃(𝑣 | 𝑥, 𝑐, 𝜏𝑗 ) are obtained by extracting the logprobs from < 𝑠𝑐𝑜𝑟𝑒𝐴 > and < 𝑠𝑐𝑜𝑟𝑒𝐵 > tags using the following prompt:
You are an expert [domain] reviewer. You will see a task description and two trajectories.
Evaluation Criteria: [domain specific criteria]
Task: {task prompt}
Trajectory A: {A} Trajectory B: {B}
Carefully analyze each trajectory, then provide your final scores:
<score_A> INTEGER_1_TO_20 </score_A>
<score_B> INTEGER_1_TO_20 </score_B>
Rating Rules: Rate correctness on a 1–20 scale based on evaluation criteria (1 = incorrect,
10 = borderline, 20 = correct)
Note: We use a letter-based scale instead of digits to enable logprob extraction for
granularity scaling.
Rather than collapsing each distribution to a single discrete score, the reward of a trajectory is approximated as:

where 𝐶 is the number of evaluation criteria, 𝐾 is the number of repeated verifications, 𝐺 is the number of score tokens (granularity level), 𝑝𝜃(𝑣𝑔 | 𝑥, 𝑐, 𝜏) is the probability assigned by model 𝜃 to score token 𝑣𝑔, and 𝜑(𝑣𝑔) maps each score token to a scalar value. First, 𝑅(𝑥, 𝜏 ) ∈ [0, 1] is normalized by the linear map 𝑅 ↦ (𝑅 − 𝜑min)/(𝜑max − 𝜑min). These continuous rewards are then converted into a pairwise preference using the Bradley–Terry model, treating 𝑅(𝑥, 𝜏 ) as the latent strength of trajectory 𝜏:

To pick the best trajectory among 𝑁 candidates, a round-robin tournament can be run that scores all nC2 pairs and accumulates wins.

However, such a schedule scales as 𝒪(𝑁²) pairwise verifications and quickly dominates verifier cost as 𝑁 grows. A budget-efficient alternative, Probabilistic Pivot Tournament (PPT), is proposed in which every candidate is compared only against a small set of 𝑘 ≪ 𝑁 pivots, reducing the budget from 𝒪(𝑁²) to 𝒪(𝑁𝑘). Critically, the choice of pivots determines whether the saved budget is well spent: arbitrary anchors waste verifications on candidates that are clearly weak.
Probabilistic Pivot Tournament.
Ring pass: A uniformly random Hamiltonian cycle 𝛾 is sampled over {1, . . . , 𝑁}, and the 𝑁 adjacent pairs are scored.
Pivot selection: Candidates are ranked by their ring-pass mean preference 𝑤𝑖/𝑐𝑖 and the top-𝑘 are chosen as the pivot set 𝒫. Selecting pivots from the empirical leaders allocates the remaining verification budget to the candidates most likely to be correct, so the subsequent pairwise comparisons distinguish among uncertain top candidates rather than spending queries on weak anchors.
Pivot rounds: With the pivot set fixed, (i) every non-pivot vs. pivot pair and (ii) every pivot vs. pivot pair are scored. All ring and pivot-round comparisons are aggregated into the same 𝑤𝑖, 𝑐𝑖, and 𝑖⋆ ∈ arg max𝑖 𝑤𝑖/𝑐𝑖 is selected. Normalizing by 𝑐𝑖 removes the bias that pivots participate in more comparisons than non-pivots.
Probabilistic Pivot Tournament with Ring-based Pivot Selection.
Verification Scaling

There are three independent axes along which verification can be scaled: the granularity of score tokens 𝐺, the number of repeated evaluations 𝐾, and the number of evaluation criteria 𝐶. Each axis targets a different source of error in the reward estimate, and the three act as complementary levers:

Granularity of Score Tokens (𝐺): This axis refers to how finely the verifier can score solutions; 𝐺 is the number of discrete scoring tokens available. More scoring tokens do NOT give the verifier more information, but they do let the system express finer distinctions between answers, mapping small differences in model beliefs into the scoring space.
Number of Repeated Evaluations (𝐾): This axis controls how many independent times the verifier evaluates the same solution. Repeated evaluation (𝐾) doesn’t change granularity, but reduces the variance by averaging over 𝐾 runs (the variance shrinks with 𝑂(1/𝐾)).
Number of Evaluation Criteria (𝐶): Instead of judging with one broad criterion (e.g., “is this correct?”), decompose the task into 𝐶 simpler, logically distinct sub-criteria. Monolithic criteria can conflate many factors and cause the verifier to overlook or overweight specific aspects based on prompt phrasing or salience. Each sub-criterion is easier and more reliable for the verifier to evaluate. The final score/reward is averaged over the 𝐶 criteria.
Verification Scaling.
For all scaling experiments, Gemini 2.5 Flash is used as the verifier, which allows extraction of up to 20 top logprobs per scoring token. Verification accuracy on 200 randomly sampled trajectories from Terminal-Bench 2.0 improves along all three dimensions, rising from 73.1% at 𝐺=1 to 77.5% at 𝐺=20, from 74.7% at 𝐾=1 to 77.4% at 𝐾=16, and from 75.2%–76.4% for any single criterion to 78.3% when the three criteria are ensembled.

Fine-grained Verifier Signals as a Proxy for Task Progress

LLM-as-a-Verifier produces fine-grained output, serving as a scalar proxy for agent task progress. This is quantified using the Value-Order Correlation (VOC), which is the Spearman rank correlation between step index and the verifier’s score for that step’s trajectory prefix.

Ideally, a good verifier would assign monotonically increasing scores during successful rollouts (VOC approaches 1) and be robust to failure (e.g., not fooled by regressions or stalls).

Dense Reward for Reinforcement Learning

A long-time challenge in RL is addressed by using the fine-grained score from LLM-as-a-Verifier as a dense reward signal. This score serves as a drop-in dense reward for both off-policy and on-policy RL, enhancing sample efficiency without requiring extra reward-model training or environment-specific reward shaping.

LLM-as-a-Verifier can be used to evaluate each reasoning trace (using the probabilistic pivot tournament), assigning each a normalized preference score 𝑅 ∈[0,1] to capture reasoning quality, even if final answers are the same.

Paper

LLM-as-a-Verifier: A General-Purpose Verification Framework 2607.05391

That’s a wrap!

If you enjoyed this breakdown, follow for more. I publish new paper explanations most weekdays.

More papers in this series, organized by lab and topic, are in the start here guide.

What’s the paper you most want covered next? Let me know below.

This connects to a broader thread on rubric-based rewards for RL: see the related papers here.

By Ritvik Rastogi on August 5, 2026.

Canonical link

Exported from Medium on August 22, 2026.
