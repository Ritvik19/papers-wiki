# Papers Explained 12: LiLT

Papers Explained 12: LiLT

Papers Explained 12: LiLT

The whole framework can be regarded as a parallel dual-stream Transformer. Given an input document image, first an off-the-shelf OCR engine…

Papers Explained 12: LiLT

The whole framework can be regarded as a parallel dual-stream Transformer. Given an input document image, first an off-the-shelf OCR engine is used to get text bounding boxes and contents. Then, the text and layout information are separately embedded and fed into the corresponding Transformer-based architecture to obtain enhanced features. Bi-directional attention complementation mechanism (BiACM) is introduced to accomplish the cross-modality interaction of text and layout clues. Finally, the encoded text and layout features are concatenated and additional heads are added upon them, for the self-supervised pre-training or the downstream fine-tuning.

Text Embeddings

where LN is the Layer Normalization

Layout Embeddings

All the bounding box coordinates are normalised and discretized to integers in the range [0, 1000], and four embedding layers are used to generate x-axis, y-axis, height and width features separately.

where CAT is the channel wise concatenation operation. The special tokens [CLS], [SEP] and [PAD] are also attached with (0, 0, 0, 0, 0, 0), (1000, 1000, 1000, 1000, 0, 0) and (0, 0, 0, 0, 0, 0) respectively.

BiACM

Given attention scores of the text and layout flows located in the same head of the same layer:

BiACM shares them as common knowledge, which is formulated as:

In order to maintain the ability of LiLT to cooperate with different off-the-shelf text models in finetuning as much as possible, we heuristically adopt the detached attention scores, so that the textual stream will not be affected by the gradient of non-textual one during pre-training, and its overall consistency can be preserved. Finally, the modified attention scores are used to weight the projected value vectors for subsequent modules in both flows.

Pretraining

Masked Visual-Language Modeling MVLM randomly masks some of the input tokens and the model is asked to recover them over the whole vocabulary using the output encoded features, driven by a cross-entropy loss. Meanwhile, the non-textual information remains unchanged.
MVLM improves model learning on the language side with cross-modality information. The given layout embedding can also help the model better capture both inter- and intra-sentence relationships.
Key Point Location KPL equally divides the entire layout into several regions (7×7=49 regions by default) and randomly masks some of the input bounding boxes. The model is required to predict which regions the key points (top-left corner, bottom-right corner, and center point) of each box belong to using separate heads.
KPL makes the model to fully understand the text content and know where to put a specific word/sentence when the surrounding ones are given.
Cross-modal Alignment Identification CMAI collects those encoded features of token-box pairs that are masked by MVLM and KPL, and build an additional head upon them to identify whether each pair is aligned.
CMAI makes the model to learn the cross-modal perception capacity.

Paper

LiLT: A Simple yet Effective Language-Independent Layout Transformer for Structured Document Understanding 2202.13669

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on February 6, 2023.

Canonical link

Exported from Medium on May 4, 2026.
