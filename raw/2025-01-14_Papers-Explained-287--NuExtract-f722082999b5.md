# Papers Explained 287: NuExtract

Papers Explained 287: NuExtract

Papers Explained 287: NuExtract

NuExtract is a lightweight text-to-JSON LLM, that allows extraction of arbitrarily complex information from text and turns it into…

Papers Explained 287: NuExtract

NuExtract is a lightweight text-to-JSON LLM, that allows extraction of arbitrarily complex information from text and turns it into structured data. This model can be directly used in a zero-shot setting or fine-tuned to solve a specific extraction problem.

The models are available on HuggingFace.

Structured Extraction

The goal of Structured Extraction is to extract all kinds of information from a document — entities, quantities, dates, and so on — and to identify their (potentially hierarchical) relationships. The extracted information is then structured in the form of a tree, which usually follows a template (a.k.a. schema) so that it can easily be parsed to fill up a database or directly used to take automatic actions.
Structured Extraction Example
NuExtract
NuExtract creation procedure.
Template/Schema Representation

The schema is represented by an empty JSON. Each array is filled with an element template, and empty strings indicate the extracted fields. Only strings are output and other JSON types are ignored as there is not much interest in supporting them (a number can always be returned as a string). This template format is used because of its simplicity.

This template format does not allow for the inclusion of field descriptions because examples are believed to be more informative than descriptions.

Dataset Creation

300k pieces of English text from the C4 dataset, a large and diverse general-domain dataset, are used. The idea is that something interesting to extract will be found in most texts. To annotate this text, an LLM is first prompted to generate a template from each piece of text.
!!!START Context!!!*<text-to-annotate>*!!!END Context!!!Goal: Generate an information extraction dataset.Input: Text document + instructions for annotation.Output: 1 JSON object (schema).Schema:Describes the information to be extracted.Each field should:Be a clear and concise name representing the extracted data.ONLY STRING TYPE ARE ALLOWED AS VALUES (it can be an array of strings, or an object with string values, or an array of objects with string values…).NO BOOLEAN, INT, ENUM, ETC.The schema can focus only on part of the context document, or on the whole document.Constraints:Extracted information should be thematically coherent and form a well-structured JSON schema with a clear relationship between fields.*<few-shot examples>*
Once templates are available, an LLM can be used to extract information according to each template. For half of the examples, information is extracted from the full text. For the other half, part of the text is removed (but the original template is kept). Removing part of the text creates empty fields in the output, and will teach the model that it is acceptable to return an empty string when the information is not present. This form of negative sampling is a way to fight hallucinations.
!!!START Context!!!*<text-to-annotate>*!!!END Context!!!Goal: Extract strings from the text corresponding to the given schema.Input: Text document + schema.Output: 1 JSON objectSchema:The schema describes the information to be extracted.ONLY STRING TYPE ARE ALLOWED AS VALUES (it can be an array of strings, or an object with string values, or an array of objects with string values…).NO BOOLEAN, INT, ENUM, ETC.The schema can focus only on part of the context document, or on the whole document.Output:THE OUTPUT SHOULD FOLLOW EXACTLY THE SCHEMA.It should respect the schema and contain the extracted information from the context document.THE STRING SHOULD BE PRESENT EXACTLY AS IT IS IN THE CONTEXT DOCUMENT. NO PARAPHRASING ALLOWED.If the information is NOT PRESENT in the context, return “” for empty string and [] for empty array. If the list of object is empty, return [].Return only the information extracted as JSON. Do not output anything else or says anything else.Information to extract:*<schema>*
This prompt is used with Llama 3 70B to annotate 300k pieces of text. Examples for which the template is not followed, as well as examples for which extracted values are not found in the text, are filtered out. This results in 50k annotated examples.

Base Models

An encoder-decoder architecture is likely the best choice for this task. However, these models have not been trained as exten

sively as recent generative LLMs. As a result, pure decoder LLMs are used. Phi-3-mini (3.8B parameters) is used for NuExtract, Phi-3-small (7B parameters) for NuExtract-large, and Qwen1.5–0.5B (0.5B parameters) for NuExtract-tiny. These base models are fine-tuned on the dataset.

