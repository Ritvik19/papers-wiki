# Papers Explained 475: ModernVBERT

Papers Explained 475: ModernVBERT

Papers Explained 475: ModernVBERT

Multimodal embedding models are typically built by finetuning large vision–language decoders with contrastive losses on text–image pairs…

Papers Explained 475: ModernVBERT

Multimodal embedding models are typically built by finetuning large vision–language decoders with contrastive losses on text–image pairs. Through controlled experiments, key factors for improving visual document retrieval models are identified, including attention masking, image resolution, modality alignment data regimes, and late interaction centered contrastive objectives. Building on these insights, ModernVBERT, a compact 250M-parameter vision–language encoder, is released. ModernVBERT outperforms models up to 10 times larger when finetuned on document retrieval tasks.

The models are available at Huggingface.

Methodology

A central aspect of the study is the impact of causal and bidirectional attention masks, extending previous work on textual representations to the vision modality.

Language Model Checkpoints: The experiments utilize checkpoints from “Should we still pretrain encoders with masked language modeling?”, which are a series of identical 210M parameter transformer models based on the Llama architecture. These models were trained on 100B tokens and differ only in their attention masking strategy during language model training, ensuring identical training data, model size, architecture, etc.

enc: A bidirectional encoder trained with Masked Language Modeling (MLM).
dec: A causal decoder trained with next token prediction.
dec-enc: A causal decoder that was annealed at the end of its textual training by removing the causal mask and switching the training objective to MLM.

Vision Tower: For visual processing, siglip2-base-16b-512 is employed. This is an 86M parameter vision transformer contrastively trained on billions of text-image pairs.

All ablations are conducted under iso-data controlled setups, meaning they are further trained on the same data sequence, with identical batch sizes, optimizers, schedulers, and hardware.
MLM-based early fusion architecture.
The analysis is not centered around novel model architectures but aims to draw broadly applicable insights by designing vision-language models following current standard training practices.

Early Fusion Architecture: The study employs an early fusion architecture. In this setup, visual patch embeddings produced by the vision encoder are projected into the language model’s input embedding space and then concatenated with text token embeddings to encourage joint processing.
Dynamic Resolutions: To handle dynamic image resolutions, large images are split into 512x512 pixel patches, as expected by the SigLIP encoder. A downscaled version of the full image is also concatenated to improve inter-patch consistency and global visual understanding.
Information Compression: For sequences of large images, pixel shuffling with a ratio of r=4 is applied to compress information, following prior work on models of comparable size.

A standard biphasic training procedure is used, focusing on retrieval performance.

Modality Alignment: The first phase involves training a pretrained textual language model to understand visual inputs through language modeling objectives.
Contrastive Post-training: The second phase relies on text-image contrastive learning to learn efficient image representations.

Modality Alignment

The image embedding projection layer is trained to map visual features into the language model’s embedding space. The pretrained language model is also finetuned using LoRA, allowing both image and text models to adapt jointly while mitigating the risk of monomodal performance collapse.

For decoder-based models, training is done with Causal Language Modeling (CLM) loss on the text tokens, as standardly done in VLM modality alignment.

This training scheme is generalized to bidirectional encoder models by using the Masked Language Modeling (MLM) loss on the textual tokens.

Models are aligned on a large corpus primarily derived from The Cauldron 2 and Docmatix, the training mixture upsamples images containing text and documents of varying complexities, specifically targeting document-focused retrieval models the final data mixture is approximately 2 billion text tokens, including diverse sources like web pages, books, and scientific papers.

All models are trained using a masking ratio of 0.5 and user-prompt masking to avoid overfitting on chat-template format.

Contrastive Post Training

After the language model learns to process image tokens, this stage specializes the models to enhance the semantic representation of their output embeddings. The dataset for this stage comprises:

118 million document-query pairs from the ColPali corpus.
118 million natural image-description pairs from the MSCOCO train set

The InfoNCE loss is employed.

For general-domain post-training, the loss is computed symmetrically. For single-vector models, the last (EOS) token is used for causal models, and all sequence tokens are mean-pooled for bidirectional encoders. Alternatively, all document and query tokens are used without pooling for late interaction matching..

Ablation Evaluation Setup

The contrastively trained models are evaluated on retrieval and zero-shot classification tasks across multiple domains.

Document Retrieval Capabilities: ViDoRe and ViDoRe v2 using nDCG@5.
Generalist Image Retrieval Capabilities: Tasks selected from MIEB, MSCOCO retrieval, and Flickr30k retrieval.
General Classification Tasks: Classification accuracy is measured by fine tuning a logistic regression head on top of the model’s embedding on Stanford Cars and Food101. Zero-shot Performance is measured on FER2013 and EuroSAT.

What makes a Great Visual Retriever

Modality Alignment Design

Impact of Modality Alignment Objective
Impact of Modality Alignment objective on downstream tasks.
Natural Image Tasks: Early fusion VLMs severely underperform the dual encoder on natural image classification tasks. This suggests that high-level representation tasks do not benefit from the granular interactions between image and text tokens learned during the VLM modality alignment phase. Large-scale contrastive training, as used by SigLIP, remains superior for these tasks.
Document Retrieval Tasks: In contrast, early fusion VLMs achieve significant gains in document retrieval tasks (+10.9 nDCG@5 on ViDoRe and ViDoRe v2 datasets). This indicates that pairing a vision model with a language model enables token-level interactions that create richer document understanding, aiding specific tasks even with less contrastive post-training.

