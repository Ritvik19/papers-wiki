# Papers Explained 410: Big Math

Papers Explained 410: Big Math

Papers Explained 410: Big Math

Big-Math is a dataset of over 250,000 high-quality math questions with verifiable answers, purposefully made for reinforcement learning…

Papers Explained 410: Big Math

Big-Math is a dataset of over 250,000 high-quality math questions with verifiable answers, purposefully made for reinforcement learning (RL). To create Big-Math, openly available datasets are rigorously filtered, cleaned, and curated, extracting questions that satisfy three requirements:

problems with uniquely verifiable solutions
problems that are open-ended
problems with a closed-form solution.

To ensure the quality of Big-Math, each step in the filtering process is manually verified, and filters are iteratively improved over multiple rounds. Based on the findings from the filtering process, 47,000 new questions with verified answers are introduced, Big-Math-Reformulated: closed-ended questions (i.e. multiple choice questions) that have been reformulated as open-ended questions through a systematic reformulation algorithm.

The dataset is available at HuggingFace.

Dataset Collection

This work selected 3 well-established mathematical problem datasets that are commonly used in recent literature: HARP, Omni-MATH, and NuminaMath.
Comparison of problems by data source.
HARP: 4,780 short answer problems from U.S. national math competitions, specifically the “short answer” subset.

Omni-MATH: Almost 4,500 olympiad-level problems from 39 competition websites, professionally annotated and verified.

NuminaMath: A subset of roughly 860,000 problems from 9 sources, with only 6 retained. The synthetic_math, synthetic_amc, and MATH subsets were excluded due to unevaluated quality and a preference for a different MATH dataset split (12,000 training, 500 test problems as perLet’s verify step by step) instead of the original NuminaMath split. The included subsets are:

cn_k12: ~275,000 problems from Chinese math exams.
Orca-Math: ~150,000 synthetically generated grade school problems, shown to be effective for training even small language models.
olympiads: 150,000 problems from international math competitions.
Art of Problem Solving forum problems: 30,000 problems with high LaTeX content and boxed/filled square symbols.
GSM8k: ~8,000 problems.
amc_aime: 4,000 math competition problems with solutions scraped online.

Dataset Cleaning and Filtering

The dataset collection leads to a combined dataset of over 640,000 problems. To achieve a dataset of the highest quality, the next step is to clean and filter the data from each source using a combination of source-specific and common strategies.

Source-specific Filtering and Cleaning

HARP: Problems containing Asymptote vector graphics language code (identified by “[asy]”) are removed (625 problems, 13% of the dataset).
Omni-MATH: Author attributions (e.g., names in parentheses or “[i] Name [/i]”) are manually removed (45 instances). Text about competition scores (e.g., “If the correct answer is X and your answer is Y”) is removed. Problems lacking solutions (e.g., “The problem provided does not contain a solution…”) are removed (2 problems).
NuminaMath: Problems are deduplicated within each subset using a MinHashLSH filter with 128 hashing functions and a similarity threshold of 0.6 or 0.7. Answers are extracted by searching for boxed solutions (“\boxed{}”). Problems without exactly one boxed answer are filtered out. For the aops_forum subset, unnecessary information like problem attribution, year of submission, and point scoring are removed using regular expressions (2535 problems).

After source-specific filtering, 463,426 problems remain.

Source-agnostic Filtering

After running each of the filters over the individual subsets, 11 filtering operations are performed across the full collection.

Deduplication and Decontamination

The SemDeDup algorithm is used to remove semantic duplicates. To embed the problems, the model at sentence-transformers/all-MiniLM-L6-v2 is utilized, and problems with a cosine similarity over 0.5 are removed. The MATH and Omni-MATH test sets are prime candidates for evaluating a model trained on the dataset, so it is necessary to ensure that the problems in those test sets do not exist in the training set.

Ensuring that problems are solvable

Language Filter: The focus is on English-only models. A FastText language identifier is used to remove any problems where English is not the primary language. Additionally, problems which were very short (< 10 characters) were often classified as non-English (even if they were entirely numbers), so all problems with fewer than 10 non-LaTeX, non-special characters are simply included.
Hyperlink Detection: Problems containing a hyperlink are removed using a simple regular expression, as the existence of hyperlinks suggests that a model may not have the full resources required to solve the problem.
Model Solve Rate: Finally, while it is not feasible to manually ensure the correctness of each problem-answer pair, a heuristic for correctness using language models is developed. For each problem, 64 solutions are generated from Llama-3.1–8B and 5–8 solutions from Llama-3.1–405B. If either model answers the question with the ground truth answer, then the question-answer pair may be valid. This filter is not applied to HARP, Omni-Math, MATH, or GSM8k as these datasets include pre-parsed answers.

Ensuring that problems are open-ended

