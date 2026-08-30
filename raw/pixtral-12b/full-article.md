# Announcing Pixtral 12B

**Source URL**: https://mistral.ai/news/pixtral-12b/  
**Published**: September 17, 2024  
**Author**: Mistral AI team

> **Heads up: this model is deprecated.** Pixtral 12B is no longer maintained and has been replaced by Mistral AI's latest vision and multimodal models.

## Pixtral 12B in short

- Natively multimodal, trained with interleaved image and text data
- Strong performance on multimodal tasks; excels in instruction following
- Maintains state-of-the-art performance on text-only benchmarks
- **Architecture:** new 400M-parameter vision encoder trained from scratch; 12B multimodal decoder based on Mistral Nemo; variable image sizes and aspect ratios; multiple images in a 128k context window
- **Use:** Apache 2.0 license; available on La Plateforme and Le Chat

Pixtral is trained to understand both natural images and documents, achieving **52.5% on MMMU**, surpassing a number of larger models. The model shows strong abilities in chart and figure understanding, document question answering, multimodal reasoning, and instruction following. Pixtral ingests images at natural resolution and aspect ratio and processes any number of images in its **128K** context window without compromising text benchmark performance.

## Performance

Pixtral was trained as a drop-in replacement for Mistral Nemo 12B, delivering best-in-class multimodal reasoning without compromising instruction following, coding, and math.

### Evaluation protocol

Mistral re-evaluated open and closed models through the same harness. Prompts were chosen to reproduce GPT-4o and Claude 3.5 Sonnet results. Pixtral substantially outperforms open models at its scale and often beats closed models such as Claude 3 Haiku; it matches or beats much larger models like LLaVA-OneVision 72B on multimodal benchmarks.

### Instruction following

Pixtral excels at multimodal and text-only instruction following vs. other open multimodal models, with ~20% relative improvement in text IF-Eval and MT-Bench over the nearest OSS model. Mistral created multimodal versions of these benchmarks (MM-IF-Eval, MM-MT-Bench) and will open-source MM-MT-Bench.

## Architecture

**Variable image size:** A new vision encoder passes images at native resolution; each 16×16 patch becomes an image token. Tokens are flattened with `[IMG BREAK]` and `[IMG END]` between rows and at image end so the model can distinguish aspect ratios with equal token counts.

**Final architecture:** Vision encoder + multimodal transformer decoder predicting next text token on interleaved image/text data; supports arbitrary image counts and sizes in 128K context.

## Qualitative examples

Demonstrations include reasoning over complex figures (European GDP table), chart understanding (training-loss spike for "dark-dragon-50"), multi-image table merging into markdown, image-to-HTML code generation, and natural-scene optical-illusion reasoning (Leaning Tower of Pisa).

## How to run Pixtral

- **Le Chat:** select Pixtral, upload an image
- **La Plateforme API:** `pixtral-12b-2409` via chat completions
- **Local:** `mistral-inference` or **vLLM** with `mistralai/Pixtral-12B-2409` on Hugging Face
