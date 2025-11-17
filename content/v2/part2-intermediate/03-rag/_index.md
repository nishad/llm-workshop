---
title: Retrieval-Augmented Generation (RAG)
weight: 3
cascade:
  type: docs
sidebar:
  open: true
---

## What is RAG?

**Retrieval-Augmented Generation (RAG)** combines the power of LLMs with external knowledge retrieval. Instead of relying only on the model's training data, RAG retrieves relevant information and includes it in the prompt.

### The Problem RAG Solves

**Standard LLM**:
- Limited to training data (knowledge cutoff)
- Cannot access your private documents
- May hallucinate facts
- Cannot cite sources

**RAG-Enhanced LLM**:
- Accesses current information
- Works with YOUR data
- Grounded in retrieved facts
- Can cite sources

---

## How RAG Works

```
User Query → Retrieve Relevant Docs → Augment Prompt → Generate Response
```

**Detailed Flow**:

1. **User asks a question**: "What are the library's hours?"

2. **Retrieve relevant documents**:
   - Convert query to embedding
   - Search vector database
   - Find most similar documents

3. **Augment the prompt**:
   ```
   Context: [Retrieved docs about library hours]

   Question: What are the library's hours?

   Answer based on the context:
   ```

4. **Generate response**:
   - LLM reads context
   - Generates accurate, grounded answer
   - Can cite specific sources

---

## Key Components

### 1. Retriever

Finds relevant information:
- Embedding model (nomic-embed-text)
- Vector database (ChromaDB)
- Similarity search

### 2. Generator

Produces the final response:
- Chat model (Llama 3.2)
- Context-aware prompting
- Structured output

---

## RAG Benefits

✓ **Accuracy**: Grounded in actual documents
✓ **Current Information**: Add new docs anytime
✓ **Privacy**: Your data stays local
✓ **Citations**: Can reference sources
✓ **Smaller Models**: External knowledge supplements model
✓ **Domain-Specific**: Works with specialized content

---

## What You'll Learn

{{< cards >}}
  {{< card link="/v2/part2-intermediate/03-rag/architecture" title="RAG Architecture" subtitle="Understand the RAG pipeline" >}}
  {{< card link="/v2/part2-intermediate/03-rag/implementation" title="Implementation" subtitle="Build a complete RAG system" >}}
  {{< card link="/v2/part2-intermediate/03-rag/notebooks" title="Workshop Notebooks" subtitle="Hands-on Jupyter notebooks" >}}
{{< /cards >}}

---

## RAG vs. Fine-Tuning

| Aspect | RAG | Fine-Tuning |
|--------|-----|-------------|
| **Setup** | Quick, add documents | Slow, requires training |
| **Updates** | Add new docs anytime | Retrain entire model |
| **Data Requirements** | Any amount | Large datasets needed |
| **Cost** | Low (storage only) | High (compute for training) |
| **Privacy** | Fully local | Fully local (if done locally) |
| **Best For** | Dynamic knowledge, Q&A | Specialized tasks, style |

**Use RAG when**: You need to work with changing information or specific documents

---

## Get Started

{{< cards >}}
  {{< card link="/v2/part2-intermediate/03-rag/architecture" title="Start Learning" icon="arrow-right" subtitle="Understand RAG architecture" >}}
{{< /cards >}}
