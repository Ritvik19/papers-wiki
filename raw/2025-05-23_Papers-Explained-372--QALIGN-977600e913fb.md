# Papers Explained 372: QALIGN

Papers Explained 372: QALIGN

Papers Explained 372: QALIGN

QLAIGN is a test-time alignment method that uses Markov Chain Monte Carlo (MCMC) sampling to generate a sequence of increasingly aligned…

Papers Explained 372: QALIGN

QLAIGN is a test-time alignment method that uses Markov Chain Monte Carlo (MCMC) sampling to generate a sequence of increasingly aligned text samples, guided by a reward model. It then selects the final output using Minimum Bayes Risk (MBR) over the generated samples.

Background: Language Model Alignment

LLMs generate text sequentially, predicting one token at a time based on the preceding tokens and the initial prompt.

where:

pLM(y | x) is the probability of generating response y given prompt x.
y is the sequence of generated tokens: <y1, y2, …, yN>.
x is the input prompt.
yi represents the i-th token in the response.
y<i represents the sequence of tokens preceding yi.

To align an LLM with human preferences, a reward function r(y, x) is introduced. This function assigns higher scores to responses y that are more desirable given a prompt x. Alignment is then framed as finding a new language model that generates high-reward responses.

Ideally, alignment could be achieved through Bayesian inference.

where:

π(y | x) is the desired probability distribution of the aligned model.
Zβ(x) is the partition function, ensuring π(y | x) sums to 1 over all possible y.
β is a temperature parameter controlling the influence of the reward. A smaller β amplifies the reward’s impact.

However, computing Zβ(x) is intractable due to the vast space of possible responses (Y).

Since exact Bayesian inference is infeasible, a variational approximation qθ(y | x) is used. This involves training a new language model, parameterized by θ, to approximate the desired posterior distribution π(y | x).

where:

qθ(y | x) is the variational approximation (the new LM being trained).
rϕ(y, x) is a learned reward function, potentially different from the true reward r. It is parameterized by ϕ.
DKL represents the Kullback-Leibler divergence, measuring the difference between qθ and pLM. Minimizing this term prevents the new model from deviating too far from the original LM’s capabilities. This acts as a regularizer.
Ex∼D denotes the expectation (average) over prompts x from a dataset D.
Ey∼qθ(y|x) denotes the expectation over responses y drawn from the current approximation qθ.

In practice, alignment is an iterative process. The variational approximation qθ and the reward function rϕ are refined iteratively using human feedback on samples generated from qθ. This feedback loop helps improve both the quality of the generated text and the accuracy of the reward model in capturing human preferences. It also helps address potential issues with the learned reward model exploiting regions where it is less accurate. Methods like Proximal Policy Optimization (PPO) are often used to optimize this objective.

Test-Time Alignment via MCMC

Casting language model alignment as posterior inference decouples the target goal from the procedure used to achieve it. While current approaches rely on variational inference to learn a single model qθ (y | x) this strategy faces four limitations:

Expensive Fine-tuning: Aligning large models requires significant computational resources for fine-tuning.
Limited Access to Model Weights: Many state-of-the-art models, like GPT-4 and Gemini, have restricted access to their weights, hindering fine-tuning efforts.
Compromised Approximation Quality: A single model attempts to approximate alignment across all prompts, potentially sacrificing quality for individual prompts.
Inflexible Preference Encoding: Current methods assume a fixed notion of human preferences, lacking adaptability to diverse user needs or contexts.

The authors advocate for methods that improve approximation quality by increasing compute budget at test time for individual prompts. This involves generating multiple samples and selecting the best one. The core idea is leveraging Markov chain Monte Carlo (MCMC) sampling with LMs to obtain a sequence of samples from the aligned distribution.

Methods for Selecting the Best Response:

Majority Voting (MV): Suitable for tasks with clear answers (e.g., math problems), this method selects the most frequent response among the generated samples.
Minimum Bayes Risk (MBR): A more general approach for open-ended generation tasks. It selects the output that maximizes the expected utility based on a task-specific metric.

where:

yˆ is the selected output.
S is the set of generated samples.
u(y, y’) is the utility function measuring the quality of y compared to y’. ROUGE score is used as the utility metric in this context. While computationally lightweight, efficient approximations can be used for more complex metrics.

Specific Approaches for Alignment:

QALIGN: A novel MCMC-based method to sample directly from the aligned distribution at test time, enabling direct application of MBR.
Importance Sampling: An alternative that reweights samples from the base LM to approximate MBR as if they were drawn from the aligned distribution, avoiding direct sampling from the aligned distribution.
Best-of-n Sampling (BoN): A simpler baseline that selects a single high-reward sample from the base model without explicitly optimizing MBR.

MCMC for Text Generation: QALIGN

The primary goal is to generate text samples (y) conditioned on an input (x) according to a distribution that considers both the language model’s (LM) fluency (pLM(y | x)) and a reward function (r(y, x)). This target distribution is denoted as πβ(y | x), where β controls the influence of the reward.

