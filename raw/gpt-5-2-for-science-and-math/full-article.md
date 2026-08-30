---
Source URL: https://openai.com/index/gpt-5-2-for-science-and-math/
Fetched via: WebFetch (curl returns 403 on openai.com/index/*)
Date: December 11, 2025
---

# Advancing science and math with GPT‑5.2

GPT‑5.2 is OpenAI's strongest model yet for math and science work.

OpenAI has been working with scientists across math, physics, biology, and computer science to understand where AI can help. An earlier paper compiled case studies across math, physics, biology, computer science, astronomy, and materials science where GPT‑5 helped researchers. With GPT‑5.2, these gains are becoming more consistent and reliable.

## Stronger performance where precision matters

GPT‑5.2 Pro and GPT‑5.2 Thinking are described as the strongest models yet for scientific and mathematical work. Strong mathematical reasoning underlies reliability in scientific and technical work: following multi-step logic, keeping quantities consistent, and avoiding subtle errors that compound in simulations, statistics, forecasting, and modeling.

On GPQA Diamond (graduate-level Q&A across physics, chemistry, biology; no tools, max reasoning effort), GPT‑5.2 Pro achieves 93.2%, GPT‑5.2 Thinking 92.4%. On FrontierMath Tier 1–3 (Python tool enabled, max reasoning effort), GPT‑5.2 Thinking sets a new state of the art, solving 40.3% of problems.

## Case study: learning-curve monotonicity

GPT‑5.2 Pro helped resolve an open research problem in statistical learning theory, documented in the paper "On Learning-Curve Monotonicity for Maximum Likelihood Estimators." The underlying question, posed as an open problem at COLT 2019 by Viering, Mey, and Loog: does more training data reliably reduce expected error (a monotone learning curve), or can it increase error in some settings? Prior work showed non-monotonic learning curves exist even in simple toy setups. The cleanest unresolved case was: a correctly specified Gaussian model with known mean but unknown standard deviation.

The new paper shows that in this clean setting, intuition holds: more data predictably improves learning. The proof was obtained by asking GPT‑5.2 Pro to solve the open problem directly (no intermediate arguments or outline provided), then carefully verified by the authors and reviewed by external subject-matter experts. Follow-up questions extended the result to higher-dimensional settings and other common statistical models. The human role stayed focused on verification and clear writing rather than supplying mathematical scaffolding.

## Looking ahead

This suggests a direction for AI-assisted research in domains with axiomatic theoretical foundations (math, theoretical CS): frontier models can help explore proofs, test hypotheses, and identify connections. These systems are not independent researchers; expert judgment, verification, and domain understanding remain essential, since even highly capable models can make mistakes or rely on unstated assumptions.
