# Distillation Regimes Compared

#summary #concept

Distillation is used for at least three different training regimes in the corpus: classical representation-level knowledge distillation, completion-distillation via [[Supervised Fine-Tuning]], and [[On-Policy Distillation]]. The first directly matches teacher probabilities, hidden states, attention maps, or embeddings; the second treats a teacher as a black-box data generator and trains on its completions; the third samples from the student policy and uses a teacher to provide dense token-level guidance on the student's own rollouts.

## Why The Term Is Overloaded

In older encoder-compression papers such as [[Papers Explained 05 - Tiny BERT]] and [[Papers Explained 06 - Distil BERT]], "distillation" means direct teacher-student matching. The teacher is available during training as a model whose outputs, logits, hidden states, attention matrices, or embeddings can be inspected. The student is trained not only to produce the correct answer, but to reproduce useful internal behavior of a larger model.

In modern LLM post-training usage, "distillation" often means something weaker and more black-box: collect completions from a stronger model, then train a smaller or cheaper model with SFT on those completions. [[Papers Explained 160 - Orca]] is a canonical example: it collects ChatGPT and GPT-4 responses, including explanation traces, and trains Orca on the teacher-generated response tokens. [[Papers Explained 394 - OpenThoughts]] follows the same broad pattern for reasoning data: source questions, generate teacher answers, optionally sample multiple answers per question, filter, and fine-tune a student.

[[On-Policy Distillation]] is a third meaning. It is not fixed teacher-completion SFT, because the responses come from the current student. It is also not classical full internal-state matching, because the core objective can be computed on student-sampled tokens rather than the teacher's full hidden computation. It is an on-policy teacher-guided update: the student visits its own states, then a teacher scores or reweights those sampled actions.

## Classical Representation-Level Distillation

Classical knowledge distillation assumes the teacher exposes rich training signals. In [[Papers Explained 06 - Distil BERT]], the student is trained with a distillation loss over the teacher's soft target probabilities. A temperature-scaled softmax smooths the teacher distribution, making relative probabilities among non-argmax labels visible to the student. DistilBERT combines this soft-target loss with the masked language modeling loss and a cosine embedding loss that aligns teacher and student hidden-state directions.

[[Papers Explained 05 - Tiny BERT]] makes the internal-matching version even more explicit. TinyBERT defines teacher and student behavior functions, then matches them across several levels:

- Embedding-layer distillation aligns student and teacher embeddings, with a learned projection when dimensions differ.
- Transformer-layer distillation maps student layers to selected teacher layers.
- Attention distillation matches per-head attention matrices.
- Hidden-state distillation aligns teacher and student hidden states, again using a projection when needed.
- Prediction-layer distillation matches teacher and student logits with temperature scaling.

The raw TinyBERT export (`raw/2023-02-06_Papers-Explained-05--Tiny-BERT-5e36fe0ee173.md`) emphasizes that the output of an MHA layer, FFN layer, attention matrix, or other intermediate representation can serve as the behavior function. The raw DistilBERT export (`raw/2023-02-06_Papers-Explained-06--Distil-BERT-6f138849f871.md`) frames KD as training a compact model to reproduce the behavior of a larger teacher or ensemble.

The "knowledge" here is not just a final answer. It is a dense geometry: how the teacher distributes probability mass, where it attends, how it represents tokens, and which hidden directions it uses. This makes classical KD especially natural for [[Model Compression and Efficiency]], where the goal is to make a smaller architecture inherit a larger architecture's competence without needing the original training budget.

## Completion-Distillation Via SFT

Completion-distillation treats the teacher as a sample generator rather than as an inspectable neural network. The pipeline is usually:

1. Choose or synthesize prompts.
2. Query a strong teacher model for completions.
3. Filter, deduplicate, rerank, or mix those completions.
4. Train a student with standard next-token loss on the saved teacher responses.

