Source URL: https://huggingface.co/blog/nvidia/nemotron-personas-india
Title: Nemotron-Personas-India: Synthesized Data for Sovereign AI

# Nemotron-Personas-India: Synthesized Data for Sovereign AI

Published October 13, 2025

Kiran Praveen, Utkarsh Vaidya, Evan A, Lipika Ramaswamy, Dhruv Nathawani, Dane Corneil, Yev Meyer (NVIDIA)

NVIDIA releases Nemotron-Personas-India, described as the first open synthetic dataset of Indic personas aligned to India's real-world demographic, geographic, and cultural distributions, licensed CC BY 4.0. It extends NVIDIA's global Sovereign AI persona-dataset collection (following earlier US and Japan persona datasets) and is built with NeMo Data Designer, NVIDIA's enterprise-grade synthetic data generation microservice. The stated motivation: India has over 700 million internet users across a highly multilingual, multi-script environment, but most open datasets reflect Western, English-only norms, leaving a data gap that limits locally-relevant AI development.

## What's in the Dataset

- 21 million personas total (3M records x 7 personas each)
- Multilingual: English and Hindi, in both Devanagari and Latin scripts
- 27 fields per record: persona traits plus contextual attributes grounded in official census/labor statistics (age, gender, education, occupation, state, district, etc.)
- 7.7 billion tokens total, including 2.9B persona tokens: English (1B tokens total, 394M persona tokens), Hindi Devanagari (4.7B tokens total, 1.8B persona tokens), Hindi Latin (2B tokens total, 746M persona tokens)
- ~560k unique full names, reflecting India's linguistic diversity
- 2.9k occupational categories spanning informal, formal, and traditional sectors
- All 36 states of India and 640 districts represented
- Natural-language fields: cultural background, linguistic background, skills/expertise, hobbies/interests
- Persona types: general, professional, linguistic, culinary, sports, arts, travel

The release complements NVIDIA's earlier Hindi evaluation datasets (ChatRAG-Hi, IFEval-Hi, MT-Bench-Hi, GSM8K-Hi, BFCL-Hi), together forming a pipeline from synthetic data generation to model evaluation for Indian AI systems.

## How It Was Built

Produced with NeMo Data Designer, a compound AI system supporting complex Jinja templating, Pydantic validation, structured outputs, automated retries, and multiple generation backends. Two models were used: a Probabilistic Graphical Model (Apache-2.0) for statistical grounding, and GPT-OSS-120B (Apache-2.0) for narrative generation in English, Hindi Devanagari, and Hindi Latin.

Personas were aligned to India's official demographic distributions from the 2011 Census and expanded across: education (India-specific degree pathways), occupations (formal, informal, and traditional sectors like farming, tailoring, street vending), life stages (student, homemaker, retired, unemployed), cultural traits (family structures, regional festivals, marriage traditions), digital-divide usage patterns (urban/rural, age, income), and linguistic diversity (first/second/third spoken languages per persona).

All personas are fully synthetic; no real names are used and none are tied to any living or deceased individual, though statistical grounding draws on 2011 Census data and parsed Indian electoral-roll data. NVIDIA frames this as removing privacy/regulatory barriers to using the dataset for training.

## Why It Matters

The post cites India's National AI Portal estimate of over 7,000 AI startups and research institutions building locally relevant AI systems, alongside Digital India and IndiaAI government programs. It frames the dataset as addressing a gap where AI systems trained on Western-centric data struggle with English-Hindi code-switching, regional occupational categories, and cultural context needed for adoption and trust — and as helping mitigate model collapse (degradation from uncurated training on other models' synthetic outputs) by grounding synthetic generation in real demographic distributions.

An extended version (including first/last names, religion, and synthetic addresses) is available directly through NeMo Data Designer rather than in the public Hugging Face release.

## Usage

```python
from datasets import load_dataset

nemotron_personas_en = load_dataset("nvidia/Nemotron-Personas-India", "en_IN")
nemotron_personas_hi_deva = load_dataset("nvidia/Nemotron-Personas-India", "hi_Deva_IN")
nemotron_personas_hi_latn = load_dataset("nvidia/Nemotron-Personas-India", "hi_Latn_IN")
```

## Key Claims

- Nemotron-Personas-India is described as the first open synthetic dataset of Indic personas aligned to India's real-world demographic, geographic, and cultural distributions (21M personas, 7.7B tokens, CC BY 4.0).
- The dataset spans all 36 states and 640 districts of India, ~2,900 occupational categories, and ~560,000 unique full names.
- Built via NeMo Data Designer using a Probabilistic Graphical Model for statistical grounding plus GPT-OSS-120B for narrative generation across English, Hindi Devanagari, and Hindi Latin script.
- Statistical grounding draws on India's 2011 Census and parsed Indian electoral-roll data, but all persona records are synthetic with no re-identification link to real individuals.
- The release extends NVIDIA's Sovereign AI persona-dataset line (after earlier US and Japan persona datasets) and complements a suite of Hindi evaluation benchmarks (ChatRAG-Hi, IFEval-Hi, MT-Bench-Hi, GSM8K-Hi, BFCL-Hi).

## Figures

No figures were extracted for this ingest, per this batch's no-figure-download policy.

## Entities

- [[NVIDIA]] — publishes the dataset and NeMo Data Designer tooling used to build it.
- [[Hugging Face]] — hosts the dataset and blog post.

## Questions & Gaps

- The post does not report any downstream fine-tuning or evaluation results demonstrating the dataset actually improves Indian-language model performance; the case is made on coverage/methodology grounds rather than measured benchmark gains.
- Demographic grounding relies on the 2011 Census (over a decade old at publication), which the post does not flag as a limitation.

## Related

- [[NVIDIA Releases 6 Million Multi-Lingual Reasoning Dataset]] — another NVIDIA multilingual data release from the same Nemotron ecosystem, translating English post-training data into five languages rather than synthesizing India-specific personas.
- [[Data for Agents]]
