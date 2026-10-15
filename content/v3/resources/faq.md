---
title: FAQ
weight: 6
---

## General

### Is it really free?

Yes. The models, the runtimes and the workshop materials cost nothing. You pay only for your own electricity and storage.

### Do I need a GPU?

No. The models run on an ordinary laptop. Memory matters more than a graphics card; see the tier table on [Choose a model size for your hardware](/v3/before-you-start/hardware).

### Can I use it for work?

Yes, for local use. The Apertus Acceptable Use Policy applies, so read it if you plan to redistribute outputs or the model.

## Models

### Is Apertus open source?

It is fully open: the weights, training code, reconstruction scripts for the data and intermediate checkpoints are published, under Apache-2.0 with an acceptable-use policy. Whether the acceptable-use policy fits the Open Source Definition is an open question. The openness ladder is in Part 1.

### Why not Llama?

Meta's Llama models are open weights under a custom license, with restrictions on use, and an exclusion for the EU on its multimodal models. That puts them on tier 1 of the openness ladder, two tiers below Apertus, and their training data is closed.

### Why is the 8B not for 8 GB machines?

The file alone is 5.06 GB and the context needs more memory on top. On 8 GB the system swaps to disk and every answer takes minutes. Use the 4B. See [Model guide](/v3/resources/models).

### What is the v1.5 preview?

An unofficial community conversion of Apertus v1.5, text only, with no parity check against the original. It is optional and for machines with 16 GB or more. Details are on the [Model guide](/v3/resources/models).

## Runtimes

### Ollama or LM Studio?

Either works for Part 1. Part 2 needs Ollama, because the notebooks talk to it.

### Does Ollama send my prompts anywhere?

No. Prompts stay on your machine. See [Privacy](/v3/before-you-start/privacy) for the model-name check and the Cloud switch.

### Where are models stored?

Ollama keeps them in `~/.ollama/models` on macOS and Linux and in `%USERPROFILE%\.ollama\models` on Windows. See [Install Ollama](/v3/before-you-start/install-ollama).

## Part 2

### Why Python 3.12?

The notebooks' environment is pinned to Python 3.12 or 3.13, the versions they were written and tested on. uv installs one for you, so your system Python does not matter.

### Why not chromadb?

It pulls in about 250 MB of dependencies and has an open Windows install issue. The notebooks use numpy and sqlite-vec instead, a 0.2 MB package.

### What if a tool call never appears?

Check these in order:

1. Write the prompt in English. The 8B may narrate instead of calling a tool when prompted in German or French.
2. Use a tag with a working tool template: `nishad/apertus:8b`, or `nishad/apertus:4b`, whose wrapper template makes its tool calls readable by Ollama.
3. Know what the loop does: the notebooks run one tool call per turn, mark any identifier that no tool returned as unverified, and remind the model once if it announces a call without making it.

When the notebook ran unattended, the 8B did not complete the two-step GND to Wikidata chain on its own, so you finish that step by hand.

### What does "exceeds the available context size" mean?

The prompt is longer than the context window set for the model. Retrieve fewer chunks or use smaller chunks. The 4B cannot go above 4,096 tokens. See [Troubleshooting](/v3/before-you-start/troubleshooting).

## Workshop

### Can I share the materials?

Yes, under CC BY 4.0. Keep the attribution, and check the license of any data file in [Data and licenses](/v3/resources/data).

### I missed it. What now?

Everything is self-paced. Work through the pages and notebooks in your own time and ask questions in the forum topic.

### Will it be recorded?

The organizers decide; the answer is posted in the forum topic once agreed.
