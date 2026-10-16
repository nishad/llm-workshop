---
title: Concepts
weight: 1
---

## Embeddings are lists of numbers

An embedding model turns a piece of text into a list of numbers, called a vector. During training, the model learns which numbers to produce. Texts with similar meanings get similar vectors; texts with different meanings get vectors that are far apart. `qwen3-embedding:0.6b` produces 1,024 numbers per text.

## Comparing vectors with cosine similarity

To compare two texts, you compare their vectors. The usual measure is cosine similarity: a score for how closely the two vectors point in the same direction. It is the cosine of the angle between them:

```text
cosine(a, b) = (a · b) / (|a| |b|)
```

If you scale every vector to length 1 (a unit vector), the bottom of the fraction becomes 1, and the cosine is just the dot product `a · b`. The notebooks' helper returns unit vectors, so one matrix product scores a whole index against a query. A score near 1 means the two vectors point the same way. Unrelated texts score noticeably lower; in this notebook, a good match is about 0.6 or more.

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

Many embedding models expect a prefix (a short fixed text) in front of a query, a document, or both. If you use the wrong prefix, quality drops and you get no error message. These are the prefixes that the notebooks' helper, `workshop/embed.py`, uses:

| Model | Query prefix | Document prefix |
|---|---|---|
| `bge-m3` | none | none |
| `qwen3-embedding` | `Instruct: Given a search term, retrieve the matching thesaurus concept\nQuery:` | none |
| `nomic-embed-text` | `search_query: ` | `search_document: ` |
| `embeddinggemma` | `task: search result \| query: ` | `title: none \| text: ` |
| `multilingual-e5` | `query: ` | `passage: ` |
| `snowflake-arctic-embed2` | `query: ` | none |
| `granite-embedding` | none | none |

Ollama does not add these prefixes; the helper does. If you call an embedding model from your own code, you must add the prefix yourself.

## Short records and prose

An embedding captures the whole text it is given. A short label such as "Bibliothek" has one clear meaning. A long document that combines a label, its alternatives and a scope note mixes several meanings. Notebook 03 shows the effect. With one long document per concept, the search put a different concept first, even though the query was one of the right concept's own labels. With one entry per label, the right concept came first (see [Vocabulary search](/v3/part2/04-embeddings/vocabulary-search)). Before you embed long prose, cut it into smaller pieces, called chunks.

## When semantic search struggles

- **Highly technical or specific terms.** The model may not clearly distinguish "TCP/IP protocol", "UDP protocol" and "HTTP protocol".
- **Numbers and dates.** "Published in 1995" and "published in 1996" can look almost the same to an embedding.
- **Negations.** "Libraries are open" and "Libraries are not open" can be close together.

The answer is hybrid search, which combines two methods: exact matching on labels, identifiers, numbers and dates (or filters on metadata), and semantic search for everything else. A thesaurus suits this well, because the exact label is always available next to the meaning.

Now [try it on two vocabularies](/v3/part2/04-embeddings/vocabulary-search).
