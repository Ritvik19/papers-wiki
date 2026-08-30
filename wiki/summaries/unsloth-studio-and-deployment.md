# Unsloth Studio and Deployment

**Ingested**: 2026-07-22  
**Tags**: #summary #topic

## Summary

Unsloth's product layer: **Studio** no-code fine-tuning UI, **OpenAI-compatible API** for serving fine-tuned models, and **Docker** guides for reproducible training environments. Targets users who want Unsloth speed without writing notebooks.

## Key Claims

- **Studio** (studio): Web UI for dataset upload, hyperparameter selection, QLoRA training, and GGUF export; wraps Unsloth Python API.
- **API** (api): Drop-in **OpenAI** / **Anthropic**-compatible REST endpoint for locally fine-tuned models; supports streaming.
- **Docker** (how-to-train-llms-with-unsloth-and-docker): Official images with CUDA, Unsloth, TRL, vLLM; volume mounts for data/checkpoints.
- Deployment path: Train in Studio/Docker → export GGUF or serve via API → Ollama/llama.cpp/vLLM.
- Pro tier unlocks Studio RL and advanced quant export.

## Figures

| Figure | Caption |
|--------|---------|
| — | Studio screenshots in source docs |

## Entities

- [[Unsloth]] — product owner.
- [[Hugging Face]] — model hub integration.
- [[vLLM]] — serving backend option.
- [[Docker]] — containerized training.

## Questions & Gaps

- Studio multi-user / team workspace features roadmap unclear.
- API auth and rate-limiting for production deployments.

## Related

- [[Unsloth Origins and Mission]]
- [[Unsloth Model Support 2026]]
- [[Native-Speed vLLM Transformers Modeling Backend]]

## Sources

- `raw/studio/full-article.md`
- `raw/api/full-article.md`
- `raw/how-to-train-llms-with-unsloth-and-docker/full-article.md`
