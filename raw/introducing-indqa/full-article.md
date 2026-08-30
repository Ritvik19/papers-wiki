---
Source URL: https://openai.com/index/introducing-indqa/
Fetched via: WebFetch (curl returns 403 on openai.com/index/*)
Date: November 3, 2025
---

# Introducing IndQA

A new benchmark for evaluating AI systems on Indian culture and languages.

About 80% of people worldwide do not speak English as their primary language, yet most existing multilingual benchmarks fall short: benchmarks like MMMLU are now saturated (top models cluster near high scores), and most focus on translation or multiple-choice tasks rather than context, culture, and history.

**IndQA** evaluates how well AI models understand and reason about questions that matter in Indian languages, across a wide range of cultural domains. India was chosen as a starting point given about a billion people who don't use English as their primary language, 22 official languages (at least seven with 50M+ speakers), and being ChatGPT's second-largest market.

## How it works

IndQA spans 2,278 questions across 12 languages and 10 cultural domains, created with 261 domain experts across India. Domains: Architecture & Design, Arts & Culture, Everyday Life, Food & Cuisine, History, Law & Ethics, Literature & Linguistics, Media & Entertainment, Religion & Spirituality, Sports & Recreation. Languages: Bengali, English, Hindi, Hinglish, Kannada, Marathi, Odia, Telugu, Gujarati, Malayalam, Punjabi, Tamil (Hinglish added given the prevalence of code-switching).

Each datapoint has a culturally grounded prompt in an Indian language, an English translation for auditability, expert-written rubric criteria, and an ideal answer. Grading is rubric-based: a model-based grader checks whether each weighted criterion is met, and the score is the sum of points for satisfied criteria out of the total possible.

## How it was built

1. **Expert-authored questions**: native-level speaking domain experts across 10 domains drafted difficult, reasoning-focused prompts tied to their regions and specialties.
2. **Adversarial filtering**: each question was tested against GPT‑4o, OpenAI o3, GPT‑4.5, and (partially, post-launch) GPT‑5; only questions where a majority of these models failed to produce acceptable answers were kept, to preserve headroom for progress.
3. **Detailed criteria**: domain experts provided grading criteria (similar to an essay rubric).
4. **Ideal answers + review**: experts added ideal answers and English translations, with peer review and iterative fixes until sign-off.

## Caveats

Because questions are not identical across languages, IndQA is not a language leaderboard; cross-language scores should not be interpreted as direct language-ability comparisons. It is intended to measure improvement over time within a model family/configuration. Because questions were adversarially filtered against GPT‑4o, o3, GPT‑4.5, and GPT‑5, this could confound relative GPT‑5 performance and potentially disadvantage OpenAI models compared to non-OpenAI models.

## Contributors

261 Indian experts (journalists, linguists, scholars, artists, industry practitioners) authored and reviewed questions, including a Nandi Award-winning Telugu actor/screenwriter, a Marathi journalist/editor, a Kannada linguistics scholar and dictionary editor, an International Chess Grandmaster, a Tamil writer/poet/cultural activist, an award-winning Punjabi music composer, a Gujarati heritage curator, an award-winning Malayalam poet, a Bengal cultural-heritage historian, and an Odishan-temple architecture professor.

## Next steps

OpenAI hopes IndQA inspires similar benchmarks for other languages/cultural domains poorly covered by existing AI benchmarks, to help research labs learn what models struggle with and provide a north star for future improvement.
