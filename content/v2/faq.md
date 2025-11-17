---
title: Frequently Asked Questions
weight: 40
---

## General Questions

### What is the difference between Llama 3.2 and other LLMs?

Llama 3.2 is Meta's latest open-source model family, optimized for efficiency and instruction-following. Key differences:

- **Open Source**: Free to use, runs locally
- **Efficient**: Smaller sizes (1B, 3B) run on consumer hardware
- **Long Context**: 128K token context window
- **Multilingual**: Supports 8 languages including German, French, Spanish
- **Vision Capable**: Some variants can process images

### Do I need a GPU to run Ollama?

**No!** Ollama works on CPU-only systems. A GPU (especially Apple Silicon or NVIDIA) will speed things up, but it's not required.

- **CPU-only**: Works fine, just slower
- **Apple Silicon (M1/M2/M3)**: Excellent performance
- **NVIDIA GPU**: Best performance with CUDA support

### How much does it cost to run models locally?

**Free!** After initial download:
- No per-token charges
- No subscription fees
- No API costs
- Only electricity (minimal)

**Cost**: Just your hardware and internet for downloading models.

### Can I use this for commercial projects?

Llama 3.2 licensing:
- **1B & 3B models**: Free for commercial use
- **Check license**: [Llama 3 Community License](https://www.llama.com/llama3/license/)
- **Ollama**: MIT licensed, free for commercial use
- **Your code**: You own it

---

## Technical Questions

### Why is my model slow?

**Speed depends on**:
- RAM available (more is better)
- CPU/GPU capabilities
- Model size (1B faster than 3B)
- Quantization level

**Try**:
- Close other applications
- Use llama3.2:1b instead of 3b
- Reduce context window
- Check system resources (Activity Monitor/Task Manager)

### Can I run multiple models simultaneously?

Yes, but it requires more RAM:
- Each model uses 2-6 GB RAM
- With 16 GB RAM, you can run 2-3 models
- Models share the Ollama server

### How do I update Ollama?

**macOS/Windows**:
- Download latest installer from ollama.com
- Run installer (keeps your models)

**Linux**:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### Where are models stored?

- **macOS**: `~/.ollama/models`
- **Linux**: `~/.ollama/models`
- **Windows**: `C:\Users\<username>\.ollama\models`

You can delete this folder to remove all models (will need to re-download).

---

## RAG & Embeddings

### What's the difference between embeddings and chat models?

| Feature | Embedding Model | Chat Model |
|---------|----------------|------------|
| Purpose | Convert text → vectors | Generate text responses |
| Output | Array of numbers | Natural language text |
| Example | nomic-embed-text | llama3.2 |
| Use | Semantic search, RAG | Conversations, Q&A |

**Don't mix them up!** Use embedding models for embeddings, chat models for generation.

### How many documents can ChromaDB handle?

- **Small scale**: 1,000s of documents (no problem)
- **Medium scale**: 10,000s (works well)
- **Large scale**: 100,000s+ (may need optimization)

For very large datasets, consider:
- Batch operations
- Approximate nearest neighbor algorithms
- Distributed vector databases (Weaviate, Qdrant)

### Do I need to re-generate embeddings when I add new documents?

**No!** Only new documents need embeddings:

```python
# Existing embeddings stay in database
collection = client.get_collection("my_docs")

# Only new docs get embedded
collection.add(documents=[new_doc], ids=[new_id])
```

### How do I choose chunk size for RAG?

**Guidelines**:
- **Too small** (<100 words): Loses context
- **Sweet spot** (200-500 words): Best for most cases
- **Too large** (>1000 words): Less precise retrieval

**Also consider**:
- Document type (code vs. prose)
- Overlap (10-20% helps continuity)
- Context window of embedding model

---

## Troubleshooting

### "Could not connect to Ollama server"

1. **Check if Ollama is running**:
   - Look for Ollama icon in system tray/menu bar
   - Or start it: open Ollama application

2. **Verify port**:
   ```bash
   curl http://localhost:11434/api/tags
   ```

3. **Check firewall**: Allow Ollama through firewall

4. **Restart Ollama**: Quit and reopen

See [Troubleshooting](/v2/part1-fundamentals/03-setup/troubleshooting) for more.

### Model download is very slow

**Try**:
- Check internet speed
- Use smaller model (llama3.2:1b)
- Download during off-peak hours
- Resume: Ollama resumes interrupted downloads

### Python can't find ollama module

```bash
# Install in current environment
pip install ollama

# Or with Python 3 specifically
python3 -m pip install ollama

# In virtual environment
source venv/bin/activate  # Activate first
pip install ollama
```

### ChromaDB persistence not working

Use absolute paths:

```python
import os

db_path = os.path.abspath("./my_chroma_db")
client = chromadb.PersistentClient(path=db_path)
```

---

## Workshop-Specific

### Can I share the workshop materials?

Yes! The workshop website and notebooks are open for sharing:
- Share the website URL
- Share the notebook repository
- Use materials for teaching (with attribution)

### I missed the live workshop. Can I still follow along?

Absolutely! The website is designed for self-paced learning:
- All content is available online
- Notebooks are fully documented
- No live session required

### Where can I get help after the workshop?

- **This website**: Reference anytime
- **GitHub Issues**: Report problems
- **Ollama Discord**: Community support
- **Stack Overflow**: Tag questions with `ollama`

---

## Privacy & Security

### Is my data safe with local LLMs?

Yes! Key privacy benefits:

✓ Data never leaves your computer
✓ No cloud services involved
✓ No tracking or logging (by Ollama)
✓ You control all data

**Perfect for**:
- Confidential documents
- Personal information
- Proprietary data
- GDPR/HIPAA compliance

### Can someone access my Ollama instance remotely?

By default, Ollama only listens on `localhost:11434` (local only).

**To allow remote access** (be careful!):
```bash
# Set environment variable
OLLAMA_HOST=0.0.0.0:11434 ollama serve
```

**Security tip**: Use firewall rules and authentication if exposing to network.

### Does Ollama collect any data?

Ollama respects privacy:
- No telemetry by default
- Models run entirely locally
- No data sent to Ollama servers (except for model downloads)

---

## Performance Optimization

### What's the fastest model for my hardware?

| RAM | Recommended | Notes |
|-----|-------------|-------|
| 8 GB | llama3.2:1b | Runs comfortably |
| 16 GB | llama3.2:3b | Good balance |
| 32 GB+ | llama3.2:3b or larger | Can run multiple models |

### How can I make responses faster?

1. **Use smaller model**: llama3.2:1b instead of 3b
2. **Reduce temperature**: Lower values = faster
3. **Limit max tokens**: Set `num_predict` parameter
4. **Close background apps**: Free up RAM
5. **Use SSD**: Faster model loading

### Should I use Q4 or Q5 quantization?

- **Q4_K_M** (default): Faster, smaller, good quality
- **Q5_K_M**: Slower, larger, better quality

**Recommendation**: Start with Q4_K_M (default). Only switch to Q5 if you have >16GB RAM and want maximum quality.

---

## Advanced Topics

### Can I fine-tune Llama 3.2?

Yes, but it's advanced:
- Requires significant RAM/GPU
- Use LoRA/QLoRA for efficiency
- Consider if RAG solves your problem first

**Resources**:
- [Hugging Face Fine-tuning Guide](https://huggingface.co/docs/transformers/training)
- [LlamaFactory](https://github.com/hiyouga/LLaMA-Factory)

### How do I deploy this in production?

For production deployments:

1. **Containerize**: Use Docker
2. **Add API**: Flask, FastAPI
3. **Monitor**: Prometheus, Grafana
4. **Scale**: Load balancing, caching
5. **Secure**: Authentication, rate limiting

**Tools to explore**:
- Docker
- FastAPI
- Redis (caching)
- Nginx (reverse proxy)

---

## Still Have Questions?

- **Check**: [Part 1](/v2/part1-fundamentals) or [Part 2](/v2/part2-intermediate) documentation
- **Search**: This website (use search feature)
- **Ask**: Ollama Discord or GitHub discussions
- **Email**: Workshop organizer

{{< callout type="info" >}}
**Didn't find your question?** Submit an issue on [GitHub](https://github.com/nishad/llm-workshop/issues) and we'll add it to the FAQ.
{{< /callout >}}
