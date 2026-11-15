---
title: Embeddings
weight: 4
cascade:
  type: docs
---

Keyword search finds the words you typed. Semantic search finds the concept you meant, in any language the embedding model knows. An embedding model turns a text into a list of numbers that represents its meaning; similar meanings give similar lists. This chapter builds semantic search over two controlled vocabularies, the STW Thesaurus for Economics and the UNESCO Thesaurus. It then measures how well the search works.

The notebook for this chapter is `03_vocabulary_search`.

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
An embedding model can place "library" and "bibliothèque" close together, although the two words share almost no letters.
{{< /callout >}}

Imagine plotting labels on a flat chart with two dimensions (real embeddings have hundreds or thousands of dimensions):

```text
                    "library" •

          "book"  •         • "bibliothèque"

                    "reading" •

      • "computer"                    • "knowledge"

    (labels with similar meanings cluster together)
```

## A second model

Apertus generates text and is not an embedding model. The workshop uses `qwen3-embedding:0.6b` beside it. Its license is Apache-2.0, its file is 639 MB, and it turns each text into 1,024 numbers (its dimensions). It has a 32k-token context window. It also expects a short instruction, called a prefix, in front of every query. The notebooks' helper adds that prefix for you. Two alternatives, `bge-m3` and `embeddinggemma`, were measured on the same gold set (a set of test queries with known correct answers). The numbers and licenses are on the [models page](/v3/resources/models).

## What the notebook covers

1. Turn SKOS labels into index entries and embed them in one batch.
2. Search by meaning with four kinds of query: free text, a cross-lingual query (a query in one language against labels in another), a held-out synonym (an alternative label used as the query), and a scope-note question (asking which concept covers a topic).
3. Set a score threshold, show up to three suggestions above it, and let a person pick one.
4. Save the index to a file with sqlite-vec, measure recall (how often the right concept is found) on a gold set, and see why index design matters as much as the model.

## The pages

{{< cards >}}
  {{< card link="/v3/part2/04-embeddings/concepts" title="Concepts" icon="chart-bar" subtitle="Vectors, cosine, prefixes and where semantic search struggles." >}}
  {{< card link="/v3/part2/04-embeddings/vocabulary-search" title="Vocabulary search" icon="search" subtitle="STW and UNESCO queries, with a measured recall." >}}
{{< /cards >}}

The data and its licenses are listed on the [data page](/v3/resources/data). The next chapter, [RAG](/v3/part2/05-rag), builds on embeddings.
