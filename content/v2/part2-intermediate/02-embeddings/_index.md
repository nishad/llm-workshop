---
title: Vector Embeddings & Semantic Search
weight: 2
cascade:
  type: docs
sidebar:
  open: true
---

## Understanding Vector Embeddings

**Vector embeddings** are numerical representations of text that capture semantic meaning. They transform words, sentences, or documents into high-dimensional vectors (arrays of numbers) where similar meanings result in similar vectors.

### The Core Idea

Traditional text matching:
```
Query: "library building"
Matches: Documents containing exactly "library" AND "building"
Misses: "biblioth", "książnica", "knowledge center", "reading hall"
```

Semantic search with embeddings:
```
Query: "library building"
Embedding: [0.23, -0.45, 0.78, ...]
Matches: Similar vectors representing:
  - "library facility"
  - "bibliotheca structure"
  - "book repository architecture"
  - "community learning center"
```

{{< callout type="info" >}}
**Key Insight**: Embeddings allow computers to understand that "library" and "bibliothèque" (French) are semantically similar, even though they share no letters.
{{< /callout >}}

### Why Embeddings Matter

**Search by Meaning, Not Keywords**:
- Find "python programming tutorial" when searching for "learning to code with python"
- Match "climate change impact" with "global warming effects"
- Discover relevant content regardless of exact wording

**Enable Semantic Applications**:
- Question answering systems
- Document similarity detection
- Recommendation engines
- Retrieval-Augmented Generation (RAG)

### What You'll Learn

{{< cards >}}
  {{< card link="/v2/part2-intermediate/02-embeddings/concepts" title="Embedding Concepts" subtitle="How embeddings represent meaning" >}}
  {{< card link="/v2/part2-intermediate/02-embeddings/semantic-search" title="Semantic Search" subtitle="Search by meaning, not keywords" >}}
  {{< card link="/v2/part2-intermediate/02-embeddings/chromadb" title="ChromaDB Setup" subtitle="Vector database for embeddings" >}}
{{< /cards >}}

### Visualization

Imagine plotting documents in 2D space (real embeddings have 1,000+ dimensions):

```
                    "library" •

          "book"  •         • "bibliothèque"

                    "reading" •

      • "computer"                    • "knowledge"

    (words with similar meanings cluster together)
```

Documents about libraries cluster near each other, even if written in different languages or using different terms.

### Get Started

{{< cards >}}
  {{< card link="/v2/part2-intermediate/02-embeddings/concepts" title="Start Learning" icon="arrow-right" subtitle="Begin with embedding concepts" >}}
{{< /cards >}}
