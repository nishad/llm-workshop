---
title: Python Basics with Ollama
weight: 2
---

## Using the Ollama Python Library

Learn the core functions of the Ollama Python library through practical examples.

---

## Core Functions Overview

The `ollama` library provides these main functions:

| Function | Purpose |
|----------|---------|
| `ollama.generate()` | Generate text from a prompt |
| `ollama.chat()` | Multi-turn conversations |
| `ollama.embed()` | Create vector embeddings |
| `ollama.list()` | List available models |
| `ollama.pull()` | Download models |
| `ollama.show()` | Get model information |

---

## 1. Basic Text Generation

The simplest way to generate text:

```python
import ollama

response = ollama.generate(
    model='llama3.2',
    prompt='Explain what a vector database is in one sentence.'
)

print(response['response'])
```

**Output**:
```
A vector database is a specialized database system designed to store and efficiently
query high-dimensional vector data, commonly used for similarity search and retrieval
of semantically similar items.
```

### Response Structure

The response is a dictionary with these keys:

```python
{
    'model': 'llama3.2',
    'created_at': '2025-01-15T10:30:00.123Z',
    'response': 'The generated text...',
    'done': True,
    'context': [...],  # Token context
    'total_duration': 1234567890,
    'load_duration': 123456,
    'prompt_eval_count': 15,
    'eval_count': 42,
    'eval_duration': 987654321
}
```

---

## 2. Streaming Responses

For real-time output (like in the GUI):

```python
import ollama

stream = ollama.generate(
    model='llama3.2',
    prompt='Write a short poem about libraries.',
    stream=True
)

for chunk in stream:
    print(chunk['response'], end='', flush=True)

print()  # New line at the end
```

**Output** (appears word-by-word):
```
Books line the shelves in rows so neat,
A quiet haven, knowledge complete,
Whispers of stories, old and new,
The library waits to welcome you.
```

---

## 3. Chat Conversations

Multi-turn conversations with message history:

```python
import ollama

messages = [
    {
        'role': 'user',
        'content': 'What is RAG in the context of LLMs?'
    }
]

response = ollama.chat(
    model='llama3.2',
    messages=messages
)

print(response['message']['content'])

# Continue the conversation
messages.append(response['message'])
messages.append({
    'role': 'user',
    'content': 'Can you give me a concrete example?'
})

response = ollama.chat(model='llama3.2', messages=messages)
print(response['message']['content'])
```

### Message Format

Messages have two required fields:

```python
{
    'role': 'user' or 'assistant',  # Who is speaking
    'content': 'The message text'    # What they said
}
```

---

## 4. Generating Embeddings

Create vector representations of text:

```python
import ollama

response = ollama.embed(
    model='nomic-embed-text',  # Specialized embedding model
    input='Libraries are important for communities.'
)

embedding = response['embeddings'][0]
print(f"Embedding dimensions: {len(embedding)}")
print(f"First 5 values: {embedding[:5]}")
```

**Output**:
```
Embedding dimensions: 1024
First 5 values: [0.023, -0.156, 0.891, -0.234, 0.445]
```

{{< callout type="info" >}}
**Embedding Models**: Use specialized models like `nomic-embed-text` for embeddings, not chat models like `llama3.2`. Embedding models are optimized for creating semantic vectors.
{{< /callout >}}

---

## 5. Model Management

List, download, and inspect models programmatically:

### List Models

```python
import ollama

models = ollama.list()

for model in models['models']:
    print(f"{model['name']}: {model['size'] / 1e9:.2f} GB")
```

### Download a Model

```python
import ollama

# Download a model (like ollama pull)
ollama.pull('llama3.2:1b')
```

### Get Model Information

```python
import ollama

info = ollama.show('llama3.2')

print(f"Model: {info['details']['family']}")
print(f"Parameters: {info['details']['parameter_size']}")
print(f"Quantization: {info['details']['quantization_level']}")
```

---

## 6. Advanced Options

Control model behavior with parameters:

```python
import ollama

response = ollama.generate(
    model='llama3.2',
    prompt='Write a creative story opening.',
    options={
        'temperature': 0.9,      # Higher = more creative
        'top_p': 0.9,            # Nucleus sampling
        'top_k': 40,             # Consider top K tokens
        'num_predict': 100,      # Max tokens to generate
        'stop': ['\n\n']         # Stop sequences
    }
)

print(response['response'])
```

### Common Options

