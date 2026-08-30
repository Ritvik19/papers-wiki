# Papers Explained 509: FACTS Leaderboard

Papers Explained 509: FACTS Leaderboard

Papers Explained 509: FACTS Leaderboard

Papers Explained 509: FACTS Leaderboard

The FACTS Leaderboard is an online leaderboard suite and associated set of benchmarks that comprehensively evaluates the ability of language models to generate factually accurate text across diverse scenarios. The suite provides a holistic measure of factuality by aggregating the performance of models on four distinct sub-leaderboards.

FACTS Multimodal, which measures the factuality of responses to image-based questions
FACTS Parametric, which assesses models’ world knowledge by answering closed-book factoid questions from internal parameters
FACTS Search, which evaluates factuality in information-seeking scenarios, where the model must use a search API
FACTS Grounding (v2), which evaluates whether long-form responses are grounded in provided documents, featuring significantly improved judge models.

Each sub-leaderboard employs automated judge models to score model responses, and the final suite score is an average of the four components, designed to provide a robust and balanced assessment of a model’s overall factuality.

To mitigate overfitting, only a subset of the prompts will be released publicly, and the remaining prompts will remain private. All model evaluation will be conducted by Kaggle.
Main results on the FACTS benchmark suite.
FACTS Multimodal

The FACTS Multimodal benchmark evaluates the ability of models to generate factually accurate text in response to image-based questions.

The evaluation set contains approximately 1,500 questions, divided and filtered into a 711-item public set and an 811-item private set. Questions were curated from various sources to reflect diverse real-world user queries and were filtered to focus on objective, information-seeking tasks. The benchmark covers a range of capabilities, including detailed visual description, data interpretation from charts and graphs, object recognition, and logical reasoning about visual scenes.
Distributions of image and question categories in the FACTS Multimodal benchmark.
For each question, human annotators created a detailed rubric listing relevant facts. Facts that are critical for a complete and satisfactory answer are labeled as Essential, while other relevant, contextual facts are labeled as Non-Essential. An automated judge, acting as a meticulous fact-checker, is used to verify the model’s response is factual using two boolean verdicts:

Coverage verdict: The model response includes the essential facts specified in the ground-truth rubric.
No-Contradiction verdict: The model response does not include any claims that contradict either the ground-truth rubrics (essential and non-essential), common knowledge or the input image itself.
Detailed results on the FACTS Multimodal benchmark.
The Gemini model family is more recall-oriented than other families, demonstrating high Coverage scores.
Conversely, GPT models are more precision-oriented, achieving the highest No-Contradiction Scores.

FACTS Parametric

The FACTS Parametric benchmark assesses the ability of models to accurately answer factual questions that users care about, without the aid of external tools. FACTS Parametric consists of 2104 QA pairs, equally divided into a 1052-item public set and a 1052-item private set. The queries span a broad range of topics, including politics, sports, and technology, while the answer types fall into diverse categories such as people, dates, and places.
Distributions of context domain and of answer type as a percent of the total set of questions in the FACTS Parametric benchmark.
Questions were collected that reflect interest shown by many users. Since strictly following these guidelines tends to yield highly popular (and therefore easier) topics, the least frequent topics from the eligible set were deliberately selected. The list of initial questions was further refined using adversarial sampling to ensure that only questions that remain challenging for models were retained. A key criterion for FACTS Parametric was established: every answer must be explicitly supported by information found within Wikipedia documents. This constraint helped ensure that the benchmark evaluates knowledge the model was likely exposed to during training, thereby allowing a clearer assessment of its ability to recall factual information learned during that phase, especially when running the assessment with no access to web-search tools.

FACTS was designed parametrically with a few important properties in mind:

Single, Atomic Fact: Each question targets exactly one piece of factual information, avoiding multi-part queries. This ensures that evaluation focuses on recalling one easily verifiable fact.
Unambiguous Answer: Questions are designed to have only one distinct, correct answer, minimizing ambiguity during evaluation.
Clear Answer Specification: The expected type of answer (e.g., person, location, date) or the required granularity is typically stated in the question itself, or is strongly implied.
Concise, Factual Answers: The expected answer is a short entity (like a name, a number, or a specific term) rather than a simple “yes/no” response (which the model can ’guess’) or a long detailed response. This simplifies matching model outputs to the ground truth.
Stable Facts: The benchmark focuses on facts that are either static or explicitly time-anchored within the question, ensuring the stability and longevity of the ground truth answers.

A multi-stage filtering pipeline was implemented. First, automatic LLM-based filters were applied to the initial set of questions, collected to reflect user interest, to identify queries satisfying the factoid criteria. Next, an adversarial sampling mechanism was utilized to isolate the most challenging examples. Finally, human verification was conducted to confirm adherence to all specified properties.
Detailed results on the FACTS Parametric benchmark.
Although GPT-o3 achieves higher raw accuracy (57.0% vs. 55.7%), GPT-5 hedges significantly more often (13.3% of cases vs. 1.9%).
Consequently, GPT-5 achieves superior attempted accuracy (64.3% vs. 58.2%) and F1 scores (59.7 vs. 57.6).

