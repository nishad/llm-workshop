---
title: Workshop Notebooks
weight: 3
---

## Jupyter Notebooks for Part 2

The workshop includes two comprehensive Jupyter notebooks that provide hands-on, executable examples of everything covered in Part 2.

{{< callout type="info" >}}
**Repository**: [github.com/nishad/llm-workshop-notebooks](https://github.com/nishad/llm-workshop-notebooks)
{{< /callout >}}

---

## Getting the Notebooks

### Clone the Repository

```bash
git clone https://github.com/nishad/llm-workshop-notebooks.git
cd llm-workshop-notebooks
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

**Contents of requirements.txt**:
```
ollama>=0.6.0
chromadb>=0.4.0
jinja2>=3.1.0
jupyter>=1.0.0
```

### Start Jupyter

```bash
jupyter notebook
```

This opens a browser window with the notebook interface.

---

## Notebook 1: Using Ollama with Python

**File**: `01_using-ollama-with-python.ipynb`

### Topics Covered

1. **Installation and Setup**
   - Installing the Ollama Python library
   - Verifying connection to Ollama
   - Checking available models

2. **Basic Text Generation**
   - Simple generate() examples
   - Controlling temperature and parameters
   - Understanding response structure

3. **Chat Interactions**
   - Multi-turn conversations
   - Message history management
   - Context preservation

4. **Streaming Responses**
   - Real-time text generation
   - Progress indicators
   - Handling streaming output

5. **Generating Embeddings**
   - Using nomic-embed-text
   - Understanding embedding dimensions
   - Measuring similarity

6. **Model Metadata**
   - Listing available models
   - Retrieving model information
   - Model management

### Key Code Examples

The notebook includes complete, runnable examples:

```python
# Example from notebook
import ollama

# Generate text
response = ollama.generate(
    model='llama3.2',
    prompt='Explain vector embeddings in simple terms.'
)

print(response['response'])

# Create embeddings
embedding = ollama.embed(
    model='nomic-embed-text',
    input='This is a test sentence.'
)

print(f"Embedding size: {len(embedding['embeddings'][0])}")
```

---

## Notebook 2: Introduction to RAG with Ollama

**File**: `02_introduction-to-rag-with-ollama.ipynb`

### Topics Covered

1. **RAG Fundamentals**
   - What is RAG and why use it
   - RAG vs. fine-tuning
   - When to use RAG

2. **ChromaDB Setup**
   - Installing and initializing ChromaDB
   - Creating collections
   - Persistent vs. in-memory databases

3. **Document Processing**
   - Loading documents
   - Chunking strategies
   - Generating and storing embeddings

4. **Retrieval Implementation**
   - Semantic search with ChromaDB
   - Similarity thresholds
   - Retrieving relevant chunks

5. **Prompt Templates with Jinja2**
   - Creating structured prompts
   - Including retrieved context
   - Template variables and loops

6. **Complete RAG Pipeline**
   - End-to-end workflow
   - Query processing
   - Response generation

7. **Comparison: With vs. Without RAG**
   - Side-by-side examples
   - Accuracy improvements
   - Source attribution

### Dataset Used

The notebook uses the **"Made with Creative Commons"** dataset:
- Real-world examples of Creative Commons usage
- Diverse document types
- Licensed under Creative Commons Attribution

### Key Code Examples

```python
# Example from notebook
import chromadb
import ollama
from jinja2 import Template

# Setup ChromaDB
client = chromadb.PersistentClient(path="./rag_demo")
collection = client.get_or_create_collection(name="creative_commons")

# Add documents
documents = [
    "Creative Commons licenses allow sharing and reuse...",
    "There are six main Creative Commons licenses...",
    # ... more documents
]

collection.add(
    documents=documents,
    ids=[f"doc_{i}" for i in range(len(documents))]
)

# Query
question = "What are Creative Commons licenses?"

# Retrieve context
results = collection.query(
    query_texts=[question],
    n_results=3
)

# Generate answer
template = Template("""
Context: {{ context }}

Question: {{ question }}

Answer:
""")

prompt = template.render(
    context=results['documents'][0],
    question=question
)

response = ollama.generate(model='llama3.2', prompt=prompt)
print(response['response'])
```

---

## Running the Notebooks

### Prerequisites

Before running the notebooks, ensure:

- [ ] Ollama is installed and running
- [ ] Llama 3.2 model is downloaded (`ollama pull llama3.2`)
- [ ] nomic-embed-text is downloaded (`ollama pull nomic-embed-text`)
- [ ] Python environment is set up with required packages

### Tips for Workshop

1. **Run Cells Sequentially**: Each cell builds on previous ones
2. **Experiment**: Try different prompts and parameters
3. **Take Notes**: Add markdown cells with your observations
4. **Save Often**: Jupyter auto-saves, but save manually too
5. **Clear Output**: Kernel → Restart & Clear Output for a fresh start

---

## Exercises in Notebooks

Both notebooks include exercises to practice:

### Notebook 1 Exercises

- Modify temperature settings and observe changes
- Create embeddings for different texts and compare
- Build a simple similarity search function
- Implement streaming with custom formatting

### Notebook 2 Exercises

- Add your own documents to the knowledge base
- Experiment with different chunk sizes
- Create custom prompt templates
- Compare RAG responses with non-RAG responses

---

## Additional Resources

The repository also includes:

- **README.md**: Setup instructions and overview
- **requirements.txt**: All necessary dependencies
- **sample_data/**: Example documents for RAG
- **utils/**: Helper functions for common tasks

---

## License and Attribution

- **Repository License**: MIT License
- **Dataset**: "Made with Creative Commons" (CC Attribution)
- **Code**: Free to use and modify

### Documentation Links

- [Ollama Python Library](https://github.com/ollama/ollama-python)
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [Jinja2 Documentation](https://jinja.palletsprojects.com/)

---

## Troubleshooting Notebooks

### Common Issues

**Kernel won't start**:
```bash
pip install --upgrade jupyter ipykernel
python -m ipykernel install --user
```

**ImportError: No module named 'ollama'**:
```bash
pip install ollama
# Or within notebook:
!pip install ollama
```

**ChromaDB persistence issues**:
```python
# Use absolute path
import os
db_path = os.path.abspath("./chroma_db")
client = chromadb.PersistentClient(path=db_path)
```

---

## Next Steps

After completing the notebooks:

{{< cards >}}
  {{< card link="/v2/resources" title="Resources" icon="book-open" subtitle="Additional materials and next steps" >}}
{{< /cards >}}

{{< callout type="success" >}}
**Congratulations!** You've completed Part 2 of the workshop. You now have practical experience with Python integration, vector embeddings, semantic search, and RAG systems!
{{< /callout >}}
