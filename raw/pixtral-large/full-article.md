# Pixtral Large

**Source URL**: https://mistral.ai/news/pixtral-large/  
**Published**: November 18, 2024  
**Author**: Mistral AI team

> **Heads up: this model is deprecated.** Pixtral Large is no longer maintained and has been replaced by Mistral AI's latest vision and multimodal models.

## Pixtral Large in short

- Frontier-class multimodal performance
- State-of-the-art on MathVista, DocVQA, VQAv2
- Extends Mistral Large 2 without compromising text performance
- **Architecture:** 123B multimodal decoder, 1B-parameter vision encoder; 128K context (≥30 high-resolution images)
- **Use:** Le Chat; API as `pixtral-large-latest`

Pixtral Large is a **124B** open-weights multimodal model built on Mistral Large 2—the second model in Mistral's multimodal family. It understands documents, charts, and natural images while retaining Mistral Large 2's leading text understanding. Available under Mistral Research License (research/education) and Mistral Commercial License (commercial use).

## Performance

Evaluated against frontier models on standard multimodal benchmarks:

- **MathVista:** 69.4%—best among compared models
- **ChartQA / DocVQA:** surpasses GPT-4o and Gemini-1.5 Pro
- **MM-MT-Bench:** beats Claude-3.5 Sonnet (new), Gemini-1.5 Pro, GPT-4o (latest)
- **LMSys Vision Leaderboard:** best open-weights model by ~50 ELO; also beats GPT-4o (August '24)

## Qualitative samples

Examples include multilingual OCR + reasoning (Swiss café receipt with 18% tip), chart understanding (training-loss instability for dark-dragon-50), and logo/company identification (BNP Paribas, Brave, Cloudflare, CMA CGM, Front use Mistral models).

## Mistral Large 24.11 update

Alongside Pixtral Large, Mistral Large gets an update (`pixtral-large-latest` on API; **Mistral Large 24.11** on Hugging Face). Improvements include long-context understanding, new system prompt, and more accurate function calling—suited for RAG and agentic enterprise workflows. Cloud availability via Google Cloud and Microsoft Azure within a week.
