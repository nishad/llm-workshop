---
title: Privacy
weight: 7
---

A local model keeps your prompts on your machine. This page explains what each tool does and does not send.

## Ollama

The first-run account screen offers an account for Ollama's cloud models and web search. Local use needs none.

To switch the cloud features off, open Settings and turn the **Cloud** switch off. This hides `:cloud` models and disables web search.

<!-- screenshot ollama-settings.png: Ollama Settings with the Cloud switch turned off; add in Task 14 -->

The terminal equivalent is the environment variable `OLLAMA_NO_CLOUD=1`.

{{< callout type="info" >}}
One honest caveat: typing a model name in the picker sends that name to ollama.com to check that it exists. Downloads come from ollama.com or Hugging Face. Your prompts never leave the machine.
{{< /callout >}}

## LM Studio

No account is needed. Chat, document chat and the local server all work offline. Only model search, downloads and runtime updates go online.

## How to confirm you are local

Turn Wi-Fi off and ask the model a question. If it answers, the work happens on your machine.

## What stays your responsibility

A local model does not make a workflow compliant with anything. It removes one data transfer. Decisions about personal or confidential data remain yours.
