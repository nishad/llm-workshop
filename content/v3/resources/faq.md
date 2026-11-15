---
title: FAQ
weight: 6
---

## General

### Is it really free?

Yes. The models, the runtimes (the programs that run them, such as Ollama and LM Studio) and the workshop materials cost nothing. You pay only for your own electricity and storage.

### Do I need a GPU?

No. The models run on an ordinary laptop. Memory matters more than a graphics card; see the tier table on [Choose a model size for your hardware](/v3/before-you-start/hardware).

### Can I use it for work?

Yes, when you run the model on your own machine. The Apertus Acceptable Use Policy applies, so read it if you plan to share the outputs or the model itself with others.

## Models

### Is Apertus open source?

It is fully open. All of it is published under Apache-2.0 with an acceptable use policy: the weights, the training code, the scripts that rebuild the training data, and the intermediate checkpoints (versions of the model saved during training). As of 15 November 2026, whether that policy fits the Open Source Definition is not settled. Part 1 explains the openness ladder.

### Why not Llama?

Meta's Llama models are open weights under a custom license. The license restricts some uses, and it excludes users in the EU from the multimodal models (the ones that also handle images). That puts them on tier 1 of the openness ladder, two tiers below Apertus. Their training data is also closed.

### Why is the 8B not for 8 GB machines?

The model file alone is 5.06 GB, and the context window (the most text the model can take in at once) needs more memory beyond that. On an 8 GB machine the system swaps to disk, which means it uses the much slower disk as extra memory. Every answer then takes minutes. Use the 4B instead. See [Model guide](/v3/resources/models).

### What is the v1.5 preview?

An unofficial conversion of Apertus v1.5 made by the community. It handles text only, and it has not been checked against the original to confirm that it behaves the same. It is optional, and it is meant for machines with 16 GB or more. Details are on the [Model guide](/v3/resources/models).

## Runtimes

### Ollama or LM Studio?

Either works for Part 1. Part 2 needs Ollama, because the notebooks connect to it.

### Does Ollama send my prompts anywhere?

No. Prompts stay on your machine. See [Privacy](/v3/before-you-start/privacy) for what happens when you type a model name, and for how to turn the Cloud switch off.

### Where are models stored?

Ollama keeps them in `~/.ollama/models` on macOS and Linux and in `%USERPROFILE%\.ollama\models` on Windows. See [Install Ollama](/v3/before-you-start/install-ollama).

## Part 2

### Why Python 3.12 or 3.13?

The environment for the notebooks is pinned (fixed) to Python 3.12 or 3.13, the versions we wrote and tested them on. uv installs one of these for you, so the Python already on your computer does not matter.

### Why not chromadb?

chromadb is a vector database library. It installs about 250 MB of other packages along with it, and it has an unresolved installation problem on Windows. The notebooks use numpy and sqlite-vec instead; sqlite-vec is a 0.2 MB package.

### What if a tool call never appears?

Check these in order:

1. Write the prompt in English. When the prompt is in German or French, the 8B may describe the tool call in words instead of making it.
2. Use a model tag with a working tool template: `nishad/apertus:8b`, or `nishad/apertus:4b`, which has a wrapper template so that Ollama can read its tool calls.
3. Know what the loop does. The notebooks run one tool call per turn. If the model's answer contains an identifier that no tool returned, they mark it as unverified. If the model announces a call but does not make it, they remind it once.

When the notebook ran without anyone guiding it, the 8B did not complete the two-step chain from GND to Wikidata. You will need to finish that step by hand.

### What does "exceeds the available context size" mean?

The prompt is longer than the context window set for the model. Retrieve fewer chunks, or use smaller chunks. The 4B cannot go above 4,096 tokens. See [Troubleshooting](/v3/before-you-start/troubleshooting).

## Workshop

### Can I share the materials?

Yes, under CC BY 4.0. Keep the attribution, and check the license of any data file in [Data and licenses](/v3/resources/data).

### I missed it. What now?

Everything is self-paced. Work through the pages and notebooks in your own time and ask questions in the [forum topic](https://forum.swib.org/t/getting-started-with-local-llms/1732).

### Will it be recorded?

The SWIB organizers decide this. Ask at the start of the session.
