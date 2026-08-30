# Papers Explained 574: Jina Embeddings v5 Omni

Papers Explained 574: Jina Embeddings v5 Omni

Papers Explained 574: Jina Embeddings v5 Omni

GELATO (Geometry-preserving Embeddings via Locked Aligned TOwers) is a multimodal embedding approach that extends Jina Embeddings v5 Text…

Papers Explained 574: Jina Embeddings v5 Omni

GELATO (Geometry-preserving Embeddings via Locked Aligned TOwers) is a multimodal embedding approach that extends Jina Embeddings v5 Text models to encode text, image, audio, and video into a unified semantic space by adding frozen non-text encoders and training only the small connecting components to produce Jina Embeddings v5 Omni.

Architecture
Architecture of jina-embeddings-v5-omni.
Jina Embeddings v5 Text is extended from text-only embedding to vision and audio by adding scale-matched Qwen3.5 vision encoders and the Qwen2.5-Omni audio encoder to the same text-sequence backbone. Encoders from trained multi-modal language systems are chosen rather than bare perceptual encoders such as SigLIP2 or Whisper-large because prior work shows that visual and audio features need explicit language-space alignment or natural-language supervision before they transfer reliably to text-conditioned multimodal tasks.

The text processing path of jina-embeddings-v5-omni is identical to Jina Embeddings v5 Text: Token embeddings pass through the frozen text transformer, the inherited task LoRA adapter is applied, and the final embedding is produced by last-token pooling and L2 normalization.

Since the output dimensions of the image and audio encoders do not match Jina Embeddings v5 Text’s input, we replace the source projection layers with new projectors that map into the text hidden space.

For audio, a randomly-initialized fc_audio layer is inserted that projects the encoder’s native 1280 dimension output into jina-embeddings-v5-omni-small’s 1024-dimension input space and jina-embeddings-v5-omni-nano’s 768-dimension one.

For vision, the Qwen3.5 visual projector converts ViT patch tokens into text-token features by applying LayerNorm, a 2×2 spatial merge, fc_vision_1, GELU, and fc_vision_2. Here, LayerNorm denotes feature normalization on the ViT patch tokens. The 2×2 spatial merge is a fixed space-to-depth (pixel-unshuffle) rearrangement that concatenates four neighboring patch embeddings into one 4𝑑vit vector, reducing the spatial token count by 4×.

Input Sequence Construction

An image is encoded with N visual slots as:

An audio is encoded with K audio slots as:

A video is a concatenation of one visual segment per sampled frame:

where ∥ denotes sequence concatenation. If a video contains an audio track, the extracted audio segment precedes the frame sequence:

For mixed-modality inputs, text spans and modality segments are concatenated in document order.

Trainable Parameters

The trainable set is fc_vision_2, fc_audio, and the modality delimiter embeddings.

jina-embeddings-v5-omni-small learns the vision and audio start/end delimiter embeddings

jina-embeddings-v5-omni-nano learns only the audio start/end delimiter embeddings. The image, video, and audio place holder positions are overwritten by projected encoder features rather than learned as standalone token embeddings.

Projector and delimiter-token training is run separately for retrieval, text-matching, clustering, and classification, while the text transformer, encoder towers, LayerNorm/fc_vision_1 vision-projector weights, and inherited LoRA adapters stay frozen. The base package stores four such task-specific sets alongside the inherited LoRA adapters.

Training

Projector training uses bidirectional in-batch InfoNCE with Matryoshka representation learning. For a batch of 𝐵 paired examples, let u𝑖 and v𝑖 be the left and right embeddings, and let u𝑖,1:𝑘 denote the first 𝑘 dimensions. With temperature 𝜏 = 0.02

The training loss sums this term over Matryoshka prefix dimensions:

Evaluations

Benchmarks:

Massive Image Embedding Benchmark (MIEB) for images.
Massive Multimodal Embedding Benchmark (MMEB-Video) for videos.
Massive Audio Embedding Benchmark (MAEB) for audio.
Massive Multilingual Text Embedding Benchmark (MMTEB) for text.
ViDoRe for page-level document retrieval.

Open-weight omni-style model scores on selected evaluation subsets.

jina-embeddings-v5-omni-small achieves the strongest text-only performance and the best overall four-modality score among models under 5B parameters (53.93), slightly above LCO-Embedding-Omni-3B and only behind the larger LCO-Embedding-Omni-7B.
Competitive on images and audio, but video performance is notably weaker compared to baselines.
Document-retrieval scores on the ViDoRe-in-MIEB subset.
Both jina-embeddings-v5-omni-nano and small show strong visual document retrieval results, with small scoring 79.08 (above LCO-Embedding-Omni-3B and close to LCO-Embedding-Omni-7B), and nano scoring 70.05 (much better than LanguageBind for its size) on the ViDoRe MIEB subset.

Main benchmark results.

jina-embeddings-v5-omni-small performs best in image classification, image clustering, visual semantic textual similarity, multilingual image retrieval, and audio classification, but is weaker for generic image retrieval, MMEB-Video, and audio clustering.

Paper

jina-embeddings-v5-omni: Geometry-preserving Embeddings via Locked Aligned Towers 2605.08384

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on June 4, 2026.

Canonical link

Exported from Medium on June 13, 2026.
