# Papers Explained 10: Layout LM

Papers Explained 10: Layout LM

Papers Explained 10: Layout LM

LayoutLM is a Neural Network that jointly models interactions between text and layout information across scanned document images, thus is…

Papers Explained 10: Layout LM

LayoutLM is a Neural Network that jointly models interactions between text and layout information across scanned document images, thus is beneficial for a great number of real-world document image understanding tasks such as information extraction from scanned documents.

Basically, there are two types of features which substantially improve the language representation in a visually rich document, which are:

Document Layout Information
Visual Information

Architecture Details

To take advantage of existing pre-trained models and adapt to document image understanding tasks, we use the BERT architecture as the backbone and add two new input embeddings: a 2-D position embedding and an image embedding.

2-D Position Embedding: Unlike the position embedding that models the word position in a sequence, 2-D position embedding aims to model the relative spatial position in a document. To represent the spatial position of elements in scanned document images, we consider a document page as a coordinate system with the top left origin. In this setting, the bounding box can be precisely defined by (x0, y0, x1, y1), where (x0, y0) corresponds to the position of the upper left in the bounding box, and (x1, y1) represents the position of the lower right. We add four position embedding layers with two embedding tables, where the embedding layers representing the same dimension share the same embedding table. This means that we look up the position embedding of x0 and x1 in the embedding table X and lookup y0 and y1 in table Y.

Image Embedding: To utilize the image feature of a document and align the image feature with the text, we add an image embedding layer to represent image features in language representation. In more detail, with the bounding box of each word from OCR results, we split the image into several pieces, and they have a one-to-one
correspondence with the words. We generate the image region features with these pieces of images from the Faster R-CNN model as the token image embeddings. For the [CLS] token, we also use the Faster R-CNN model to produce embeddings using the whole scanned document image as the Region of Interest (ROI) to benefit the downstream tasks which need the representation of the [CLS] token.

Pre-Trained Layout LM

Masked Visual-Language Model: Inspired by the masked language model, the Masked Visual-language Model (MVLM) learns the language representation with the clues of 2-D position embeddings and text embeddings. During the pre-training, we randomly mask some of the input tokens but keep the corresponding 2-D position embeddings, and then the model is trained to predict the masked tokens given the contexts. In this way, the LayoutLM model not only understands the language contexts but also utilizes the corresponding 2-D position information, thereby bridging the gap between the visual and language modalities.

Multi-label Document Classification: For document image understanding, many tasks require the model to generate high quality document-level representations. As the IIT-CDIP Test Collection includes multiple tags for each document image, LayoutLM uses a Multi-label Document Classification (MDC) loss during the pre-training phase. Given a set of scanned documents, we use the document tags to supervise the pre-training process so that the model can cluster the knowledge from different domains and generate better document-level representation. Since the MDC loss needs the label for each document image that may not exist for larger datasets, it is optional during the pre-training and may not be used for pre-training larger models in the future.

The layoutLM model is pre-trained on the IIT-CDIP Test Collection 1.0, which contains more than 6 million documents, with more than 11 million scanned document images.

Fine Tuned Layout LM

The pre-trained LayoutLM model is fine-tuned on three document image understanding tasks, including a form understanding task, a receipt understanding task as well as a document image classification task.

For the form and receipt understanding tasks, LayoutLM predicts {B, I, E, S, O} tags for each token and uses sequential labeling to detect each type of entity in the dataset. SROIE Dataset is used for the purpose

For the document image classification task, LayoutLM predicts the class labels using the representation of the [CLS] token. The FUNSD Dataset and the RVL-CDIP Dataset are used for this purpose

Reference

LayoutLM: Pre-training of Text and Layout for Document Image Understanding paper: 1912.13318

Note:

The existing model only provides the language model, i.e. the LayoutLM embeddings, and not the final layers which combine visual features.

For further explanation refer to LayoutLMv1

Layout LM v1 in Action

Here are the implementations of Layout LM on custom datasets

Document Classifcation
Information Extraction

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on February 6, 2023.

Canonical link

Exported from Medium on May 4, 2026.
