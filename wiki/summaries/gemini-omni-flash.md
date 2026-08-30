# Gemini Omni Flash

**Source**: `raw/gemini-omni/full-article.html` (424 KB)  
**URL**: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni/  
**Ingested**: 2026-06-06  
**Tags**: #summary

## Summary

At Google I/O 2026, Google DeepMind introduced **Gemini Omni**, a model family where Gemini's reasoning meets generative creation — starting with **video**. **Gemini Omni Flash**, the first Omni model, accepts images, audio, video, and text as input and generates high-quality videos grounded in Gemini's real-world knowledge. Users edit videos through natural-language conversation: each instruction builds on the last with character consistency, coherent physics, and scene memory.

Key capabilities include transforming worlds and actions in existing footage, reimagining scenes with new characters or objects, and generating visuals from short prompts that blend Gemini's world knowledge with creative intent. Omni reasons about what should happen next — combining intuitive **physics** understanding (gravity, kinetic energy, fluid dynamics) with history, science, and cultural context for meaningful storytelling beyond photorealism alone.

Rollout at launch: Google AI Plus, Pro, and Ultra subscribers globally via the Gemini app and Google Flow; free access on YouTube Shorts and YouTube Create starting that week; developer and enterprise APIs planned in coming weeks. Future Omni output modalities (image, audio) are noted as in development. **Avatars** let users generate videos with their own voice and digital likeness. All Omni videos carry imperceptible **SynthID** watermarks verifiable through the Gemini app, Gemini in Chrome, and Google Search.

## Key Claims

- Gemini Omni creates from any input — video is the first output modality; image and audio outputs planned.
- Multimodal inputs: images, audio, video, and text combined into grounded video generation.
- **Conversational editing**: natural-language instructions chain with consistent characters, physics, and scene memory.
- Physics reasoning: improved intuitive understanding of gravity, kinetic energy, and fluid dynamics for realistic motion.
- World-knowledge grounding: connects language, imagery, and meaning beyond pattern matching for explainers and culturally informed scenes.
- **Gemini Omni Flash** ships to Gemini app, Google Flow, and YouTube Shorts/Create at I/O; APIs for developers and enterprises follow in weeks.
- **Avatars**: users can create videos with their own voice via a digital avatar; speech-editing in video is still under responsible-testing review.
- **SynthID** watermark on all Omni-generated videos; verification tools in Gemini app, Chrome, and Search.
- Builds on the Nano Banana image-generation line and natively multimodal Gemini architecture.

## Figures

No benchmark figures in the source; demos are video carousel examples rather than quantitative charts.

## Entities

- [[DeepMind]] — develops Gemini Omni and SynthID.
- [[Vision Language Models]] — natively multimodal input (image, video, text) for video output.
- [[Audio Models]] — audio as input modality; avatar voice generation; future audio output planned.
- [[Computer Vision]] — video generation, physics-grounded scene synthesis, and conversational visual editing.

## Questions & Gaps

- No published benchmark tables or quantitative comparisons to prior video models (Veo, etc.) in this announcement.
- Responsible-deployment boundaries for editing third-party video audio/speech are explicitly still under review.
- Developer API pricing, rate limits, and enterprise terms not specified at launch.
- Technical architecture (diffusion, autoregressive, hybrid) and training data scope are not disclosed.

## Related

- [[Gemini 3.5 Flash]] — sibling I/O 2026 release focused on agentic intelligence and coding speed.
- [[DeepMind]] — entity page for Google DeepMind Gemini 3-era releases.
- [[Vision Language Models]] — multimodal understanding and generation topic hub.
- [[Computer Vision]] — video synthesis and visual reasoning.
- [[Papers Explained 393 - Gemini 2.5]] — prior Gemini generation native multimodal and audio-generation context.
