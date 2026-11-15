---
title: Download the models
weight: 5
---

Download the model for your machine. First find your tier on [Choose a model size for your hardware](/v3/before-you-start/hardware). The tier depends on your computer's memory. With 16 GB or more you use the 8B model, and with 8 GB you use the 4B model. Then follow the tab for the tool you installed, Ollama or LM Studio.

{{< tabs >}}

{{< tab name="Ollama" >}}
**16 GB or more (8B)**

1. In the Ollama app, open the model picker and type exactly `thalhath/apertus:8b`.
2. Select the entry with the download arrow and send any message. The download bar appears in the chat.

Typing `apertus` alone shows "No models found". Always type the full tag, which is the model's complete name.

Or run this in a terminal:

```bash
ollama pull thalhath/apertus:8b
```

**8 GB (4B)**

Do the same with `thalhath/apertus:4b` (2.4 GB), or run `ollama pull thalhath/apertus:4b` in a terminal.

**Optional preview**

If you want to compare, `thalhath/apertus:8b-v1.5-preview` is the newer Apertus v1.5, converted for local use by a community member. Nothing in the workshop needs it.

**Embeddings for Part 2**

Part 2 also needs an embedding model. This second model does not write answers. It turns text into lists of numbers that represent the text's meaning, and Part 2 uses those numbers for searching. This step works in the terminal only:

```bash
ollama pull qwen3-embedding:0.6b
```

It is 639 MB.
{{< /tab >}}

{{< tab name="LM Studio" >}}
**16 GB or more (8B)**

1. Open Discover (the magnifying glass) and paste `https://huggingface.co/unsloth/Apertus-8B-Instruct-2509-GGUF`.
2. Choose **Q4_K_M** (5.06 GB) and click Download. Q4_K_M is a quantization label. Quantization shrinks a model file by storing its numbers with less precision.

**8 GB (4B)**

Paste `https://huggingface.co/jondale/Apertus-v1.1-4B-Instruct-GGUF` and choose **Q4_K_M** (2.43 GB).

**Alternative**

In your browser, open the model's page on Hugging Face (the website where most open models are published). Click the "Use this model" button and choose the LM Studio entry.
{{< /tab >}}

{{< /tabs >}}

## Sizes and budget

| Item | Size |
|---|---|
| Ollama install (Windows) | about 4 GB |
| `thalhath/apertus:8b` | 5.1 GB |
| `thalhath/apertus:4b` | 2.4 GB |
| `qwen3-embedding:0.6b` | 639 MB |
| Python environment | about 0.5 GB |

The total stays well under the 20 GB of free disk space we ask for. On a 20 Mbit/s connection, the 8B model takes about 35 minutes to download.

## Two index files for Part 2

Notebook 03 needs two vector index files, `stw-de-labels.sqlite` (85.7 MB) and `unesco-en-labels.sqlite` (34.4 MB). A vector index stores the lists of numbers that an embedding model makes from each text. It can then find texts with similar meanings quickly. Building these two yourself is slow on most laptops, so download the prebuilt files instead. Download them from the [swib26 release](https://github.com/nishad/llm-workshop-notebooks/releases/tag/swib26) of the notebooks repository; the direct links are in step 4 of [Before you start](/v3/before-you-start#4-part-2-only-python-and-the-notebooks). Put them in the `runs/` folder of the notebooks repository. To confirm that the files arrived complete and unchanged, use the checksums and the command on the [environment page](/v3/part2/01-environment#download-the-prebuilt-index-files).

## If Ollama cannot find the tag

The workshop tags are built from model files on Hugging Face. If `ollama pull thalhath/apertus:8b` says that the model was not found, build the same tag yourself from its Modelfile, a short text file that tells Ollama which file to download and how to set it up. Run these two lines in a terminal. In Windows PowerShell, write `curl.exe` instead of `curl`.

```bash
curl -LO https://llm-workshop.thalhath.org/models/apertus-8b.Modelfile
ollama create thalhath/apertus:8b -f apertus-8b.Modelfile
```

On an 8 GB machine:

```bash
curl -LO https://llm-workshop.thalhath.org/models/apertus-4b.Modelfile
ollama create thalhath/apertus:4b -f apertus-4b.Modelfile
```

Ollama downloads the model file from Hugging Face by itself. The result is the same model with the same digest as the published tag, and everything else in the workshop works unchanged.

## Offline alternative

{{< details title="Show the offline options" >}}
Copy the `manifests` and `blobs` folders from `~/.ollama/models` on a colleague's machine into your own models folder. Or open Settings, then Model location, and select a USB stick that holds a copy of those folders.

Another option is to create the tag yourself from a GGUF file, the single-file format used for local models. Use the Modelfiles from the section above; they are also in the `models/` folder of the notebooks repository:

```bash
ollama create thalhath/apertus:8b -f Modelfile
```
{{< /details >}}

## Verify

Open a chat with the model you downloaded and send this message:

> Reply with the word OK and the model name you think you are.

Read the answer. Then, if you use Ollama, run this in a terminal to list your models:

```bash
ollama list
```

Your tag should be in the list. In LM Studio, the model appears under My Models instead.

## Digests and sources

A digest is a code computed from the model's contents; it identifies the exact file you downloaded, and `ollama list` shows its first 12 characters. Two tags with the same digest are the same model.

| Tag | Source GGUF | GGUF sha256 | Digest (`ollama list`) |
|---|---|---|---|
| `thalhath/apertus:8b` (also `:latest`) | `unsloth/Apertus-8B-Instruct-2509-GGUF`, Q4_K_M | `87e7f0eb5a1d33e1a8ea4e7fdd2363764e0465061dd92962e0073aec31a7944d` | `4a85a6fea0b8` |
| `thalhath/apertus:4b` | `jondale/Apertus-v1.1-4B-Instruct-GGUF`, Q4_K_M | not recorded | `87ca69a79aed` |
| `thalhath/apertus:8b-v1.5-preview` | `Colby/apertus-v1.5-8b-text-Q4_K_M-GGUF`, Q4_K_M | `a037df8d87ff6caacee794ee85f55342f2152e0d359b7389033300c3bee5f299` | `6f25f6ba0b62` |
