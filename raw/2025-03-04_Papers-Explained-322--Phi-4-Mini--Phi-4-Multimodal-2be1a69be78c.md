# Papers Explained 322: Phi 4 Mini, Phi 4 Multimodal

Papers Explained 322: Phi 4 Mini, Phi 4 Multimodal

Papers Explained 322: Phi 4 Mini, Phi 4 Multimodal

A 3.8B parameter language model excelling in math and coding, utilizing high-quality web and synthetic data, and featuring a 200K token…

Papers Explained 322: Phi 4 Mini, Phi 4 Multimodal

A 3.8B parameter language model excelling in math and coding, utilizing high-quality web and synthetic data, and featuring a 200K token vocabulary and group query attention.

Extends Phi-4-Mini with vision and speech/audio modalities via a novel “mixture of LoRAs” approach, enabling combined modality inference without interference and achieving state-of-the-art performance in various multimodal tasks while maintaining the base language model’s capabilities.

Phi-4-Mini is a 3.8B parameter language model trained on high-quality web and synthetic data, significantly outperforming recent open-source models of similar size and matching the performance of models twice its size on math and coding tasks requiring complex reasoning.

Phi-4-Multimodal is a multimodal model that integrates text, vision, and speech/audio input modalities into a single model. Its novel modality extension approach leverages LoRA adapters and modality-specific routers to allow multiple inference modes combining various modalities without interference. Phi-4-Multimodal supports scenarios involving (vision + language), (vision + speech), and (speech/audio) inputs, outperforming larger vision-language and speech-language models on a wide range of tasks.

Model architecture

Phi-4-Mini and Phi-4-Multimodal share the same language model backbone. Phi-4-Mini consists of 32 Transformer layers with a hidden state size of 3,072 and tied input/output embedding which reduces the memory consumption significantly while providing much wider coverage of vocabularies compared to Phi-3.5. Each Transformer block includes an attention mechanism based on Group Query Attention (GQA) which optimizes key and value memory (KV cache) usage for long-context generation. Specifically, the model employs 24 query heads and 8 key/value heads, reducing KV cache consumption to one-third of its standard size. Additionally, in the RoPE configuration, a fractional RoPE dimension is used, ensuring that 25% of the attention head dimension remains position-agnostic. This design supports smoother handling of longer contexts. Phi-4-Mini models use the tokenizer o200k base tiktoken with a vocabulary size of 200,064 intended to support multilingual and multimodal input and output more efficiently.
A overview of the Multimodal architecture for Phi-4-Multimodal.
In order to enable modality-specific functionality, multimodal models generally require fine-tuning the base language model, which often diminishes its original language capabilities. To address this, LLama- Vision adopts a strategy inspired by Flamingo, adding extra cross-attention layers while preserving the core language model. However, this approach will result in reduced performance on vision-language benchmarks compared to fully fine-tuned models. To fill the performance gap, NVLM further explores a hybrid framework, employing joint supervised fine-tuning with high-quality text SFT data. Yet, this approach only examines limited language benchmarks and does not address additional training stages often required after SFT. A mixture of LoRAs design is adopted for the Phi-4-Multimodal architecture to support variant multi-modality use cases. Different LoRAs are trained to handle interactions between different modalities.

Vision modality

The vision modality is implemented with an image encoder, a projector to align the vision and text embeddings and a LoRA adapter. The vision encoder is based on SigLIP-400M that is finetuned with LLM2CLIP on large scale image-text pairs with resolution 448 × 448 . The projector is a 2-layer MLP that maps the vision features dimension to the text embedding dimension. Extra LoRA is added on all the linear layers in the language decoder and only deployed in the supervised fine tuning (SFT) stage. The image encoder and projector introduce 440M model parameters while the vision adapter LoRA_V consumes another 370M model parameters.

In order to enable the model to process images with diverse resolution effectively and efficiently, a new dynamic multi-crop strategy is proposed. Specifically, given a target image, the crop number for each side is computed by dividing the original size by the crop-size, i.e. ⌈ H/C ⌉ × ⌈ W/C ⌉, here H, W, C are the image height, width and crop size respectively. If the total crop number is within the maximum number, i.e., 16 in the pretraining stage and 36 in SFT, the image is slightly resized to let it fit the size given by the computed image crops. Otherwise, the crop number is found by matching the best aspect ratio.

