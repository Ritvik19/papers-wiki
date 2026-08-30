# Mistral OCR

**Source URL**: https://mistral.ai/news/mistral-ocr/  
**Published**: March 6, 2025  
**Author**: Mistral AI Team

Mistral OCR is an Optical Character Recognition API for document understanding. It comprehends media, text, tables, and equations in images and PDFs, extracting ordered interleaved text and images—ideal for RAG over multimodal documents (slides, complex PDFs).

Default document model on **Le Chat**; API **`mistral-ocr-latest`** at **$1 per 1,000 pages** (≈2× pages per dollar with batch). Available on La Plateforme; cloud/inference partners and on-premises coming soon.

## Highlights

- State-of-the-art understanding of complex documents
- Natively multilingual and multimodal
- Top-tier benchmarks
- Fastest in its category (up to **2,000 pages/minute** on one node)
- Doc-as-prompt, structured output (JSON)
- Selective self-host for sensitive/classified workloads

## Complex document understanding

Handles interleaved imagery, math, tables, LaTeX layouts, and scientific papers with charts and figures. Demo notebook extracts PDF content to markdown with embedded images.

## Benchmarks (Mistral OCR 2503)

| Model | Overall | Math | Multilingual | Scanned | Tables |
|-------|---------|------|--------------|---------|--------|
| Google Document AI | 83.42 | 80.29 | 86.42 | 92.77 | 78.16 |
| Azure OCR | 89.52 | 85.72 | 87.52 | 94.65 | 89.52 |
| Gemini-1.5-Flash-002 | 90.23 | 89.11 | 86.76 | 94.87 | 90.48 |
| Gemini-1.5-Pro-002 | 89.92 | 88.48 | 86.33 | 96.15 | 89.71 |
| Gemini-2.0-Flash-001 | 88.69 | 84.18 | 85.80 | 95.11 | 91.46 |
| GPT-4o-2024-11-20 | 89.77 | 87.55 | 86.00 | 94.58 | 91.70 |
| **Mistral OCR 2503** | **94.89** | **94.29** | **89.55** | **98.96** | **96.12** |

Mistral also extracts embedded images from documents (capability absent in compared LLM OCR baselines). Multilingual fuzzy-match generation: **99.02%** vs. Azure 97.31%, Gemini-2.0-Flash 96.53%, Google Document AI 95.88%.

## Doc-as-prompt and self-host

Documents can be used as prompts for structured JSON extraction and downstream agent chaining. Self-hosting available for regulated environments.

## Use cases

Scientific paper digitization, historical/cultural heritage preservation, customer-service knowledge bases, and AI-ready conversion of technical literature, engineering drawings, lecture notes, presentations, and regulatory filings.
