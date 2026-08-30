# Papers Explained 536: DeepSeek-OCR 2

Papers Explained 536: DeepSeek-OCR 2

Papers Explained 536: DeepSeek-OCR 2

DeepSeek-OCR 2 investigates the feasibility of a novel encoder DeepEncoder V2 capable of dynamically reordering visual tokens upon image…

Papers Explained 536: DeepSeek-OCR 2

DeepSeek-OCR 2 investigates the feasibility of a novel encoder DeepEncoder V2 capable of dynamically reordering visual tokens upon image semantics. Conventional vision-language models invariably process visual tokens in a rigid raster-scan order with fixed positional encoding when fed into LLMs. DeepEncoder V2 is designed to provide the encoder with causal reasoning capabilities, enabling it to intelligently reorder visual tokens prior to LLM-based content interpretation. This work explores a novel paradigm: whether 2D image understanding can be effectively achieved through two-cascaded 1D causal reasoning structures, thereby offering a new architectural approach with the potential to achieve genuine 2D reasoning.

Architecture

DeepSeek-OCR 2.

DeepSeek-OCR 2 inherits the overall architecture of DeepSeek-OCR, which consists of an encoder and a decoder. The encoder discretizes images into visual tokens, while the decoder generates outputs conditioned on these visual tokens and text prompts. The key distinction lies in the encoder: DeepEncoder is upgraded to DeepEncoder V2, which retains all capabilities of its predecessor while introducing causal reasoning through a novel architectural design.

DeepEncoder V2
DeepEncoder V2.
The first component of DeepEncoder V2 is a vision tokenizer. Following DeepEncoder, an architecture combining an 80M-parameter SAM-base along with two convolutional layers is employed. The output dimension of the final convolutional layer is reduced from 1024 in DeepEncoder to 896 to align with the subsequent pipeline. This compression-based tokenizer is not mandatory and can be replaced with simple patch embedding. It is retained because it achieves 16×token compression through window attention with minimal parameters, significantly reducing both computational cost and activation memory for the subsequent global attention module. Moreover, its parameter count (80M) remains comparable to the typical 100M parameters used for text input embeddings in LLMs.

In DeepEncoder, a CLIP ViT follows the vision tokenizer to compress visual knowledge. DeepEncoder V2 redesigns this component into an LLM-style architecture with a dual-stream attention mechanism. Visual tokens utilize bidirectional attention to preserve CLIP’s global modeling capability, while newly introduced causal flow queries employ causal attention. These learnable queries are appended after visual tokens as a suffix, where each query attends to all visual tokens and preceding queries. By maintaining equal cardinality between queries and visual tokens, this design imposes semantic ordering and distilling on visual features without altering token count. Finally, only the causal query outputs are fed to the LLM decoder.

This architecture is instantiated using Qwen2–0.5B, whose 500M parameters are comparable to CLIP ViT (300M) without introducing excessive computational overhead. This architecture establishes two-stage cascade causal reasoning: the encoder semantically reorders visual tokens through learnable queries, while the LLM decoder performs autoregressive reasoning over the ordered sequence.

Causal flow query
Token count calculation in DeepEncoder V2.
The number of causal query tokens equals the number of visual tokens, computed as 𝑊×𝐻 / 16 ×16, where 𝑊 and 𝐻 denote the width and height of the image input to the encoder. To avoid maintaining multiple query sets for different resolutions, a multi-crop strategy with fixed query configurations at predefined resolutions is adopted. Specifically, the global view uses a resolution of 1024 ×1024, corresponding to 256 query embeddings denoted as queryglobal. Local crops adopt a resolution of 768 ×768, with the number of crops 𝑘 ranging from 0 to 6 (no cropping is applied when both image dimensions are smaller than 768). All local views share a unified set of 144 query embeddings, denoted as querylocal. Therefore, the total number of reordered visual tokens fed to the LLM is 𝑘×144 +256, ranging from [256, 1120]. This maximum token count (1120) is lower than DeepSeek-OCR’s 1156 (Gundam mode).

Attention mask
Attention mask architecture of DeepEncoder V2.
The attention mask is composed of two distinct regions. The left region applies bidirectional attention (similar to ViT) to original visual tokens, allowing full token-to-token visibility. The right region employs causal attention (triangular mask, identical to decoder-only LLMs) for causal flow tokens, where each token attends only to previous tokens. These two components are concatenated along the sequence dimension to construct DeepEncoder V2’s attention mask (M):

where 𝑛 is the number of causal query tokens, 𝑚 represents vanilla visual tokens number, and LowerTri denotes a lower triangular matrix.

DeepSeek-MoE Decoder

DeepSeek-OCR 2 primarily focuses on encoder improvements. The decoder component is not upgraded, retaining DeepSeek-OCR’s decoder−a 3B-parameter MoE structure with about 500M active parameters. The core forward pass of DeepSeek-OCR 2 can be formulated as:

