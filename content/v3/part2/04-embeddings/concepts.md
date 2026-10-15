---
title: Concepts
weight: 1
---

## Embeddings are lists of numbers

An embedding model turns a piece of text into a list of numbers, a vector. The specific values are learned during training. Texts with similar meanings end up with similar vectors; texts with different meanings end up far apart. `qwen3-embedding:0.6b` produces 1,024 numbers per text.

## Comparing vectors with cosine similarity

To compare two texts you compare their vectors. The usual measure is the cosine of the angle between them:

```text
cosine(a, b) = (a · b) / (|a| |b|)
```

If you scale every vector to length 1 (a unit vector), the denominator is 1 and the cosine is just the dot product `a · b`. The notebooks' helper returns unit vectors, so a whole index can be scored against a query with one matrix product. A score near 1 means "pointing the same way"; unrelated texts score noticeably lower, and in this notebook a good match is about 0.6 or more.

Picture two arrows from the same point. A small angle between them gives a score near 1; a wide angle gives a low score.

## Embedding model or chat model

| | Embedding model | Chat model |
|---|---|---|
| Purpose | Turn text into a vector | Generate text |
| Output | A fixed-length list of numbers | Tokens, one after another |
| Workshop example | `qwen3-embedding:0.6b` | `nishad/apertus:8b` |
| Size | Small (639 MB here) | Large (5.1 GB here) |
| Used for | Search, matching, clustering | Writing, extracting, answering |

{{< callout type="warning" >}}
Do not use a chat model such as Apertus for embeddings. Use a model built for it, and use the same one for the index and for the queries.
{{< /callout >}}

## Prefix conventions

Many embedding models expect a short prefix in front of a query, a document, or both. Using the wrong one lowers quality without any error message. These are the conventions in the companion `workshop/embed.py`:

| Model | Query prefix | Document prefix |
|---|---|---|
| `bge-m3` | none | none |
| `qwen3-embedding` | `Instruct: Given a search term, retrieve the matching thesaurus concept\nQuery:` | none |
| `nomic-embed-text` | `search_query: ` | `search_document: ` |
| `embeddinggemma` | `task: search result \| query: ` | `title: none \| text: ` |
| `multilingual-e5` | `query: ` | `passage: ` |
| `snowflake-arctic-embed2` | `query: ` | none |
| `granite-embedding` | none | none |

Ollama adds nothing; the helper does. If you call an embedding model from your own code, you add the prefix yourself.

## Short records and prose

An embedding captures the whole text it is given. A short label such as "Bibliothek" has one clear meaning. A long document with a label, its alternatives and a scope note mixes several. Notebook 03 shows the effect: with one long document per concept, a query that was itself one of a concept's labels ranked a different concept first; with one entry per label, the right concept came first (see [Vocabulary search](/v3/part2/04-embeddings/vocabulary-search)). Long prose should be chunked into pieces before embedding.

## When semantic search struggles

- **Highly technical or specific terms.** "TCP/IP protocol", "UDP protocol" and "HTTP protocol" may not be told apart well.
- **Numbers and dates.** "Published in 1995" and "published in 1996" can look almost the same to an embedding.
- **Negations.** "Libraries are open" and "Libraries are not open" can be close together.

The answer is hybrid search: exact matching on labels, identifiers, numbers and dates (or metadata filters), and semantic search for the rest. In a thesaurus this is natural, because the exact label is always available next to the meaning.

Now [try it on two vocabularies](/v3/part2/04-embeddings/vocabulary-search).
