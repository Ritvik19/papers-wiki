# Papers Explained: Extracting alignment data in open models

Papers Explained: Extracting alignment data in open models

Papers Explained: Extracting alignment data in open models

This work hypothesizes that since the chat template is exclusively introduced in post-training, if the model is prompted with the template…

Papers Explained 491: Extracting alignment data in open models

This work hypothesizes that since the chat template is exclusively introduced in post-training, if the model is prompted with the template, it will generate alignment data.

The model is prompted with the chat template and sample. This is repeated a number of times to generate a set of synthetic data points. For each synthetic data point, the closest sample in the post-training dataset is found according to embedding similarity, using an embedding model.

The synthetic data points are found to be from the same distribution as the alignment dataset.

Extracting alignment data

The proposed extraction strategy is based on the observation that certain prompts seem to consistently induce the model into outputting alignment-like data. To enable the attack, special tokens from the chat template are used that are precisely introduced during post-training, making them ideal artifacts that can be leveraged to extract specific types of data. The main contribution is confirming that many of such generations are either exact copies or very close to true training samples under an appropriate measure of similarity.
An overview of the data extraction process.
The pipeline functions as follows: the entire post-training set is embedded using an embedding model, constructing a vector search engine. A number of samples are then generated simply by prompting the model using a chosen prefix repeatedly. For each generated sample, it is embedded and searched against the vector database to retrieve the best match and its score. The study focuses on OLMo 2 for SFT and Open-Reasoner-Zero for RL.

The observation that chat templates can be used to generate useful synthetic data has been pointed out already, where special prompts and a filtering pipeline are used to generate a dataset that can be used to post-train models using SFT. This work studies this from a different angle and aims to understand the extent to which the generations correspond to reproduced training data. The data generated might have been training data.

A central theme is the wish to broaden the definition of memorization beyond simple string matching, due to its natural limitations. The usefulness of extracted samples as training points is of interest; if two samples are semantically equivalent, then they reasonably should be treated equal as training samples. The gemini-embedding-001 model is used to generate a single embedding for each sample, removing all special tokens and therefore only considering the plain text. This acts as a vector search engine, where similarity with respect to each training sample can be computed using a single matrix multiplication and taking the argmax. A threshold of 0.95 for neural embeddings was chosen as a more conservative choice.

Large scale extraction of SFT data

The study focuses on OLMo 2. The uncompressed pre-training mix has a size of 22.4 TB while the higher quality mid-training split has a size of 5.14 TB. The post-training is divided into 3 stages: an SFT stage with a dataset containing 939k samples, then a Direct Preference Optimisation step with 378k samples, and finally an RL with Verifiable Rewards (RLVR) step with 29.9k samples. SFT training samples are embedded using gemini-embedding-001 by concatenating the question and answer sequences as a single block of text. To extract the data from the model, conditioning is generated on the following initial tokens <|endoftext|><|user|>, which are the starting tokens of the chat template. The temperature is left at the default value of 1.

The memorisation is evaluated using traditional string matching metrics. 100k generations for OLMo 2 13B are considered using the extraction method and their closest match is searched for in the post-training set, with respect to different similarity measures.

The normalised Levenshtein similarity is defined as 1−Levenshtein(𝐴,𝐵)/max(len(A),len(B))
The normalised Indel similarity is defined as 1−Indel(𝐴,𝐵)/(len(A) +len(B)). The Indel similarity is related to the Levenshtein distance, but applies a cost of 2 to substitutions.

For each generated sample, the highest similarity based on the two string matching methods in the post-training set is found.

When judging memorization rates based on string matching scores, memorization rates seem negligible. This however does not paint the entire picture.

String matching results are compared to matching done using neural embeddings. 1 million samples are generated with OLMo 13B using the same method and embedded using gemini-embedding-001. String matching distances are not well-aligned with semantic memorisation and also seem to exhibit a strong string length bias, where longer generations are consistently given lower Levenshtein similarity scores. Neural embeddings are much better.

Some samples are much more memorised than others. It is hard to understand exactly why, but investigations revealed that samples are much more likely to be memorised if similar samples are also present in the pre and mid training datasets.

Direct distillation on extracted data

To explore that “if the generated data is similar to the original post-training dataset, can it be used to post-train a model directly”, Post-training is conducted using SFT OLMo 2 7B in two ways:

the original dataset in order to reproduce the original results
a generated dataset of a similar size of ≈930k samples

Even though the number of samples is the same, the original SFT training is over ≈1.3B tokens, while the synthetic training set has only ≈850M tokens as the filtered generations remain shorter.
Model performance after SFT on the benchmarks considered by OLMo.
The model trained on synthetic data also achieves comparable performance on the benchmarks, except for the IFE task. It is suspected that the pipeline generates too few examples that target this benchmark.

Large scale extraction of RL data

The Open-Reasoner-Zero model is used, which was trained from the Qwen2.5 base model with PPO using post-training data that is publicly available. With RL, the training samples consist of questions and answers, but the reasoning traces are not part of the training dataset as they are artifacts of the training rollout. For this reason, the focus is on the extraction of the questions and answer part of the dataset although note that reasoning traces can be useful in their own right. The model is prompted by again taking the first part of the chat template specified by the developers of the model and generate 100k samples independently. It is found that the model very consistently generates a question, followed by a thinking trace, and finally an answer. The training set was then searched for these generations. A number of training samples were again found being regurgitated verbatim. The fact that models are capable of regurgitating RL training samples is found to be counterintuitive as the PPO objective, at least at a glance, seems rather misaligned with the memorisation of training samples, especially when compared to methods such as SFT that instead very explicitly increase sequence likelihoods.

This phenomenon is explored further by measuring the likelihoods of each PPO training sample question under the Qwen 2.5 base model and the Open-Reasoner-Zero model. If the RL process induces memorisation, then the likelihood using the post-trained model would increase on the training samples.
Count of training samples (prompt only) with likelihood above a certain threshold before and after RL.
The results show that RL training induces many of the training prompts to increase in likelihood.

RL on extracted dataset

Starting with the Qwen2.5 7B base model, post-training is conducted using Dr. GRPO and the ORZ 57k dataset. The resulting post-trained model is termed ‘Baseline’. Next, 100k samples are generated using the method and processed with Gemini 2.5 to filter out invalid, incomplete, or incorrect samples. From this set, 57k synthetic samples are randomly selected to create synthetic training data. This synthetic data is then used to post-train the Qwen2.5 7B base model.
RL training using the ORZ dataset and a dataset that was extracted.
The model trained on the synthetic data extracted from the ‘Baseline’ achieves comparable performance on the benchmarks.

Paper

Extracting alignment data in open models 2510.18554

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on November 13, 2025.

Canonical link

Exported from Medium on May 4, 2026.
