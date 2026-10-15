---
title: Tool use
weight: 6
cascade:
  type: docs
---

A tool call is the model asking your program to do something: look up a name in the GND, ask Wikidata a question, run a SPARQL query. The model only proposes the call. A person approves, corrects or refuses it, Python runs it, and the result goes back to the model.

Notebook 05, `05_tool_use`, takes about 15 minutes in the workshop. It defines three tools as plain Python functions, shows the gate where you decide, corrects a misspelled name, chains a GND lookup to Wikidata and the Historical Dictionary of Switzerland, and provokes the failure the loop is built to catch: an identifier the model made up.

## What the notebook covers

1. Define tools as plain Python functions with docstrings.
2. Let the model propose a call; approve it, correct it or refuse it; feed the result back.
3. Chain two tools: GND identifier, then Wikidata, then the Historical Dictionary of Switzerland.
4. Recognize the failure modes and what the loop does about them.

{{< callout type="warning" >}}
Run this chapter's prompts in English. In the October 2026 tests the 8B model called a tool for every English prompt in one probe and for only 1 of 9 German prompts.
{{< /callout >}}

## The pages

{{< cards >}}
  {{< card link="/v3/part2/06-tool-use/concepts" title="Concepts" icon="adjustments" subtitle="The loop, what Apertus does with tools, why the gate, and the rules." >}}
  {{< card link="/v3/part2/06-tool-use/human-in-the-loop" title="Human in the loop" icon="shield-check" subtitle="Notebook 05 with its executed outputs and the SPARQL guard." >}}
{{< /cards >}}

Tool use builds on [structured output](/v3/part2/03-structured-output), because a tool call is a small structured record, and on [RAG](/v3/part2/05-rag), for the questions a document index cannot answer.
