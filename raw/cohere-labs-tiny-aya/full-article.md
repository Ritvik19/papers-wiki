Source URL: https://cohere.com/blog/cohere-labs-tiny-aya
Title: Cohere Labs Launches Tiny Aya, Making Multilingual AI Accessible
Published: Feb 17, 2026

---

# Cohere Labs Launches Tiny Aya, Making Multilingual AI Accessible

Today, Cohere Labs, Cohere’s research arm, is introducing **Tiny Aya**, the most capable multilingual open-weight model at its scale. Tiny Aya delivers state-of-the-art translation quality, strong multilingual understanding, top-quality target language responses, and broad language coverage in a model small enough to run locally, even on consumer hardware and mobile phones. No barriers to experimentation, just a powerful family of models that can run anywhere. 

Multilingual AI has made rapid progress, but performance and usability still concentrate around a small set of dominant languages and large-scale infrastructure. Tiny Aya takes a different approach: combining efficient design with deep multilingual research to support balanced performance across languages while remaining practical to deploy and adapt. Instead of shallow coverage across hundreds of languages, Tiny Aya emphasizes meaningful multilingual depth enabling researchers, developers, and communities to build AI that reflects their own linguistic and cultural contexts.

 **What We're Releasing**

**TinyAya-Base, a pretrained 3.35B-parameter model:** TinyAya-Base covers 70+ languages*, including many lower-resourced languages from around the globe.

**TinyAya-Global, a powerful instruction-tuned multilingual model: **Built on top of TinyAya-Base, TinyAya-Global delivers strong, balanced performance across 67 supported languages. It serves as the default truly multilingual system, ideal for applications that require consistent quality across diverse linguistic settings in a single deployment.

**A family of specialized instruction-tuned models**: Alongside TinyAya-Global, we’re introducing specialized variants that deepen performance within specific linguistic regions while maintaining strong multilingual capability more broadly. This structure combines shared cross-lingual learning with targeted regional depth giving researchers and builders flexibility in how they deploy multilingual AI (details of the model variants and regional specializations are described below).

**A new massively multilingual fine-tuning dataset and benchmarks:** Covering multiple domains, languages, and tasks, these resources provide a foundation for systematic multilingual experimentation, enabling reproducible evaluation and continued exploration of data-centric training strategies.

**A detailed technical report****:** Sharing the research, training strategy, and evaluation insights behind Tiny Aya.

The instruction-tuned models from the Tiny Aya family perform competitively with existing massively multilingual models at this scale. Aggregating benchmark performance on our focus languages across multiple tasks (translation, language understanding, mathematical reasoning, and open-ended generations on both technical and non-technical domains), we find that Tiny Aya is advancing the state-of-the-art in generative multilingual AI at this scale across all languages from West Asia and Africa.Tiny Aya represents a shift in how we think about how multilingual systems are built and shared. With efficient design, deep research into multilingual pretraining and post-training, and a focus on linguistic diversity from the ground up, Tiny Aya brings high-quality AI closer to the people who need it most: researchers working on underrepresented languages, developers building locally, and communities shaping technology on their own terms. For example, a university lab in India could deploy Tiny Aya as an offline translation or AI education tool in classrooms and community settings without relying on cloud APIs.  

 

The dominance of languages on the web, here measured by page counts in CommonCrawl, typically steers the performance across languages in multilingual LLMs. Tiny Aya maintains stable performance even for languages that are under-represented on the web (the right end of this graph), and advances their inclusion in multilingual AI.**Technical Innovation**

Tiny Aya is grounded in several years of research from the Aya initiative on how multilingual models can scale responsibly. In particular, the training approach builds on our recent research around increasing language plasticity through tokenization, increasing naturalization of synthetic data, smart fusion of diverse generations and targeted selection of merging methods. Together, these methods allow multilingual signals to be combined while preserving linguistic nuance and strengthening language-specific structure. 

Another core design principle behind Tiny Aya was efficiency under realistic compute budgets. By completing post-training on a single 64 NVIDIA H100 GPU cluster, we demonstrate that careful multilingual data design and training strategy can substitute for brute-force scaling. These ideas shaped Tiny Aya from the ground up, guiding the tokenizer design, the data mixture, and the way we approached specialization across language clusters. 

Tiny Aya moves beyond multilinguality as a uniform objective and incorporates strategies that preserve diversity during training while enabling efficient downstream adaptation. This design allows researchers to reshape the model without fighting against rigid alignment or over-specialized post-training, making it easier to fine-tune for new domains, emerging languages, or community-driven evaluation frameworks. 

Open-ended generation scores in relation to model size. Tiny Aya demonstrates improved generation quality relative to previous Aya models while operating at a smaller scale, and outperforms strong multilingual baselines such as Gemma at comparable parameter counts.**Small Models, Strong Performance**

We approached building Tiny Aya with a broader goal in mind: building models that remain reliable across many languages while staying efficient enough for local use. The result is a family of models that remain competitive with existing multilingual models across a range of evaluations, especially in tasks like translation, open-ended generation quality, and mathematical reasoning for lower-resourced languages. 

