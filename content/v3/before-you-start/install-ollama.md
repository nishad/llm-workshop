---
title: Install Ollama
weight: 3
---

Ollama is the program that runs the models, and we use it in both halves of the workshop. Install it, open it once, and check the version.

{{< tabs >}}

{{< tab name="macOS" >}}
{{% steps %}}

### Download

Get `Ollama.dmg` from https://ollama.com/download. You need macOS 14 or newer.

### Install

Open the downloaded disk image and drag Ollama into the Applications folder.

### Open

Open Ollama from Applications. If macOS blocks it, go to System Settings, then Privacy & Security, and choose **Open Anyway**.

{{% /steps %}}
{{< /tab >}}

{{< tab name="Windows" >}}
{{% steps %}}

### Download

Get `OllamaSetup.exe` from https://ollama.com/download. It is about 1.6 GB and needs Windows 10 22H2 or newer.

### Install

Run the installer. You do not need administrator rights. The installation uses about 4 GB of disk space.

### Allow it

If a Windows SmartScreen warning appears, choose **More info**, then **Run anyway**.

{{% /steps %}}
{{< /tab >}}

{{< tab name="Linux" >}}
{{% steps %}}

### Run the install script

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### Leave the service alone

The script sets up Ollama as a background service (a systemd service) and starts it for you. Do not run `ollama serve` afterwards, because the service is already running.

### Pick a chat window

There is no desktop app on Linux. Use the terminal, or install [LM Studio](/v3/before-you-start/install-lm-studio) for a chat window.

{{% /steps %}}
{{< /tab >}}

{{< /tabs >}}

## First run

When you open the app for the first time on macOS or Windows, Ollama shows "Welcome to Ollama" and then a "Create an account" screen.

Choose **No thanks, I'll use Ollama locally**. The account is only for Ollama's paid cloud models; you do not need it for this workshop. The next screen, "Run Ollama", shows a terminal command. You can close that screen.

{{< callout type="info" >}}
If you skipped the account screen by accident, nothing is lost. Local use never needs an account.
{{< /callout >}}

## Verify

The app window opens with "Select a model". In a terminal, run:

```bash
ollama --version
```

{{< callout type="success" >}}
The command must print 0.40 or newer. We tested the workshop materials on 0.40.4.
{{< /callout >}}

## Where models live

| System | Folder |
|---|---|
| macOS and Linux (user install) | `~/.ollama/models` |
| Windows | `%USERPROFILE%\.ollama\models` |
| Linux (system service) | `/usr/share/ollama/.ollama/models` |

You can change the location in Settings, under Model location.
