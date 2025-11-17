---
title: Semantic Search
weight: 2
---

## Semantic Search vs. Keyword Search

**Semantic search** finds information based on meaning and intent, not just exact word matches.

### The Difference

**Keyword Search** (Traditional):
```
Query: "library services"
Matches: Documents containing "library" AND "services"
Misses:  "bibliothèque programs", "what libraries offer"
```

**Semantic Search** (Modern):
```
Query: "library services"
Finds:   - "What do libraries offer?"
         - "Bibliothèque community programs"
         - "Public library resources and amenities"
         - "Services provided by reading centers"
```

### How It Works

1. **Convert query to embedding**
2. **Convert all documents to embeddings** (done once, stored)
3. **Find most similar embeddings** using vector math
4. **Return matching documents**

---

## Semantic Search Implementation

### Basic Example

```python
import ollama
import numpy as np

# Documents to search
documents = [
    "Libraries provide free access to books, computers, and educational programs.",
    "Community centers offer recreational activities and social events.",
    "Museums display historical artifacts and cultural exhibitions.",
    "Digital archives preserve electronic records and manuscripts.",
    "Public libraries support literacy through reading programs and tutoring."
]

# Generate embeddings once
def get_embedding(text):
    response = ollama.embed(model='nomic-embed-text', input=text)
    return np.array(response['embeddings'][0])

print("Generating embeddings...")
doc_embeddings = {doc: get_embedding(doc) for doc in documents}

# Search function
def semantic_search(query, top_k=3):
    """Find most relevant documents for query."""
    query_emb = get_embedding(query)

    # Calculate similarities
    results = []
    for doc, doc_emb in doc_embeddings.items():
        similarity = np.dot(query_emb, doc_emb) / (
            np.linalg.norm(query_emb) * np.linalg.norm(doc_emb)
        )
        results.append((doc, similarity))

    # Sort by similarity
    results.sort(key=lambda x: x[1], reverse=True)

    return results[:top_k]

# Try different queries
queries = [
    "What do libraries offer?",
    "Where can I find historical items?",
    "Places for community activities"
]

for query in queries:
    print(f"\nQuery: {query}")
    print("-" * 60)
    results = semantic_search(query)

    for doc, score in results:
        print(f"Score: {score:.3f} | {doc[:60]}...")
```

**Output**:
```
Query: What do libraries offer?
------------------------------------------------------------
Score: 0.892 | Libraries provide free access to books, computers...
Score: 0.847 | Public libraries support literacy through reading...
Score: 0.623 | Digital archives preserve electronic records...

Query: Where can I find historical items?
------------------------------------------------------------
Score: 0.834 | Museums display historical artifacts and cultural...
Score: 0.712 | Digital archives preserve electronic records...
Score: 0.421 | Libraries provide free access to books...
```

---

## vs. Traditional Search (TF-IDF)

### TF-IDF (Term Frequency-Inverse Document Frequency)

Traditional method that counts word importance:

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# TF-IDF approach
documents = [
    "Libraries provide books and educational resources",
    "Books are available at libraries for reading"
]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

query = "bibliothèque educational materials"
query_vec = vectorizer.transform([query])

scores = cosine_similarity(query_vec, tfidf_matrix)[0]
print(scores)  # [0.52, 0.0] - misses second doc entirely!
```

**Problems**:
- Misses synonyms ("bibliothèque" = "library")
- Misses paraphrases ("materials" ≠ "resources")
- Keyword-dependent

### Semantic Search Wins

```python
# Semantic approach
emb_query = get_embedding("bibliothèque educational materials")
emb_doc1 = get_embedding(documents[0])
emb_doc2 = get_embedding(documents[1])

score1 = cosine_similarity_vec(emb_query, emb_doc1)  # 0.78
score2 = cosine_similarity_vec(emb_query, emb_doc2)  # 0.71

# Both documents recognized as relevant!
```

---

## Practical Use Cases

### 1. Question Answering

```python
def qa_system(question, knowledge_base):
    """Find relevant context and answer question."""

    # Find relevant documents
    relevant_docs = semantic_search(question, top_k=3)

    # Combine into context
    context = "\n\n".join([doc for doc, _ in relevant_docs])

    # Generate answer
    prompt = f"""Context:
    {context}

    Question: {question}

    Answer based on the context:"""

    response = ollama.generate(model='llama3.2', prompt=prompt)
    return response['response']

