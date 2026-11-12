---
title: Model Guide
weight: 1
---

## Llama 3.2 Models

### Text Models

**llama3.2:3b** (Default - Recommended for Workshop)
- **Size**: 2.0 GB download
- **Parameters**: 3 billion
- **Context**: 128K tokens
- **RAM**: 4-6 GB required
- **Use Cases**: General purpose, instruction following, summarization
- **Download**: `ollama pull llama3.2`

**llama3.2:1b** (Faster Alternative)
- **Size**: 1.3 GB download
- **Parameters**: 1 billion
- **Context**: 128K tokens
- **RAM**: 2-3 GB required
- **Use Cases**: Quick responses, resource-constrained systems
- **Download**: `ollama pull llama3.2:1b`

### Vision Models (Advanced)

**llama3.2-vision:11b**
- **Size**: 7.9 GB download
- **Capabilities**: OCR, image analysis, visual Q&A
- **RAM**: 8+ GB required
- **Download**: `ollama pull llama3.2-vision`

---

## Embedding Models

**nomic-embed-text** (Recommended)
- **Dimensions**: 1,024
- **Context**: 8,192 tokens
- **Size**: 274 MB
- **Use**: Semantic search, RAG
- **Download**: `ollama pull nomic-embed-text`

**mxbai-embed-large** (Alternative)
- **Dimensions**: 1,024
- **Size**: 669 MB
- **Use**: High-quality embeddings
- **Download**: `ollama pull mxbai-embed-large`

---

## Other Useful Models

**codellama:7b** (Code Generation)
```bash
ollama pull codellama:7b
```

**mistral:7b** (Alternative LLM)
```bash
ollama pull mistral:7b
```

**llama3.1:8b** (Previous Version)
```bash
ollama pull llama3.1:8b
```

---

## Choosing the Right Model

| Scenario | Recommended Model |
|----------|-------------------|
| Workshop learning | llama3.2:3b |
| Low RAM (<8 GB) | llama3.2:1b |
| Code generation | codellama:7b |
| Embeddings/RAG | nomic-embed-text |
| Multilingual | llama3.2:3b |
| Image analysis | llama3.2-vision:11b |

---

## Model Management

**List installed models**:
```bash
ollama list
```

**Remove a model**:
```bash
ollama rm llama3.2:1b
```

**Update a model**:
```bash
ollama pull llama3.2  # Downloads latest version
```

**Check model details**:
```bash
ollama show llama3.2
```

---

## Quantization Levels

Models are available in different quantizations (size vs. quality trade-offs):

- **Q4_K_M**: Default, balanced (recommended)
- **Q5_K_M**: Larger, better quality
- **Q2_K**: Smallest, lower quality

**Example**:
```bash
ollama pull llama3.2:3b-q5_k_m  # Higher quality quantization
```

See [Quantization](/v2/part1-fundamentals/02-concepts/quantization) for more details.
