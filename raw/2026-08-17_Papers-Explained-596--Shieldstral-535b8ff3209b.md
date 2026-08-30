# Papers Explained 596: Shieldstral

Papers Explained 596: Shieldstral

Papers Explained 596: Shieldstral

Shieldstral is a 3B-parameter policy-adaptive multimodal safety classifier that formulates content moderation as a binary…

Papers Explained 596: Shieldstral

Shieldstral is a 3B-parameter policy-adaptive multimodal safety classifier that formulates content moderation as a binary question-answering task, enabling heterogeneous safety datasets with divergent taxonomies to be consolidated under one training framework.

Task Definition
Shieldstral architecture.
Since the goal is to train a policy-adaptive safety classification model on a wide variety of datasets, the task is reduced to a standard binary question-answering task.

Each input is structured as follows:

System message. A fixed instruction establishing the meta-task and the expected grammar of the input and output.
User message. Composed of three tagged fields:

High-level task framing describing the evaluation context and strictness level. This is expected to be constant across a dataset or task.
A specific yes/no question about the document (e.g., “Does this content promote violence?”).
The content being evaluated : a user prompt, a model response, a formatted prompt–response pair, or an image (optionally accompanied by text).

At training time, Shieldstral is trained using standard cross-entropy loss over the full vocabulary at the output position. At inference time, only the “yes” and “no” token IDs are unembedded, yielding logprobs z_yes and z_no respectively. The safety score s is then computed as the softmax-normalised score s = exp(z_yes) / (exp(z_yes) + exp(z_no)) and thresholded at τ = 0.5 for binary classification.

Model Architecture

Shieldstral is built upon Ministral-3B-Base-2512, a 3B-parameter causal language model from the Mistral-3 family with native multimodal support via a Pixtral vision encoder.

Training Data Construction

A diverse training data of approximately 54.1M samples (45.2M open-source text samples, 4.4M synthetic contrastive text samples, 4.5M multimodal samples) is drawn from and generated based on a wide range of heterogeneous sources spanning safety, toxicity, hate speech, jailbreak detection, content moderation, and response quality domains. These sources differ widely in label formats, category taxonomies, and annotation conventions ranging from binary safe/unsafe flags to multi-label taxonomies.

A four stage pipeline is used:

A template-based unification layer converts every dataset into a common instruction–query–document format, reducing diverse safety tasks: prompt classification, response moderation, refusal detection, toxicity detection, to a single yes/no question-answering problem.
Contrastive sample curation pairs the same content with both matching and non-matching queries, sharpening the model’s decision boundaries by forcing it to distinguish which specific policy a piece of content violates rather than learning a coarse safe-vs-unsafe split.
Contrastive sample generation rewrites safe samples into contrastive positive and hard-negative pairs, teaching the model to distinguish subtle differences between similar categories and enhancing its adaptability to user-defined policies.
A dedicated image data pipeline (Section 3.4) addresses the scarcity of visual safety data by supplementing limited moderation datasets with general-purpose image datasets and mutating queries across categories, helping the model ground textual safety concepts in visual content.

Template-Based Data Unification
Training sample examples.
These heterogeneous sources are unified into a single training format through the instruction–query–document structure. A diverse set of candidate phrasings is created, and random sampling among them occurs at data-generation time. In total, this yields 45.2M text samples.

Each dataset is handled by its own processor i.e., a manually designed dataset-specific pipeline based on the existing description of the dataset that defines the labelling logic, category mappings, and instruction templates tailored to that dataset’s task and annotation conventions. An LLM is used to generate multiple paraphrase variants of instruction templates for each processor that encode

The task framing (e.g., safety classification vs. quality assessment).
The intended strictness level (strict, moderate, or lenient).
Domain-specific context such as multilinguality or adversarial framing.
Instruction template strictness levels.
Query templates encode the specific yes/no question the model must answer. They are organised into several task types, each with multiple paraphrase variants:

Category-specific queries. For datasets with fine-grained taxonomies, each category has its own query pool (e.g., “Does this content promote violence?”, “Does this message contain hate speech targeting a racial group?”).
Binary queries. Variants asking about overall safety without specifying a category (e.g., “Is this content harmful?”).
Refusal detection queries. Dedicated variants for detecting whether a response constitutes a refusal (e.g., “Does the assistant refuse to answer the user’s request?”)

When evaluating prompt safety, the document field contains the raw prompt text. For prompt–response pairs, the two are combined using a randomly selected format from diverse template families.
Document format families with examples.
For datasets involving images, the template system employs a multi-version curation strategy:

One query evaluates whether the image is unsafe in isolation.
Another evaluates whether the accompanying text is unsafe in isolation.
A query assesses the combined content, deeming it unsafe if either component is unsafe.

Contrastive Sample Curation

The key insight of this data strategy is generating contrastive training pairs from the same content by varying the query. This teaches the model to discriminate between categories rather than simply detecting “unsafe” content.

Positive samples: For each piece of harmful content, multiple positive samples are generated: a coarse-grained binary query (“Is this message unsafe?”), a category-specific query (“Does this content promote violence?”), and, when applicable, a target-group-specific query (“Does this content promote violence toward children?”).

Negatives samples: Negatives are generated through three strategies:

Category-based hard negatives, where content violating category A is paired with queries about absent categories B, C, . . .
Demographic-based negatives, where content targeting group A is paired with queries about unrelated groups;
Safe-content negatives, where genuinely safe samples are paired with binary harmfulness queries.

Contrastive generation naturally produces more negatives than positives. To counteract this imbalance, each positive sample is duplicated k times with independently paraphrased instruction and query per copy, serving the dual purpose of increasing the positive ratio and augmenting template diversity.

