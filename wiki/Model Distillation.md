# Model Distillation

#concept

Model Distillation transfers behavior or capability from a teacher model into a student model, often by training the student on teacher outputs or teacher probability signals.

In [[On SFT RL and On-Policy Distillation]], distillation is most efficient when teacher and student are from the same family. Cross-family distillation can waste training signal on tokenizer mismatch, formatting habits, and recipe artifacts instead of capability transfer.

## Related

- [[Distillation Regimes Compared]]
- [[On SFT RL and On-Policy Distillation]]
- [[Supervised Fine-Tuning]]
- [[On-Policy Distillation]]
- [[Model Compression and Efficiency]]
- [[Large Language Models]]
- [[Inference Engineering]] — covers distillation as a model selection strategy for inference optimization (§1.3.3); DeepSeek-R1 distills as a key example.
- [[Papers Explained 05 - Tiny BERT]]
- [[Papers Explained 06 - Distil BERT]]
- [[Papers Explained 39 - DeiT]]
- [[Papers Explained 71 - Zephyr]]
- [[Papers Explained 89 - ColBERTv2]]
- [[Papers Explained 138 - LLMLingua-2]]
- [[Papers Explained 157 - Gemma 2]]
- [[Papers Explained 201 - SimCLRv2]]
