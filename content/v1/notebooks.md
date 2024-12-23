---
title: Workshop Notebooks
weight: 6
---

**Notebooks for this workshop are available in the repository [https://github.com/nishad/llm-workshop-notebooks](https://github.com/nishad/llm-workshop-notebooks).**


## Notebooks

#### 1. `01_using-ollama-with-python.ipynb`
This notebook introduces the **Ollama** Python library and provides a step-by-step guide on:
- Installing and setting up Ollama.
- Interacting with models for text generation and embedding creation.
- Retrieving and understanding metadata of available models.
- Streaming dynamic Markdown responses.

#### 2. `02_introduction-to-rag-with-ollama.ipynb`
This notebook demonstrates how to implement a **Retrieval-Augmented Generation (RAG)** pipeline using:
- **ChromaDB** for embedding storage and retrieval.
- **Jinja2** for creating structured prompts.
- **Ollama** for embedding generation and context-aware responses.

Topics covered include:
- Setting up a persistent vector database to avoid re-indexing data.
- Retrieving relevant paragraphs for context-aware prompts.
- Comparing model outputs with and without external knowledge augmentation.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/nishad/llm-workshop-notebooks
   ```
2. Navigate to the repository:
   ```bash
   cd llm-workshop-notebooks
   ```
3. Install required packages:
   ```bash
   pip install jupyter
   ```
4. Open the notebooks in Jupyter Notebook or JupyterLab:
   ```bash
   jupyter notebook
   ```
5. Follow the notebooks:
   - Start with `01_using-ollama-with-python.ipynb` for basic concepts.
   - Proceed to `02_introduction-to-rag-with-ollama.ipynb` for advanced RAG workflows.

## Resources

- [Ollama Python Library Documentation](https://github.com/ollama/ollama-python)
- [ChromaDB](https://www.trychroma.com/)
- [Jinja2 Documentation](https://jinja.palletsprojects.com/)
- [Creative Commons: Made with Creative Commons](https://creativecommons.org/share-your-work/made-with-cc/)

## License

This repository is licensed under the MIT License. The dataset used in the examples is sourced from **"Made with Creative Commons"** and is licensed under Creative Commons Attribution.
