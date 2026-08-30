# Papers Explained 590: Nemotron 3 Nano Omni

Papers Explained 590: Nemotron 3 Nano Omni

Papers Explained 590: Nemotron 3 Nano Omni

Nemotron 3 Nano Omni is the newest model in the Nemotron multimodal series, natively supporting audio, text, image, and video inputs. Built…

Papers Explained 590: Nemotron 3 Nano Omni

Nemotron 3 Nano Omni is the newest model in the Nemotron multimodal series, natively supporting audio, text, image, and video inputs. Built on the Nemotron 3 Nano 30B-A3B Mixture-of-Experts backbone, with C-RADIOv4-H1 vision and Parakeet-TDT-0.6B audio encoders, it delivers notable improvements in real-world document understanding, long audio-video comprehension, and agentic computer use via advances such as native audio support, dynamic image resolution, temporal video compression, and an extended 256K token context length.

Model Architecture
Nemotron 3 Nano Omni architecture.
The model follows an encoder-projector-decoder design, combining the Nemotron 3 Nano 30B-A3B language model with modality-specific encoders for vision and audio, connected via MLP projectors. The vision encoder is based on C-RADIOv4-H, while the audio encoder is initialized with Parakeet-TDT-0.6B-v2.

To handle varying image resolutions, the tiling strategy is replaced with dynamic resolution processing that preserves the native aspect ratio. Each image is decomposed into a variable number of 16 × 16 patches, with the total number of visual tokens per image constrained between 1,024 and 13,312. This equates to an image size of 512 × 512 and 1840 × 1840, respectively, for square images. Prior to projection, a pixel shuffle operation with 4× downsampling is applied to reduce the token count presented to the language model. For video frames, a Conv3D patch embedder is used that compresses every two frames into one, leading to a 2× reduction in the total number of tokens for video inputs.

Audio inputs are resampled to 16 kHz mono and encoded using the Parakeet-TDT-0.6B-v2 FastConformer encoder. Log-mel spectrogram features are computed with a 10 ms hop size, followed by three stride-2 convolutional subsampling layers, resulting in an overall ∼8× temporal downsampling. This yields approximately 12.5 tokens per second of audio (i.e., ∼80 ms per token). Audio streams are segmented into 30-second clips (corresponding to ∼375 tokens per clip) with the last clip accounting for the remainder. Streams shorter than 30 seconds are not padded. The model is trained to handle inputs ranging from 0.5 second to 20 minutes, but the model context length can accommodate audio input of over 5 hours.

For multimodal inputs containing both visual and audio streams (e.g., videos with audio), modality tokens are interleaved in temporal order during sequence construction to enable joint temporal reasoning across modalities.

Training Recipe & Datasets
Staged training recipe for the v3 omni-modal model.
SFT
Approximate values for the total number of samples and tokens in the training datasets across the SFT stages.
The SFT pipeline is split into seven stages that progressively introduce new modalities and increase context length.

Stage 0: Vision projector warmup

This stage train only the vision MLP projector to align the vision and language modalities with a maximum context length of 16384, while all other components are kept frozen.

Stage 1: Vision SFT 16k

After training the vision projector, both the language model and the vision encoder are unfrozen for joint vision–language fine-tuning. During this stage, the model develops its core vision-language capabilities.

The training data builds upon the SFT Stage 1 dataset used in Nemotron Nano V2 VL , with several key enhancements.

Its text-only subset is replaced with a portion of the SFT dataset from Nemotron 3 Nano 30B-A3B, resulting in higher-quality text reasoning samples.
Label quality is improved by re-annotating noisy subsets using models from the Qwen3-VL series.
The availability and quality of reasoning traces are enhanced by incorporating both human-annotated and model-generated chains of thought, leveraging models from the Qwen3-VL, Qwen3.5, and Kimi-K2.5 families.
The coverage is expanded across domains, including GUI understanding, visual grounding, charts, tables, document understanding, and video understanding, as well as across multiple languages. This is achieved through a combination of publicly available datasets, as well as internally curated data, including human annotation.
To increase domain coverage, fully-synthetic data pipelines are developed, ensuring broad representation across domains, question types, and visual diversity. Guided by the gaps identified in the training blend, relevant data is sourced and synthetic question-answer pairs are generated at scale using frontier open-source models such as Qwen3-VL, Qwen 3.5, GPT-OSS, Nemotron-Parse, and DeepSeek-OCR.

