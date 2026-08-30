Source URL: https://huggingface.co/blog/llama4-release
Title: Welcome Llama 4 Maverick & Scout on Hugging Face

# Welcome Llama 4 Maverick & Scout on Hugging Face

Published April 5, 2025

ben burtenshaw, Vaibhav Srivastav, Pedro Cuenca, Clem, Rajat Arya, Jared Sulzdorf, Lysandre

We are incredibly excited to welcome the next generation of large language models from Meta to the Hugging Face Hub: Llama 4 Maverick (~400B) and Llama 4 Scout (~109B)! Both are Mixture of Experts (MoE) models with 17B active parameters.

Released today, these powerful, natively multimodal models represent a significant leap forward. We've worked closely with Meta to ensure seamless integration into the Hugging Face ecosystem, including both transformers and TGI from day one.

This is just the start of our journey with Llama 4. Over the coming days we'll continue to collaborate with the community to build amazing models, datasets, and applications with Maverick and Scout!

## What is Llama 4?

Llama 4, developed by Meta, introduces a new auto-regressive Mixture-of-Experts (MoE) architecture. This generation includes two models:

- The highly capable Llama 4 Maverick with 17B active parameters out of ~400B total, with 128 experts.
- The efficient Llama 4 Scout also has 17B active parameters out of ~109B total, using just 16 experts.

Both models leverage early fusion for native multimodality, enabling them to process text and image inputs. Maverick and Scout are both trained on up to 40 trillion tokens on data encompassing 200 languages (with specific fine-tuning support for 12 languages including Arabic, Spanish, German, and Hindi).

For deployment, Llama 4 Scout is designed for accessibility, fitting on a single server-grade GPU via on-the-fly 4-bit or 8-bit quantization, while Maverick is available in BF16 and FP8 formats. These models are released under the custom Llama 4 Community License Agreement, available on the model repositories.

## Features and Integrations on Hugging Face

- Model Checkpoints on the Hub: Both Llama 4 Maverick and Llama 4 Scout model weights are available directly on the Hugging Face Hub under the `meta-llama` organization. This includes both base and instruction tuned variants. You need to accept the license terms on the model card before accessing the weights.
- Hugging Face `transformers` integration: Llama 4 models are fully integrated with `transformers` (version `v4.51.0`), including support for their native multimodal capabilities, and downstream libraries like TRL.
- Automatic support for tensor-parallel and automatic device mapping in transformers.
- Text Generation Inference (TGI) Support: For optimized and scalable deployment, both models are supported by TGI.
- Quantization Support: Code for on-the-fly int4 quantization is provided for Scout. Maverick includes FP8 quantized weights.
- Xet Storage: All Llama 4 models use the Xet storage backend, achieving ~25% deduplication (base models) and ~40% for derivative (finetune, quantization) models.

## Context Length and Architecture Choices

The Llama 4 models were pre-trained with a context length of 256K. The Instruct models were fine-tuned to support much larger context lengths: 1M in the large 128 experts version (Maverick), and 10M for the 16 experts version (Scout).

| Model | Instruct | Context Length |
| --- | --- | --- |
| Scout (16E) | Yes | 10M |
| Maverick (128E) | Yes | 1M |
| Scout (16E) | No | 256K |
| Maverick (128E) | No | 256K |

These large context lengths come with a few very interesting architecture choices. Until an official technical report is published, this is what we know so far.

- **No RoPE (NoPE) layers**: NoPE, explored as far back as 2022, forgoes traditional positional encoding schemes such as RoPE. In Llama 4, NoPE layers are used every 4 layers and use the full causal mask over the context. For RoPE layers (three out of 4), chunked attention is used. Meta refers to the interleaved use of NoPE layers, together with temperature scaling, as the `iRoPE` architecture.
- **Chunked attention (in RoPE layers)**: As a way to reduce memory requirements, Llama 4 uses chunked attention in the layers that work with traditional RoPE positional encodings (three out of 4 decoder layers). In Llama 4, chunked attention length is `8192`. RoPE layers can only keep track of context in 8K blocks, while NoPE layers have access to the full context — a more memory- and compute-efficient version of Sliding Window Attention.
- **Attention Temperature Tuning**: Attention probability scores fade closer to zero as sequence length increases, a known consequence of applying softmax to very long sequences. Llama 4 uses a scaled softmax ("temperature tuning") to address this, applied in the NoPE layers but not the RoPE ones. This is likely one of the key factors to achieve 10M context length in Llama 4 Scout.
- **QK Normalization**: Llama Scout (16 experts) uses an additional RMS normalization without a learnable parameter of the Query and Key states in RoPE layers, after RoPE embeddings have been applied.
- **MoE interleaving**: Llama Scout is a full MoE consisting of 16 experts. Llama Maverick uses 128 experts, but MoE and dense layers alternate, so experts are applied in half of the layers.
- **Co-distillation**: Llama Maverick was co-distilled from a larger model, Llama Behemoth, using a novel loss function that dynamically weights the student and teacher logits.
- **MetaP**: The models leverage MetaP, a methodology likely inspired by MuP, to optimally tune hyperparameters across different dimensions including training budget and model size.

