# IndQA

**Source**: `raw/introducing-indqa/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

IndQA is a benchmark OpenAI introduced November 3, 2025 for evaluating how well AI models understand and reason about questions grounded in Indian languages and culture. OpenAI frames it as a response to a gap in existing multilingual evaluation: benchmarks like MMMLU have become saturated, with top models clustering near the top of the scale, and most multilingual benchmarks lean on translation or multiple-choice tasks rather than testing context, culture, and history. India was chosen as the starting point given roughly a billion people who do not use English as a primary language, 22 official languages (at least seven with more than 50 million speakers each), and its position as ChatGPT's second-largest market.

The benchmark spans 2,278 questions across 12 languages (Bengali, English, Hindi, Hinglish, Kannada, Marathi, Odia, Telugu, Gujarati, Malayalam, Punjabi, and Tamil) and 10 cultural domains: architecture and design, arts and culture, everyday life, food and cuisine, history, law and ethics, literature and linguistics, media and entertainment, religion and spirituality, and sports and recreation. Hinglish was included specifically to capture code-switching between Hindi and English, which is common in everyday use. Each question was written by one of 261 domain experts across India and includes a culturally grounded prompt in an Indian language, an English translation for auditability, expert-written rubric criteria, and an ideal answer; a model-based grader checks each weighted criterion against a model's response and sums the points for criteria that are satisfied.

Building the dataset had four stages. Native-level domain experts across the 10 categories first drafted difficult, reasoning-focused questions tied to their own regions and specialties. Each question then went through adversarial filtering: it was tested against GPT-4o, OpenAI o3, GPT-4.5, and, after launch, partially against GPT-5, and only kept if a majority of these models failed to answer it acceptably, which preserves room for future models to show improvement. Experts then wrote detailed grading criteria similar to an essay rubric, and finally added ideal answers and English translations, with peer review and iterative fixes before sign-off. The 261 contributors included journalists, linguists, scholars, artists, and industry practitioners, among them a Nandi Award-winning Telugu actor and screenwriter, a Marathi journalist and editor, a Kannada linguistics scholar, an International Chess Grandmaster, and a Tamil writer and cultural activist.

OpenAI states that IndQA is not a language leaderboard: because questions differ across languages, cross-language score comparisons should not be read as claims about relative language ability, and the benchmark is meant to track improvement within a model family or configuration over time rather than rank languages against each other. The adversarial filtering against GPT-4o, o3, GPT-4.5, and GPT-5 could also confound GPT-5's own relative performance and may put OpenAI's models at a disadvantage compared with non-OpenAI models on the resulting question set. OpenAI says it hopes IndQA prompts similar benchmarks for other languages and cultural domains that existing benchmarks cover poorly.

## Key Claims

- Introduced November 3, 2025; 2,278 questions across 12 languages and 10 cultural domains.
- Languages: Bengali, English, Hindi, Hinglish, Kannada, Marathi, Odia, Telugu, Gujarati, Malayalam, Punjabi, Tamil.
- Built with 261 domain experts across India; questions are adversarially filtered against GPT-4o, OpenAI o3, GPT-4.5, and (partially) GPT-5, keeping only those a majority of these models failed to answer acceptably.
- Each item has a rubric-based grading scheme: expert-written weighted criteria, an ideal answer, and an English translation for auditability.
- Explicitly not designed as a cross-language leaderboard; intended to track improvement within a model family over time.
- OpenAI acknowledges the adversarial-filtering process could disadvantage its own models in relative comparisons against non-OpenAI models.

## Figures

No article figures extracted; openai.com blocks direct HTML download so figures could not be downloaded, and WebFetch markdown does not preserve chart images.

## Entities

- [[OpenAI]]: publisher of IndQA.

## Questions & Gaps

- The article does not report actual model scores or a leaderboard for IndQA, only the methodology behind it.
- No detail is given on how the model-based grader itself is validated against human judgment.

## Related

- [[OpenAI]]
- [[Evaluation and Benchmarks]]
- [[Multilingual Models]]