# Example
knowledge = [
    "The Dewey Decimal system was created in 1876.",
    "Libraries use call numbers to organize books.",
    "The Library of Congress classification is an alternative system."
]

answer = qa_system("When was the Dewey Decimal system created?", knowledge)
```

### 2. Document Clustering

Group similar documents:

```python
from sklearn.cluster import KMeans

# Generate embeddings for all docs
embeddings_matrix = np.array([doc_embeddings[doc] for doc in documents])

# Cluster into groups
kmeans = KMeans(n_clusters=3)
clusters = kmeans.fit_predict(embeddings_matrix)

# Group documents by cluster
for cluster_id in range(3):
    print(f"\nCluster {cluster_id}:")
    for i, doc in enumerate(documents):
        if clusters[i] == cluster_id:
            print(f"  - {doc[:60]}...")
```

### 3. Recommendation System

"Find similar items":

```python
def find_similar(item, all_items, top_k=5):
    """Find items similar to the given item."""
    item_emb = get_embedding(item)

    similarities = []
    for other_item in all_items:
        if other_item == item:
            continue  # Skip the item itself

        other_emb = get_embedding(other_item)
        sim = cosine_similarity_vec(item_emb, other_emb)
        similarities.append((other_item, sim))

    similarities.sort(key=lambda x: x[1], reverse=True)
    return similarities[:top_k]

# Example: Find books similar to what user liked
user_liked = "A mystery novel set in Victorian London"
all_books = [
    "Detective stories from 19th century England",
    "Modern science fiction adventure",
    "Historical fiction about Victorian era",
    "Space opera with alien civilizations"
]

recommendations = find_similar(user_liked, all_books, top_k=2)
```

---

## Optimization Techniques

### 1. Batch Embedding Generation

Process multiple texts at once:

```python
def embed_batch(texts):
    """Generate embeddings for multiple texts efficiently."""
    # Note: Current ollama.embed() processes one at a time
    # This is a pattern for when batch support is added
    embeddings = []
    for text in texts:
        response = ollama.embed(model='nomic-embed-text', input=text)
        embeddings.append(response['embeddings'][0])
    return embeddings

# Use it
docs = ["doc1...", "doc2...", "doc3..."]
embeddings = embed_batch(docs)
```

### 2. Caching Embeddings

Don't re-generate:

```python
import json

def save_embeddings(doc_embeddings, filename):
    """Save embeddings to disk."""
    # Convert numpy arrays to lists for JSON
    saveable = {
        doc: emb.tolist()
        for doc, emb in doc_embeddings.items()
    }

    with open(filename, 'w') as f:
        json.dump(saveable, f)

def load_embeddings(filename):
    """Load embeddings from disk."""
    with open(filename, 'r') as f:
        loaded = json.load(f)

    # Convert lists back to numpy arrays
    return {
        doc: np.array(emb)
        for doc, emb in loaded.items()
    }

# Usage
save_embeddings(doc_embeddings, 'embeddings.json')
# Later...
doc_embeddings = load_embeddings('embeddings.json')
```

### 3. Approximate Nearest Neighbor (ANN)

For large datasets (10,000+ documents), use specialized libraries:

```python
# This is what vector databases like ChromaDB do internally
# We'll use ChromaDB in the next section for this!
```

---

## Limitations and Considerations

### When Semantic Search Struggles

**1. Highly Technical/Specific Terms**:
```python
# May not distinguish well
"TCP/IP protocol" vs "UDP protocol" vs "HTTP protocol"
```

**2. Numbers and Dates**:
```python
# Embeddings may not preserve exact numerical relationships
"published in 1995" vs "published in 1996"
```

**3. Negations**:
```python
# May miss subtle negations
"Libraries are open" vs "Libraries are not open"
```

**Solutions**:
- Combine with keyword filters for precision
- Use metadata for numbers/dates
- Careful prompt engineering

### Best Practices

✓ Chunk long documents into paragraphs
✓ Include context in chunks (not just isolated sentences)
✓ Use consistent preprocessing (lowercase, remove special chars)
✓ Cache embeddings for repeated queries
✓ Combine semantic + keyword search for best results

---

## Next: Vector Databases

Manual embedding management becomes unwieldy with thousands of documents. Let's use ChromaDB:

{{< cards >}}
  {{< card link="/v2/part2-intermediate/02-embeddings/chromadb" title="ChromaDB Setup" icon="arrow-right" subtitle="Efficient vector storage and retrieval" >}}
{{< /cards >}}
