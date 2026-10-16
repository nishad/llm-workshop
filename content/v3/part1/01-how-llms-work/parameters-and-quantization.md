---
title: Parameters and quantization
weight: 4
---

## Parameters

**Parameters**, also called weights, are the numbers a model learns during training. Think of them as dials, billions of them. Training adjusts the dials until the model turns an input (a sentence) into a useful output (the next token).

When you learn a language, its patterns, grammar and vocabulary are stored somewhere in your head. In a model, the parameters are where that knowledge is stored. "8B" means eight billion of them.

## From parameters to file size

Each parameter is a number, and every number needs some bytes of storage. How many bytes depends on how precisely the number is stored:

- At full precision, 2 bytes each: 16 GB for the 8B model.
- At Q8_0, about 1 byte each: 8.6 GB.
- At Q4_K_M, about 0.6 bytes each: 5.1 GB.

**Quantization** stores those numbers with less precision, so each one takes fewer bytes. It works like compressing an image: the file shrinks a lot, and most of what you see survives. The file size is also the memory the model needs, because the whole file is loaded into memory when the model runs.

Apertus 8B file sizes in GGUF, the single-file format that Ollama and LM Studio load:

| Quantization | Size |
|---|---|
| Q8_0 | 8.57 GB |
| Q6_K | 6.62 GB |
| Q5_K_M | 5.81 GB |
| Q4_K_M | 5.06 GB |
| Q3_K_M | 4.17 GB |
| Q2_K | 3.29 GB |

The 70B model at Q4_K_M is 43.7 GB.

## What quantization costs

The llama.cpp project (the engine behind Ollama and LM Studio) measured the quality cost on Llama 3 8B. It used perplexity, a score for how surprised a model is by real text, and recorded how much that score rose at each level. The smaller the increase, the less quality was lost:

| Quantization | Perplexity increase |
|---|---|
| Q8_0 | +0.02% |
| Q6_K | +0.3% |
| Q5_K_M | +0.9% |
| Q4_K_M | +2.8% |
| Q3_K_M | +10.5% |
| Q2_K | +56% |

On a 70B model the Q4_K_M cost is only +1.2%.

How to read this:

- Q4_K_M is the default choice: the best balance of size and quality.
- Q8_0 is the high-quality choice when memory allows.
- Avoid Q2 and Q3.
- Bigger models lose less quality at 4 bits (Q4).

Two refinements improve on plain quantization. QAT (quantization-aware training) models are trained to expect the low precision, so they lose less. Dynamic quants keep the most sensitive parts of the model at higher precision and compress the rest more.

## How to read a tag

`nishad/apertus:8b` has three parts: a namespace (`nishad`, the account that published it), a model name (`apertus`) and a tag (`8b`).

`8b-instruct-q4_K_M` has three parts too: a size (`8b`), a variant (`instruct`, a version trained to follow instructions) and a quantization (`q4_K_M`).

{{< callout type="info" >}}
A simple estimate: the memory you need is about the model file, plus the context memory, plus about 3 GB for the operating system and your other apps. See [Hardware](/v3/before-you-start/hardware) for the memory tiers.
{{< /callout >}}
