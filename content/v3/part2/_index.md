---
title: "Part 2: Working with your data"
weight: 20
sidebar:
  open: true
cascade:
  type: docs
---

Part 2 runs from 06:10 to 08:00 UTC. You move from typing into a chat window to calling the same model from Python, with notebooks that you run, change and keep.

{{< callout type="warning" >}}
Part 2 runs on Ollama. If you installed only LM Studio, install Ollama now (10 minutes) or follow as a listener. The steps are on [Install Ollama](/v3/before-you-start/install-ollama).
{{< /callout >}}

## Learning outcomes

After Part 2 you can:

- call a local model from Python, set its options yourself, and record which model and settings each call used;
- get structured output (an answer that must follow a fixed format, usually JSON), validate it and handle missing values;
- embed vocabulary concepts (turn each one into a list of numbers that stands for its meaning) and search them by meaning across languages;
- build a small RAG pipeline that cites its sources and says so when the documents do not answer (RAG means fetching the relevant passages first and giving them to the model with the question);
- let a model propose a tool call (a request for your program to run a function, such as an authority lookup or a SPARQL query) and approve or correct it before anything runs;
- explain the limits of small local models from evidence they produced themselves.

## Program

Type-along means we run the notebook cells together. An exercise means you work on your own or in a small breakout room.

| Segment | Mode | Notebook | Site pages |
|---|---|---|---|
| Re-entry check: environment, server, model | type-along | `00_check_setup` | [Environment](/v3/part2/01-environment) |
| Python and Ollama: chat, system prompt, options, streaming, the OpenAI-client switch, provenance logging | type-along | `01_python_and_ollama` | [Python and Ollama](/v3/part2/02-python-and-ollama) |
| Structured output and validation | exercise | `02_structured_output` | [Structured output](/v3/part2/03-structured-output) |
| Embeddings and semantic search over a controlled vocabulary | exercise | `03_vocabulary_search` | [Embeddings](/v3/part2/04-embeddings) |
| RAG over your own documents | exercise | `04_rag` | [RAG](/v3/part2/05-rag) |
| Tool use with a human in the loop | demo then exercise | `05_tool_use` | [Tool use](/v3/part2/06-tool-use) |
| Wrap-up: provenance checklist, next steps | demo | | [Wrap-up](/v3/part2/07-wrap-up) |

If Part 2 runs late, we cut the Stretch tiers of RAG and tool use first. They stay in the notebooks for self-study.

## From manual to automated

In Part 1 you worked by hand:

- typing one prompt at a time into a chat window;
- reading each answer yourself;
- copying and pasting data in and out.

In Part 2 you work with code:

- a script handles hundreds of records;
- a run can be repeated and checked, because the model, options and prompt are recorded;
- every call is logged, so any result can be traced.

## Three ways to take part

- **GUI only.** You work in a graphical chat app and write no code. That covers all of Part 1. In Part 2 you follow as a listener and watch the notebooks run.
- **Run the notebooks.** You need the environment from the [next page](/v3/part2/01-environment) and the model from [Download the models](/v3/before-you-start/download-models).
- **Read afterwards.** Every notebook is saved with its outputs, so you can read it later without running anything.

Each exercise has three tiers: GUI (do the task in your chat window), Run and change (change one thing and compare) and Stretch (go one step further).

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
