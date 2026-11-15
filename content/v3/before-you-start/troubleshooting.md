---
title: Troubleshooting
weight: 8
---

Find your problem below and follow the fix. Commands are shown for macOS and Linux first, then for Windows PowerShell. If nothing helps, use the diagnostic block at the end of this page and ask in the forum.

## The app will not open

{{< tabs >}}

{{< tab name="macOS" >}}
macOS blocked the app. Go to System Settings, then Privacy & Security, scroll to Security, and choose **Open Anyway** next to the message about Ollama or LM Studio. Confirm with **Open**.
{{< /tab >}}

{{< tab name="Windows" >}}
Windows SmartScreen, the built-in security check, showed "Windows protected your PC". Choose **More info**, then **Run anyway**. This is safe when the installer came from the official Ollama or LM Studio site.
{{< /tab >}}

{{< /tabs >}}

## "No models found" in the picker

Type the full name `thalhath/apertus:8b` (or `thalhath/apertus:4b`). The picker only knows names that exist on ollama.com, so a partial name finds nothing.

## A download stalls

First check that your network can reach the download servers:

```bash
curl -sI https://ollama.com
```

```powershell
Invoke-WebRequest -Method Head https://ollama.com
```

Then start the download again. It continues from where it stopped. If your network blocks the download, use the offline option on [Download the models](/v3/before-you-start/download-models).

## Answers are slow

```bash
ollama ps
```

Look at the PROCESSOR column. `100% GPU` is best. A CPU percentage means part of the model runs on the CPU, which is slower. Try these fixes in order:

1. Close browsers and other large applications.
2. On a machine with 8 GB of memory, use the 4B model, `thalhath/apertus:4b`.

On Windows laptops with integrated graphics (no separate graphics card), Ollama runs on the CPU, so slower answers are normal.

## Memory errors or swapping

Lower the context length, which is how much text the model can hold at once. Try these in order:

1. In the Ollama app, open Settings, find Context length, and set it to 4k.
2. In a chat in the terminal, type `/set parameter num_ctx 4096`.
3. Set the environment variable `OLLAMA_CONTEXT_LENGTH=4096` for the server.

For the third option, note that Ollama is already using port 11434: the app on macOS and Windows, or the systemd service on Linux. If you start `ollama serve` while it is running, the command fails with "address already in use". Quit the app first. On Linux, edit the service instead, as shown in the Linux tab below.

{{< tabs >}}

{{< tab name="macOS (terminal)" >}}
Quit the Ollama app from the menu bar, then start the server from a terminal where the variable is set:

```bash
export OLLAMA_CONTEXT_LENGTH=4096
ollama serve
```
{{< /tab >}}

{{< tab name="Windows PowerShell" >}}
Quit the Ollama app first, then start the server from a terminal where the variable is set:

```powershell
$env:OLLAMA_CONTEXT_LENGTH = "4096"
ollama serve
```
{{< /tab >}}

{{< tab name="Linux (systemd service)" >}}
Run `sudo systemctl edit ollama`, add these lines, then restart the service:

```ini
[Service]
Environment="OLLAMA_CONTEXT_LENGTH=4096"
```

```bash
sudo systemctl restart ollama
```
{{< /tab >}}

{{< /tabs >}}

The environment variable `OLLAMA_KV_CACHE_TYPE=q8_0` cuts the memory used by the context in half. Set it in the same way: quit the app first, or on Linux add it to the systemd service.

{{< callout type="warning" >}}
Never use `q4_0` for the cache with Apertus.
{{< /callout >}}

## I want to change temperature or the system prompt

The Ollama app has no settings for these. In a chat in the terminal, type `/set parameter temperature 0.2` or `/set system "..."`. LM Studio has both settings in its sidebar.

## Port 11434 is busy or "could not connect"

A port is a numbered channel that programs on one computer use to talk to each other. Ollama listens on port 11434. Check whether its server answers:

```bash
curl http://localhost:11434/api/version
```

```powershell
Invoke-RestMethod http://localhost:11434/api/version
```

If the command prints a version number, the server is running. If there is no answer, restart the app. On Linux, restart the service:

```bash
sudo systemctl restart ollama
```

If another program is using the port, start the Ollama server on a different port. The address below also keeps the server reachable from this machine only:

```bash
OLLAMA_HOST=127.0.0.1:11435 ollama serve
```

```powershell
$env:OLLAMA_HOST = "127.0.0.1:11435"; ollama serve
```

Start JupyterLab from a terminal where `OLLAMA_HOST=http://127.0.0.1:11435` is set, so the notebooks use the same address.

## LM Studio problems

- "Failed to load the model": pick a smaller quantization (a more compressed copy of the model) or lower the context length when you load it.
- "The AI has nothing to say": the conversation has grown longer than the context length. Start a new chat.

## Logs

| Tool | Location |
|---|---|
| Ollama on macOS and Linux | `~/.ollama/logs/server.log` |
| Ollama on Windows | `%LOCALAPPDATA%\Ollama\server.log` |
| LM Studio | Developer, then logs |

## Python and Jupyter (Part 2)

- **`uv sync` fails.** Update uv with `uv self update`, check your internet connection, and run `uv sync` from inside the repository folder.
- **The wrong kernel.** The kernel is the Python environment that runs the notebook's cells. Register the environment with `uv run python -m ipykernel install --user --name swib26`, then pick `swib26` in the kernel menu.
- **`ModuleNotFoundError: workshop`.** You started JupyterLab outside the repository folder. Close it, `cd` into the repository folder, and run `uv run jupyter lab`.
- **`UnicodeDecodeError` on Windows.** Open files with `encoding="utf-8"` in your own code.

## Diagnostic block to paste

```bash
ollama --version
ollama list
ollama ps
curl http://localhost:11434/api/version
```

```powershell
ollama --version
ollama list
ollama ps
Invoke-RestMethod http://localhost:11434/api/version
```

Add your operating system, how much memory your computer has, and the exact error text. Post all of this in the forum topic (<https://forum.swib.org/t/getting-started-with-local-llms/1732>).
