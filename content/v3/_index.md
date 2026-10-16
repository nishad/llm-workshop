---
title: "Getting started with local LLMs (SWIB26)"
toc: false
cascade:
  type: docs
---

Local large language models (LLMs) have moved on since the first edition of this workshop in 2024. The privacy and cost arguments still apply, but many capable models now run on an ordinary laptop and come with permissive licenses, and a few are fully open: the weights, the training code, and the training data or the scripts to rebuild it are all published. For libraries, provenance, reproducibility and independence from a single vendor become things you can check on your own machine. This third edition is built around Apertus, a fully open multilingual model family from the Swiss AI Initiative (EPFL, ETH Zurich, CSCS).

**Part 1 - Fundamentals**

How LLMs work (parameters, tokens, quantization, context); the difference between open source, open weights, and fully open models. Installing a local runtime (Ollama or LM Studio). Choosing a model size for your hardware and writing effective prompts. No programming experience required for this part.

**Part 2 - Working with your data**

Working with LLMs from Python. Generating structured output and validating it. Embeddings and semantic search over controlled vocabularies. Retrieval-augmented generation (RAG) over your own documents. Basics of tool use, such as querying a SPARQL endpoint or an authority file, with a human in the loop.

This is a hands-on workshop. You can follow along with the graphical tools only, run the notebooks, or work through the materials afterwards. The four hours are split into two halves. Part 1 is for beginners and needs no prior experience. Part 2 assumes you can already run a local model and builds on it with Python. Each half stands on its own: you can leave at the break, or join at the break for Part 2.

## What you need

A computer running Windows, macOS or Linux with 20 GB of free storage. 8 GB of RAM is enough for the small model; 16 GB lets you run the larger one. You need an internet connection to download the models, or you can download them in advance; the steps are on [Before you start](before-you-start). For Part 2 you also need Python 3.12 or 3.13 (uv can install it for you).

## When

Monday 16 November 2026, 04:00-08:00 UTC, with a ten-minute break at 06:00. Zoom opens at 03:30 UTC for installation help. Local times, the Zoom details and the setup steps are on [Before you start](before-you-start).

## Three ways to take part

| Way | What you do | What you need |
|---|---|---|
| GUI only | Part 1 fully, Part 2 as a listener | Ollama or LM Studio and the model |
| Run the notebooks | Follow Part 2 hands-on | Python 3.12 or 3.13, uv, the notebooks repository, Ollama |
| Read afterwards | Work through the executed notebooks and these pages | Nothing to install |

## Before the workshop

{{< cards >}}
  {{< card link="before-you-start" title="Before you start" icon="play" subtitle="Everything to do before the day, in order." >}}
  {{< card link="before-you-start/download-models" title="Download the model" icon="download" subtitle="Get the model files before the session." >}}
  {{< card link="before-you-start/check" title="Am I ready?" icon="check-circle" subtitle="A short check that everything works." >}}
{{< /cards >}}

## During the workshop

{{< cards >}}
  {{< card link="part1" title="Part 1" icon="academic-cap" subtitle="Fundamentals: models, runtimes, prompts." >}}
  {{< card link="part2" title="Part 2" icon="code" subtitle="Working with your data from Python." >}}
  {{< card link="resources" title="Resources" icon="book-open" subtitle="Reading, links and reference pages." >}}
  {{< card link="https://github.com/nishad/llm-workshop-notebooks" title="Notebooks" icon="external-link" subtitle="The companion repository on GitHub." >}}
{{< /cards >}}

Facilitator: Nishad Thalhath, RIKEN Center for Integrative Medical Sciences. Materials CC BY 4.0, code MIT.
