# Papers Explained 28: Masked AutoEncoder

Papers Explained 28: Masked AutoEncoder

Papers Explained 28: Masked AutoEncoder

The appetite for data has been successfully addressed in natural language processing (NLP) by self-supervised pretraining. The solutions…

Papers Explained 28: Masked AutoEncoder

The appetite for data has been successfully addressed in natural language processing (NLP) by self-supervised pretraining. The solutions, based on autoregressive language modeling in GPT and masked autoencoding in BERT, are conceptually simple: they remove a portion of the data and learn to predict the removed content.

The idea of masked autoencoders, a form of more general denoising autoencoders, is natural and applicable in computer vision as well. But what makes masked autoencoding different between vision and language?

In vision, convolutional networks were dominant over the last decade. Convolutions typically operate on regular grids and it is not straightforward to integrate ‘indicators’ such as mask tokens or positional embeddings into convolutional networks. This architectural gap, however, has been addressed with the introduction of Vision Transformers (ViT).
Information density is different between language and vision. Languages are human-generated signals that are highly semantic and information-dense. When training a model to predict only a few missing words per sentence, this task appears to induce sophisticated language understanding. Images, on the contrary, are natural signals with heavy spatial redundancy — e.g., a missing patch can be recovered from neighboring patches with little high-level understanding of parts, objects, and scenes. To overcome this difference and encourage learning useful features, we show that a simple strategy works well in computer vision: masking a very high portion of random patches. This strategy largely reduces redundancy and creates a challenging selfsupervisory task that requires holistic understanding beyond low-level image statistics.
The autoencoder’s decoder, which maps the latent representation back to the input, plays a different role between reconstructing text and images.

Driven by this analysis, MAE masks random patches from the input image and reconstructs the missing patches in the pixel space. It has an asymmetric encoder-decoder design. Our encoder operates only on the visible subset of patches (without mask tokens), and our decoder is lightweight and reconstructs the input from the latent representation along with mask tokens.

Architecture

Masking Following ViT, an image is divided into regular non-overlapping patches. Then a subset of
patches is sampled and the remaining ones are masked.

MAE encoder The encoder is a ViT but applied only on visible, unmasked patches. Thus the encoder only operates on a small subset (~25%) of the full et. Masked patches are removed, no mask tokens are used. This allows is to train very large encoders with only a fraction of compute and memory. The full set is handled by a lightweight decoder.

MAE decoder The input to the MAE decoder is the full set of tokens consisting of (i) encoded visible patches, and (ii) mask tokens. Each mask token is a shared, learned vector that indicates the presence of a missing patch to be predicted. Positional embeddings are added to all tokens in this full set; without this, mask tokens would have no information about their location in the image. The decoder has another series of Transformer blocks. The MAE decoder is only used during pre-training to perform the image reconstruction task. Therefore, the decoder architecture can be flexibly designed in a manner that is independent of the encoder design.

Reconstruction Target MAE reconstructs the input by predicting the pixel values for each masked patch. Each element in the decoder’s output is a vector of pixel values representing a patch. The last layer of the decoder is a linear projection whose number of output channels equals the number of pixel values in a patch. The decoder’s output is reshaped to form a reconstructed image. The loss function computes the mean squared error (MSE) between the reconstructed and original images in the pixel space. Loss is computed only on masked patches, similar to BERT.

Paper

Masked Autoencoders Are Scalable Vision Learners: 2111.06377

Implementation

Masked Autoencoder — Vision Transformer

Recommended Reading [Vision Transformers]

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on February 9, 2023.

Canonical link

Exported from Medium on May 4, 2026.
