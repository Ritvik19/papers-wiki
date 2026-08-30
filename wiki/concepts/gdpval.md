# GDPval

**Type**: concept  
**Tags**: #concept

## Overview

**GDPval** is an OpenAI benchmark that measures how well a model performs well-specified knowledge work across 44 occupations, scored by whether a model's output ties or beats work produced by an industry professional on the same task. It is one of OpenAI's primary benchmarks for economically valuable, non-coding work such as spreadsheet modeling, document drafting, and research reports.

## Appearances

- [[GPT-5.2]] — `gpt-5.2-thinking` beats or ties top industry professionals on 70.9% of GDPval comparisons, at more than 11x the speed and under 1% the cost of a human professional.
- [[GPT-5.4]] — reaches 83.0% wins-or-ties, up from 70.9% for GPT-5.2.
- [[GPT-5.5]] — reaches 84.9% wins-or-ties (GPT-5.5 Pro: 82.3%), against GPT-5.4's 83.0%, Claude Opus 4.7's 80.3%, and Gemini 3.1 Pro's 67.3%.
- [[Introducing Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber]] — GDPval-AA v2: Gemini 3.6 Flash 1421 vs 3.5 Flash 1349; 3.5 Flash-Lite 1140 vs 3.1 Flash-Lite 642.

## Notes

- GDPval scores are reported as "wins or ties" against professional baselines rather than a raw accuracy percentage, since many of the underlying tasks (e.g. building a financial model) do not have one objectively correct output.
- The benchmark spans 44 occupations, which is broader than most coding- or math-focused evaluations and is used by OpenAI specifically to argue for progress on general knowledge work rather than narrow technical tasks.

## Related

- [[OpenAI]]
- [[GPT-5.2]]
- [[GPT-5.4]]
- [[GPT-5.5]]
- [[Evaluation and Benchmarks]]
