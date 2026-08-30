# Welcome the NVIDIA Llama Nemotron Nano VLM to Hugging Face Hub

**Source**: `raw/llama-nemotron-nano-vl/full-article.html` (236 KB), `raw/llama-nemotron-nano-vl/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

Llama Nemotron Nano VL is NVIDIA's 8B-parameter vision-language model for intelligent document processing (IDP) and OCR, built on Llama-3.1-8B-Instruct paired with C-RADIOv2-VLM-H, an NVIDIA-trained Vision Transformer that serves as the vision backbone. The stated target is enterprise document workflows: invoices, receipts, contracts, tax forms, and medical/insurance records, where a model needs to read dense text, parse tables and charts, and localize where on the page that information lives.

The vision backbone is the differentiator. C-RADIOv2-VLM-H is trained on multi-resolution data with multiple distillation techniques and multiplicative weight noise for generalization, then combined with a design that dynamically aggregates patch features and uses high-resolution tiling. That lets the model process documents of arbitrary aspect ratio at high resolution, preserving small fonts and multi-column layouts, without the spatial distortion that comes from naively resizing a page to a fixed square input. Training follows a two-stage recipe: pre-training aligns vision and language through an MLP connector on roughly 1.5M samples (public, synthetic, and internally curated), then supervised fine-tuning trains the full model end-to-end on OCR, text grounding, table parsing, and document VQA tasks, with reading-order prediction, markdown reconstruction with semantic classes (Captions, Titles, Section headers), bounding-box grounding, and LaTeX table/formula extraction. A large share of the fine-tuning data derives from NVIDIA's own NeMo Retriever Parse OCR pipeline (NVPDFTex arXiv documents, human-annotated Common Crawl PDFs, rendered Wikipedia pages) plus refined versions of public datasets like DocLayNet, FinTabNet, and PubTables-1M.

The model is evaluated on OCRBench v2 (10,000+ human-verified QA pairs testing text localization, table parsing, diagram reasoning, and key-value extraction), where it outperforms other VLMs tested, and also scores strongly on ChartQA and AI2D. NVIDIA frames the release around four concrete enterprise use cases: invoice/receipt line-item extraction, compliance document analysis (passports, IDs, tax forms), contract clause/date extraction, and healthcare/insurance claim processing, with a companion tutorial and notebook for building an invoice/receipt pipeline. The model is deployable via the NVIDIA NIM API or downloadable from Hugging Face, and can be fine-tuned on custom data with NVIDIA NeMo.

## Key Claims

- Llama Nemotron Nano VL outperforms other tested VLMs on OCRBench v2, a benchmark of 10,000+ human-verified real-world document QA pairs covering text localization, table parsing, diagram reasoning, and key-value extraction.
- The model also scores strongly on ChartQA and AI2D, cited as evidence of general chart/diagram reasoning beyond pure OCR.
- Vision backbone C-RADIOv2-VLM-H uses high-resolution tiling with dynamic patch-feature aggregation, letting the model handle documents of arbitrary aspect ratio at high resolution with reduced distortion versus naive resizing.
- Supports grounding: the model can predict bounding-box coordinates in normalized space for text-referring and table/element localization tasks.
- Pre-training uses ~1.5M samples (public + synthetic + internally curated); a substantial share of SFT data derives from NVIDIA's internal NeMo Retriever Parse OCR pipeline and its NVPDFTex arXiv-document dataset.
- Training used NVIDIA Megatron with Transformer Engine and Megatron Energon for multimodal dataloading; example training/inference scripts are released.

## Figures

No figures were extracted for this ingest; the source article's dataset-composition figures (pre-training data mix, SFT task distribution) and example table/VQA/text-extraction outputs are referenced inline in the summary above but not downloaded, per this batch's no-figure-download policy.

## Entities

- [[NVIDIA]] — publishing organization; Nemotron model family and NeMo Retriever Parse OCR pipeline.
- [[Hugging Face]] — hosts the blog post and the model weights.
- [[Papers Explained 187a - Llama 3]] — Llama-3.1-8B-Instruct is the language backbone this VLM is built on.

## Questions & Gaps

- The post does not give exact OCRBench v2 numerical scores for Llama Nemotron Nano VL versus the specific competing VLMs it outperforms, only that it leads the benchmark.
- C-RADIOv2-VLM-H's own training details (dataset size, distillation teacher models) are referenced but not fully specified in this post; readers are pointed to a separate model card.
- No comparison is given against NVIDIA's other Nemotron VLM releases in the same size class from this batch (e.g. Nemotron Nano Omni).

## Related

- [[Granite 4.0 3B Vision: Compact Multimodal Intelligence for Enterprise Documents]] — competing enterprise document-understanding VLM from IBM, targeting an overlapping set of table/chart/KVP extraction tasks.
- [[Papers Explained 187a - Llama 3]] — the language-model backbone.
- [[Document AI]] — topic page for document understanding and OCR model coverage.
- [[Vision Language Models]] — topic page for multimodal model coverage.
- [[NVIDIA]]
- [[Hugging Face]]
