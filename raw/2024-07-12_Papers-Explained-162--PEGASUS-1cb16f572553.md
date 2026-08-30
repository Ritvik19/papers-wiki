# Papers Explained 162: PEGASUS

Papers Explained 162: PEGASUS

Papers Explained 162: PEGASUS

PEGASUS (Pre-training with Extracted Gap-sentences for Abstractive SUmmarization Sequence-to-sequence models) utilizes the same…

Papers Explained 162: PEGASUS

PEGASUS (Pre-training with Extracted Gap-sentences for Abstractive SUmmarization Sequence-to-sequence models) utilizes the same encoder-decoder model architecture as BART. For pre-training, it employs two self-supervised objectives: Masked Language Modeling (MLM) and Gap Sentence Generation (GSG) for summarization.
The base architecture of PEGASUS is a standard Transformer encoder-decoder. Both GSG and MLM are applied simultaneously to this example as pre-training objectives. Originally there are three sentences. One sentence is masked with [MASK1] and used as target generation text (GSG). The other two sentences remain in the input, but some tokens are randomly masked by [MASK2] (MLM).
Gap Sentences Generation (GSG)

It is hypothesized that the use of a pre-training objective that more closely resembles the downstream task leads to better and faster fine-tuning performance.

Whole sentences from documents are selected and masked, and gap-sentences are concatenated into a pseudo-summary. The corresponding position of each selected gap sentence is replaced by a mask token [MASK1] to inform the model.

To even more closely approximate a summary, sentences that appear to be important/principal to the document are selected.

Three primary strategies are considered for selecting m gap sentences without replacement from a document D, comprised of n sentences:

Random Uniformly select m sentences at random.
Lead Select the first m sentences.
Principal Select top-m scored sentences according to importance. As a proxy for importance we compute ROUGE- F1 between the sentence and the rest of the document

Masked Language Model (MLM)

15% of the tokens in the input text are selected following BERT. The selected tokens are replaced in one of three ways: 80% of the time by a mask token [MASK2], 10% of the time by a random token, or 10% of the time without any change.

It is observed that using MLM during pre-training does not significantly enhance downstream tasks, even after a large number of pre-training steps. As a result, MLM is not incorporated into the final model, PEGASUS-LARGE.

Pre-training Corpus

C4, or the Colossal and Cleaned version of Common Crawl, consists of text from 350M Web-pages (750GB).
HugeNews, a dataset of 1.5B articles (3.8TB) collected from news and news-like websites from 2013- 2019. A whitelist of domains ranging from highquality news publishers to lower-quality sites such as high-school newspapers, and blogs was curated and used to seed a web-crawler. Heuristics were used to identify news-like articles, and only the main article text was extracted as plain text.

Downstream Tasks/Datasets

XSum consists of 227k BBC articles from 2010 to 2017 covering a wide variety of subjects along with professionally written single-sentence summaries.
CNN/DailyMail dataset contains 93k articles from the CNN, and 220k articles the Daily Mail newspapers. Both publishers supplement their articles with bullet point summaries.
NEWSROOM is a large dataset containing 1.3M article-summary pairs written by authors and editors in the newsrooms of 38 major publications between 1998 and 2017.
Multi-News is a multi-document summarization dataset consisting of 56k pairs of news articles and their human-written summaries from the site newser.com.
Gigaword contains 4M examples extracted from news articles from the Gigaword corpus. The task is to generate the headline from the first sentence.
arXiv, PubMed are two long document datasets of scientific publications from arXiv.org (113k) and PubMed (215k). The task is to generate the abstract from the paper body.
BIGPATENT consists of 1.3 million U.S. patents along with human summaries under nine patent classification categories.
WikiHow is a large-scale dataset of instructions from the online WikiHow.com website. Each of 200k examples consists of multiple instruction-step paragraphs along with a summarizing sentence. The task is to generate the concatenated summary-sentences from the paragraphs.
Reddit TIFU contains 120K posts of informal stories from the online discussion forum Reddit, more specifically the TIFU sub-reddit from 2013-Jan to 2018-Mar. The sub-reddit posts strictly follow the rule of writing a descriptive ”TL;DR” summary.
AESLC consists of 18k email bodies and their subjects from the Enron corpus, a collection of email messages of employees in the Enron Corporation.
BillSum contains 23k US Congressional bills and human-written reference summaries from the 103rd-115th (1993–2018) sessions of Congress.

Experiments

PEGASUSBASE had L = 12, H = 768, F = 3072, A = 12

PEGASUSLARGE had L = 16, H = 1024, F = 4096, A = 16

where L denotes the number of layers for encoder and decoder (i.e. Transformer blocks), H for the hidden size, F for the feed-forward layer size and A for the number of self-attention heads.

Sinusoidal positional encodings are used.

Paper

PEGASUS: Pre-training with Extracted Gap-sentences for Abstractive Summarization 1912.08777

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on July 12, 2024.

Canonical link

Exported from Medium on May 4, 2026.
