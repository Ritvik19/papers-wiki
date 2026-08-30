# Papers Explained 431: Anatomy of a Machine Learning Ecosystem

Papers Explained 431: Anatomy of a Machine Learning Ecosystem

Papers Explained 431: Anatomy of a Machine Learning Ecosystem

This work analyzes 1.86 million models on Hugging Face. The study of model family trees — networks that connect fine-tuned models to their…

Papers Explained 431: Anatomy of a Machine Learning Ecosystem

This work analyzes 1.86 million models on Hugging Face. The study of model family trees — networks that connect fine-tuned models to their base or parent — reveals sprawling fine-tuning lineages that vary widely in size and structure. Using an evolutionary biology lens to study ML models, model metadata and model cards are used to measure the genetic similarity and mutation of traits over model families.

Genetic Trait Analysis: The authors tracked the “genetic traits” of models using metadata and model cards and measured the genetic similarity between models within the same family. They found that models within the same family are similar, but mutations occur at a high rate, with fine-tuned siblings sharing more traits than parent/child pairs.
Network Analysis of Trait Diffusion: The authors conducted a network analysis of how model traits diffuse between models. They found that mutations of traits like licenses, languages, and tasks are overwhelmingly acyclic. They also determined optimal orderings for these properties, verifying that translation models are genetically upstream from text-generation models and that models with llama3 licenses are genetically upstream from those with apache-2.0 licenses.
Hypotheses about Environmental Pressures: The authors proposed hypotheses about the environmental pressures driving model evolution based on observed trends. For example, the trend toward permissive licenses suggests that preferences for open source outweigh regulatory pressures, and the drift toward English-language models suggests a strong market for English-language products.

Data

The data for the dataset was collected in two stages. In the first stage, the Hugging Face ‘model’ API was used to collect the model features and relationships, that is, all pieces of information in the dataset aside from the model cards. In the second stage, the full text of every model’s model card was collected through individual, per-model API calls to the model cards API.

Model metadata comes in JSON format. These JSONs include the model id (a unique identifier for each model containing its author and name), likes, trendingScore (a trait defined by Hugging Face for ranking models on their website), downloads, pipeline tag (also known as task — a categorization of models into e.g., feature-extraction, text-generation, image-classification, and other modalities), library name (the Hugging Face library used to support development), createdAt (the date and time that the model was created), and tags. Tags contain a structured list of strings, some with organized prefixes. For example, tags beginning with base model:finetune: link a finetuned model to its parent’s model id, tags beginning with license: contain the model’s license, and those beginning with arxiv: contain links to the arXiv identifiers of accompanying papers. Other tags do not have these prefixes, but their meaning can still be inferred. For example, languages are listed using two- or three-letter ISO-639 codes.

Permissive licenses especially apache-2.0 and mit are dominant, constituting over 60% of all reported licenses.
Text-based tasks — and especially text-generation — are most common.
English is by far the dominant language compatibility on Hugging Face, with over 75% of models that document any language compatibility marking english as a supported language.
Chinese is the second most-common at 4.4%.
transformers is the most common Hugging Face library.
black-forest-labs/FLUX.1-dev is the model that has the most children.
imagefolder is the most commonly recorded dataset in metadata.
Machine Learning and Computers and Society codes are the most common among linked arXiv papers.
Falconsai/nsfw image detection is the most downloaded model.

Throughout the paper, the snippets of text provided by the metadata JSON are treated as the model’s DNA, as it contains rich information about traits and allows tracking changes and differences over generations.
The diff between two sequences of model metadata.
Measuring genetic similarity

Inspired by ecological and genetic perspectives and existing work on network diffusion, the relationship between family structure and attribute similarity is explored. A method is developed for measuring how related two models tend to be given their proximity in the graph. One way of measuring genetic relation is by measuring the overlap or similarity in DNA sequences. The approach measures the semantic distance between the models’ tokenized metadata. Measuring the frequency of different terms in the model metadata and tracking differences in these relative frequencies is proposed.

The approach to calculating similarities borrows from classical contributions in natural language processing based on term frequency. The analysis is replicated for three similarity measures:

