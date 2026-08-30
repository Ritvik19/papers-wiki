# Papers Explained 105: Gemini 1.5 Pro

Papers Explained 105: Gemini 1.5 Pro

Papers Explained 105: Gemini 1.5 Pro

Gemini 1.5 Pro marks a significant milestone in the evolution of multi-modal mixture-of-experts models, pushing the boundaries of compute…

Papers Explained 105: Gemini 1.5 Pro

Gemini 1.5 Pro marks a significant milestone in the evolution of multi-modal mixture-of-experts models, pushing the boundaries of compute efficiency, reasoning, and long-context performance. It is designed to handle unprecedented context lengths, capable of processing and reasoning over millions of tokens from diverse modalities including text, video, and audio.

Recommended Reading [Papers Explained 80: Gemini 1.0]
Gemini 1.5 Pro compared to Gemini 1.0 family.
Model Architecture

Gemini 1.5 Pro is built upon a sparse mixture-of-experts Transformer based architecture, inheriting and enhancing the multimodal capabilities of its predecessor, Gemini 1.0. The MoE approach employs a learned routing function to direct inputs to a subset of the model’s parameters, enabling conditional computation. This architecture allows for the expansion of the model’s total parameter count while maintaining a constant number of activated parameters for any given input, ensuring its efficiency in serving.

This facilitates the model’s long-context understanding, enabling it to process inputs up to 10 million tokens in length. This capability translates to processing almost a day’s worth of audio recordings, the entirety of extensive literary works, substantial code-bases, or hours of video content in a single pass.

Training Infrastructure and Dataset

The training of Gemini 1.5 Pro leverages Google’s state-of-the-art TPUv4 accelerators, distributed across multiple data-centers, to handle the extensive computational demands of the model. The training dataset encompasses a wide variety of multimodal and multilingual data, sourced from web documents, code, images, audio, and video content. Furthermore, the model undergoes an instruction-tuning phase, complemented by further tuning based on human preference data, optimizing the model’s performance and alignment with human expectations.

Long Context Evaluation

Gemini 1.5 Pro achieves near-perfect “needle” recall (>99.7%) up to 1M tokens of “haystack” in all modalities, i.e., text, video and audio.
It maintains this recall performance when extending to 10M tokens in the text modality (approximately 7M words); 2M tokens in the audio modality (up to 22 hours); 2.8M tokens in the video modality (up to 3 hours).

Perplexity over Long Sequences
Cumulative average negative log-likelihood (NLL) as a function of token position in long documents and code data. A lower value demonstrates better prediction.
Objective: Evaluate the ability of models to make use of very long contexts to improve next-token prediction

Method: Record negative log-likelihood (NLL) of tokens at different positions in input sequences from held-out text

Results:

NLL decreases monotonically with sequence length, indicating improved prediction accuracy up to tested sequence lengths
Models can make use of the whole input even at very long-context lengths
Power law of the form 𝐿(𝑥) = 𝛼𝑥 𝛽 + 𝛾 fits the data points well

Conclusions:

Models can improve predictions by finding useful patterns in tokens even at very long-context lengths
Increased context occasionally provides outsized benefit, potentially due to repetition of code blocks, leading to power-law deviation

Text-Haystack
Comparison of Gemini 1.5 Pro with GPT-4 Turbo for the text needle-in-a-haystack task.
Objective: Testing long-context recall using the needle-in-a-haystack evaluation

Method: Using a set of concatenated and repeated essays written by Paul Graham to fill the desired context length, inserting a needle at linearly spaced intervals with varied prompts, reporting magic number recall at various context lengths and positions in the input sequence

Results/Conclusions: Gemini 1.5 Pro achieves 100% recall up to 530k tokens and >99.7% recall up to 1M tokens, still able to find and extract information with 99.2% accuracy up to 10M tokens

Video-Haystack

Objective: To test Gemini 1.5 Pro’s ability to retrieve specific information across multiple hours of video using a cross-modal evaluation

Method: Hidden needle-in-a-haystack evaluation adapted for cross-modal testing, with a needle hidden in a three-hour-long video and retrieval query given in text

Results/Conclusions:

Gemini 1.5 Pro successfully retrieved the secret word across various video lengths and different locations of the randomly inserted “needle” frame.
In comparison, the GPT-4V API was limited to supporting video lengths of only up to approximately the first 3 minutes, indicating a significant advantage of Gemini 1.5 Pro in handling longer video content.

Audio-Haystack
Audio version of the needle-in-a-haystack experiment comparing Gemini 1.5 Pro and a combination of Whisper and GPT-4 Turbo.
Objective: Testing Gemini 1.5 Pro’s long context capabilities on audio understanding

