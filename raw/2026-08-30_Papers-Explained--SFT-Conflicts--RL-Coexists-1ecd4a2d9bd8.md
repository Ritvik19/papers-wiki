# Papers Explained: SFT Conflicts, RL Coexists

Papers Explained: SFT Conflicts, RL Coexists

Papers Explained: SFT Conflicts, RL Coexists

The paper investigates the differences between Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) for enhancing multi-task…

Papers Explained: SFT Conflicts, RL Coexists

The paper investigates the differences between Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) for enhancing multi-task reasoning in large language models (LLMs). It finds that SFT suffers from severe task conflicts and performance collapse in multi-stage training, while RL enables stable and cumulative improvements due to sparse and approximately orthogonal parameter updates across tasks. Theoretical analysis shows that SFT interference is norm-limited and scales with gradient magnitude, whereas RL interference is variance-limited and bounded, allowing tasks to coexist.

Preliminary Experiments

Model: DeepSeek-R1-Distill-Qwen-1.5B & 7B
Domains: math, science, coding, and logic
SFT Datasets: subset of OpenR1-Math-220k, subset of AM-Thinking-v1-Distilled, AM-DeepSeek-Distilled-40M, knights-and-knaves.
RL Datasets: subset of DeepScaleR-Preview-Dataset, subset of AM-Thinking-v1-Distilled, subset of the DeepCoder-Preview a subset of the knights-and-knaves.
Benchmarks: (MATH500, AIME2025), (MMLU, GPQA-Diamond) Knights & Knaves, and LiveCodeBench.

For LoRA experiments, the rank is set to r = 64 and the scaling factor to α = 32. For multi-stage training, the following task order is chosen: Math, Science, Code, Logic. For RL, GRPO is used.
Accuracy (%) of SFT and RL with different strategies.
Under multi-stage training, SFT suffers a significant decline across tasks, averaging 23.1% below the base model, whereas mixed-data SFT yields a 7.4% gain.
RL exhibits robust improvements in both multi-stage and mixed-data settings, achieving average gains of 24.9% and 12.6%, respectively.
Multi-stage SFT leads to performance collapse, whereas RL enables stable and cumulative performance growth across distinct tasks.Accuracy (%) on all tasks after single-task training using RL and SFT.
SFT improves the target task by an average of 4.0%, it comes at the cost of degradation in untrained tasks, resulting in an average decline of 5.1% across other tasks.
RL achieves a superior average gain of 6.8% on the target task while simultaneously exerting a positive influence on others, yielding an average improvement of 2.3% on untrained tasks.
SFT suffers from task conflicts, where optimizing one capability severely compromises others; in contrast, RL exhibits task coexistence, allowing the model to learn new tasks while preserving existing ones.
Parameter-Level Empirical Analysis

To investigate the mechanism underlying the contrasting generalization behaviors during single-task training, the parameter update dynamics are analyzed. For each task Ti, the parameter update vector ∆Wi is computed and two key geometric properties are evaluated: the magnitude (L2 norm) and the pairwise cosine similarity between tasks.
Analysis of Parameter Update Dynamics across SFT and RL.
Observation 1: The magnitude of RL updates is minimal and sparse.

The average L2 norm of ∆W is approximately 3×10−2 for RL, whereas it reaches 7.4 for SFT, showing a difference of over two orders of magnitude.
RL updates exhibit high sparsity; only about 20% of parameters in RL have magnitudes exceeding 10⁻⁵, compared to 93% in SFT.

Observation 2: The optimization directions of RL across different tasks are approximately orthogonal.

