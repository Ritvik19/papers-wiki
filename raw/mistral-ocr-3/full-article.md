# Introducing Mistral OCR 3

**Source URL**: https://mistral.ai/news/mistral-ocr-3/  
**Published**: December 17, 2025  
**Author**: Mistral AI

## Highlights

- **74% overall win rate** over Mistral OCR 2 on forms, scanned documents, complex tables, and handwriting
- State-of-the-art accuracy vs. enterprise document processing and AI-native OCR solutions
- Powers **Document AI Playground** in Mistral AI Studio (drag-and-drop PDF/image → text or structured JSON)
- Major upgrade on forms, handwriting, low-quality scans, and tables

## Overview

Mistral OCR 3 extracts text and embedded images from diverse documents with high fidelity. Markdown output includes **HTML-based table reconstruction** for structure-aware downstream use. Smaller than most competitors; priced at **$2 per 1,000 pages** ($1 with 50% Batch API discount).

API model id: **`mistral-ocr-2512`**. Document AI UI available in Mistral AI Studio.

## Upgrades over prior OCR models

General-purpose (not single document-type specialized):

- **Handwriting:** cursive, mixed annotations, handwritten text over printed forms
- **Forms:** boxes, labels, handwritten entries, dense layouts (invoices, receipts, compliance, government docs)
- **Scanned/complex docs:** robust to compression, skew, distortion, low DPI, noise
- **Complex tables:** headers, merged cells, multi-row blocks, column hierarchies; HTML `colspan`/`rowspan` output

## Recommended use cases

High-volume enterprise pipelines and interactive workflows: markdown extraction for agents/knowledge systems, automated form/invoice parsing, end-to-end document understanding, handwriting/historical digitization.

Early customers: invoice field extraction, archive digitization, clean text from technical/scientific reports, enterprise search.

## Availability

API and Document AI Playground in Mistral AI Studio. Backward compatible with Mistral OCR 2. Selective self-host for data-privacy requirements.
