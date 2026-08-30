# Papers Explained 23: Structural LM

Papers Explained 23: Structural LM

Papers Explained 23: Structural LM

Taking advantage of existing pretrained language models and to adapt to document image understanding tasks, Structural LM uses the BERT…

Papers Explained 23: Structural LM

Taking advantage of existing pretrained language models and to adapt to document image understanding tasks, Structural LM uses the BERT architecture as the backbone.

Based on the architecture, we propose to utilize the cell-level layout information from document images and incorporate them into the transformer encoder.

First, given a set of tokens from different cells and the layout information of cells, the cell level input embeddings are computed by summing the corresponding word embeddings, cell-level 2Dposition embeddings, and original 1D-position embeddings. Then, these input embeddings are passed through a bidirectional Transformer encoder that can generate contextualized representations with an attention mechanism.

Pre Training

Masked Visual-Language Modeling: Some of the input tokens are randomly masked but the corresponding cell-level position embeddings are kept , and then the model is pre-trained to predict the masked tokens.

Compared with the MVLM in LayoutLM, StructuralLM makes use of the cell-level layout information and predicts the mask tokens more accurately.

Cell Position Classification: First, the image is split into N areas of the same size. Then the area to which the cell belongs to is calculated through the center 2D-position of the cell.

Meanwhile, some cells are randomly selected, and the 2D-positions of tokens in the selected cells are replaced with (0; 0; 0; 0). A classification layer is built above the encoder outputs. This layer predicts a label [1,N] of the area where the selected cell is located, and computes the cross-entropy loss.

Following LayoutLM, StructuralLM is pre-trained on the IIT-CDIP Test Collection 1.0.

To take advantage of existing pre-trained models and adapt to document image understanding tasks, the weights of StructuralLM model are initialized with the pre-trained RoBERTa large model except for the 2D-position embedding layers.

Fine Tuning

Form and Receipt Understanding: FUNSD dataset
Document Image Classification: RVL-CDIP dataset
Document Visual Question Answering: DocVQA dataset

Paper

StructuralLM: Structural Pre-training for Form Understanding 2105.11210

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on February 7, 2023.

Canonical link

Exported from Medium on May 4, 2026.