FACTS Search

The FACTS Search benchmark evaluates the ability of models to use web search. The evaluation set contains 1884 questions, which are split into public and private test sets, of sizes 890 and 994 respectively. The set of questions consists of four subsets, each generated using a different strategy. One subset was written by human raters, and the other three were synthetically generated.

Hard Tail: Raters were instructed to write questions that require information that is challenging to extract with web search. Specifically, there is no single-step web search answer available on the first page, or the information is not readily available as a verbatim piece of text on the internet. Raters were also asked to verify that the Gemini 1.5 model could not solve these, even when using search.

Wiki Two-Hop: An initial set of QA pairs was extracted from Wikipedia abstracts, and filtered to focus on tail entities. Next, each question was modified to be a harder, multi-step question via synthetic alteration. This was achieved by substituting the main entity of the question with a different description of this entity that is extracted from the Google Knowledge Graph.

WikiMulti-Doc: First, a seed document 𝐷𝑠𝑒𝑒𝑑 was sampled. Then, it was used to sample a set of similar documents 𝐷𝑟𝑒𝑙𝑎𝑡𝑒𝑑, and only the documents 𝐷𝑡𝑜𝑟𝑠𝑜 with rank that is neither too low nor too high are kept. Finally, Gemini was prompted to synthesize a query-answer pair (𝑄,𝐴) from the content of these 𝑛documents. The query 𝑄 was formulated to be answerable only by synthesizing information present in both the seed document 𝐷𝑠𝑒𝑒𝑑 and one or more documents from the 𝐷𝑡𝑜𝑟𝑠𝑜 subset. The prompt also encouraged Gemini to find interesting ways to connect information rather than relying on a simple direct chain or a combination of unrelated queries.

Next, questions were filtered as follows. First, an automated critic model filtered out pairs where the question was not self-contained or the answer was not strictly grounded in the source documents. Second, a hardness filter was applied, discarding any queries that Gemini could correctly answer when utilizing standard web search tools.

KG Hops: First, common path-queries, such as “films that actor X appeared in”, were collected. These queries were then concatenated and combined with other functions (e.g., max) to create more complex ones. For example, “films that actor X appeared in” and “publication date of film X” could be combined to create “publication date of the first film that actor X appeared in”.

The final dataset sizes are 328, 932, 268, 356 for Hard Tail,Wiki Two-Hop,Wiki Multi-Doc, and KG Hops respectively.

The FACTS leaderboard evaluation uses the Brave Search API as the search tool. Given a query, a model response, and a gold response, Gemini 2.0 Flash is prompted to assess if the response is correct, incorrect or does not attempt to answer the query.
Detailed results on the FACTS Search benchmark.
Gemini 3 Pro, the highest-performing model, conducts fewer searches on average than other top models,
The Grok model family searches the most.

FACTS Grounding (v2)

The FACTS Grounding v2 benchmark evaluates whether a model response is consistent with the given context document and user query about that document. The set of prompts for FACTS Grounding v2 is the same as v1. Third-party human raters were instructed to design prompts requiring the processing of long-form input and the writing of long-form output. These tasks include Q&A, summarization, and document rewriting. Each example within the evaluation set consists of a context, which is a document or set of reviews sourced from the web, paired with a non-trivial user request that can be addressed using the provided context, necessitating a long-form response.
Distributions of context domain and of task requested by the user as a percent of the total set of prompts in the benchmark.
The evaluation approach is the same as in FACTS Grounding v1. First, multiple “judge” LLMs determine if the response is grounded in the input. Ineligible responses that do not sufficiently address the user request are found and marked as inaccurate. Only grounded and eligible responses are labeled as accurate. The main updates in FACTS Grounding v2 are the LLMs used as judges, and the prompt used.

Unadjusted Factuality Score: A language model judge is utilized to produce a binary classification label identifying whether a full model response is grounded in the user request and the context document given an instruction. Two different judge models are used in order to reduce the bias of a particular judge model. The judge models are Gemini 2.5 Flash and GPT-5. FACTS Grounding v1 used a different set of models: Gemini 1.5 Pro, GPT-4o, and Claude 3.5 Sonnet.

Disqualifying Ineligible Responses: Metrics that are focused on evaluating the factuality of the generated text with respect to a context document can be “hacked” by ignoring user intent. This is safeguarded against by using prompted judge LLMs to determine whether a given generated response sufficiently addresses the user’s request. The judge LLM is asked to output a binary label indicating the eligibility of the response: either “eligible,” signifying that it answers the user request, or “ineligible,” otherwise. Ineligible responses are disqualified from factuality evaluation and the final factuality score is adjusted such that ineligible responses are deemed as inaccurate.

Paper

The FACTS Leaderboard: A Comprehensive Benchmark for Large Language Model Factuality 2512.10791

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on December 25, 2025.

Canonical link

Exported from Medium on May 4, 2026.
