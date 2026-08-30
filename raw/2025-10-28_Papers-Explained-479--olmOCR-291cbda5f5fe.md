# Papers Explained 479: olmOCR

Papers Explained 479: olmOCR

Papers Explained 479: olmOCR

Traditional open source tools often produce lower quality extractions compared to vision language models, but reliance on the best VLMs can…

Papers Explained 479: olmOCR

Traditional open source tools often produce lower quality extractions compared to vision language models, but reliance on the best VLMs can be prohibitively costly or infeasible if the PDFs cannot be sent to proprietary APIs. olmOCR is an open-source toolkit for processing PDFs into clean, linearized plain text in natural reading order while preserving structured content like sections, tables, lists, equations, and more. The toolkit runs a fine-tuned 7B VLM trained on olmOCR-mix-0225, a sample of 260,000 pages from over 100,000 crawled PDFs with diverse properties, including graphics, handwritten text and poor quality scans. To aid comparison with existing systems, olmOCR-Bench, a curated set of 1,400 PDFs capturing many content types that remain challenging even for the best tools and VLMs, including formulas, tables, tiny fonts, old scans, and more, is introduced.

The data and models are available at HuggingFace.

Creating and Training on olmOCR mix

PDFs are randomly sampled from an internal dataset of 240 million PDFs crawled from public internet sites, as well as PDFs of public domain books sourced from the Internet Archive. While the web crawled set is often born-digital documents, PDFs from the Internet Archive consist of image scans. Using the Lingua package, non-English documents are identified and filtered out. Further, any document that failed to be parsed by pypdf, contains spam keywords, is a fillable form, or whose text is too short is removed. Three pages are then sampled uniformly at random from each PDF.

GPT-4o was used to reliably convert PDF pages to linearized plain text. GPT-4o, however, does not produce sufficiently high-fidelity plain text on its own; for high-density pages or complex layouts, it is prone to omitting content, rewriting or completing content in a manner unfaithful to the original, or captioning images when not instructed to do so. To help guide GPT-4o generations, document-anchoring was experimented with. This approach augments the visual input (PDF page raster) with text blocks and position information extracted from the page.

The pypdf library was used to extract a representation of the page’s structure from the PDF’s internal data. This representation is highly noisy: reading order is not preserved and main content is interwoven with boilerplate text and PDF rendering-related artifacts. Blocks were sampled from this long extraction to add to the prompt until maximum input length was exceeded; text blocks and images located at the start and end of the document were prioritized.

Finally, GPT-4o was instructed to respond with structured output to requests. This forces the model to first extract page metadata, such as language, page orientation, and presence of tables, before generating the text of the page in a natural reading order.
olmOCR-mix-0225 composition.
Model Training

Starting from a Qwen2-VL-7B-Instruct checkpoint, the olmOCR-7B-0225-preview is fine-tuned on using olmOCR-mix-0225. During fine-tuning, the document-anchoring prompt is slightly altered. Some instructions are removed and the image size is shrunk so that PDF pages are rendered to a maximum dimension of 1024 pixels on the longest edge. The prompt is capped to 6,000 characters, so a typical prompt uses about 1,000 tokens to encode a page image, 1,800 tokens for the anchor text, for about 3,000 total input tokens. Each training example was truncated to 8,192 tokens to cover cases when the prompt was unusually large. Loss was masked so only the final response tokens participated in the loss calculation.

Building olmOCR-Bench

olmOCR-Bench operates by assessing a series of predefined pass-or-fail “unit-tests”. Given an input whole PDF, does the plain text output satisfy a specific property or contain a specific element? Each test is designed to be simple, unambiguous, and deterministically machine-verifiable. olmOCR-Bench comprises 1,402 distinct PDF documents derived from diverse source repositories, covered by 7,010 unique test cases:
Counts of unit test types in olmOCR-Bench.
​​Text Presence:

Verifies that a specific text segment (typically 1–3 sentences) is correctly identified and present within the plain text output.
Allows for soft/fuzzy matching to accommodate slight variations.
Can specify if the text must be in the first N or last N characters of the document.
Case-sensitive by default.

Text Absence:

Verifies that a specific text segment is successfully excluded from the plain text output.
Primarily targets peripheral content like recurring headers, footers, and pagination markers.
Allows for soft/fuzzy matching.
Can specify if the text must be in the first N or last N characters of the document.
Not case-sensitive by default.

