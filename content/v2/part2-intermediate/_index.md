---
title: "Part 2: Intermediate Topics"
weight: 20
cascade:
  type: docs
---

## Workshop Part 2: Intermediate Topics (2 hours)

Welcome to Part 2! Now that you understand LLM fundamentals and can interact with them effectively, we'll explore programmatic automation, vector embeddings, and retrieval-augmented generation (RAG).

### Learning Objectives

By the end of Part 2, you will be able to:

✓ Automate LLM interactions using Python
✓ Understand vector embeddings and semantic similarity
✓ Build semantic search systems with ChromaDB
✓ Implement RAG pipelines to enhance LLM responses with external data
✓ Work with Jupyter notebooks for exploratory AI work

### Timeline (2 hours)

| Time | Topic | Duration |
|------|-------|----------|
| 2:15 - 2:45 | Python Integration & Automation | 30 min |
| 2:45 - 3:15 | Vector Embeddings & Semantic Search | 30 min |
| 3:15 - 3:45 | Retrieval-Augmented Generation (RAG) | 30 min |
| 3:45 - 4:00 | Wrap-up & Next Steps | 15 min |

### Topics Covered

{{< cards >}}
  {{< card link="/v2/part2-intermediate/01-python-integration" title="Python Integration" icon="code" subtitle="Automate and script LLM interactions" >}}
  {{< card link="/v2/part2-intermediate/02-embeddings" title="Vector Embeddings" icon="sparkles" subtitle="Understand semantic search and vector databases" >}}
  {{< card link="/v2/part2-intermediate/03-rag" title="RAG Systems" icon="database" subtitle="Build retrieval-augmented generation pipelines" >}}
{{< /cards >}}

### What You'll Build

In Part 2, you'll move from interactive chat to programmatic automation:

- **Python Scripts**: Automate document processing and analysis
- **Semantic Search**: Find relevant information using meaning, not keywords
- **RAG Pipeline**: Combine your data with LLM capabilities
- **Jupyter Workflows**: Create reproducible AI workflows

### Prerequisites for Part 2

To follow along hands-on with Part 2, you should have:

- **Python 3.8+** installed
- **Jupyter Notebook** or JupyterLab
- **Ollama running** with Llama 3.2 model
- **Basic Python knowledge** (variables, functions, loops)

{{< callout type="info" >}}
**Don't Have Python Setup?** You can still follow along conceptually! We'll explain each step clearly. You can set up Python later and try the notebooks on your own time.
{{< /callout >}}

### Python Libraries We'll Use

```bash
pip install ollama chromadb jinja2
```

- **ollama**: Official Python library for Ollama
- **chromadb**: Vector database for embeddings
- **jinja2**: Template engine for prompts

### From Manual to Automated

**Part 1** (Manual Interaction):
- Type prompts in GUI
- Read responses
- Copy/paste data manually

**Part 2** (Programmatic):
- Scripts process hundreds of documents
- Automated data extraction
- Batch operations
- Reproducible workflows

### Why This Matters

**Automation** scales your work:
- Process 1,000 documents instead of 10
- Consistent, repeatable results
- Integration with existing systems
- Build custom applications

**RAG** enhances capabilities:
- LLM knows about YOUR data
- Cite sources in responses
- Always up-to-date information
- Private data stays private

### Workshop Notebooks

All Part 2 content has companion Jupyter notebooks:

{{< cards >}}
  {{< card link="https://github.com/nishad/llm-workshop-notebooks" title="Workshop Notebooks" icon="document-text" subtitle="Clone the repository to follow along" >}}
{{< /cards >}}

```bash
# Clone the repository
git clone https://github.com/nishad/llm-workshop-notebooks.git
cd llm-workshop-notebooks

# Install dependencies
pip install -r requirements.txt

# Start Jupyter
jupyter notebook
```

### Get Started

Ready to start coding?

{{< cards >}}
  {{< card link="/v2/part2-intermediate/01-python-integration" title="Start with Python" icon="arrow-right" subtitle="Begin with Python integration" >}}
{{< /cards >}}
