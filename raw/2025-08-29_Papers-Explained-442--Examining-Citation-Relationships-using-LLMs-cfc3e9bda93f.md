# Papers Explained 442: Examining Citation Relationships using LLMs

Papers Explained 442: Examining Citation Relationships using LLMs

Papers Explained 442: Examining Citation Relationships using LLMs

This paper addresses the challenge of ensuring the trustworthiness and interpretability of LLMs when applied to document-based tasks such…

Papers Explained 442: Examining Citation Relationships using LLMs

This paper addresses the challenge of ensuring the trustworthiness and interpretability of LLMs when applied to document-based tasks such as summarization, question answering, and information extraction. The focus is on attribution, which involves tracing the generated outputs back to their source documents to verify the information’s provenance and ensure accuracy and reliability.

The paper proposes and evaluates two techniques: a zero-shot approach framing attribution as textual entailment (using flan-ul2) and an attention-based binary classification technique (using flan-t5-small).

Method and Experimental Setup

The attribution task is defined as a binary classifica- tion problem, where the objective is to determine whether a given claim is attributable to its associated references.

Zero-shot Textual Entailment

This attribution task is framed as a textual entailment problem to ensure simplicity and efficiency. Textual entailment refers to the relationship between two text fragments, typically a premise and a hypothesis, where the goal is to determine whether the premise entails the hypothesis. Formally, given two sentences S1 (premise) and S2 (hypothesis), textual entailment can be defined as a binary relation Entail(S1, S2), where:

Here, S1 entails S2 if the meaning of S1 logically supports or guarantees the truth of S2. The task is to model this relation using techniques, such as deep learning models, to predict this entailment relationship based on a large corpora of annotated text pairs. In this problem formulation, the LLM is tasked with a textual entailment problem.

Attention-based attribution

Experiments are designed using the flan-t5-small model, to analyze attention layers in addressing the attribution task. Attention weights from each layer were utilized as input to a fully connected layer for binary attribution classification. This was done for all 12 layers.

Result and Analysis

The proposed zero-shot method outperforms the baseline in both ID and OOD settings.

In distribution zero shot approach on AttributionBench.

Flan-ul2 performs better with F1 accuracy metrics in Stanford-GenSearch and the LFQA sub-dataset for ID data.

Out ofdistribution zero shot approach on AttributionBench.

Flan-ul2 also performs best for OOD tasks, specifically for the AttrScore-GenSearch and HAGRID sub-datasets.
Using Attention Layers.
Using attention layers on the LFQA attribution subset, F1 scores generally outperform the baseline across nearly all layers, except for layers 4 and 8 to 11.

Paper

Document Attribution: Examining Citation Relationships using Large Language Models 2505.06324

Hungry for more insights?

Don’t miss out on exploring other fascinating threads in this series. Simply click here and uncover the state-of-the-art research!

Do Subscribe for weekly updates!!

By Ritvik Rastogi on August 29, 2025.

Canonical link

Exported from Medium on May 4, 2026.
