---
title: LM Studio
weight: 2
---

LM Studio gives you more controls than the Ollama app: a system prompt, temperature, presets and a built-in way to chat with documents.

## Get the model and chat

{{% steps %}}

### Open Discover

Click Discover in the left bar.

### Paste the Hugging Face URL

Paste `https://huggingface.co/unsloth/Apertus-8B-Instruct-2509-GGUF` into the search field.

### Choose Q4_K_M

Pick the Q4_K_M file (5.06 GB).

### Download

Click Download and wait for it to finish.

<!-- screenshot lmstudio-discover.png: the LM Studio Discover view with the Hugging Face URL pasted and the Q4_K_M file (5.06 GB) selected; add in Task 14 -->

### Load with context length 8192

Load the model and set the context length to 8192 before you confirm. The context setting is chosen at load time.

### Chat

Type a message in the chat box and send it.

### Open the sidebar

Switch to Developer mode to see the sidebar. There you can set a **system prompt**, change the **temperature** and **save as preset** to keep the combination under a name.

<!-- screenshot lmstudio-sidebar.png: the LM Studio sidebar in Developer mode with the system prompt, temperature and save as preset visible; add in Task 14 -->

{{% /steps %}}

For what these settings do, see [Temperature](/v3/part1/01-how-llms-work/temperature).

## Chat with documents

{{% steps %}}

### Attach a PDF

Attach a PDF to your message in a chat.

### Ask a question about it

Ask something the document can answer, for example for a summary of one section.

{{% /steps %}}

<!-- screenshot lmstudio-documents.png: an LM Studio chat with a PDF attached and a question about it; add in Task 14 -->

LM Studio handles an attached document in one of two ways:

- **Full document**: if the whole file fits in the context, it is put into the prompt as is.
- **Retrieval (RAG)**: if it does not fit, only the passages that seem relevant to your question are added.

This is a no-code preview of the RAG you build in Part 2. The model never reads a document it was not given, so a too-small context is a common reason for a poor answer.

Models and sizes are covered in [Download the models](/v3/before-you-start/download-models). Next, try the [first prompts](/v3/part1/03-first-chat/first-prompts).
