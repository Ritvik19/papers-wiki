# Papers Explained 510: OEIS Sequence Benchmark

Papers Explained 510: OEIS Sequence Benchmark

Papers Explained 510: OEIS Sequence Benchmark

This work presents a novel benchmark designed to rigorously evaluate the capabilities of LLMs in mathematical reasoning and algorithmic…

Papers Explained 510: OEIS Sequence Benchmark

This work presents a novel benchmark designed to rigorously evaluate the capabilities of LLMs in mathematical reasoning and algorithmic code synthesis tasks. The benchmark comprises integer sequence generation tasks sourced from the Online Encyclopedia of Integer Sequences (OEIS), testing LLMs’ abilities to accurately and efficiently generate Python code to compute these sequences without using lookup tables. The benchmark provides important insights into the strengths and limitations of state-of-the-art LLMs, particularly emphasizing the necessity for further advancements to reliably solve complex mathematical reasoning tasks algorithmically.

The project is available at GitHub.

Benchmark Design

Dataset Selection
Workflow for curating the OEIS-based benchmark dataset.
The dataset for the benchmark is derived from OEIS, an extensive database of integer sequences contributed by a community of mathematicians around the world. The latest 250 easy and 250 hard sequences based on OEIS labels were selected — around 30 new sequences are added to OEIS every day. The set of sequences is defined as S= Seasy ∪Shard, where Seasy are 250 recent sequences labeled as easy, and Shard are 250 recent sequences labeled as hard in OEIS. An additional 250 easy and 250 hard sequences that are the oldest such sequences in OEIS were also sourced and called the classic sequences. These classic sequences are included because many of them are of significant mathematical interest.

Problem Definition

For each sequence s ∈S, an LLM M is tasked with generating Python code Cs that computes the first N terms of the sequence s, where N is a fixed positive integer (e.g., N = 10). Each integer sequence is a function:

where i0 is an offset indicating where the sequence starts. The code Cs should define a function

such that fs(n) = s(n) for all n ≥i0. For each sequence, the prompt includes only the OEIS Name and Comments fields; sequence values/formulas are withheld for testing.

The following constraints are imposed on the generated code:

the code Cs must not contain a lookup table of the sequence terms
the execution time ts of Cs must satisfy ts ≤T where T is a predefined time limit
the code must be valid Python code executable in a standard environment without external library dependencies.

The models are evaluated using T ∈{0.5, 4} seconds, but these thresholds may need to increase as the models begin to perform better on the benchmark, especially for the hard sequences.

Evaluation Metrics

The performance is measured using three factors: accuracy, efficiency, and avoiding lookup tables. For each sequence s, we define the accuracy As(n) as:

Results

The o3 model performed best with the highest fraction of perfect scores on both easy and hard sequences.
The o3-mini model had the highest average score on hard sequences, though fewer perfect scores compared to o3 and o4-mini.
Reasoning models (o3, o3-mini, o4-mini) from OpenAI scored above 70% accuracy on easy sequences and outperformed non-reasoning models.
Reasoning models benefited more from extra time (4 seconds vs. 0.5 seconds) to execute code.
The latest Gemini models (2.5 flash and pro) performed better than older non-reasoning Gemini models.
Distribution of scores for the top three reasoning and non-reasoning models.
All models used lookup tables more frequently on hard sequences than on easy ones.
Models with the lowest occurrences of cheating were not the strongest performers.
There were regressions in cheating within the same series (e.g., o3 cheated more than o1, and o4-mini cheated more than o3-mini).

Paper

Benchmarking Large Language Models with Integer Sequence Generation Tasks 2411.04372

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on December 26, 2025.

Canonical link

Exported from Medium on May 4, 2026.
