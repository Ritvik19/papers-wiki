# Encoder-Only Language Models

Encoder-only language models are bidirectional Transformer systems built to produce contextual representations for classification, retrieval, question answering, and token-level understanding tasks. In this wiki, their development runs from [[Papers Explained 02 - BERT]] through training-focused upgrades like [[Papers Explained 03 - RoBERTa]] and [[Papers Explained 173 - ELECTRA]], architecture-focused upgrades like [[Papers Explained 08 - DeBERTa]] and [[Papers Explained 182 - DeBERTa V3]], and newer long-context and specialization work such as [[Papers Explained 277 - ModernBERT]], [[Papers Explained 327 - NeoBERT]], [[Papers Explained 465 - EmbeddingGemma]], and [[Papers Explained 471 - mmBERT]].

This summary page groups the main encoder-only lineage that appears across [[Large Language Models]], [[Embedding and Retrieval]], [[Model Compression and Efficiency]], and [[Multilingual Models]].

## Timeline

### 2018: BERT establishes the template

According to [[Papers Explained 02 - BERT]], the foundational encoder-only recipe is a multi-layer bidirectional Transformer encoder trained with masked language modeling and next sentence prediction, then adapted via fine-tuning. This creates the basic pattern that later models either scale, refine, compress, or specialize.

### 2019: RoBERTa shows the recipe matters

According to [[Papers Explained 03 - RoBERTa]], BERT was significantly undertrained. RoBERTa improves the family mostly through training changes rather than a new backbone: more data, longer training, larger batches, dynamic masking, and a larger byte-level BPE vocabulary. This marks the start of the training-recipe branch of encoder progress.

### 2019: ALBERT improves parameter efficiency

According to [[Papers Explained 07 - ALBERT]], encoder-only models can also improve by reducing redundancy. ALBERT uses factorized embeddings and cross-layer parameter sharing, while replacing next sentence prediction with sentence-order prediction. This makes encoder scaling more parameter-efficient without changing the overall encoder-only role.

### 2020: ELECTRA improves sample efficiency

According to [[Papers Explained 173 - ELECTRA]], encoder pretraining becomes more sample-efficient with replaced token detection. A generator corrupts tokens and a discriminator learns to classify whether each token is original or replaced, allowing the encoder to learn from all token positions rather than only the masked subset used in standard masked language modeling.

### 2020: DeBERTa improves the encoder architecture

According to [[Papers Explained 08 - DeBERTa]], DeBERTa upgrades BERT-like encoders through disentangled attention and an enhanced mask decoder. Instead of mixing content and position into a single representation at input, it models them separately and uses relative-position-aware attention more explicitly.

### 2021: DeBERTa V3 combines architectural and objective gains

According to [[Papers Explained 182 - DeBERTa V3]], DeBERTa V3 merges DeBERTa’s disentangled attention with ELECTRA-style replaced token detection and adds gradient-disentangled embedding sharing. In the wiki’s lineage, this is a major synthesis point where architecture and pretraining efficiency improve together.

### 2024: ModernBERT modernizes the whole stack

According to [[Papers Explained 277 - ModernBERT]], later encoder progress shifts toward long-context support and hardware-aware design. ModernBERT introduces RoPE, pre-normalization, GeGLU, alternating local and global attention, unpadding, Flash Attention, and sequence packing. It also removes next sentence prediction, raises the masking ratio, and extends context length to 8192 tokens.

### 2025: NeoBERT refines the modern recipe

According to [[Papers Explained 327 - NeoBERT]], the modern encoder stack continues to converge around RoPE, RMSNorm, SwiGLU, deeper-and-narrower scaling, larger modern web corpora, and staged long-context training. The emphasis becomes careful ablation across architecture, data mixture, optimizer, and masking ratio rather than a single dramatic change.

### 2025: MLM is re-evaluated rather than discarded

According to [[Papers Explained 407 - Should We Still Pretrain Encoders with Masked Language Modeling]], masked language modeling still tends to outperform causal-language-model pretraining on representation-heavy downstream tasks, even though CLM can be more data-efficient early and more stable during fine-tuning. The page highlights a newer hybrid view where two-stage CLM+MLM training can outperform MLM-only training under fixed compute.

### 2025: Encoder-only models become specialized systems

According to [[Papers Explained 465 - EmbeddingGemma]], encoder-only models can now be adapted from decoder families and specialized for embedding quality with contrastive losses, geometric distillation, orthogonal regularization, and model souping. According to [[Papers Explained 471 - mmBERT]], they can also be scaled multilingual with ModernBERT-like architecture, annealed language learning, and stage-wise masking schedules.

## Main Branches

- Recipe scaling and data improvements: [[Papers Explained 03 - RoBERTa]], [[Papers Explained 173 - ELECTRA]], [[Papers Explained 407 - Should We Still Pretrain Encoders with Masked Language Modeling]]
- Architectural refinement: [[Papers Explained 08 - DeBERTa]], [[Papers Explained 182 - DeBERTa V3]], [[Papers Explained 277 - ModernBERT]], [[Papers Explained 327 - NeoBERT]]
- Specialization for retrieval and multilinguality: [[Papers Explained 465 - EmbeddingGemma]], [[Papers Explained 471 - mmBERT]]
- Compression and deployment branch: [[Efficient Encoder Models]]

## Takeaways

- The original encoder-only template comes from [[Papers Explained 02 - BERT]].
- The first major lesson was that pretraining recipe quality matters at least as much as the base architecture, as shown by [[Papers Explained 03 - RoBERTa]].
- The second major lesson was that better pretraining objectives and better position handling both matter, as shown by [[Papers Explained 173 - ELECTRA]] and [[Papers Explained 08 - DeBERTa]].
- The modern phase combines long-context support, hardware-aware kernels, larger data, and specialization for retrieval or multilingual work, as shown by [[Papers Explained 277 - ModernBERT]], [[Papers Explained 327 - NeoBERT]], [[Papers Explained 465 - EmbeddingGemma]], and [[Papers Explained 471 - mmBERT]].

## Related

- [[Large Language Models]]
- [[Embedding and Retrieval]]
- [[Model Compression and Efficiency]]
- [[Multilingual Models]]
- [[Efficient Encoder Models]]
- [[Papers Explained 02 - BERT]]
- [[Papers Explained 03 - RoBERTa]]
- [[Papers Explained 07 - ALBERT]]
- [[Papers Explained 08 - DeBERTa]]
- [[Papers Explained 173 - ELECTRA]]
- [[Papers Explained 182 - DeBERTa V3]]
- [[Papers Explained 277 - ModernBERT]]
- [[Papers Explained 327 - NeoBERT]]
- [[Papers Explained 407 - Should We Still Pretrain Encoders with Masked Language Modeling]]
- [[Papers Explained 465 - EmbeddingGemma]]
- [[Papers Explained 471 - mmBERT]]

#summary #topic
