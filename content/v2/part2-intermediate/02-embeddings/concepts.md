---
title: Embedding Concepts
weight: 1
---

## Vector Embeddings Explained

**Vector embeddings** are numerical representations of data that capture semantic meaning in a continuous vector space.

### What Are Embeddings?

An embedding transforms text into an array of numbers:

```python
Text: "Libraries preserve knowledge"
Embedding: [0.23, -0.45, 0.78, -0.12, 0.56, ...]  # 1,000+ dimensions
```

Each number represents a feature or aspect of meaning. The specific values are learned by neural networks during training.

---

## Key Properties

### 1. Dimensionality

**Dimension count** determines how much information the embedding can encode:

| Model | Dimensions | Use Case |
|-------|-----------|----------|
| Small (BERT-base) | 384 | Fast, lower quality |
| **nomic-embed-text** | 1,024 | **Recommended for workshop** |
| Large (OpenAI ada-002) | 1,536 | High quality, slower |
| Very Large | 3,072+ | Research applications |

**Trade-off**: More dimensions = better semantic understanding, but slower and more storage.

### 2. Semantic Proximity

Similar meanings → similar vectors:

```python
embedding("library") ≈ embedding("bibliothèque")
embedding("cat") ≈ embedding("feline")
embedding("run quickly") ≈ embedding("sprint")
```

Dissimilar meanings → distant vectors:

```python
embedding("library") ≠ embedding("rocket")
embedding("happy") ≠ embedding("database")
```

### 3. Vector Math

Embeddings support mathematical operations:

```
embedding("Paris") - embedding("France") + embedding("Japan") ≈ embedding("Tokyo")
```

This allows for analogical reasoning and relationship discovery.

---

## How Embeddings Are Generated

### Embedding Models

Specialized neural networks create embeddings. For this workshop, we'll use:

**nomic-embed-text** (Recommended):
- 1,024 dimensions
- Optimized for semantic search
- Fast and accurate
- Outperforms OpenAI ada-002 on many benchmarks

**Download it**:
```bash
ollama pull nomic-embed-text
```

{{< callout type="info" >}}
**Why this model?** While there are more recent embedding models available, we're using `nomic-embed-text` for consistency with the previous workshop. You're welcome to explore and test other embedding models listed in the [Ollama embeddings documentation](https://docs.ollama.com/capabilities/embeddings), but we won't be switching models during this workshop.
{{< /callout >}}

### Generation Process

1. **Input**: Raw text
2. **Tokenization**: Break into pieces
3. **Neural Network**: Process through layers
4. **Output**: High-dimensional vector

```python
import ollama

response = ollama.embed(
    model='nomic-embed-text',
    input='Libraries preserve knowledge for future generations.'
)

embedding = response['embeddings'][0]
print(f"Dimensions: {len(embedding)}")  # 1,024
print(f"Sample values: {embedding[:5]}")  # [0.23, -0.45, ...]
```

---

## Similarity Measurement

To find similar texts, we measure distance between vectors:

### Cosine Similarity

Most common metric for text embeddings:

```python
import numpy as np

def cosine_similarity(vec1, vec2):
    """Calculate cosine similarity between two vectors."""
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    return dot_product / (norm1 * norm2)

# Range: -1 (opposite) to 1 (identical)
# Typical semantic match: 0.7-0.9
```

**Example**:
```python
import ollama
import numpy as np

def get_embedding(text):
    response = ollama.embed(model='nomic-embed-text', input=text)
    return response['embeddings'][0]

# Generate embeddings
emb1 = get_embedding("public library")
emb2 = get_embedding("community library facility")
emb3 = get_embedding("rocket science")

# Calculate similarities
sim_1_2 = cosine_similarity(emb1, emb2)  # ~0.85 (very similar)
sim_1_3 = cosine_similarity(emb1, emb3)  # ~0.15 (not similar)

print(f"library vs library facility: {sim_1_2:.2f}")
print(f"library vs rocket science: {sim_1_3:.2f}")
```

---

## Important Concepts

### Context Window

Embeddings are typically generated for:
- **Short texts**: Sentences or paragraphs (best quality)
- **Medium texts**: Documents up to 8,192 tokens (nomic-embed-text limit)
- **Long texts**: Should be chunked into smaller pieces

### Embedding Models vs. Chat Models

**Don't confuse them**:

| Type | Purpose | Example |
|------|---------|---------|
| **Embedding Model** | Convert text → vector | nomic-embed-text |
| **Chat/LLM** | Generate text responses | llama3.2 |

{{< callout type="warning" >}}
**Common Mistake**: Don't use Llama 3.2 for embeddings! Use specialized embedding models like `nomic-embed-text`.
{{< /callout >}}

### Embedding Stability

Same input → same embedding (deterministic):

```python
emb_1a = get_embedding("hello world")
emb_1b = get_embedding("hello world")
# emb_1a == emb_1b (identical)

emb_2 = get_embedding("hello world!")  # Different punctuation
# emb_2 ≈ emb_1a (very similar, but not identical)
```

---

## Practical Example: Finding Similar Documents

```python
import ollama
import numpy as np

# Sample documents
documents = [
    "Public libraries offer free access to books and computers.",
    "The library provides community programs and educational resources.",
    "Rockets use combustion to achieve thrust and escape velocity.",
    "Space exploration requires advanced propulsion systems.",
    "Digital libraries preserve historical documents electronically."
]

# Generate embeddings for all documents
def get_embedding(text):
    response = ollama.embed(model='nomic-embed-text', input=text)
    return np.array(response['embeddings'][0])

doc_embeddings = [get_embedding(doc) for doc in documents]

# Query
query = "What services do libraries provide?"
query_embedding = get_embedding(query)

# Find most similar documents
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

similarities = [
    (i, cosine_similarity(query_embedding, doc_emb))
    for i, doc_emb in enumerate(doc_embeddings)
]

# Sort by similarity
similarities.sort(key=lambda x: x[1], reverse=True)

# Show top 3 matches
print("Top 3 similar documents:\n")
for i, sim in similarities[:3]:
    print(f"Similarity: {sim:.3f}")
    print(f"Document: {documents[i]}\n")
```

**Expected Output**:
```
Top 3 similar documents:

Similarity: 0.872
Document: The library provides community programs and educational resources.

Similarity: 0.845
Document: Public libraries offer free access to books and computers.

Similarity: 0.723
Document: Digital libraries preserve historical documents electronically.
```

Notice: Rocket-related docs score much lower (~0.2-0.3)

---

## Benefits and Limitations

### ✓ Benefits

- Capture semantic meaning beyond keywords
- Work across languages (with multilingual models)
- Enable similarity search and clustering
- Support recommendation systems
- Foundation for RAG and advanced AI applications

### ✗ Limitations

- Require storage (1KB per document with 1,024 dims)
- Computation cost for large datasets
- "Black box" - hard to interpret specific dimensions
- Quality depends on embedding model training
- May not capture very domain-specific nuances

---

## Next: Semantic Search

Now that you understand embeddings, let's build a semantic search system:

{{< cards >}}
  {{< card link="/v2/part2-intermediate/02-embeddings/semantic-search" title="Semantic Search" icon="arrow-right" subtitle="Build search by meaning, not keywords" >}}
{{< /cards >}}
