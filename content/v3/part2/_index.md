---
title: "Part 2: Working with your data"
weight: 20
sidebar:
  open: true
cascade:
  type: docs
---

Part 2 runs from 06:10 to 08:00 UTC, 110 minutes. You move from typing into a chat window to calling the same model from Python, with notebooks that you run, change and keep.

{{< callout type="warning" >}}
Part 2 runs on Ollama. If you installed only LM Studio, install Ollama now (10 minutes) or follow as a listener. The steps are on [Install Ollama](/v3/before-you-start/install-ollama).
{{< /callout >}}

## Learning outcomes

After Part 2 you can:

- call a local model from Python with controlled options and record what was used;
- obtain schema-valid structured output and validate it, handling missing values;
- embed vocabulary concepts and run cross-lingual semantic search;
- build a small RAG pipeline that cites and refuses;
- let a model propose a tool call (authority lookup, SPARQL) and approve or correct it before execution;
- explain the limits of small local models from evidence they produced themselves.

## Timeline

Minutes are counted from 06:10 UTC. Type-along means we run the cells together; an exercise means you work on your own or in a small breakout.

| Minutes | Segment | Mode | Notebook | Site pages |
|---|---|---|---|---|
| 0-10 | Re-entry check: environment, server, model | type-along | `00_check_setup` | [Environment](/v3/part2/01-environment) |
| 10-28 | Python and Ollama: chat, system prompt, options, streaming, the OpenAI-client switch, provenance logging | type-along | `01_python_and_ollama` | [Python and Ollama](/v3/part2/02-python-and-ollama) |
| 28-50 | Structured output and validation | exercise | `02_structured_output` | [Structured output](/v3/part2/03-structured-output) |
| 50-72 | Embeddings and semantic search over a controlled vocabulary | exercise | `03_vocabulary_search` | [Embeddings](/v3/part2/04-embeddings) |
| 72-90 | RAG over your own documents | exercise | `04_rag` | [RAG](/v3/part2/05-rag) |
| 90-105 | Tool use with a human in the loop | demo then exercise | `05_tool_use` | [Tool use](/v3/part2/06-tool-use) |
| 105-110 | Wrap-up: provenance checklist, next steps | demo | | [Wrap-up](/v3/part2/07-wrap-up) |

If the half runs late, the Stretch tiers of RAG and tool use are cut first. They stay in the notebooks for self-study.

## From manual to automated

In Part 1 you worked by hand:

- one prompt at a time in a chat window;
- reading each answer yourself;
- copying and pasting data in and out.

In Part 2 you work with code:

- a script handles hundreds of records;
- every run is repeatable, because the model, options and prompt are fixed;
- every call is logged, so any result can be traced.

## Three ways to take part

- **GUI only.** Part 1 entirely. In Part 2 you follow as a reader and watch the notebooks run.
- **Run the notebooks.** You need the environment from the [next page](/v3/part2/01-environment) and the model pulled.
- **Read afterwards.** Every notebook is committed with its outputs, so you can read it later without running anything.

Each exercise has three tiers: GUI, Run-and-change and Stretch.

## The pages

{{< cards >}}
  {{< card link="/v3/part2/01-environment" title="Environment" icon="terminal" subtitle="Install uv, clone the notebooks, run the readiness check." >}}
  {{< card link="/v3/part2/02-python-and-ollama" title="Python and Ollama" icon="code" subtitle="Chat, options, streaming, the OpenAI client, provenance." >}}
  {{< card link="/v3/part2/03-structured-output" title="Structured output" icon="table" subtitle="Schema-valid records from catalog cards." >}}
  {{< card link="/v3/part2/04-embeddings" title="Embeddings" icon="search" subtitle="Cross-lingual search over a controlled vocabulary." >}}
  {{< card link="/v3/part2/05-rag" title="RAG" icon="document-text" subtitle="Answers with citations, and refusals." >}}
  {{< card link="/v3/part2/06-tool-use" title="Tool use" icon="adjustments" subtitle="The model proposes, you approve." >}}
  {{< card link="/v3/part2/notebooks" title="Notebooks" icon="book-open" subtitle="The index of all six notebooks." >}}
{{< /cards >}}
