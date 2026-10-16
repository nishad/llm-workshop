---
title: Install LM Studio
weight: 4
---

LM Studio is a graphical desktop application and an alternative to Ollama. It is all you need for Part 1.

{{< callout type="warning" >}}
The download page lists **LM Studio Bionic** first. That is a different product with paid cloud plans. Download the second entry, **LM Studio** (0.4.26 or newer).
{{< /callout >}}

<!-- screenshot lmstudio-download-page.png: the LM Studio download page with the second entry, "LM Studio", marked and "LM Studio Bionic" listed first; add in Task 14 -->

## Requirements

- macOS 14 or newer on Apple Silicon only. Intel Macs should use Ollama.
- Windows x64 with AVX2 (any CPU from the last ten years), or Windows ARM.
- Linux: the download is an AppImage file.

## Install

{{% steps %}}

### Install and open

Install LM Studio for your system and open it.

### Choose User mode

User mode is enough to finish the installation and download a model. You switch to Developer mode later, in the First chat chapter. That mode shows a sidebar with the two settings the Part 1 exercises use. One is the system prompt, which gives the model its role and rules. The other is the temperature, which controls how varied the answers are.

<!-- screenshot lmstudio-mode.png: the LM Studio mode switch with User selected; add in Task 14 -->

### Install the runtime

When LM Studio asks, install the llama.cpp runtime. This is the engine that runs the model. Cmd+Shift+R (Ctrl+Shift+R on Windows and Linux) shows the runtimes.

### Skip sign-in

Skip any sign-in prompt. LM Studio works without an account.

{{% /steps %}}

## Verify

{{< callout type="success" >}}
Click the magnifying glass to open Discover, then try a search. If search works, nothing else is needed before you download the model.
{{< /callout >}}

{{< callout type="info" >}}
In Part 2 the notebooks connect to Ollama. If you install only LM Studio, you can still follow Part 2 by watching, without running the notebooks yourself.
{{< /callout >}}