Natural Reading Order:

Verifies the correct order between two text segments.
Example: Checks if the first sentence of an article appears after the heading of that article.
Designed to avoid penalizing for the order of independent articles on the same page.
Allows for soft matching.
Case-sensitive by default.

Table Accuracy:

Checks that the plain text output contains a table with a cell containing a specific value, and that its neighboring cells have certain properties.
Example: Validates that a table contains a cell with “4.5%” and that the cell above it contains “2.4%”.
Supports both Markdown and HTML-based tables.

Math Formula Accuracy:

Checks that the plain text output contains a given math equation.
Renders a reference LaTeX equation using KaTeX in a headless browser.
Extracts all rendered symbols and their visual bounding boxes.
Checks if a matching collection of symbols, with the same relative orientations, exists in the OCR document.

Baseline:

Provides a default test case for each PDF document.
Ensures that some plain text output containing alphanumeric characters was produced.
Verifies that the output does not have a string of repeating N grams at the end (longer than 30).
Ensures that the output does not contain any characters from the Chinese, Japanese, or Emoji Unicode charsets (unless manually flagged as legitimate).

Sourcing Documents and Creating Tests

Seven distinct document types were found that olmOCR often struggled to process. Documents that contained PII and were not meant for public dissemination were removed.

arXiv Math (AR):

Downloaded papers from the math subset of arXiv with single TeX source files and corresponding PDFs.
Used olmOCR to identify pages with TeX expressions.
Matched pages back to the original TeX source.
Validated TeX rendering compatibility with KaTeX.
Manually verified test cases to exclude custom macros and split multi-part equations.

Old Scans Math (OSM):

Crawled old, public domain math textbooks from the Internet Archive.
Extracted random pages from these documents.
Used olmOCR to find candidate pages with formulas.
Manually annotated each formula on the page to use as test cases.

Tables (TA):

Sampled documents from an internal crawled PDF repository.
Filtered documents to those containing tables using a prompt with Gemini-Flash-2.0.
Prompted Gemini-Flash-2.0 for relationships between randomly chosen cells within the tables.
Manually reviewed the tests for accuracy.

Old Scans (OS):

Sampled historical letters and typewritten documents with existing human transcriptions from the Library of Congress digital archives.
Wrote a script to generate Natural Reading Order cases consisting of sentences that were naturally before or after one another in the original human transcriptions.
Manually added test cases to cover headers/footers that should be excluded.
Underwent a second pass of human review for accuracy.

Headers Footers (HF):

Sampled documents from the same internal crawled PDF repository as olmOCR-mix-0225.
Used DocLayout-YOLO to identify page regions labeled as headers or footers.
Visually masked out the rest of the document and prompted Gemini-Flash-2.0 for the content of the header/footer regions.
Added these extracted snippets as test cases that should be absent in linearized output.
Manually reviewed to remove mistakenly filtered text and set conditions (e.g., limiting the search area to the first N or last N characters).

Multi Column (MC):

Visually sampled documents from an internal crawled PDF repository to find documents with multi-column layouts and multiple articles on one page.
Used Claude-Sonnet-3.7 to render those pages to HTML.
Extracted text segments before/after one another from the HTML.
Manually reviewed each entry for accuracy.
Purposely selected simple text blocks from coherent regions, avoiding math formulas, superscripts, or subscripts.

Long Tiny Text (LTT):

Crawled documents from the Internet Archive containing a large amount of dense, small print on a single page.
Generated test cases using Gemini-Flash-2.0.
Verified them manually.

Evaluation
Evaluation results on olmOCR-Bench grouped by document types.
olmOCR significantly outperforms both the best commercial dedicated OCR tool (Mistral), its teacher model (GPT-4o), and Qwen 2.5 VL on olmOCR-Bench. Qualitatively, it produces significantly cleaner plain text.
Inference cost comparison against other OCR methods.
olmOCR is highly cost-efficient for real-world use. Processing a million pages with olmOCR is estimated to cost $178 which is over five times cheaper than Mistral OCR ($1,000) and substantially less expensive than GPT-4o ($12,480).

Paper

olmOCR: Unlocking Trillions of Tokens in PDFs with Vision Language Models 2502.18443

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on October 28, 2025.

Canonical link

Exported from Medium on May 4, 2026.
