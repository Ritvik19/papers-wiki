# Introducing the Synthetic Data Generator - Build Datasets with Natural Language

**Source**: `raw/synthetic-data-generator/full-article.md`, `raw/synthetic-data-generator/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

A Hugging Face / Argilla post introducing the Synthetic Data Generator, a no-code Space that turns a natural-language description of a dataset into a generated, reviewable, and trainable dataset. Underneath the UI, generation is powered by `distilabel` (an open-source LLM pipeline framework) calling the free Hugging Face text-generation API; the tool hides this pipeline behind a three-step flow: describe the dataset in a prompt, refine the auto-generated system prompt and task settings against a live sample, then generate the full dataset and push it directly to both Argilla (for review) and the Hugging Face Hub.

At launch, the tool supports two task types with different generation pipelines: text classification (a two-stage LLM pipeline that first generates diverse texts, then labels them into categories) and chat/SFT data (single-turn conversational examples for supervised fine-tuning). Default throughput on the free API is roughly 50 samples/minute for classification and 20/minute for chat. Generated datasets integrate directly with Argilla for semantic search and filter-based review before being curated and pushed to the Hub, and can be turned into a deployed model with no code via AutoTrain (demonstrated end-to-end on a synthetic news-classification dataset, trained on free CPU hardware in a few minutes).

Advanced usage lets users duplicate the Space privately to swap in a larger free model, point at an OpenAI-compatible endpoint (e.g. `gpt-4o` via `BASE_URL`/`MODEL` env vars), raise the generation `BATCH_SIZE`, or point at a private Argilla instance. The tool is also open-sourced (Apache 2.0, `pip install synthetic-dataset-generator`) for fully local/self-hosted use, and every generated pipeline is itself reproducible and publishable alongside its output dataset. As of this ingest, the originally hosted Space returns a 404; a comment from the project's author indicates a more capable, interactive successor project has since superseded it, though RAG support and LLM-judge custom evals, both flagged as "what's next" in the original post, do not appear to have shipped in this exact tool.

## Key Claims

- Three-step no-code flow: describe dataset → configure/refine system prompt and settings against a sample → generate full dataset and push to Argilla + Hugging Face Hub.
- Built on `distilabel` pipelines calling the free Hugging Face text-generation API by default; each generated pipeline's code is itself shareable/reproducible via the output dataset's Hub repo.
- Two supported task types at launch: text classification (two-stage generate-then-label pipeline) and chat/SFT datasets (single-turn conversational examples); default throughput ~50 samples/min (classification) and ~20 samples/min (chat) on the free API.
- Generated datasets can be trained into a deployed model with zero code via AutoTrain, demonstrated on a synthetic news-classification example trained on free CPU hardware.
- Advanced/self-hosted configuration supports swapping in larger HF models, OpenAI-compatible endpoints, custom batch sizes, and private Argilla instances; the tool is open-sourced under Apache 2.0 as `synthetic-dataset-generator`.
- Planned RAG support and LLM-as-judge custom evals were tracked as future work at launch; as of this ingest the originally hosted Space is defunct (404), with the author noting a more capable successor project has since been built.

## Figures

No figures were extracted for this ingest, per this batch's no-figure-download policy.

## Entities

- [[Hugging Face]] — hosts the Space, provides the free text-generation API backing default generation, and co-publishes the post.

## Questions & Gaps

- The post does not name the successor project referenced in a later community comment, so it's unclear whether functionality was folded into an existing HF tool or spun out separately.
- No accuracy/quality benchmark is given for the generated synthetic datasets themselves (e.g. how classifier accuracy trained on synthetic vs. real data compares).

## Related

- [[Open-Source DeepResearch - Freeing Our Search Agents]] — another Hugging Face team tool-release post from the same era of the blog, similarly wrapping an underlying pipeline (agentic search vs. `distilabel` generation) behind a simple UI.