Across a comprehensive multilingual generative benchmark suite, Tiny Aya holds its own against leading models at this scale, advancing performance across all regions. What stands out most is the consistency Tiny Aya maintains across diverse linguistic settings. Instead of optimizing for a narrow set of headline scores, our focus was on stability, breadth, and real-world usability. We cared as much about the “how” as the “what”, meaning that we took into account factors of quality that native speakers care about, concerning fluency and coherence of a response. In practical multilingual scenarios, where efficiency, adaptability, and language coverage matter as much as raw scale, Tiny Aya is best in class and offers a compelling balance between capability and accessibility.

**Accessibility as a Design Principle**

Tiny Aya is designed to run where people are: on local devices, in classrooms, in community labs, and in regions where large-scale infrastructure isn’t always available, for example translating across languages far from cloud infrastructure in a remote village. Lowering the barrier to entry means more people can build, experiment, and shape the future of multilingual AI themselves.

Beyond the model size, accessibility also depends on how efficiently language is represented. Tiny Aya’s tokenizer was designed to reduce fragmentation across scripts and linguistic structures, producing fewer tokens per sentence across languages. This improved tokenization efficiency lowers memory and compute requirements during inference, making multilingual applications more practical on local hardware while also improving responsiveness in real-world use.

Tokenization efficiency across languages measured by average tokens per sequence (lower is better) when encoding the Flores dataset. Tiny Aya achieves the most efficient tokenization across the vast majority of evaluated languages, indicating improved language coverage and reduced fragmentation compared to existing multilingual tokenizers.We see this release as a foundation for a broader ecosystem of specialized multilingual models created by the research community itself. We invite researchers and builders everywhere to take these models and datasets and create their own language-focused systems extending coverage, exploring new evaluation strategies, and pushing multilingual AI in directions we can’t predict alone. The future of multilingual AI will not be one giant model. It will be a vibrant ecosystem of many models, shaped by many voices.

**A Family of Specialized Models**

Tiny Aya prioritizes 67 languages in post-training from 5 regions around the globe.Tiny Aya is built on a shared multilingual foundation that enables cross-lingual learning across 70+ languages. On top of this foundation, we explored how performance can be strengthened within specific language ecosystems without sacrificing broader multilingual capability.

TinyAya-base provides a consistent multilingual backbone across regions. The specialized variants extend this backbone by focusing more deeply on particular linguistic communities, namely Africa, South Asia, and Asia-Pacific, while retaining strong performance outside their primary region.

This approach allows each model to develop stronger linguistic grounding and cultural nuance, creating systems that feel more natural and reliable for the communities they are meant to serve. At the same time, all Tiny Aya models retain broad multilingual coverage, making them flexible starting points for further adaptation and research.

The result is a coordinated model family of regionally specialized variants:

- **TinyAya-Earth**: strongest for languages across Africa and West Asia regions
- **TinyAya-Fire**: strongest for South Asian languages
- **TinyAya-Water**: strongest for the Asia-Pacific and Europe region
Together, these models offer both a globally balanced option and region-focused variants, allowing researchers and builders to choose the right level of coverage for their use cases.

We release four specialized models each with a unique strength profile across regions. **Try Tiny Aya Now**

Tiny Aya is available today as open weight models. You can explore and use Tiny Aya family of models in multiple ways:

- Try it instantly on Hugging Face Space or on the Cohere platform.
- Download the weights on Hugging Face and Kaggle for local deployment and research use.
- Learn more in our detailed technical report describing the training strategy, comprehensive evaluations, and design decisions behind Tiny Aya. 
- Ready to build with Tiny Aya? Learn more about Expedition Tiny Aya- a multi-phase, mentor-supported research challenge designed to catalyze new projects using the Tiny Aya model family
*TinyAya-Base covers 70+ languages including: Amharic, Arabic, Basque, Bengali, Bulgarian, Burmese, Cantonese, Catalan, Chinese (simplified and traditional), Croatian, Czech, Danish, Dutch, English, Estonian, Finnish, French, Galician, German, Greek, Gujarati, Hausa, Hebrew, Hindi, Hungarian, Igbo, Indonesian, Irish, Italian, Japanese, Javanese, Khmer, Korean, Lao, Latvian, Lithuanian, Malagasy, Malay, Maltese, Marathi, Nepali, Nigerian Pidgin, Norwegian (Bokmål), Persian, Polish, Portuguese, Punjabi, Romanian, Russian, Serbian, Shona, Slovak, Slovenian, Spanish, Swahili, Swedish, Tagalog, Tamil, Telugu, Thai, Turkish, Ukrainian, Urdu, Vietnamese, Welsh, Wolof, Xhosa, Yoruba and Zulu.

Tiny Aya: Bridging Scale and Multilingual Depth (2026), by Alejandro R. Salamanca, Diana Abagyan, Daniel D’souza, Ammar Khairi, David Mora, Saurabh Dash, Viraat Aryabumi, Sara Rajaee, Mehrnaz Mofakhami, Ananya Sahu, Thomas Euyang, Brittawnya Prince, Madeline Smith, Hangyu Lin, Acyr Locatelli, Sara Hooker, Tom Kocmi, Aidan Gomez, Ivan Zhang, Phil Blunsom, Nick Frosst, Joelle Pineau, Beyza Ermis, Ahmet Üstün, Julia Kreutzer, Marzieh Fadaee. https://arxiv.org/abs/2603.11510
