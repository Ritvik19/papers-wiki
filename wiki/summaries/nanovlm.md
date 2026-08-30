# nanoVLM: The simplest repository to train your VLM in pure PyTorch

**Source**: `raw/nanovlm/full-article.html` (253 KB), `raw/nanovlm/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

nanoVLM is Hugging Face's minimal, from-scratch PyTorch codebase for training a Vision Language Model, explicitly modeled on Andrej Karpathy's nanoGPT: a small, readable reference implementation meant to teach the mechanics of VLM training rather than to compete with state-of-the-art models. It targets Visual Question Answering as its sole training objective and is light enough to train on a free-tier Colab notebook.

The architecture pairs a standard SigLIP vision transformer (`google/siglip-base-patch16-224`) with a Llama-3-style language decoder (`HuggingFaceTB/SmolLM2-135M`), connected by a Modality Projection module: a pixel-shuffle operation that compresses image tokens, followed by a linear layer that maps the compressed image embeddings into the language model's embedding space. Because the projector is trained from scratch while both backbones start pretrained, the optimizer uses two learning rates: a higher one for the projector and a smaller one for the vision/language backbones, so the new component learns quickly without disturbing the pretrained knowledge.

The repository ships a working reference model, trained for about 6 hours on a single H100 GPU on roughly 1.7M samples from the Cauldron dataset, along with a `generate.py` inference script and a Hugging Face Space for interactive testing. The whole codebase totals a handful of files (`data/`, `models/`, `train.py`, `generate.py`) each kept intentionally short and documented, so the project doubles as a teaching tool for how image and text tokens get aligned and fed into a shared decoder.

## Key Claims

- The vision backbone is an unmodified SigLIP ViT (`google/siglip-base-patch16-224`); the language backbone follows the Llama 3 architecture (`HuggingFaceTB/SmolLM2-135M`); both are swappable for other SigLIP/SigLIP 2 or SmolLM2 variants.
- The Modality Projection module (pixel shuffle + linear layer) is the only newly-initialized component; it uses a separate, higher learning rate than the pretrained backbones during training.
- The released reference checkpoint trained in about 6 hours on one H100 GPU over roughly 1.7M Cauldron samples.
- Training uses mixed precision (`torch.autocast`), a cosine LR schedule with linear warmup, and periodic (every 250 steps, configurable) evaluation on validation and MMStar test sets with checkpointing on improvement.
- The project is explicitly positioned as a learning tool, not a benchmark-competitive model.

## Figures

No figures were extracted for this ingest; the source article's architecture diagram and pixel-shuffle visualization are referenced inline in the summary above but not downloaded, per this batch's no-figure-download policy.

## Entities

- [[Hugging Face]] — publishes the blog and the nanoVLM repository and Space.

## Questions & Gaps

- The post does not report quantitative benchmark scores for the released reference checkpoint against other small VLMs (e.g. SmolVLM), only that it is "not intended to compete with SoTA models."
- No ablation is given for the two-learning-rate optimizer split (e.g. how much it matters versus a single shared learning rate).

## Related

- [[Papers Explained 176 - Smol LM]] — SmolLM2 is the language backbone used in nanoVLM's reference model, and SmolVLA (below) reuses the same backbone family for its VLM component.
- [[SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data]] — a robotics VLA model that uses SmolVLM2 (built on the same SmolLM2/SigLIP lineage) as its vision-language backbone.
- [[Vision Language Models]] — topic page for multimodal model coverage.
- [[Gemma 3n fully available in the open-source ecosystem!]] — contemporaneous small on-device multimodal model release cited as related work.
- [[Hugging Face]]