| Option | Description | Default | Range |
|--------|-------------|---------|-------|
| `temperature` | Randomness/creativity | 0.7 | 0.0-2.0 |
| `top_p` | Nucleus sampling threshold | 0.9 | 0.0-1.0 |
| `top_k` | Number of tokens to consider | 40 | 1-100 |
| `num_predict` | Max tokens to generate | -1 (unlimited) | any int |
| `stop` | Stop sequences | None | list of strings |
| `repeat_penalty` | Penalty for repetition | 1.1 | 1.0-2.0 |

---

## 7. Error Handling

Always handle potential errors:

```python
import ollama

try:
    response = ollama.generate(
        model='llama3.2',
        prompt='Hello!'
    )
    print(response['response'])

except ollama.ResponseError as e:
    print(f"Ollama error: {e}")

except ConnectionError:
    print("Could not connect to Ollama. Is it running?")

except Exception as e:
    print(f"Unexpected error: {e}")
```

---

## 8. Complete Example: Document Summarizer

Putting it all together:

```python
import ollama

def summarize_document(text, max_words=100):
    """Summarize a document using Ollama.

    Args:
        text: The document text to summarize
        max_words: Maximum words in summary

    Returns:
        str: The summary
    """
    prompt = f"""Summarize the following text in no more than {max_words} words.
    Focus on the main points only.

    Text:
    {text}

    Summary:"""

    try:
        response = ollama.generate(
            model='llama3.2',
            prompt=prompt,
            options={
                'temperature': 0.3,  # Low for consistent summaries
                'num_predict': max_words * 2  # Rough token estimate
            }
        )
        return response['response'].strip()

    except Exception as e:
        return f"Error: {e}"

# Example usage
document = """
Libraries have been central to communities for centuries, serving as repositories
of knowledge and centers of learning. In the digital age, their role has evolved
significantly. Modern libraries offer not just books, but digital resources,
maker spaces, community programs, and technology access. They bridge the digital
divide by providing free internet and computer access to those who might not
have it at home. Libraries also serve as quiet study spaces, meeting rooms,
and cultural centers hosting events and exhibitions.
"""

summary = summarize_document(document, max_words=50)
print("Summary:")
print(summary)
```

**Output**:
```
Summary:
Libraries have evolved from book repositories to multifaceted community hubs offering
digital resources, technology access, and cultural programs. They bridge the digital
divide and serve as vital spaces for learning, working, and community engagement in
the modern era.
```

---

## Best Practices

### 1. Reuse Connections

Don't create new connections for each request - the library handles this efficiently:

```python
# Good
for doc in documents:
    summary = ollama.generate(model='llama3.2', prompt=f"Summarize: {doc}")
```

### 2. Handle Long Texts

Break long texts into chunks if needed:

```python
def chunk_text(text, max_length=2000):
    """Split text into chunks."""
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0

    for word in words:
        current_chunk.append(word)
        current_length += len(word) + 1

        if current_length >= max_length:
            chunks.append(' '.join(current_chunk))
            current_chunk = []
            current_length = 0

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

### 3. Save API Responses

Cache responses to avoid re-processing:

```python
import json

def save_response(response, filename):
    """Save Ollama response to file."""
    with open(filename, 'w') as f:
        json.dump(response, f, indent=2)

def load_response(filename):
    """Load saved response."""
    with open(filename, 'r') as f:
        return json.load(f)
```

### 4. Use Appropriate Temperature

```python
# Factual tasks - low temperature
factual = ollama.generate(
    model='llama3.2',
    prompt='What is the capital of France?',
    options={'temperature': 0.1}
)

# Creative tasks - higher temperature
creative = ollama.generate(
    model='llama3.2',
    prompt='Write a creative story opening.',
    options={'temperature': 0.9}
)
```

---

## Quick Reference

**Generate text**:
```python
ollama.generate(model='llama3.2', prompt='...')
```

**Chat conversation**:
```python
ollama.chat(model='llama3.2', messages=[...])
```

**Create embeddings**:
```python
ollama.embed(model='nomic-embed-text', input='...')
```

**Stream output**:
```python
ollama.generate(model='llama3.2', prompt='...', stream=True)
```

---

## Next: Practical Examples

Ready to build real applications?

{{< cards >}}
  {{< card link="/v2/part2-intermediate/01-python-integration/examples" title="Practical Examples" icon="arrow-right" subtitle="Build useful automation scripts" >}}
{{< /cards >}}
