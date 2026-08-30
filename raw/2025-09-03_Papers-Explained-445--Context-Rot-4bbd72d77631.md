# Papers Explained 445: Context Rot

Papers Explained 445: Context Rot

Papers Explained 445: Context Rot

LLMs are typically presumed to process context uniformly. However, in practice, this assumption does not hold. Model performance varies…

Papers Explained 445: Context Rot

LLMs are typically presumed to process context uniformly. However, in practice, this assumption does not hold. Model performance varies significantly as input length changes, even on simple tasks. Because these models achieve near-perfect scores on widely adopted benchmarks like Needle in a Haystack (NIAH), it’s often assumed that their performance is uniform across long-context tasks.

However, NIAH is fundamentally a simple retrieval task, in which a known sentence (the “needle”) is placed in a long document of unrelated text (the “haystack”), and the model is prompted to retrieve it. While scalable, this benchmark typically assesses direct lexical matching, which may not be representative of flexible, semantically oriented tasks.

This report evaluates 18 LLMs, including the state-of-the-art GPT-4.1, Claude 4, Gemini 2.5, and Qwen3 models. Results reveal that models do not use their context uniformly; instead, their performance grows increasingly unreliable as input length grows.

Needle in a Haystack Extension

The classic Needle in a Haystack task involves placing a random fact (the ‘needle’) in the middle of a long context window (the ‘haystack’), then asking the model about that fact.

The original implementation of this task uses a needle-question pair with lexical matches. However, usage of long context in practice often requires semantic understanding of ambiguous tasks.
Example Needle in a Haystack (NIAH) Setup
NoLiMa has demonstrated non-lexical matching to be a challenge for models as context length increases. This task utilizes needle-question pairs that require models to infer latent associations.

Testing the impact of non-lexical matching in isolation remains underexplored. Furthermore, this binary distinction of “lexical” versus “non-lexical” oversimplifies the complexity of question-answering in real-world scenarios. Needle-question pairs exist on a spectrum of similarity, yet they are all classified under these broad categories.

Models often have to deal with distractors as well, which has been shown to degrade performance.
Comparison — Distractor vs. Irrelevant Context
Distractors are topically related to the needle, but do not quite answer the question
Irrelevant content is unrelated to the needle and question

Another underexplored aspect of NIAH is the haystack itself, which is often simply treated as a means of scaling input length, but this assumes that the haystack content itself has no effect on task performance. If the model is indeed insensitive to the content of the haystack, then varying this content, for example the haystack’s topic or narrative flow, should have no influence on the results. However, this assumption remains largely untested.

Four controlled experiments are designed to investigate the influence of these factors:

Needle-Question Similarity

Cosine similarity between needle-question pairs is computed using embeddings. For robustness, the average across five embedding models is taken: text-embedding-3-small, text-embedding-3-large, jina-embeddings-v3, voyage-3-large, and all-MiniLM-L6-v2. Model performance is measured as input length increases, considering the impact of needle-question similarity.

Impact of Distractors

Taking a high-similarity needle-question pair, four distractors are written. The following setups are used:

Baseline: needle only, no distractors
Single distractor: needle + one randomly positioned distractor
Multiple distractors: needle + all four distractors randomly positioned

The impact of distractors on model performance is tested as input length increases to measure non-uniformity amongst distractors and input lengths.

Needle-Haystack Similarity

Two thematically distinct haystacks, Paul Graham essays and arXiv papers, are used. Corresponding needles are written for each. To measure needle-haystack similarity, the haystack is embedded and the top-5 chunks for each needle are retrieved. The average cosine similarity scores are then calculated. This process is repeated across five different embedding models for robustness.

Haystack Structure

In typical NIAH setups, haystacks are concatenations of coherent texts, each with their own logical flow of ideas. For instance, the original NIAH benchmark uses a series of Paul Graham essays, where each essay follows a structured organization of ideas to form an argument. To evaluate whether this structure influences model performance, two conditions are compared:

Original: preserves the natural flow of ideas within each excerpt
Shuffled: sentences are randomly reordered throughout the haystack to maintain the same overall topic without logical continuity

Details

For every unique combination of needle type, haystack topic, and haystack structure, models are tested across:

8 input lengths
11 needle positions

Models are evaluated across their maximum context window with temperature=0 unless that setting is incompatible (i.e. o3) or explicitly discouraged (i.e. Qwen’s “thinking mode”). For Qwen models, the YaRN method is applied to extend from 32,768 to 131,072 tokens.

Models are included in both standard and “thinking mode” where applicable. Model outputs are evaluated using an aligned GPT-4.1 judge.

Needle-Question Similarity

The experiment uses two domains for the haystack content: Paul Graham (PG) essays and arXiv papers.