Method: Hiding a short clip of audio within up to 22 hours long audio signal, requiring cross-modal reasoning

Results/Conclusions:

Gemini 1.5 Pro achieved 100% accuracy in identifying the secret keyword in all instances
Existing models struggled with long audio context, requiring transcription into text for comparison
Whisper combined with GPT-4 Turbo achieved around 94.5% accuracy in identifying the keyword

Improved Diagnostics
Retrieval performance of the “multiple needles-in-haystack” task, which requires retrieving 100 unique needles in a single turn.
Objective:

To evaluate the performance of the Gemini 1.5 Pro model on the needle-in-a-haystack tasks across text, video, and audio modalities.
To explore the model’s limitations and propose extensions to the task for a more comprehensive assessment of long-context retrieval capabilities.

Method:

An extension to the task involved increasing the number of unique “needles” in each haystack and requiring the model to retrieve all of them, with up to 1M tokens in context length and 100 different needles inserted.

Results/Conclusions:

Gemini 1.5 Pro outperformed GPT-4 Turbo on the multiple needles-in-a-haystack task up to 128K tokens.
GPT-4 Turbo’s recall oscillated with longer context lengths, while Gemini 1.5 Pro maintained consistent recall.
Prompting method and type of needle influenced model performance.
Advocated for evaluating models on tasks that demand complex reasoning over long contexts for deeper insights into their capabilities.

In-context language learning — Learning to translate a new language from one book
Quantitative results for Kalamang↔English translation on MTOB.
Objective: To evaluate the in-context learning abilities of Gemini 1.5 Pro on the Machine Translation from One Book (MTOB) benchmark, focusing on the translation between English and Kalamang, a language with fewer than 200 speakers.

Method:

Gemini 1.5 Pro was provided with a comprehensive set of instructional materials in Kalamang, including a reference grammar, a bilingual wordlist, and additional parallel sentences, totaling approximately 250k tokens.
The model’s performance was compared against Claude 2.1 and GPT-4 Turbo using both the full materials and a reduced set (half of the grammar book).
A 0-shot setup was also tested to evaluate the model’s reliance on in-context information versus pre-training data.
Human evaluation involved a non-native, non-fluent speaker rating the quality of translations on a scale from 0 to 6.
Automatic metrics used included BLEURT for Kalamang to English and chrF for English to Kalamang translations.

Results and Conclusions:

In the 0-shot setting, all models performed essentially at random, indicating no pre-existing knowledge of Kalamang in their training data.
Gemini 1.5 Pro significantly outperformed GPT-4 Turbo and Claude 2.1 in the half book setting and achieved even higher scores with the entire book, as shown in Table 2.
Human evaluation scores for Gemini 1.5 Pro were 4.36 for Kalamang to English and 5.52 for English to Kalamang, closely approaching the scores of a human language learner.
The results underscore the importance of long-context understanding and sufficient contextual information for learning new skills, particularly for languages not represented in pre-training corpora.
Gemini 1.5 Pro’s performance suggests the potential of long-context models to support the preservation and revitalization of endangered languages and improve cross-linguistic communication and understanding.
Future research should focus on enhancing translation quality and addressing the evaluation challenges of LLMs on low-resource and under-represented languages.

Long-document QA
Evaluating the ability to answer questions about large collections of text across three context sizes.
Objective: To evaluate the in-context language learning capabilities of Gemini 1.5 Pro and compare Gemini 1.5 Pro against Gemini 1.0 Pro and Claude 2.1

Method:

Created questions from “Les Misérables” and provide the entire book as input
Gemini 1.0 Pro uses retrieval-augmented generation with TF-IDF indexing and external database
Gemini 1.5 Pro eliminates the need for additional data post-processing and retrieval pipelines
Human evaluation using the Attributable to Identified Sources (AIS) protocol
Automatic evaluation using the AutoAIS metric

Results/Conclusions:

Gemini models show good knowledge of the source material in the 0-shot setup
Claude 2.1 often declines to answer to avoid non-factual claims
Providing the full book as context eliminates the need for additional retrieval components without loss of performance
AutoAIS metric shows agreement between human and automatic evaluation
Gemini 1.5 Pro can act as a model-based evaluator, showcasing the benefits of long-context models for reasoning and verification from large amounts of text.

Long-context Audio
Word error rate (WER) for various models on 15-minute videos.
Objective: To evaluate the long-context understanding capabilities of Gemini 1.5 Pro on audio inputs, specifically focusing on automatic speech recognition (ASR) performance.

Method:

Gemini 1.5 Pro was tested on 15-minute segments of an internal YouTube video-based benchmark.
Performance was compared against the 1.0 Pro model, the Universal Speech Model (USM), and Whisper.
Word Error Rate (WER) was used as the metric for evaluation, where a lower WER indicates better performance.

