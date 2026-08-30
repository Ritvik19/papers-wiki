# Papers Explained: Unsupervised Process Reward Models

Papers Explained: Unsupervised Process Reward Models

Papers Explained: Unsupervised Process Reward Models

This work proposes a method for training unsupervised PRMs (uPRM) that requires no human supervision, neither at the level of step-by-step…

Papers Explained: Unsupervised Process Reward Models

This work proposes a method for training unsupervised PRMs (uPRM) that requires no human supervision, neither at the level of step-by-step annotations nor through ground-truth verification of final answers. The key idea behind this approach is to define a scoring function, derived from LLM next-token probabilities, that jointly assesses candidate positions of first erroneous steps across a batch of reasoning trajectories.

Supervised Process Reward Models

A trajectory consists of a problem (x) and a sequence of reasoning steps (y = (y_1, …, y_T)) At each step (t), a correctness label (c_t ∈ {0, 1} is assigned, where (c_t = 1) means the step is correct, and (c_t = 0) means it’s incorrect.

The PRM (ri ( ct | t ≤ τ ) ) defines a probability that the current step (y_t) is correct, given all prior steps.

In practice, training a PRM requires a labeled dataset D where each solution trajectory t is paired with the corresponding ground truth label j^gt that indicates the position of the first erroneous step.

Given such labeled dataset, PRM is usually trained with the maximum likelihood objective:

with the log-likelihood log pi (j|t ) defined as:

LLMs as Scoring Functions

LLMs, given a prompt, assign probabilities to possible next tokens (words or parts of words). By creating a specific template (for example, “Albert Einstein won [award] in [year] for [contribution]”) and filling in different candidate answers, one can use the model’s probabilities to measure how plausible each candidate is.

Unsupervised Process Reward Models

The goal is to train a PRM without relying on the curated labels. The key idea is to define a scoring function derived from LLM next-token probabilities, which measures how plausible a candidate position of the first erroneous step is in a given trajectory.

Scoring First Erroneous Position with LLMs

Consider a trajectory τ = (x, y1, . . . , yT ) and a candidate position of the first erroneous step j ∈ {1, . . . , T + 1}. To define the scoring function, reasoning steps are interleaved with correctness labels, marking steps y1, . . . , yj−1 as correct and step yj as incorrect, resulting into a sequence:

where “+” and “-” denote correct and incorrect labels respectively. The special case j = T + 1 (no error) corresponds to all steps marked as correct:

The constructed sequence is fed to an LLM and the next-token probabilities assigned by the LLM to each label are extracted to define the scoring function S(j; s) as follows:

where p+ and p- denote the LLM’s next-token probabilities of generating the label tokens “+” and “-” after yt, respectively, renormalized over {+, -}.

Scoring Multiple Trajectories at Once

Recent works have shown that LLMs produce more reliable judgments when evaluating multiple instances jointly rather than independently. To jointly score a batch of trajectories, marked sequences s(τn, jn) are concatenated together, obtaining:

It is worth noting that in this formulation, the score for a trajectory τn is computed given the previous trajectories τ1, . . . , τn−1 along with their candidate labels j1, . . . , jn−1 as in-context examples.

Training PRM via Optimizing Joint Score

PRM rθ (ct|τ≤t) is parameterized by applying LoRA [42] to the same LLM used for computing the joint score. Given a trajectory τ = (x, y1, . . . , yT ), a sequence is constructed by interleaving each reasoning step with a special token [*]:

where the embedding of [] is trainable. This sequence is processed with the LLM and the last-layer hidden state zt is extracted at each [] token position following step yt.

To obtain step-level correctness probabilities, the language modeling head is replaced with a two-layer MLP with ReLU activation that projects each hidden state to two logits:

which are converted to probabilities via softmax.

pθ is trained by optimizing the following entropy-regularized objective:

where H(·) denotes Shannon entropy that prevents pθ from premature convergence, and γ corresponds to the regularization strength. γ is set by monitoring the training curves and choosing the value that prevents collapse of rθ throughout the training.

Experiments

Qwen2.5–14B-Instruct is employed to calculate the joint score and instantiate the PRM rθ. uPRM is trained on the PRM800K dataset using only the reasoning trajectories without any correctness labels.
Results on the ProcessBench dataset (F1 score).
uPRM consistently outperforms the LLM-as-a-Judge baseline on all ProcessBench datasets.
The improvements are especially large on harder datasets (OlympiadBench and Omni-MATH: +13% F1 each).
Accuracy of LLMs across different scales.
uPRM helps improve accuracy as compute budget increases, especially in smaller LLMs.
The benefits of uPRM depend strongly on model size and sampling strategy (e.g., DVTS is especially helpful for small models but degrades with larger LLMs).
Performance comparison between supervised PRMs and uPRM on Best-of-8 strategy for
generations from Qwen2.5-Math-7B-Instruct.
uPRM matches or is competitive with several supervised PRMs (both generic and math-specialized), even though it was trained fully unsupervised.
Accuracy on mathematical benchmarks after RL training with different reward sources.
Using uPRM as a reward in RL (within PURE and RLOO training) produces policies that are comparable or even superior to those trained with ground-truth verifiable reward or with supervised PRMs.

Paper

Unsupervised Process Reward Models 2605.10158

That’s a wrap!

If you enjoyed this breakdown, follow for more. I publish new paper explanations most weekdays.

More papers in this series, organized by lab and topic, are in the start here guide.

What paper should I cover next? Let me know in the responses.

View original.

Exported from Medium on August 22, 2026.