Stage 2: Audio projector warmup

This stage warms up the audio MLP projector while keeping the LLM, vision encoder, and Parakeet-TDT audio encoder all frozen. The training data consists of the Granary v1.1 ASR dataset of diverse automatic speech recognition data across varied acoustic conditions, speaking styles, and languages.

Stage 3: Audio projector & encoder

This stage unfreezes the Parakeet-TDT audio encoder while keeping the LLM backbone and vision encoder frozen. The audio encoder and its associated projector are jointly trained on an expanded audio corpus.
Dataset composition for the audio pretraining stage.
Audio samples are paired with captions, multiple-choice questions, and open-ended questions, with a subset further augmented with reasoning traces. The synthetic data generation pipeline leverages open models like Qwen3-Omni-30B-A3B to produce captions and specialized music tools to produce metadata. These outputs are then used to generate QA pairs via GPT-OSS-120B.

Stage 4: Omni SFT 16k

All model parameters, including the LLM backbone, are trainable. The data mixture combines vision SFT, text instruction following, safety, video understanding, omni (audio+video) QA and captioning, ASR, and audio reasoning data.
Dataset composition for Stage 4: Joint Omni SFT at 16k context length.
The omni-modal data used in this stage is a blend of audio-visual captions, open-ended QA and MCQ style QA. Videos less than 2 minutes length are used as source media for this data. The question-answer pairs and captions are synthetically generated by first extracting audio-visual metadata from videos and then using that metadata for question-answer generation and summarization using open-source models Qwen3-Omni-30B-A3B and GPT-OSS-120B. The audio reasoning dataset comprises speech-to-text conversations synthesized by converting text SFT user turns into spoken form and generating LLM responses to a curated subset of ASR prompts.

Stage 5: Omni SFT 48k

This stage extends the context length to 49,152 tokens with all model parameters trainable. The data mixture is rebalanced to emphasize longer sequences, with reduced sampling of short-context data and increased weight on medium and long video, omni, and reasoning data.
Stage 5 (Omni SFT 48k) data composition by category.
To improve safety coverage, the safety data blend from Nemotron 3 Super is additionally incorporated. Omni-modal data comprising reasoning and non-reasoning single-turn QA is synthesized from diverse domains and categories. The pipeline segments videos into 20-second clips, extracts audio-visual metadata using multimodal models such as Qwen3-Omni-30B-A3B, and generates QA pairs and reasoning traces via open-source reasoning models such as GPT-OSS-120B.

Stage 6: Omni SFT 256k

This stage extends the context length to 262,144 and is intended to significantly increase the model’s long context capabilities.
Dataset composition for the ultra-long context Stage 6.
It particularly improves the model’s ability to analyze documents spanning 10 to 100+ pages, including reasoning over text, charts, and complex tables. A diverse collection of long-form documents is assembled, including academic papers, financial reports, and presentations, and vision-language models are leveraged to generate synthetic question-answer pairs and reasoning traces at the page, multi-page, and full-document levels.

Training Details
Summary of the SFT training hyperparameters.
Reinforcement Learning

An adapted version of Group Sequence Policy Optimization (GSPO) is used as the RL training algorithm.

Preference Optimization

To align the model using both preference-level and quality-level supervision, Mixed Preference Optimization (MPO) is adopted, which combines a preference loss (Preference Optimization (DPO) in this case) and a quality loss (Binary Classifier Optimization (BCO) in this case) during the offline reinforcement learning stage. To construct the training data, rejection sampling is applied to generate candidate responses in the vision domain and assign binary labels based on outcome correctness, yielding positive samples for accepted responses and negative samples for rejected ones.

Text-RL

During text-only RL, only the LM parameters of the model are trained via multi-environment RLVR/RLHF for improving general capabilities. The RL data and infrastructure from the post-training of Nemotron 3 Nano and Supe are reused. The LM input token embedding parameters are frozen to mitigate representational drift between multi-modal stages.

Image RL

Outcome-based RL is employed on visual reasoning tasks, which can be divided into the following categories.

Chart, document, and text-rich image reasoning: numerical, comparative, and trend reasoning over plots, tables, diagrams, infographics, and natural images containing text (∼28K). -STEM and mathematical problems: geometry, algebra, functions, and counting, in both English and Chinese (∼19K).
Game and puzzle reasoning: rule-based reasoning over rendered game-board states (∼12K).
Visual question answering: open-ended and multiple-choice questions covering spatial relations, attribute recognition, and yes/no judgements (∼8K).
Visual grounding: click-coordinate prediction on desktop, mobile, and web screenshots (∼7K).

