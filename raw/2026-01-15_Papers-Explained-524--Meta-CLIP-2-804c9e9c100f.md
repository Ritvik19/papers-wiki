# Papers Explained 524: Meta CLIP 2

Papers Explained 524: Meta CLIP 2

Papers Explained 524: Meta CLIP 2

Although CLIP is successfully trained on billion-scale image-text pairs from the English world, scaling CLIP’s training further to learning…

Papers Explained 524: Meta CLIP 2

Although CLIP is successfully trained on billion-scale image-text pairs from the English world, scaling CLIP’s training further to learning from the worldwide web data is still challenging:

No curation method is available to handle data points from non-English world
The English performance from existing multilingual CLIP is worse than its English-only counterpart, i.e., “curse of multilinguality” that is common in LLMs.

Meta CLIP 2, the first recipe training CLIP from scratch on worldwide web-scale image-text pairs, is presented.

The Meta CLIP 2 Recipe

A from-scratch, worldwide CLIP training recipe that extends Meta CLIP’s English-only data curation to 300+ languages using Wikipedia and multilingual WordNet, with per-language substring matching and balancing to create a controlled, concept-balanced training distribution from native, non-translated web alt-texts.
Overview of Meta CLIP 2 recipe.
The scaling of CLIP to native worldwide data and training comprises three steps:

Constructing worldwide metadata
Implementing worldwide curation algorithm
Building training framework for worldwide model.

For generalizable recipe and findings, Meta CLIP 2 is designed to maximize overlapping with OpenAI CLIP and Meta CLIP, and only adopts necessary changes to learn from worldwide data.

Revisit of Meta CLIP Algorithm

The algorithm first constructs metadata M, a list of high-quality visual concepts, from corpora written by human experts. M contains 500k entries, a combination and deduplication of entities from four high-quality sources:

all English WordNet Synsets
Wikipedia English unigrams, bigrams
Wikipedia page titles.

Then, the algorithm performs substring matching on each alt-text (from a given image-text pair in the data pool D) using metadata M to obtain a list matched_entry_ids. Global counting is conducted to calculate the number of matches over D for each entry in M as entry_count.

Finally, the algorithm applies balancing to transform the raw image-text pair distribution into a distribution that is balanced for head and tail concepts and ready for training, by associating each pair with a sampling probability.

Specifically, the count per entry is first converted into a probability of sampling each entry, entry_prob, where tail entries (defined as entry_count < t) have a probability set to 1, and all the other head entries have t/entry_count as sampling probabilities.

Each pair is then sampled based on probabilities of matched entries in its alt-text. Here, t is a threshold to decide head vs. tail entries and set to 20k in OpenAI CLIP; Meta CLIP raised t to 170k for scaling to billion English pairs.

Worldwide Metadata

The first challenge for worldwide scaling is addressed by constructing missing metadata to cover the non-English world. Independent metadata per language is maintained since such design is intuitive, has better performance, and is flexible for adding and curating a new set of languages in future.

Metadata is from the same four sources as OpenAI CLIP and Meta CLIP, but beyond English. Key changes are as follows:

Multilingual WordNet: all synsets from 31 languages are included.
Wikipedia Unigrams and Bigrams: unigram and bigram are processed from Wikipedia dumps dated on May 2024, which include corpora in 329 languages. The corpora are cleaned into plain text with WikiExtractor. For most languages, space and punctuation are used to tokenize text into words, and then unigrams and bigrams are counted. For languages without space separation, open-source tokenizers are used.
Wikipedia Titles: page titles from 40 random dates of Wikipedia snapshots are used and ranked by click-through traffic for each language.

Curation Algorithm

1. Language Identification and Metadata Mapping:

The process begins with identifying the language of each alt-text using Language Identification (LID).
Metadata is then selected based on the identified language, using a mapping between LID languages and metadata language groups. This ensures relevant metadata is used for each image-text pair.

2. Substring Matching and Count Aggregation:

Substring matching is performed between the alt-text and the metadata corresponding to its predicted language.
This identifies matching concepts and their frequency of occurrence, stored in entry_counts.

3. Threshold-Based Data Balancing:

A threshold t is used to define “head” and “tail” concepts based on their match counts. Head concepts have high counts, while tail concepts have low counts.
This threshold is crucial for balancing the training data distribution. A higher t leads to more head concepts and less tail concepts.

4. Language-Dependent Thresholds:

