---
title: RAG Implementation
weight: 2
---

## Complete RAG System

Build a production-ready RAG system step-by-step.

---

## Full Implementation

```python
import chromadb
import ollama
from jinja2 import Template
from pathlib import Path

class RAGSystem:
    """A complete RAG system with Ollama and ChromaDB."""

    def __init__(self, db_path="./rag_database", collection_name="knowledge"):
        """Initialize RAG system."""
        # Setup ChromaDB
        self.client = chromadb.PersistentClient(path=db_path)
        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )

        # Prompt template
        self.template = Template("""
You are a helpful assistant. Answer the question based on the provided context.

Context:
{% for chunk in context %}
{{ chunk }}

{% endfor %}

Question: {{ question }}

Answer based ONLY on the context above. If the answer is not in the context,
say "I don't have enough information to answer that."

Answer:
""")

    def chunk_text(self, text, chunk_size=400, overlap=50):
        """Split text into overlapping chunks."""
        words = text.split()
        chunks = []

        for i in range(0, len(words), chunk_size - overlap):
            chunk = ' '.join(words[i:i + chunk_size])
            if chunk:  # Skip empty chunks
                chunks.append(chunk)

        return chunks

    def add_document(self, text, doc_id, metadata=None):
        """Add a document to the knowledge base."""
        # Chunk the document
        chunks = self.chunk_text(text)

        # Add each chunk
        for i, chunk in enumerate(chunks):
            chunk_id = f"{doc_id}_chunk_{i}"
            chunk_metadata = metadata.copy() if metadata else {}
            chunk_metadata['chunk_index'] = i
            chunk_metadata['total_chunks'] = len(chunks)

            self.collection.add(
                documents=[chunk],
                ids=[chunk_id],
                metadatas=[chunk_metadata]
            )

        print(f"Added document '{doc_id}' ({len(chunks)} chunks)")

    def add_documents_from_directory(self, directory_path):
        """Add all .txt files from a directory."""
        directory = Path(directory_path)

        for file_path in directory.glob('*.txt'):
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()

            self.add_document(
                text=text,
                doc_id=file_path.stem,
                metadata={'source': str(file_path)}
            )

    def query(self, question, n_results=3, temperature=0.3):
        """Query the RAG system."""
        # Retrieve relevant chunks
        results = self.collection.query(
            query_texts=[question],
            n_results=n_results
        )

        context_chunks = results['documents'][0]

        # Create prompt
        prompt = self.template.render(
            context=context_chunks,
            question=question
        )

        # Generate response
        response = ollama.generate(
            model='llama3.2',
            prompt=prompt,
            options={'temperature': temperature}
        )

        return {
            'answer': response['response'],
            'context': context_chunks,
            'metadata': results.get('metadatas', [[]])[0]
        }

# Example Usage
rag = RAGSystem()

# Add a document
document = """
The Metropolitan Public Library is open Monday through Friday from 9 AM to 8 PM.
On Saturdays, the library is open from 10 AM to 6 PM. The library is closed on
Sundays and major holidays. During summer months (June-August), extended hours
are available until 9 PM on weekdays.
"""

rag.add_document(
    text=document,
    doc_id="library_hours",
    metadata={"type": "policy", "department": "operations"}
)

# Query
result = rag.query("What are the library's hours?")
print("Answer:", result['answer'])
print("\nContext used:")
for chunk in result['context']:
    print(f"- {chunk[:100]}...")
```

---

## Advanced Features

### Streaming Responses

```python
def query_stream(self, question, n_results=3):
    """Query with streaming response."""
    # Retrieve context
    results = self.collection.query(
        query_texts=[question],
        n_results=n_results
    )

    # Create prompt
    prompt = self.template.render(
        context=results['documents'][0],
        question=question
    )

    # Stream response
    stream = ollama.generate(
        model='llama3.2',
        prompt=prompt,
        stream=True
    )

    full_response = ""
    for chunk in stream:
        text = chunk['response']
        print(text, end='', flush=True)
        full_response += text

    print()  # New line
    return full_response
```

