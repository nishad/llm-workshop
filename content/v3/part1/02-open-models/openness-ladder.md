---
title: The openness ladder
weight: 1
---

Models are open to different degrees. This ladder has four tiers, or levels, numbered 0 to 3, plus a 3+ for models trained only on openly licensed data. We checked the examples in October 2026.

| Tier | Meaning | Examples |
|---|---|---|
| 0 Closed | API only | GPT-5, Claude, Gemini, Meta Muse Spark |
| 1 Open weights, custom license | downloadable, use restrictions, not OSI-approved | Llama 3/4 (a cap of 700 million monthly users, naming rules, and an EU exclusion for the multimodal models in the acceptable-use policy), Gemma 1-3, Qwen2.5-72B, Mistral Large 2407, Teuken-7B v0.6 (CC BY-NC) |
| 2 Open weights, OSI license, data and code closed | | Qwen3/3.5, DeepSeek V3.2/V4 (MIT), gpt-oss, Phi-4, Mistral Small 3.2, Gemma 4 (Apache-2.0 since April 2026), EuroLLM-9B, Salamandra |
| 3 Fully open | weights + training code + data or reproducible recipe + checkpoints | Apertus 1.0 and 1.5, OLMo 3, SmolLM3, Marin, Pythia, EuroLLM-22B (claimed) |
| 3+ Open data | trained only on public-domain or openly licensed text | Pleias 1.0 on Common Corpus, Comma v0.1 on the Common Pile (which includes HathiTrust/IA pre-1929 books, Library of Congress digitized books, BHL, Project Gutenberg) |

Apertus reaches tier 3 by naming sources you can obtain yourself and by publishing scripts that rebuild the training data from them. There is no ready-made dataset to download. That is a weaker kind of openness than publishing the dataset itself.

## Four yardsticks

Different organizations measure openness in different ways.

- **OSI Open Source AI Definition 1.0** (October 2024), from the Open Source Initiative. It requires enough "data information" to rebuild the training set, but not the data itself. Pythia and OLMo pass.
- **Model Openness Framework**. Class I means weights, code, data and checkpoints (versions of the model saved at points during training) are all released. That is tier 3 on the ladder.
- **EU AI Act, Article 53**. Since August 2025, every provider of a general-purpose model in the EU must publish a summary of its training content, using the European Commission's template. This includes providers of open-source models. Fines have applied since August 2026.
- **SWIB draft policy**. Training data must be available.

## Four things that are easy to confuse

- **Open weights are not the same as open source.** Mixtral, Phi-2 and Llama 2 can all be downloaded, yet none of them meets the OSI definition.
- **Fully open is not the same as ethically sourced.** Pythia is tier 3, yet its training set, the Pile, contained Books3.
- **Open data does not mean a weak model.** Comma v0.1, trained only on openly licensed text, matches Llama 2 7B.
- **A permissive license is not the same as stable terms.** Gemma 3 had custom terms and Gemma 4 is Apache-2.0. Teuken 0.4 was Apache-2.0 and 0.6 is non-commercial. Apertus 1.0 could be downloaded directly, and 1.5 is gated: you must agree to a policy before you can download it.

{{< callout type="warning" >}}
Check the license of the exact version you download. Terms can change between versions of the same model family.
{{< /callout >}}

## Exercise: place a model on the ladder

Pick a model you have heard of. Open its page on Hugging Face (the website where most open models are published) and find two things: the license, and whether the training data is listed. Then choose its tier.

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
