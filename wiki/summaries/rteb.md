# Introducing RTEB: A New Standard for Retrieval Evaluation

**Source**: `raw/rteb/full-article.html` (298 KB), `raw/rteb/full-article.md`
**Ingested**: 2026-07-10
**Tags**: #summary

## Summary

RTEB (Retrieval Embedding Benchmark) is a new beta benchmark from MongoDB and the MTEB team, launched as part of the MTEB leaderboard's Retrieval section, aimed squarely at the "teaching to the test" problem in embedding evaluation. Public retrieval benchmarks are repeatedly reused as evaluation targets, and models that train on data overlapping those benchmarks can post inflated zero-shot-looking scores without actually generalizing. RTEB's fix is structural rather than curatorial: every dataset is either fully open (public corpus, queries, and labels, reproducible by anyone) or fully private (held by MTEB maintainers only, who commit to never training on it and only reporting scores through the public leaderboard). A model that scores well on the open half but drops sharply on the private half is flagged as likely overfit to public benchmarks rather than genuinely capable at retrieval.

The benchmark is also explicitly enterprise-shaped rather than academic-shaped: it groups datasets by domain (law, healthcare, finance, code) and language (20 languages spanning English, Japanese, German, French, and lower-resource languages like Bengali and Finnish) rather than by a rigid task taxonomy, and it deliberately avoids repurposing generic QA datasets when better-fitting retrieval-native datasets exist (though the authors note about half of current datasets are still repurposed from QA, an acknowledged limitation). NDCG@10 is the default leaderboard metric.

The open half currently spans 17 datasets (AILA case docs/statutes, LegalQuAD, FinanceBench, HumanEval, MBPP, MIRACL hard negatives, and others); the closed half currently spans 12 private datasets across German/Japanese/French legal, English/German finance, code, and healthcare. Both halves are expected to grow, and the authors explicitly invite dataset submissions through the MTEB GitHub repo.

## Key Claims

- Existing public retrieval benchmarks suffer a "generalization gap": models can score highly on a benchmark by training on data that overlaps its evaluation set, without generalizing to genuinely unseen data. RTEB directly measures this with a paired open/private dataset design.
- Roughly 50% of RTEB's current retrieval datasets are repurposed from QA datasets, an acknowledged limitation that can bias results toward lexical-overlap-friendly models rather than pure semantic retrieval.
- Coverage requirements per dataset: at least 1,000 documents and 50 queries, to stay meaningful without being prohibitively expensive to evaluate.
- Current scope is text-only retrieval; multimodal (text-image) retrieval is planned but not yet included.
- Private datasets are evaluated only by MTEB maintainers, who commit to not training models on them, to preserve a genuinely unbiased generalization signal for the whole community.

## Figures

No figures were extracted for this ingest; the source article's performance-discrepancy chart (public vs. closed dataset scores) is referenced inline in the summary above but not downloaded, per this batch's no-figure-download policy. The open/closed dataset listing is preserved as markdown tables in the source article.

## Entities

- [[Hugging Face]] — hosts the blog and the MTEB Leaderboard Space referenced in the post.
- MongoDB (Frank Liu, Zoltán Fődi) — co-authoring organization; no dedicated entity page created, tracked here and via [[Embedding and Retrieval]].
- Massive Text Embedding Benchmark (MTEB) team (Kenneth Enevoldsen, Roman Solomatin, Isaac Chung, Tom Aarsen) — maintains the underlying leaderboard infrastructure RTEB extends.

## Questions & Gaps

- No academic paper accompanies the RTEB launch yet; a community member asks about this in the comments and the authors do not confirm a timeline.
- It's unclear how RTEB's private-dataset scores will be kept current as new model releases occur without re-running the full private suite each time.
- The post does not report which models currently show the largest open-vs-private generalization gap, beyond noting that the phenomenon is "already apparent with some models."

## Related

- [[Introducing the Ettin Reranker Family]] — reranker release that references RTEB's motivating framing (open vs private evaluation) as relevant context for generalization claims.
- [[Embedding and Retrieval]] — topic page for retrieval/benchmark coverage.
- [[Evaluation and Benchmarks]] — topic page for benchmark-methodology coverage generally.
- [[Hugging Face]]