Unlike previous approaches that used a single threshold for all languages, this method employs language-dependent thresholds (tlang).
This is achieved by first calculating a global tail proportion p based on English tail entries. Then, for each non-English language, tlang is determined to ensure the same tail proportion across all languages.

5. Sampling and Curated Dataset:

Based on the calculated tlang and entry_counts, sampling probabilities (entry_probs) are generated for each language.
Image-text pairs are then sampled based on these probabilities. Tail concept matches are always selected (probability = 1.0), while head concept matches have probabilities based on tlang and entry_counts.
This results in a curated dataset D* with balanced and diverse training pairs.

Training Framework

Existing CLIP training, while using globally curated data, still suffers from the curse of multilinguality.

The framework builds upon OpenAI/Meta CLIP’s training setting and model architecture with three key additions:

Multilingual text tokenizer: Enables support for various languages.
Scaling seen training pairs: Addresses the imbalance introduced by adding non-English data.
Study of minimal viable model capacity: Determines the smallest model size needed to effectively handle multilingual data.

Scaling seen training pairs:

Simply increasing the dataset size without proportionally scaling English training pairs harms English performance.
To maintain the original English training amount, the global batch size is increased by 2.3x to reflect the 44% proportion of English pairs in the dataset. This encourages cross-lingual learning.

Minimal viable model capacity:

Even the largest ViT-L/14 model struggles with the curse of multilinguality.
ViT-H/14 is identified as the inflection point, demonstrating significant performance improvement in both English and non-English tasks.
Hyperparameters of OpenAI CLIP / Meta CLIP vs Meta CLIP 2.
Evaluation

Main ablation.

Scaling worldwide data with sufficient model capacity (ViT-H/14, 2.3× seen pairs) allows Meta CLIP 2 to:

Outperform English-only and non-English-only variants on both English and multilingual benchmarks.
“Break the curse of multilinguality”: adding non-English data no longer harms English performance when training is scaled appropriately.

The curse persists when:

Seen pairs are not scaled (Worldwide 1.0×), or
The model is smaller (ViT-L/14), even with more worldwide data (2.3×).

Meta CLIP 2 (ViT-H/14, worldwide 2.3×) vs baselines:

Outperforms mSigLIP with fewer seen pairs (72% of mSigLIP) and lower resolution (224px vs 256px).
Surpasses mSigLIP on IN, SLIP 26, DC 37, and surpasses SigLIP 2 on SLIP 26 and DC 37.

Achieves new SoTA on many multilingual benchmarks, e.g.:

Babel-IN: +3.8% over prior best.
XM3600: +1.1% (T→I) / +1.5% (I→T).
CVQA: +3% (EN) / +7.6% (local).
Flickr30k-200: +7.7% (T→I) / +7.0% (I→T).
XTD-200: +6.4% (T→I) / +5.8% (I→T).

SigLIP 2, which heavily prioritizes English (90% English training data), underperforms mSigLIP on multilingual tasks and Meta CLIP 2 on most English benchmarks except ImageNet.

Ablation study of metadata and alt-texts combination on ViT-B/32.

Transitioning from English-only to worldwide metadata/curation (ViT-B/32, Worldwide 1.0×) shows:

Removing English filter on alt-texts (all alt-texts curated by English metadata): Slight drop on ImageNet (−0.6%), indicating that isolating English text/metadata by language before matching is important for English performance.
Merging all metadata without language separation: Further degrades English performance but begins to build multilingual capability.
Language-by-language curation with a single threshold (ten) across all languages: Lowers English performance because ten is too high for low-resource languages, letting head (high-resource) languages dominate curation.
Language-specific thresholds (tlang): Maintains a similar head-to-tail concept ratio per language. Improves both English and non-English performance, though the curse of multilinguality remains unresolved at this small model scale (ViT-B/32).

Ablation study of various multilingual tokenizers with ViT-B/32 and Worldwide 1.0×.

Swapping the English tokenizer for multilingual ones (ViT-B/32, Worldwide 1.0×) with minimal architectural changes:

XLM-V (900k vocab) yields the strongest overall performance:
Ties or matches best on ImageNet (64.7).
Best on Babel-IN (32.7).
Competitive on XM3600 and CVQA, with particularly strong local-language CVQA performance.

Paper

Meta CLIP 2: A Worldwide Scaling Recipe 2507.22062

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on January 15, 2026.

Canonical link

Exported from Medium on May 4, 2026.
