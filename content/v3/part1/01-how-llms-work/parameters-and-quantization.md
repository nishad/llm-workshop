---
title: Parameters and quantization
weight: 4
---

## Parameters

**Parameters** are the numbers a model learns during training. They are the knobs and dials of the model: training turns them until the model transforms input (a sentence) into a useful output (the next token).

Think of your brain learning a new language. With practice you pick up patterns, grammar and vocabulary, and they are stored somewhere. In a model, the parameters are that store. "8B" means eight billion of them.

## From parameters to file size

Each parameter is a number, and a number takes bytes:

- At full precision, 2 bytes each: 16 GB for the 8B model.
- At Q8_0, about 1 byte each: 8.6 GB.
- At Q4_K_M, about 0.6 bytes each: 5.1 GB.

**Quantization** stores those numbers with less precision. It works like compressing an image: the file shrinks a lot, and most of what you see survives. The file size is also the memory the model needs, because the whole file is loaded.

Apertus 8B GGUF file sizes:

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

The llama.cpp project measured the quality cost on Llama 3 8B as the increase in perplexity (lower is better, so a smaller increase is better):

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

- Q4_K_M is the default sweet spot.
- Q8_0 is the high-quality choice when memory allows.
- Avoid Q2 and Q3.
- Bigger models tolerate 4-bit better.

Two refinements exist. QAT (quantization-aware training) builds are trained with the low precision in mind, so they lose less. Dynamic quants keep the most sensitive layers at higher precision and squeeze the rest.

## How to read a tag

`nishad/apertus:8b` is a namespace (`nishad`), a model (`apertus`) and a tag (`8b`).

`8b-instruct-q4_K_M` is a size (`8b`), a variant (`instruct`) and a quantization (`q4_K_M`).

{{< callout type="info" >}}
Rule of thumb: memory needed is about the model file, plus the context memory, plus about 3 GB for the operating system and your other apps. See [Hardware](/v3/before-you-start/hardware) for tiers.
{{< /callout >}}

Next: [Temperature](/v3/part1/01-how-llms-work/temperature).
