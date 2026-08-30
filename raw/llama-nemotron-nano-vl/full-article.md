Source URL: https://huggingface.co/blog/nvidia/llama-nemotron-nano-vl
Title: Welcome the NVIDIA Llama Nemotron Nano VLM to Hugging Face Hub
Published: June 27, 2025

# Welcome the NVIDIA Llama Nemotron Nano VLM to Hugging Face Hub

NVIDIA Llama Nemotron Nano VL is a state-of-the-art 8B Vision Language Model (VLM) designed for intelligent document processing, offering high accuracy and multimodal understanding. It excels at extracting and understanding information from complex documents like invoices, receipts, contracts, and more, with strong OCR capabilities and industry-leading accuracy on the OCRBench v2 benchmark for text/table extraction and chart/diagram/table parsing.

## High-accuracy OCR

Llama Nemotron Nano VL is evaluated on OCRBench v2, a benchmark of real-world OCR and document understanding tasks (text recognition, table extraction, element parsing across document types):

- Text Recognition: high accuracy in real-world OCR tasks such as invoice processing.
- Element Parsing: accurately identifies and extracts tables, charts, and images.
- Table Extraction: highly accurate extraction of tabular data, suitable for financial statements.
- Grounding: supports grounding via bounding boxes in both queries and outputs.

## Model architecture and innovations

The model builds on Llama-3.1-8B-Instruct and C-RADIOv2-VLM-H, a Vision Transformer (ViT) backbone for visual feature extraction that handles complex visual elements like charts, graphs, and diagrams.

### Core technologies

- **C-RADIOv2-VLM-H vision backbone**: trained on multi-resolution data using multiple distillation techniques, with multiplicative noise applied to weights during training for generalization. The model dynamically aggregates encoded patch features to support high-resolution input without sacrificing spatial continuity, processing documents of arbitrary aspect ratios with less distortion via high-resolution tiling.
- **High-quality document intelligence data**: trained using several open-source datasets plus data from NVIDIA's NeMo Retriever Parse VLM-based OCR solution, including synthetic table-extraction datasets. This gives text/table parsing and grounding capabilities.
  - Pre-training (~1.5M samples, public + synthetic + internally curated) trains a Multi-Layer Perceptron (MLP) connector for cross-modal alignment between language and vision.
  - Supervised Fine-Tuning trains end-to-end on synthetic, public, and internally curated datasets covering OCR, text grounding, table parsing, and document VQA, including reading-order prediction, markdown reconstruction with semantic classes (Captions, Titles, Section headers), bounding boxes, LaTeX formula parsing, and table extraction in LaTeX/HTML/markdown. Affine and photometric augmentations improve robustness; tables/charts are swapped between datasets to diversify layouts. Internal datasets include NVPDFTex (arXiv documents with ground-truth reading order, bounding boxes, semantic classes, LaTeX tables/equations), human-annotated Common Crawl PDFs, rendered Wikipedia text, and refined public datasets (DocLayNet, FinTabNet, PubTables-1M).

Training used NVIDIA Megatron, efficient Transformer Engine implementations, and Megatron Energon for multimodal dataloading. Example Megatron training/inference scripts are provided.

## OCRBench v2 benchmark

OCRBench v2 includes over 10,000 human-verified question-answer pairs assessing visual text localization, table parsing, diagram reasoning, and key-value extraction. Llama Nemotron Nano VL outperforms other VLMs on this benchmark and also scores strongly on ChartQA and AI2D.

## Advanced use cases

1. Invoice and Receipt Processing — extracting line items, totals, dates for accounting/ERP/expense management.
2. Compliance Document Analysis — structured data from passports, IDs, tax forms for KYC/regulatory compliance.
3. Contract Review — identifying key clauses, dates, obligations in legal documents.
4. Healthcare and Insurance Automation — extracting patient data, claim information, policy details.

## Getting started

The model is available via the NVIDIA NIM API and for download on Hugging Face; NVIDIA NeMo can be used to fine-tune it on custom datasets. A hands-on tutorial and notebook/video walk through building an invoice/receipt document intelligence pipeline.

## Contributors

Amala Sanjay Deshmukh, Kateryna Chumachenko, Tuomas Rintamaki, Matthieu Le, and a large NVIDIA team (full list in the source article).
