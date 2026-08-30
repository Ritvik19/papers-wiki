# Papers Explained 93: TinyLlama

Papers Explained 93: TinyLlama

Papers Explained 93: TinyLlama

TinyLlama is a compact 1.1B language model built upon the architecture and tokenizer of Llama 2, pre-trained on around 1 trillion tokens…

Papers Explained 93: TinyLlama

TinyLlama is a compact 1.1B language model built upon the architecture and tokenizer of Llama 2, pre-trained on around 1 trillion tokens for approximately 3 epochs, leveraging various advances (e.g., FlashAttention), to achieve better computational efficiency.

The model checkpoints and code are publicly available on GitHub

Recommended Reading [Papers Explained 55: LLaMA] [Papers Explained 60: Llama 2]

Approach

Pre-training data

A mixture of natural language data and code data is used to pre-train TinyLlama, sourcing natural language data from SlimPajama and code data from Starcoderdata.

SlimPajama is a large open-source corpus derived by cleaning and deduplicating the original RedPajama,. which is an open-source research effort aimed at reproducing Llama’s pre-training data.

Starcoderdata was collected to train StarCoder, comprising approximately 250 billion tokens across 86 programming languages.

Combining these two corpora yields approximately 950 billion tokens for pre-training in total. TinyLlama is trained on these tokens for approximately three epochs. During training, the natural language data is sampled to achieve a ratio of around 7:3 between natural language data and code data.

Architecture
Details of model architecture.
A similar model architecture to Llama 2 is adopted with the following details:

RoPE (Rotary Positional Embedding) to inject positional information into the model.
In pre-normalization, to attain a more stable training, the input is normalized before each transformer sub-layer using RMSNorm, which can improve training efficiency.
Following Llama 2 SwiGLU is used as the activation function.
To reduce memory bandwidth overhead and speed up inference, grouped-query attention is used. There are 32 heads for query attention and 4 groups of key-value heads. With this technique, the model can share key and value representations across multiple heads without sacrificing much performance.
Another critical improvement is the integration of Flash Attention 2, an optimized attention mechanism. The repository also provides fused layernorm, fused cross entropy loss, and fused rotary positional embedding, which together play a pivotal role in boosting computational throughput

Evaluation

Commonsense reasoning tasks
Zero-shot performance on commonsense reasoning tasks.
TinyLlama achieved the highest average scores among the evaluated models.

Evolution of performance during training
Evolution of performance in commonsense reasoning benchmarks during pre-training.
Improvement in TinyLlama’s performance with increased computational resources
Surpassed Pythia-1.4B accuracy in most benchmarks

Problem-solving evaluation
Performance of problem-solving tasks on the InstructEval Benchmark.
TinyLlama demonstrates better problem-solving skills compared to existing models.

Paper

TinyLlama: An Open-Source Small Language Model 2401.02385

Recommended Reading [Decoder-Only Language Transformers]

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on January 22, 2024.

Canonical link

Exported from Medium on May 4, 2026.