Regular Expression Filters: For multiple choice questions, a simple regular expression filter is used that searches for either alphabetic options (A, B, C, D) or numerical options (1, 2, 3, 4), occurring in order. To ensure that questions referring to shapes (e.g. “rectangle ABCD…”) or numbers (e.g. 1234) are not incidentally removed, those strings are first removed from the question, prior to the regular expression search. Next, for the True/False questions, a search is conducted for either “true” or “false” in the answer or, when available, in the final line of the solution. Then, for Yes/No questions, the same check as True/False questions is performed, searching in the answer or solution for exact phrases. Additionally, the final line of the question is searched for specific phrases that imply a Yes/No question: “is”, “are”, “do”, “does”, and “can”.
Model-based Filters: For each question type, a model-based filter is designed by iteratively developing a prompt to use with Llama-3.1–70B. The filter is run over the dataset, and 100 problems classified as positive examples (multiple choice) and 100 problems classified as negative examples (open-ended) are inspected. Difficult incorrectly classified problems are iteratively added into the prompt, mostly selecting problems following a previously unseen pattern.

Ensuring that problems are uniquely verifiable

Answer Filter: All examples where the final answer did not previously exist, or could not be extracted from the solution are removed.
Multi-part Question Filter: A large proportion of questions with multiple parts requiring multiple corresponding answers is found. There are surely methods with which to handle partial correctness in multi-part questions, but this is still an open research question requiring further study, so these problems are left for future, more difficult, versions of the dataset. For the regular expressions, the filter searches for commonly found signals: ordered roman numerals (e.g. I, II), multiple numbered parts in parentheses (e.g. (1) … (2)), multiple numbered parts with a period (e.g. 1. … 2.), as well as numbered special characters (e.g. 1 … 2 ). For the model-based filter, an iterative process using a Llama-3.1–70B is used.
Proof Filter: While proofs can be verified, there can be many correct variations, and how to quickly verify proofs written in natural language is unclear at the moment (other than converting to a theorem proving language, which can incur additional parsing errors). Therefore, proofs are removed from the dataset. The regular expression filter simply searches for either of the following phrases in the problem: “prove that” or “a proof”. The model-based filter is implemented through an iterative improvement process with Llama-3.1–70B.

Big-Math-Reformulated
Reformulation strategy.
During the development of filters, a staggering number of multiple choice questions (> 117,000) were found and removed during the filtering process for Big-Math. The inherent structure of multiple choice questions presents a challenge for RL algorithms. Specifically, the multiple-choice format increases the probability of answering correctly regardless of the correctness of a reasoning chain. To address this issue, an approach is proposed to reintroduce these valuable questions by reformulating the multiple choice questions into open-ended questions with a series of carefully devised and detailed steps enacted by large language models. This results in a new subset of 47,000 questions and answers, Big-Math-Reformulated.

Llama-3.1–405B is used for reformulating MCQs into open ended questions. The process involves four steps:

Key Information Extraction, where core information, mathematical concepts, problem details, reformulation strategies, and the expected answer format are identified.
Reformulation, where the multiple-choice question is converted into an open-ended question based on the extracted information.
Judgement where the reformulated question is evaluated to ensure it is open-ended, free from information distortion, has a clear answer format, and can stand alone.
Verification, where the presence of expected information (answer format, rephrasing strategy, etc.) is confirmed.

After these steps, 88,983 questions passed the judgement and verification steps. These questions then undergo post-processing to ensure they are uniquely verifiable, open-ended with closed-form solutions. Llama-3.1–8B and Llama-3.1–405B are used to evaluate the solvability of each reformulated problem, filtering the dataset down to 48,698 problems solved at least once by either model, but not solved 100% by Llama-3.1–8B.

Finally, Big-Math-Reformulated undergoes the same comprehensive filters as the rest of the datasets, resulting in a final set of 47,010 reformulated and filtered problems. This process successfully reintroduces high-quality questions, particularly from the amc_aime subset, where 63.4% of previously identified multiple-choice problems were reintroduced.

Analysis
Distribution of solve rates on each subset of Big Math, calculated with Llama-3.1–8B.
Problems are grouped into quintiles with varying success rates: <20% (hardest) to >80% (easiest).
Distribution of problems across quintiles: 71,926 (28.64%), 30,533 (12.16%), 25,763 (10.26%), 31,249 (12.44%), and 91,647 (36.50%).
The hardest two quintiles contain >120,000 problems, significantly more than other RL-suitable datasets.

Big-Math-Reformulated Subset:

Follows a similar solve rate distribution but is skewed towards more difficult problems.
34.44% in the hardest quintile and 16.42% in the second hardest quintile, totaling over 50% of the subset.
Distribution of solve rates by domain, calculated with Llama-3.1–8B.
Differential equations, discrete mathematics, and abstract algebra are the most difficult domains.
Prealgebra is the easiest domain.
Other domains have a wide distribution of difficulties, indicating varying levels of expertise required.
Linear algebra is easier, while geometry is more difficult, possibly due to domain classification or specific training data.

Paper

Big-Math: A Large-Scale, High-Quality Math Dataset for Reinforcement Learning in Language Models 2502.17387

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on July 16, 2025.

Canonical link

Exported from Medium on May 4, 2026.
