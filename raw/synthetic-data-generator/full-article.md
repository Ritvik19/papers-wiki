Source URL: https://huggingface.co/blog/synthetic-data-generator
Title: Introducing the Synthetic Data Generator - Build Datasets with Natural Language

# Introducing the Synthetic Data Generator - Build Datasets with Natural Language

Published December 16, 2024

David Berenstein, Sara Han Díaz, Leire Aguirre, Daniel Vila, Ame Vi, ben burtenshaw

Introducing the Synthetic Data Generator, a user-friendly application that takes a no-code approach to creating custom datasets with Large Language Models (LLMs). A simple step-by-step process makes dataset creation a non-technical breeze, allowing anyone to create datasets and models in minutes without any code.

Synthetic data is artificially generated information that mimics real-world data. It allows overcoming data limitations by expanding or enhancing datasets.

## From Prompt to Dataset to Model

The synthetic data generator takes a description of the data you want (a custom prompt) and returns a dataset for your use case, using a synthetic data pipeline. This is powered in the background by distilabel and the free Hugging Face text-generation API, but the UI hides that complexity.

### Supported Tasks

The tool currently supports text classification and chat datasets. These tasks determine the type of dataset generated: classification requires categories, while chat data requires a conversation. Based on demand, tasks like evaluation and RAG will be added over time.

**Text Classification**: common for categorizing text like customer reviews, social media posts, or news articles. Generating a classification dataset relies on two LLM-driven steps: first generating diverse texts, then labeling them. Example: `argilla/synthetic-text-classification-news`, classifying synthetic news articles into 8 classes.

**Chat datasets**: used for supervised fine-tuning (SFT), the technique that lets LLMs work with conversational data via a chat interface. Example: `argilla/synthetic-sft-customer-support-single-turn`, an LLM designed to handle customer support (in this example, support for the synthetic data generator itself).

Generation throughput on the free Hugging Face API is roughly 50 samples/minute for text classification and 20/minute for chat; this can be scaled up with a custom account, models, API providers, or generation configurations.

### The Three-Step Process

After logging in (to allow the tool access to the organizations you want to generate datasets for):

1. **Describe Your Dataset**: provide a description including example use cases; describe the goal and assistant type in detail. Hitting "Create" produces a sample dataset.
2. **Configure and Refine**: adjust the generated `system prompt` and task-specific settings, iterating by hitting "Save" and regenerating the sample.
3. **Generate and Push**: fill out dataset name/organization, number of samples, and generation temperature (controls generation creativity), then hit "Generate" for a full run. Output is saved directly to Argilla and the Hugging Face Hub.

### Reviewing the Dataset

Even synthetic data benefits from inspection. The tool integrates directly with Argilla, a collaboration tool for AI engineers and domain experts to build high-quality datasets, enabling semantic search and composable filters for exploring and evaluating the synthetic dataset before exporting the curated version to the Hub.

### Training a Model

Datasets can be turned into models without code using AutoTrain. Using the `argilla/synthetic-text-classification-news` dataset as an example: select the "Text Classification" task, provide the dataset source, choose a project name, and start training (on free Hugging Face CPU hardware for this example). After a couple of minutes, the trained model can be deployed as a live service or used as a `text-classification` pipeline.

## Advanced Features

### Improving Speed and Accuracy

Duplicating the Space (as a private Space) allows configuring environment variables:

1. Use a different free Hugging Face model, changing `MODEL` from the default `meta-llama/Llama-3.1-8B-Instruct` to e.g. `meta-llama/Llama-3.1-70B-Instruct`.
2. Use an OpenAI model by setting `BASE_URL` to `https://api.openai.com/v1/` and `MODEL` to `gpt-4o`.
3. Increase `BATCH_SIZE` from the default `5` to generate more samples per minute (subject to API provider rate limits).
4. Use a private Argilla instance by setting `ARGILLA_URL` and `ARGILLA_API_KEY`.

### Local Deployment

The tool is also open-source under Apache 2.0 and installable via `pip install synthetic-dataset-generator`, with the same environment variables configurable locally.

### Customizing Pipelines

Each synthetic data pipeline is built on distilabel, an open-source framework for synthetic data and AI feedback; pipeline code is shareable and reproducible (e.g. the pipeline behind `argilla/synthetic-text-classification-news` is published in the dataset's Hub repository).

## What's Next

Planned improvements (tracked on GitHub) include Retrieval Augmented Generation (RAG) support and custom evals with LLMs as a judge.

### Community follow-up

Users reported occasional non-sensical generation and Argilla SDK push errors during the tool's active period. As of 2025, the hosted Space returns a 404; the project's author (dvilasuero) noted in the comments that a more powerful, interactive successor project has since been built.