The pairwise cosine similarity of ∆W between different RL tasks is negligible, averaging around 10−5. In contrast, SFT exhibits high similarity across tasks (on the order of 10−1 to 1.0), with some updates even pointing in opposite directions.
Consequently, the ∆Wi for task Ti obtained from RL training can be considered practically orthogonal, resulting in minimal interference with the optimization landscapes of other tasks.
Whereas the ∆Wi from SFT exhibit overlapping optimization directions, which leads to significant mutual interference and the observed catastrophic forgetting.
Unlike SFT, RL induces sparse, minimal updates that are approximately orthogonal across tasks, naturally decoupling the optimization of different ttasks. This parametric mechanism fundamentally explains why RL supports robust multi-stage training.
Theoretical Analysis

Let πθ denote the policy parameterized by θ, πexpert be the supervision distribution. The expected gradients can be formalized as follows:

There are two fundamental distinctions:

Policy Source: SFT is off-policy where the target response y is sampled from the fixed expert distribution (πexpert (ground truth). In contrast, RL is on-policy, where y is sampled from πθ .
Advantage (or Reward) Function: The RL gradient incorporates a scalar weighting term A(x, y).

Sparsity and Small Magnitude of RL Updates

Because RL updates are sparse and small, update vectors from different RL tasks end up being nearly orthogonal to each other in high-dimensional parameter space. Mathematically, in high-dimensional spaces, “sparse vectors tend to be mutually orthogonal with high probability”.

Recent theory, particularly a result called RL’s Razor, explains the origin of this sparsity. The key finding is: “Even without explicitly penalising KL divergence during RL training, on-policy RL implicitly biases the solution toward policies that are closest to the initial policy (in KL-divergence terms).”

In summary, unlike SFT which must bridge a potentially large gap to fit an extrinsic expert distribution, RL implicitly minimizes DKL(π∗||π0). This restriction on deviation directly leads to the observed sparsity and small magnitude in parameter updates.

Qualitative Analysis of Multi-Task Gradients

Consider two different tasks, i and j, with distinct data distributions Di and Dj.

GRPO Gradient: Given input x from task i, generate G rollouts y_k. The empirical gradient for this input is:

where ^A_i,k (x) is the standardized advantage for sample k.

Let the score function: S_i,k (x)=∇_θ logπ_θ (y_k | x).

The advantage function has the “zero-sum property”:∑ ^A_i,k (x) = 0.

Define Gradient Interference between tasks i and j as the expected inner product of their gradient directions.

Gradient Interference in SFT:

Let π∗ denote the expert policy (i.e., the supervision distribution). For a task the target response is y∗ ∼ π∗(·|x). The expert score function S∗i (x) := ∇θ log πθ (y∗i |x). Thus, the expected gradient interference in SFT is as follows:

Gradient Interference in RL:

This can be decomposed using the zero-sum property: Let the mean score function for input x be Sˉi and let the residual be δS_i,k (x)=S _i,k (x)− Sˉi (x). Then:

The gradient interference in SFT and RL can be analysed from two mechanisms:

Mechanism of Advantages

The advantage function “filters out” the mean gradient direction Sˉ , focusing only on residuals from individual rollouts.
This algebraically removes directions common across rollouts, meaning the RL gradient interference only depends on variations (residuals) within the group for the same input, not on the main/high-magnitude directions.
SFT, in contrast, does NOT filter out the mean component and thus dense directions can interfere strongly across tasks.
Thus, Multi-task RL exhibits much less gradient interference compared to SFT.

Mechanism of Policy Source

SFT is off-policy: targets the expert (external) distribution, which may be very different — leading to large, dense, overlapping updates.
RL is on-policy: samples y from the model itself, so rollouts are all close to the same region of function space.
For two different tasks i and j, data distributions Di and Dj are independent, leading to residuals δSi and δSj that are: Statistically independent, Zero mean (due to the advantage) and Sparse.
In high-dimensional parameter spaces, the concentration of measure implies such sparse, zero-mean, independent vectors are approximately orthogonal with high probability.
Thus, RL’s on-policy nature and the advantage filtering ensure that task gradients rarely interfere.

Upper Bound of Gradient Orthogonality

The upper bound on the gradient interference quantifies the qualitative differences established earlier: why RL task gradients are nearly orthogonal, but SFT’s are not.

Assumption 4.4: For any task i:

SFT Score Function Norm: The expected squared L2 norm of the expert score function is capped by Mi² (a constant):

This characterizes how strong/dense the SFT updates for task i can be.

RL Score Function Variance: The expected average intra-group variance (across G rollouts) of the RL residual score function is capped by Vi² (a constant):

This expresses the magnitude of within-group residuals for task i in RL, which are known to be small.

Theorem 4.5: Under Assumption 4.4, the expected gradient inner product for SFT and RL (GRPO) satisfies the following upper bounds:

Interpretation and Key Takeaways:

SFT’s interference is fundamentally limited by the absolute size of the task’s score functions, which are generally large (so interference can also be large).
RL’s interference is limited only by the intra-group residuals’ variance, which, because of the on-policy nature and advantage filtering, remains small through most of training and shrinks further as the model converges.
This means RL’s multi-task gradients remain almost orthogonal, while SFT’s often do not.
Gradient interference in SFT is norm-limited, governed by the absolute magnitude of parameter updates. Conversely, RL interference is variance limited, strictly bounded by the diversity of intra-group rollouts, which filters the common-mode conflicts.
Parallel-RL

The finding that parameter updates for distinct reasoning tasks occupy approximately orthogonal subspace implies that the interference term ⟨∆Wi, ∆Wj ⟩ is negligible. Considering optimization directions are irrelevant, the sum of parameter updates obtained from parallel training of different tasks should theoretically approximate the result of multi-stage training of tasks.

In Parallel-RL, each task can be optimized independently. N parallel RL training processes are launched. Each process i produces a task-specific update ∆Wi. The final model parameter Wfinal is obtained by merging (e.g., linear averaging or SVD) these independent updates.

Several basic strategies for implementing and merging on Parallel-RL are explored.

Naive Parallel-RL employs two strategies: (a) sum: directly summing the ∆Wi, (b) mean: averaging the ∆Wi.
Sparse Parallel considers two sparsification strategies. (a) standard TIES method. (b) SVD on each update and retain only the rank-1 directions for merging.
Adapted Parallel-RL leverages the fact that different RL models enhance the sampling probability of high-reward trajectory for their respective tasks, allowing the merged model to benefit from light post-merge adaptation. After Naive Parallel RL (sum), rapid adaptation is performed using a small subset of samples (5% of the original train-set size) to refine the model.

The accuracy (%) on different tasks.

Even Naive Parallel-RL (sum) allows different task updates (∆Wi) to coexist, largely preserving the performance gains (95%) from single task training and achieving an average improvement of 5.0% over the base model.
Parallel-SFT (sum) suffers from severe task conflicts, with only 66% of the performance of the corresponding single-task SFT retained.
Incorporating sparsification strategies further enhances the compatibility of various ∆Wi for RL. TIES and SVD Parallel-RL respectively retained 98% and 96% of the performance of the corresponding single-task RL.
Adapted Parallel-RL achieves the best performance across most tasks. It delivers a 9.4% gain over the base model and even surpasses individual task-specific models, retaining an average of 102.8% of the Single-Task RL performance.
Despite these gains, this paradigm only needs an additional 5% samples adaptation time compared to single-task training, demonstrating both the efficiency and superior efficacy of our approach.

Paper

SFT Conflicts, RL Coexists: A Theoretical and Empirical Analysis of Multi-Task Learning for LLMs 2608.03573

For a comprehensive understanding of the contrast between SFT and RL, recommend reading: SFT Memorizes, RL Generalizes

That’s a wrap!

If you enjoyed this breakdown, follow for more. I publish new paper explanations most weekdays.

More papers in this series, organized by lab and topic, are in the start here guide.

What paper should I cover next? Let me know in the responses.

View original.

Exported from Medium on August 30, 2026.