Scaling the Modality Alignment Phase for Better Token Representations
Modality alignment scaling of early fusion encoders for up to 1 epoch (3.5B tokens) of data.
The researchers tested whether scaling the modality alignment phase, known to improve generative abilities of VLMs, also benefits retrieval by contrastively finetuning encoder checkpoints during Masked Language Model (MLM) modality alignment.
Document Retrieval: Document retrieval performance consistently improves with more modality alignment data, largely surpassing the vision tower evaluated in isolation and showing clear scaling benefits.
Natural Image Tasks: Natural image tasks, however, plateau past 1 billion tokens of alignment data, remaining far from the standalone dual encoder baseline.
This demonstrates that document and natural image retrieval leverage different mechanisms and should not be optimized in the same way. Document retrieval benefits from learning fine-grained interactions between image and text tokens through the language model, while the language model has limited utility for high-level natural image tasks.

Bidirectional Attention Fully Unlocks Late Interaction
Impact of attention masks and training objectives on document retrieval performances.
Inspired by the effectiveness of bidirectional attention in text-only retrieval, the study investigated its impact on visual document retrieval, especially with multi-vector late interaction matching. They evaluated standard encoder (MLM) and decoder (CLM) models, as well as dec-enc and dec models modality aligned with MLM objectives.
Single-Vector Embedding Results: For document retrieval, single-vector embedding results are close between bidirectional and causal attention models, with the encoder (bidirectional) slightly outperforming the decoder (causal) by +1.6 nDCG@5.
Late Interaction Results: Bidirectional attention makes a huge difference in late interaction settings, substantially exceeding its causal counterpart by +10.6 nDCG@5.
Causal decoders are incapable of correctly contextualizing image or text token representations seen at the beginning of the sequences.
Most current visual retrievers, including late interaction variants, are causal models, suggesting a significant amount of performance is being left on the table. Furthermore, simply removing the causal attention mask during training is insufficient to recover the encoder’s late interaction performance, indicating that converting trained decoders into effective late interaction retrievers is highly non-trivial. Training encoder models from scratch is generally better for retrieval tasks.

Contrastive Training Design

Image Resolution Benefits are Task-Specific
Effect of image resolution on VL encoder abilities.
Modality alignment is performed at a fixed image resolution of 1024 x 1024 pixels.
Document Retrieval: Training with higher resolution inputs substantially improves results on visual document retrieval benchmarks. Additionally, adding a “cool-down” phase by exposing the model to higher-resolution images towards the end of the modality alignment phase yields further gains. This suggests models can adapt their attention mechanisms to finer details with increased resolution.
Natural Image Tasks: Interestingly, these benefits do not extend to natural image tasks, where increasing image resolution can even degrade performance.

Increasing the Pool of Contrastive Pairs
Impact of contrastive training mixtures on downstream tasks.
Current visual retrievers face a severe limitation due to the lack of large volumes of high-quality (document image, query) pairs. Existing datasets are often small and of varying quality. The study explored whether the abundance of text-only query-document pairs could improve visual retrieval via cross-modal capability transfer. They interleaved text-only pairs and text-image pairs throughout training at a 1:1 ratio, unlike prior work that “warms up” or trains exclusively with text-only pairs.
Results (Text-Only Pairs): Incorporating text-only pairs yielded a sizable improvement on visual document retrieval (+1.7 NDCG@5), indicating clear cross-modal transfer, likely facilitated by the backbone’s jointly learned text-image embedding space. This suggests that domain-specific training corpora can be assembled irrespective of native modality, reducing data collection costs.
Results (NatCap): Further evaluation with NatCap, a corpus of natural images paired with synthetic, highly detailed captions, improved downstream performance across the board. This was most notable on natural-image tasks, with a smaller but consistent gain on document retrieval (+0.2 NDCG@5).
These findings underscore the importance of scaling contrastive learning with high-quality data, which does not need to be exclusively image-document focused

Building a Small Yet Mighty Visual Retriever

Putting together the results from the experiments, a training recipe for a small visual document retriever ModernVBERT is devised.

It combines a state-of-the-art 150M text bidirectional encoder with the ModernBERT architecture and a small vision encoder SigLIP2–16B-512 of 100M parameters. Both models are modality aligned with a MLM objective for 10B tokens. To boost document understanding, the input image resolution is augmented from 1024px to 2048px during a modality alignment cooldown stage (2B tokens). The resulting model is called ModernVBERT.

The contrastive training mix is then scaled to combine document–query pairs with text-only pairs, and 1 hard negative is used for each document-query pair and 2 for each text-only pair. This results in ColModernVBERT, a compact late interaction model.

For reference, BiModernVBERT, a single-vector variant, is also trained.

Evaluation
Pareto efficiency.
ColModernVBERT demonstrates strong performance on visual document retrieval benchmarks, especially considering its size.
ViDoRe Leaderboard.
It performs competitively with much larger models (e.g., ColPali) despite having significantly fewer parameters.
It outperforms many larger single-vector repurposed VLM models.
It significantly outperforms a related smaller model, ColFlor.
It outperforms off-the-shelf dual encoders, even those with larger parameter counts.
It achieves a significant speedup on CPU compared to models with similar performance, making it suitable for practical text retrieval applications.

Paper

ModernVBERT: Towards Smaller Visual Document Retrievers 2510.01149

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on October 15, 2025.

Canonical link

Exported from Medium on May 4, 2026.
