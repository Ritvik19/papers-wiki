# Papers Explained: Gemma 4

Papers Explained: Gemma 4

Papers Explained: Gemma 4

A breakdown of Google’s native multimodal family. How per-layer embeddings, p-RoPE, and encoder-free 12B design match 27B performance.

Papers Explained 586: Gemma 4

Gemma 4 is a family of natively multimodal language models designed to advance compute efficiency and reasoning. It features dense and Mixture-of-Experts architectures, ranging from 2.3B to 31B parameters. Alongside improved vision and audio encoders for all model sizes, a unified, encoder-free architecture is proposed for the 12B model, which ingests raw audio and image patches.

Model Architecture

Gemma 4 models follow a decoder-only Transformer architecture. The models have pre-norm and post-norm with RMSNorm, and QKNorm.

The family comprises dense models, with effective 2.3B (E2B), effective 4.5B (E4B), 12B and 31B parameters, as well as an MoE model with 3.8B activated parameters for 26B total parameters (26B-A4B). The E2B and E4B models use per-layer embedding (PLE) making them 2.3B and 4.5B effective out of 5B and 8B total parameters respectively.
Parameter counts for the Gemma 4 models.
Long Context Efficiency

The local to global attention ratio patterns utilize 4-to-1 local attention blocks for E2B and 5-to-1 for the rest. Memory efficiency is improved by re-using keys as values in the global attention layers (except in E2B and E4B).

Position is encoded with 𝑝-RoPE with 𝑝 = 0.25 on global attention layers and with RoPE on local attention layers, effectively reducing the global KV cache by 37.5%. The RoPE frequencies are set to 1M and 10k on global and local attention layers, respectively. Finally, the KV cache is shared with ratios of 20/35 and 18/42 for the E2B and E4B model.

Vision modality

E2B and E4B Gemma models come with a 150M vision encoder, while larger models use a 550M encoder (except for the unified 12B). Both are Vision Transformers with a patch size of 16 and incorporate both axial 2D-RoPE with non-causal attention and 2D absolute positional embeddings.
Vision encoder architecture.
The vision encoders support variable aspect ratios:
Image resizing.Aspect-Ratio Preserving Image Resizing.
1. Compute the pooled patch size: Here, patches of size p×p are pooled using a kernel of size k, making each pooled patch m×m in size.
2. Compute the target number of pooled patches: This scales the target number of pooled patches so we do not exceed N_max tokens.
3. Calculate the ideal scaling factor: This finds the scale factor so that, after resizing, the image can be chunked into at most N_max tokens.
4 and 5. Compute the ideal resized height and width
6 and 7. Round dimensions to nearest pooled patch size: This guarantees the final dimensions are divisible by the pooled patch size.
8. Resize the image: The image is then bicubically resized to these computed dimensions.
9. Return the resized image

Audio modality

E2B and E4B Gemma models use a 305M audio encoder that processes audio in 40ms chunks with Mel filterbank inputs. The encoder architecture is based on the Universal Speech Model, consisting of two downsampling convolution layers followed by twelve Conformer layers. While the architecture remains similar to that of Gemma 3n, the number of parameters is reduced by 55% (from 680M to 305M). Vector quantization is not used; the LLM ingests the continuous representations produced by the audio encoder. As with the vision encoder, weights are kept frozen during pre-training.

Encoder-free architecture

Gemma 4 12B is trained from scratch based on a new, unified, and encoder-free model paradigm, replacing the separate vision and audio encoders with lightweight projection modules. For the vision modality, Gemma 4 12B takes in 48×48×3 RGB patches, but replaces the 550M vision encoder by a single large matmul (35M parameters). Spatial awareness is maintained by adding 2D coordinate-based positional embeddings directly to the patch representations before a final LayerNorm layer.

For audio, the 305M USM-based conformer encoder is entirely discarded. Raw audio is segmented into 40ms chunks at 16kHz, resulting in 640-dimensional vectors per chunk. These are projected directly into the LLM embedding space. Since audio is a temporal sequence, it does not require additional positional encoding.

Multi Token Prediction
The autoregressive MTP drafter.
A small autoregressive MTP drafter head is trained with the models, used for speculative decoding. In the MTP procedure, the model’s last layer activations from the previous step and token embeddings are fed into the MTP head. The MTP head generates future tokens sequentially using a separate embedder and a 4-layer Transformer block that cross-attends to the KVs of the main model, thus eliminating the need for MTP prefill and supporting any draft length. The Transformer block has model dimension 256 for E2B and E4B, 1024 for 26B-A4B and 31B, three local, and one global attention layers.