the normalized Levenshtein Distance, which directly computes character-level insertions and deletions
the cosine similarity in term frequency (or “bag-of-words”) embeddings
the cosine similarity in term frequency-inverse document frequency (“TF-IDF”) embeddings.

Similarities are measured across two different model artifacts: metadata JSONs and the text of model cards.

The analysis specifically considers fine-tuning edges to construct the family trees.

Omissions:

Model Merges: These are omitted because they represent a form of “sexual reproduction” (multiple parents), which would result in a graph that is no longer a tree (nodes can have more than one predecessor). They are also considerably rarer.
Adaptations and Quantizations: These are omitted because they are less likely to branch and support their own offspring compared to fine-tunes.

Estimating quantities over local family structures (e.g., all pairs of siblings) can be computationally burdensome due to the combinatorial explosion of such structures in a large graph (e.g., 500 children lead to 124,750 sibling pairs). An estimation procedure is designed using a representative sample.

A condition is specified to check if a node or edge resides within a certain subgraph structure.
The multiplicity (how many such subgraphs it belongs to) is counted.
For example, for sibling pairs, if a node u has nsucc(u) children, it contributes (nsucc(u) choose 2) sibling pairs.
A lookup table of nodes meeting the subgraph condition and their multiplicities is maintained.
A weighted sample of nodes from this lookup table is drawn to efficiently estimate quantities over sibling pairs.

The study samples all possible subgraphs of size 2, 3, and 4, and estimates similarities between all possible pairs of nodes within these subgraphs (e.g., parents, grandparents, siblings).
Subgraph patterns, their total occurrences, sampling conditions, and associated multiplicities conditioned on each pattern.
Family resemblance and diffusion characteristics
Cosine similarity between TF-IDF embedding vectors, trained on terms appearing in the model metadata for all models in the dataset.
Overall Finding:

Models that are topologically close in the network exhibit considerably higher similarity than randomly selected pairs, providing evidence for “family resemblances” in model family trees.

Counter-Intuitive Observation:

Siblings are significantly more similar to one another than either is to their parent, on average.
This contradicts predictions from a simple asexual model of genetic reproduction with random mutation, where children would inherit parent’s genes and siblings would be more related to their parent than each other.
This suggests a “directional effect of fine-tuning,” where all child models tend to depart from their parents’ attributes in characteristically similar ways.

Three Major Heuristics Dictating Similarity:

Same Family:

Models belonging to the same family tree show significantly higher similarity compared to randomly paired models.

Low Generational Divide:

Models of the same generation (e.g., siblings, cousins) have significantly higher similarity.
Models one generation apart (e.g., parent/child, uncle/nephew) are significantly more similar than models two generations apart (e.g., grandparent/grandchild). This trend continues for greater generational divides.

Network Distance:

The total number of edges between two nodes also explains observed similarities, aligning with predictions from a genetic model of mutation-based asexual reproduction.
Evidence: Uncle/nephew pairs are less similar than parent/child pairs within the same subgraph structures.
Relative Importance: While generational divide generally outweighs network distance in importance, there is one exception where a parent-child pair (network distance one) exhibits higher similarity than a sibling pair (network distance two).

Evolution of traits

A key observation is that traits often change between parent and child models, leading to the observed diversity in features. The analysis focuses on these instances of “mutation” where a parent’s trait differs from its child’s.

Two general empirical observations are made regarding trait evolution:

Directedness (Drift): Mutations tend to be overwhelmingly directed. For any two traits (i, j), it’s most common for mutations to flow predominantly from i to j or from j to i, rather than a balanced flow in both directions. This phenomenon is termed “drift.”
Orderedness: The orientations of these directed mutations are ordered. It’s possible to find orderings over the “typical” transitions between traits that explain virtually all observed orientations. This implies that cycles (e.g., i to j, j to k, k back to i) are rare for the vast majority of drifts.

While finding such an ordering over a directed graph is generally an NP-hard problem, the natural orderings emerging from the observed graphs allow for optimal solutions.

Licenses drift from commercial to permissive and copyleft

