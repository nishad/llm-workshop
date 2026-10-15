---
title: Install LM Studio
weight: 4
---

LM Studio is a graphical alternative to Ollama. It is enough for Part 1.

{{< callout type="warning" >}}
The download page lists **LM Studio Bionic** first. That is a different product with paid cloud plans. Download the second entry, **LM Studio** (0.4.26 or newer).
{{< /callout >}}

<!-- screenshot lmstudio-download-page.png: the LM Studio download page with the second entry, "LM Studio", marked and "LM Studio Bionic" listed first; add in Task 14 -->

## Requirements

- macOS 14 or newer on Apple Silicon only. Intel Macs should use Ollama.
- Windows x64 with AVX2 (any CPU from the last ten years), or Windows ARM.
- Linux: an AppImage.

## Install

{{% steps %}}

### Install and open

Install LM Studio for your system and open it.

### Choose User mode

User mode is enough to install and download a model. The First chat chapter switches to Developer mode, which shows the sidebar with the system prompt and temperature that Part 1's exercises use.

<!-- screenshot lmstudio-mode.png: the LM Studio mode switch with User selected; add in Task 14 -->

### Install the runtime

When prompted, install the llama.cpp runtime. Cmd+Shift+R (Ctrl+Shift+R on Windows and Linux) shows the runtimes.

### Skip sign-in

Skip any sign-in prompt. LM Studio works without an account.

{{% /steps %}}

## Verify

{{< callout type="success" >}}
Discover (the magnifying glass) opens and search works. Nothing else is needed before the model download.
{{< /callout >}}

{{< callout type="info" >}}
In Part 2 the notebooks talk to Ollama. If you only install LM Studio, you can follow Part 2 as a listener.
{{< /callout >}}
