# Papers Explained: Position Encodings in Transformers

Papers Explained: Position Encodings in Transformers

Papers Explained: Position Encodings in Transformers

Since all tokens in a sequence are processed in parallel by the Transformer, the model has no inherent information about their positions or…

Papers Explained: Position Encodings in Transformers

Since all tokens in a sequence are processed in parallel by the Transformer, the model has no inherent information about their positions or the order in which they appear. Therefore, positional information needs to be explicitly incorporated into the input.

The Transformer does this by adding a positional vector to each token embedding. These vectors follow a structured pattern that allows the model to infer the position of each token as well as the relative distance between tokens in the sequence. By combining positional information with the token embeddings, the resulting representations retain information about word order, which can then influence the Q/K/V projections and the dot-product attention mechanism.

Sinusoidal Positional Encoding

The encoding proposed in the original transformers paper is a simple technique. It’s a d -dimensional vector that contains information about a specific position in a sentence. For a position pos and vector dimension index i:

Each dimension of the positional encoding corresponds to a sinusoid of different wavelengths ranging from 2π to 10000⋅2π These wavelengths form a geometric progression, where lower dimensions capture fine-grained positional differences, while higher dimensions capture long-range patterns.
The 128-dimensional positonal encoding for a sentence with the maximum lenght of 50.
You can observe the rate at which each bit changes: the LSB toggles with every number, the next bit changes every two numbers, the third every four numbers, and so on, similar to binary representation of numbers.
import torch
import torch.nn as nn

class SinusoidalPositionalEncoding(nn.Module):
    def __init__(self, d_model: int, max_len: int = 5000):
        super().__init__()
        
        # Create a matrix of shape (max_len, d_model)
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        
        # Compute division term in log space for numerical stability: 10000^(2i/d_model)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-torch.log(torch.tensor(10000.0)) / d_model))
        
        # Apply sine to even indices; cosine to odd indices
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        
        # Add batch dimension: shape (1, max_len, d_model)
        pe = pe.unsqueeze(0)
        self.register_buffer('pe', pe)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # x shape: (batch_size, seq_len, d_model)
        return x + self.pe[:, :x.size(1)]
Learned (Absolute) Positional Encoding

Unlike sinusoidal encodings (which use fixed mathematical sine/cosine functions), Absolute Learned Positional Embeddings treat each position index (0,1,2,…,N−1) as a discrete key in a trainable lookup table.

For a token sequence of length T:

Create a sequence of position indices p=[0,1,2,…,T−1].
Look up the corresponding learnable position vectors: Epos
Add the positional embedding to the semantic token embedding before passing into the Transformer layers: H0 =Etoken + Epos​

Furthermore this encoding can be learned differently per layer.
import torch
import torch.nn as nn

class AbsoluteLearnedPositionalEmbedding(nn.Module):
    def __init__(self, max_seq_len: int, d_model: int):
        super().__init__()
        # Trainable lookup table for positions 0 to max_seq_len - 1
        self.pos_embedding = nn.Embedding(max_seq_len, d_model)
        
    def forward(self, token_embeddings: torch.Tensor) -> torch.Tensor:
        # token_embeddings shape: (batch_size, seq_len, d_model)
        seq_len = token_embeddings.size(1)
        
        # Create position indices: [0, 1, 2, ..., seq_len - 1]
        positions = torch.arange(seq_len, device=token_embeddings.device).unsqueeze(0)
        
        # Retrieve position embeddings: shape (1, seq_len, d_model)
        pos_embeds = self.pos_embedding(positions)
        
        # Element-wise addition of token and positional embeddings
        return token_embeddings + pos_embeds
Key LLMs:

BERT, RoBERTa
GPT-1, GPT-2, GPT-3
OPT (Meta)
BART

Relative Positional Encoding

This presents an alternative approach, extending the self-attention mechanism to efficiently consider representations of the relative positions, or distances between sequence elements.

In this sense, the input is modeled as a labeled, directed, fully-connected graph. The edge between input elements xi and xj is represented by vectors aV_ij, aK_ij.

The raw attention logit eij​ between query position i and key position j is modified by adding the relative key vector aK_ij​:

Expanding this dot product yields two distinct terms:

Term 1 (Semantic Match): Asks: “Does token j’s meaning match what I am looking for?”
Term 2 (Positional Preference): Asks: “Given the kind of word I am (qi​), how much do I care about a token sitting at distance offset (j−i)?”