where I ∈R𝐻×𝑊×3 is the input image, E is the vision tokenizer mapping images to 𝑚 visual tokens V ∈R𝑚×𝑑, Q0 ∈R𝑛×𝑑 are learnable causal query embeddings, ⊕ denotes sequence concatenation, T𝐿 represents an 𝐿-layer Transformer with masked attention, M ∈{0, 1}2𝑛×2𝑛 is the block causal attention mask defined, 𝜋𝑄 is the projection operator that extracts the last 𝑛tokens (i.e., Z= X𝑚+1:𝑚+𝑛), D is the language decoder, and O ∈R𝑛×|V|is the output logits over LLM vocabulary.

Training

Data Engine

DeepSeek-OCR 2 employs the same data sources as DeepSeek-OCR, comprising OCR 1.0, OCR 2.0, and general vision data, with OCR data constituting 80% of the training mixture. Two modifications are introduced: (1) a more balanced sampling strategy for OCR 1.0 data, partitioning pages by content type (text, formulas, tables) with a 3:1:1 ratio, and (2) label refinement for layout detection by merging semantically similar categories (e.g., unifying “figure caption” and “figure title”). Given these minimal differences, DeepSeek-OCR is considered a valid baseline for comparison.

Training Pipelines

DeepSeek-OCR 2 is trained in three stages:

Encoder pretraining: enables the vision tokenizer and LLM-style encoder to acquire fundamental capabilities in feature extraction, token compression, and token reordering capabilities.
Query enhancement: further strengthens the token reordering capability of the encoder while enhancing visual knowledge compression.
Decoder specialization: freezes the encoder parameters and optimizes only the decoder, enabling higher data throughput under the same FLOPs.

Encoder pretraining

DeepEncoder V2 is trained using a language modeling objective, coupling the encoder with a lightweight decoder for joint optimization via next token prediction. Two dataloaders at resolutions of 768×768 and 1024×1024 are employed. The vision tokenizer is initialized from DeepEncoder, and the LLM-like encoder from Qwen2–0.5B-base. After pretraining, only the encoder parameters are retained for subsequent stages.

Query enhancement

After DeepEncoder V2 pretraining, DeepSeek-3B-A500M [24, 25] is integrated as the final pipeline. The visual tokenizer (SAM-conv structure) is frozen while jointly optimizing the LLM encoder and LLM decoder to enhance query representations. At this stage, the two resolutions are unified into a single dataloader via a multi-crop strategy.

Decoder specialization

To rapidly consume training data, all DeepEncoder V2 parameters are frozen in this stage and only DeepSeek-LLM parameters are updated. This stage accelerates training while helping the LLM better understand DeepEncoder V2’s reordered visual tokens.

Evaluation

Overall Benchmark Performance (OmniDocBench)
Comprehensive evaluation of document reading on OmniDocBench v1.5.
DeepSeek-OCR 2 achieves 91.09% overall performance with the smallest V-tokenₘₐₓ, showing strong accuracy under tight visual token constraints.
Compared to the DeepSeek-OCR baseline, DeepSeek-OCR 2 improves by +3.73 percentage points under similar training data, confirming the benefit of the new architecture.
Reading order ED improves from 0.085 → 0.057, indicating better selection and ordering of visual tokens by DeepEncoder V2.

Element-wise Document Parsing
Edit Distances for different categories of document-elements in OmniDocBench v1.5.
Under a similar visual token budget (V-tokenₘₐₓ = 1120), DeepSeek-OCR 2 achieves:
Overall ED = 0.100, better than Gemini-3 Pro’s 0.115.
Lower ED across document elements (text, formula, table, R-order) compared to DeepSeek-OCR and Gemini-3 Pro in most cases.

Per-Document-Type Performance and Headroom
Detailed comparison between DeepSeek-OCR 2 and DeepSeek-OCR across 9 document types.
Across 9 document types, DeepSeek-OCR 2 generally has lower text ED than DeepSeek-OCR, indicating better text recognition in most categories (e.g., PPT, academic papers, books, colorful textbooks, exam papers, magazines, notes, research reports).
Newspapers remain a weakness: Text ED for DeepSeek-OCR 2 is > 0.13, worse than in other categories.
Authors attribute this to:
Low V-tokenₘₐₓ, which harms recognition in text-dense layouts like newspapers.
Insufficient training data for newspapers (only ~250k samples), limiting DeepEncoder V2’s specialization.
For reading order (R-order), DeepSeek-OCR 2 consistently outperforms DeepSeek-OCR across all document types, supporting the effectiveness of the visual causal flow encoder design.

Practical Readiness in Production
Production performance comparison between DeepSeek-OCR and DeepSeek-OCR 2.
In real production settings (no ground truth), repetition rate is used as the main quality metric:
Online user-log images: repetition rate reduced from 6.25% → 4.17% (Δ = –2.08%).
Pretrain PDF data: repetition rate reduced from 3.69% → 2.88% (Δ = –0.81%).
These reductions indicate fewer redundant or repeated outputs when DeepSeek-OCR 2 is used in:
Online OCR service for DeepSeek-LLMs.
Batch PDF processing in the pretraining data pipeline.

Paper

DeepSeek-OCR 2: Visual Causal Flow 2601.20552

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on February 9, 2026.

Canonical link

Exported from Medium on May 4, 2026.
