# Papers Explained: No Position Encoding (NoPE)

Papers Explained: No Position Encoding (NoPE)

Papers Explained: No Position Encoding (NoPE)

This work conducts a systematic empirical study comparing the length generalization performance of decoder-only Transformers with five…

Papers Explained: No Position Encoding (NoPE)

This work conducts a systematic empirical study comparing the length generalization performance of decoder-only Transformers with five different position encoding approaches including Absolute Position Embedding (APE), T5’s Relative PE, ALiBi, and Rotary, in addition to Transformers without positional encoding (NoPE). The results reveal that the most commonly used positional encoding methods are not well suited for length generalization in downstream tasks. More importantly, NoPE outperforms other explicit positional encoding methods while requiring no additional computation.

Experiment Setup

The focus is on algorithmic tasks such as copying, addition, etc. For each task, training is performed on a finite number of examples of up to a certain length, with testing conducted on both seen and unseen lengths at inference. Formally, let D = {(xi, yi)} denote a dataset of such task where xi is the input and yi is the output sequence. For each task, a function λ : D → N can be defined that returns the length bucket of a task instance d ∈ D. This can be the number of tokens or any general notion of length/depth of reasoning. Using this function and a threshold L, samples where λ ≤ L are employed for learning the task and samples where λ > L are used for evaluating generalization. The performance on each instance is reported as the exact-match accuracy of its answer with the ground truth.
Examples of the input and output of the tasks.
A conventional decoder-only Transformer architecture is used as a base for all experiments, considering different approaches for encoding positions: Absolute Position Embedding (APE), ALiBi, Rotary, T5’s Relative Bias, and removing the positional encoding (NoPE). Note that APE with sinusoidal functions is used, as the learnable variant cannot produce embeddings for unseen positions.

The Effect of Positional Encoding?
The generalization behavior of different positional encodings on 6 datasets.
T5’s Relative Bias consistently outperforms other explicit positional encodings in most extrapolation scenarios.
ALiBi achieves moderate results, generally positioned in the middle of the ranked models.
Both APE and Rotary positional encodings display poor generalization performance for longer sequence lengths, with Rotary behaving more like APE than other relative schemes, despite its reputation.
The NoPE model surprisingly matches or exceeds T5’s Relative Bias in performance on generalization, without additional computational overhead.
The computational cost of T5’s Relative Bias is significant, with potential to double training and inference time compared to APE, while NoPE avoids such cost.

How Does NoPE Represent Positions

The central idea is: Causal attention provides an implicit notion of “how far into the sequence I am,” because token t sees exactly t previous/current tokens; the network can turn this prefix length into an absolute position, and subsequent attention layers can subtract two absolute positions to obtain relative distance.

Absolute Positional Encoding in NoPE
Theorem 1 (Absolute Encoding): Let x be an input sequence of length T + 1 to the model. Then, the first layer of fθ can recover absolute positions [1, . . . , T + 1] in the hidden state H(1). That is, there exist WQ, WK , WV , WO , W1, and W2 such that the self-attention and feedforward operations in the first layer compute absolute positions and write it to the next hidden state.
In this parameterization, only the first three dimensions of the hidden states are required. The rest of the heads, as long as they do not override the first three dimensions, can be arbitrary. This does not impose any challenges as Transformers used in practice usually have a very large model dimension d.

First, the word embedding matrix WE is constructed, where each column is the embedding of a token in the vocabulary. This matrix is defined such that it always sets the first dimension of every embedding vector to be 1. Additionally, it sets the second dimension to 1 if and only if the token is <bos>. Otherwise, it sets it to zero. The third dimension of all embedding vectors is set to zero.

Secondly, for head dimensions h ≥ 1, the weights WQ, WK, WV, WO of the first attention head in the first layer are constructed. Specifically:

WQ can be any arbitrary matrix.
WK reads from the first dimension of the hidden state, which is initialized with 1 using the embedding matrix. Since all word embeddings have one in their first dimension, this parameterization will result all key vectors to be the same i.e. I.
WV reads from the second dimension of the hidden state, which is initialized with 1 if the token is <bos>. So, the value vector will have 1 in its first dimension only if the corresponding token is <bos>.
WO will write the result of the attention to the third dimension of the hidden state.

For any input sequence x = [<bos>, x1, . . . , xT ], the first layer can recover absolute positions [1, . . . , T + 1] in the hidden state H(1).

First, the word embedding matrix WE is used to compute the embedding H(0):

Compute the query vector qt = WQ . h_t(0).

Compute the key vectors by applying ki = WK . h_i(0)

Note that all key vectors are the same and only need to be computed up to position t as the attention mask is causal, i.e., query can only look at positions ≤ t. Next, the attention weight vectors α are computed:

where α ∗ = q1 + q2 + . . . + qh. 

Softmax is applied to compute the attention probabilities. There are t copies of the same value because, due to the causal mask, position t can attend to positions 1,…,t.

Compute the value vectors by applying vi = WV . h_i(0):

Because the second dimension of the embedding is 1 just for <BOS> and 0 for every other token.

Compute the output of the attention head by applying WO:

Thus, the output of the constructed attention head recovers the absolute position information and writes it to the third dimension of output.

With this information available to the rest of the network, the feedforward sub-layer, with sufficient hidden width, can recover the absolute positions [1, 2, . . . , T +1] from the third dimension of attention output.

Relative Positional Encoding in NoPE
Theorem 2 (Relative Encoding): Suppose that the hidden state H(1) contains absolute positional information, as stated in Theorem 1, and assume that it is not overwritten by any subsequent layers. Then, the self-attention in all subsequent layers can implement a relative positional encoding: there exists a parameterization of fθ such that, for l ≥ 2, the attention dot product between query qt and key ki at positions t and i (t ≥ i) can be expressed as: ⟨qt, ki⟩ = fcnt(qt, ki) + frel(t − i) (1) where fcnt is a function of their content, and frel is a function of their relative distance.
For head dimension h ≥ 2, construct the weights WQ, WK of the attention heads in the second layers and above:

The corresponding WV and WO can take any arbitrary values as long as they do not override the first three dimensions of the residual stream.

Assume that absolute positions are computed in the hidden state H(l)
for l ≥ 1, as stated in Theorem 1:

Compute the query vector qt by applying qt = WQ . h_t(l):

Compute the key vectors by applying ki = WK . h_i(l):

So, for ki:

The attention dot product between qt and ki:

Thus, the dot product between qt and ki depends on the relative distance between tokens.

Note that the proof uses the linear spacing between tokens, but the MLP the first layer can write any arbitrary function of absolute positions to the third dimension of the hidden state, which enables more complex relative encoding schemes.

Paper

The Impact of Positional Encoding on Length Generalization in Transformers 2305.19466

That’s a wrap!

If you enjoyed this breakdown, follow for more. I publish new paper explanations most weekdays.

More papers in this series, organized by lab and topic, are in the start here guide.

What paper should I cover next? Let me know in the responses.

View original.

Exported from Medium on August 22, 2026.