For each haystack topic, common themes were identified to guide question and needle writing. This involved chunking documents, embedding the chunks, using UMAP for dimensionality reduction, and HDBSCAN for clustering. Representative chunks from the largest clusters were examined manually to determine their themes and style. For PG essays, writing advice was identified as a common theme, while information retrieval, specifically re-ranking, was identified for arXiv papers.

Corresponding questions were written for each topic. Before writing the needles, it was verified that answers to these questions did not exist in the haystack content by querying a vector database of haystack chunk embeddings and manually examining the top-10 results.

For each question, eight needles were written, each belonging to the large cluster, verified using approximate predictions. Needles belonging to the writing/retrieval cluster with >0.9 probability were considered to topically blend into the haystack. The needles were manually written to avoid data contamination. The level of ambiguity was varied for the eight needles by computing embeddings for the needle and question and their cosine similarity across five embedding models. For the PG essays topic, the needles ranged from 0.445–0.775 needle-question similarity, and for the arXiv topic, the range was 0.521–0.829.

NIAH: Needle-Question Similarity.

Performance Degradation with Lower Similarity: Model performance degrades more quickly with increasing input length when needle-question pairs have lower semantic similarity. This reflects more realistic scenarios where semantic ambiguity compounds the challenge of long input processing.
Initial High Performance: At short input lengths, models (especially high/medium-performance ones) perform well even on low-similarity pairs, demonstrating their capability for the task under less demanding conditions.
Input Size as Primary Factor: The observed performance degradation at longer input lengths is primarily due to the increasing input size (amount of irrelevant content), rather than the intrinsic difficulty of the needle-question pairing itself.
No Influence of Needle Position: Testing across 11 needle positions revealed no notable variation in performance for this specific NIAH (Needle In A Haystack) task.

Impact of Distractors

The experiment focused on one needle with high needle-question similarity to create a condition where the needle should be relatively easy to identify. This allowed for better isolation and measurement of the impact of distractors alone.

Three test conditions were implemented: a baseline condition with only the needle (no distractors), a single distractor condition with the needle and one randomly positioned distractor, and a multiple distractor condition with the needle and all four distractors randomly positioned throughout the haystack.
Impact of Distractors — Three Conditions

Impact of Distractors: Performance by Number of Distractors — arXiv haystack/PG essay needles

Performance Degradation by Distractors: Even a single distractor reduces model performance compared to the baseline (needle only), and adding more distractors (four) further compounds this performance degradation.

Impact of Distractors: Performance by Individual Distractors — arXiv haystack/PG essay needles

Non-Uniform Impact of Individual Distractors: Distractors do not have a uniform impact; some individual distractors cause a greater decline in performance than others (e.g., distractor 3 in the arXiv haystack/PG essay needle combination).

Impact of Distractors: Failure Analysis — arXiv haystack/PG essay needles

Hallucination Patterns: Analysis of failed attempts in the 4-distractor condition revealed that specific distractors (e.g., distractors 2 and 3 for the arXiv haystack/PG essay needle) appear most frequently in hallucinated responses across models.
Claude models (specifically Sonnet 4 and Opus 4) consistently exhibit the lowest hallucination rates and tend to be conservative, often abstaining and explicitly stating when an answer cannot be found due to uncertainty.
GPT models show the highest rates of hallucination, frequently generating confident but incorrect responses when distractors are present.
Amplified Impact with Input Length: The impact of distractors and their non-uniformity amplifies as input length increases across all tested models, including the latest state-of-the-art models.

Needle-Haystack Similarity

The experiment involved placing both PG essay and arXiv needles within each type of haystack. For example, both types of needles were placed within a Paul Graham essay haystack to compare the performance of semantically similar needles (PG essay needles) against unrelated needles (arXiv needles). The same process was repeated with the arXiv haystack.
Needle-Haystack Similarity: Experimental SetupNeedle-Haystack Similarity Results
In the Paul Graham essay haystack, models performed significantly better when the needle (arXiv needles) did not semantically blend in with the haystack, compared to when it did (PG essay needles).
Conversely, in the arXiv haystack, only minimal performance differences were observed between arXiv needles and PG essay needles.
The findings reveal that needle-haystack similarity has a non-uniform effect on model performance, highlighting the non-uniform nature of long-context processing.
Even when task structure and needle-question similarity are held constant, the semantic similarity between the needle and the haystack can influence results.
While testing across only two topics is insufficient to draw a generalizable conclusion that higher needle-haystack similarity consistently degrades model performance, this area is identified as underexplored in long-context benchmarks and a meaningful direction for future research.

Haystack Structure

