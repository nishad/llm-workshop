---
title: Troubleshooting
weight: 8
---

Find your symptom, apply the fix. Commands are for macOS and Linux first, then Windows PowerShell. If nothing helps, use the diagnostic block at the end and ask in the forum.

## The app will not open

{{< tabs >}}

{{< tab name="macOS" >}}
macOS blocked the app. Go to System Settings, then Privacy & Security, scroll to Security, and choose **Open Anyway** next to the message about Ollama or LM Studio. Confirm with **Open**.
{{< /tab >}}

{{< tab name="Windows" >}}
SmartScreen showed "Windows protected your PC". Choose **More info**, then **Run anyway**. This is safe for installers downloaded from the official sites.
{{< /tab >}}

{{< /tabs >}}

## "No models found" in the picker

Type the full name `nishad/apertus:8b` (or `nishad/apertus:4b`). The picker only knows names that exist on ollama.com, so a partial name finds nothing.

## A download stalls

Test that your network can reach the servers:

```bash
curl -sI https://ollama.com
```

```powershell
Invoke-WebRequest -Method Head https://ollama.com
```

Then retry the pull; it resumes where it stopped. If the network blocks the download, use the offline alternative on [Download the models](/v3/before-you-start/download-models).

## Answers are slow

```bash
ollama ps
```

Look at the PROCESSOR column. `100% GPU` is best; a CPU percentage means part of the model runs on the slow path. Fixes, in order:

1. Close browsers and other large applications.
2. On an 8 GB machine, use the 4B tag.
3. On Windows, integrated graphics are not used by Ollama, so a CPU-only speed is expected.

## Memory errors or swapping

Lower the context. Try these in order:

1. In the Ollama app, set Settings, then Context length, to 4k.
2. In a CLI chat, type `/set parameter num_ctx 4096`.
3. Set the environment variable `OLLAMA_CONTEXT_LENGTH=4096` for the server.

For the third option, the app (macOS and Windows) or the systemd service (Linux) already holds port 11434, so `ollama serve` fails with "address already in use" unless you stop it first. Linux users with the installer's service use the systemd tab; running `ollama serve` beside the service fails with "address already in use".

{{< tabs >}}

{{< tab name="macOS (terminal)" >}}
Quit the Ollama app from the menu bar first, then in Terminal start the server from a terminal where the variable is set:

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

`OLLAMA_KV_CACHE_TYPE=q8_0` halves the context memory; set it the same way, with the app quit first or in the systemd unit.

{{< callout type="warning" >}}
Never use `q4_0` for the cache with Apertus.
{{< /callout >}}

## I want to change temperature or the system prompt

The Ollama app has no controls for these. In the CLI, type `/set parameter temperature 0.2` or `/set system "..."` inside a chat. LM Studio has both in its sidebar.

## Port 11434 is busy or "could not connect"

```bash
curl http://localhost:11434/api/version
```

```powershell
Invoke-RestMethod http://localhost:11434/api/version
```

Restart the app. On Linux, restart the service:

```bash
sudo systemctl restart ollama
```

If another program holds the port, serve on a different one, bound to this machine only:

```bash
OLLAMA_HOST=127.0.0.1:11435 ollama serve
```

```powershell
$env:OLLAMA_HOST = "127.0.0.1:11435"; ollama serve
```

Start JupyterLab from a terminal where `OLLAMA_HOST=http://127.0.0.1:11435` is set, so the notebooks use the same address.

## LM Studio problems

- "Failed to load the model": pick a smaller quantization or lower the context length at load.
- "The AI has nothing to say": the context overflowed. Start a new chat.

## Logs

| Tool | Location |
|---|---|
| Ollama on macOS and Linux | `~/.ollama/logs/server.log` |
| Ollama on Windows | `%LOCALAPPDATA%\Ollama\server.log` |
| LM Studio | Developer, then logs |

## Python and Jupyter (Part 2)

- **`uv sync` fails.** Update uv with `uv self update`, check your connection, and run it from the repository folder.
- **The wrong kernel.** Register the environment and pick `swib26` in the kernel menu: `uv run python -m ipykernel install --user --name swib26`.
- **`ModuleNotFoundError: workshop`.** JupyterLab was started outside the repository. Close it, `cd` into the repository folder and run `uv run jupyter lab`.
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

Add your operating system, your memory, and the exact error text. Post it in the forum topic (https://forum.swib.org/t/getting-started-with-local-llms/1732).
