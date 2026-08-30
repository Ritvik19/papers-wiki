# Papers Explained 07: ALBERT

Papers Explained 07: ALBERT

Papers Explained 07: ALBERT

ALBERT presents certain parameter reduction techniques to lower memory consumption and increase the training speed of BERT

Papers Explained 07: ALBERT

ALBERT presents certain parameter reduction techniques to lower memory consumption and increase the training speed of BERT

Model Architecture Choice

The backbone of the ALBERT architecture is similar to BERT in that it uses a transformer encoder with GELU nonlinearities. ALBERT uses the feed-forward/filter size as 4H and the number of attention heads as H/64. where H is the hidden size in BERT.

Similar to BERT, all the experiments with ALBERT use a vocabulary size V of 30,000.

Factorized Embedding Parameterization

In BERT, as well as subsequent modeling improvements the WordPiece embedding size E is tied with the hidden layer size H, i.e., E ≡ H. This decision appears suboptimal:

From a modeling perspective, WordPiece embeddings are meant to learn context-independent representations, whereas hidden-layer embeddings are meant to learn context-dependent representations. untying the WordPiece embedding size E from the hidden layer size H allows us to make a more efficient usage of the total model parameters as informed by modeling needs, which dictate that H >> E.

From a practical perspective, natural language processing usually require the vocabulary size V to be large. If E ≡ H, then increasing H increases the size of the embedding matrix, which has size V ×E. This can easily result in a model with billions of parameters, most of which are only updated sparsely during training.

Therefore, for ALBERT, a factorization of the embedding parameters is used, decomposing them into two smaller matrices. Instead of projecting the one-hot vectors directly into the hidden space of size H, we first project them into a lower dimensional embedding space of size E, and then project it to the hidden space. By using this decomposition, we reduce the embedding parameters from O(V × H) to O(V × E + E × H). This parameter reduction is significant when H >> E.

Cross-Layer Parameter Sharing

ALBERT proposes cross-layer parameter sharing as another way to improve parameter efficiency. There are multiple ways to share parameters, e.g., only sharing feed-forward network (FFN) parameters across layers, or only sharing attention parameters. The default decision for ALBERT is to share all parameters across layers.

Inter-Sentence Coherence Loss

In addition to the masked language modeling (MLM) loss, BERT uses an additional loss called next-sentence prediction (NSP). Subsequent studies found NSP’s impact unreliable and decided to eliminate it, a decision supported by an improvement in downstream task performance across several tasks.

ALBERT conjecture that the main reason behind NSP’s ineffectiveness is its lack of difficulty as a task.

That is, for ALBERT, sentence-order prediction (SOP) loss is used. The SOP loss uses as positive examples the same technique as BERT (two consecutive segments from the same document), and as negative examples the same two consecutive segments but with their order swapped. This forces the model to learn finer-grained distinctions about discourse-level coherence properties.

Model Setup

ALBERT-large has about 18x fewer parameters compared to BERT-large, 18M versus 334M.

An ALBERT-xlarge configuration with H = 2048 has only 60M parameters.

ALBERT-xxlarge configuration with H = 4096 has 233M parameters, i.e., around 70% of BERTlarge’s parameters

To keep the comparison as meaningful as possible, we follow the BERT setup in using the BOOKCORPUS and English Wikipedia for pretraining baseline models.

Results

Paper

ALBERT: A Lite BERT for Self-supervised Learning of Language Representations 1909.11942

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on February 6, 2023.

Canonical link

Exported from Medium on May 4, 2026.
