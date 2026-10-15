---
title: RAG
weight: 5
cascade:
  type: docs
---

Think of an open-book exam. A student who has memorized the course may still get a detail wrong, but a student who may look in the book can find the page and quote it. Retrieval-augmented generation (RAG) gives the model the book: your program finds the few passages that matter, puts them in the prompt, and asks for an answer that cites them.

Notebook 04, `04_rag`, takes about 20 minutes in the workshop. It builds the whole pipeline in a few cells, without a framework: load two standards documents, cut them into chunks, embed each chunk once, retrieve the best chunks for a question, and ask the model to answer from them with numbered citations or to say that the documents do not answer.

## What the notebook covers

1. Load and chunk documents, keeping the source of every chunk.
2. Embed once and retrieve by question.
3. Prompt for grounded answers with citations and a refusal when the documents are silent.
4. Respect the context budget, and judge five questions against expected answers.

{{< callout type="info" >}}
The notebook shows the retrieved passages before the answer. If the right passage is not among them, no prompt can fix the answer, so look at retrieval first.
{{< /callout >}}

## The pages

{{< cards >}}
  {{< card link="/v3/part2/05-rag/concepts" title="Concepts" icon="book-open" subtitle="The four steps, chunking, the grounded prompt and when RAG is not the answer." >}}
  {{< card link="/v3/part2/05-rag/pipeline" title="Pipeline" icon="document-text" subtitle="Notebook 04 with its executed outputs, including the failures." >}}
{{< /cards >}}

RAG builds on the [embeddings](/v3/part2/04-embeddings) chapter, which explains how a question and a passage become comparable vectors.