Many public safety datasets contain incorrect labels. An open-source LLM is employed to cross-validate dataset labels, removing samples where the dataset’s label disagrees with the LLM’s classification at both the binary (safe/unsafe) and per-category levels. This filtering improves label consistency across heterogeneous sources and reduces noise such as false positives and false negatives in the training signal.

Contrastive Sample Generation

Building on the contrastive approach from the previous section, an LLM is further employed to generate contrastive pairs. Rather than teaching the model to recognise a fixed set of policies, it is trained to discriminate between similar categories. In total, this produces approximately 4.4M samples.

A training taxonomy for synthetic dataset generation is first defined. It is organised as a hierarchical structure with 11 super classes and 73 leaf categories.

Training samples are generated by rewriting safe source texts into unsafe variants using an LLM. For every category, whether super class, subcategory, or leaf, the LLM receives a safe text along with a target category and a sibling (negative) category, and produces:

An unsafe rewrite exhibiting the target category while avoiding the sibling
A query about the target category
A negative query about the sibling category.

This yields both positive and negative training pairs from a single LLM call.

The positive training sample pairs the rewritten content (1) with the target-category query (2) and an assistant response of “yes”, while the negative sample pairs the same content (1) with the sibling-category query (3) and an assistant response of “no”. Because the taxonomy is hierarchical, content that violates a leaf category also violates every ancestor up to the super class.

This is exploited by recursively generating additional positive samples: for each ancestor category, a query phrasing is sampled for that category and paired with the same rewritten content, labelled “yes”.
Example contrastive training pair generated from a single LLM call.
Image Data Processing

Compared to text, image safety data is considerably more difficult to obtain at scale. The limited moderation sources are supplemented with general-purpose image classification and object-detection datasets, which provide a large pool of diverse, naturally safe images that serve as high-quality negatives. Combined with LLM-based query mutation and hard-negative construction, this pipeline yields approximately 4.5M multimodal training samples.

Query mutation: The image pipeline generates approximately 2,000 diverse query phrasings from a (fixed) 14-subcategory visual moderation taxonomy (covering NSFW, violence, hate, and illegal content) using an LLM. Approximately 30% of queries are inverse formulations (e.g., “Is this image safe from violence?”) that teach the model to handle both positive and negative framings of the same category.

After dataset construction, a vision–language reranker model scores every image–query pair, filtering mislabelled source data and LLM hallucinations. Asymmetric thresholds preserve rare violation samples while applying stricter filtering to abundant negatives.

An LLM generates hard negatives, that is, images paired with near-miss queries from sibling categories, to sharpen the model’s within-domain discrimination. These hard negatives are re-filtered through the VL reranker before inclusion in the final training set.

Training Recipe

Shieldstral is fine-tuned with LoRA on the language model parameters using cross-entropy loss on the single output token. A comparison of LoRA and full SFT observed no significant difference, so LoRA is adopted for its training efficiency. Two specialised checkpoints are trained: one on public safety datasets (P) excluding the generated data, and one on the combination of public and generated taxonomy data (PG) from the entire pipeline.

The two data regimes exhibit complementary strengths: P is well-calibrated to standard benchmarks, whereas PG adds fine-grained category discrimination but may suffer from distribution drift. To combine both without additional training, SLERP is applied, merging with three components:

PG (weight 0.6): the checkpoint trained on public + generated taxonomy data, providing policy-adaptive generalisation.
P (weight 0.3): the checkpoint trained on public data only, anchoring benchmark calibration.
Ministral-3B-Instruct (weight 0.1): the base instruct checkpoint, contributing general instruction-following capability.

Evaluation
F1 scores (%) on safety classification benchmarks.
Shieldstral matches the much larger GPT-OSS-Safeguard-20B in overall text F1 score (84.9%), despite having only 3B parameters, indicating strong efficiency and performance.
F1 scores (%) on refusal detection benchmarks.
Shieldstral excels at refusal detection, demonstrating robustness in handling risky prompts.
The model’s high performance across language splits confirms the effectiveness of the data curation pipeline for consolidating diverse datasets.
F1 scores (%) on multimodal safety benchmarks.
Shieldstral leads on multimodal benchmarks with an overall F1 of 83.8%, outperforming OmniGuard (77.6%) and excelling on VLGuard and UnsafeBench, despite having less than half the parameters of OmniGuard (3B vs. 7B).
Its success across text and image tasks confirms the generalisability of the data curation pipeline used in training, with conversation-centric models less effective in image-only domains.

Adaptability Evaluation

General safety moderation can be measured using existing benchmarks. However, adaptability requires special safety datasets. These datasets must include:

Policies that drift from training categories
Entirely novel policies not seen in training

Hence, the evaluation taxonomy is crafted independently and follows four principles:

Disjoint Categories: No sibling overlappings; each content only maps to one leaf category.
Type-based Distinctions: Categories are based on harm type, not severity level.
Action-oriented Naming: Definitions are concrete and operational, not abstract legal terms.
Mutual Sibling Requirement: At least two leaf categories per subcategory, which is needed for effective contrastive sample generation.
Scores (%) on the adaptability benchmark.
Shieldstral achieves 91.3% F1 on the adaptability benchmark, closely trailing the largest competitor (94.1%) but doing so with greater inference efficiency (single-token output vs. lengthy reasoning traces), making Shieldstral more practical for deployment.
The model’s adaptability highlights an efficient approach for policy evaluation without sacrificing significant accuracy.

Paper

Shieldstral 2607.25857

That’s a wrap!

If you enjoyed this breakdown, follow for more. I publish new paper explanations most weekdays.

More papers in this series, organized by lab and topic, are in the start here guide.

What paper should I cover next? Let me know in the responses.

By Ritvik Rastogi on August 17, 2026.

Canonical link

Exported from Medium on August 22, 2026.
