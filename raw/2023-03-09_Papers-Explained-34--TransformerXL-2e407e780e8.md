# Papers Explained 34: TransformerXL

Papers Explained 34: TransformerXL

Papers Explained 34: TransformerXL

The Transformer XL architecture is an extension of the original Transformer model for sequence-to-sequence tasks such as machine…

Papers Explained 34: TransformerXL

The Transformer XL architecture is an extension of the original Transformer model for sequence-to-sequence tasks such as machine translation. The main difference between the two models is that Transformer XL is designed to handle longer sequences of text by introducing recurrence into the self-attention mechanism.

The basic building blocks of Transformer XL are the same as in the original Transformer model. It consists of a stack of identical encoder and decoder layers, each of which includes multi-head self-attention and feedforward layers.

Recurrence Mechanism

In Transformer XL, the self-attention mechanism is modified to include a recurrence mechanism that allows the model to handle sequences longer than the maximum sequence length used during training.

The recurrence mechanism in Transformer XL is based on a technique called “segment-level recurrence”. In this technique, the input sequence is split into segments of a fixed length, and the hidden state of each segment is passed on to the next segment. This allows the self-attention mechanism to attend to previous segments of the input sequence, effectively extending the receptive field of the model.

In addition to the segment-level recurrence mechanism, Transformer XL also includes a number of other techniques for handling longer sequences, including relative positional encoding, adaptive input embeddings, and a modified training procedure that encourages the model to learn to predict future tokens in the sequence.

Relative positional embeddings

Relative positional embeddings capture the relative position of a token to other tokens in the same segment, rather than its absolute position in the entire sequence. This allows the model to generalize better to longer sequences and helps avoid overfitting to specific positions in the input sequence.

Adaptive input embeddings

Adaptive input embeddings allow the model to dynamically adjust the size of the embedding matrix based on the input sequence length. This helps to reduce the memory footprint of the model and improves its ability to handle longer input sequences.

Modified training objective

The authors propose a new training objective called “targeted cased perplexity”, which encourages the model to generate more accurate predictions for rare and difficult words in the input sequence. This helps to improve the model’s overall performance on language modeling tasks, particularly on challenging datasets that contain many rare or out-of-vocabulary words.

Evaluation

The Transformer XL model has been evaluated for its ability to generate high-quality text by predicting the next word in the sequence given the previous context, on the following datasets. The model’s performance is typically evaluated using perplexity, a measure of how well the model can predict the next word in the sequence. The Transformer XL model has been shown to outperform existing state-of-the-art models on all of these datasets, demonstrating its effectiveness for a wide range of language modeling tasks:

WikiText-103: This is a large language modeling dataset based on articles from Wikipedia. The dataset contains over 100 million tokens, making it a challenging benchmark for language modeling models.
Text8: This is a smaller language modeling dataset that contains a cleaned version of a subset of Wikipedia. The dataset contains 100 million characters, and is often used as a benchmark for smaller-scale language modeling tasks.
enwik8: This is a larger dataset than Text8, containing 100 million characters from Wikipedia. It is often used as a benchmark for evaluating language modeling models that can handle longer contexts.
One Billion Word: This is a dataset that contains approximately 1 billion words from web pages. It is a popular benchmark for evaluating large-scale language modeling models.
Penn Treebank: This is a widely used benchmark dataset for evaluating language modeling models. It contains over 4 million words from newspaper articles, and is often used as a benchmark for evaluating the performance of language models on tasks such as sentence completion and text generation.

Paper

Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context 1901.02860

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on March 9, 2023.

Canonical link

Exported from Medium on May 4, 2026.
