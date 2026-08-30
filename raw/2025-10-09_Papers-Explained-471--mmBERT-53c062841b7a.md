# Papers Explained 471: mmBERT

Papers Explained 471: mmBERT

Papers Explained 471: mmBERT

mmBERT is an encoder-only language model pretrained on 3T tokens of multilingual text in over 1800 languages using an architecture inspired…

Papers Explained 471: mmBERT

mmBERT is an encoder-only language model pretrained on 3T tokens of multilingual text in over 1800 languages using an architecture inspired from ModernBERT. To build mmBERT, several novel elements are introduced, including an inverse mask ratio schedule and an inverse temperature sampling ratio. Over 1700 low-resource languages are added to the data mix only during the decay phase, showing that it boosts performance dramatically and maximizes the gains from the relatively small amount of training data.

Models and data are available at HuggingFace.

Architecture

An identical architecture to ModernBERT is used, but the Gemma 2 tokenizer handles multilingual input. 22 layers and an 1152 intermediate dim are used for both base and small versions (same as ModernBERT-base), but a hidden dimension of 768 for base and 384 for small. The base version has the same number of non-embedding parameters as ModernBERT-base (110M) but a total of 307M parameters due to the larger vocabulary. MMBERT small has 140M total parameters, with 42M non-embedding parameters.
Common Configuration Parameters.
Training Data

Previous work such as XLM-R and mT5 used a very low percentage of English content (5.7% for mT5). However, the highest quality data (filtered DCLM) only exists in English. Thus, a significantly higher percentage of English was used comparative to previous work. Nonetheless, a significant portion of the training data was non-English: for this data was gathered from FineWeb2 and a filtered version of 20 languages from FineWeb2 called FineWeb2-HQ. MegaWika v2 for Multilingual Wikipedia, which covers 60 languages, was also used and filtered. Several other curated corpora in English were included. From Dolma, StarCoder, Stackexchange, Arxiv, and PeS2o were used. From Dolmino, math, filtered Stackexchange, Tulu Flan instruction data, and books were used. From ProLong, their code repositories and their textbooks were used. Thus, the data mix is higher quality than previous work (through the use of filtered DCLM and FineWeb2), more diverse in content (code, instructions, web data, papers), and includes a greater variety of languages and scripts.

Cascading Annealed Language Learning (ALL)
Inverse temperature sampling ratio throughout training from Fineweb2 data, from τ of 0.7 to 0.5 to 0.3.
Unlike previous work which uses a fixed set of languages and a set temperature to sample multilingual data, a novel approach that changes the temperature during training and iteratively adds new languages (i.e. annealing over languages) is used.

Lower-resource languages have smaller amounts of pre-training data and relatively lower quality (since there is less to filter). Thus, learning from these languages in the most impactful way (e.g. avoiding more than 5x epochs of them) while also keeping data quality high is desired. To do this, starting with higher resource languages and slowly adding languages throughout training is done. At each change point, the ratio is re-sampled, taking the distribution from more high-resource biased to more uniform. This allows for avoiding doing many epochs on lower-resource data and allows for quicker learning of new languages as they already have a strong base in the existing language set.

A set of 60 languages (as well as code) that cover a broad range of language families and scripts is started with. This is then increased to 110 languages, covering more “mid-resource” languages (greater than 200 million tokens of data). Finally, all languages/scripts included in FineWeb2 (1833 languages, 1895 language/script variants) are included. The temperature for sampling languages goes from 0.7 to 0.5 to 0.3. Including all the languages at the very end allows for taking advantage of the decay phase learning to rapidly increase performance.

Training Recipe

The same three phase approach as ModernBERT is employed but with a novel inverse masking rate learning schedule. Instead of simply using a lower masking ratio at the end of training, the mask rate is progressively lowered at each stage. For mmBERT small, the weights are also initialized from base using strided sampling.
Training data mixture across the various training stages.
Base Pre-training: This stage encompasses the warmup and stable phase of the trapezoidal learning rate, training for 2.3T tokens. Both learning rate and batch size warmup are used. The data in this stage does not include the filtered FineWeb2 data or the higher quality DCLM. 60 languages (plus code languages) are used in this stage of training and a 30% masking rate to start.
Context Extension / Mid-Training: The quality of the data is increased by switching to the filtered higher-quality versions of the datasets. The RoPE values are changed to handle up to 8192 tokens (i.e. theta of 160k) for global and local layers. The number of languages is further increased to 110 languages (plus code). Training is conducted for 600B tokens and the stable phase is continued, lowering the mask rate to 15%.
Decay Phase: An inverse square root learning rate schedule is used to decay for 100B tokens to 0.02 of the peak LR. Unlike ModernBERT and Ettin, a 5% mask rate is chosen for decay and three different datasets are used to produce three different variants: English-focused (Decay-Eng), 110 languages (same as the mid-training phase, Decay-Cont), and a 1833 language variant (all FineWeb2 languages, Decay-All).
Model Merging: Model merging is used to combine the best qualities from each decay mixture. For the base version, the best checkpoint from each mixture is selected and TIES-merging is used to mitigate parameter interference. Merging across mixtures was ineffective for small models, likely due to less parameter agreement in the smaller weight space. Therefore, an exponential weighting of the Decay-All checkpoints was merged, as that merged mixture performed best.

