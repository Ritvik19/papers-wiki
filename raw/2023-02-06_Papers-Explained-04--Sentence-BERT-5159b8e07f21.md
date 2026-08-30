# Papers Explained 04: Sentence BERT

Papers Explained 04: Sentence BERT

Papers Explained 04: Sentence BERT

BERT and RoBERTa require that both sentences are fed into the network, which causes a massive computational overhead: Finding the most…

Papers Explained 04: Sentence BERT

BERT and RoBERTa require that both sentences are fed into the network, which causes a massive computational overhead: Finding the most similar pair in a collection of 10,000 sentences requires about 50 million inference computations (~65 hours) with BERT. The construction of BERT makes it unsuitable for semantic similarity search as well as for unsupervised tasks like clustering.

Sentence-BERT (SBERT), presents a modification of the pretrained BERT network that use siamese and triplet network structures to derive semantically meaningful sentence embeddings that can be compared using cosine-similarity. This reduces the effort for finding the most similar pair from 65 hours with BERT / RoBERTa to about 5 seconds with SBERT, while maintaining the accuracy from BERT.

Architecture

SBERT adds a pooling operation to the output of BERT / RoBERTa to derive a fixed sized sentence embedding. Three pooling strategies are experimented:

Using the output of the CLS-token
Computing the mean of all output vectors (MEAN-strategy)
Computing a max-over-time of the output vectors (MAX-strategy).

The default configuration is MEAN

In order to fine-tune BERT / RoBERTa, siamese and triplet networksare created to update the weights such that the produced sentence embeddings are semantically meaningful and can be compared with cosine-similarity.

Classification Objective Function

The sentence embeddings u and v are concatenated with the element-wise difference |u−v| and multiplied with the trainable weight Wt and Cross-entropy loss is optimized:

Regression Objective Function

The cosine similarity between the two sentence embeddings u and v is computed and mean squared-error loss is used as the objective function.

Triplet Objective Function

Given an anchor sentence a, a positive sentence p, and a negative sentence n, triplet loss tunes the network such that the distance between a and p is smaller than the distance between a and n.

Mathematically, we minimize the following loss function:

Training and Evaluation

SBERT is trained on the combination of the SNLI and the Multi-Genre NLI dataset. The SNLI is a collection of 570,000 sentence pairs annotated with the labels contradiction, eintailment, and neutral. MultiNLI contains 430,000 sentence pairs and covers a range of genres of spoken and written text.

The performance of SBERT is evaluated for common Semantic Textual Similarity (STS) tasks.

Cosine-similarity is used to compare the similarity between two sentence embeddings.

Paper

Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks 1908.10084

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on February 6, 2023.

Canonical link

Exported from Medium on May 4, 2026.
