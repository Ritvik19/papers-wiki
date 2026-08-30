# Efficient Encoder Models

Efficient encoder models are the branch of encoder-only language models that prioritize lower parameter count, faster inference, mobile deployment, or adaptive runtime while preserving as much of BERT-style language understanding performance as possible. In this wiki, that branch centers on [[Papers Explained 05 - Tiny BERT]], [[Papers Explained 06 - Distil BERT]], [[Papers Explained 07 - ALBERT]], [[Papers Explained 36 - MobileBERT]], and [[Papers Explained 37 - FastBERT]].

This summary page groups the compact and speed-oriented encoder work that is otherwise spread across [[Model Compression and Efficiency]], [[Model Distillation]], and [[Large Language Models]].

## Timeline

### 2019: Distillation becomes the first compression path

According to [[Papers Explained 06 - Distil BERT]], DistilBERT keeps the general BERT architecture but removes token-type embeddings and the pooler, cuts the number of layers in half, and trains the student with masked language modeling, soft-target distillation, and cosine alignment. This is the cleanest “smaller BERT” path in the wiki.

According to [[Papers Explained 05 - Tiny BERT]], TinyBERT pushes this further with fine-grained distillation across embeddings, hidden states, attention maps, and logits. It also introduces a two-stage framework of general distillation plus task-specific distillation, making it a more comprehensive teacher-student compression system than DistilBERT.

### 2019: ALBERT reduces redundancy directly

According to [[Papers Explained 07 - ALBERT]], not every efficient encoder needs distillation. ALBERT reduces memory and parameter cost by factorizing embeddings and sharing parameters across layers, while replacing next sentence prediction with sentence-order prediction. It is an efficiency model by architecture and parameterization rather than by student-teacher compression.

### 2020: MobileBERT targets device deployment

According to [[Papers Explained 36 - MobileBERT]], MobileBERT keeps the depth of BERT-LARGE but makes each block much thinner through bottlenecks. It uses a specially adapted teacher, feature-map transfer, attention transfer, pretraining distillation, and progressive transfer strategies. In this branch, MobileBERT is the most explicitly device-oriented redesign.

### 2020: FastBERT targets adaptive latency

According to [[Papers Explained 37 - FastBERT]], FastBERT is optimized for speed-tunable inference rather than only model size. It adds student classifiers after intermediate Transformer layers and uses self-distillation so the model can exit early on easier inputs. This makes FastBERT the runtime-adaptive member of the family.

## Comparison

### DistilBERT

According to [[Papers Explained 06 - Distil BERT]], DistilBERT is best understood as a compact BERT baseline. It makes relatively modest architectural changes and relies on a simple but effective pretraining-time distillation recipe.

### TinyBERT

According to [[Papers Explained 05 - Tiny BERT]], TinyBERT is more aggressive and more granular than DistilBERT. Its strength is the breadth of internal signals used for distillation and its two-stage learning process.

### ALBERT

According to [[Papers Explained 07 - ALBERT]], ALBERT is not mainly a distillation model. Its efficiency comes from parameter sharing and factorized embeddings, so it belongs in this family for efficiency but solves the problem differently.

### MobileBERT

According to [[Papers Explained 36 - MobileBERT]], MobileBERT is a mobile-first architectural redesign rather than a shallow compressed clone. It remains deep while making each block narrow and latency-aware.

### FastBERT

According to [[Papers Explained 37 - FastBERT]], FastBERT is the member of the family that changes inference behavior the most. It is useful when the desired tradeoff is dynamic speed per example rather than a fixed smaller checkpoint.

## Takeaways

- [[Papers Explained 06 - Distil BERT]] is the simplest “drop-in smaller BERT” path.
- [[Papers Explained 05 - Tiny BERT]] is the strongest distillation-centric path in the small-BERT family covered here.
- [[Papers Explained 07 - ALBERT]] shows that parameter redundancy can be attacked directly without classic distillation.
- [[Papers Explained 36 - MobileBERT]] focuses on mobile deployment through deep-thin bottleneck design.
- [[Papers Explained 37 - FastBERT]] focuses on adaptive inference with early exits.
- This branch complements the broader encoder lineage summarized in [[Encoder-Only Language Models]].

## Related

- [[Encoder-Only Language Models]]
- [[Model Compression and Efficiency]]
- [[Model Distillation]]
- [[Large Language Models]]
- [[Papers Explained 05 - Tiny BERT]]
- [[Papers Explained 06 - Distil BERT]]
- [[Papers Explained 07 - ALBERT]]
- [[Papers Explained 36 - MobileBERT]]
- [[Papers Explained 37 - FastBERT]]

#summary #topic
