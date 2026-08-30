# Layer Normalization

**Type**: concept  
**Tags**: #concept

## Overview

Layer normalization (LN; Ba et al., 2016) standardizes activations **per sample** by computing mean and variance across all channels and spatial positions (for 4D feature maps) or across the feature dimension (for 2D sequence tensors). Unlike [[Batch Normalization]], LN statistics are independent of batch size — making it the default normalization in [[How Transformers Work in Deep Learning and NLP: An Intuitive Introduction|transformers]] and other sequence models.

## Appearances

- [[In-layer Normalization Techniques for Training Very Deep Neural Networks]] — LN introduced for RNN outputs; generalized to 4D tensors by averaging over C×H×W per sample; contrasted with BN and IN.
- [[Papers Explained Review 10 - Normalization Layers]] — paper survey with TensorFlow implementation.

## Notes

GN with groups=1 reduces to LN. LN does not maintain separate running statistics at inference — it uses batch-independent per-sample stats at both train and test time.

## Related

- [[Batch Normalization]]
- [[Group Normalization]]
- [[Instance Normalization]]
- [[Self-Attention]]
