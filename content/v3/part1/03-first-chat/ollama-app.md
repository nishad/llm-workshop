---
title: Ollama app
weight: 1
---

The Ollama app is the quickest way to a first answer. It downloads the model for you the first time you send a message.

## First message

{{% steps %}}

### Open the app

Start the Ollama app. A chat window opens.

### Open the model picker

Click the model name in the chat window to open the picker.

### Type the full model name

Type `nishad/apertus:8b` exactly. Use `nishad/apertus:4b` if your machine is small (see [Hardware](/v3/before-you-start/hardware)).

{{< callout type="info" >}}
Typing `apertus` alone shows "No models found". The picker looks names up on ollama.com, so it needs the full name. Only this lookup goes online; chatting afterwards does not.
{{< /callout >}}

<!-- screenshot ollama-picker-typed.png: the Ollama model picker with nishad/apertus:8b typed and the entry with the download arrow; add in Task 14 -->

### Choose the entry with the download arrow

The entry with the download arrow is the model that is not on your machine yet. Click it.

### Send a first message

Type a short message such as "Hello" and send it. The download starts.

### Watch the download bar

A bar shows the progress. The 8B model is about 5 GB, so this takes a while on a slow connection. If you already downloaded the model as described in [Download the models](/v3/before-you-start/download-models), there is no bar and the answer comes at once.

<!-- screenshot ollama-download-bar.png: the Ollama chat window with the download progress bar under the first message; add in Task 14 -->

### Read the answer

When the download ends, the model answers in the same window. You are chatting with a model that runs on your own computer.

{{% /steps %}}

## Interface tour

<!-- screenshot ollama-chat.png: the Ollama chat window with the new chat button, the model picker, the + attach button and the settings entry marked; add in Task 14 -->

- **New chat**: starts a fresh conversation with an empty context.
- **Model picker**: switches between the models on your machine.
- **Attach (+)**: adds a text file or a PDF to your message.
- **Settings**: a Cloud switch, a Context length slider and the Model location.

{{< callout type="warning" >}}
The app has no temperature setting and no system prompt. For those, use [LM Studio](/v3/part1/03-first-chat/lm-studio) or the terminal, for example `ollama run nishad/apertus:8b`.
{{< /callout >}}

To see what temperature does, read [Temperature](/v3/part1/01-how-llms-work/temperature). Next, try the [first prompts](/v3/part1/03-first-chat/first-prompts).
