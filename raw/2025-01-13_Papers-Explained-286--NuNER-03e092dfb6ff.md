# Papers Explained 286: NuNER

Papers Explained 286: NuNER

Papers Explained 286: NuNER

NuNER is a compact language representation model specialized in the Named Entity Recognition (NER) task. It can be fine-tuned to solve…

Papers Explained 286: NuNER

NuNER is a compact language representation model specialized in the Named Entity Recognition (NER) task. It can be fine-tuned to solve downstream NER problems in a data-efficient way, outperforming similar-sized foundation models in the few-shot regime and competing with much larger LLMs.
NuNER creation procedure.
The models are available on HuggingFace.

Dataset Creation

A random sample of C4, an English web crawl corpus containing text from blog posts, news articles, and social media messages, is selected for its domain diversity. The dataset is annotated with entities spanning a large and diverse set of types so that the model can generalize to all kinds of NER problems. An unconstrained approach is taken, allowing the LLM to extract any entity it identifies and assign any type it deems appropriate for each entity. This includes annotating with concepts more akin to topics than entity types. These entity types/topics are referred to as concepts. To resolve potential ambiguities, the LLM is also asked to provide descriptions for the concepts it identifies.
The goal is to create a dataset for entity recognition. Label as many entities, concepts, and ideas as possible in the input text. Invent new entity types that may not exist in traditional NER Tasks such as more abstract concepts and ideas. Make sure the entity concept is not part of speech but something more meaningful. Avoid finding meaningless entities.Output format (separate entities with new line):entity from the text <> entity concept <> description of entity group/conceptInput: [INPUT SENTENCE]
The position of the entity in the text is not returned because LLMs are not good at counting. To train NuNER, the position is retrieved through an exact string match, which can lead to annotation errors in rare cases. GPT-3.5-turbo-0301 is used with a prompt to annotate 1.35M sentences. A simple filter is then applied to remove sentences containing an annotation with the concept “concept”, as it is considered too uninformative. This results in a final dataset of 1M annotated sentences, a total of 4.38M entity annotations, distributed across 200k unique concepts.
Feature map of the 50k most common concepts extracted by gpt-3.5-turbo-0301. Embeddings are obtained from the concept encoder.
This dataset contains 200k concepts and exhibits high concept-imbalance. Some concepts are similar to each other, such as “company” and “company name”. Additionally, many potential entities in a sentence are not extracted.
Frequency of each concept assigned by GPT-3.5.
Due to these factors, training a conventional token classifier over the entire set of concepts is not practical. A training method based on the contrastive learning framework is proposed instead.
NuNER’s pre-tranining procedure.
The training network consists of two separate sub-networks: the first is NuNER, which encodes the input text as a sequence of vectors. The second encodes a concept name as a unique vector. The text vectors are matrix-multiplied with the concept vector to obtain logits, which are then passed through a logistic sigmoid to yield probabilities. During training, this setup encourages each token embedding to align with the concept embedding if the token instantiates the concept, and to become opposite otherwise.

RoBERTa-base is used for both the text encoder and the concept encoder. The model is trained for 10 epochs on the full 1M sentence dataset. The bottom 6 layers of the text encoder are frozen as it leads to better training stability. After training, the concept encoder is discarded and the text encoder NuNER is kept.

Experiments

Few-Shot with Frozen Foundation

Comparing NuNER’s pre-training with an alternative large-scale NER dataset (NERBERT).

NuNER outperforms RoBERTa trained on NER-BERT data by a significant margin across all training sizes and datasets.

Few-Shot with TadNER on Few-NERD

Adapted the TadNER framework, replacing its BERT components with NuNER.
Few-NERD performance using TadNER and a modified TadNER using NuNER-BERT as the backbone.
NuNER establishes itself as the new state-of-the-art for the Few-NERD benchmark.

Comparison with LLMs

Comparison of the performance of NuNER with modern generative LLMs like GPT-3.5, GPT-4, and UniversalNER in the NER task, by creating training sets with a specific number of words belonging to a given entity type, called kw, instead of using the k ∼ 2k entity-based mining method.

GPT-3.5 and GPT-4: Used via in-context learning with Spacy’s NER V3 prompt.
UniversalNER: Fine-tuned for few-shot learning using the original training settings with modifications for enhanced performance.
NuNER: A two-layer fully-connected network is attached and fine-tuned for 30 epochs.
Comparison of NuNER with LLMs.
GPT-3.5 and GPT-4 perform well in zero-shot and show rapid improvement with added examples.
GPT-3.5 plateaus for larger training sets and is outperformed by UniversalNER and NuNER when kw > 8.
UniversalNER starts lower but catches up and surpasses GPT-3.5.
NuNER starts lower than others but quickly matches UniversalNER and surpasses GPT-3.5.
NuNER vs. UniversalNER few-shot entity-level F1-score in the k ∼ 2k setting.
NuNER and UniversalNER have similar performance in a standard k ∼ 2k setting, despite being 56 times smaller. This could be due to:
An inherent advantage of encoders over generative models for NER.
NuNER’s pre-training encourages human concepts in the last layers, easily accessible during few-shot training.

Paper

NuNER: Entity Recognition Encoder Pre-training via LLM-Annotated Data 2402.15343

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on January 13, 2025.

Canonical link

Exported from Medium on May 4, 2026.
