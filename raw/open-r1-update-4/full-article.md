Source URL: https://huggingface.co/blog/open-r1/update-4
Title: Open R1: Update #4

# Open R1: Update #4

Team Article. Published March 26, 2025

Leandro von Werra, Vaibhav Srivastav, Daniel Vila, Yacine Jernite (open-r1)

## Welcome DeepSeek-V3-0324

This week, a new model from DeepSeek silently landed on the Hub: an updated version of DeepSeek-V3, the base model underlying the R1 reasoning model.

### What we know so far

The model has the same architecture as the original DeepSeek-V3 and now comes with an MIT license, while the previous V3 model had a custom model license. The focus of this release was improving instruction following as well as code and math capabilities.

### How good is it?

DeepSeek evaluated the model on a range of math and coding tasks; it plays in the top league, often on par with GPT-4.5 and generally stronger than Claude-Sonnet-3.7. Benchmark deltas:

| Benchmark | Before | After | Delta |
| --- | --- | --- | --- |
| MMLU-Pro | 75.9 | 81.2 | +5.3 |
| GPQA | 59.1 | 68.4 | +9.3 |
| AIME | 39.6 | 59.4 | +19.8 |
| LiveCodeBench | 39.2 | 49.2 | +10.0 |

The model card mentions targeted improvements in front-end web development (more aesthetically pleasing pages/games, better executability), Chinese writing proficiency, multi-turn interactive rewriting, translation/letter writing, Chinese search report analysis, and function-calling accuracy.

### How did they do it?

Given the naming and architecture, the new model is almost certainly based on the previous V3 checkpoint, continued via either continual pretraining (newer, better-curated data) or improved post-training (better data mix and/or algorithm), or some combination. No technical report had been released at time of writing.

### How to use the model

Available via Hugging Face Inference Providers (Fireworks, Hyperbolic, Novita):

```python
from huggingface_hub import InferenceClient

client = InferenceClient(provider="fireworks-ai")

messages = [{"role": "user", "content": "..."}]
completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3-0324",
    messages=messages,
    temperature=0.3,
)
```

Also supported in Text Generation Inference (TGI 3.2.1) and SGLang (with Multi-Head Latent Attention and Data Parallelism). Unsloth AI released Dynamic Quantizations enabling the model to run with roughly half the compute of one H100 node via llama.cpp with limited benchmark degradation.

### Is it safe?

- **Downloading and running the model**: yes. The Hub stores weights in `safetensors` (no hidden code execution risk, unlike PyTorch pickle). Modeling code is fully visible, requires explicit `trust_remote_code=True`, and is scanned for malicious code; pinning a reviewed `revision` adds extra safety.
- **Model outputs — alignment mismatch**: every provider aligns models to different, often opaque values that can shift over time; open models can be re-aligned via custom fine-tuning (e.g. Perplexity's DeepSeek R1 1776).
- **Code generation**: LLMs trained on public code can reproduce known vulnerabilities; review and scan generated code like any other contribution.
- **Agents**: use sandboxes, avoid sharing private credentials (use scoped access keys), and keep a human in the loop for high-stakes automated actions.

TL;DR: downloading and running the models is safe, but use the same output-safety precautions you would with any LLM.
