# Papers Explained 421: AdaptiVocab

Papers Explained 421: AdaptiVocab

Papers Explained 421: AdaptiVocab

AdaptiVocab is an end-to-end approach for vocabulary adaptation, designed to enhance LLM efficiency in low- resource domains. It can be…

Papers Explained 421: AdaptiVocab

AdaptiVocab is an end-to-end approach for vocabulary adaptation, designed to enhance LLM efficiency in low- resource domains. It can be applied to any tokenizer and architecture, modifying the vocabulary by replacing tokens with domain-specific n-gram-based tokens, thereby reducing the number of tokens required for both input processing and output generation.

Method

The AdaptiVocab pipeline

AdaptiVocab comprises four stages:

Vocabulary modification: by replacing tokens with domain-specific n-tokens that reduces the total tokens count.
Tokenization patching algorithm: which ensures our method can be applied to any tokenizer.
Embedding initialization: of new n-tokens suited for auto-regressive generation.
Lightweight adaptation training: of only the embedding matrices and two layers.
Tokenization before and after vocabulary adaptation to the History of Physics domain.
Domain-specific vocabulary modification

The algorithm takes the following inputs:

tokenizer: The existing tokenizer used by the LLM.
corpus D: A domain-specific corpus of text.
m: The number of original tokens to be replaced with new n-tokens.
n: The maximum length of the n-tokens (i.e., the maximum number of original tokens that can be combined into a single new token).

The algorithm outputs Vnew, the modified vocabulary.

Initialization:

Vold: The original vocabulary of the tokenizer is stored.
Vnew: An empty dictionary is initialized to store the new vocabulary.
Dtok: The domain-specific corpus D is tokenized using the original tokenizer. The result is a list of tokenized documents.
n tokens: Candidate n-tokens are prepared from the tokenized corpus Dtok, considering the maximum n-token length n. These n-tokens are combinations of existing tokens that could potentially form new vocabulary entries.
Fn-tok: A dictionary is created to store the frequencies of each candidate n-token in the tokenized corpus Dtok. This counts how often each n-token appears.
Foverlaps: A dictionary is created to store the number of mutual occurrences (overlaps) between every pair of overlapping n-tokens. Two n-tokens are considered overlapping if one contains the other or if the suffix of one matches the prefix of the other.
S: A dictionary is initialized to store the savings score for each candidate n-token t. The initial score S0[t] is calculated as the product of its frequency Fn-tok[t] and its length len(t) (the number of original tokens it comprises). This score represents the potential reduction in token count if the n-token is added to the vocabulary.

Iterative Replacement:

The algorithm iterates m times, replacing m original tokens with new n-tokens.

In each iteration i:

token id: An original token with the lowest frequency is removed from the original vocabulary Vold. The ID of this token will be assigned to the new n-token.
t: The n-token with the highest savings score S[t] is selected.
The selected n-token t is added to the new vocabulary Vnew and assigned the token id of the removed token.
Score Update: The savings scores of all n-tokens that overlap with the newly added n-token t are updated. For each overlapping n-token t’, its score S[t’] is reduced by Foverlaps[t][t’] * len(t’), where Foverlaps[t][t’] is the number of times t and t’ overlap in the corpus, and len(t’) is the length of t’. This reduction accounts for the redundancy introduced by adding t and ensures that subsequent selections prioritize n-tokens that offer the most additional token savings.

Vocabulary Update:

After the loop completes, the new vocabulary Vnew is updated with the remaining tokens from the original vocabulary Vold.

Return:

The algorithm returns the modified vocabulary Vnew.

Tokenization patching algorithm

The primary goal is to adapt the tokenization process to accommodate n-tokens (combinations of existing tokens treated as a single unit) after the vocabulary has been modified.

Tokenization with the Original Tokenizer:

The input text is first tokenized using the original tokenizer (the tokenizer that was used before the vocabulary modification). This provides an initial tokenization of the text.

Decomposition of Removed Tokens:

Any tokens that were removed from the original vocabulary during the vocabulary modification process are replaced with their corresponding decompositions.
The decomposition process follows the original tokenizer’s merging rules and is applied recursively.
The DECOMP function (Algorithm 2, lines 1–5) defines this recursive decomposition. If a token t is in the new vocabulary, it’s returned as is. Otherwise, the token is split into two smaller tokens (t1 and t2) based on the tokenizer’s merging rules, and the DECOMP function is recursively applied to t1 and t2.
For example, if the token “tokenization” was constructed by merging “tokeniza” and “tion”, and both “tokenization” and “tokeniza” were removed from the vocabulary, then “tokenization” would first be replaced with “tokeniza” and “tion”, and then “tokeniza” would be replaced by “token” and “iza”, resulting in the sequence “token”, “iza”, “tion”.

Merging into N-Tokens:

The algorithm iteratively replaces spans of original tokens with the longest possible n-token.
It prioritizes merging based on n-token length rather than savings score (which involves frequency) to reduce the total number of tokens for a given text.
A greedy left-to-right merging strategy is used because the algorithm operates at the tokenized text level.
For example, the tokens “elect”, “rod”, “ynamics” might be replaced by the n-token “electrodynamics”.

Exponential embedding initialization

Averaging the embeddings of constituent tokens treats the new n-token as a simple average of its parts, failing to capture the sequential structure crucial for auto-regressive generation.

In auto-regressive generation, tokens are produced sequentially from left to right. The influence of constituent tokens within an n-token should vary depending on their position to ensure coherent generation.

The exponential initialization adjusts the influence of constituent token embeddings based on their position within the n-token. This is done differently for input and output embeddings to align with the processing and generation aspects of the LLM.

enew: The new embedding for the n-token.
k: The number of tokens in the n-token.
eti: The embedding of the i-th token in the n-token.
wi: The weight assigned to the i-th token’s embedding.
The + sign is used for input embeddings.
The — sign is used for output embeddings.

Efficient adaptation fine-tuning

Only a subset of the model’s parameters are fine-tuned, keeping most transformer layers frozen.

The input embedding matrix which incorporates the modified vocabulary
The language model head (decoding matrix) to ensure proper n-tokens generation
The first and last transformer layers, which directly interact with the embedding matrices.

Experimental setup

Experiments are conducted on Mistral-7B v0.3, which has a vocabulary of 32,768 tokens, and Llama-v2, which has a vocabulary of 32,000 tokens. Mistral-7B v0.3 is evaluated on three domains, while Llama-v2 complements the results in a single domain.

Two baselines are primarily experimented with: the off-the-shelf (Vanilla) LLM and a fine-tuned version trained on domain-specific data (Vanilla+FT). The method (AdaptiVocab+FT) is also compared to a variant without fine-tuning (AdaptiVocab).

The M2D2 collection, which comprises unlabeled datasets from 145 diverse, specialized domains, is utilized. Manually examining dozens of domains from the M2D2 collection, domains featuring proper English text with minimal HTML markup and containing at least 2.5 million tokens are selected. Three domains are hence selected: Earth Science, History and Philosophy of Physics (both have 8.3 million tokens), and Games & Toys (2.9 million tokens).

A maximum n-token length of 3 is used and 10,000 tokens are modified.

Results
Main results.
AdaptiVocab achieves a 22.9–27.9% token reduction in input text processing and a 24.9–27.6% token reduction in text generation, leading to faster generation.
Without fine-tuning, AdaptiVocab results in poor generation quality, but lightweight fine-tuning allows the LLM to adapt and produce outputs comparable to vanilla LLMs.

Human evaluations show that AdaptiVocab’s outputs are ranked on par with vanilla LLMs in most pairwise comparisons.
Multiple-choice QA performance.
Fine-tuning on domain-specific data improves LLM performance on knowledge-based question answering tasks.
AdaptiVocab+FT achieves question answering accuracy comparable to Vanilla+FT, indicating that vocabulary adaptation does not hinder knowledge retention.

Paper

AdaptiVocab: Enhancing LLM Efficiency in Focused Domains through Lightweight Vocabulary Adaptation 2503.19693

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on July 31, 2025.

Canonical link

Exported from Medium on May 4, 2026.
