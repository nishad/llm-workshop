---
title: Wrap-up
weight: 5
---

Part 1 is done. This page recaps what you can now do, checks it with five questions, and lists what Part 2 assumes.

## What you can do now

1. Explain next-token prediction, tokens, context window, parameters and quantization in plain words, and connect them to file size, memory and speed.
2. Place a model on the four-tier openness ladder and say why libraries care (provenance, reproducibility, vendor independence).
3. Install Ollama or LM Studio, configure privacy settings, download a model that fits your hardware and verify it works.
4. Write and iteratively improve prompts for cataloging-style tasks.
5. Recognize a confident wrong answer and know two checks for it.

## Self-check

Answer in your head or on paper first, then open the answer.

**1. Why can a model give you 21 words when you asked for exactly 20?**

{{< details title="Show the answer" >}}
It predicts one token at a time and has no counter. Length instructions are followed approximately.
{{< /details >}}

**2. An 8B model file is about 5 GB at Q4_K_M. How much memory does it need, and what adds to it?**

{{< details title="Show the answer" >}}
At least the file size, because the whole file is loaded into memory. The context window adds more: for the 8B model, each token of context costs 128 KiB.
{{< /details >}}

**3. Your prompt asks for books before 1950, sorted by year. The answer is tidy but wrong. What do you change?**

{{< details title="Show the answer" >}}
Split the task. First extract every book with its year, then filter and sort in a second step, or outside the model. Check the result against the text.
{{< /details >}}

**4. Which tier of the openness ladder is Apertus, and why is that not the same as open source?**

{{< details title="Show the answer" >}}
Tier 3, fully open: weights, training code, a reproducible way to rebuild the data and checkpoints. Open weights alone is a lower tier. The OSI definition of open source asks for data information, and Llama 2, for example, fails it although its weights are downloadable.
{{< /details >}}

**5. The model gives you an ISBN, a DOI or a thesaurus term. Name two checks.**

{{< details title="Show the answer" >}}
Look it up in a real source (the DNB catalog, Crossref, the thesaurus). Ask the same question twice in new chats and compare the answers.
{{< /details >}}

## What Part 2 assumes

Part 2 runs notebooks on your machine. Before the break, tick these:

- [ ] The model is pulled: `ollama pull nishad/apertus:8b` (or `nishad/apertus:4b` on an 8 GB machine) finished.
- [ ] `ollama ps` shows the model while it is loaded.
- [ ] Python 3.12 or 3.13 is installed.
- [ ] `uv` is installed.
- [ ] The notebooks repository is cloned.
- [ ] `00_check_setup` is green on every line.

The full steps are on [Am I ready?](/v3/before-you-start/check). If one box is not ticked, use the break to fix it, or ask for help. Part 2 starts with the environment check, described on [Environment](/v3/part2/01-environment).

## Leaving now?

You can stop here. Part 1 stands on its own. Everything in Part 2 is available afterwards as executed notebooks with their outputs, in the notebooks repository: [github.com/nishad/llm-workshop-notebooks](https://github.com/nishad/llm-workshop-notebooks). Read them at your own pace, and run them when you are ready. [Part 2](/v3/part2) describes what they cover.
