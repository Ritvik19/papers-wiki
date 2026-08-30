# Grok Speech to Text and Text to Speech APIs

Source: https://x.ai/news/grok-stt-and-tts-apis
Published: Apr 17, 2026

Today, we are excited to announce two powerful standalone audio APIs: Grok Speech to Text (STT) and Grok Text to Speech (TTS). Built on the same stack that powers Grok Voice, Tesla vehicles, and Starlink customer support.

These standalone endpoints make it straightforward for developers to integrate high-quality speech features into any application, whether you're creating voice agents, real-time transcription tools, accessibility solutions, podcasts, or interactive audio experiences.

## Speech to Text

High accuracy, low latency.

- Generate transcripts from large audio files in milliseconds via our REST API
- Transcribe speech in real time with our lowest latency WebSocket API

We've added powerful features like word-level timestamps, speaker diarization, and multichannel support. It further includes intelligent Inverse Text Normalization that correctly handles numbers, dates, currencies, and more.

**xAI example transcript (0 mistakes):**

> Thank you for holding, Anghared Llewelyn Bowen. I see here your mortgage rate lock is set at 3.75% and is valid until March 10th, 2024. Oisin MacGiolla Phadraigh, once we receive your signed documents by February 15th, we can aim for a closing date on March 20th. If you have any concerns, please feel free to email me at a.bowen@bestbank.com.

**Other models (6 mistakes):** misheard names, dates as 03/10/2024, spelled-out email.

### Pricing

We keep pricing straightforward and predictable: Speech to Text is $0.10 per hour for batch and $0.20 per hour for streaming. Full details and current rate limits are available in the xAI API console.

### Enterprise-Grade Transcription

Grok STT is evaluated against the top commercial models on phone calls, meetings, video/podcasts, and telephony. It excels at entity recognition and business use cases like medical, legal, and financial.

| Domain (Word Error Rate) | Grok STT | ElevenLabs | Deepgram | AssemblyAI |
| --- | --- | --- | --- | --- |
| Phone Call Entities | 5.0% | 12.0% | 13.5% | 21.3% |
| Video/Podcasts | 2.4% | 2.4% | 3.0% | 3.2% |
| Meetings | 10.9% | 12.2% | 16.3% | 15.7% |
| Telephone | 9.3% | 9.4% | 11.0% | 11.2% |
| Overall | 6.9% | 9.0% | 11.0% | 12.9% |

Most transcription models give you raw spoken words. Grok Speech to Text goes further.

When you enable formatting, the API performs advanced Inverse Text Normalization that intelligently converts spoken language into proper structured output:

- "My name is John Smith and my phone number is 4145551234."
- "I saw a transaction for 6.99 on my account."

### Multilingual fluency

The Grok Speech to Text API offers strong multilingual support across 25+ languages, switch languages seamlessly without missing a beat.

### Multichannel & Diarization (Speaker Identification)

Transcribe multichannel audio files for perfect speaker separation with the same API.

Detect speakers in both pre-recorded and real-time streaming with word-level speaker IDs using Diarization.

## Text to Speech

Fast, natural, and expressive voices with Speech Tags.

- Turn long-form text into speech with our REST API
- Generate speech in real time with our WebSocket API

### Fine-Grained Control

Add natural prosody and emotion using simple inline and wrapping speech tags: `[laugh]`, `[sigh]`, `[whisper]`, and many more. These controls let you create engaging, lifelike delivery without complex markup.

### Pricing

Text to Speech is priced at $15.00 per 1 million characters, with straightforward usage-based billing and no hidden fees.
