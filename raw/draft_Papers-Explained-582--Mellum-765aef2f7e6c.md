# Papers Explained 582: Mellum

Papers Explained 582: Mellum

Papers Explained 582: Mellum

Mellum is a family of open-weight, 4B-parameter code completion models designed by JetBrains for interactive use in IDEs, specifically…

Papers Explained 582: Mellum

Mellum is a family of open-weight, 4B-parameter code completion models designed by JetBrains for interactive use in IDEs, specifically optimized for multi-line, in-editor completion with low latency and a compact size. Trained from scratch on 4T tokens of permissively licensed, multi-language code, Mellum incorporates disciplined data governance, multi-stage pretraining and supervised fine-tuning (including fill-in-the-middle and project context), and direct preference optimization.

The models are available at HuggingFace.

Training Pipeline

The goal was to train a model suitable for production grade multi-line code completion, which implies the following constraints:

Low latency for real-time code completion suggestions in the IDE, with 90% of requests served within 500 ms
Reasonable model size, so that Mellum together with data batches fit cost efficient GPUs; and deployment hardware required to provide at least 80 GB of VRAM to host the model and the processed data.
A widely adopted architecture to use optimized training and inference frameworks.

To satisfy these constraints, a scaled-down version of the Llama 2 architecture with 4 billion parameters is used with 24 attention and KV heads, 30 layers, hidden size of 3,072, and MLP hidden size of 8,256.

A custom tokenizer (49,152 tokens) was created based on the dataset that includes both code and natural text data, with a bigger share of code examples. The context size of 8,192 was kept both for pre-training and fine-tuning steps.

Data

The raw data included datasets with code-specific data: The Stack, The Stack v2, StarCoder data, RosettaCode, CommitPack, and CodeNet. For general knowledge and basic natural language understanding, the Wikipedia dataset was also included to allow for a better completion of comments and string literals.

Since these datasets are not fully up to date, this was addressed by collecting additional data with fresh open-source code.

After collecting raw data, file-level filtering by permissive licenses was applied and it was cleaned of personal identifiable information (PII) using the Starcoder-PII model.

Pre-training

The combined dataset was sampled multiple times to reach approximately 4 trillion tokens. Data examples were split into chunks of matching size. For half of the files in each chunk, the fill-in-the-middle transformation was applied. FIM examples were split into three random-sized parts — prefix (P), middle (M), and suffix (S) — that were rearranged into S-P-M order for each particular sample. The order represents the left-to-right prediction of the middle part given the suffix and the prefix as context. The resulting mix of raw and FIM data represents a complete dataset for the pre-training step of the model.

Supervised Fine-tuning

The same raw datasets are used but pre-processed differently: better fill-in-the-middle examples are created and repository-level contextual information was added. This allowed the model to shape generations’ scope to real-world cases and leverage project-level context.

Better FIM

In real-world scenarios, users typically work on semantically complete code segments, such as implementing a function or a loop body, rather than randomly filling parts of files. For code completion tasks, the approach differs from the pre-training step, where code segments (prefix, middle, suffix) are randomly sliced. Instead, more meaningful samples are prepared using Code Engine, an internal command-line tool for code processing, to select appropriate middle segments like function or loop bodies. The method identifies syntactic boundaries (block boundary, line start, line middle, token middle) and probabilistically determines where to start or end the middle segment. The length of these middle chunks is limited to 700 characters to prevent overly long completions.

Project-level Context Collection

Effective code completion requires relevant context from the user’s code base. To bring project-level context into supervised fine-tuning (SFT), Code Engine collects contextual info directly from the project directory. It searches for the most relevant code chunks using various context collection strategies, which were mixed in the SFT dataset to avoid overfitting and allow flexible experimentation during inference, including user-driven and IDE-based strategies.

Strategies for Context Collection:

IoU Strategy: Collects files from the same directory as the current file and selects the closest based on IoUline similarity.
Path Distance Strategy: Ideal for highly modular projects, it identifies relevant code possibly found outside the current directory. Path distance is defined as the minimum directory traversals needed to navigate between files. The implementation uses breadth-first traversal, collecting files in order of increasing path distance.
RAG (Retrieval-Augmented Generation) Strategy: Addresses irrelevance in naive file collection by searching for relevant chunks among files chosen via Path Distance.

Gather candidate files using Path Distance.
Split each file into overlapping line chunks with a sliding window.
Extract a context window around the cursor position.
Score each chunk by IoUBPE similarity versus cursor context.
Select highest-scoring chunks across all files for inclusion in context.

Incorporating Recent Files: In practice, programmers often have several semantically connected files open. During inference, such recent files (opened by the developer in the IDE) are included in the candidate list in step 1. This can’t be accounted for during training, as IDE interactions are unavailable in static datasets. However, during inference, adding recent files expands the relevant chunk search.

Direct Preference Optimization

After the SFT stage, the model adhered closely to the FIM objective and the usage of contexts. However, it still tended to produce verbose, hard-to-read code and occasionally generated syntactically correct yet unhelpful outputs (e.g., NotImplementedError stubs in empty methods). To improve both readability and utility, a dataset was constructed for the direct preference optimization (DPO). Outputs were sampled from the SFT model across multiple model’s temperatures to get diverse examples for the same inputs. Then, an LLM-as-a-Judge was used, leveraging the Tree-sitter parser to segment large FIM instances into shorter, stylistically preferable snippets. During DPO training, the model was trained to directly align with preference labels. As a result of this stage, several models were acquired, like Mellum-4b-dpo-python (Python-specific data only), and Mellum-4b-dpo-all (data for all languages) .

Evaluation
Overall performance of code completion models.
Supervised fine-tuning with project-wide context significantly improves Mellum’s performance across all metrics compared to the base model and even outperforms larger models like Qwen-2.5-Coder-7B, Seed-Coder-8B-Base, and DeepSeek-Coder-5.7B on JetComplete.
Mellum shows modest yet competitive results on SAFIM and RepoBench-C; SFT yields notable improvements on Python-focused HumanEval-Infilling.
Direct Preference Optimization further improves metrics and stopping behavior, bringing generated output closer to ground truth and boosting performance on JetComplete.
Performance on JetComplete.
Multi-lingual SFT delivers larger gains than Python-only fine-tuning, while maintaining strong Python performance. Multi-lingual DPO models further extend advantages to other languages.

Paper

Mellum: Production-Grade in-IDE Contextual Code Completion with Multi-File Project Understanding 2510.05788

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

View original.

Exported from Medium on June 21, 2026.