Evaluation

To assess the performance of NuExtract models in structured extraction tasks, a benchmark is created by selecting “problems” like parsing resumes, creating templates for each problem, finding raw text and manually extracting information.

Additionally, metrics are developed to evaluate the performance of NuExtract models. A tree matching method is used to align extracted values, with similarity computation between corresponding values using exact matching. The average leaf similarities are then used to obtain a measure between 0 (completely different) and 1 (perfect match).
Comparison of NuExtract models with popular generic LLMs in the zero-shot setting.
NuExtract-tiny outperforms GPT-3.5 while being at least 100 times smaller.
NuExtract outperforms Llama3–70B while being 35 times smaller.
NuExtract-large reaches GPT-4o levels while being at least 100 times smaller.
Comparison of NuExtract models with popular generic LLMs of the chemical extraction problem.
Fine-tuning NuExtract models on the chemistry problem significantly improves performance.
NuExtract-tiny, despite having only 0.5B parameters, surpasses GPT-4o after fine-tuning.
NuExtract and NuExtract-large achieve exceptional performance after fine-tuning.
Fine-tuning small language models for structured extraction problems yields substantial benefits.

NuExtract 1.5

NuExtract 1.5 is the new version of our foundation model for structured extraction. It is multilingual, can handle arbitrarily long documents, and outperforms GPT-4o in English while being 500 times smaller.

The models are available at HuggingFace.

Dataset Creation

For the training dataset, raw documents are taken from the C4 dataset. Fifty percent of English documents and fifty percent of documents from other languages (mainly French, German, Spanish, Italian, and Portuguese) are chosen. To enable NuExtract to handle long documents properly, longer documents are included than in the original NuExtract.

An English template is used for half the documents, regardless of their language, while the same language as the document is used for the other half. This allows users to create a unique template in English when processing documents in multiple languages. The same automatic annotating procedure as in the original NuExtract is then used.

Infinite Context

To solve the memory issue for long sequences, NuExtract is trained to be able to extract information from a document while being given previous information. To give this ability to NuExtract 1.5, new examples are added to the dataset for which previous information is given, such as:
Example of continuation extraction.
With such examples, the model should learn to merge previous and new information. This merging is not trivial; sometimes there is conflicting information. In this case, the temperature value is overwritten as the new information is more relevant.

This “continuation” ability allows processing of arbitrarily long documents by iteratively re-injecting the current state of information while processing text via a sliding context window — reminiscent of recurrent neural networks.

Training

Phi-3.5 mini (3.8B) is trained on the dataset to obtain NuExtract 1.5. A 0.5B model is also attempted to be trained on this dataset, but it proves too small to be multilingual and have continuation abilities. As a result, Qwen 2.5 0.5B is trained only on English documents and without continuation examples.

Evaluation

English Performance
Zero-shot results on the structured extraction benchmark.
Zero-Shot Results: NuExtract 1.5 significantly outperforms the original NuExtract and slightly surpasses GPT-4o in zero-shot performance.
Many-shot results on the structured extraction benchmark.
Few-Shot Results: With few-shot learning (fine-tuning for NuExtract, in-context learning for GPT-4o), all models improve substantially. GPT-4o slightly outperforms NuExtract 1.5. NuExtract 1.5 significantly outperforms NuExtract 1.5 tiny, suggesting a larger NuExtract model could outperform GPT-4o.

Multilingual Performance
Multilingual zero-shot results on the structured extraction benchmark.
NuExtract 1.5 shows significant improvement over the original NuExtract but is outperformed by GPT-4o. Model size is suspected to be a key factor in multilingual performance.

