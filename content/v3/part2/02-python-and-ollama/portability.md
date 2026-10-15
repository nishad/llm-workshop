---
title: Portability
weight: 2
---

Many tools speak the OpenAI API. Ollama answers it on port 11434 under `/v1`. The same code can therefore talk to Ollama, LM Studio, llama.cpp's server or a hosted provider by changing one thing: the base URL. This is section 01.06 of notebook 01.

## The same call through the OpenAI client

```python
from openai import OpenAI
oa = OpenAI(base_url=f"{settings.host}/v1", api_key="ollama")   # the key is required by the client but ignored by Ollama
completion = oa.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "Reply with one word: which city is the ETH Zurich in?"}],
    temperature=0,
)
print(completion.choices[0].message.content)
```

```text
Zurich
```

From the executed notebook 01, 15 October 2026.

## Base URLs

| Server | Base URL |
|---|---|
| Ollama | `http://localhost:11434/v1` |
| LM Studio | `http://localhost:1234/v1` |
| llama.cpp's server | `http://localhost:8080/v1` |
| The Llama app | `http://localhost:9931/v1` |
| A hosted provider | the URL and API key from the provider |

The `model` name is whatever the server calls the model. For a hosted provider, the key is real and your prompts leave your machine.

## What Ollama's endpoint does not support

Ollama's OpenAI-compatible endpoint is a subset of the API. Two limits matter for this workshop:

- `tool_choice` is ignored. You cannot force the model to call a particular tool.
- `logprobs` with tools returns an error.

For anything beyond plain chat, such as the tool use in notebook 05, the workshop uses Ollama's own client.

## Why this matters

Code written against one standard interface does not belong to one vendor. If a provider changes its terms or its prices, or a better local runtime appears, you change a URL and a model name, and your pipeline keeps running. That is the vendor independence from [Open models](/v3/part1/02-open-models) in practice. Test on a small model locally, and decide later where the production run happens.