For the E2B and E4B drafters, the decoding overhead is reduced by replacing the projection operation to the entire vocabulary by a top-k operation on clusters of tokens. As a result, final matrix multiplication is reduced from 𝑑 × 262,000 to 𝑑 × 4096 while preserving a similar acceptance rate.

Per Layer Embedding

The fundamental concept involves augmenting the single input embedding with distinct layer-wise signals for every token. To optimize memory footprint, these per-layer embeddings use a reduced dimensionality (256, compared to the standard 1536 in E2B and 2056 in E4B) relative to the primary lookup table.

During the initial inference phase, the system retrieves the full set of embeddings for each input token. Each token is associated with a specific embedding for every layer. This retrieval occurs as a single operation, ensuring computational efficiency by eliminating the need for repeated lookups as individual layers are activated.

A gating mechanism processes these representations between decoder blocks, determining the relative weights for the values within a selected embedding. This enables the model to selectively emphasize specific features of the retrieved representation. The gated embedding, maintaining its 256-dimensional size, is subsequently projected to align with the primary model dimension.

Following a normalization step, this weighted signal is integrated with the output from the preceding decoder block. This architecture ensures the processed representations remain anchored to the original token identity, preventing the initial signal from being obscured by the accumulation of contextual information across successive layers.

Despite their substantial size (262,144 x 35 x 256), these per-layer embeddings are maintained in flash memory. Since only a limited subset of embeddings is required during inference, utilizing (V)RAM for storage is avoided. Consequently, the “E” designation in E2B and E4B refers to the total parameter count excluding these per-layer embedding structures.

Pre-training

The pre-training dataset is a large-scale, diverse collection of data from a wide range of domains and modalities, including web documents, code, images, and audio, with a cutoff date of January 2025. The same tokenizer as Gemini 2.5 is used; that is, a SentencePiece tokenizer with split digits, preserved whitespace, and byte-level encodings. The vocabulary has 262k entries.

Instruction Tuning
Formatting for Gemma IT models.
Careful optimization of the data used in post-training maximizes model performance. Examples that show certain personal information, unsafe or toxic model outputs, mistaken self-identification data, and duplicated examples are filtered out. Including subsets of data that encourage better in-context attribution, hedging, and refusals to minimize hallucinations also improves performance on factuality metrics, without degrading model performance on other metrics.

Evaluations

Human evaluation was conducted using Arena benchmarks, featuring blind side-by-side assessments by human raters against other state-of-the-art models.

Automated benchmarks were used for general performance, vision benchmarks, and multilingual audio tasks, as well as tests on long-context capabilities.
Leading open-weight models on Arena Text.
Gemma 4 31B achieves the highest performance among open dense models according to Elo scores, and both Gemma 4 31B and 26B-A4B match the performance of much larger open models.
Performance comparison of Gemma 3 27B and Gemma 4 models on diverse benchmarks.
Compared to Gemma 3 27B, Gemma 4 31B shows significantly better results across a variety of static benchmarks.
The E2B model achieves performance on par with Gemma 3 27B but with 10x fewer parameters, representing high parameter efficiency
Gemma 4 models performance on vision benchmarks at different resolutions.
On vision benchmarks, Gemma 4 models (notably E4B) perform as well as or better than Gemma 3 27B across all tasks evaluated
Audio performance for Gemma 4 and Gemma 3n models.Audio performance of Gemma 4 12B model on supported languages.
E2B and E4B, as well as 12B, demonstrate strong multilingual audio transcription and translation performance.
Long context performance of Gemma 3 and Gemma 4 models.
A substantial improvement in long-context capabilities is observed in Gemma 4 models, with E4B clearly outperforming Gemma 3 27B.

Paper

Gemma 4 Technical Report 2607.02770

That’s a wrap!

If you enjoyed this breakdown, follow for more. I publish new paper explanations most weekdays.

More papers in this series, organized by lab and topic, are in the start here guide.

What’s the paper you most want covered next? Let me know below.

Interested in how the Gemma architecture evolved across all its versions? Find every Gemma paper here.

By Ritvik Rastogi on August 3, 2026.

Canonical link

Exported from Medium on August 22, 2026.
