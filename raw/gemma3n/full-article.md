Source URL: https://huggingface.co/blog/gemma3n
Title: Gemma 3n fully available in the open-source ecosystem!
Published: June 26, 2025

# Gemma 3n fully available in the open-source ecosystem!

Gemma 3n was announced as a preview during Google I/O. The on-device community got excited because this is a model designed from the ground up to run locally on hardware. It is natively multimodal, supporting image, text, audio, and video inputs.

Gemma 3n is now available on the most used open source libraries: transformers & timm, MLX, llama.cpp (text inputs), transformers.js, ollama, Google AI Edge, and others.

## Models released today

Two model sizes have been released, with two variants (base and instruct) each: `gemma-3n-E2B` and `gemma-3n-E4B`. The `E` preceding the parameter count stands for `Effective`. Their actual parameter counts are 5B and 8B respectively, but thanks to improvements in memory efficiency they only need 2B and 4B in VRAM (GPU memory).

| Size | Base | Instruct |
| --- | --- | --- |
| 2B | google/gemma-3n-e2b | google/gemma-3n-e2b-it |
| 4B | google/gemma-3n-e4b | google/gemma-3n-e4b-it |

The E2B model can run in as little as 2GB of GPU RAM, while E4B can run with just 3GB of GPU RAM.

## Details of the models

In addition to the language decoder, Gemma 3n uses an audio encoder and a vision encoder.

- Vision Encoder (MobileNet-V5-300): 300M parameters, supports resolutions of 256x256, 512x512, and 768x768, achieves 60 FPS on Google Pixel while outperforming ViT Giant using 3x fewer parameters. Added to timm.
- Audio Encoder: based on the Universal Speech Model (USM), processes audio in 160ms chunks, enables speech-to-text and translation (e.g. English to Spanish/French).
- Gemma 3n Architecture and Language Model: added to transformers, branches out to timm for image encoding so there is a single reference implementation of the MobileNet architecture.

### Architecture highlights

- MatFormer Architecture: a nested transformer design, similar to Matryoshka embeddings, allows various subsets of layers to be extracted as if they were individual models. E2B and E4B were trained together, with E2B configured as a sub-model of E4B. Users can mix and match layers depending on hardware and memory budget.
- Per-Layer Embeddings (PLE): reduces accelerator memory usage by offloading embeddings to the CPU. This is why E2B, despite having 5B real parameters, takes about as much GPU memory as a 2B parameter model.
- KV Cache Sharing: accelerates long-context processing for audio and video, achieving 2x faster prefill compared to Gemma 3 4B.

### Performance and benchmarks

- LMArena Score: E4B is the first sub-10B model to achieve a score of 1300+.
- MMLU Scores: competitive performance across E4B, E2B, and several Mix-n-Match configurations.
- Multilingual support: 140 languages for text, 35 languages for multimodal interactions.

## Inference and fine-tuning

The post includes code snippets for inference via `transformers` pipeline and `AutoModelForImageTextToText` (text-only, audio, image/video inputs), MLX (`mlx-vlm`, day-0 support across all 3 modalities), llama.cpp (text-only, via `llama-server -hf ggml-org/gemma-3n-E4B-it-GGUF:Q8_0`), and Transformers.js/ONNXRuntime (ONNX weights released for `gemma-3n-E2B-it`). A free Google Colab notebook is provided for fine-tuning, including a dedicated notebook for audio tasks. The Hugging Face Gemma Recipes repository was introduced alongside this release, with notebooks and scripts to run and fine-tune the models.

## Conclusion

The post frames Gemma 3n as a multimodal, small-sized, and highly capable release, with integration credited to Arthur, Cyril, Raushan, Lysandre, and the Hugging Face team.
