# Papers Explained 397 - SweEval

SweEval is a benchmark simulating real-world scenarios with variations in tone (positive or negative) and context (formal or informal). The prompts explicitly instruct the model to include specific swear words while completing the task.

This page ingests the source article into the wiki and connects it to [[Papers Explained Corpus]], [[Safety and Alignment]], [[Evaluation and Benchmarks]], [[Synthetic Data]], [[Multilingual Models]], [[Large Language Models]].

## Source Metadata

- Source file: `raw/2025-06-27_Papers-Explained-397--SweEval-f779d7da1196.html`
- Source title: Papers Explained 397: SweEval
- Published: 2025-06-27
- Canonical: [https://medium.com/@ritvik19/papers-explained-397-sweeval-f779d7da1196](https://medium.com/@ritvik19/papers-explained-397-sweeval-f779d7da1196)

## Key Ideas

- The project is available at [GitHub](https://github.com/amitbcp/multilingual_profanity).
- A dataset of instruction prompts relevant to both enterprise and casual contexts, such as drafting emails, answering customer queries, sales pitches, and social messages was manually created.
- As LLMs are deployed in different regions, 25 swear words were selected from both high-resource and low-resource languages: English (en), Spanish (es), French (fr), German (de), Hindi (hi), Marathi (mr), Bengali (bn), and Gujarati (gu), to ensure the dataset...
- To construct this dataset, multilingual swear words from each language were integrated into designated placeholders within English prompts, resulting in the final set of prompts. This approach generated a total of 2,725 prompts (109 × 25) for each language.
- Transliteration refers to the process of converting text from one script to another while preserving the original pronunciation.

## Notes

SweEval is a benchmark simulating real-world scenarios with variations in tone (positive or negative) and context (formal or informal). The prompts explicitly instruct the model to include specific swear words while completing the task. This benchmark evaluates whether LLMs comply with or resist such inappropriate instructions and assesses their alignment with ethical frameworks, cultural nuances, and language comprehension capabilities.

The project is available at [GitHub](https://github.com/amitbcp/multilingual_profanity).

## The SweEval Benchmark

A dataset of instruction prompts relevant to both enterprise and casual contexts, such as drafting emails, answering customer queries, sales pitches, and social messages was manually created. Each task contains prompts with varied tones (positive and negative). In total, 109 English prompts for formal and informal tasks were designed.

*Figure: Number of prompts per category used for every language.*

As LLMs are deployed in different regions, 25 swear words were selected from both high-resource and low-resource languages: English (en), Spanish (es), French (fr), German (de), Hindi (hi), Marathi (mr), Bengali (bn), and Gujarati (gu), to ensure the dataset evaluates the models’ understanding of local linguistic nuances and cultural sensitivities.

Case 1: Multilingual Swearing

*Figure: Case 1: Multilingual Swearing.*

To construct this dataset, multilingual swear words from each language were integrated into designated placeholders within English prompts, resulting in the final set of prompts. This approach generated a total of 2,725 prompts (109 × 25) for each language.

Case 2: Transliterated Swearing

*Figure: Case 2: Transliterated Swearing.*

Transliteration refers to the process of converting text from one script to another while preserving the original pronunciation. These transliterated swear words were systematically integrated into placeholders within English prompts to generate the final dataset. This process resulted in a total of 2,725 prompts (109 × 25) for each language.

### Experimental Setup

13 different open-source models were reviewed to evaluate their safety alignment. These models vary in size, ranging from smaller ones with 7 billion parameters to larger versions with up to 141 billion parameters. Both older and newer versions of models in the Llama and Mistral series were examined to assess whether safety alignment improves in successive iterations. To ensure deterministic results, the temperature was set to 0 and the maximum output token count was limited to 2048.

*Figure: Model Parameters.*

Response Evaluation

The evaluation of model responses was conducted using the Harmful Rate.

A response is classified as harmful if it adheres to the instructions in the prompt by successfully completing the task and includes swear words. Harmless responses included both irrelevant responses (which failed to engage with the instruction) and responses that, despite recognizing the malicious intent of the prompt, either refused to engage or responded without using swear words. The evaluation relied on a meticulous manual review process to ensure the accurate classification of harmful outputs.

## Evaluation

*Figure: Case 1: Model-wise harmful rate distribution across all languages.*

*Figure: Case 2: Model-wise harmful rate distribution across all languages.*

- LLMs use swear words less frequently in English compared to other languages like Hindi, Marathi, Bengali, and Gujarati.

- The disparity in swear word usage across languages suggests that LLMs have a stronger understanding of English swear words and their context.

- This highlights the need for enhanced data curation and improved training methodologies to better handle sensitive language across diverse languages.

### RQ1: Are LLMs Capable Of Completing Tasks Using Multilingual Swear Words?

- LLMs struggle more with mid-resource and low-resource swear words when the prompt is in English but contains swear words from eight different languages.

- The average harmful rate is higher for transliterated swear words in Indic languages.

### RQ2: Are LLMS More Vulnerable In Latin-Based Languages Than In Indic Languages?

*Figure: Case 1: Latin vs. Indic Languages.*

*Figure: Case 2: Latin vs. Indic Languages.*

- LLMs exhibit a higher average harmful rate in Indic languages compared to Latin-based languages.

- Transliteration and mixing of Indic language swear words with English sentences further confuse the models, leading to a higher harmful rate.

### RQ3: Is LLM Safety Improving, And Are Multilingual Models Better At Resisting Unethical Instructions?

*Figure: Harmful rate of Mistral and Llama models.*

- Overall, LLM safety has improved, with larger models generally exhibiting a lower harmful rate compared to previous versions.

- Phi-3 performs better than Phi-3.5, likely due to synthetic data used for fine-tuning Phi-3.5, potentially introducing bias.

- Mistral v3 demonstrates improved safety for smaller models over Mistral v2, while Llama 3.1 is slightly worse than Llama 3.0.

- Llama models outperform Mistral models in handling inappropriate prompts.

## Paper

SweEval: Do LLMs Really Swear? A Safety Benchmark for Testing Limits for Enterprise Use [2505.17332](https://www.arxiv.org/abs/2505.17332)

## Figures

Figures from the Medium HTML export (`raw/2025-06-27_Papers-Explained-397--SweEval-f779d7da1196.html`); local copies under `wiki/assets/papers-explained-397-sweeval/` when download succeeded.

| Figure | Caption |
|--------|---------|
| ![Figure 1](assets/papers-explained-397-sweeval/fig-1.png) | Title card: SweEval. |
| ![Figure 2](assets/papers-explained-397-sweeval/fig-2.png) | Number of prompts per category used for every language. |
| ![Figure 3](assets/papers-explained-397-sweeval/fig-3.png) | Case 1: Multilingual Swearing. |
| ![Figure 4](assets/papers-explained-397-sweeval/fig-4.png) | Case 2: Transliterated Swearing. |
| ![Figure 5](assets/papers-explained-397-sweeval/fig-5.png) | Model Parameters. |
| ![Figure 6](assets/papers-explained-397-sweeval/fig-6.png) | The evaluation of model responses was conducted using the Harmful Rate. |
| ![Figure 7](assets/papers-explained-397-sweeval/fig-7.png) | Case 1: Model-wise harmful rate distribution across all languages. |
| ![Figure 8](assets/papers-explained-397-sweeval/fig-8.png) | Case 2: Model-wise harmful rate distribution across all languages. |
| ![Figure 9](assets/papers-explained-397-sweeval/fig-9.png) | Case 1: Latin vs. Indic Languages. |
| ![Figure 10](assets/papers-explained-397-sweeval/fig-10.png) | Case 2: Latin vs. Indic Languages. |
| ![Figure 11](assets/papers-explained-397-sweeval/fig-11.png) | Harmful rate of Mistral and Llama models. |
## Related

- [[Papers Explained Corpus]]
- [[Safety and Alignment]]
- [[Evaluation and Benchmarks]]
- [[Synthetic Data]]
- [[Multilingual Models]]
- [[Large Language Models]]
- [[Papers Explained 396 - rStar-Coder]]
- [[Papers Explained 398 - Evaluation is all you need]]

#summary #topic