## How to Use with Transformers

Getting started with Llama 4 using `transformers` is straightforward (`pip install -U transformers huggingface_hub[hf_xet]`, `transformers v4.51.0` or later). Example using the instruction-tuned Maverick model with tensor parallel across 8 GPUs:

```python
from transformers import AutoProcessor, Llama4ForConditionalGeneration
import torch

model_id = "meta-llama/Llama-4-Maverick-17B-128E-Instruct"

processor = AutoProcessor.from_pretrained(model_id)
model = Llama4ForConditionalGeneration.from_pretrained(
    model_id,
    attn_implementation="flex_attention",
    device_map="auto",
    torch_dtype=torch.bfloat16,
)

messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "url": url1},
            {"type": "image", "url": url2},
            {"type": "text", "text": "Can you describe how these two images are similar, and how they differ?"},
        ]
    },
]

inputs = processor.apply_chat_template(
    messages, add_generation_prompt=True, tokenize=True,
    return_dict=True, return_tensors="pt",
).to(model.device)

outputs = model.generate(**inputs, max_new_tokens=256)
```

## Evaluation Scores

Evaluation results confirm the strength of these models, showing state-of-the-art performance that significantly outperforms predecessors like Llama 3.1 405B. On reasoning and knowledge tasks, the instruction-tuned Maverick achieves 80.5% on MMLU Pro and 69.8% on GPQA Diamond, while Scout scores 74.3% and 57.2% respectively.

### Pre-trained models

| Category | Benchmark | Metric | Llama 3.1 70B | Llama 3.1 405B | Llama 4 Scout | Llama 4 Maverick |
| --- | --- | --- | --- | --- | --- | --- |
| Reasoning & Knowledge | MMLU (5-shot) | macro_avg/acc_char | 79.3 | 85.2 | 79.6 | 85.5 |
| Reasoning & Knowledge | MMLU-Pro (5-shot) | macro_avg/em | 53.8 | 61.6 | 58.2 | 62.9 |
| Reasoning & Knowledge | MATH (4-shot) | em_maj1@1 | 41.6 | 53.5 | 50.3 | 61.2 |
| Code | MBPP (3-shot) | pass@1 | 66.4 | 74.4 | 67.8 | 77.6 |
| Multilingual | TydiQA (1-shot) | average/f1 | 29.9 | 34.3 | 31.5 | 31.7 |
| Image | ChartQA (0-shot) | relaxed_accuracy | no multimodal support | 83.4 | 85.3 |
| Image | DocVQA (0-shot) | anls | no multimodal support | 89.4 | 91.6 |

### Instruction tuned models

| Category | Benchmark | Metric | Llama 3.3 70B | Llama 3.1 405B | Llama 4 Scout | Llama 4 Maverick |
| --- | --- | --- | --- | --- | --- | --- |
| Image Reasoning | MMMU (0-shot) | accuracy | no multimodal support | 69.4 | 73.4 |
| Image Reasoning | MMMU Pro (0-shot) | accuracy | no multimodal support | 52.2 | 59.6 |
| Image Reasoning | MathVista (0-shot) | accuracy | no multimodal support | 70.7 | 73.7 |
| Image Understanding | ChartQA (0-shot) | relaxed_accuracy | no multimodal support | 88.8 | 90.0 |
| Image Understanding | DocVQA test (0-shot) | anls | no multimodal support | 94.4 | 94.4 |
| Coding | LiveCodeBench 10/01/2024-02/01/2025 (0-shot) | pass@1 | 33.3 | 27.7 | 32.8 | 43.4 |
| Reasoning & Knowledge | MMLU Pro (0-shot) | macro_avg/em | 68.9 | 73.4 | 74.3 | 80.5 |
| Reasoning & Knowledge | GPQA Diamond (0-shot) | accuracy | 50.5 | 49.0 | 57.2 | 69.8 |
| Multilingual | MGSM (0-shot) | average/em | 91.1 | 91.6 | 90.6 | 92.3 |
| Long context | MTOB half book eng->kgv/kgv->eng | chrF | context window is 128K | 42.2/36.6 | 54.0/46.4 |
| Long context | MTOB full book eng->kgv/kgv->eng | chrF | context window is 128K | 39.7/36.3 | 50.8/46.7 |

## Acknowledgments

Releasing a giant like Llama 4 takes a colossal effort across teams, geographies and a lot of VMs. Thanks to the Transformers team, the vLLM team, the Xet team, and the rest of the Hugging Face, vLLM and Meta Llama teams.

## References

- To learn more about Xet Storage: blog post, and Hub docs.
- Check out Meta's release blog post.

## Models mentioned in this article

- meta-llama/Llama-4-Maverick-17B-128E-Instruct (402B, Image-Text-to-Text)
- meta-llama/Llama-4-Scout-17B-16E-Instruct (109B, Image-Text-to-Text)

## Papers mentioned in this article

- 2203.03466 (MuP-related paper, Mar 7 2022)
