---
title: Wrap-up
weight: 5
---

Part 1 is done. This page recaps what you can now do, checks it with five questions, and lists what Part 2 assumes.

## What you can do now

1. Explain next-token prediction, tokens, context window, parameters and quantization in plain words, and connect them to file size, memory and speed.
2. Place a model on the four-tier openness ladder and say why libraries care (provenance, reproducibility, vendor independence).
3. Install Ollama or LM Studio, adjust the privacy settings, download a model that fits your hardware, and check that it works.
4. Write prompts for cataloging-style tasks and improve them step by step.
5. Recognize a confident wrong answer and know two checks for it.

## Self-check

Answer in your head or on paper first, then open the answer.

**1. Why can a model give you 21 words when you asked for exactly 20?**

{{< details title="Show the answer" >}}
It predicts one token at a time and has no counter, so it follows length instructions only approximately.
{{< /details >}}

**2. An 8B model file is about 5 GB at Q4_K_M. How much memory does it need, and what adds to it?**

{{< details title="Show the answer" >}}
At least the file size, because the whole file is loaded into memory. The context window adds more: for the 8B model, each token of context costs 128 KiB.
{{< /details >}}

**3. Your prompt asks for books before 1950, sorted by year. The answer is tidy but wrong. What do you change?**

{{< details title="Show the answer" >}}
Split the task. First ask the model to extract every book with its year. Then filter and sort in a second step, or do that part without the model. Check the result against the text.
{{< /details >}}

**4. Which tier of the openness ladder is Apertus, and why is that not the same as open source?**

{{< details title="Show the answer" >}}
Tier 3, fully open: the weights, training code and checkpoints are published, with scripts to rebuild the training data. Open weights alone puts a model on a lower tier. The Open Source Initiative (OSI) definition of open source asks for information about the training data. Llama 2, for example, fails it although its weights can be downloaded.
{{< /details >}}

**5. The model gives you an ISBN, a DOI or a thesaurus term. Name two checks.**

{{< details title="Show the answer" >}}
Look it up in a real source: a library catalog such as the DNB catalog for an ISBN, Crossref for a DOI, or the thesaurus itself for a term. Ask the same question twice in new chats and compare the answers.
{{< /details >}}

## What Part 2 assumes

Part 2 runs notebooks on your machine. Before you start Part 2, tick these:

- [ ] `ollama pull thalhath/apertus:8b` (or `thalhath/apertus:4b` on an 8 GB machine) has finished.
- [ ] `ollama pull qwen3-embedding:0.6b` has finished.
- [ ] `ollama ps` shows the model while it is loaded.
- [ ] Python 3.12 or 3.13 is installed.
- [ ] `uv` is installed.
- [ ] The notebooks repository is cloned.
- [ ] `00_check_setup` is green on every line.

The full steps are on [Am I ready?](/v3/before-you-start/check). If any box is not ticked, fix it before Part 2 starts. In the live session, use the break for this and ask for help if you get stuck. Part 2 starts with the environment check, described on [Environment](/v3/part2/01-environment).

## Stopping after Part 1?

You can stop here. Part 1 stands on its own. Everything in Part 2 is also available as executed notebooks with their outputs, in the notebooks repository: [github.com/nishad/llm-workshop-notebooks](https://github.com/nishad/llm-workshop-notebooks). Read them at your own pace, and run them when you are ready. [Part 2](/v3/part2) describes what they cover.
