# Papers Explained 218: Idefics 3

Papers Explained 218: Idefics 3

Papers Explained 218: Idefics 3

This paper can be seen as a tutorial for building a VLM. It begins by providing a comprehensive overview of the current state-of-the-art…

Papers Explained 218: Idefics 3

This paper can be seen as a tutorial for building a VLM. It begins by providing a comprehensive overview of the current state-of-the-art approaches, highlighting the strengths and weaknesses of each, addressing the major challenges in the field, and suggesting promising research directions for under explored areas. It then walks through the practical steps to build Idefics3–8B

The model is available at HuggingFace.

Recommended Reading [Papers Explained 180: Idefics 2]

Analyzing architectural choices and Training Methods in VLMs

Connecting unimodal pre-trained models

Most VLMs have been built on top of unimodal pre-trained backbones, a language model and/or a vision encoder, rather than training entirely new models from scratch. These two pre-trained models are usually connected with either a cross-attention or a self-attention architecture.

Cross-attention architecture

The cross-attention architecture is introduced in Flamingo. The image hidden states encoded by the vision backbone are used to condition the frozen language model using freshly initialized cross-attention layers that are interleaved between the pretrained language model layers. The keys and values in these layers are obtained from the vision features, while the queries are derived from the language inputs. In practice, a cross-attention block is inserted after every four Transformer blocks in the LLM, adding newly initialized parameters equivalent to roughly 1/4th of the LLM’s size. This significant increase in parameters enhances the model’s expressivity, allowing it to achieve strong performance without unfreezing the LLM during training, thereby preserving the pre-trained LLM’s performance on text-only tasks.

Self-attention architecture
The self-attention, or fully-autoregressive, architecture.
In the self-attention architecture (or fully-autoregressive architecture), introduced in FROMAGe and BLIP2, the output of the vision encoder is treated as tokens and concatenated to the sequence of text tokens. The entire sequence is then passed as input to the language model. The sequence of visual tokens can be optionally pooled into a shorter sequence, making the model more efficient both during the training and at inference. The layers that map the vision-hidden space to the text-hidden space are referred to as modality projection layers. Most recent VLMs have now adopted this design.

Which architecture performs best?

The cross-attention architecture significantly outperforms when the backbones are kept frozen during training. However, when parts of the vision encoder and language model are trained with LoRA, adding an extra 200M trainable parameters distributed across both models, the cross-attention architecture performs worse despite having more parameters overall.

Is a vision encoder really necessary?

Instead of employing a vision encoder, Fuyu feeds image patches directly into the language model after applying a simple linear projection to adjust the dimensions. This architecture offers two main advantages: it is independent of another pre-trained model and preserves all the information from the original image. The original image details might be necessary for accurately responding to the promp, a pre-trained vision encoder transforms an image into a representation that is independent of the user’s prompt. As a result, vision encoders aim to capture as much information as possible and can still miss details pertinent to the prompt.

Despite these advantages, this architecture has not yet demonstrated superior performance. Fuyu scores significantly lower on benchmarks compared to the best models of similar size released around the same time.

How should we connect the vision encoder to the language model?

Many models, such as FROMAGe and LLaVA (Liu et al., 2023), use a simple linear layer between the vision encoder and the LLM, ensuring that all encoded visual information is retained since no pooling strategy is applied. However, this approach results in a long sequence of visual tokens, making training and inference less efficient. To address this, Qwen-VL reduces the number of visual tokens by using a single-layer cross-attention module between a group of embeddings and the image hidden states.

The image-splitting strategy: a trick to increase the number of visual tokens

Introduced in UReader and SPHINX, the image splitting strategy involves dividing an original image into multiple sub-images, each of which is encoded separately by the vision encoder.

When the number of tiles is based on the original resolution, the model is trained with varying numbers of visual tokens. This approach is particularly advantageous during inference: for simpler tasks, fewer visual tokens are needed, saving computational resources, while more computing can be allocated by increasing the image resolution for tasks that require intensive OCR.

Most vision encoders are designed for relatively low, fixed image resolutions and are not well-suited for processing large images. The image-splitting strategy addresses this by enabling the use of off-the-shelf pre-trained vision encoders at their original resolution, simply by feeding multiple smaller sub-images to the encoder instead of the original large image.

However, since the tiles of an image are not independent, encoding each one separately can be suboptimal and may result in a loss of global context. To address this, the current strategy involves adding the downscaled original image to the list of tiles, resizing it to match the resolution supported by the vision encoder.

Can we do better than the image-splitting strategy?

An alternative to the image-splitting strategy and a promising direction for future research is to develop a vision encoder that can natively process images of varying resolutions, including very large ones, without changing the original aspect ratios, potentially incorporating a mechanism for handling long-context efficiently. This model could be trained efficiently using the Patch’n’Pack strategy at a different number of visual tokens per image based on the original resolution, enabling the entire image to be encoded directly without the need to crop it into multiple sub-images.

Training methods and datasets for VLMs
The different stages of training and the types of datasets used.
Training VLMs typically occurs in multiple stages, primarily due to (a) the limited availability of high-quality data at scale, (b) memory constraints for efficient training, and © stability issues. During these stages, progressively higher-quality data is introduced, the maximum image resolution is gradually increased, and more model parts are unfrozen.