Long Documents Performance
Performance on long documents (between 8k and 10k tokens).
8k-10k token documents: NuExtract 1.5 outperforms GPT-4o on documents in the 8k-10k token range. This suggests NuExtract 1.5 handles long contexts effectively. NuExtract 1.5 significantly outperforms NuExtract 1.5 tiny.
Performance on even longer documents (between 10k and 20k tokens).
10k-20k token documents: Using a 10k token sliding window, NuExtract 1.5 continues to outperform GPT-4o, confirming its strong performance on long documents and the effectiveness of the continuation strategy.
Performance of NuExtract on long documents (8k-10k tokens) as function of the size of the extraction window.
Extraction Window Size Impact: NuExtract 1.5’s performance degrades gracefully as the extraction window size decreases. A 2k token window is required for GPT-4o to outperform NuExtract 1.5. Smaller windows reduce memory usage significantly. While the continuation procedure isn’t perfect, it allows processing of documents exceeding GPU memory capacity.

NuExtract 2

NuExtract 2.0 is an update over NuExtract 1.5. This version introduces vision (processing images), abstraction (classification, reformulation, formatting, etc.), and in-context learning (customization via examples in the prompt).

The models are available at HuggingFace.

3 open-source versions of NuExtract 2.0 are released:

NuExtract 2.0 2B (Qwen 2.0 VL 2B base, MIT license)
NuExtract 2.0 4B (Qwen 2.5 VL 3B base, research license)
NuExtract 2.0 8B (Qwen 2.5 VL 7B base, MIT license)

All have a 32k token context.
Creation procedure of NuExtract 2.0.
It uses Vision Language Models to extract information directly from images without OCR, avoiding formatting loss (for instance, tables and diagrams are preserved).

Prior versions (1.0 and 1.5) could only copy-paste text (pure extraction). NuExtract 2.0 supports:

Reformatting outputs (e.g., standardize dates, country codes, numbers).
Deducing answers (e.g., infer country from capital city).
Classification (e.g., job mode: remote/on-site/hybrid).
Text Generation (e.g., translation, summarization).
Templates now specify desired types: “verbatim-string” for literal extraction, “string” for free generation, as well as “choice” (enumerations), “date”, “number”, and “null” for missing information.
Template field types.Template constructors.Example of a NuExtract 2.0 template and a compatible extraction output.
In-Context Learning
Minimalist training example to teach NuExtract to perform in-context learning.
If a template cannot specify everything, you can add examples to the prompt (“few shot” learning).
NuExtract 2.0 was trained with examples-in-prompt for both text and images, making it adaptable by simply showing “shots” of what’s needed.

Performance

Even three examples can boost performance significantly.

NuExtract 2.0 8B reaches 73 F-Score, a bit better than non-reasoning frontier models.

NuExtract 2.0 PRO largely outperforms frontier models, with a +9 F-Score margin over GPT-4.1.
NuExtract 2.0 PRO is also ahead of frontier reasoning models: +5 F-Score over reasoning Claude 4 Opus, +2 F-Score over Gemini 2.5 PRO.

NuExtract 3

NuExtract3 unifies structured extraction (documents to JSON) and content extraction (OCR) into a single model. It is trained via Reinforcement Learning to develop extraction-specific reasoning abilities, which can be switched on and off on demand.

The model is available at HuggingFace.
Structured extraction task.Content extraction task (a.k.a. OCR).
NuExtract 3 is trained on a diverse and challenging dataset, combining real-world documents (from the Fine-PDF dataset) and synthetically generated complex documents. It is trained in two phases: SFT followed by RL.
Training procedure for NuExtract3.
NuExtract3 introduces 14 new field types:

Performance

An in-house structured extraction benchmark, which includes about 600 challenging extractions across 15 different problems is used to compare the models:

NuExtract3 outperforms generalist models substantially

150 complex documents (mostly weird tables) are used to compare extracted markdowns between NuExtract3 and models of similar size, both generalist and specialized:

NuExtract3 largely outperforms generalist models at content extraction.

The inhouse structured extraction benchmark is repurposed to measure OCR capabilities:

NuExtract outperforms both generalist and specialist models

Paper

NuExtract: A Foundation Model for Structured Extraction

NuExtract 1.5 — Multilingual, Infinite context, still small, and better than GPT-4o!

NuExtract 2.0: Outclassing Frontier LLMs in Information Extraction

NuExtract3: The Reasoning Open-Source OCR & Structured Extraction LLM

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on January 14, 2025.

Canonical link

Exported from Medium on June 13, 2026.