Evaluation

MMBERT is benchmarked on NLU datasets (GLUE, XTREME), retrieval benchmarks (MTEB v2 for English and multilingual, CoIR for code retrieval), and low-resource language evaluation datasets (TiQuaD for Tigray, FoQA for Faroese).

Comparisons are made against a variety of baselines including XLM-R, mGTE, EuroBERT-210m (base size), mDistilBERT, Multilingual MiniLM (small size), ModernBERT (English upper bound), and the decoder model Gemma 3 270M.
GLUE (English) benchmark results.XTREME benchmark results.
NLU Performance: MMBERT small significantly outperforms other small variants on English GLUE (84.7 average vs MiniLM’s 78.3) and even previous base-sized models. MMBERT base approaches ModernBERT’s English performance (86.3 vs 87.4) despite using mostly non-English data. On multilingual XTREME, MMBERT base outperforms other models on average (72.8 vs XLM-R’s 70.4), showing significant improvements in classification (77.1 XNLI vs 74.6 XLM-R) and question-answering (74.5 F1 on TyDiQA vs 70.5 XLM-R).
MTEB v2 English results.
Retrieval Performance (English): MMBERT models show large gains on English MTEB v2. MMBERT small outperforms mGTE and XLM-R. MMBERT base achieves an average of 53.9, outperforming mGTE (52.7) and performing similarly to ModernBERT (53.8).
MTEB v2 multilingual results.
Retrieval Performance (Multilingual): Both MMBERT models score approximately 1.5 points better on average than their similarly sized counterparts on multilingual MTEB v2 (e.g., 54.1 avg for MMBERT base vs XLM-R’s 52.4).
Retrieval scores on the CoIR Benchmark.
Code Retrieval Performance: MMBERT base (42.2 average) significantly outperforms other massively multilingual models like XLM-R (33.6) on the CoIR benchmark, though it underperforms EuroBERT-210m (45.3) likely due to EuroBERT’s access to a higher-quality, non-public training corpus.
Comparing EuroBERT and MMBERT on EuroBERT’s in-distribution languages on XNLI and PAWS-X.
Comparison with EuroBERT: MMBERT base and small outperform EuroBERT-210m even on EuroBERT’s in-distribution languages for XNLI and PAWS-X (e.g., 74.5 F1 on Arabic XNLI for MMBERT base vs 66.8 F1 for EuroBERT).
Encoder vs. Decoder Models: Encoder-only MMBERT models significantly outperform similar-sized SOTA decoder models (e.g., Gemma 3 270M scored much worse on XNLI and GLUE than even MMBERT small), reinforcing the benefits of encoder-only architectures for these tasks.
Performance of models using different decay phases on two languages (Tigray and Faroese) only added during the decay phase.
Impact of Annealing Language Learning: Including more languages during the decay phase significantly boosts low-resource language performance. MMBERT with the 1833 language decay phase shows rapid performance improvements, with a 68% increase for base on Tigray and a 26% increase for Faroese. MMBERT base even outperforms larger models like Google’s Gemini 2.5 Pro and OpenAI’s o3 on FoQA. Model merging also helps retain performance.
Throughput efficiency for various sequence lengths and variable input length.
Efficiency: MMBERT models are significantly faster and more efficient than previous multilingual encoder-only models. MMBERT base is more than 2x faster on variable sequences and approximately 4x faster on long context lengths. MMBERT small is roughly 2x faster than MMBERT base and other similarly-sized multilingual models. Crucially, MMBERT supports context lengths up to 8192 tokens, whereas previous models like MiniLM and XLM-R are limited to 512 tokens, with MMBERT performing at 8192 tokens as fast as others at 512. This efficiency is attributed to Flash Attention 2 and unpadding techniques.

Paper

mmBERT: A Modern Multilingual Encoder with Annealed Language Learning 2509.06888

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on October 9, 2025.

Canonical link

Exported from Medium on May 4, 2026.