Results/Conclusions:

The 1.0 Pro model showed a WER of 100% when transcribing 15-minute videos without segmentation due to a mismatch in training and testing audio lengths. However, with segmentation every 30 seconds, its WER improved to 7.8%.
The USM model achieved a WER of 8.8%, indicating robustness to long segments without needing segmentation.
Whisper required segmentation every 30 seconds to achieve a WER of 7.3%, showing it is not robust to long segments.
Gemini 1.5 Pro outperformed all other models with a WER of 5.6%, demonstrating superior long-context understanding capabilities without the need for extra input segmentation and pre-processing.

Long-context Video QA
Comparison between GPT-4V and Gemini 1.5 Pro on 1H-VideoQA.Comparison between 1H-VideoQA and EgoSchema.
Objective: To introduce a new benchmark, 1H-VideoQA, for evaluating question-answering models that can handle long-context videos, addressing the limitations of existing benchmarks like EgoSchema which only include videos up to 3 minutes long.

Method:

The 1H-VideoQA benchmark is composed of 126 five-way multiple choice questions over public videos ranging from 40–105 minutes long.
Annotations were collected to require understanding of one or multiple events within the videos, making it challenging to infer answers by looking at a few randomly sampled frames.
Experiments were conducted by extracting video frames at one frame-per-second and linearly subsampling long videos to a fixed context length. Performance was also measured by providing all frames for each video as a reference.

Results and Conclusions:

Gemini 1.5 Pro achieves 64.5% accuracy on EgoSchema with 16 frames, outperforming GPT4V
Performance of Gemini 1.5 Pro consistently increases on 1H-VideoQA as the number of frames provided increases, indicating the need for more frames as context
Gemini 1.5 Pro consistently outperforms GPT-4V on 1H-VideoQA, whether the video is subsampled to 16 or 150 frames
1H-VideoQA is a useful benchmark for evaluating and driving the development of future long-context video models

Core Capabilities
Gemini 1.5 Pro vs Gemini 1.0
Objective: Evaluate the core capabilities of Gemini 1.5 Pro model compared to its predecessors, focusing on non long-context tasks

Method: Used established benchmarks and internal benchmarks covering text, vision, and audio modalities

Results/Conclusions: Generational improvement between 1.0 and 1.5 series, with 1.5 Pro outperforming 1.0 Pro and approaching 1.0 Ultra on most benchmarks

Text Evaluations
Evaluation results of Gemini 1.5 Pro and Gemini 1.0 models on standard coding, multilingual as well as maths, science and reasoning benchmarks.
Reasoning, Maths, and Science: 1.5 Pro outperforms 1.0 Ultra and 1.0 Pro on various maths and reasoning tasks
Code: 1.5 Pro surpasses 1.0 Ultra on code generation tasks
Multilinguality: 1.5 Pro improves over 1.0 Ultra on multilingual tasks, showing substantial improvement across different languages
Instruction Following: 1.5 Pro outperforms 1.0 series models in following complex instructions, with a significant improvement in full-response accuracy

Vision Multimodal Evaluations
Comparison of Gemini 1.5 Pro with Gemini 1.0 Pro and Ultra on image and video understanding benchmarks.
Gemini 1.5 Pro improves substantially over Gemini 1.0 Pro on 5 multimodal reasoning benchmarks
Gemini 1.5 Pro matches or exceeds Gemini 1.0 Ultra on 2 multimodal reasoning benchmarks
Gemini 1.5 Pro approaches but does not surpass Gemini 1.0 Pro on benchmarks requiring strong OCR capabilities
Error analysis revealed many false negatives, lower-bounding the model’s true performance
Future work should focus on human evaluations for datasets requiring strong OCR capabilities and develop softer metrics
Gemini 1.5 Pro outperforms Gemini 1.0 Ultra on question-answering and video captioning benchmarks
Gemini 1.5 Pro matches performance on YouCook2 and surpasses Gemini 1.0 Ultra on VATEX and VATEX ZH

Audio Multimodal Evaluations
Comparison of Gemini 1.5 Pro with USM, Whisper, Gemini 1.0 Pro and Gemini 1.0 Ultra on audio understanding tasks.
Gemini 1.5 Pro outperforms specialist models like USM and Whisper on speech understanding benchmarks
Gemini 1.5 Pro performs similarly to Gemini 1.0 Pro on Speech Understanding
Gemini 1.0 Ultra offers slight benefits over 1.5 Pro but requires more training compute and serving resources

Paper

Gemini 1.5: Unlocking multi-modal understanding across millions of tokens of context

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on February 26, 2024.

Canonical link

Exported from Medium on May 4, 2026.
