# Papers Explained 426: Arcee Foundation Models

Papers Explained 426: Arcee Foundation Models

Papers Explained 426: Arcee Foundation Models

Arcee Foundation Models is a new family of generative AI models built from the ground up for enterprise reality. Combined with built-in…

Papers Explained 426: Arcee Foundation Models

Arcee Foundation Models is a new family of generative AI models built from the ground up for enterprise reality. Combined with built-in support for function calling and agentic reasoning, AFM-4.5B is ready to automate complex workflows immediately i.e. no fragile prompt engineering required.

The development of Arcee Foundation Model (AFM) was driven by the following issues:

Performance and Size Gaps: Edge-optimized models weren’t simply reliable enough for demanding tasks. Customers needed a model that could run on modest hardware, yet still deliver top-tier accuracy and robustness.
Regulatory and Licensing Friction: The most advanced models from major Chinese AI labs (Deepseek, Qwen, GLM, MiniCPM) offered impressive results, but rarely satisfied Western compliance standards, disqualifying them for regulated industries.
Stagnant Western Alternatives: Models from Meta (Llama) and Mistral, while solid, were quickly becoming outdated in relevance. The 3–10B parameter space was primarily served by models a year old or older, outpaced by newer research, data pipelines, and post-training strategies.

Pre Training

Uncompromising Data Quality: Arcee AI partnered with DatologyAI to assemble 6.58 trillion tokens of high-quality, relevant data.
Data Curation Challenges: Data curation for foundation models is a frontier research and engineering problem, requiring expertise in algorithms, scaling, and implementation.
DatologyAI’s Pipeline: DatologyAI’s curation pipeline integrates proprietary algorithms, including model-based quality filtering, embedding-based curation, target distribution-matching, source mixing, and synthetic data. These algorithms were customized to generate a strong general-purpose dataset that also targeted the capabilities Arcee AI wanted their model to have.
Early Results: By 2 trillion tokens, AFM-4.5B was already outperforming competing models trained on dramatically larger, but noisier datasets.

Post Training

The process begins with midtraining, where the model was infused with high-leverage datasets (math, code, complex reasoning) and carefully selected samples from DatologyAI’s corpus. This step gave the model strong early instincts for precision and clarity. From there, checkpoint merging was performed, consolidating and enhancing intermediate models into a cohesive base. Context length was extended using YaRN, a rotary scaling method that retains performance at scale, and this long-context foundation was refined through advanced merging using MergeKit, which allowed precise control over the model’s composition — layer-wise weighting, residual scaling, and targeted integrations — all of which contributed to consistency across varied tasks.

Next, supervised fine-tuning was conducted, focusing on instruction clarity, diversity, and alignment. Here, the model learned to adapt to a wide range of prompts — from legal analysis to creative writing — while avoiding the overfitting that weakens many instruction-tuned models.

Finally, reinforcement learning was applied using verifiable reward signals, helping the model prefer factual, high-utility responses. Post-RL merges smoothed out inconsistencies, followed by KTO, an alignment method where the model learns directly from trusted reference behavior.

Evaluations

Paper

Announcing Arcee Foundation Models
Deep Dive: AFM-4.5B, the First Arcee Foundation Model

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on August 7, 2025.

Canonical link

Exported from Medium on May 4, 2026.
