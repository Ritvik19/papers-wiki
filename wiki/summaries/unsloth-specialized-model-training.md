# Unsloth Specialized Model Training

**Ingested**: 2026-07-22  
**Tags**: #summary #topic

## Summary

Beyond chat LLMs, Unsloth documents fine-tuning for **text-to-speech** (Orpheus, CSM, Whisper), **embedding/reranker** models (SentenceTransformers, BERT), and **DeepSeek-OCR** vision-language OCR. These workflows reuse the same QLoRA + kernel stack with modality-specific data loaders and loss heads.

## Key Claims

- **TTS** (tts): Fine-tune **Orpheus**, **CSM**, and **Whisper** for speech synthesis/ASR; audio tokenization + lower learning rates.
- **Embedding fine-tuning** (embedding-finetuning):
  - SentenceTransformers bi-encoders and cross-encoder rerankers.
  - In-batch negatives + contrastive loss via Unsloth.
  - BERT-family encoder support.
- **DeepSeek-OCR** (deepseek-ocr): Vision encoder + text decoder QLoRA; document OCR SFT recipes.
- Modality-specific memory: audio spectrograms and image patches benefit from packing less than text SFT.

## Figures

| Figure | Caption |
|--------|---------|
| — | Notebook walkthroughs in source docs |

## Entities

- [[DeepSeek]] — DeepSeek-OCR model.
- [[Sentence Transformers]] — embedding framework.
- [[Audio Models]] — TTS/ASR topic.
- [[Unsloth]] — shared training stack.

## Questions & Gaps

- Real-time TTS inference latency after QLoRA not benchmarked.
- OCR fine-tune eval on non-Latin scripts undocumented.

## Related

- [[Unsloth Model Support 2025]]
- [[Embedding Models]]
- [[Computer Vision]]

## Sources

- `raw/tts/full-article.md`
- `raw/embedding-finetuning/full-article.md`
- `raw/deepseek-ocr/full-article.md`
