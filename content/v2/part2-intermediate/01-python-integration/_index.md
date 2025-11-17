---
title: Python Integration
weight: 1
cascade:
  type: docs
sidebar:
  open: true
---

## Automating LLM Interactions with Python

In Part 1, you interacted with Ollama through its GUI. Now we'll use Python to automate and script LLM interactions, enabling powerful workflows and batch processing.

### Why Python Integration?

**Manual Approach** (GUI):
- Great for exploration and testing
- One prompt at a time
- Manual copy/paste
- Limited to what the GUI offers

**Programmatic Approach** (Python):
- Process hundreds/thousands of items
- Consistent, repeatable workflows
- Integration with databases, APIs, files
- Custom applications and tools
- Automated data analysis

### What You'll Learn

{{< cards >}}
  {{< card link="/v2/part2-intermediate/01-python-integration/setup" title="Setup" subtitle="Install and configure Ollama Python library" >}}
  {{< card link="/v2/part2-intermediate/01-python-integration/basics" title="Basics" subtitle="Generate text, chat, and create embeddings" >}}
  {{< card link="/v2/part2-intermediate/01-python-integration/examples" title="Examples" subtitle="Practical automation scripts" >}}
{{< /cards >}}

### The Ollama Python Library

The official `ollama` Python library provides:

- **Simple API**: Easy-to-use functions
- **Streaming Support**: Real-time response generation
- **Model Management**: List, pull, remove models programmatically
- **Embeddings**: Generate vector embeddings
- **Async Support**: Concurrent operations

**Installation**:
```bash
pip install ollama
```

**Current Version**: 0.6.1 (as of 2025)

### Quick Example

Here's what Python + Ollama looks like:

```python
import ollama

# Generate text
response = ollama.generate(
    model='llama3.2',
    prompt='Explain quantum computing in one sentence.'
)

print(response['response'])
```

That's it! Simple and powerful.

### What You Can Build

With Python + Ollama, you can create:

**Document Processing**:
- Summarize hundreds of PDFs
- Extract structured data from text
- Classify documents automatically
- Generate metadata for archives

**Data Analysis**:
- Analyze survey responses
- Extract insights from research data
- Generate reports automatically
- Clean and normalize text data

**Custom Applications**:
- Chatbots for specific domains
- Question-answering systems
- Content generation tools
- Educational applications

**Research Workflows**:
- Automated literature review
- Coding assistance
- Data exploration
- Hypothesis generation

### Prerequisites

Before starting, ensure you have:

- [ ] Python 3.8 or later installed
- [ ] Ollama running with Llama 3.2 model
- [ ] Basic Python knowledge
- [ ] Text editor or IDE (VS Code, PyCharm, etc.)

### Notebook Available

The companion Jupyter notebook for this section:

**`01_using-ollama-with-python.ipynb`**

Contents:
- Installation and setup
- Basic text generation
- Chat interactions
- Streaming responses
- Generating embeddings
- Model metadata

{{< callout type="info" >}}
**Follow Along**: Open the notebook while reading this section. The notebook has runnable code you can experiment with.
{{< /callout >}}

### Ready to Start?

Let's begin with setup:

{{< cards >}}
  {{< card link="/v2/part2-intermediate/01-python-integration/setup" title="Setup Guide" icon="arrow-right" subtitle="Install and configure Python environment" >}}
{{< /cards >}}
