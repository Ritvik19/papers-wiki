# article-body

Today, Cohere For AI, Cohereâs open research arm, is proud to announce Aya Vision, a state-of-the-art vision model excelling across multiple languages and modalities. While AI has made significant progress, there is still a big gap in how well models perform across different languages â one that becomes even more noticeable in multimodal tasks that involve both text and images.

Aya Vision aims to explicitly help close that gap. Our release expands multimodal capabilities to 23 languages spoken by over half the world's population. This represents meaningful multimodal progress toward models that can interpret the complex nuances of our world.  

Our Aya Vision models perform well in a variety of tasks, including image captioning, visual question answering, text generation, and translating both text and images into clear, natural-language text. For example, you can attach an image of a piece of art you see while traveling and learn more about what style was used and what region it originated from to foster greater cultural understanding. 

Multilingual excellence

New frontier in vision performance. Aya Vision outperforms the leading open-weight models in multilingual text generation and image understanding.  In its parameter class, Aya Vision 8B achieves the best performance in combined multilingual multimodal tasks, outperforming Qwen2.5-VL 7B, Gemini Flash 1.5 8B, Llama-3.2 11B Vision, and Pangea 7B by up to 70% win rates on AyaVisionBench and 79% on m-WildVision. Aya Vision 32B sets a new frontier in multilingual vision open-weights models, outperforming Llama-3.2 90B Vision, Molmo 72B and Qwen2-VL 72B by up to 64% win rates on AyaVisionBench and 72% win rates on m-WildVision.

Aya Vision outperforms far larger models.  Aya Vision 8B outperforms models 10x its size such as Llama-3.2 90B Vision with 63% win rates. Aya Vision 32B outperforms models more than 2x of its size, such as Llama-3.2 90B Vision, Molmo 72B, and Qwen2.5-VL 72B, with win rates ranging from 50% to 64% on AyaVisionBench and 52% to 72% on mWildVision average across 23 languages.

This showcases our critical focus on efficiency and achieving more using less compute. This also enables greater support for the research community, who often have more limited access to compute resources. 

Scaling gains in performance.  There are key algorithmic breakthroughs we developed over the year and unified in Aya Vision. These include synthetic annotations, scaling up multilingual data through translation and rephrasing, and multimodal model merging â which improve both language and vision understanding in a multilingual setting.  Each step led to significant gains in multimodal performance, improving win rates from 40.9% to 79.1% for our 8B model.  

These breakthroughs further scale with the large 32B model size and enable state-of-the-art performance. Similar to our smaller model, this recipe leads to a significant improvement in performance. 

Bridging gaps in needed multilingual multimodal evaluation. In addition to releasing Aya Vision open-weights, we will open source Aya Vision Benchmark which is a rigorous evaluation set in 23 languages for multimodal multilingual evaluation. In contrast to benchmarks to date which have been focused on academic multiple choice questions, Aya Vision Benchmark captures more nuanced open-ended questions, capturing the evolving nature of real-world user interactions. 

Open-weights and research access

The release of Aya Vision's open-weights is a significant step towards making technical breakthroughs accessible to researchers worldwide. We are releasing Aya Vision as both 8 and 32 billion open-weights models available on Kaggle and Hugging Face, as part of our continued commitment to multilingual research and to accelerate the frontier for multilingual AI.

As part of our commitment to access, we are also enabling free access to our models on WhatsApp. This allows people around the world to leverage these multimodal capabilities across various languages on a platform they already use to communicate every day.
