---
title: Download the models in advance
weight: 5
---

Download your model before the workshop. First find your tier on [Choose a model size for your hardware](/v3/before-you-start/hardware): 16 GB or more uses the 8B, 8 GB uses the 4B. Then follow the tab for the tool you installed.

{{< tabs >}}

{{< tab name="Ollama" >}}
**16 GB or more (8B)**

1. In the Ollama app, open the model picker and type exactly `nishad/apertus:8b`.
2. Select the entry with the download arrow and send any message. The download bar appears in the chat.

Typing `apertus` alone shows "No models found". Always type the full tag.

Terminal alternative:

```bash
ollama pull nishad/apertus:8b
```

**8 GB (4B)**

Do the same with `nishad/apertus:4b` (2.4 GB), or `ollama pull nishad/apertus:4b`.

**Optional preview**

`nishad/apertus:8b-v1.5-preview` is a community conversion for the curious.

**Embeddings for Part 2**

Part 2 needs an embedding model. This step works in the terminal only:

```bash
ollama pull qwen3-embedding:0.6b
```

It is 639 MB.
{{< /tab >}}

{{< tab name="LM Studio" >}}
**16 GB or more (8B)**

1. Open Discover and paste `https://huggingface.co/unsloth/Apertus-8B-Instruct-2509-GGUF`.
2. Choose **Q4_K_M** (5.06 GB) and click Download.

**8 GB (4B)**

Paste `https://huggingface.co/jondale/Apertus-v1.1-4B-Instruct-GGUF` and choose **Q4_K_M** (2.43 GB).

**Alternative**

On the Hugging Face page, the "Use this model" button has an LM Studio entry.
{{< /tab >}}

{{< /tabs >}}

## Sizes and budget

| Item | Size |
|---|---|
| Ollama install (Windows) | about 4 GB |
| `nishad/apertus:8b` | 5.1 GB |
| `nishad/apertus:4b` | 2.4 GB |
| `qwen3-embedding:0.6b` | 639 MB |
| Python environment | about 0.5 GB |

The total stays well under the 20 GB prerequisite. At 20 Mbit/s the 8B takes about 35 minutes.

## If you are short on time in Part 2

Notebook 03 builds two vector indexes: about 20,000 STW labels and the UNESCO English labels. This takes a few minutes on Apple Silicon and much longer on a CPU-only laptop. Prebuilt files will be linked here the week before the workshop (link to follow):

- `stw-de-labels.sqlite` (86 MB)
- `unesco-en-labels.sqlite` (34 MB)

Put them in the `runs/` folder of the notebooks repository.

## Offline alternative

{{< details title="Show the offline options" >}}
Copy the `manifests` and `blobs` folders from `~/.ollama/models` on a colleague's machine into your own models folder. Or point Settings, then Model location, at a USB stick.

Another route is to build the tag from a GGUF file, using the Modelfile from the `models/` folder of the notebooks repository:

```bash
ollama create nishad/apertus:8b -f Modelfile
```
{{< /details >}}

## Verify

Send this message:

> Reply with the word OK and the model name you think you are.

Read the answer. Then check the list:

```bash
ollama list
```

It shows the tag. In LM Studio the model appears under My Models.

## Digests and sources

| Tag | Source GGUF | GGUF sha256 | Digest (`ollama list`) |
|---|---|---|---|
| `nishad/apertus:8b` (also `:latest`) | `unsloth/Apertus-8B-Instruct-2509-GGUF`, Q4_K_M | `87e7f0eb5a1d33e1a8ea4e7fdd2363764e0465061dd92962e0073aec31a7944d` | `4a85a6fea0b8` |
| `nishad/apertus:4b` | `jondale/Apertus-v1.1-4B-Instruct-GGUF`, Q4_K_M | not recorded | `87ca69a79aed` |
| `nishad/apertus:8b-v1.5-preview` | `Colby/apertus-v1.5-8b-text-Q4_K_M-GGUF`, Q4_K_M | `a037df8d87ff6caacee794ee85f55342f2152e0d359b7389033300c3bee5f299` | `6f25f6ba0b62` |