Speech and Audio Modality

The speech/audio inputs used are 80-dim log-Mel filter-bank features with the frame rate of 10ms. To enable Phi-4-Multimodal speech and audio functions, a pre-trained audio encoder and Phi-4-Mini are connected through an audio adapter. In addition, LoRA is applied on the language decoder to improve the performance of speech/audio benchmarks while preserving the text capability. The introduced modules for the speech/audio modality include:

An audio encoder, which consists of 3 convolution layers and 24 conformer blocks with 1024 attention dimensions, 1536 feed-forward dimensions, and 16 attention heads. The convolution layers contribute to a sub-sampling rate of 8, and thus 80ms token rate for the language decoder.
An audio projector, which is a 2-layer MLP that maps the 1024-dim speech features to the text embedding space of 3072 dimensions, similar to the vision projector.
LoRA_A has been applied to all attention and MLP layers in Phi-4-Mini with a rank of 320. The audio encoder and projector introduce 460M parameters while LoRA_A consumes another 460M parameters.

Note that the speech token rate is 80ms, indicating 750 tokens for 1-minute audio.

Training Pipeline

Vision Training

Vision training follows a four-stage process:

Projector Alignment stage: initially, only the projector is trained using caption data to align vision and text embeddings while preserving the pretrained representation of the vision encoder.
Joint Vision Training stage: Next, the projector and vision encoder are jointly trained on the full vision pretraining dataset to enhance key vision capabilities, such as OCR and dense understanding.
Generative Vision- Language Training stage: LoRA is then deployed on the language decoder and trained alongside the vision encoder and projector using curated single-frame SFT data, equipping the model with generative capabilities for vision-language inputs.
Multi-Frame Training stage: Finally, the model is trained on multi-frame SFT data with the vision encoder frozen, extending the context length coverage to 64k and enabling multi-image and temporal understanding.

Speech and Audio Training

A two-stage paradigm for speech and audio training, known as speech/audio pre-training and post-training, is used. In the pre-training stage, large-scale automatic speech recognition (ASR) data aligns the audio encoder and Phi-4-Mini in the semantic space. During this stage, the encoder and projector are updated while the language decoder is frozen. The audio encoder is initialized with a pre-trained encoder from the attention-based encoder decoder (AED) ASR model.

After the pre-training stage, the model can only perform the ASR task. To unlock the instruction following capability of Phi-4-Multimodal for a variety of speech and audio tasks, the model is continued to be trained with about 100M curated speech and audio SFT samples (after weighted up) as the speech post-training stage.

In speech/audio post-training, the audio encoder is frozen. The audio projector and LoRA_A are updated for another 50k steps. Different maximum audio lengths are considered for different tasks in post-training. For the speech summarization task, training is conducted up to 30-minute audio (22.5k tokens). For other tasks, the maximum audio exposed in training is 30s (375 tokens).

Vision-speech Joint Training

Vision-speech joint training is conducted after vision post-training and speech post-training. The language base model, audio encoder, and audio projector are frozen, while the vision adapter LoRA_V, vision encoder, and the vision projector are finetuned. In this stage, the model is trained mainly on vision-speech SFT data but a mixture of language and vision post-training data is also included to maintain the corresponding performance.

Reasoning Training

A pre-training phase is conducted on extensive reasoning data to capture general reasoning chains, followed by careful fine-tuning on curated SFT or preference data. The continued training of Phi-4-Mini for reasoning proceeds in three distinct stages.

First, building on Phi-4-Mini, the model is pre-trained on approximately 60 billion reasoning CoT tokens generated by frontier reasoning LLMs. Rejection sampling is then employed to filter out incorrect outputs, allowing the reasoning extension of Phi-4-Mini to learn the reasoning chains produced by these models.
In the second stage, the model is fine-tuned on a smaller but carefully curated dataset of around 200K high-quality CoT samples, chosen to cover diverse domains and varying difficulty levels.
Finally, in the third stage, filtered incorrect outputs are labeled as “dis-preferred” and their corrected counterparts as ‘preferred’, compiling a new dataset of 300K preference samples for DPO training.

Language training data

Pre-training data

A 5 trillion pre-training data corpus is built, which is larger and of higher quality compared to Phi-3.5-Mini.

Post-training data