QALIGN employs the Metropolis-Hastings (MH) algorithm, a standard MCMC method, to sample from the desired distribution. MH constructs a Markov chain of text samples, where each new sample is accepted or rejected based on a specific criterion.

Initialization: The chain starts with an initial sample generated from the language model: y0 ~ pLM(y | x).

Proposal: In each iteration, a new candidate sample (y) is proposed based on the current sample (yt) using a proposal distribution q(y | yt, x). QALIGN uses a specific proposal mechanism inspired by QUEST:

A random index (i) within the current sample (yt) is chosen.
The prefix of yt up to index i (yt<i) is kept.
The LM is used to generate a suffix completion starting from index i: pLM(yi:N | yt<i, x). This forms the proposed sample y. This approach ensures that proposals are similar to the current sample, differing only in the suffix.

Acceptance/Rejection: The proposed sample (y) is accepted with a probability αβ(y, yt), calculated using the Metropolis-Hastings acceptance criterion:

This criterion compares the target distribution probabilities of the current (yt) and proposed (y) samples.
Crucially, the acceptance calculation simplifies to depend only on the reward difference between the two samples and their lengths, avoiding the need to compute the intractable partition function of the target distribution: αβ(y,yt) = min(1, exp(β * (r(x,y) — r(x,yt)) * |yt|/|y|)).
If accepted, the next state in the chain becomes yt+1 = y; otherwise, yt+1 = yt (the chain remains at the current sample).

Importance Sampling

Sample Generation: Generate multiple text samples (y(0), y(1), …, y(T)) from the base LM, pLM(y | x).

Reward Evaluation: Evaluate each generated sample using the reward model r(y, x), obtaining corresponding reward values (r(0), r(1), …, r(T)). This reflects how well each generated sample aligns with the desired properties.

Importance Weight Calculation: Compute importance weights (w(0), w(1), …, w(T)) for each sample. These weights reflect how important each sample is in approximating the target distribution. The weight for a sample is calculated as:

w(i) = exp(r(i)/β) / (∑Tj=0 exp(r(j)/β))

where:

r(i) is the reward of the i-th sample.
β is a temperature parameter that controls the sharpness of the distribution. A lower β leads to a more peaked distribution, emphasizing high-reward samples.

Expectation Approximation: For a given hypothesis y’, approximate the expected utility under the target distribution using the weighted average of the utility function applied to each generated sample:

E[u(y, y’)] ≈ ∑T(i=0) w(i) * u(y(i), y’)

where:

u(y, y’) is the utility function comparing a generated sample y with a hypothesis y’.

Best-of-n Sampling

BoN sampling is a straightforward method for improving the quality of language model predictions during testing. It works by generating multiple candidate responses and selecting the one with the highest reward according to a reward model (RM).

Evaluation

Task Specific Fine Tuning
Average accuracy vs. floating point operations (FLOPS) in log scale.
QALIGN demonstrates progressively lower error rates with increased computational resources on both GSM8K and GSM-Symbolic datasets. It shows robustness to imperfections in the RM and can extract useful signals even when the RM’s reliability is compromised.
MV shows initial improvement but quickly saturates on GSM8K. It exhibits greater robustness to distribution shift compared to BoN and WMV because it doesn’t rely on the RM.
BoN initially outperforms QALIGN on GSM8K but eventually reaches an inflection point where error rates increase. This aligns with previous observations and theoretical results. It struggles more with the distribution shift in GSM-Symbolic due to its reliance on the RM.
WMV performs well on GSM8K initially but deteriorates after a certain computational budget. Like BoN, it struggles with the distribution shift in GSM-Symbolic.
All methods experience performance drops on GSM-Symbolic compared to GSM8K, highlighting the challenge of out-of-distribution generalization in mathematical reasoning. This confirms previous findings about significant performance degradation of LLMs on GSM-Symbolic due to simple variations in problem structure.

General Alignment
Overview of the results on general alignment.Average error rate as a function of inference-time floating point operations (FLOPS) in log scale.
QALIGN, MV, and WMV consistently reduced error rates across all five datasets as the computational budget increased.
MV generally outperformed WMV and BoN in these general alignment tasks, similar to results on GSM-Symbolic.
MV applied to the DPO model initially showed lower error rates but saturated quickly, ultimately performing slightly worse than QALIGN.
BoN’s performance improvement plateaued at a lower computational budget compared to task-specific experiments, suggesting its ineffectiveness for real-world alignment problems.
QALIGN maintained its performance improvement trajectory even with general reward models, demonstrating its effectiveness as a test-time alignment approach.

Paper

Sample, Don’t Search: Rethinking Test-Time Alignment for Language Models 2504.03790

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on May 23, 2025.

Canonical link

Exported from Medium on May 4, 2026.
