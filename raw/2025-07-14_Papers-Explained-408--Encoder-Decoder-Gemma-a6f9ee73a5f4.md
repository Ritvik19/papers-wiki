# Papers Explained 408: Encoder-Decoder Gemma

Papers Explained 408: Encoder-Decoder Gemma

Papers Explained 408: Encoder-Decoder Gemma

Papers Explained 408: Encoder-Decoder Gemma

This paper studies a novel problem: adapting pre-trained decoder-only LLMs to encoder-decoder, with the goal of leveraging the strengths of both approaches to achieve a more favorable quality-efficiency trade-off.

Approach: Encoder-Decoder Adaptation

Architecture
Overview of the approach.
Pretraining LLMs is both compute and time intensive. To reduce the amount of training required, existing decoder-only LLMs are adapted to encoder-decoder and leverage pretrained decoder-only checkpoints for initialization.

The encoder has exactly the same architecture as the decoder-only model, but self-attention is switched from causal to bidirectional.
In each Decoder block, FFN and self-attention parts are identical to the corresponding parts in decoder-only models, and cross-attention has the same number of heads and head dimensions as self-attention, but attends to the whole output of the encoder.

This study is based on Gemma 2 but the method can easily be applied to other model families. Additionally, this approach allows for unbalanced encoder-decoder models, where the decoder is significantly smaller than the encoder. This provides better support for applications where input processing capabilities are more important than generative capacity.

For example, for summarization, deep understanding of the input text is often more important than the generation part, as it doesn’t need to generate any new information. As a result, generation time is significantly reduced, while providing competitive quality.

Initialization

The encoder is fully initialized from the decoder-only checkpoint, as it doesn’t introduce any new weights.

In the decoder, FFN and self-attention subblocks are initialized from the FFN and self-attention weights from the corresponding layers in the decoder-only checkpoint. Cross-attention is initialized from self-attention weights in the balanced setup where encoder and decoder have the same configuration.

Otherwise, cross-attention is first initialized from scratch and then finetuned for the first K steps as a warmup while freezing other model parameters. After K steps, all model parameters are tuned.

In unbalanced encoder-decoder adaptation, e.g. 9B-2B, the cross-attention warmup step Kto is set to 1000.

Pretraining Objective

Two classical pretraining objectives for encoder-decoder modeling are explored: prefix language modeling (PrefixLM) and UL2.

Prefix Language Modeling (PrefixLM)

PrefixLM is a pre-training objective that combines aspects of both causal language modeling and encoder-decoder architectures. It trains the model to predict subsequent tokens given a context or “prefix”.
A sequence of text is split into two parts: a prefix and a suffix.
The model is trained to predict the suffix, conditioned on the prefix.
During pretraining, the prefix is usually chosen at random for each sample.

UL2

UL2 is a unified pre-training framework designed to improve language model performance across various datasets and setups. It employs a “Mixture-of-Denoisers” (MoD) pre-training objective, combining diverse pre-training paradigms.
R-denoising (Regular Span Corruption): Emulates the standard T5 span corruption objective.
X-denoising (Extreme Span Corruption): Involves aggressive denoising, where a significant portion (e.g., 50%) of the input sequence is masked by increasing the span length and/or corruption rate.
S-denoising (Sequential PrefixLM): A sequential or prefix language modeling approach.
A paradigm token (e.g., [R], [X], or [S]) is appended to the input to indicate the denoising task at hand.

Data Setting

Data for pretraining and instruction tuning, including supervised finetuning (SFT) and reinforcement learning from human feedback (RLHF), follow Gemma 2.

Model Setting

Gemma 2 (2B and 9B) is used as the base decoder-only LLM. Several smaller models (Small, Base, Large, and XL) are pretrained following mT5 configurations under the Gemma 2 framework, and then adapted to encoder-decoder LLMs.
Model configurations.
Evaluation Settings

Pretraining (PT) benchmarks: Boolq, SIQA, PIQA, ARC-c & ARC-e, MMLU, MMLU Pro, HellaSwag, Winogrande, TruthfulQA, AGIEval, BBH, DROP, GPQA, GSM8K, HumanEval, Lambada, MATH-500, MBPP, NQ, TriviaQA, WMT23,

Instruction-tuning (IT) benchmarks: GSM8K, MMLU, MMLU Pro, MBPP, HumanEval, MATH-500, BBH, GPQA (Diamond), WMT23, MGSM

SuperGLUE:

Used to examine the learned contextual representation.
A task-specific head is stacked on the representation of the last token in the encoder (decoder) of the encoder-decoder (decoder-only) LLM.
All parameters are finetuned on the training set.

Evaluation
Pretraining performance as a function of the number of pretrained tokens during the adaptation.
Rapid Convergence & Efficiency: The encoder-decoder adaptation converges rapidly, particularly for balanced architectures, demonstrating high computational efficiency.
Architecture Impact on Convergence: Balanced architectures (e.g., 2B-2B, 9B-9B) converge significantly faster than unbalanced ones (e.g., 9B-2B) because all parameters in the former are initialized from pretrained decoder-only models, unlike the randomly initialized cross-attention in the latter.
Feasibility of Varying-Sized Adaptation: The consistent performance increase of the 9B-2B model, quickly surpassing Gemma 2 2B and moving towards Gemma 2 9B, demonstrates the feasibility of encoder-decoder adaptation from varying-sized decoder-only LLMs and their ability to utilize pretrained knowledge.
Main results on PT, IT, and SuperGLUE benchmarks.
Impact of Pretraining Objective:
UL2 delivers stronger contextual representations, outperforming PrefixLM on SuperGLUE across most model scales.
PrefixLM, enhanced with knowledge distillation, produces more powerful generative LLMs, surpassing UL2 on PT and IT benchmarks in most cases.
Performance Improvement over Decoder-Only LLMs: Adapted encoder-decoder LLMs achieve comparable or slightly better pretraining performance but substantially improved instruction-tuning performance compared to their decoder-only counterparts (e.g., 9B-9B encoder-decoder surpasses Gemma 2 9B by 1.4 on PT and 4.9 on IT).
Superior Contextual Representation: Encoder-decoder LLMs consistently perform better than decoder-only LLMs on SuperGLUE, suggesting higher quality contextual representations, likely due to bidirectional self-attention.
Detailed results on different tasks for PT and RLHFed models.
Task-Specific Performance Variability: Performance can vary significantly across specific downstream tasks, with some favoring encoder-decoder models while others favor decoder-only models, especially for PT models. This illustrates the complexity of LLM evaluation and the risk of reaching misleading conclusions with biased evaluation tasks.
Comparisons of decoder-only LLMs with adapted encoder-decoder models under inference flops.
Improved Quality-Efficiency Trade-Off: Encoder-decoder LLMs balance quality and inference efficiency more effectively, exhibiting similar inference flops and latency to their decoder-only counterparts while delivering clearly better performance.
Specifically, the 9B-2B model shows similar latency to Gemma 2 2B but significantly better performance than 2B-2B, confirming the flexibility of encoder-decoder adaptation in balancing quality and inference speed.
Is the improvement after the adaptation simply due to the extra pretraining compute?: The improvement from adaptation (PT score 49.7) was not solely due to extra compute, as Gemma 2 2B with more pretraining only reached 48.57. This suggests that the inductive bias of encoder-decoder modeling plays a crucial role in the oberved gains.
Results for encoder-decoder models adapted with PrefixLM (Adaptation) and pretrained from scratch (Scratch).
Pretraining from Scratch vs. Adaptation: Pretraining from scratch only yielded better performance at smaller scales (S-S, B-B); beyond these, adaptation showed clear superiority. This demonstrates that adaptation is a more computationally efficient method for developing powerful encoder-decoder LLMs compared to pretraining from scratch.

Impact of Bidirectional Self-Attention: Keeping the encoder self-attention causal significantly reduced performance (PT 45.6, IT 41.7) compared to its bidirectional counterpart (lagging by 4.1 and 4.7, respectively). This indicates that bidirectional self-attention contributes greatly to the success of the adaptation, though it is not the only factor.

Importance of Cross-Attention Warmup: Pretraining performance (Boolq and GSM8K) decreased without warmup (from 62.5 to 61.8) and with increased warmup steps (to 60.2 for 5K steps). This highlights the necessity of an adequate amount of cross-attention warmup optimization for optimal performance in unbalanced encoder-decoder models.

Encoder Attention Mechanism (GQA vs. MHA): While MHA improved PT performance (to 50.2 by 0.5), it reduced IT performance (to 43.5 by 2.9). Due to these mixed results, the authors decided to stick with GQA for the encoder when adapting Gemma 2 2B and 9B.

Paper

Encoder-Decoder Gemma: Improving the Quality-Efficiency Trade-Off via Adaptation 2504.06225

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on July 14, 2025.

Canonical link

Exported from Medium on May 4, 2026.