The output representation zi​ adds the relative value vector aV_ij​:

Two learnable position tables are introduced for relative keys and relative values. Rather than learning separate relative position vectors for every possible distance in a long sequence, relative distances are clipped to a maximum absolute threshold k. This constrains the model to exactly 2k+1 unique relative edge representations:

For query position i and key/value position j:
import torch
import torch.nn as nn
import math

class NaiveShawRelativeSelfAttention(nn.Module):
    def __init__(self, d_model: int, num_heads: int, max_relative_position: int = 16):
        super().__init__()
        self.d_model = d_model
        self.num_heads = num_heads
        self.d_k = d_model // num_heads
        self.k = max_relative_position
        
        self.w_q = nn.Linear(d_model, d_model)
        self.w_k = nn.Linear(d_model, d_model)
        self.w_v = nn.Linear(d_model, d_model)
        self.w_o = nn.Linear(d_model, d_model)
        
        # Relative position lookup table for Keys: (2k + 1, d_k)
        self.rel_embedding_k = nn.Embedding(2 * self.k + 1, self.d_k)
        
    def _relative_position_matrix(self, seq_len: int, device: torch.device) -> torch.Tensor:
        # Generate matrix of relative offsets (j - i)
        range_vec = torch.arange(seq_len, device=device)
        distance_mat = range_vec[None, :] - range_vec[:, None] # shape: (seq_len, seq_len)
        
        # Clip relative distances to [-k, k] and shift to index range [0, 2k]
        clipped_mat = torch.clamp(distance_mat, -self.k, self.k)
        return clipped_mat + self.k

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        b_size, seq_len, _ = x.shape
        
        # 1. Standard projection of Q, K, V -> (B, H, T, d_k)
        q = self.w_q(x).view(b_size, seq_len, self.num_heads, self.d_k).transpose(1, 2)
        k = self.w_k(x).view(b_size, seq_len, self.num_heads, self.d_k).transpose(1, 2)
        v = self.w_v(x).view(b_size, seq_len, self.num_heads, self.d_k).transpose(1, 2)
        
        # 2. Lookup relative key embeddings a_k -> Shape: (T, T, d_k)
        rel_indices = self._relative_position_matrix(seq_len, x.device)
        a_k = self.rel_embedding_k(rel_indices) # a_k[i, j] is the relative key vector for (i, j)
        
        # 3. DIRECT NAIVE ADDITION: (x_j * W^K + a_ij^K)
        # Expand content keys k to shape (B, H, 1, T, d_k)
        k_content_expanded = k.unsqueeze(2) 
        
        # Expand relative position keys a_k to shape (1, 1, T, T, d_k)
        a_k_expanded = a_k.unsqueeze(0).unsqueeze(0)
        
        # Add relative key embeddings directly to content key vectors!
        # K_total[b, h, i, j] = k[b, h, j] + a_k[i, j]  --> Shape: (B, H, T, T, d_k)
        k_total = k_content_expanded + a_k_expanded
        
        # 4. DIRECT NAIVE DOT PRODUCT: q_i * (K_total_ij)^T
        # Expand q to shape (B, H, T, 1, d_k)
        q_expanded = q.unsqueeze(3)
        
        # Compute dot product along the d_k dimension
        # (B, H, T, 1, d_k) * (B, H, T, T, d_k) -> sum over d_k -> (B, H, T, T)
        logits = (q_expanded * k_total).sum(dim=-1) / math.sqrt(self.d_k)
        
        # 5. Softmax & Value Aggregation
        attn_weights = torch.softmax(logits, dim=-1)
        out = torch.matmul(attn_weights, v)
        out = out.transpose(1, 2).contiguous().view(b_size, seq_len, self.d_model)
        
        return self.w_o(out)
Naively storing pairwise relative position vectors for every batch b, head h, and token pair (i,j) requires O(b⋅h⋅n^2⋅d_z) memory. This breaks standard fast GPU matrix multiplication (QK⊤).

The Solution:

Sharing Parameters Across Heads: Relative position embeddings wK and wV are shared across all attention heads within a layer, reducing memory overhead to O(n2⋅dz).
Tensor Reshaping & Computation Splitting: Split eijinto T1+T2:

T1​=xi ​WQ (xj ​WK)⊤: Computed via standard batch matrix multiplication ([b,h,n,dz]×[b,h,dz,n]→[b,h,n,n]).
T2​=xi​ WQ (aK_ij​)⊤: Reshape xWQ to [n,b⋅h,dz] and multiply by the relative lookup table [dz,2k+1], then perform a tensor gather/shift to map relative distances to [b,h,n,n].
import torch
import torch.nn as nn
import math

class ShawRelativeSelfAttention(nn.Module):
    def __init__(self, d_model: int, num_heads: int, max_relative_position: int = 16):
        super().__init__()
        self.d_model = d_model
        self.num_heads = num_heads
        self.d_k = d_model // num_heads
        self.k = max_relative_position
        
        self.w_q = nn.Linear(d_model, d_model)
        self.w_k = nn.Linear(d_model, d_model)
        self.w_v = nn.Linear(d_model, d_model)
        self.w_o = nn.Linear(d_model, d_model)
        
        # Relative position lookup table for Keys: 2k + 1 vectors of size d_k
        self.rel_embedding_k = nn.Embedding(2 * self.k + 1, self.d_k)
        
    def _relative_position_matrix(self, seq_len: int, device: torch.device) -> torch.Tensor:
        # Generate matrix of relative offsets (j - i)
        range_vec = torch.arange(seq_len, device=device)
        distance_mat = range_vec[None, :] - range_vec[:, None] # shape: (seq_len, seq_len)
        
        # Clip relative distances to [-k, k] and shift to index range [0, 2k]
        clipped_mat = torch.clamp(distance_mat, -self.k, self.k)
        return clipped_mat + self.k

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        b_size, seq_len, _ = x.shape
        
        # Project Q, K, V
        q = self.w_q(x).view(b_size, seq_len, self.num_heads, self.d_k).transpose(1, 2) # (B, H, T, d_k)
        k = self.w_k(x).view(b_size, seq_len, self.num_heads, self.d_k).transpose(1, 2) # (B, H, T, d_k)
        v = self.w_v(x).view(b_size, seq_len, self.num_heads, self.d_k).transpose(1, 2) # (B, H, T, d_k)
        
        # 1. Content-to-content term: Q * K^T -> (B, H, T, T)
        content_logits = torch.matmul(q, k.transpose(-2, -1))
        
        # 2. Content-to-relative-position term: Q * (a^K)^T
        rel_indices = self._relative_position_matrix(seq_len, x.device) # (T, T)
        rel_keys = self.rel_embedding_k(rel_indices)                     # (T, T, d_k)
        
        # Efficient tensor multiplication for relative position logits
        # Reshape q to (T, B * H, d_k) and multiply by rel_keys (T, d_k, T)
        q_trans = q.permute(2, 0, 1, 3).contiguous().view(seq_len, b_size * self.num_heads, self.d_k)
        rel_logits = torch.matmul(q_trans, rel_keys.transpose(-2, -1)) # (T, B*H, T)
        rel_logits = rel_logits.view(seq_len, b_size, self.num_heads, seq_len).permute(1, 2, 0, 3) # (B, H, T, T)
        
        # Total attention logits
        logits = (content_logits + rel_logits) / math.sqrt(self.d_k)
        attn_weights = torch.softmax(logits, dim=-1)
        
        # Output aggregation
        out = torch.matmul(attn_weights, v) # (B, H, T, d_k)
        out = out.transpose(1, 2).contiguous().view(b_size, seq_len, self.d_model)
        return self.w_o(out)
Key LLMs:

T5 simplified this by turning aK_i,j into a learned scalar relative bias added directly to the attention logits matrix, using a logarithmic clipping/bucketing function for distance ∣i−j∣.
Transformer-XL adapted this formulation to work across cached segment memories, allowing attention to span infinitely across chunk boundaries without losing relative distance context.

References

Sinusoidal Positional Encoding: Attention Is All You Need 1706.03762
Learned (Absolute) Positional Encoding: Convolutional Sequence to Sequence Learning 1705.03122
Relative Positional Encoding: Self-Attention with Relative Position Representations 1803.02155

That’s a wrap!

If you enjoyed this breakdown, follow for more. I publish new paper explanations most weekdays.

More papers in this series, organized by lab and topic, are in the start here guide.

What paper should I cover next? Let me know in the responses.

View original.

Exported from Medium on August 22, 2026.