Challenges in evaluating VLMs on Open-ended and multiple-choice benchmarks

The earliest and most popular multimodal benchmarks rely on specific ground-truth answers for each question, so even minor variations in the model’s responses can lead to a score marked as incorrect.

This method of evaluation tends to favor models that produce answers closely aligned with the benchmark’s expected format or writing style.

One potential way to mitigate this bias is to perform few-shot evaluations, although this approach is less effective than training on the benchmark training set, and is not currently used for evaluating instruct models.

Recently proposed, the LAVE metric consists of asking an LLM to evaluate whether the response generated by the VLM is correct, given the ground truth and the specific question, thereby reducing the template problem.

Another way to reduce ambiguity is to use benchmarks that include multiple-choice questions (MCQs), where the model selects the correct option by choosing the corresponding letter.

Challenges in model evaluation during the pre-training stage

There is a significant discrepancy between the performance of VLMs at the pre-training stage versus after fine-tuning. One reason for this gap is that the model only starts learning the specific task of visual question answering (beyond just image captioning or text transcription) during the fine-tuning stage — unless a third pre-training stage is conducted using large synthetic VQA datasets.

When instruction data is omitted during pre-training, more complex tasks like document understanding may perform poorly, and the impact of development choices in the VLM may only become evident after fine-tuning, leading to a delayed feedback loop, making pre-training ablations misleading.

Therefore, to obtain more accurate insights during pre-training ablations, we recommend incorporating instruction data into the data mixture.

Idefics3

Idefics3 is based on Llama 3.1 and SigLIP-SO400M.

Dataset preparation

Extending The Cauldron:

The Cauldron is a collection of 50 high-quality datasets from existing literature. This collection is expanded by adding 6 more datasets: Cord- v27 for training models to output information in JSON format, LNQA for large-scale real-world visual question answering, ShareGPT-4o and IIW-400 for generating detailed captions, Geo170K for tasks involving geometry, and Docmatix for document understanding.

Enhancing document understanding capabilities with Docmatix:
Overview of the pipeline used for the creation of Docmatix.
Document understanding is a critical business application for VLMs. Yet, only a few open-source datasets are available for boosting the performance of models in this area, and they typically include only a limited number of examples. However generating high-quality synthetic data for this task is relatively straightforward if we reframe the problem as one of LLM-based data generation rather than relying solely on VLMs. Standard OCR tools can accurately extract text from PDF documents, and an LLM can then be used to generate QA pairs based on this text.

Text transcriptions from the English PDFA dataset are used to generate QA pairs with Phi-3-small. To ensure diverse outputs, five different prompts are employed. To maintain dataset quality, results are filtered, by using regular expressions to detect code and removing answers containing the keyword “unanswerable.”

The resulting dataset, Docmatix, includes 2.4M images and 9.5M QA pairs derived from 1.3M PDF documents.

Architecture

Idefics3 uses SigLIP-SO400M for the vision encoder, and Llama 3.1 instruct as the language model.

The crucial difference lies in the connector between the vision and language models. Idefics3 uses pixel shuffle strategy that reduces the number of visual tokens to 169 by encoding images up to 364x364 pixels.

To maintain 2D image structure information, a newline character (‘\n’) is inserted after each row of tiles. The original downscaled image (364x364 pixels) is appended to the sequence to provide the complete image context. Each tile is prepended with textual tokens ‘<row_x_col_y>’ indicating its position in the matrix.

Training Details
The different training stages of Idefics3, along with the parameters and datasets used.
In the first pre-training stage, the model’s backbones remain frozen to preserve their performance while learning the newly initialized parameters. The maximum image resolution is gradually increased from 364x364 to 1820x1820. From the second stage onward, the backbones are trained using DoRA, and larger images are introduced into the training data. The final pre-training stage focuses on training with large synthetic datasets. During the supervised fine-tuning phase, NEFTune noise is applied to the inputs and the loss is calculated only on the answer tokens.

Evaluation

Idefics3 is evaluated on five benchmarks: MMMU, MathVista, MMStar, DocVQA, and TextVQA.
Performance of Idefics3 against Idefics2–8B and Idefics2–70B. The evaluations are done in zero shot and without any chain-of-thought prompting.Detailed performance of Idefics3 across each category of MMMU.
Idefics3 outperforms Idefics2 on most benchmarks, particularly in document understanding tasks (13.7 point improvement on DocVQA). This improvement is attributed to:

More visual tokens per image in Idefics3.
A third pre-training stage on high-quality synthetic datasets.
An improved language model backbone.

Despite these enhancements, scale remains important: Idefics2–70B still outperforms Idefics3 on the MMMU benchmark by 11.4 points, suggesting the need for larger models to fully capture the knowledge required for this task.

Paper

Building and better understanding vision-language models: insights and future directions 2408.12637

Recommended Reading [Multi Modal Transformers]

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on September 25, 2024.

Canonical link

Exported from Medium on May 4, 2026.
