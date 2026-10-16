---
title: Context
weight: 3
---

The **context window** is the working memory of the model. Everything you typed, everything the model answered and anything you pasted or attached must fit inside it. When it is full, the oldest parts of the conversation are dropped.

## Two numbers

- **The model's maximum.** Apertus 8B supports 65,536 tokens.
- **What Ollama or LM Studio actually uses.** Ollama picks a default based on how much memory your computer has: 4,096 tokens on laptops with under 24 GiB of memory, 32,768 tokens on 24 to 48 GiB, and 262,144 above that. In the Ollama app you change it under Settings, Context length. LM Studio sets it when you load a model.

{{< callout type="warning" >}}
A pasted 20-page PDF does not fit in 4,096 tokens; the model sees the end of it and answers confidently anyway.
{{< /callout >}}

## Context costs memory

For the 8B model, each token of context takes 128 KiB. That means about 0.5 GiB at 4k (4,096 tokens), 1 GiB at 8k and 8 GiB at 64k, in addition to the memory for the model file itself.

We measured this with `ollama ps` in October 2026 on an Apple Silicon laptop:

| Context length | Memory in use |
|---|---|
| 4,096 | 5.3 GB |
| 8,192 | 5.8 GB |
| 32,768 | 9.0 GB |
| 65,536 | 13.1 GB |

The model tags for this workshop use 8,192 tokens: enough for a record, a short document and the answer, and small enough to fit on a 16 GB laptop.

## Demo (type-along, optional)

In a terminal, run `ollama ps` while a model is loaded and note the size. Raise the context length slider in the Ollama app, send one message, and run `ollama ps` again. The size grows with the slider.
