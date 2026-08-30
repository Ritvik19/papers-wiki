# Papers Explained 01: Transformer

Papers Explained 01: Transformer

Papers Explained 01: Transformer

Most competitive neural sequence transduction models have an encoder-decoder structure. Here, the encoder maps an input sequence of symbol…

Papers Explained 01: Transformer

Most competitive neural sequence transduction models have an encoder-decoder structure. Here, the encoder maps an input sequence of symbol representations (x1, …, xn) to a sequence of continuous representations z = (z1, …, zn). Given z, the decoder then generates an output sequence (y1, …, ym) of symbols one element at a time. At each step the model is auto-regressive, consuming the previously generated symbols as additional input when generating the next.

The Transformer follows this overall architecture using stacked self-attention and point-wise, fully connected layers for both the encoder and decoder,

Encoder

The encoder is composed of a stack of N = 6 identical layers. Each layer has two sub-layers. The first is a multi-head self-attention mechanism, and the second is a simple, positionwise fully connected feed-forward network. A residual connection is employed around each of the two sub-layers, followed by layer normalization.

That is, the output of each sub-layer is

where Sublayer(x) is the function implemented by the sub-layer itself.

To facilitate these residual connections, all sub-layers in the model, as well as the embedding layers, produce outputs of dimension d_model = 512.

Decoder

The decoder is also composed of a stack of N = 6 identical layers. In addition to the two sub-layers in each encoder layer, the decoder inserts a third sub-layer, which performs multi-head attention over the output of the encoder stack.

The self-attention sub-layer in the decoder stack is also modified to prevent positions from attending to subsequent positions. This masking, combined with fact that the output embeddings are offset by one position, ensures that the predictions for position i can depend only on the known outputs at positions less than i.

Attention

An attention function can be described as mapping a query and a set of key-value pairs to an output, where the query, keys, values, and output are all vectors. The output is computed as a weighted sum of the values, where the weight assigned to each value is computed by a compatibility function of the query with the corresponding key.

Multi-Head Attention

Instead of performing a single attention function with dmodel-dimensional keys, values and queries, it is beneficial to linearly project the queries, keys and values h times with different, learned linear projections to dk, dk and dv dimensions, respectively.

On each of these projected versions of queries, keys and values the attention function is performed in parallel, yielding dv-dimensional output values. These are concatenated and once again projected, resulting in the final values,

Multi-head attention allows the model to jointly attend to information from different representation subspaces at different positions. With a single attention head, averaging inhibits this.

where

Embeddings

Similarly to other sequence transduction models, Transformers also use learned embeddings to convert the input tokens and output tokens to vectors of dimension d_model.

Positional Encoding

Since transformer model contains no recurrence and no convolution, in order for the model to make use of the order of the sequence, some information about the relative or absolute position of the tokens must be injected in the sequence.

Hence positional encodings are added to the input embeddings at the
bottoms of the encoder and decoder stacks. The positional encodings have the same dimension d_model as the embeddings, so that the two can be summed

Training Data

The transformer is trained on the standard WMT 2014 English-German dataset consisting of about 4.5 million sentence pairs. Sentences were encoded using byte-pair encoding, which has a shared sourcetarget vocabulary of about 37000 tokens.

For English-French, the significantly larger WMT 2014 English-French dataset consisting of 36M sentences is used and split tokens into a 32000 word-piece vocabulary.

Paper

Attention Is All You Need 1706.03762

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on February 6, 2023.

Canonical link

Exported from Medium on May 4, 2026.
