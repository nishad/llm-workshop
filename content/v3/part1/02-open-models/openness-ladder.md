---
title: The openness ladder
weight: 1
---

Models are open in different degrees. This ladder has four tiers, with verified examples as of October 2026.

| Tier | Meaning | Examples |
|---|---|---|
| 0 Closed | API only | GPT-5, Claude, Gemini, Meta Muse Spark |
| 1 Open weights, custom license | downloadable, use restrictions, not OSI-approved | Llama 3/4 (700M MAU, naming, EU exclusion for multimodal via the AUP), Gemma 1-3, Qwen2.5-72B, Mistral Large 2407, Teuken-7B v0.6 (CC BY-NC) |
| 2 Open weights, OSI license, data and code closed | | Qwen3/3.5, DeepSeek V3.2/V4 (MIT), gpt-oss, Phi-4, Mistral Small 3.2, Gemma 4 (Apache-2.0 since April 2026), EuroLLM-9B, Salamandra |
| 3 Fully open | weights + training code + data or reproducible recipe + checkpoints | Apertus 1.0 and 1.5, OLMo 3, SmolLM3, Marin, Pythia, EuroLLM-22B (claimed) |
| 3+ Open data | trained only on public-domain or openly licensed text | Pleias 1.0 on Common Corpus, Comma v0.1 on the Common Pile (which includes HathiTrust/IA pre-1929 books, Library of Congress digitized books, BHL, Project Gutenberg) |

Apertus reaches tier 3 through obtainable sources plus reconstruction scripts; there is no hosted corpus to download. That is a weaker kind of openness than a published dataset, and it is worth saying so plainly.

## Four yardsticks

Different bodies measure openness differently.

- **OSI Open Source AI Definition 1.0** (October 2024). It requires "data information" sufficient to rebuild the training set, not the data itself. Llama 2, Mixtral and Phi-2 fail it. Pythia and OLMo pass.
- **Model Openness Framework**. Class I means weights, code, data and checkpoints are all released. That is tier 3 on the ladder.
- **EU AI Act, Article 53**. Since August 2025, every provider of a general-purpose model in the EU must publish a summary of its training content on the Commission's template. Providers of open-source models are included. Fines apply since August 2026.
- **SWIB draft policy**. Training data must be available.

## Four things that are easy to confuse

- **Open weights are not the same as open source.** OSI's definition is failed by Mixtral, Phi-2 and Meta's Llama 2, all of which you can download.
- **Fully open is not the same as ethically sourced.** Pythia is tier 3, yet its training set, the Pile, contained Books3.
- **Open data is not the same as weak.** Comma v0.1, trained only on openly licensed text, matches Llama 2 7B.
- **A permissive license is not the same as stable terms.** Gemma 3 had custom terms and Gemma 4 is Apache-2.0. Teuken 0.4 was Apache-2.0 and 0.6 is non-commercial. Apertus 1.0 was ungated and 1.5 is gated.

{{< callout type="warning" >}}
Check the license of the exact version you download. Terms can change between versions of the same model family.
{{< /callout >}}

## Exercise: place a model on the ladder

Pick a model you have heard of. Open its page on Hugging Face and find two things: the license, and whether the training data is listed. Then choose its tier.

{{< details title="Show a solution" >}}
Three examples, as of October 2026:

- **Llama 3**: tier 1. The weights are downloadable, but the license is custom, with use restrictions.
- **Qwen3**: tier 2. The license is OSI-approved, but the training data and code are closed.
- **OLMo 3**: tier 3. Weights, code, data and checkpoints are all published.
{{< /details >}}

## Check yourself

- [ ] I can name the four tiers of the ladder.
- [ ] I looked up a license and the training-data statement for one model.
- [ ] I can say why "open weights" is not the same as "open source".

{{< callout type="success" >}}
**What you should see:** one model placed on a tier, with the license and the data statement as your two reasons.
{{< /callout >}}
