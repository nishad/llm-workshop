---
title: RAG Architecture
weight: 1
---

## RAG Pipeline Components

A complete RAG system has these parts:

```
┌──────────────────────────────────────────────────┐
│                                                  │
│  1. DOCUMENT PROCESSING                          │
│     • Load documents                             │
│     • Split into chunks                          │
│     • Generate embeddings                        │
│     • Store in vector DB                         │
│                                                  │
└──────────────┬───────────────────────────────────┘
               │
               ▼
┌──────────────────────────────────────────────────┐
│                                                  │
│  2. QUERY PROCESSING                             │
│     • User asks question                         │
│     • Convert to embedding                       │
│     • Search vector DB                           │
│     • Retrieve top-k similar documents           │
│                                                  │
└──────────────┬───────────────────────────────────┘
               │
               ▼
┌──────────────────────────────────────────────────┐
│                                                  │
│  3. PROMPT AUGMENTATION                          │
│     • Format retrieved docs as context           │
│     • Construct prompt with context + question   │
│     • Send to LLM                                │
│                                                  │
└──────────────┬───────────────────────────────────┘
               │
               ▼
┌──────────────────────────────────────────────────┐
│                                                  │
│  4. RESPONSE GENERATION                          │
│     • LLM reads context                          │
│     • Generates grounded response                │
│     • (Optional) Cite sources                    │
│                                                  │
└──────────────────────────────────────────────────┘
```

---

## 1. Document Processing (One-Time Setup)

### Chunking Strategy

Split documents into manageable pieces:

```python
def chunk_text(text, chunk_size=500, overlap=50):
    """Split text into overlapping chunks."""
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size - overlap):
        chunk = ' '.join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks

# Example
document = "Very long document text here..."
chunks = chunk_text(document, chunk_size=200, overlap=20)
```

**Why chunk?**:
- Embeddings work best on paragraphs, not entire books
- Retrieves precise, relevant sections
- Fits within context windows

**Chunk Size Guidelines**:
- Too small (< 100 words): Loses context
- Too large (> 1000 words): Less precise retrieval
- **Sweet spot**: 200-500 words with 10-20% overlap

### Embedding & Storage

```python
import chromadb
import ollama

# Initialize
client = chromadb.PersistentClient(path="./rag_db")
collection = client.get_or_create_collection(name="documents")

# Add chunks
for i, chunk in enumerate(chunks):
    collection.add(
        documents=[chunk],
        ids=[f"chunk_{i}"],
        metadatas=[{"source": "document.pdf", "page": i // 10}]
    )
```

---

## 2. Retrieval Process

### Query Embedding

```python
def retrieve_context(query, n_results=3):
    """Retrieve relevant chunks for query."""
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )

    return results['documents'][0]  # Top results
```

### Retrieval Strategies

**1. Top-K Retrieval** (Simplest):
```python
# Get top 3 most similar chunks
chunks = retrieve_context(query, n_results=3)
```

**2. Threshold-Based**:
```python
# Only use chunks above similarity threshold
results = collection.query(query_texts=[query], n_results=10)

filtered = [
    doc for doc, dist in zip(results['documents'][0], results['distances'][0])
    if dist < 0.5  # Lower distance = more similar
]
```

**3. MMR (Maximal Marginal Relevance)**:
```python
# Retrieve diverse results (avoid redundancy)
# ChromaDB doesn't support this natively, but you can implement:
def mmr_rerank(query_emb, doc_embs, lambda_param=0.5):
    """Re-rank to balance relevance and diversity."""
    # Implementation left as exercise
    pass
```

---

## 3. Prompt Construction

### Basic Template

```python
from jinja2 import Template

rag_template = Template("""
You are a helpful assistant. Answer the question based on the context provided.

Context:
{% for chunk in context_chunks %}
{{ chunk }}

{% endfor %}

Question: {{ question }}

Answer based ONLY on the context above. If the answer is not in the context, say "I don't have enough information to answer that."

Answer:
""")

def create_rag_prompt(question, context_chunks):
    return rag_template.render(
        question=question,
        context_chunks=context_chunks
    )
```

### Advanced Template (with Citations)

```python
citation_template = Template("""
Answer the question using the provided context. Cite your sources using [1], [2], etc.

Context:
{% for i, chunk in enumerate(context_chunks) %}
[{{ i + 1 }}] {{ chunk }}

{% endfor %}

Question: {{ question }}

Provide a detailed answer with citations.

Answer:
""")
```

---

## 4. Generation

```python
def rag_query(question, n_results=3):
    """Complete RAG pipeline."""

    # 1. Retrieve context
    context = retrieve_context(question, n_results)

    # 2. Create prompt
    prompt = create_rag_prompt(question, context)

    # 3. Generate response
    response = ollama.generate(
        model='llama3.2',
        prompt=prompt,
        options={'temperature': 0.3}  # Lower for factual
    )

    return {
        'answer': response['response'],
        'context': context,
        'sources': [...]  # Optional: track sources
    }

# Usage
result = rag_query("What are the library's hours?")
print(result['answer'])
```

---

## RAG Enhancements

### 1. Re-ranking

Improve retrieval quality:

```python
def rerank_results(query, initial_results, model='llama3.2'):
    """Re-rank results using LLM."""
    reranked = []

    for doc in initial_results:
        prompt = f"""
        Rate how relevant this document is to the query (0-10):

        Query: {query}
        Document: {doc}

        Relevance score (just the number):
        """

        score = ollama.generate(model=model, prompt=prompt)
        reranked.append((doc, float(score['response'])))

    reranked.sort(key=lambda x: x[1], reverse=True)
    return [doc for doc, score in reranked]
```

### 2. Hybrid Search

Combine semantic + keyword:

```python
def hybrid_search(query, semantic_weight=0.7):
    """Combine semantic and keyword search."""

    # Semantic results
    semantic = collection.query(query_texts=[query], n_results=10)

    # Keyword results (simplified - use BM25 in practice)
    keyword = keyword_search(query, n_results=10)

    # Merge with weights
    combined = merge_results(
        semantic,
        keyword,
        semantic_weight=semantic_weight
    )

    return combined
```

### 3. Query Expansion

Improve retrieval with multiple queries:

```python
def expand_query(original_query):
    """Generate alternative phrasings."""
    prompt = f"""
    Generate 3 alternative ways to ask this question:

    {original_query}

    Return just the 3 alternatives, one per line.
    """

    response = ollama.generate(model='llama3.2', prompt=prompt)
    alternatives = response['response'].strip().split('\n')

    return [original_query] + alternatives

# Use all variants for retrieval
queries = expand_query("library hours")
all_results = []
for q in queries:
    all_results.extend(retrieve_context(q, n_results=2))

# Deduplicate and use top results
```

---

## Performance Considerations

### Latency Breakdown

Typical RAG query:
- Embedding generation: 100-200ms
- Vector search: 10-50ms
- LLM generation: 2-10 seconds (depends on length)

**Total**: ~3-10 seconds

### Optimization Strategies

1. **Cache Embeddings**: Don't re-embed same queries
2. **Limit Retrieved Chunks**: 3-5 is often enough
3. **Batch Processing**: Process multiple queries together
4. **Use Smaller Models**: Consider llama3.2:1b for speed

---

## Next: Implementation

Ready to build a complete RAG system?

{{< cards >}}
  {{< card link="/v2/part2-intermediate/03-rag/implementation" title="RAG Implementation" icon="arrow-right" subtitle="Build a working RAG system" >}}
{{< /cards >}}
