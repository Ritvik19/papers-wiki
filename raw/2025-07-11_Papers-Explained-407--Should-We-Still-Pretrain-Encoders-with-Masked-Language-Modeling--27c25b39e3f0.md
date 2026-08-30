# Papers Explained 407: Should We Still Pretrain Encoders with Masked Language Modeling?

Papers Explained 407: Should We Still Pretrain Encoders with Masked Language Modeling?

Papers Explained 407: Should We Still Pretrain Encoders with Masked Language Modeling?

While encoder pretraining has traditionally relied on Masked Language Modeling (MLM), recent evidence suggests that decoder models…

Papers Explained 407: Should We Still Pretrain Encoders with Masked Language Modeling?

While encoder pretraining has traditionally relied on Masked Language Modeling (MLM), recent evidence suggests that decoder models pretrained with Causal Language Modeling (CLM) can be effectively repurposed as encoders, often surpassing traditional encoders on text representation benchmarks.

This paper addresses whether these gains reflect an inherent advantage of the CLM objective or arise from confounding factors such as model and data scale, through a series of large-scale, carefully controlled pretraining ablations. A total of 38 models ranging from 210 million to 1 billion parameters were trained, and over 15,000 fine-tuning and evaluation runs were conducted.

Training with MLM generally yields better performance across text representation tasks. CLM-trained models are more data-efficient and demonstrate improved fine-tuning stability.

Experimental Setup
Experimental setup overview and key results on sequence classification.
Models:

The model architectures closely follow those of the EuroBERT models, with sizes of 210M, 610M, and 1B parameters. All models use a maximum context length of 2,048 tokens and a RoPE θ value of 10,000.

Pretraining data:

Models are trained on unique English tokens from the FineWeb-Edu dataset, which is known for supporting efficient model training.

Pretraining objectives:

Models are trained using one of 3 approaches:

CLM uses next-token prediction, where each token is predicted autoregressively using a causal attention mask. The training objective is to minimize the negative log-likelihood:

MLM, by contrast, randomly masks a subset of tokens and trains the model to reconstruct them using a bidirectional attention mask. The objective is:

A two-stage CLM+MLM approach sequentially applies CLM pretraining followed by MLM.

Pretraining hyperparameters:

Pretraining is performed with a per-device batch size of 12 samples across 192 GPUs, yielding an effective batch size of 2,373,120 tokens. A Warmup-Stable-Decay (WSD) learning rate schedule is employed: a 2,000-step warmup phase, followed by 38,000 steps with a constant learning rate of 5e-4, ending with a 2,000-step linear decay phase, for a total of 42,000 training steps.

Pretraining Setups

Pretraining From Scratch (PFS):

Initialization: Models are trained from random initialization.
Objectives: CLM, MLM, or sequential CLM+MLM.
Learning Rate: Standard WSD scheduler for CLM and MLM. For CLM+MLM, CLM training is performed first, then MLM is resumed from CLM checkpoints that have not yet undergone learning rate decay.

Continued PreTraining (CPT):

Initialization: Models are initialized from existing checkpoints pretrained with either CLM or MLM.
Objective: Training is resumed using the MLM objective.
The pretrained models used for CPT have already undergone learning rate decay during their initial training.
CPT starts from checkpoints where the loss has already converged, unlike PFS where the objective switch often occurs during active learning.

Fine-tuning tasks and datasets:

Sequence Classification: SST-2, MNLI and QQP.
Token Classification: English subsets of CoNLL, OntoNotes and UNER.
Question Answering: SQuAD, SQuAD-v2, and ReCoRD.
Information Retrieval: MS MARCO, NQ and the English subset of MLDR for long-context evaluation.

Fine-tuning Protocol

Training Length: Up to 1,000 steps or one full epoch, whichever comes first.
Batch Size: 32.
Learning Rate Selection: A grid search is performed over 6 learning rates (1e-5, 2e-5, 5e-5, 1e-4, 2e-4, and 5e-4) for each model-dataset pair.
Learning Rate Schedule: 10% warmup followed by linear decay. The learning rate yielding the best validation performance is selected.
Attention Mask: Bidirectional attention mask is used.
Loss Functions:
SC: Cross-entropy on mean-pooled token embeddings.
TC & QA: Token-level cross-entropy.
IR: InfoNCE loss with in-batch negatives, using mean pooling.
Stability: The entire procedure is repeated across 5 random seeds to account for fine-tuning instability commonly observed in BERT-style models.
Training Data: Fine-tuning is conducted on the in-domain training set, except for NQ and MLDR, which are trained on MS MARCO.

