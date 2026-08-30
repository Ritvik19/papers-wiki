# Papers Explained 159: XLM Roberta

Papers Explained 159: XLM Roberta

Papers Explained 159: XLM Roberta

XLM-RoBERTa combines RoBERTa techniques with XLM, excluding translation language modelling. Instead, it focuses on masked language…

Papers Explained 159: XLM Roberta

XLM-RoBERTa combines RoBERTa techniques with XLM, excluding translation language modelling. Instead, it focuses on masked language modelling in sentences from a single language. The model is trained on a vast array of languages (100) and possesses the ability to identify the input language without relying on language embeddings.

Model

A Transformer model is trained with the multilingual masked language modeling (MLM) objective using only monolingual data. Streams of text are sampled from each language, and the model is trained to predict the masked tokens in the input. Subword tokenization is applied directly on raw text data using SentencePiece.

A large vocabulary size of 250,000 is used with a full softmax, and two different models are trained.: XLM-R Base (L = 12, H = 768, A = 12, 270M params) and XLM-R (L = 24, H = 1024, A = 16, 550M params).

Data
Languages and statistics of the CC-100 corpus
Paper

Unsupervised Cross-lingual Representation Learning at Scale 1911.02116

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on July 5, 2024.

Canonical link

Exported from Medium on May 4, 2026.
