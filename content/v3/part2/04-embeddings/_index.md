---
title: Embeddings
weight: 4
cascade:
  type: docs
---

Keyword search finds the words you typed. Semantic search finds the concept you meant, in any language the embedding model knows. This chapter builds semantic search over two controlled vocabularies, the STW Thesaurus for Economics and the UNESCO Thesaurus, and measures how well it works.

Notebook 03, `03_vocabulary_search`, takes about 25 minutes in the workshop.

## Keywords versus meaning

Traditional text matching:

```text
Query: "library building"
Matches: documents containing exactly "library" AND "building"
Misses: "bibliotheca", "knowledge center", "reading hall"
```

Semantic search with embeddings:

```text
Query: "library building"
Embedding: [0.23, -0.45, 0.78, ...]
Matches: similar vectors, representing:
  - "library facility"
  - "bibliotheca structure"
  - "book repository architecture"
  - "community learning center"
```

{{< callout type="info" >}}
**Key insight:** an embedding model can place "library" and "bibliothèque" (French) close together, even though the two words share almost no letters.
{{< /callout >}}

Imagine plotting labels in two dimensions (real embeddings have hundreds or thousands):

```text
                    "library" •

          "book"  •         • "bibliothèque"

                    "reading" •

      • "computer"                    • "knowledge"

    (labels with similar meanings cluster together)
```

## A second model

{{< callout type="info" >}}
Apertus is a chat model; the embedding model is a second, small open-weights model.
{{< /callout >}}

Apertus generates text and has no embedding model in the Ollama library. The workshop uses `qwen3-embedding:0.6b` beside it: Apache-2.0, 639 MB, 1,024 dimensions, a 32k-token context, and an instruction prefix on queries that the notebooks' helper adds. Two alternatives were measured on the same gold set (`bge-m3` and `embeddinggemma`); the numbers and licences are on the [models page](/v3/resources/models).

## What the notebook covers

1. Turn SKOS labels into index entries and embed them in one batch.
2. Search by meaning: a free-text query, a cross-lingual query, a held-out synonym, a scope-note question.
3. Decide with a threshold and a person: suggest three, pick one.
4. Persist the index with sqlite-vec, measure recall on a gold set, and see why index design matters as much as the model.

## The pages

{{< cards >}}
  {{< card link="/v3/part2/04-embeddings/concepts" title="Concepts" icon="chart-bar" subtitle="Vectors, cosine, prefixes and where semantic search struggles." >}}
  {{< card link="/v3/part2/04-embeddings/vocabulary-search" title="Vocabulary search" icon="search" subtitle="STW and UNESCO queries, with a measured recall." >}}
{{< /cards >}}

The data and its licences are listed on the [data page](/v3/resources/data). Embeddings feed the next chapter, [RAG](/v3/part2/05-rag).
