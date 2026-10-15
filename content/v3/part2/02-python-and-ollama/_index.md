---
title: Python and Ollama
weight: 2
cascade:
  type: docs
---

In Part 1 you typed into a chat window. Here the same model answers your code. That is the whole point of scripting what you did by hand: you can send it a hundred records, keep every answer, and record exactly which model produced what.

Notebook 01, `01_python_and_ollama`, takes about 18 minutes in the workshop (minutes 10 to 28 of Part 2). It is a type-along: we run the cells together and you change a few.

## What the notebook covers

1. List the models Ollama has and read a model's facts from Python.
2. Send a chat with a system prompt and control temperature, seed and context length.
3. Stream an answer.
4. Make the same call through the OpenAI client.
5. Record provenance for every result.

## The pages

{{< cards >}}
  {{< card link="/v3/part2/02-python-and-ollama/basics" title="Basics" icon="code" subtitle="Models, chat, temperature and seed, streaming." >}}
  {{< card link="/v3/part2/02-python-and-ollama/portability" title="Portability" icon="switch-horizontal" subtitle="One client, many servers, by changing the base URL." >}}
  {{< card link="/v3/part2/02-python-and-ollama/reproducibility" title="Reproducibility" icon="clipboard-check" subtitle="What to record with every result." >}}
{{< /cards >}}