The Hugging Face Hub hosts 162 unique license types, with 98 being standardized categories. Each model has one license. Analysis of license drifts shows a strong directedness. An optimal ordering of licenses can be produced that accounts for 94% of all drift directions and 84% of all mutations. icenses exhibit a surprising pattern where more restrictive, commercial licenses are “upstream” from more permissive and copyleft licenses. This suggests a “relaxation” of terms is the norm.

Example 1 (Gemma): The Gemma license, which includes restrictions (e.g., no sexually explicit content) and requires agreement distribution, frequently mutates to Apache-2.0 and MIT licenses, which lack such provisions.
Example 2 (CC-BY-NC-4.0): The CC-BY-NC-4.0 license, a copyleft license restricting commercial use, often mutates to MIT (granting broad permissions including commercial use) or other Creative Commons licenses without the non-commercial restriction.

Of the first eight licenses in the observed optimal ordering, seven are commercial (Gemma or Llama varieties) or restrictive (OpenRail varieties). Conversely, none of the last eight licenses in the ordering are commercial; they include permissive (CC, Apache-2.0, Artistic-2.0) and copyleft (CC-BY-*, GPL-3.0) varieties.

The observed mutation drift suggests that market and behavioral pressures toward openness outweigh the potential for legal enforcement as a motivator for AI developers.

Documentation thins

Documentation tends to “thin” over generations.
Model cards are highly prevalent for models within family trees.
Missing model cards are significantly more frequent among models without family ties.
For models with family ties, model cards are almost always available, even if very short.
Among parent-child pairs with model cards, the length of these cards drops by approximately 5,000 characters on average. The parent’s model card is roughly twice the size of the child’s.
Despite shortening, model cards more frequently contain terms suggesting automatic generation, such as “automatically generated” or “generated automatically.” About 30% of derivative models include these bigrams.
These findings suggest pressures toward lean documentation and the adoption of automation technologies that reduce the cost of documenting and explaining models.
Markers of auto-generated cards are uniquely observed in finetunes and adapters, implying they are byproducts of existing packages and libraries that facilitate the creation of these specific types of derivatives, rather than merges or quantizations.

Languages specialize and drift toward English

For languages, partial mutations are allowed. The overall mutation rate is calculated as the shared members of language groups divided by their union. Distinct directional mutations are logged from every dropped language to every child language, and from every parent language to every added language.

The observed mutation rate for languages is 12.80%. An optimal ordering accounts for 97.89% of drifts and 74.71% of mutations.
Specialization: There is a significant reduction in language compatibility from base models to child models. Large base models supporting extensive family trees tend to support many languages, whereas derivative models typically list compatibility with only one or a handful of languages. This results in a precipitous reduction in language support between parents and fine-tuned children.
Drift Towards English: Language support overwhelmingly drifts from broad language compatibility to English-language support.
This drift suggests considerable market pressure towards English-speaking products and compatibility.
Despite an increasing number of Chinese models being developed and hosted, a commensurate drift towards Chinese compatibility is not observed.

Tasks appear to recapitulate the machine learning lifecycle

The results suggest that tasks progress from:

Low-level feature extraction tasks (e.g., fill-mask, feature-extraction, automatic-speech-recognition).
To modality translations (e.g., translation, text-generation, summarization, text-to-image).
To classification and reinforcement learning tasks (e.g., object-detection, image-classification, text-classification, reinforcement-learning).

This progression appears to reflect stages in the machine learning training pipeline:

Raw Input Processing: Tokenization or embedding of inputs (text, speech, video).
Representation Learning: Generating contextual embeddings through techniques like masked token prediction.
Model Adaptation: Handling cross-modal inputs or supporting low-resource languages.
Classification: Assigning discrete labels based on learned representations.
Generative Tasks: Producing outputs from context (e.g., summarization, text-to-image synthesis).
Improvement and Alignment: Techniques like instruction tuning and reinforcement learning to enhance output generation, especially for complex reasoning or human preference alignment.

This interpretation is offered as a possible explanatory hypothesis, and further research is needed to substantiate or refute it, drawing an analogy to the contested theories of recapitulation in human development.

Paper

Anatomy of a Machine Learning Ecosystem: 2 Million Models on Hugging Face 2508.06811

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on August 14, 2025.

Canonical link

Exported from Medium on May 4, 2026.
