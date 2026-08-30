# Papers Explained: Rotary Position Embedding(RoPE)

Papers Explained: Rotary Position Embedding(RoPE)

Papers Explained: Rotary Position Embedding(RoPE)

Rotary Position Embedding (RoPE) encodes the absolute position with a rotation matrix and meanwhile incorporates the explicit relative…

Papers Explained: Rotary Position Embedding(RoPE)

Rotary Position Embedding (RoPE) encodes the absolute position with a rotation matrix and meanwhile incorporates the explicit relative position dependency in self-attention formulation. It enables flexibility of sequence length, decaying inter-token dependency with increasing relative distances, and the capability of equipping the linear self-attention with relative position encoding.

Formulation

Attention and Position Encodings

Let S_N be a sequence of N input tokens with wi being the ith element with xi, the d-dimensional word embedding vector of token wi without position information. The self-attention first incorporates position information to the word embeddings and transforms them into queries, keys, and value representations.
Equation 1
where qm, kn and vn incorporate the mth and nth positions through fq , fk and fv , respectively. The query and key values are then used to compute the attention weights, while the output is computed as the weighted sum over the value representation.

The existing approaches of transformer-based position encoding mainly focus on choosing a suitable function to form EQN 1.

A typical choice of EQN 1 is adding a vector depending of the position of token xi:

The original transformer proposed to generate pi using the sinusoidal function:

whereas a lot of llms use a set of trainable vectors.

Instead of directly adding the position to the context representation, RoPE proposes to incorporate the relative position information by multiplying with the sinusoidal functions.

Rotary Position Embedding

Transformer-based language modeling usually leverages the position information of individual tokens through a self-attention mechanism. In order to incorporate relative position information, the inner product of query qm and key kn is required to be formulated by a function g, which takes only the word embeddings xm, xn, and their relative position m − n as input variables.

The central idea is: Instead of adding a positional vector to a token embedding, rotate the query and key vectors by an angle determined by their positions.
Implementation of Rotary Position Embedding.
A 2D case

Consider a simple case with a dimension d = 2. Under these settings, the geometric property of vectors on a 2D plane and its complex form is used to prove that a solution to the above equation is:

Think of this as two operations:

Normal query projection:
x_m​→W_q​ . x_m​
This is exactly what a normal Transformer does.

Rotate it according to position:
W_q​ . x_m→(W_q​ . x_m) . e^(imθ)
Exactly the same thing is done for the key

Calculate the attention score: The complex analogue of the dot product is not qk. Instead, it’s q∗k​, where q∗ is the complex conjugate.
Let q = q1 + iq2 and k = k1 + ik2We have q∗ = q1 − iq2Therefore: q∗k = (q1 − iq2)(k1 + ik2).Expanding: q∗k = q1.​k1 ​+ q2.k2 + i(q1.​k2 ​− q2.​k1​)Look at the real part: Re(q∗k) = q1.​k1 ​+ q2. ​k2 ​= qTk​​Therefore: g = Re[(W_q​ . x_m​).(W_k . ​x_n​)∗ e^i(m−n)θ]
θ ∈ R is a preset non-zero constant. 

The attention score thus depends on (m−n) rather than separately on m and n.

f{q,k} can be further written in a multiplication matrix:
Equation 13.
The standard 2D rotation matrix is:

Therefore Equation 13 is essentially:

Similarly, g can be viewed as a matrix and thus enables the solution of formulation under the 2D case. Specifically, incorporating the relative position embedding is straightforward: simply rotate the affine transformed word embedding vector by amount of angle multiples of its position index and thus interprets the intuition behind Rotary Position Embedding.

General Form

In order to generalize the results from 2D to any even d, the d-dimensional subspace is divided into d/2 2D subspaces , calculate its contribution to the dot product, and then add all those contributions together.

where θi​=10000−2(i−1)/d.

This means θ1​,θ2​,θ3​,… are progressively smaller. The different θi’s play a role somewhat similar to different bits in a binary representation: they give different dimensions different positional “resolutions.”

Now the attention score computation becomes:

Evaluation

The proposed RoFormer (incorporating Rotary Position Embedding, RoPE) is compared to standard Transformers.

Evaluation is conducted on machine translation (WMT 2014 English-German), language modeling (using BookCorpus, Wikipedia, and Enwik8 datasets), and standard NLP downstream tasks from the GLUE benchmark.
WMT 2014 English-to-German translation task.
RoFormer achieves better BLEU scores than the baseline Transformer on WMT 2014 English-German, showing effectiveness for sequence-to-sequence task.
Evaluation of RoPE in language modeling pre-training.
RoFormer converges faster during pre-training compared to BERT, as shown by lower MLM loss.
Comparing RoFormer and BERT by fine tuning on downstream GLEU tasks.
RoFormer outperforms BERT significantly on three out of six GLUE datasets, proving strong generalization.

Paper

RoFormer: Enhanced Transformer with Rotary Position Embedding 2104.09864

That’s a wrap!

If you enjoyed this breakdown, follow for more. I publish new paper explanations most weekdays.

More papers in this series, organized by lab and topic, are in the start here guide.

What paper should I cover next? Let me know in the responses.

View original.

Exported from Medium on August 22, 2026.
