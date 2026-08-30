# Papers Explained 134: Open ELM

Papers Explained 134: Open ELM

Papers Explained 134: Open ELM

OpenELM is an open language model by Apple with not only open source model weights and inference code but the complete framework for…

Papers Explained 134: Open ELM

OpenELM is an open language model by Apple with not only open source model weights and inference code but the complete framework for training and evaluation of the language model.

It uses a layer-wise scaling strategy to efficiently allocate parameters within each layer of the transformer model, leading to enhanced accuracy.

The source code along with pre-trained model weights and training recipes are available at GitHub.

OpenELM Architecture

OpenELM adopts the decoder-only transformer-based architecture.

Learnable bias parameters are not used in any fully-connected (linear) layers
Pre-normalization is applied using RMSNorm
Rotary positional embedding (ROPE) is used for encoding positional information
Grouped query attention (GQA) is used instead of multi-head attention (MHA)
The feed forward network (FFN) is replaced with SwiGLU FFN
Flash attention is used for computing the scaled dot-product attention
The tokenizer from LLama is used.

Layer-wise scaling

A standard transformer model has N transformer layers and the dimensionality of the input to each layer is d_model. The MHA has n_h heads and dimension of each head is d_h = d_model /n_h .Also, the hidden dimension for FFN is d_FFN = m · d_model, where m is a scalar FFN multiplier.

Parameters α and β are introduced to scale the number of attention heads n_h and FFN multiplier m per layer, thus the width of the FFN layers respectively. For the i-th layer, n_h and m are computed as:

Pre-training data

Publicly available datasets totalling 1.8 T tokens used for pretraining.

Text filtering and tokenization are performed on the fly facilitating seamless experimentation with various tokenizers. Sequences having less than 200 characters or 256 tokens are removed.
Dataset used for pre-training OpenELM.
Training details

OpenELM variants are pre-trained for 350k iterations, with the following hyperparameters.
Pre-training details for different variants of OpenELM.
The cleaned variant of UltraFeedback dataset that consists of 60k prompts is used for instruction tuning using the Alignment Handbook library. For optimization, either the statistical rejection sampling method or the direct preference optimization method is used.
Instruction tuning details for different variants of OpenELM.
Evaluation

Tasks and metrics used for evaluating OpenELM.

Pre-training results

. OpenELM’s performance across training iterations on standard zero-shot tasks.

OpenELM shows an overall increase in accuracy with longer training durations.

Results on zero-shot tasks.Results on OpenLLM Leaderboard tasks.Results on LLM360 tasks.

OpenELM 1.1 B parameters 1.28% (Zero Shot Tasks), 2.36% (OpenLLM Leaderboard), and 1.72% (LLM360) higher accuracy compared to OLMo 1.2 B, while using 2× less pretraining data..

Instruction tuning results

Results on zero-shot tasks.Results on OpenLLM Leaderboard tasks.Results on LLM360 tasks.

Instruction tuning consistently improves OpenELM’s average accuracy by 1–2% across different evaluation frameworks.

Parameter-efficient fine-tuning (PEFT) results.

OpenELM with PEFT.

LoRA and DoRA deliver similar accuracy on average across the given CommonSense reasoning datasets.

Paper

OpenELM: An Efficient Language Model Family with Open-source Training and Inference Framework 2404.14619

Recommended Reading: [Small LLMs]

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on May 8, 2024.

Canonical link

Exported from Medium on May 4, 2026.
