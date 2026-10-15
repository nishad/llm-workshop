---
title: "Getting started with local LLMs (SWIB26)"
toc: false
cascade:
  type: docs
---

Local large language models (LLMs) have moved on since the first edition of this workshop in 2024. The privacy and cost arguments still apply, but many capable models now run on an ordinary laptop, come with permissive licenses, and a few are fully open, with weights, training data, and training code all open. For libraries, this makes provenance, reproducibility, and vendor independence practical concerns. This third edition is built around Apertus, a fully open multilingual model family from the Swiss AI Initiative (EPFL, ETH Zurich, CSCS).

**Part 1 - Fundamentals**

How LLMs work (parameters, tokens, quantization, context); the difference between open source, open weights, and fully open models. Installing a local runtime (Ollama or LM Studio). Choosing a model size for your hardware and writing effective prompts. No programming experience required for this part.

**Part 2 - Working with your data**

Working with LLMs from Python. Generating structured output and validating it. Embeddings and semantic search over controlled vocabularies. Retrieval-augmented generation (RAG) over your own documents. Basics of tool use, such as querying a SPARQL endpoint or an authority file, with a human in the loop.

This is a hands-on workshop. Participants can follow along with the graphical tools only, run the notebooks, or work through the materials afterward. The workshop runs for four hours in two halves. Part 1 (first two hours) is for beginners and needs no prior experience; Part 2 (second two hours) assumes you can already run a local model and builds on it with Python. Each half stands on its own, so you can attend only Part 1 and leave at the break, or join at the break for Part 2. Exact times will be posted with the programme.

Prerequisites:

A computer running Windows, macOS, or Linux with 20 GB of free storage. 8 GB of RAM is sufficient with a small model; 16 GB is recommended for a larger model. A stable internet connection is needed to download models, or you can download them in advance (instructions will be posted about a week before). For Part 2, a working Python environment (3.12 or newer) is needed to follow along.

The Zoom room opens 30 minutes early for installation help.

## When

| | UTC | Tokyo | Sydney | Delhi | Berlin / Zurich | New York |
|---|---|---|---|---|---|---|
| Part 1 | 04:00-06:00 | 13:00-15:00 | 15:00-17:00 | 09:30-11:30 | 05:00-07:00 | 23:00 Sun - 01:00 |
| Break | 06:00-06:10 | | | | | |
| Part 2 | 06:10-08:00 | 15:10-17:00 | 17:10-19:00 | 11:40-13:30 | 07:10-09:00 | 01:10-03:00 |

Zoom opens at 03:30 UTC for installation help. Each half stands on its own: leave at the break, or join at the break for Part 2.

## Three ways to take part

| Way | What you do | What you need |
|---|---|---|
| GUI only | Part 1 fully, Part 2 as a listener | Ollama or LM Studio and the model |
| Run the notebooks | Follow Part 2 hands-on | Python 3.12 or 3.13, uv, the notebooks repository, Ollama |
| Read afterwards | Work through the executed notebooks and these pages | Nothing to install |

## Before the workshop

{{< cards >}}
  {{< card link="before-you-start" title="Before you start" icon="play" subtitle="Check your hardware and install a runtime." >}}
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

## How we work together

- Questions go into the shared document (link added the week before).
- Use the green check and red X in Zoom's participant panel to tell us how you are doing.
- Helpers join breakout rooms when you ask.
- Cameras are optional.

Facilitator: Nishad Thalhath, RIKEN Center for Integrative Medical Sciences. Materials CC BY 4.0, code MIT.
