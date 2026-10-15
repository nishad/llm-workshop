---
title: Choose a model size for your hardware
weight: 2
---

Pick one row of the table below and use that model throughout. The Apple Silicon numbers on this page are October 2026 measurements; the Windows and Linux rows are estimates from published benchmarks.

## What uses your memory

1. **The model file.** About 0.6 GB per billion parameters in the compressed form the workshop uses (Q4_K_M); higher-precision versions are larger. [Parameters and quantization](/v3/part1/01-how-llms-work/parameters-and-quantization) explains the names.
2. **The context window's memory.** For the 8B model this is about 0.5 GB for every 4,096 tokens of context.

Both must fit in RAM next to your operating system and open applications.

```mermaid
flowchart LR
    RAM[Your RAM] --> OS[OS and apps, about 3 GB]
    RAM --> M[Model file]
    RAM --> C[Context memory]
```

## The tiers

| Your memory | Model tag | File | In memory | Context | What it cannot do |
|---|---|---|---|---|---|
| 8 GB | `nishad/apertus:4b` | 2.4 GB | about 2.8 GB | 4,096 tokens (hard limit) | Long documents in RAG; tool calls less reliable (11 of 20 in testing); quality below the 8B |
| 16 GB or more | `nishad/apertus:8b` | 5.1 GB | about 5.3 GB at 4,096 and 5.8 GB at 8,192 context | 8,192 tokens by default, up to 65,536 | Nothing in this workshop |
| 16 GB, curious | `nishad/apertus:8b-v1.5-preview` | 5.1 GB | as the 8B | 8,192 by default | Unofficial build, not checked against the original; see the [Model guide](/v3/resources/models) |

{{< callout type="warning" >}}
Do not try the 8B on an 8 GB machine. It will swap to disk and every answer will take minutes.
{{< /callout >}}

## Speed you can expect

Speeds for the 8B in tokens per second: measured on Apple Silicon, estimated for Windows and Linux. The 4B is roughly twice as fast.

| Machine | Tokens per second |
|---|---|
| Base Apple M1, M2 or M4 | about 14 to 24 |
| Apple M-Pro and M-Max | 40 to 80 |
| Windows or Linux laptop, no graphics card, DDR4 | 3 to 7 |
| Windows or Linux laptop, no graphics card, DDR5 | 9 to 14 |

Prompt processing on a CPU is slow: a 2,000-token prompt takes 35 to 80 seconds before the first word appears. This is why Part 2 keeps RAG prompts short on 8 GB machines.

## Special cases

- **Intel Macs** run Ollama on the CPU only, and LM Studio not at all.
- **Windows laptops with integrated Intel or AMD graphics** run on the CPU. Ollama does not use the integrated GPU by default.
- **A laptop NVIDIA card with 6 to 8 GB** fits the 8B only at 4k context.

## Measure your own machine

```bash
ollama run nishad/apertus:8b --verbose
```

Ask one question and read the `eval rate` line. While the model is loaded, `ollama ps` shows SIZE, PROCESSOR (100% GPU or a CPU split) and CONTEXT.

{{< callout type="success" >}}
If `eval rate` is above 10 tokens per second you will be comfortable in both halves.
{{< /callout >}}

## Why 70B is not on the list

The 70B variant is a 44 GB file. It does not fit on a laptop, and the workshop does not need it.
