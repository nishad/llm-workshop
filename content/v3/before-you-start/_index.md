---
title: Before you start
weight: 1
cascade:
  type: docs
---

This page has everything to do before the workshop, in the order you do it. Each step links to a longer page for your system. Plan on 20 to 30 minutes, plus download time. The larger model is 5.1 GB, so on a slow connection start a few days early.

Questions and problems go to the [forum topic](https://forum.swib.org/t/getting-started-with-local-llms/1732). Everything else is on this page, and it is updated when something changes.

## When

Monday 16 November 2026. The Zoom room opens at 03:30 UTC for installation help.

| | UTC | Tokyo | Sydney | Delhi | Berlin / Zurich | New York |
|---|---|---|---|---|---|---|
| Part 1 | 04:00-06:00 | 13:00-15:00 | 15:00-17:00 | 09:30-11:30 | 05:00-07:00 | 23:00 Sun - 01:00 |
| Break | 06:00-06:10 | | | | | |
| Part 2 | 06:10-08:00 | 15:10-17:00 | 17:10-19:00 | 11:40-13:30 | 07:10-09:00 | 01:10-03:00 |

Each half stands on its own. Part 1 needs no programming, and you can leave at the break. Part 2 assumes you can run a local model and adds Python, and you can join at the break.

## 1. Pick the model for your machine

| Your memory | Model | Download |
|---|---|---|
| 16 GB or more | `nishad/apertus:8b` | 5.1 GB |
| 8 GB | `nishad/apertus:4b` | 2.4 GB |

Keep 20 GB of disk free in total. Do not try the 8B on an 8 GB machine: it swaps to disk and every answer takes minutes. Speed estimates, special cases and how to measure your own machine are on [Choose a model size](hardware).

## 2. Install the app

Install [Ollama](https://ollama.com/download) and open it once. It is used in both halves. [LM Studio](https://lmstudio.ai/) is a graphical alternative for Part 1 only. The steps for macOS, Windows and Linux are on [Install Ollama](install-ollama) and [Install LM Studio](install-lm-studio).

## 3. Download the model

**Ollama.** In the app, open the model picker, type the full tag, select the entry with the download arrow and send any message. Typing `apertus` alone shows "No models found". Or in a terminal:

```bash
ollama pull nishad/apertus:8b
```

On 8 GB:

```bash
ollama pull nishad/apertus:4b
```

**LM Studio.** Open Discover and paste `https://huggingface.co/unsloth/Apertus-8B-Instruct-2509-GGUF`, then choose Q4_K_M. On 8 GB paste `https://huggingface.co/jondale/Apertus-v1.1-4B-Instruct-GGUF` instead.

**Check it.** Send one message: "Reply with the word OK and the model name you think you are." Download times, the offline route and the file digests are on [Download the models](download-models).

Part 1 ends here. If you only want Part 1, you are ready.

## 4. Part 2 only: Python and the notebooks

Part 2 needs Ollama, one more model, two tools and the notebooks repository.

1. Pull the embedding model (639 MB). This step works in the terminal only:

   ```bash
   ollama pull qwen3-embedding:0.6b
   ```

2. Install uv. It installs Python 3.12 or 3.13 for you if the system one is older or newer.

   macOS and Linux:

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

   Windows PowerShell:

   ```powershell
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

3. Make sure you have git. macOS asks to install its command line tools on the first `git` call. Windows does not ship git: install [Git for Windows](https://git-scm.com/download/win), or use the green Code button on the repository page and Download ZIP, unpack it, and skip the `git clone` line below.

4. Get the notebooks and start JupyterLab. The same four lines work in Windows PowerShell.

   ```bash
   git clone https://github.com/nishad/llm-workshop-notebooks
   cd llm-workshop-notebooks
   uv sync
   uv run jupyter lab
   ```

5. Download the two prebuilt index files for notebook 03, `stw-de-labels.sqlite` (85.7 MB) and `unesco-en-labels.sqlite` (34.4 MB), into the `runs/` folder of the repository. Create the folder if it does not exist. Building the files yourself takes about seven minutes on a fast Mac and much longer on a laptop without a graphics card.

   <!-- INDEX FILES: replace the next line with the download link once the two files are published, for example "Download both files from <URL>." -->
   The download link appears here in the week before the workshop.

   The checksums and the command to check them are on the [environment page](/v3/part2/01-environment#download-the-prebuilt-index-files).

6. In JupyterLab, open `00_check_setup.ipynb` and run all cells. Every line must be green, including "Ollama 0.40 or newer".

pip instead of uv, VS Code instead of JupyterLab, and the Windows notes are on [Set up the environment](/v3/part2/01-environment).

## Am I ready?

- [ ] I know my model size.
- [ ] Ollama or LM Studio is installed and was opened once.
- [ ] The model for my machine is downloaded.
- [ ] It answered a first message.
- [ ] Part 2 only: `qwen3-embedding:0.6b` is pulled, the repository is cloned, `uv sync` finished, the two index files are in `runs/`, and `00_check_setup` is green on every line.

Part 1 needs the first four. [Am I ready?](check) has the same list with the commands.

## If something does not work

Look up the symptom on [Troubleshooting](troubleshooting); most problems are there. Otherwise post in the [forum topic](https://forum.swib.org/t/getting-started-with-local-llms/1732) with your operating system, your memory and the exact error text, plus the output of the last cell of `00_check_setup.ipynb` if you are doing Part 2. Or come to the Zoom room at 03:30 UTC on the day.

## On the day

<!-- ON THE DAY: in the week before the workshop, fill in the Zoom link with meeting ID and passcode, the shared document link, and the recording decision. -->

- **Zoom:** the link and the meeting details appear here in the week before the workshop. The room opens at 03:30 UTC.
- **Questions and notes:** a shared document, linked here as well in the week before. Paste the output of the last cell of `00_check_setup.ipynb` there when you ask for help.
- **Recording:** decided with the organizers; the answer appears here.
- Use the green check and red X in Zoom's participant panel to tell us how you are doing.
- Helpers join breakout rooms when you ask.
- Cameras are optional.

Have open on the day: this site, Ollama with your model downloaded, and for Part 2 the `llm-workshop-notebooks` folder with `uv sync` finished.

## The detail pages

{{< cards >}}
  {{< card link="hardware" title="Hardware" icon="chip" subtitle="Choose a model size for your machine." >}}
  {{< card link="install-ollama" title="Install Ollama" icon="download" subtitle="macOS, Windows and Linux." >}}
  {{< card link="install-lm-studio" title="Install LM Studio" icon="desktop-computer" subtitle="The graphical alternative." >}}
  {{< card link="download-models" title="Download the models" icon="cloud-download" subtitle="Get the files before the session." >}}
  {{< card link="check" title="Am I ready?" icon="check-circle" subtitle="Check Part 1 and Part 2." >}}
  {{< card link="privacy" title="Privacy" icon="shield-check" subtitle="What stays on your machine." >}}
  {{< card link="troubleshooting" title="Troubleshooting" icon="support" subtitle="Find your symptom, apply the fix." >}}
{{< /cards >}}