### With Source Citations

```python
def query_with_citations(self, question, n_results=3):
    """Query and return citations."""
    results = self.collection.query(
        query_texts=[question],
        n_results=n_results
    )

    # Template with citations
    citation_template = Template("""
Answer the question using the provided context. Cite sources using [1], [2], etc.

Context:
{% for i, chunk in enumerate(context) %}
[{{ i + 1 }}] {{ chunk }}

{% endfor %}

Question: {{ question }}

Answer with citations:
""")

    prompt = citation_template.render(
        context=results['documents'][0],
        question=question
    )

    response = ollama.generate(model='llama3.2', prompt=prompt)

    return {
        'answer': response['response'],
        'sources': [
            {
                'citation': i + 1,
                'text': chunk,
                'metadata': meta
            }
            for i, (chunk, meta) in enumerate(
                zip(results['documents'][0], results['metadatas'][0])
            )
        ]
    }
```

---

## Production Improvements

### Error Handling

```python
def safe_query(self, question, n_results=3):
    """Query with comprehensive error handling."""
    try:
        # Check if collection has documents
        if self.collection.count() == 0:
            return {
                'answer': "No documents in knowledge base.",
                'error': 'empty_collection'
            }

        # Query
        result = self.query(question, n_results)
        return result

    except Exception as e:
        print(f"Error during query: {e}")
        return {
            'answer': "An error occurred processing your question.",
            'error': str(e)
        }
```

### Caching

```python
from functools import lru_cache
import hashlib

class CachedRAGSystem(RAGSystem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.query_cache = {}

    def query(self, question, n_results=3, temperature=0.3):
        """Query with caching."""
        # Create cache key
        cache_key = hashlib.md5(
            f"{question}_{n_results}_{temperature}".encode()
        ).hexdigest()

        # Check cache
        if cache_key in self.query_cache:
            print("Cache hit!")
            return self.query_cache[cache_key]

        # Query normally
        result = super().query(question, n_results, temperature)

        # Cache result
        self.query_cache[cache_key] = result

        return result
```

---

## Testing Your RAG System

```python
def test_rag_system():
    """Test RAG system with sample data."""
    rag = RAGSystem(db_path="./test_db")

    # Add test documents
    test_docs = [
        ("The library was founded in 1895.", "history"),
        ("We have over 500,000 books in our collection.", "collection"),
        ("Digital resources are available 24/7 online.", "digital")
    ]

    for text, doc_id in test_docs:
        rag.add_document(text, doc_id)

    # Test queries
    test_queries = [
        "When was the library founded?",
        "How many books are there?",
        "Can I access resources online?"
    ]

    for query in test_queries:
        print(f"\nQ: {query}")
        result = rag.query(query)
        print(f"A: {result['answer']}")

test_rag_system()
```

---

## Comparison: With vs. Without RAG

```python
def compare_with_without_rag(question):
    """Compare RAG vs. non-RAG responses."""

    # Without RAG
    no_rag = ollama.generate(
        model='llama3.2',
        prompt=question
    )

    # With RAG
    rag = RAGSystem()
    rag.add_document(your_document, "doc1")
    with_rag = rag.query(question)

    print("Without RAG:")
    print(no_rag['response'])
    print("\nWith RAG:")
    print(with_rag['answer'])

# Try it
compare_with_without_rag("What are your library's hours?")
```

**Without RAG**: Generic answer or "I don't know"
**With RAG**: Specific, accurate answer based on your documents

---

## Next: Workshop Notebooks

See RAG in action with hands-on notebooks:

{{< cards >}}
  {{< card link="/v2/part2-intermediate/03-rag/notebooks" title="Workshop Notebooks" icon="arrow-right" subtitle="Jupyter notebooks with complete examples" >}}
{{< /cards >}}