The outcome score comes from one of four rule-based verifiers, chosen per prompt: string-match for free-form text answers, mathruler for symbolic equivalence on numeric and algebraic answers, multiple-choice for selected-letter answers, and gui-coordinate for click-target predictions, where the reward decays smoothly with distance from the target. The format score rewards a single reasoning block followed by a single \boxed answer, with partial credit when the policy emits extra reasoning or boxed entries.

Pass-rate filtering is applied using 8 rollouts per prompt from the initial policy checkpoint, retaining only prompts whose empirical pass rate is below 0.8. A small set of unanswerable or image-text-mismatched prompts is additionally included to train the policy to abstain when visual evidence is insufficient.

Omni-RL

A diverse, omni-modal training corpus of approximately 120K prompts spanning 113 sub-datasets across four modality groups: image, video, audio, and text-only reasoning is curated. The dataset is constructed by aggregating and filtering data from multiple sources:

Omni RL data (∼17.6K samples): synthetic data generated from video content with accompanying audio, covering diverse visual understanding and temporal reasoning tasks
Video RL data (∼8.5K): video-only question–answer pairs targeting spatial, temporal, and causal reasoning.
Image RL data (∼32K): a large-scale image understanding set drawing from OCR (∼10.5K), chart analysis (∼8.9K), game-related visual QA (∼11.9K), GUI grounding (∼7.1K), and additional curated domains
Audio RL data (∼4.2K) and ASR (∼3.8K): audio question-answering and automatic speech recognition tasks at various utterance lengths.

Only prompts on which the base model achieves a pass rate between 0.1 and 0.9 are retained, with stricter 0.3–0.7 bands for AudioQA. The verification pipeline supports five task types: multiple-choice (34%), string matching (31%), mathematical rule-based verification (26%), GUI coordinate grounding (6%), and ASR evaluation (3%). Additionally, a small set of unanswerable or mismatched samples (∼4K) is included to train the model to appropriately abstain when evidence is insufficient.

Evaluation
Comparison of Nemotron 3 Nano Omni with other omni-modal models.
Nemotron 3 Nano Omni shows significant improvements across all vision benchmarks relative to Nemotron Nano V2 VL and outperforms Qwen3-Omni on several tasks
Comparison of Nemotron 3 Nano Omni on diverse audio and speech tasks, ASR (OpenASR), long-form ASR (TED-LIUM), MMAU, and VoiceBench.
The model outperforms the Qwen family in Automatic Speech Recognition (ASR) and VoiceBench, exhibiting strong speech, sound, and interaction abilities.
Comparison of Nemotron 3 Nano Omni on Video+Audio (Omni) benchmarks.
Nemotron 3 Nano Omni surpasses Qwen3-Omni in reasoning and perception tasks on DailyOmni and WorldSense, both in reasoning-on and -off modes.
Comparison of Nemotron 3 Nano Omni across selected text-only benchmarks.
The Omni model maintains text performance comparable to its backbone LLM (Nemotron 3 Nano 30B-A3B) while adding vision and audio capabilities.
Effect of reasoning budget across several key benchmarks.
Adjusting reasoning budgets during inference improves accuracy on select benchmarks with no observed degradation, allowing early termination of problematic reasoning traces.
Per-benchmark accuracy (128 frames / 256 frames) and TTFT at concurrency 1 across Conv3D and EVS combinations, with EVS rate 𝑞 = 0.5, reasoning off.BF16 with Conv3D enabled, varying EVS pruning rate 𝑞, reasoning off.
Both mechanisms reduce TTFT and input tokens; stacking Conv3D and EVS drops TTFT by 33% vs baseline, with minimal accuracy loss. EVS pruning rate up to q=0.7 shows flat accuracy, but aggressive pruning reduces accuracy, especially in long-video tasks.

Paper

Nemotron 3 Nano Omni: Efficient and Open Multimodal Intelligence 2604.24954

That’s a wrap!

If you enjoyed this breakdown, follow for more. I publish new paper explanations most weekdays.

More papers in this series, organized by lab and topic, are in the start here guide.

What paper should I cover next? Let me know in the responses.

By Ritvik Rastogi on August 7, 2026.

Canonical link

Exported from Medium on August 22, 2026.
