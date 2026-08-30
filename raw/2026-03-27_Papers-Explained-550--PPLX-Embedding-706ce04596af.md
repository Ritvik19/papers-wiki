# Papers Explained 550: PPLX Embedding

Papers Explained 550: PPLX Embedding

Papers Explained 550: PPLX Embedding

pplx-embed is a family of multilingual embedding models that employ multi-stage contrastive learning on a diffusion-pretrained language…

Papers Explained 550: PPLX Embedding

pplx-embed is a family of multilingual embedding models that employ multi-stage contrastive learning on a diffusion-pretrained language model backbone for web-scale retrieval. By leveraging bidirectional attention through diffusion-based pretraining, the models capture comprehensive bidirectional context within passages, enabling the use of mean pooling and a late chunking strategy to better preserve global context across long documents. Two model types are released: pplx-embed-v1 for standard retrieval, and pplx-embed-context-v1 for contextualized embeddings that incorporate global document context into passage representations.

PPLX Embedding
Training pipeline of pplx-embed-v1 and pplx-embed-context-v1.
Continued Diffusion Pretraining

Two bidirectional diffusion language models are trained via continued pretraining of existing autoregressive decoder-only backbones. Considering the state-of-the-art performance of the Qwen3 family, Qwen3–0.6B4 and 4B5 are chosen as base models. Causal attention masking is disabled and the resulting transformer encoders are trained to reverse a corrupting noise process.

A continuous-time formulation and an absorbing state process are adopted in which, at timestep 𝑡 ∈[0,1], each token has decayed to the absorbing [MASK] state independently with probability 𝑡. The [MASK] state is represented by repurposing a rarely used token from the Qwen3 vocabulary. The left-shift operation applied during autoregressive pretraining is preserved.

During training, 𝑡∼𝒰(0.001,1) is sampled for each input sequence independently and each token in the input sequence is masked with probability 𝑡. Models are trained via the standard evidence lower bound, which is given by the sum of token-wise cross entropies at masked positions, scaled by 1/𝑡.

Half of the training data consists of English educational web pages from FineWeb-Edu, while the other half covers 29 other languages with data sourced from FineWeb2 and FineWeb2-HQ. Models are trained for 60,000 steps with a global batch size of 1024 and a sequence length of 4096. This results in pretraining on approximately 250 billion tokens of multilingual text data. One percent of the training sequences are truncated to a randomly chosen length to ensure models are exposed to varying sequence lengths.

Pooling and Quantization

To produce embeddings, token-level representations extracted from the backbone model are pooled into a sequence-level representation. While recent embedding models based on decoder-only transformers typically employ last-token pooling, the bidirectional architecture allows the application of mean pooling. A pooling method that natively combines mean pooling with quantization is proposed. Given token-wise embeddings (v𝑙) for a sequence of length 𝐿, the sequence-level embedding is defined as:

The resulting vector has integer entries in {−127,…,127}, which are representable as signed 8-bit integers. The quantization above is employed not only during inference, but also during all contrastive training stages. Straight-through gradient estimation is used to backpropagate through the non-differentiable rounding operation. The quantized embeddings are compared via their cosine similarity.

Binary quantization is also supported, which reduces the size of output embeddings by setting each entry of the mean-pooled embedding vector to−1 or 1:

While an embedding model could be trained using binary quantization with straight-through gradient estimation, training-free post-hoc binarization can be applied with minimal performance loss.

Pair Training

Pair training represents the first contrastive learning stage, establishing foundational semantic alignment between queries and documents. An InfoNCE contrastive loss is employed, which contrasts queries simultaneously against in-batch documents and other in-batch queries. Given a set of 𝑁 query-document pairs, corresponding embedding vectors q𝑖 and d𝑖 are obtained from an encoder for 𝑖= 1,…,𝑁. For a temperature 𝜏 >0, the loss is defined as:

with 𝑚𝑖(x) = 1{𝑠(q𝑖,x)≤𝑠(q𝑖,d𝑖)+0.1} masking some terms, and 𝑠(q𝑖,d𝑖) = q𝑖·d𝑖 / ‖q𝑖‖2‖d𝑖‖2 being the cosine similarity.

The masking function 𝑚 is designed to mitigate the effects of false negative samples. It compares the similarity of each in-batch negative to the query against that of the positive pair. When a negative sample’s similarity exceeds that of the positive pair by more than 0.1, indicating potential semantic relevance, and thus a likely false negative, the function masks its contribution, thereby preventing distortion of the learned representation space.

Pair training is conducted in three steps to gradually incorporate non-English data: first, the model is trained only on English, then on English and cross-lingual data, and finally on the entire pair dataset containing multilingual samples.

Contextual Training

Contextual training is an approach for training embedding models on long documents divided into chunks such that the embedding of each chunk retains contextual information from the whole document. Given 𝑁 query-document pairs where each document contains 𝐶 chunks, 𝑑𝑖 we compute embedding vectors c𝑖𝑘 ∈R𝑑 for chunk 𝑘 from document 𝑖. A dual-objective loss function is used to capture local chunk-level semantics as well as global document-level representations. The local loss is defined as a combination of the in-batch and in-sequence losses for chunks. For the in-sequence contrastive loss, the target (gold) chunk from a document is treated as the positive sample, and all remaining chunks from the same document are used as negatives. In contrast, for the in-batch loss, the gold chunk remains the positive sample, but the negatives are defined as all other chunks in the batch, including those from the same document. The sequence loss is defined as:

with c𝑖*representing the embedding of the gold chunk. Furthermore, the in-batch loss is:

The final local loss is then calculated by:

In experiments, 𝛼= 0.2 is set. For the global loss, an InfoNCE objective is employed to model query-document similarities. However, multiple queries within a batch may correspond to the same document, which would erroneously treat duplicate documents as negatives and introduce false negatives during training. To mitigate this, duplicate documents in the batch are identified and masked by comparing their hashes. Similar to the pair loss, similarity threshold masking and query-query negatives are applied. Combining these with duplicate document masking, the global loss is defined as:

For the total loss, pplx-embed-context-v1 combines local and global losses with a scheduled weight 𝛽. A cosine schedule starting at 𝛽 = 0.2 with a final target value of 0.5 is used.

Triplet Training

Triplet training extends traditional pairwise contrastive learning by incorporating explicit hard negative examples alongside positive documents, enabling models to learn more discriminative embeddings through fine-grained relevance distinctions. Given a set of 𝑁 query-document triplets, embeddings d corresponding to the hard negatives of the query q are computed. The triplet contrastive InfoNCE loss is then formulated as:

Datasets for Contrastive Learning

For contrastive training, English, multilingual, and synthetic datasets are employed. The final set contains 65.6% English, 6.7% cross-lingual, 1% code, and 26.7% multilingual samples from 60 different languages. Contextual training is performed on the ConTEB training data, as well as data synthesized from the MLDR training set. Triplet training uses considerably less but higher-quality data, spanning 12 datasets. Of this data, 92% is English, 1% is code, and 7% consists of multilingual text covering 15 different languages. All synthetic training data are generated using LLM-based synthesis with the Qwen3–30B-A3B-Instruct-2507 model. The synthesis pipeline employs a two-stage persona-based approach to create diverse query-document pairs from web-scale corpora based on the top-5 relevant personas. For contextual training, a similar pipeline is utilized that generates synthetic queries for passages in a given document.

Evaluations

MTEB Multilingual

pplx-embed-v1–4B outperforms gemini-embedding-001 and is close to Qwen3-Embedding-4B in average score, while being substantially more storage-efficient.
pplx-embed-v1–0.6B outperforms Qwen3-Embedding-0.6B.

MTEB Code

pplx-embed-v1–4B slightly underperforms Qwen3-Embedding-4B but outperforms text-embedding-3-large and gemini-embedding-001 on code retrieval.
pplx-embed-v1–0.6B outperforms Qwen3-Embedding-0.6B on code tasks.
nDCG@10 on the MIRACLRetrievalHardNegatives task per language.
MIRACL benchmark

Use MIRACL (subset of MTEB Multilingual) to analyze language-specific retrieval performance across 18 languages and scripts, reporting nDCG@10 per language.
pplx-embed-v1–0.6B (INT8) outperforms Qwen3-Embedding-0.6B on all language subsets; its binarized variant also beats Qwen3-Embedding-0.6B on average.
The 0.6B model achieves a higher average score than the 4B model on MIRACL.
On average, all pplx-embed-v1 models outperform text-embedding-3-large but trail Qwen3-Embedding-4B and gemini-embedding-001.
Comparison of performance on ConTEB.
ConTEB (non-contextual models)

Among non-contextual models, pplx-embed-v1–4B (INT8/BIN) and pplx-embed-v1–0.6B (INT8/BIN) outperform Qwen3-Embedding-0.6B and Qwen3-Embedding-4B on average nDCG@10.

ConTEB (contextual models)

pplx-embed-context-v1–4B achieves the best overall performance among contextual models.
pplx-embed-context-v1–0.6B ranks third, outperforming ModernBERT-Large and Anthropic Contextual but trailing voyage-context-3.
Match metric on the BERGEN benchmark with Qwen/Qwen2.5–32B-Instruct as a generator.
BERGEN benchmark (RAG pipeline)

pplx-embed-v1–4B (INT8) achieves the best results on 3/5 tasks and outperforms Qwen3-Embedding-4B on 4/5 tasks.
pplx-embed-v1–0.6B outperforms Qwen3-Embedding-4B on 3/5 tasks, showing strong performance despite smaller size.
Results on ToolRet benchmark.
ToolRet benchmark (tool search)

pplx-embed-v1–4B achieves an average nDCG@10 of 44.45%, ranking second overall and showing particularly strong Web performance (42.07% nDCG@10).
pplx-embed-v1–0.6B achieves 43.05% average nDCG@10, remaining competitive with larger full-precision baselines despite INT8 quantization.
Semantic retrieval with these models reduces context explosion by selecting relevant tools from large API corpora.

Diffusion vs. Autoregressive Pretraining

Starting from pretrained base models, a small number of contrastive pair training steps are performed and the performance of the resulting embedding models is evaluated. Four configurations derived from two base models and two pooling strategies are evaluated. The causally masked Qwen3 base model (denoted as Qwen3) is compared against a bidirectional backbone pretrained with a diffusion objective (denoted as Diffusion). For each backbone, either mean pooling or last-token pooling is applied. The Qwen3 base model remains causally masked during contrastive training, while the diffusion base model uses bidirectional attention throughout training. Pair training is performed on English data for less than one epoch.

[ FIG 2 ]

Configurations using the bidirectional diffusion backbone achieve substantially lower training loss than those initialized with the causally masked Qwen3 model.

[ TAB 9 ]

Across English retrieval tasks (e.g., CQADupstackGaming, DBpedia, FEVER, HotpotQA, MSMARCO, SCIDOCS, SciFact), diffusion-pretrained models generally outperform Qwen3-based models.
The combination of diffusion pretraining and mean pooling yields the best overall performance, with an average improvement of ~1 percentage point over other configurations.
Mean pooling not only modestly improves benchmark performance but is crucial for contextual embedding training, because it allows computing many chunk-level representations from a single document efficiently.

Paper

Diffusion-Pretrained Dense and Contextual Embeddings 2602.11151

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on March 27, 2026.

Canonical link

Exported from Medium on May 4, 2026.
