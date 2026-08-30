Source URL: https://huggingface.co/blog/nanovlm
Title: nanoVLM: The simplest repository to train your VLM in pure PyTorch
Published: May 21, 2025

# nanoVLM: The simplest repository to train your VLM in pure PyTorch

nanoVLM is the simplest way to get started with training a Vision Language Model (VLM) using pure PyTorch. It is a lightweight toolkit that allows launching a VLM training run on a free-tier Colab notebook. The project is inspired by Andrej Karpathy's nanoGPT, providing a similar minimal, readable project for the vision domain.

## What is a Vision Language Model?

A VLM is a multi-modal model that processes vision and text, typically taking images and/or text as input and generating text as output (captioning, object detection, VQA, etc.). nanoVLM focuses only on Visual Question Answering as the training objective.

## Working with the repository

Repository structure:

```
.
├── data
│   ├── collators.py
│   ├── datasets.py
│   └── processors.py
├── generate.py
├── models
│   ├── config.py
│   ├── language_model.py
│   ├── modality_projector.py
│   ├── utils.py
│   ├── vision_language_model.py
│   └── vision_transformer.py
└── train.py
```

## Architecture

The vision backbone (`models/vision_transformer.py`) is a standard vision transformer, specifically Google's SigLIP vision encoder. The language backbone follows the Llama 3 architecture.

Vision and text modalities are aligned using a Modality Projection module, which takes image embeddings from the vision backbone and transforms them into embeddings compatible with the text embedding layer of the language model. These embeddings are concatenated and fed into the language decoder. The Modality Projection module consists of a pixel shuffle operation followed by a linear layer; pixel shuffle reduces the number of image tokens, cutting computational cost and speeding up training since transformer-based language decoders are sensitive to input length.

Pre-trained backbone weights used during training:

1. Vision backbone: `google/siglip-base-patch16-224`
2. Language backbone: `HuggingFaceTB/SmolLM2-135M`

Other variants of SigLIP/SigLIP 2 (vision) and SmolLM2 (language) can be swapped in.

## Train your own VLM

Training is launched with `python train.py`, which handles dataset loading/preprocessing, model initialization, optimization, and logging.

- Configuration: `TrainConfig` (learning rates, checkpoint paths) and `VLMConfig` (hidden dimensions, attention heads) from `models/config.py`.
- Data loading: `get_dataloaders` loads datasets via Hugging Face's `load_dataset`, combines/shuffles multiple datasets, applies a train/val split, and wraps them in `VQADataset`/`MMStarDataset` with `VQACollator`/`MMStarCollator`. `data_cutoff_idx` is useful for debugging on small subsets.
- Model initialization: via the `VisionLanguageModel` class, either from a checkpoint (`VisionLanguageModel.from_pretrained(model_path)`) or freshly initialized with optionally preloaded backbones.
- Optimizer setup: two learning rates, a higher one for the freshly-initialized modality projector (MP) and a smaller one for the pre-trained encoder/decoder stack, so the MP learns quickly while preserving backbone knowledge.
- Training loop: mixed precision via `torch.autocast`, cosine LR schedule with linear warmup, tokens/sec logging per batch. Every 250 steps (configurable) the model is evaluated on validation and MMStar test sets and checkpointed if accuracy improves.
- Logging: optional Weights & Biases integration; runs auto-named from sample size, batch size, epoch count, learning rates, and date.
- Push to Hub: `model.save_pretrained(save_path)` then `model.push_to_hub("hub/id")`.

## Run inference on a pre-trained model

Using nanoVLM, the authors trained and published a model using `google/siglip-base-patch16-224` and `HuggingFaceTB/SmolLM2-135M` as backbones, trained for about 6 hours on a single H100 GPU on about 1.7M samples of the Cauldron dataset. This model is not intended to compete with state-of-the-art VLMs; it exists to demystify the components and training process of VLMs.

Inference is run via `generate.py --image path/to/image.png --prompt "Your prompt here"`, which loads the model with `VisionLanguageModel.from_pretrained(source)`, tokenizes the prompt, processes the image, and calls `model.generate`.

A Hugging Face Space is provided for interactive inference.

## Conclusion

The post frames nanoVLM as both a learning tool and a foundation to build on: for understanding how multi-modal inputs are aligned, or for training a VLM on a custom dataset.

## References

1. GitHub: huggingface/nanoVLM
2. Vision Language Models (Better, faster, stronger)
3. Vision Language Models Explained
4. A Dive into Vision-Language Models
5. SmolVLM: Redefining small and efficient multimodal models