Two variants of the haystack were created: an “Original” version that preserved the natural flow of ideas within each excerpt, and a “Shuffled” version where sentences were randomly reordered throughout the haystack, maintaining the same overall topic but without logical continuity. The experiment then compared model performance on these two haystack structures across 18 different models and various needle-haystack configurations.
Haystack Structure: Sample Experimental SetupHaystack Structure: Averaged Performance Across 18 Models for Original vs Shuffled Haystacks
Surprisingly, structural coherence consistently hurts model performance; models perform worse when the haystack preserves a logical flow of ideas.
Shuffling the haystack and removing local coherence consistently improves model performance.
Across all 18 models and needle-haystack configurations tested, a consistent pattern was observed where models performed better on shuffled haystacks than on logically structured ones.
These results suggest that structural patterns of inputs could influence the model’s internal processing, particularly how the attention mechanism is applied, especially as input length increases.
The findings point to a potential direction for interpretability research to understand how attention is influenced by input structure, which could help explain long context failure patterns.

LongMemEval

LongMemEval is a long-context benchmark for conversational question-answering, to evaluate models in a realistic setting. The core idea is to assess how well models can answer questions based on a long chat history between a user and an assistant.

The experiment involves presenting models with two types of inputs:

Focused Input: This input contains only the relevant parts of the chat history needed to answer the question. The model’s task is primarily reasoning, as it doesn’t need to sift through irrelevant information. These prompts average around 300 tokens.
Full Input: This input includes the entire 113k token LongMemEval input, containing both relevant and irrelevant context. The model must perform retrieval (identifying relevant information) and reasoning to answer the question.

The LongMemEval_s dataset was filtered for knowledge update, temporal reasoning, and multi-session tasks. The dataset was then manually cleaned to remove ambiguous or unanswerable questions, resulting in a final set of 306 prompts.

Model outputs were judged using an aligned LLM judge (GPT-4.1 with >99% alignment to human judgment).
LongMemEval — Examples by Question TypeLongMemEval Results — Claude FamilyLongMemEval Results — GPT FamilyLongMemEval Results — Gemini FamilyLongMemEval Results — Qwen Family
Across all models, there was significantly higher performance on focused prompts compared to full prompts. This suggests that adding irrelevant context, which forces models to perform an additional retrieval step, significantly degrades their ability to maintain reliable performance.
The Claude models exhibited the most pronounced performance gap between focused and full prompts, largely due to abstentions arising from ambiguity, particularly in Claude Opus 4 and Sonnet 4.
This trend of stronger performance on focused prompts also held true for the GPT, Gemini, and Qwen model families.
While enabling “thinking modes” led to notable gains on both focused and full prompts for models that support it, a performance gap between the two input lengths still persisted, indicating that even advanced reasoning capabilities don’t fully mitigate the challenge of irrelevant context.

Repeated Words

The experiment was designed to assess how well language models can replicate a sequence of repeated words with a single unique word inserted at a specific position, as context length increases. The prompt explicitly instructed the model to reproduce the input text exactly.

Prompt: “Simply replicate the following text, output the exact same text: [repeated words] [unique word] [repeated words]”.

Word Combinations: The task was performed for the following word combinations:

Common word: “apple” | unique word: “apples”
Common word: “apples” | unique word: “apple”
Common word: “golden” | unique word: “Golden”
Common word: “orange” | unique word: “run”
Common word: “orange” | unique word: “San Francisco”
Common word: “San Francisco” | unique word: “sf”
Common word: “Golden Gate Bridge” | unique word: “Golden Gate Park”

For each word combination, 1090 variations of context lengths and unique word indices were created. The number of words in the sequence varied across the following values: 25, 50, 75, 100, 250, 500, 750, 1000, 2500, 5000, 7500, and 10000. The index of the unique word was set to every possible position when the total number of words was less than or equal to 100. Otherwise, the index was incremented by num_words // 100.
Repeated Words — Claude FamilyRepeated Words — GPT FamilyRepeated Words — Gemini FamilyRepeated Words — Qwen Family
General Performance Degradation: Model performance consistently degrades across all models as context length (input + output) increases. This suggests LLMs are not uniformly reliable for straightforward tasks at scale.
Model Refusals/Non-Attempts: Models across all families exhibit patterns of not attempting the task, with varying refusal rates and reasons.
Claude Opus 4 refused 2.89% of tasks, often starting from 2500 words, citing reasons like copyrighted material risk or perceived inconsistencies.
GPT-4.1 had a 2.55% refusal rate, typically starting around 2500 words.
Qwen3–8B showed 4.21% non-attempts.
Random Outputs and Variability: Several models generated random words not present in the input, indicating a breakdown in faithful reproduction.
GPT-4.1 mini sometimes generated random words for specific combinations.
GPT-4.1 nano occasionally output lowercase versions of words (e.g., “san” instead of “San”).
GPT-4 Turbo exhibited the most variable outputs in its family, with a greater tendency for diverse random outputs.
Most Gemini family models (except Gemini 2.5 Flash on one combination) generated random words.

Paper

Context Rot: How Increasing Input Tokens Impacts LLM Performance

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on September 3, 2025.

Canonical link

Exported from Medium on May 4, 2026.
