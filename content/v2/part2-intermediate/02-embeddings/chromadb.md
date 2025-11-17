---
title: ChromaDB for Vector Storage
weight: 3
---

## What is ChromaDB?

**ChromaDB** is a vector database designed for storing and querying embeddings efficiently. It handles the complexity of vector similarity search so you can focus on building applications.

### Why ChromaDB?

✓ **Easy Setup**: Runs directly from Python, no server required
✓ **Fast**: Optimized for similarity search
✓ **Persistent**: Save your embeddings to disk
✓ **Flexible**: Supports custom embeddings or built-in models
✓ **Production-Ready**: Scales from prototypes to production

---

## Installation

```bash
pip install chromadb
```

That's it! No database server to configure.

---

## Basic Usage

### Create a Collection

```python
import chromadb

# Create client
client = chromadb.Client()

# Create a collection (like a database table)
collection = client.create_collection(name="library_docs")

# Add documents
collection.add(
    documents=[
        "Libraries provide free access to books.",
        "Digital resources are available online.",
        "Community programs support literacy."
    ],
    ids=["doc1", "doc2", "doc3"]
)

# Query
results = collection.query(
    query_texts=["What services do libraries offer?"],
    n_results=2
)

print(results['documents'][0])
```

**Output**:
```
['Libraries provide free access to books.',
 'Community programs support literacy.']
```

{{< callout type="success" >}}
**That Simple!** ChromaDB automatically generated embeddings, stored them, and performed similarity search - all in a few lines of code.
{{< /callout >}}

---

## Persistent Storage

Save embeddings to disk:

```python
import chromadb

# Create persistent client
client = chromadb.PersistentClient(path="./chroma_db")

# Create or get collection
collection = client.get_or_create_collection(name="library_docs")

# Add documents (only needed once)
collection.add(
    documents=["doc1 text", "doc2 text"],
    ids=["id1", "id2"]
)

# Next time, just load:
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection(name="library_docs")
# Your data is still there!
```

---

## Using Custom Embeddings (Ollama)

Instead of ChromaDB's default embeddings, use Ollama models:

```python
import chromadb
import ollama

# Custom embedding function
class OllamaEmbeddingFunction:
    def __init__(self, model_name="nomic-embed-text"):
        self.model_name = model_name

    def __call__(self, input):
        """Generate embeddings for input texts."""
        embeddings = []
        for text in input:
            response = ollama.embed(model=self.model_name, input=text)
            embeddings.append(response['embeddings'][0])
        return embeddings

# Create collection with custom embeddings
client = chromadb.Client()
collection = client.create_collection(
    name="library_docs",
    embedding_function=OllamaEmbeddingFunction()
)

# Now uses Ollama for embeddings!
collection.add(
    documents=["Libraries preserve knowledge"],
    ids=["doc1"]
)
```

---

## Advanced Features

### Metadata Filtering

Add metadata for precise filtering:

```python
collection.add(
    documents=[
        "Pride and Prejudice by Jane Austen",
        "1984 by George Orwell",
        "To Kill a Mockingbird by Harper Lee"
    ],
    metadatas=[
        {"year": 1813, "genre": "romance"},
        {"year": 1949, "genre": "dystopian"},
        {"year": 1960, "genre": "drama"}
    ],
    ids=["book1", "book2", "book3"]
)

# Query with metadata filter
results = collection.query(
    query_texts=["classic literature"],
    where={"year": {"$gt": 1900}},  # Only after 1900
    n_results=2
)
```

### Update Documents

```python
collection.update(
    ids=["doc1"],
    documents=["Updated text"],
    metadatas=[{"updated": True}]
)
```

### Delete Documents

```python
collection.delete(ids=["doc1", "doc2"])
```

### Get Collection Stats

```python
count = collection.count()
print(f"Documents in collection: {count}")
```

---

## Complete Example: Library Search System

```python
import chromadb
import ollama

class LibrarySearch:
    def __init__(self, db_path="./library_db"):
        """Initialize library search system."""
        self.client = chromadb.PersistentClient(path=db_path)

        # Custom embedding function
        class EmbedFunc:
            def __call__(self, input):
                embeddings = []
                for text in input:
                    response = ollama.embed(
                        model='nomic-embed-text',
                        input=text
                    )
                    embeddings.append(response['embeddings'][0])
                return embeddings

        self.collection = self.client.get_or_create_collection(
            name="library_catalog",
            embedding_function=EmbedFunc()
        )

    def add_books(self, books):
        """Add books to the search index.

        Args:
            books: List of dicts with 'id', 'text', and metadata
        """
        self.collection.add(
            ids=[book['id'] for book in books],
            documents=[book['text'] for book in books],
            metadatas=[book.get('metadata', {}) for book in books]
        )

    def search(self, query, n_results=5, filters=None):
        """Search for relevant books."""
        return self.collection.query(
            query_texts=[query],
            n_results=n_results,
            where=filters
        )

# Usage
library = LibrarySearch()

# Add books
books = [
    {
        'id': 'book1',
        'text': 'Pride and Prejudice: A romantic novel about Elizabeth Bennet',
        'metadata': {'author': 'Jane Austen', 'year': 1813}
    },
    {
        'id': 'book2',
        'text': '1984: A dystopian novel about totalitarian surveillance',
        'metadata': {'author': 'George Orwell', 'year': 1949}
    }
]

library.add_books(books)

# Search
results = library.search("romance stories", n_results=1)
print(results['documents'][0])
# ['Pride and Prejudice: A romantic novel...']
```

---

## Performance Tips

### 1. Batch Operations

Add many documents at once:

```python
# Good: Batch insert
collection.add(
    documents=list_of_1000_docs,
    ids=list_of_1000_ids
)

# Avoid: One at a time
for doc, id in zip(docs, ids):
    collection.add(documents=[doc], ids=[id])  # Slow!
```

### 2. Appropriate n_results

```python
# Don't fetch more than you need
results = collection.query(
    query_texts=["query"],
    n_results=5  # Not 100 if you only need 5
)
```

### 3. Use Metadata Filters

```python
# Faster: Filter before similarity search
results = collection.query(
    query_texts=["query"],
    where={"category": "fiction"},  # Pre-filter
    n_results=10
)

# Slower: Filter after fetching all results
```

---

## Comparison: Manual vs. ChromaDB

### Manual Approach (from earlier)

```python
# Store embeddings manually
doc_embeddings = {}
for doc in documents:
    emb = get_embedding(doc)
    doc_embeddings[doc] = emb

# Search manually
query_emb = get_embedding(query)
similarities = []
for doc, doc_emb in doc_embeddings.items():
    sim = cosine_similarity(query_emb, doc_emb)
    similarities.append((doc, sim))
similarities.sort(reverse=True)
results = similarities[:5]
```

**Problems**:
- No persistence
- Slow for large datasets
- Manual similarity computation
- No filtering capabilities

### ChromaDB Approach

```python
collection.add(documents=documents, ids=ids)
results = collection.query(query_texts=[query], n_results=5)
```

**Benefits**:
- Persistent storage
- Optimized search
- Built-in similarity computation
- Metadata filtering

---

## Next: RAG Systems

Now that you can store and search embeddings, let's build Retrieval-Augmented Generation systems:

{{< cards >}}
  {{< card link="/v2/part2-intermediate/03-rag" title="RAG Systems" icon="arrow-right" subtitle="Combine retrieval with generation" >}}
{{< /cards >}}
