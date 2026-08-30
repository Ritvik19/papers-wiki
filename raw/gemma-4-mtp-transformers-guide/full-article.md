# Gemma 4 Multi-Token Prediction (MTP) using Hugging Face Transformers

**Source URL**: https://ai.google.dev/gemma/docs/mtp/mtp

To improve the inference speed of the Gemma 4 models, a new series of autoregressive "drafter" models has been released alongside the main lineup. Instead of solely relying on the primary Gemma 4 models (referred to as the "target" models), the draft model predicts several tokens autoregressively in the time it takes the target model to process just one. This technique is also known as speculative decoding.

After the drafter has predicted multiple draft tokens, the target model now only has to verify those suggested draft tokens. The verification is done in parallel thereby drastically speeding up inference. It reduces the number of forward passes the target model has to do for each token. Because our drafter generates a sequence of tokens for verification, we refer to it as the Multi-Token Prediction (MTP) head.

The draft models released for the Gemma 4 family are small and introduce several enhancements to improve the quality of drafted tokens and to further speed up inference, like using the target model activations and KV-cache to get better predictions.

## Load the Models

For each target model, there is an assistant to help speed up inference. Load two models:

- **Target** (e.g., `google/gemma-4-E2B-it`): The full Gemma 4 target model
- **Drafter** (e.g., `google/gemma-4-E2B-it-assistant`): The lightweight 4-layer MTP drafter that proposes candidate tokens

```python
TARGET_MODEL_ID = "google/gemma-4-E2B-it"
ASSISTANT_MODEL_ID = TARGET_MODEL_ID + "-assistant"

from transformers import AutoProcessor, AutoModelForCausalLM

processor = AutoProcessor.from_pretrained(TARGET_MODEL_ID)
target_model = AutoModelForCausalLM.from_pretrained(TARGET_MODEL_ID, torch_dtype=torch.bfloat16, device_map="auto")
assistant_model = AutoModelForCausalLM.from_pretrained(ASSISTANT_MODEL_ID, torch_dtype=torch.bfloat16, device_map="auto")
```

## Generate with MTP

Pass `assistant_model` to `target_model.generate()`:

```python
outputs = target_model.generate(
    **inputs,
    assistant_model=assistant_model,
    max_new_tokens=256,
    do_sample=False,
)
```

## Under the hood

- The drafter proposes N tokens generated autoregressively
- The target model verifies all N tokens in one forward pass
- Drafted tokens with high probabilities are accepted; low-probability tokens are rejected
- The target model always generates 1 additional token by itself regardless of accept count

## Draft token scheduling

Tune `num_assistant_tokens` and `num_assistant_tokens_schedule` on the assistant model:

- `"heuristic"` schedule: increase draft length by 2 when all tokens accepted; decrease by 1 on any rejection
- `"constant"` schedule: fixed draft length
