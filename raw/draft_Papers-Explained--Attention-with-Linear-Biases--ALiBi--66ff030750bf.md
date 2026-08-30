# Papers Explained: Attention with Linear Biases (ALiBi)

Papers Explained: Attention with Linear Biases (ALiBi)

Papers Explained: Attention with Linear Biases (ALiBi)

Attention with Linear Biases (ALiBi) is a position representation method for transformers that enables efficient and effective…

Papers Explained: Attention with Linear Biases (ALiBi)

Attention with Linear Biases (ALiBi) is a position representation method for transformers that enables efficient and effective extrapolation to longer input sequences. Unlike traditional positional embeddings, ALiBi directly biases query-key attention scores with a linearly increasing penalty based on their distance, requiring no additional runtime or parameters and incurring negligible memory overhead.

Method

In the transformer model position embeddings are added to the word embeddings at the bottom of the network. For an input subsequence of length L, the attention sublayer computes the attention scores for the ith query Q in each head, given the first i keys K:
softmax(QK’)
These attention scores are then multiplied by the values to return the output of the attention sublayer.

When using ALiBi, position embeddings are not added at any point in the network. The only modification applied is after the query-key dot product, where a static, non-learned bias is added:
softmax(QK’ + m·[−(i − 1), …, −2, −1, 0])
where scalar m is a head-specific slope fixed before training.

For models with 8 heads, the slopes used are the geometric sequence: 1/2¹, 1/2², …, 1/2⁸. For models that require 16 heads, those 8 slopes are interpolated by geometrically averaging every consecutive pair, resulting in the geometric sequence that starts at 1/√2 and has the ratio of 1/√2: 1/2^(0.5), 1/2¹, 1/2^(1.5), 1/2², …, 1/2⁸. In general, for n heads, the set of slopes is the geometric sequence that starts at 1/2^(8/n) and uses that same value as its ratio.

This set of slopes works on a wide variety of text domains and model sizes. Therefore, it is not necessary to tune these slope values every time a new model is trained on a new dataset. This approach is similar to the sinusoidal method, where the hyperparameters (the start and end of the geometric progression of wavelengths) were set once and then reused in different models of different sizes on different datasets.

ALiBi has an inductive bias towards recency; it penalizes attention scores between distant query-key pairs, with the penalty increasing as the distance between a key and a query grows. The different heads increase their penalties at different rates, depending on the slope magnitude.

Initial experiments with making the slopes trainable did not yield strong extrapolation results and also slowed down the training speed by 3%. A brief manual exploration of around ten slope sets led to the discovery of the set of slopes that was ultimately selected. The main insight from this exploration is that the slope sets that work best are those with slopes in the (0, 1) range, with the slopes’ density increasing as they get closer to 0. The method was also found to be robust to slope choice, as even randomly sampling from the exponential distribution worked well in some cases, although that method had high variance.

Evaluation

ALibi is validated on WikiText-103 corpus, and then applied with identical hyperparameters to the Toronto BookCorpus as a cross-domain test, and finally scaled up to a 1.3B parameter model trained on a large (461GB) CC100+RoBERTa corpus.
Perplexity when ALiBi extrapolates on the WikiText-103 development set.
ALiBi outperforms the sinusoidal embedding baseline on WikiText-103 across all training subsequence lengths, sometimes by significant margins (17.60 vs. 18.67 perplexity for L=3072)
ALiBi models exhibit strong extrapolation: models trained with short sequences (e.g. L=512) outperform sinusoidal models trained with much longer sequences (L=3072) when evaluated on long sequences (512-to-3072 tokens).
Test perplexity and runtime on WikiText-103.Valid and test perplexity scores on WikiText-103 with sliding window evaluation.
ALiBi’s good extrapolation extends beyond 3x the training sequence length (L); performance only gradually degrades as sequence length increases, unlike baselines where performance falls off rapidly.
ALiBi models extrapolating on the Toronto BookCorpus development set.Validation and test perplexities on the Toronto Book Corpus dataset.Validation and test perplexities on the Toronto Book Corpus dataset with a sliding window.
Results transfer robustly to books data without adjusting hyperparameters, and ALiBi continues to outperform the sinusoidal baseline in both in-domain and extrapolation settings.
Perplexity, memory, and train time on the CC100+RoBERTa corpus.Perplexity, train time and memory use on the CC100+RoBERTa corpus.
In large-scale experiments (1.3B parameters, 461GB dataset), ALiBi matches or very slightly trails sinusoidal (0.06 perplexity difference) when comparing same training sequence lengths, but achieves faster training (7%-11% speedup), significantly reduces memory use (up to 3.1GB less RAM), and can outperform the sinusoidal baseline when evaluated on longer sequence.
Sinusoidal baselines cannot extrapolate at all; their performance drops as soon as evaluation sequence exceeds training sequence

Paper

Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation 2108.12409

That’s a wrap!

If you enjoyed this breakdown, follow for more. I publish new paper explanations most weekdays.

More papers in this series, organized by lab and topic, are in the start here guide.

What paper should I cover next? Let me know in the responses.

View original.

Exported from Medium on August 22, 2026.
