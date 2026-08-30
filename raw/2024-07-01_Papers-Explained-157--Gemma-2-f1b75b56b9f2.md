# Papers Explained 157: Gemma 2

Papers Explained 157: Gemma 2

Papers Explained 157: Gemma 2

Gemma 2 is a new addition to the Gemma family with several technical modifications, including interleaving local-global attentions and…

Papers Explained 157: Gemma 2

Gemma 2 is a new addition to the Gemma family with several technical modifications, including interleaving local-global attentions and group-query attention. The model is trained with knowledge distillation instead of next token prediction, which results in better performance for its size and competitive performance with larger models.

The models are available at HuggingFace.

Recommended Reading [Papers Explained 106: Gemma]

Model Architecture
Overview of the main model parameters and design choices.
Gemma 2 are somewhat similar to Gemma 1 models:

a context length of 8192 tokens
the use of Rotary Position Embeddings (RoPE)
the approximated GeGLU non-linearity

However there are several notable differences:

Gemma 2 alternates between a local sliding window attention and global attention in every other layer. The sliding window size of local attention layers is set to 4096 tokens, while the span of the global attention layers is set to 8192 tokens.
To stabilize training, RMSNorm is used to normalize the input and output of each transformer sub-layer, the attention layer, and the feedforward layer.
Both the 27B and 9B models use GQA with num_groups = 2
Following Gemini 1.5, the logits in each attention layer and the final layer are capped as logits ← soft_cap ∗ tanh(logits/soft_cap). For the 9B and 27B models, the attention logits are capped at 50.0 and final logits at 30.0.
Parameter counts for the Gemma models.
Pre Training

The pre-training data is primarily English and comes from a variety of data sources, including web documents, code, and science articles.

27B model is trained on 13T tokens
9B model on 8T tokens
2.6B model on 2T tokens

The same tokenizer as Gemma 1 and Gemini is used: a SentencePiece tokenizer with split digits, preserved whitespace, and byte-level encodings, resulting in a vocabulary of 256k.

The same data filtering techniques as Gemma 1 are used . Specifically, the pretraining dataset is filtered to minimize the risk of unwanted or unsafe utterances. Certain personal information or other sensitive data is filtered out. The evaluation sets in the pre-training data mixture are removed from the pre-training data mixture. The risk of recitation is minimized by eliminating the proliferation of sensitive outputs.

Increasing the length of training only scales logarithmically with dataset size, therefore the focus is to improve the quality of information received by the network at each training step by replacing the next token prediction task with a richer objective. Hence, the 9B and 2.6B models are trained using knowledge distillation with the 27B model as the teacher. Since the vocabulary has 256k entries, only a sampled subset of the teacher probabilities are stored.

Post Training

The post-training process for Gemma 2 models involves three phases:

Supervised Fine-Tuning (SFT): The pre-trained models are fine-tuned on a mix of text-only, English-only synthetic and human-generated prompt-response pairs using behavioral cloning and distillation from a larger teacher model.
Reinforcement Learning from Human Feedback (RLHF): The fine-tuned models are then used as the policy in an RLHF algorithm, where the reward model is trained on labeled English-only preference data and the policy is based on the same prompts as the SFT phase.
Model Merging: The models obtained after each phase are averaged to improve their overall performance. The models are merged using Warp, a new merging technique that merges models in three distinct stages:

Exponential Moving Average (EMA): This is applied during the reinforcement learning (RL) fine-tuning process.
Spherical Linear intERPolation (SLERP): This is applied after the RL fine-tuning of multiple policies.
Linear Interpolation Towards Initialization (LITI): This stage is applied after the SLERP stage.

The post-training recipe includes tuned hyperparameters chosen to improve helpfulness while minimizing model harms. The data mixtures used for post-training are a combination of internal and external public data, including prompts from LMSYS-chat-1M but not the answers.

Formatting

Gemma 2 models are fine-tuned with a different formatting schema from Gemma 1 models, but use the same control tokens.
Relevant formatting control tokens used for Gemma models.
The model explicitly ends generations with <end_of_turn><eos> tokens, while previously it only generated <eos>.
Example dialogue with user and model control tokens.
Evaluation

Pre-training Evaluations

Gemma 2 27B model outperforms Qwen1.5 32B and is only a few percent below LLaMA-3 70B despite being 2.5× smaller and trained on 2/3rds less data.

Overall, the Gemma 2 models are the best in their size category and are even competitive with a larger model that is trained for longer.

Post-training Evaluations
Evaluation of Gemma 2 9B and 27B Instruction Tuned models on the Chatbot Arena.
Preliminary results show that the Gemma 27B model sets a new state of the art for open-weights model, slightly surpassing the much larger Llama3–70BInstruct and Nemotron-4–340B-Instruct models.
Gemma 9B strongly outperforms all other models in the same range of parameters.

Paper

Gemma 2: Improving Open Language Models at a Practical Size

Recommended Reading [Gemini / Gemma Models] [Small LLMs]

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on July 1, 2024.

Canonical link

Exported from Medium on May 4, 2026.