[[Papers Explained 160 - Orca]] shows this clearly. Each training instance is a triple of system message, user query, and large-foundation-model response. Orca samples 5 million FLAN-v2 user queries for ChatGPT responses and 1 million for GPT-4 responses. During training, the loss is computed only on teacher-generated tokens, so the student learns to produce the response conditioned on the instruction and system message. This is distillation in the sense of behavioral imitation, not in the sense of matching GPT-4's logits, attention maps, or hidden states.

[[Papers Explained 394 - OpenThoughts]] shows the modern reasoning-data version. The pipeline sources questions from fully synthetic, semi-synthetic, and non-synthetic sources, uses teacher models such as DeepSeek-R1 or QwQ-32B to generate answers, explores sampling multiple answers per question, and then trains reasoning models from the resulting corpus. The teacher's internal state is not the training target. The saved text is the artifact.

This is why modern "distilled" reasoning models can be simultaneously powerful and limited. The student receives high-quality demonstrations, including long reasoning traces, but the data distribution is fixed once the corpus is generated. If the student later improves and begins visiting different states, the teacher-completion dataset does not automatically adapt. The method is cheap after data generation, easy to run with black-box API teachers, and compatible across model families, but it is still offline imitation.

## On-Policy Distillation

[[On-Policy Distillation]] changes the sampling distribution. Instead of training on teacher-written completions, the student samples its own responses. A teacher then evaluates the exact tokens the student sampled, often through a log-probability difference or reverse-KL-style token advantage. The student receives dense token-level guidance, but the states are on-policy because they come from the student's current behavior.

[[Papers Explained 552 - Nemotron Cascade 2]] is the strongest corpus anchor. Its Multi-domain On-Policy Distillation stage uses teachers selected from the Cascade RL pipeline. For each prompt, a student response is sampled, a domain teacher is selected, and the token-level distillation advantage is defined from the teacher-student log-probability difference. The loss is applied only to valid response tokens, and truncated importance weighting corrects mismatch between inference-time sampling and training-time optimization.

OPD therefore occupies a middle ground. Like completion-SFT, it uses a teacher and remains teacher-bounded. Like [[Reinforcement Learning]], it samples from the current student policy, so the training signal can follow the student's evolving mistakes and capabilities. Unlike pure RL, it can provide dense token-level signal instead of waiting for a sparse verifier or reward model.

Same-family teacher choice matters much more for OPD than for completion-SFT. A GPT-4 response can be useful SFT data for a Llama-family student even if the tokenizers differ, because the target is just text. In OPD, the teacher is assigning probability to student-sampled tokens. If teacher and student have different tokenizers, chat templates, or recipe artifacts, the token-level signal becomes harder to interpret. This is why [[Papers Explained 552 - Nemotron Cascade 2]] emphasizes teachers from the same pipeline and shared vocabulary.

The visual article [[SFT, RL, and On-Policy Distillation Visual Notes]] sharpens the comparison by drawing SFT as dense forward-KL-like pressure over a dataset distribution, RL as sparse pressure through current-policy samples, and OPD/MOPD as same-family teacher scoring on student rollouts. Its figures also show a practical caveat: token-level KL can concentrate on style or mode-control tokens rather than the task tokens a practitioner may care about most.

## Comparison Matrix

