Source URL: https://huggingface.co/blog/ibm-granite/granite-4-vision
Title: Granite 4.0 3B Vision: Compact Multimodal Intelligence for Enterprise Documents
Published: March 31, 2026

# Granite 4.0 3B Vision: Compact Multimodal Intelligence for Enterprise Documents

IBM announces Granite 4.0 3B Vision, a compact vision-language model (VLM) for enterprise document understanding, purpose-built for reliable information extraction from complex documents, forms, and structured visuals. It excels at:

- Table Extraction: parsing complex table structures (multi-row, multi-column) from document images.
- Chart Understanding: converting charts and figures into structured machine-readable formats, summaries, or executable code.
- Semantic Key-Value Pair (KVP) Extraction: identifying and grounding semantically meaningful key-value field pairs across diverse document layouts.

The model ships as a LoRA adapter on top of Granite 4.0 Micro (the dense language model), keeping vision and language modular so the same deployment can serve both multimodal and text-only workloads, falling back to the base model automatically when vision is not needed. It also supports general image-to-text tasks (e.g. "Describe this image in detail") and can be used standalone or with Docling for document processing pipelines.

## How it was built

Three investments drive performance: a purpose-built chart-understanding dataset via code-guided data augmentation, a DeepStack variant for high-detail visual feature injection, and a modular LoRA-adapter design.

### ChartNet

ChartNet is a million-scale multimodal dataset for chart interpretation and reasoning (detailed in an upcoming CVPR 2026 paper). It uses a code-guided synthesis pipeline generating 1.7 million diverse chart samples spanning 24 chart types and 6 plotting libraries. Each sample has five aligned components: plotting code, rendered image, data table, natural language summary, and QA pairs, giving the model a cross-modal view of what a chart means rather than just what it looks like. The dataset also includes human-annotated and real-world subsets filtered for visual fidelity, semantic accuracy, and diversity.

### DeepStack visual feature injection

Most VLMs inject visual information at a single point, forcing the model to handle high-level semantics and fine-grained spatial detail simultaneously. Granite 4.0 3B Vision uses DeepStack Injection: abstract visual features are routed into earlier layers for semantic understanding, while high-resolution spatial features feed into later layers to preserve detail. This matters for tasks like table extraction, chart understanding, and KVP parsing where layout matters as much as content.

### Modularity

Packaging as a LoRA adapter on Granite 4.0 Micro means the same deployment serves both multimodal and text-only workloads without sacrificing performance, simplifying enterprise integration.

## Performance

- Charts (ChartNet benchmark, LLM-as-judge): Chart2Summary 86.4% (highest among evaluated models, including larger ones); Chart2CSV 62.1% (second, behind Qwen3.5-9B at 63.4%, a model more than double its size).
- Tables (TEDS metric across TableVQA-extract, OmniDocBench-tables, PubTables-v2, cropped and full-page settings): strongest performance across benchmarks — PubTablesV2 cropped 92.1 and full-page 79.3, OmniDocBench 64.0, TableVQA 88.1.
- Semantic KVP (VAREX benchmark, 1,777 U.S. government forms spanning simple to complex nested/tabular layouts, exact-match metric): 85.5% EM accuracy zero-shot.

## How to use it

Two modes: (1) stand-alone image understanding for targeted visual extraction without modifying upstream systems, suitable for lightweight task-specific tools; (2) integrated with Docling for end-to-end document understanding across multi-page PDFs, with Docling handling detection/segmentation/cropping of figures and tables before routing clean crops to Granite Vision for fine-grained extraction.

Example use cases: form processing (invoices, forms, receipts via KVP or image2text), financial report analysis (Docling + chart2csv/chart2code + tables_json), and research document intelligence (Docling OCR/layout parsing + chart2summary + tables_html).

## Availability

Granite 4.0 3B Vision is available on Hugging Face under the Apache 2.0 license, with full technical details and benchmark results in the model card.
