# Papers Explained 575: Gemini Embedding 2

Papers Explained 575: Gemini Embedding 2

Papers Explained 575: Gemini Embedding 2

Gemini Embedding 2 is a native multimodal embedding model that allows embedding video, audio, image, and text modalities in a unified…

Papers Explained 575: Gemini Embedding 2

Gemini Embedding 2 is a native multimodal embedding model that allows embedding video, audio, image, and text modalities in a unified representation space. It leverages the multimodal capabilities of Gemini to produce embeddings for arbitrary combinations of interleaved inputs across all these modalities that generalize well across a wide variety of tasks.

Model Architecture

The embedding model is initialized from Gemini and further fine-tuned with task-specific, modality specific, and cross-modality training. This allows Gemini Embedding 2 to build representations on top of the vast knowledge already present in the Gemini parameters.

After tokenization, an input sequence T of 𝐿 tokens is processed by M, a transformer with bidirectional attention initialized from Gemini, producing a sequence of token embeddings T_embed = M (T)

To generate a single embedding representing all the information in the input, a pooler P is applied, P_embed = P(T_embed)

Finally, a randomly initialized linear projection f is applied to scale the embedding to the target dimension, E = f (P_embed)
Conceptual overview of the Gemini Embedding 2 workflow.
Training Objective

Gemini Embedding 2 model is trained with a noise-contrastive estimation (NCE) loss with in-batch negatives

The exact loss differs slightly depending on the task being trained. In general, a training example includes a query 𝑞𝑖, a positive target 𝑝+ 𝑖 and (optionally) a hard negative target 𝑝− 𝑖. In text-only training tasks, each example also has a prescribed task string 𝑡, for example “question answering” or “fact checking”, describing the nature of the task. During training, the task string 𝑡 is randomly dropped off to augment the robustness of the model to different modality inputs where the task strings are not used.

Given a batch of size 𝐵 the loss applied to these embeddings is as follows:

where sim(x, y) is cosine similarity, and

This masking term is particularly relevant for classification tasks, where the number of targets (labels) is small. It should be noted that the second term in the denominator is omitted if no hard negatives are provided.

In order to support different dimensions of embeddings with a single model, the above loss is adapted using MRL into 𝑘 separate losses across 𝑘 overlapping sub-dimensions of the embedding dimensions.

Gemini Embedding 2 provides 𝑑 = 3,072 dimensional embeddings, with the MRL support optimized for 768 and 1,536 dimensions.

Recipe

Pre-Fine-Tuning (PFT): To adapt the parameters in the model from auto-regressive generation to encoding, this stage uses as training a large number of potentially noisy query–target pairs in a multi-task setup. Further, in this stage it is beneficial to use large batch sizes which provide more stable gradients, mitigating the impact of the noisy inputs. During this stage, only image, text and code tasks are used.

Fine-Tuning (FT): The fine-tuning stage for this model is based on training with a large number of text, code, document, image, audio, and video tasks. For this training stage it is beneficial to tune batch sizes for each task to improve quality on corresponding evaluations. In this stage examples are also sampled from one single task to build the training batches. The alignment between modalities is based on training multiple single-modality batches as well as cross-modality ones.

Model Soup: To systematize the combination of different checkpoints and obtain additional generalization performance across the different modalities, the parameters obtained from individual fine-tuning runs are averaged.

Evaluation
Comparison of embedding models on retrieval benchmarks.
Gemini Embedding 2 leads on global mean scores for unimodal image, text-to-image, image-to-text, and text-to-video tasks, showing particularly strong performance in challenging long-caption benchmarks (DOCCI, TextCaps)
Demonstrates robust generalization to third-party evaluation tasks despite not having specific in-domain training splits.
On ViDoRe Benchmark V2: Achieves a document retrieval score of 64.9, outperforming Amazon Nova MME (60.6) and close to Voyage-3.5-multimodal (65.5), with support across the full Video/Audio/Image/Text modalities.
Comparison of multimodal and text-only embedding models on the MTEB, MTEB(Multilingual), MTEB Code v1, and CoIR benchmarks.
Outperforms other multimodal models on text-only tasks, demonstrating that expanded multimodal capabilities do not compromise text understanding.
Surpasses its own earlier (text-only) Gemini Embedding model with a higher mean task score (69.9 vs. 68.32).
Sets new state-of-the-art results in code retrieval benchmarks, outperforming both text-only and domain-specific models such as voyage-code-3.
Results on the passage retrieval split of the MSEB benchmark.
Processing native audio inputs (without intermediate transcription) achieves higher retrieval performance (average mrr@10 of 73.99 vs. 70.40 for ASR-based approach).
Direct audio encoding improves both intra-lingual (+2.0 points) and cross-lingual (+5.01 points) retrieval tasks, indicating deep semantic alignment and avoidance of error propagation seen in cascaded (ASR) approaches.
Gemini Embedding 2’s modality-agnostic latent space robustly models raw audio, consolidating a holistic representation that outperforms transcription-reliant bottlenecks.

Paper

Gemini Embedding 2: A Native Multimodal Embedding Model from Gemini

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on June 5, 2026.

Canonical link

Exported from Medium on June 13, 2026.