| Axis | Classical KD, e.g. DistilBERT/TinyBERT | Completion-distillation SFT | On-Policy Distillation |
| --- | --- | --- | --- |
| Teacher interface | White-box or at least logit-access teacher | Black-box text generator is enough | Usually log-probability access on student-sampled tokens |
| Training data | Fixed input corpus; teacher and student run on same inputs | Saved prompt-completion corpus generated by teacher | Prompts plus current student rollouts |
| Student distribution | Mostly not on-policy; the input distribution is fixed | Not on-policy after corpus generation | On-policy or near-on-policy |
| Target signal | Soft probabilities, logits, hidden states, attention matrices, embeddings | Hard text completions and reasoning traces | Dense token-level teacher advantage on sampled tokens |
| Typical loss | KL/cross-entropy on soft targets, MSE/cosine losses for representations, supervised auxiliary losses | Next-token SFT loss on teacher response tokens | Policy-gradient-like objective with teacher-derived token advantages; often reverse-KL flavored |
| Teacher-family constraint | Strong when matching internal states; architectures and dimensions must be mapped | Weak; any teacher that writes useful text can help | Strong; same tokenizer/vocabulary/template makes token-level probabilities meaningful |
| Main goal | Compress a model while preserving behavior and representations | Transfer behaviors, style, reasoning traces, or task solutions into a student | Improve or rebalance a student on its own state distribution with dense teacher guidance |
| Cost profile | Teacher is queried throughout training; can be expensive but highly informative | Expensive data generation, then ordinary SFT | Expensive rollout plus teacher scoring loop, but often denser than RL |
| Ceiling | Teacher-bounded, though auxiliary supervised losses help | Teacher/data-bounded | Teacher-bounded unless combined with verifier or reward learning |
| Main failure mode | Overconstraining a student to teacher internals; poor layer mapping; architecture mismatch | Frozen dataset, teacher style overfitting, hallucinated demonstrations, no compounding | Tokenizer/recipe mismatch, stale rollout-policy mismatch, dense biased gradients suppressing exploration |

## The Key Conceptual Differences

The first difference is what counts as the teacher signal. Classical KD says the signal is the teacher's probability distribution and internal computation. Completion-SFT says the signal is a sampled teacher answer. OPD says the signal is the teacher's judgment about the student's sampled action.

The second difference is when the teacher is consulted. In classical KD, the teacher may be used throughout training to produce logits or representations for each batch. In completion-SFT, the teacher is usually used before training to build a dataset. In OPD, the teacher is consulted during the on-policy loop, after the student has generated rollouts.

The third difference is whether the data improves with the student. Completion-SFT does not automatically compound: the dataset remains the same even if the student changes. OPD can track the student because every round samples from the current policy. Classical KD can be repeated on new data, but the central setup is still teacher behavior on a fixed input distribution.

The fourth difference is softness. Classical KD is soft at the distribution and representation level. Completion-SFT is hard: the student sees one or more sampled strings, not the teacher's uncertainty. OPD recovers some softness by asking how much more or less likely the teacher would make each student-sampled token.

## Practical Decision Rule

Use classical representation-level KD when the objective is compression and the teacher is accessible enough to expose logits, hidden states, attention maps, or embeddings. DistilBERT and TinyBERT are archetypal because they are about making BERT-family encoders smaller, faster, and cheaper while preserving behavior.

Use completion-distillation SFT when the teacher is a strong black-box generator and the main bottleneck is high-quality data. Orca-style explanation tuning and OpenThoughts-style reasoning corpora fit here. This is the most flexible regime across model families, but it is also the most offline.

Use OPD when the student needs guidance on its own rollouts and a same-family or closely matched teacher can score those rollouts. It is especially useful after RL or multi-domain post-training, where specialized teachers can consolidate strengths back into a single student, as in [[Papers Explained 552 - Nemotron Cascade 2]].

## Related

- [[SFT, RL, and On-Policy Distillation Visual Notes]]
- [[Sasha Rush Explains Targeted On-Policy Self-Distillation]] — Sasha Rush's verbal walkthrough of the three-regime progression (sequence KD → OPD → OPSD), with a tennis analogy distinguishing off-policy imitation from on-policy correction.
- [[Model Distillation]]
- [[On-Policy Distillation]]
- [[On-Policy Self-Distillation]]
- [[Supervised Fine-Tuning]]
- [[Reinforcement Learning]]
- [[Policy Gradient]]
- [[KL Regularization]]
- [[Model Compression and Efficiency]]
- [[Large Language Models]]
- [[Synthetic Data]]
- [[Papers Explained 05 - Tiny BERT]]
- [[Papers Explained 06 - Distil BERT]]
- [[Papers Explained 160 - Orca]]
- [[Papers Explained 394 - OpenThoughts]]
- [[Papers Explained 552 - Nemotron Cascade 2]]
- [[Papers Explained: On-policy Distillation with Verifiable Reward]] — [[OPDVR]] and [[GRPD]] combining OPD with verifiable rewards via ReLU gating.
- [[OPDVR]]
- [[GRPD]]
