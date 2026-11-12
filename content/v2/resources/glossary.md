---
title: Glossary
weight: 2
---

## Key Terms

### A

**API (Application Programming Interface)**
: A set of functions and protocols for building software applications. Ollama provides an API for programmatic access.

### C

**Chat Model**
: A language model optimized for conversational interactions (e.g., Llama 3.2).

**ChromaDB**
: An open-source vector database for storing and querying embeddings.

**Context Window**
: The maximum amount of text (in tokens) a model can process at once. Llama 3.2 has a 128K token context window.

**Cosine Similarity**
: A metric for measuring similarity between two vectors, commonly used with embeddings.

### E

**Embedding**
: A numerical representation of text that captures semantic meaning. Typically a high-dimensional vector.

**Embedding Model**
: A specialized model for converting text into embeddings (e.g., nomic-embed-text).

### F

**Few-Shot Learning**
: Providing a model with a few examples to guide its behavior on a task.

**Fine-Tuning**
: Training a pre-trained model on specific data to specialize it for a task.

### G

**GUI (Graphical User Interface)**
: Visual interface for interacting with software. Ollama now includes a native GUI.

### H

**Hallucination**
: When an LLM generates plausible-sounding but incorrect information.

### I

**Inference**
: The process of using a trained model to generate predictions or responses.

### L

**LLM (Large Language Model)**
: A neural network model trained on vast amounts of text data to understand and generate human language.

### M

**Model Parameters**
: Internal weights learned during training that determine model behavior. Llama 3.2 has 1B or 3B parameters.

### N

**nomic-embed-text**
: An embedding model with 1,024 dimensions, optimized for semantic search.

### O

**Ollama**
: An open-source tool for running LLMs locally on personal hardware.

### P

**Prompt**
: The input text provided to an LLM to generate a response.

**Prompt Engineering**
: The practice of crafting effective prompts to get desired outputs from LLMs.

### Q

**Quantization**
: Reducing the numerical precision of model weights to decrease model size and memory usage.

### R

**RAG (Retrieval-Augmented Generation)**
: A technique that combines information retrieval with text generation to produce more accurate, grounded responses.

**Retriever**
: The component in RAG that finds relevant documents based on a query.

### S

**Semantic Search**
: Searching for information based on meaning and context rather than exact keyword matches.

**Streaming**
: Generating and displaying model output in real-time as it's produced.

**System Prompt**
: An instruction given to a model to define its role or behavior for a conversation.

### T

**Temperature**
: A parameter controlling randomness in model outputs. Lower = more deterministic, higher = more creative.

**Token**
: The smallest unit of text processed by an LLM. Can be a word, part of a word, or punctuation.

**Tokenization**
: The process of breaking text into tokens.

**Top-K**
: Limiting the model to consider only the top K most likely next tokens.

**Top-P (Nucleus Sampling)**
: Selecting from the smallest set of tokens whose cumulative probability exceeds P.

### V

**Vector**
: An array of numbers. Embeddings are represented as high-dimensional vectors.

**Vector Database**
: A database optimized for storing and querying vector embeddings.

### Z

**Zero-Shot Learning**
: Asking a model to perform a task without providing examples, relying on its training.

---

## Common Abbreviations

- **AI**: Artificial Intelligence
- **ANN**: Approximate Nearest Neighbor
- **API**: Application Programming Interface
- **BERT**: Bidirectional Encoder Representations from Transformers
- **CLI**: Command-Line Interface
- **GPU**: Graphics Processing Unit
- **GUI**: Graphical User Interface
- **LLM**: Large Language Model
- **ML**: Machine Learning
- **NLP**: Natural Language Processing
- **RAG**: Retrieval-Augmented Generation
- **RAM**: Random Access Memory

---

## Units and Measurements

**B** (Billion): 1,000,000,000 (e.g., 3B parameters)

**GB** (Gigabyte): ~1 billion bytes of storage

**K** (Thousand): 1,000 (e.g., 128K tokens = 128,000 tokens)

**ms** (Millisecond): 1/1,000 of a second

**Tokens/Second**: Speed metric for text generation
