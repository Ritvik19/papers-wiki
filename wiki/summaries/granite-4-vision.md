# Granite 4.0 3B Vision: Compact Multimodal Intelligence for Enterprise Documents

**Source**: `raw/granite-4-vision/full-article.html` (173 KB), `raw/granite-4-vision/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

Granite 4.0 3B Vision is IBM's compact vision-language model for enterprise document understanding, built as a LoRA adapter on top of the Granite 4.0 Micro dense language model rather than a standalone model. That packaging choice is deliberate: the same deployment can serve multimodal and text-only requests interchangeably, falling back to the base Granite 4.0 Micro model automatically when an input has no image, which keeps enterprise integration simple. The model targets three specific enterprise extraction tasks: table extraction from complex multi-row/multi-column layouts, chart understanding (converting charts into structured data, summaries, or executable code), and semantic key-value pair (KVP) extraction from diverse document layouts (invoices, forms, government documents).

Two technical contributions drive the model's performance on these tasks. ChartNet is a new million-scale chart-understanding dataset (detailed in an upcoming CVPR 2026 paper) built with a code-guided synthesis pipeline that generates 1.7 million chart samples across 24 chart types and 6 plotting libraries; each sample includes five aligned components (plotting code, rendered image, data table, natural-language summary, and QA pairs), giving the model a genuinely cross-modal view of what a chart encodes rather than just what it looks like. The dataset also includes filtered human-annotated and real-world subsets. The second contribution is a DeepStack-style visual feature injection scheme: instead of injecting visual features into the language model at one point, abstract semantic features go into earlier layers while high-resolution spatial features go into later layers, which the authors argue is why the model handles layout-sensitive tasks like table and KVP extraction well despite its small size.

On IBM's own benchmark suite, Granite 4.0 3B Vision leads or is competitive with substantially larger models: it posts the top Chart2Summary score among all models tested (including much larger ones) and a close second on Chart2CSV behind a model more than double its parameter count. On table extraction it leads across all three benchmark datasets tested (cropped and full-page settings), and it hits 85.5% exact-match accuracy zero-shot on a semantic KVP benchmark built from 1,777 U.S. government forms. IBM positions the model for two deployment patterns: standalone use on individual images for lightweight extraction tools, or integration with Docling for full end-to-end multi-page PDF pipelines where Docling handles page segmentation and Granite Vision handles fine-grained extraction on the cropped regions.

## Key Claims

- Packaged as a LoRA adapter on Granite 4.0 Micro, not a standalone model; the same deployment serves both multimodal and text-only workloads with automatic fallback.
- ChartNet: 1.7M synthetic chart samples across 24 chart types and 6 plotting libraries, each with five aligned components (code, image, table, summary, QA); plus filtered human-annotated and real-world subsets. Full methodology reserved for an upcoming CVPR 2026 paper.
- DeepStack-style injection routes abstract semantic visual features into earlier language-model layers and high-resolution spatial features into later layers, rather than injecting all visual information at a single point.
- Chart benchmark (LLM-as-judge on the ChartNet human-verified set): Chart2Summary 86.4% (highest of all models evaluated); Chart2CSV 62.1% (second, behind Qwen3.5-9B's 63.4%, a model more than 2x the size).
- Table extraction (TEDS metric): leads on PubTablesV2 cropped (92.1) and full-page (79.3), OmniDocBench (64.0), and TableVQA-extract (88.1), across all evaluated models on these benchmarks.
- Semantic KVP extraction: 85.5% exact-match accuracy, zero-shot, on the VAREX benchmark (1,777 U.S. government forms spanning simple to complex nested/tabular layouts).

## Figures

No figures were extracted for this ingest; the source article's ChartNet pipeline diagram and chart/table/KVP benchmark comparison charts are referenced inline in the summary above but not downloaded, per this batch's no-figure-download policy. Numeric results are preserved as text above.

## Entities

- [[IBM]] — releasing organization; Granite model family.
- [[Hugging Face]] — hosts the blog post and model weights.

## Questions & Gaps

- The full ChartNet dataset methodology and generation pipeline details are deferred to an unpublished CVPR 2026 paper; only a high-level description is given here.
- The post does not specify how large the "significantly larger" chart-understanding baseline models are, beyond naming Qwen3.5-9B for the Chart2CSV comparison.
- No comparison is given against NVIDIA's competing enterprise document VLM from this same batch (Llama Nemotron Nano VL), despite targeting an overlapping use case.

## Related

- [[Welcome the NVIDIA Llama Nemotron Nano VLM to Hugging Face Hub]] — competing enterprise document-understanding VLM from NVIDIA, targeting overlapping table/chart/KVP extraction tasks.
- [[Granite Embedding Multilingual R2]] — sibling IBM Granite 4.x release from the same period, covering embeddings rather than vision.
- [[Document AI]] — topic page for document understanding and OCR model coverage.
- [[Vision Language Models]] — topic page for multimodal model coverage.
- [[IBM]]
- [[Hugging Face]]
