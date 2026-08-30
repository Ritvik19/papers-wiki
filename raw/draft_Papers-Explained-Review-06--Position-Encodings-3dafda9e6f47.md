# Papers Explained Review 06: Position Encodings

Papers Explained Review 06: Position Encodings

Papers Explained Review 06: Position Encodings

Table of Contents

Papers Explained Review 06: Position Encodings

Table of Contents

Absolute Position Encodings (2017)
Relative Position Encodings (2018)
Rotary Embeddings (2021)
Attention with Linear Biases (2021)

Absolute Position Encodings

Unlike traditional neural networks that utilise recurrence or convolution to process sequential data, transformers lack an inherent mechanism to recognize the order of input sequences. To address this limitation, absolute positional encodings were introduced to.

Positional encodings are added directly to the input embeddings at the initial layers of both the encoder and decoder stacks within a transformer model. These encodings share the same dimensionality, as the input embeddings, allowing for a straightforward element-wise summation.

The formulation of positional encodings can vary, encompassing both learned and fixed strategies. In the original transformer implementation, sine and cosine functions of different frequencies are employed to generate fixed positional encodings. 

This approach creates a unique positional encoding for each token, with the wavelengths of these sinusoidal functions forming a geometric progression. 

Sinusoidal positional encodings were preferred over learned embeddings due to the potential for the model to generalize to sequence lengths beyond those encountered during training. 

Back to Top

Relative Position Encodings

Traditional absolute positional encodings have limitations, notably their fixed maximum sequence length, which restricts the model’s ability to process longer sequences. This challenge is addressed by relative positional encodings, which focus on the pairwise distances between tokens, allowing for the processing of sequences of arbitrary length.

Introduced in Self-Attention with Relative Position Representations, relative positional encodings add a new dimension to self-attention mechanisms by incorporating the relative distances between tokens into the model. This is achieved through modifications to the self-attention equations, where relative positional information is integrated into both the keys and values matrices.

First, relative positional information is supplied to the model as an additional component to the keys.

The softmax operation remains unchanged from vanilla self-attention.

Lastly, relative positional information is supplied again as a sub-component of the values matrix.

This approach enables the model to understand the context based on the relative positions of tokens, rather than their absolute positions in the sequence.

However, the original method proposed in Self-Attention with Relative Position Representations for calculating relative positional encodings was memory-intensive, scaling with the square of the sequence length (O(L²D)). To address this, Music Transformer introduced an efficient computation method through a skewing operation, focusing on optimizing the encoding process for the keys component and omitting the additional relative positional embedding for the value term.

Specifically, S_rel in the music transformer paper is simply

This significantly reduces the computational complexity and memory requirements, making it more feasible for processing long sequences.

Back to Top

Rotary Embeddings
Implementation of Rotary Position Embedding(RoPE).
Unlike traditional position embeddings that add position information directly to token embeddings, RoPE incorporates position by rotating the embedding vectors in a high-dimensional space. This method is grounded in the geometric properties of vectors and complex numbers, offering a unique way to integrate relative position information multiplicatively.

In the simplest 2D case, the essence of RoPE can be captured by considering a vector (x_m) in a two-dimensional space. The position embedding for a query vector (q) and a key vector (k) can be represented as:

where (W_q) and (W_k) are the weight matrices for the query and key, respectively, (m) and (n) are the position indices, and (theta) is a constant angle. The interaction between these position-encoded vectors is captured by the real part of their complex product, emphasizing the relative position through rotation by an angle proportional to the position indices.

To extend this concept to higher dimensions where (d) is even, the space is divided into (d/2) sub-spaces. Each sub-space undergoes a similar rotation, described by the rotary matrix (R^d_{Theta,m}), which is a block diagonal matrix with 2x2 rotation matrices as its blocks. The rotation angles (theta_i) are predefined, creating a structured way to encode positions across multiple dimensions.

The general form of the RoPE transformation is given by: 

This transformation is applied to both query and key vectors in the self-attention mechanism, enabling the model to understand relative positions through the geometric relationship of rotated vectors. RoPE’s multiplicative nature and its reliance on rotation matrices distinguish it from additive position embeddings, offering a potentially more stable and interpretable method for encoding sequence positions.

Back to Top

Attention with Linear Biases

In the ALiBi method, instead of incorporating position embeddings at any layer, a static, non-learned bias is added to the attention mechanism. Specifically, after computing the dot product between queries and keys within the attention sublayer, a head-specific bias is introduced. This bias is a simple linear function of the distance between the positions of the query and the key, effectively modifying the attention scores based on the relative positions of tokens.

The bias is defined by a scalar (m), which represents a slope that is fixed before training begins. For a model with multiple attention heads, each head is assigned a unique slope, creating a set of slopes that follow a geometric sequence. This design choice allows different heads to specialize in capturing relationships over varying distances, with some heads focusing on nearby tokens and others on more distant ones.

ALiBi’s approach is grounded in the observation that certain geometric sequences of slopes, particularly those in the range (0, 1), yield the most effective results across a wide array of text domains and model sizes. This finding suggests that the specific values of these slopes do not require fine-tuning for each new dataset or model configuration, offering a more generalizable and efficient solution for incorporating positional information.

By penalizing the attention scores for distant query-key pairs more heavily, ALiBi inherently biases the model towards prioritizing more recent information. This inductive bias towards recency is adjustable across different heads by varying the slope magnitudes, allowing the model to dynamically adapt its focus based on the relative positions of tokens within the sequence.

Back to Top

References

Attention Is All You Need
Self-Attention with Relative Position Representations
Music Transformer
RoFormer: Enhanced Transformer with Rotary Position Embedding
Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

View original.

Exported from Medium on May 4, 2026.
