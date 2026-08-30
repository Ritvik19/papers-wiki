# Introducing Cohere Transcribe: a new state-of-the-art in open-source speech recognition

**Source URL**: https://cohere.com/blog/transcribe  
**Published**: Mar 26, 2026

Unmatched transcription accuracy — our first step toward powering enterprise speech intelligence in North.

Cohere is announcing Transcribe, a state-of-the-art automatic speech recognition (ASR) model that is open source and available today for download.

Speech is rapidly becoming a core modality for AI-enabled workloads and automations — from meeting transcription and speech analytics to real-time customer support agents.

Our objective was straightforward: push the frontier of dedicated ASR model accuracy under practical conditions. The model was trained from scratch with a deliberate focus on minimizing word error rate (WER), while keeping production readiness top-of-mind. In other words, not just a research artifact, but a system designed for everyday use.

Cohere Transcribe reflects that intent. It is available for open-source use with full infrastructure control, maintains a manageable inference footprint suitable for practical GPU and local utilization, delivers best-in-class serving efficiency, and is also available via Model Vault— Cohere's secure, fully managed model inference platform.

Cohere Transcribe currently ranks #1 for accuracy on HuggingFace's Open ASR Leaderboard, setting a new benchmark for real-world transcription performance.

This marks our zero-to-one in bringing high-performance speech recognition into enterprise AI workflows.

## Model overview

| Field | Value |
| --- | --- |
| Name | cohere-transcribe-03-2026 |
| Architecture | conformer-based encoder-decoder |
| Input | audio waveform → log-Mel spectrogram |
| Output | transcribed text |
| Model size | 2B |
| Model | a large Conformer encoder extracts acoustic representations, followed by a lightweight Transformer decoder for token generation |
| Training objective | standard supervised cross-entropy on output tokens; trained from scratch |
| Languages | 14 languages: European (English, French, German, Italian, Spanish, Portuguese, Greek, Dutch, Polish); APAC (Chinese Mandarin, Japanese, Korean, Vietnamese); MENA (Arabic) |
| License | Apache 2.0 |

Image 1: Cohere Transcribe is an open-weights Conformer ASR model converting speech audio into text across 14 supported languages.

## Model performance

### Accuracy

Cohere Transcribe is the latest standard for English speech recognition accuracy. It leads the HuggingFace Open ASR Leaderboard with an average word error rate of just 5.42%, outperforming all open- and closed-source dedicated ASR alternatives, including Whisper Large v3, ElevenLabs Scribe v2, and Qwen3-ASR-1.7B. This captures the model's versatile capability across real-world speech tasks, such as robustness to multiple-speaker environments, boardroom-style acoustics (e.g. AMI dataset), and diverse accents (e.g. Voxpopuli dataset).

| Model | Average WER | AMI | Earnings 22 | Gigaspeech | LS clean | LS other | SPGISpeech | Tedlium | Voxpopuli |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cohere Transcribe | 5.42 | 8.13 | 10.86 | 9.34 | 1.25 | 2.37 | 3.08 | 2.49 | 5.87 |
| Zoom Scribe v1 | 5.47 | 10.03 | 9.53 | 9.61 | 1.63 | 2.81 | 1.59 | 3.22 | 5.37 |
| IBM Granite 4.0 1B Speech | 5.52 | 8.44 | 8.48 | 10.14 | 1.42 | 2.85 | 3.89 | 3.10 | 5.84 |
| NVIDIA Canary Qwen 2.5B | 5.63 | 10.19 | 10.45 | 9.43 | 1.61 | 3.10 | 1.90 | 2.71 | 5.66 |
| Qwen3-ASR-1.7B | 5.76 | 10.56 | 10.25 | 8.74 | 1.63 | 3.40 | 2.84 | 2.28 | 6.35 |
| ElevenLabs Scribe v2 | 5.83 | 11.86 | 9.43 | 9.11 | 1.54 | 2.83 | 2.68 | 2.37 | 6.80 |
| Kyutai STT 2.6B | 6.40 | 12.17 | 10.99 | 9.81 | 1.70 | 4.32 | 2.03 | 3.35 | 6.79 |
| OpenAI Whisper Large v3 | 7.44 | 15.95 | 11.29 | 10.02 | 2.01 | 3.91 | 2.94 | 3.86 | 9.54 |
| Voxtral Mini 4B Realtime 2602 | 7.68 | 17.07 | 11.84 | 10.38 | 2.08 | 5.52 | 2.42 | 3.79 | 8.34 |

Image 2: the Hugging Face Open ASR Leaderboard as of 03.26.2026.

Critically, these gains aren't limited to benchmark datasets. We see the same state-of-the-art performance carried over into human evaluations, where trained reviewers assess transcription quality across real-world audio for accuracy, coherence, and usability.

Image 3: human preference evaluation of model transcripts in English.

Image 4: human evaluation of ASR accuracy for a selection of supported languages.

### Throughput

In production settings, ASR systems must operate under strict latency and throughput constraints; even if accurate, slow or resource-intensive transcription can directly impact user experience, operational efficiency, and cost.

Transcribe extends the Pareto frontier, delivering state-of-the-art accuracy (low WER) while sustaining best-in-class throughput (high RTFx) within the 1B+ parameter model cohort.

Image 5: throughput (RTFx) vs accuracy (WER) plot for leading models larger than 1B in size.

## Zero to one, and beyond

We are working towards deeper integration of Cohere Transcribe with North, Cohere's AI agent orchestration platform. With planned updates, Cohere Transcribe will evolve from a high-accuracy transcription model into a broader foundation for enterprise speech intelligence.

## Getting started

Cohere Transcribe is now available for download on Hugging Face. You can also access Cohere Transcribe via API for free experimentation subject to rate limits, or provision a dedicated Model Vault for production deployment without rate limits.