Evaluation protocol:

SC is assessed with accuracy, TC and QA with F1 score, and IR with NDCG@10.

Results are reported averaged across seeds, along with 95% confidence intervals.

Pretraining with CLM or MLM
MLM vs. CLM downstream performance, averaged across tasks and reported for all model sizes.
MLM generally outperforms CLM on text representation tasks, particularly on SC (Sentence Classification) and QA (Question Answering), attributed to its bidirectional attention during pretraining.
The performance gap between MLM and CLM on SC and QA tasks is consistent across model sizes, with QA being particularly sensitive to the absence of bidirectional attention.
Task-specific trends exist for the MLM-to-CLM gap: it widens with increasing model size on SC but narrows on IR (Information Retrieval).
CLM models can perform competitively, achieving strong results on token-level tasks (TC) and even outperforming MLM at the 610M size, despite generally underperforming on SC, QA, and IR.
Task-wise downstream performance across different masking ratios for all model sizes.
There is no universally optimal masking ratio for MLM pretraining; it depends on both model size and the specific downstream task, making it a delicate balance. (Refers to Figure 3: demonstrates how the optimal masking ratio varies with model size and downstream task).
Masking ratio preferences vary: larger models tend to benefit from higher ratios, IR datasets consistently prefer higher ratios, while smaller models for token-level tasks (TC — Token Classification, QA) perform better with lower ratios. Larger models (610M and 1B) exhibit a U-shaped performance curve, indicating improved performance at both low and high masking ratios.
Downstream performance as a function of pretraining steps for CLM and MLM objectives.
CLM is more data-efficient than MLM in the early stages of training, consistently outperforming MLM in downstream performance during initial training steps.
CLM’s early efficiency makes it an appealing option for data-scarce scenarios (e.g., low-resource languages) or as a warmup stage before MLM-based encoder training, even though MLM models tend to catch up and surpass CLM in later training stages.
Impact of the fine-tuning learning rate on MLM- vs. CLM-pretrained models.
CLM-based pretraining improves fine-tuning stability, demonstrating lower sensitivity to learning rate choices compared to MLM.
CLM pretraining provides a more stable initialization for fine-tuning, leading to more reliable performance and reducing the need for extensive hyperparameter tuning.

Two-Stage CLM+MLM Pretraining
Impact of two-stage CLM+MLM pretraining on downstream performance under different training
budgets.
Starting pretraining with CLM and continuing with MLM (two-stage approach) yields better results than using MLM alone under fixed compute constraints.
Combining CLM and MLM consistently improves downstream performance compared to using MLM alone, though the effect varies by task and training budget.
A split between 25%-75% (CLM-MLM) and 50%-50% (CLM-MLM) appears to provide the best balance for two-stage pretraining.
Comparison of downstream performance variability across different masking ratios for CLM and CLM+MLM pretraining configurations.
CLM-based models exhibit lower sensitivity to the masking ratio compared to fully MLM-trained models.
Initial CLM pretraining appears to stabilize model weights, making adaptation more robust to masking ratio choices and yielding more consistent downstream performance that is less sensitive to this design parameter.

Continued Pretraining from CLM and MLM Models
Impact of performing MLM CPT on either CLM- or MLM-pretrained models.
MLM CPT applied to a CLM-pretrained model consistently achieves superior downstream performance compared to continuing MLM-only training.
On Text Classification (TC), the strong performance of CLM-only models was maintained, and the gap to MLM remained.
For Question Answering (QA) and Information Retrieval (IR), the performance gap between CLM and MLM was effectively closed.
For Semantic Classification (SC), the MLM-adapted CLM model significantly outperformed the MLM-only model.
MLM loss curves for CLM- and MLM-pretrained models across the 3 CPT compute budgets.
It is not necessary to run the full 22,000 CPT steps; strong performance comparable to MLM-only CPT can be achieved with fewer steps.
As early as 12,000 CPT steps, results are already strong and broadly match those of MLM-only CPT in terms of loss and downstream performance, with better results on TC and IR, comparable on SC, and nearly on par on QA.
Downstream performance as a function of CPT length for CLM- and MLM-pretrained models.
Applying MLM CPT on a CLM model shows a more promising trend with a steeper improvement curve toward the end, whereas MLM-only training tends to plateau (particularly noticeable on SC).

Paper

Should We Still Pretrain Encoders with Masked Language Modeling? 2507.00994

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on July 11, 2025.

Canonical link

Exported from Medium on May 4, 2026.