Phi-4-Mini includes a significantly larger and more diverse set of function calling and summarization data compared to Phi-3.5-Mini. Additionally, a substantial amount of instruction-following data is synthesized to enhance the model’s instruction-following capabilities. For coding, extensive code completion data is incorporated, including tasks that require the model to generate missing code in the middle of an existing code snippet.

Reasoning training data

A large volume of synthetic chain-of-thought (CoT) data is generated from larger reasoning models, covering diverse domains and difficulty levels. During sampling, rule-based and model-based rejection methods are employed to discard incorrect generations and feed them back for resampling. This data has been utilized exclusively for the experimental reasoning model and has not been applied to the officially released checkpoint Phi-4-Mini.

Vision-language training data

The Phi-4-Multimodal model’s pre-training phase involves a rich and varied dataset, encompassing interleaved image-text documents, image-text pairs, image grounding data, synthetic datasets from OCR of PDFs and realistic images, and synthesized datasets for chart comprehension.

The pre-training process involves a total of 0.5T tokens, combining both visual and textual elements. Additionally, the maximum image resolution is capped at 1344x1344, as most training images are smaller than this size.

For supervised fine-tuning (SFT), a combination of a text SFT dataset, publicly available multimodal instruction tuning datasets, and large-scale in-house multimodal instruction tuning datasets is utilized. These datasets span diverse domains and tasks, including general natural image understanding, chart, table, and diagram comprehension and reasoning, PowerPoint analysis, OCR, multi-image comparison, video summarization, and model safety.

Collectively, the multimodal SFT data comprises approximately 0.3T tokens.

Vision-speech training data

The Phi-4-Multimodal model is trained on a diverse set of synthetic vision-speech data, covering single-frame and multi-frame scenarios. A subset of vision-language SFT data is reused and an in-house text-to-speech (TTS) engine is run to convert the user queries from texts to audios.

The quality of the synthetic speech is measured by transcribing the audio with an in-house ASR model and calculating the word error rate (WER) between the original text and transcription. The final vision-speech data is generated with the WER-based filtering to ensure the quality.

Speech and Audio Training Data

Pre-training Data

To pre-train the adapter and reduce the modality gap between the speech and text sequences, a dataset of approximately 2M hours of anonymized in-house speech-text pairs with strong/weak ASR supervisions was curated. This dataset covers the eight supported languages: Chinese, English, French, German, Italian, Japanese, Portuguese, and Spanish.

Post-training Data

Both real and synthetic speech/audio data are used during speech post-training, covering the majority of speech and audio understanding tasks.

Speech Recognition Data: ASR training data contains about 20k hours anonymized in-house, and 20k hours selected public transcribed speech recordings that span eight languages. The weighted ASR training data contributes to 28M SFT examples.

Speech Translation Data: AST training data contains about 30K hours of anonymized in-house and public speech data with translations in two directions: from 7 languages to English and from English to 7 languages. This data contains both supervised and synthetic translation from a machine translation model. The AST data is created with two formats: direct ST and ASR + translation in a Chain-of- Thoughts (CoT) manner, contributing to 28M weighted training examples in post-training.

Speech and Spoken Query Question Answering Data: SQA and SQQA training data contain synthetic QA pairs from real speech and synthetic audio from text SFT data.

Synthetic QA pairs for SQA: To enable SQA capability, we reuse the speech-transcript pairs in the ASR training data and prompt the language model to generate multiple text QA pairs for each transcript. The low-quality QA pairs are filtered during training.
Synthetic spoken query (audio) for SQQA: SQA is tasked to respond to speech context plus text query. Responding to spoken query directly is also an important capability for Phi-4-Multimodal. Consequently, samples are taken from the language post-training data and the text query is converted to an audio query using an internal zero-shot TTS system.
Synthetic LM response for SQQA: Synthetically generated responses for speech prompts are created by prompting the language model with the ASR transcripts of those prompts. The LM response data can improve the SQQA robustness of Phi-4-Multimodal in real scenarios because of more diverse spoken queries sampled from the ASR training data.

The total SQA and SQAQA data contribute to 26M weighted SFT examples.

