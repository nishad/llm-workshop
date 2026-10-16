---
title: Privacy
weight: 7
---

A local model keeps your prompts on your machine. This page explains what each tool sends over the internet, and what it does not.

## Ollama

When you first open Ollama, a screen offers you an account. The account is for Ollama's cloud models and web search. You do not need one to run models on your own machine.

To switch the cloud features off, open Settings and turn the **Cloud** switch off. This hides the `:cloud` models and turns off web search.

<!-- screenshot ollama-settings.png: Ollama Settings with the Cloud switch turned off; add in Task 14 -->

If you use the terminal instead, set the environment variable `OLLAMA_NO_CLOUD=1`. An environment variable is a setting that a program reads when it starts. This one has the same effect as the Cloud switch.

{{< callout type="info" >}}
Typing a model name in the model picker sends that name to ollama.com to check that it exists. Downloads come from ollama.com or Hugging Face. Your prompts never leave the machine.
{{< /callout >}}

## LM Studio

LM Studio needs no account. Chat, document chat and the local server all work offline. Only three things go online: searching for models, downloading them, and updating the runtime (the engine that runs the model).

## How to confirm you are local

Turn Wi-Fi off and ask the model a question. If it answers, the work happens on your machine.

## What stays your responsibility

Using a local model does not by itself make your work comply with any rule or law. It only removes one place where data would leave your machine. Decisions about personal or confidential data are still yours.
