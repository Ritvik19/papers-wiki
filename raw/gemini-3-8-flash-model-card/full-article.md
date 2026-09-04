Source URL: https://deepmind.google/models/model-cards/gemini-3-8-flash/
Title: Gemini 3.8 Flash - Model Card

Published: September 2026

# Gemini 3.8 Flash

## Model Information

### Description

Gemini 3.8 Flash is the next iteration in the Gemini 3 model family, building on Gemini 3.7 Flash, delivering performance advancements across software engineering and agentic knowledge workflows. It continues to support customizable effort levels to control the mix of quality, cost and latency.

### Model dependencies

Gemini 3.8 Flash is based on Gemini 3.7 Flash.

### Inputs

Text strings (e.g., a question, a prompt, document(s) to be summarized), images, audio, and video files, with a token context window of up to 1M.

### Outputs

Text, with a 64K token output.

### Architecture

Gemini 3.8 Flash is based on Gemini 3.7 Flash. For more information about the model architecture for Gemini 3.8 Flash, see the Gemini 3.7 Flash model card.

## Distribution

Gemini 3.8 Flash is distributed in the following channels:

* Gemini app
* Gemini Enterprise Agent Platform
* Google AI Studio
* Gemini API
* Google AI Mode
* Google Antigravity

## Evaluation

### Approach

Gemini 3.8 Flash was evaluated across a range of benchmarks, including coding, knowledge work, multimodal capabilities, long-context, computer use, and scientific reasoning. Additional benchmarks and details on approach, results and their methodologies can be found at: deepmind.com/models/evals-methodology/gemini-3-8-flash.

## Intended Usage and Limitations

### Benefit and Intended Usage

Gemini 3.8 Flash is well-suited for users, developers, and enterprises, designed for cost-effective scaling of general-purpose, production-ready agents. Some use cases include: software engineering, agent tasks, and complex knowledge workflows.

### Known Limitations

Gemini 3.8 Flash may exhibit some of the general limitations of foundation models, such as hallucinations. At times, the model might use more tokens to maximize performance, especially at higher effort levels.

The knowledge cutoff date for Gemini 3.8 Flash is March 2026 – users can expect updated information for some domains while in others they may experience the model's knowledge is limited to January 2025 (in line with the Gemini 3 Model Family).

## Ethics and Content Safety

Overall, Gemini 3.8 Flash performs similarly to Gemini 3.7 Flash across both safety and tone, with low unjustified refusals. Safety performance across non-English languages regressed slightly relative to 3.7 Flash.

| Evaluation | Description | Gemini 3.8 Flash vs. Gemini 3.7 Flash |
| --- | --- | --- |
| Text to Text Safety | Automated content safety evaluation measuring safety policies | **-0.4pp** Lower is better |
| Multilingual Safety | Automated safety policy evaluation across multiple languages | +5.4pp Lower is better |
| Image to Text Safety | Automated content safety evaluation measuring safety policies | 0.0pp Lower is better |
| Tone | Automated evaluation measuring objective tone of model responses | **+0.2pp** Higher is better |
| Unjustified-refusals | Automated evaluation measuring model's ability to respond to borderline prompts while remaining safe | +1.1pp Lower is better |

Gemini 3.8 Flash is part of the Gemini 3 series of models. Assessments have shown that Gemini 3.8 Flash does not have meaningful new capabilities or material increases in performance with respect to the domains outlined in the Frontier Safety Framework compared to Gemini 3.7 Flash.