Speech Summarization Data: The summarization training data is assembled from anonymized audio recordings paired with their transcripts. The audio consists of multi-speaker conversational speech that spans a range of topics. To construct query-summary pairs for each audio clip, GPT-4 generates a variety of queries and their respective summaries based on the transcripts. For each audio clip, the summarization queries address specific or general aspects of the conversation and vary in format, including length (number of words or sentences) and structure (summaries formatted as bullet points, JSON, or email). The weighted dataset contributes to 1M SFT examples with English speech only.

Audio Understanding Data: The audio understanding data contributes to around 17 million weighted SFT examples sourced from public. The dataset is created in the form of (audio, question, answer) tuples, where “audio” contains speech, audio, and music inputs. The question and answer pairs are generated from GPT4 based on audio transcripts and/or meta information.

Evaluation

Language benchmarks

Phi-4-Mini language benchmark scores.

Phi-4-Mini demonstrates strong overall performance across diverse language understanding benchmarks, often outperforming similarly sized models and matching or exceeding the performance of models twice its size.
Phi-4-Mini excels in math and reasoning tasks, attributed to its training on reasoning-rich synthetic data. It significantly outperforms similar-sized models and even some larger models on math benchmarks.
Phi-4-Mini shows substantial improvement over its predecessor (Phi-3.5-Mini) in instruction following and function calling, likely due to improved data curation and post-training processes.

Phi-4-Mini coding performance comparison.

Phi-4-Mini exhibits strong coding performance, outperforming most models of similar and larger sizes on coding benchmarks. This is attributed to the inclusion of high-quality organic and synthetic code data during training.

CoT Reasoning results of reasoning-enhanced Phi-4-Mini.

A reasoning-enhanced version of Phi-4-Mini achieves comparable performance to larger reasoning models, even with significantly fewer parameters.

Vision Benchmarks

Comparison results on public vision-language benchmarksComparison results on public vision-speech benchmarks.

Phi-4-Multimodal shows significant improvements over Phi-3.5-Vision and outperforms similar-sized open-source models on vision-language benchmarks.
Phi-4-Multimodal surpasses some closed-source models (Gemini, GPT-4o) on chart understanding and science reasoning tasks.
Phi-4-Multimodal significantly outperforms larger models like InternOmni and Gemini-2.0-Flash on vision-speech benchmarks, achieving a >10 point improvement on some (ShareGPT4o AI2D, ShareGPT4o ChartQA).
Phi-4-Multimodal maintains language performance for pure text input by using fine-tunable LoRA modules and keeping the base language model frozen, unlike other models that fully fine-tune and experience language performance degradation.

Speech and Audio Benchmarks

Main Results on the speech benchmarks.Detailed results on ASR benchmarks, with CER (↓) for JA and ZH, and WER (↓) for other
languages.Detailed results on AST benchmarks with BLEU (↑) score reported.Result details on speech QA/summarization/audio understanding tasks for multi-modal models.

Strong ASR and AST Performance: Phi-4-Multimodal outperforms expert ASR and AST models (WhisperV3, SeamlessM4T-large-v2) on several datasets (CommonVoice, FLEURS, OpenASR, CoVoST2).
Leading OpenASR Performance: Achieved top ranking on the Huggingface OpenASR leaderboard with a 5.5% relative WER improvement over the previous best model.
Open-Source Speech Summarization Capability: First open-sourced model with this capability, demonstrating quality close to GPT-4o in terms of adherence and low hallucinations.
Efficient Multi-modal Performance: Outperforms Qwen2-audio, a model twice its size, on several tasks.
Optimized for Speech/Audio Understanding: Excels in ASR and AST compared to Gemini and GPT-4o, which are potentially more optimized for chat experiences. Shows a performance gap in SQQA tasks.
CoT Benefit for AST: CoT prompting significantly improves AST performance.
Language Agnostic ASR: Successfully recognizes target language without explicit language information in the prompt, unlike some other models.
Competitive Speech Summarization: Shows competitive performance against Gemini-2.0-Flash and GPT-4o on Golden3 and AMI datasets, despite limited training data for summarization.
Strong Audio Understanding: Achieves strong performance in audio and music understanding on AIRBench-chat and MMAU, outperforming Qwen2-audio.

Paper

Phi-4-Mini Technical Report: Compact yet Powerful Multimodal
Language Models via Mixture-of-LoRAs

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on March 4, 2025.

Canonical link

Exported from Medium on May 4, 2026.
