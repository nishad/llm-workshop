---
title: LM Studio
weight: 2
---

LM Studio gives you more controls than the Ollama app: a system prompt, temperature, presets and a built-in way to chat with documents. A system prompt is a set of instructions that gives the model its role and rules for the whole conversation. Temperature controls how random the output is.

## Get the model and chat

{{% steps %}}

### Open Discover

Click Discover in the left bar.

### Paste the Hugging Face URL

Paste `https://huggingface.co/unsloth/Apertus-8B-Instruct-2509-GGUF` into the search field. If your computer has 8 GB of memory, paste `https://huggingface.co/jondale/Apertus-v1.1-4B-Instruct-GGUF` instead and choose its Q4_K_M file (2.43 GB).

### Choose Q4_K_M

Choose the Q4_K_M file (5.06 GB). The label describes the quantization: the model's numbers are stored at lower precision, which makes the file smaller.

### Download

Click Download and wait for it to finish.

<!-- screenshot lmstudio-discover.png: the LM Studio Discover view with the Hugging Face URL pasted and the Q4_K_M file (5.06 GB) selected; add in Task 14 -->

### Load with context length 8192

Load the model and set the context length to 8192 (4096 for the 4B) before you confirm. The context length is how much text the model can hold at once, prompt and answer together. You can only set it when the model loads.

### Chat

Type a message in the chat box and send it.

### Open the sidebar

Switch to Developer mode to see the sidebar. There you can set a **system prompt**, change the **temperature** and **save as preset**, which stores these settings under a name so you can reuse them later.

<!-- screenshot lmstudio-sidebar.png: the LM Studio sidebar in Developer mode with the system prompt, temperature and save as preset visible; add in Task 14 -->

{{% /steps %}}

To learn what these settings do, see [Temperature](/v3/part1/01-how-llms-work/temperature).

## Chat with documents

{{% steps %}}

### Attach a PDF

Attach a PDF to your message in a chat.

### Ask a question about it

Ask something the document can answer. For example, ask for a summary of one section.

{{% /steps %}}

<!-- screenshot lmstudio-documents.png: an LM Studio chat with a PDF attached and a question about it; add in Task 14 -->

LM Studio handles an attached document in one of two ways:

- **Full document**: if the whole file fits in the context, LM Studio puts the full text into the prompt, unchanged.
- **Retrieval (RAG)**: if it does not fit, LM Studio selects the passages that seem relevant to your question and adds only those.

Here you get a preview of the RAG you build in Part 2, without writing any code. RAG stands for retrieval-augmented generation: the program fetches the relevant passages first and gives them to the model with your question. The model sees only the text that was put into its context. If the context is too small, or if retrieval picks the wrong passages, the answer gets worse.

Models and sizes are covered in [Download the models](/v3/before-you-start/download-models). Next, try the [first prompts](/v3/part1/03-first-chat/first-prompts).
