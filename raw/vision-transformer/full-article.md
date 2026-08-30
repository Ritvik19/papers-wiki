# How the Vision Transformer (ViT) works in 10 minutes: an image is worth 16x16 words

Nikolas Adaloglou on 2021-01-28 · 6 mins

Source: https://theaisummer.com/vision-transformer/

This time I am going to be sharp and short. In 10 minutes I will indicate the minor modifications of the transformer architecture for image classification.

Since it is a follow-up article feel free to advise my previous articles on Transformer and attention if you don't feel that comfortable with the terms.

Transformers lack the inductive biases of Convolutional Neural Networks (CNNs), such as translation invariance and a locally restricted receptive field. Convolution is a linear local operator; transformers are permutation invariant and need sequences — so spatial images are converted to patch token sequences.

## How the Vision Transformer works in a nutshell

1. Split an image into patches
2. Flatten the patches
3. Produce lower-dimensional linear embeddings from the flattened patches
4. Add positional embeddings
5. Feed the sequence as an input to a standard transformer encoder
6. Pretrain the model with image labels (fully supervised on a huge dataset)
7. Finetune on the downstream dataset for image classification

Image patches are sequence tokens (like words). The encoder block is identical to the original transformer (Vaswani et al. 2017). Three ViT variants (Base/Large/Huge) differ mainly in depth, heads, and MLP size. No decoder — only an MLP classification head. Hidden size D is fixed throughout for short residual skip connections.

## Important details

ViT needs datasets with more than ~14M images to approach or beat state-of-the-art CNNs; otherwise ResNets or EfficientNets are preferable. Pretrain on a large dataset, then fine-tune on small datasets by replacing the MLP head with a new D×K linear layer. Authors recommend fine-tuning at higher resolution than pre-training, using 2D interpolation of pre-trained position embeddings.

## Representing an image as a sequence of patches

For image x ∈ R^{H×W×C} and patch size P, create N = HW/P² patches in R^{N×(P²C)}. Einops rearrange and `nn.Linear(P²C, D)` project patches to embeddings.

## Positional embeddings

Trainable position embeddings are added after projection. At patch granularity, order is easier to learn than at pixel level; many PE schemes showed little difference. Learned embeddings show 2D structure after training.

## Key findings

Early ViT layer filters (PCA visualization) can resemble early conv filters. For patch size P, maximum attention distance within a patch is P×P (128 for 16×16 patches) from layer 1 — global within-patch interactions without stacked conv layers. Mean attention distance grows with depth like receptive field. Some heads stay highly localized in early layers; hybrid ResNet+Transformer models show fewer such heads. Attention distance = average query-to-patch-pixel distance weighted by attention (128 images averaged). Model attends to semantically relevant regions for classification.

## Implementation

Full PyTorch ViT class using `einops.rearrange`, learnable CLS token, trainable 1D position embeddings, and `TransformerEncoder` from self_attention_cv.

## Conclusion

Key engineering: formulate image classification as sequential patch-token processing with a Transformer. Requires massive data and compute; original JFT pretraining dataset is not publicly reproducible.
