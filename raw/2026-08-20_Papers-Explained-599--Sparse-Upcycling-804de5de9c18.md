# Papers Explained 599: Sparse Upcycling

Papers Explained 599: Sparse Upcycling

Papers Explained 599: Sparse Upcycling

Sparse upcycling is a simple way to reuse sunk training costs by initializing a sparsely activated Mixture-of-Experts model from a dense…

Papers Explained 599: Sparse Upcycling

Sparse upcycling is a simple way to reuse sunk training costs by initializing a sparsely activated Mixture-of-Experts model from a dense checkpoint. Sparsely upcycled T5 Base, Large, and XL language models and Vision Transformer Base and Large models, respectively, significantly outperform their dense counterparts on SuperGLUE and ImageNet, using only ∼ 50% of the initial dense pretraining sunk cost. The upcycled models also outperform sparse models trained from scratch on 100% of the initial dense pretraining computation budget.

Router Types

Expert Choice Routing: The router assigns each expert a quota (based on the capacity factor 𝐶), so each expert chooses its top- 𝐶 tokens to process, rather than each token going to its 𝐾 best experts. This emphasizes expert-centric selection: each expert picks which tokens to attend to.

Top-K Routing: Each token is sent to its top 𝐾 most suitable experts according to the router. This is token-focused: for each input token, the router decides which 𝐾 experts process it.

The Upcycling Algorithm
The upcycling initialization process.
The number and shape of Transformer blocks in the new model is identical to that in the original dense model. A subset of the MLP layers are expanded into MoE layers. The remaining MLP layers, along with all of the layer-norm and attention layers, and the embedding and output layers are copied across from the original model to the new model. Each MoE layer contains a fixed number of experts. Each expert is initialized as a copy of the original MLP. In addition, a router is added whose weights are randomly initialized.

Different variations on this basic recipe are experimented with. After the new model is loaded and initialized, it is continued training for a number of additional steps depending on the available budget and resources. The original hyperparameters are used: same batch size, learning rate schedule, and weight decay leading to the original checkpoint.

Design Decisions

Router type: For upcycled vision models and for the encoder of upcycled language models, Expert Choice routing with capacity factor C = 2 is used. To avoid train time (full batch teacher forcing) versus inference time (single token auto-regressive decoding) discrepancies, Top-K (K = 2) routing is used in the language decoder.
Number layers to upcycle: Adding more MoE layers increases the model capacity dramatically, at the expense of increasing the model’s cost, and also causing the quality of the upcycled model to initially drop further relative to the original dense model. Half of the MLP layers in the upcycled models are replaced with MoE layers.
Number of experts to add in upcycled layers: Each new expert provides new learnable parameters that extend the model capacity. The expert capacity i.e. the number of tokens each expert processes, is inversely proportional to the number of experts, thus adding more experts does not significantly affect the FLOPS or the run time of the model. However, with a very large number of experts, the upcycled model experiences a larger initial quality drop relative to the baseline dense model. Given sufficient upcycling compute, this initial drop can be overcome. Upcycling with +20% to +100% of the initial dense baseline model’s computational cost, 32 experts provides a good compromise.
Expert capacity: By tuning the expert capacity, C, the number of experts that process each token on average is controlled. Larger expert capacity generally yields larger quality but also increases the FLOPS and run time. Although increasing the expert capacity yields quality gains on a per step basis, C = 2 generally offers good quality on a compute time basis.
Resuming optimizer state (vision only): When upcycling a model, the optimizer state can be resumed from the original dense checkpoint together with the model parameters. Reusing the optimizer state gives a performance boost for vision models. However, no improvement was observed from reusing the dense model optimizer state in language experiments, so the optimizer state is only reused for vision models.
Normalize weights after routing (vision only): In an effort to reduce the performance drop when applying the upcycling model surgery, an attempt was made to normalize the router combine weights of each token to 1. This follows the intuition that each token was previously only processed by a single “expert” MLP in the dense model. Router weight normalization helps upcycled vision models, but hurts the performance of upcycled language models. One hypothesis for this different behavior is that the vision models use Expert Choice routing everywhere, but the language models use Expert Choice in the encoder and Top-K routing in the decoder.

Experiments

All upcycled experiments begin from a pretrained dense model checkpoint. Because all starting dense checkpoints are trained with an inverse square root learning rate schedule, training can be continued without discontinuities in the learning rate schedule. As a baseline, the training of the original dense model (“dense continuation”) is also continued.

For MoE Vision Transformers (“V-MoE”) models, upstream pretraining is done on JFT300M, with validation metrics computed on a held-out set of 894,574 examples. For few-shot transfer, a least-squares regressor predicts one-hot classes given frozen image representations. Results on ImageNet are further validated using 10-shot, i.e., 10 training examples per class. This is done for 5 different training sets, and average accuracy is reported across them. For full finetuning, the pretraining head is replaced with a randomly initialized head, and the entire network is finetuned.

For language experiments, pretraining uses the span corruption task on the English C4 dataset, and finetuning is performed on a proportional mix of all SuperGLUE tasks. For Base model sizes, the dense baseline starting checkpoint is pretrained independently. To highlight the versatility of the upcycling algorithm, for Large and XL models, all experiments begin from official T5 1.1 checkpoints.

Results
Pretraining performance achieved by the dense continuation and upcycling methods, for different Transformer variants.
Upcycled models show strong performance gains over dense continuation models when given a non-trivial extra compute budget
With limited extra training, dense and upcycled models perform similarly, close to the original checkpoint; substantial improvement appears only after more computation is applied.
Full finetuning performance achieved by the dense continuation and upcycling methods.
Upstream gains from upcycled vision models transfer well downstream after finetuning, while upcycled language models show more variance but are generally favored over dense counterparts.
Pretraining performance achieved by the upcycling method and a MoE model trained from scratch.
Sparse upcycling is more efficient than training sparse models from scratch, since it leverages the computation already invested in the dense checkpoint; sparse-from-scratch requires additional computation to catch up.
MoE models trained from scratch eventually match upcycled models if computation budget is large (>100% of original), but upcycling is best for limited compute (<100%), indicating it is an efficient use of resources.
Pretraining performance achieved by sparse upcycling and dense upcycling from a T5 Base checkpoint.
Dense upcycling (warm starting with depth tiling) shows quick gains over the base dense checkpoint but underperforms the sparse upcycled models, supporting the advantage of sparse upcycling.

Paper

Sparse Upcycling: Training Mixture-of-Experts from Dense Checkpoints 2212.05055

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on August 20, 2026.

Canonical link

Exported from Medium on August 22, 2026.
