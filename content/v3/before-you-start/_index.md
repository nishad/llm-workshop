---
title: Before you start
weight: 1
cascade:
  type: docs
---

This page lists the setup steps in the order you do them. Each step links to a longer page with the details for your computer. Expect the setup to take 20 to 30 minutes, plus download time. You will download a model, the large file that your computer uses to produce answers. The larger of the two models is 5.1 GB, so if your connection is slow, start that download first and read on while it runs.

Post questions and problems in the [forum topic](https://forum.swib.org/t/getting-started-with-local-llms/1732). Everything else is on this page.

## When

Monday 16 November 2026. The Zoom room opens at 03:30 UTC for installation help.

| | UTC | Tokyo | Sydney | Delhi | Berlin / Zurich | New York |
|---|---|---|---|---|---|---|
| Part 1 | 04:00-06:00 | 13:00-15:00 | 15:00-17:00 | 09:30-11:30 | 05:00-07:00 | 23:00 Sun - 01:00 |
| Break | 06:00-06:10 | | | | | |
| Part 2 | 06:10-08:00 | 15:10-17:00 | 17:10-19:00 | 11:40-13:30 | 07:10-09:00 | 01:10-03:00 |

You can attend either half on its own. Part 1 needs no programming, and you can leave at the break. Part 2 assumes you can already run a model on your computer, and it adds Python. You can join at the break.

## 1. Pick the model for your machine

| Your memory | Model | Download |
|---|---|---|
| 16 GB or more | `thalhath/apertus:8b` | 5.1 GB |
| 8 GB | `thalhath/apertus:4b` | 2.4 GB |

Keep 20 GB of disk space free in total. Do not try the 8B model on an 8 GB machine: it does not fit in memory, so the computer moves parts of it to disk, and every answer takes minutes. Speed estimates, special cases and how to measure your own machine are on [Choose a model size](hardware).

## 2. Install the app

Install [Ollama](https://ollama.com/download) and open it once. We use it in both halves. [LM Studio](https://lmstudio.ai/) is an alternative app with a graphical interface; you can use it for Part 1 only. The steps for macOS, Windows and Linux are on [Install Ollama](install-ollama) and [Install LM Studio](install-lm-studio).

## 3. Download the model

**Ollama.** In the app, open the model picker and type the full model tag (the model's complete name) from the table above. Then select the entry with the download arrow and send any message. If you type only `apertus`, the app shows "No models found". Or run this in a terminal:

```bash
ollama pull thalhath/apertus:8b
```

On an 8 GB machine:

```bash
ollama pull thalhath/apertus:4b
```

**LM Studio.** Open Discover and paste `https://huggingface.co/unsloth/Apertus-8B-Instruct-2509-GGUF`, then choose the file marked Q4_K_M (the compressed version the workshop uses). On an 8 GB machine, paste `https://huggingface.co/jondale/Apertus-v1.1-4B-Instruct-GGUF` instead.

**Check it.** Send one message: "Reply with the word OK and the model name you think you are." Download times, the offline option and the file digests (the codes that identify the exact file contents) are on [Download the models](download-models).

The setup for Part 1 ends here. If you only want Part 1, you are ready.

## 4. Part 2 only: Python and the notebooks

Part 2 needs Ollama, one more model, two tools and the notebooks repository (the folder on GitHub that holds the Python notebooks).

1. Download the embedding model (639 MB). This is a second, smaller model that turns text into lists of numbers that represent its meaning. This step works in the terminal only:

   ```bash
   ollama pull qwen3-embedding:0.6b
   ```

2. Install uv, a tool that manages Python and its packages. It installs Python 3.12 or 3.13 for you if the Python on your system is older or newer.

   macOS and Linux:

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

   Windows PowerShell:

   ```powershell
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

3. Make sure you have git. On macOS, the first time you run `git`, the system asks to install the command line tools. Windows does not include git: install [Git for Windows](https://git-scm.com/download/win). If you prefer not to install git, go to the repository page, click the green Code button, choose Download ZIP, unpack the file, and skip the `git clone` line below.

4. Get the notebooks and start JupyterLab. The same four lines work in Windows PowerShell.

   ```bash
   git clone https://github.com/nishad/llm-workshop-notebooks
   cd llm-workshop-notebooks
   uv sync
   uv run jupyter lab
   ```

5. Download the two ready-made index files for notebook 03, `stw-de-labels.sqlite` (85.7 MB) and `unesco-en-labels.sqlite` (34.4 MB), and put them in the `runs/` folder of the repository. Create the folder if it does not exist. Building these files yourself takes about seven minutes on a fast Mac and much longer on a laptop without a graphics card.

   Download both from the [swib26 release](https://github.com/nishad/llm-workshop-notebooks/releases/tag/swib26) of the notebooks repository: [stw-de-labels.sqlite](https://github.com/nishad/llm-workshop-notebooks/releases/download/swib26/stw-de-labels.sqlite) and [unesco-en-labels.sqlite](https://github.com/nishad/llm-workshop-notebooks/releases/download/swib26/unesco-en-labels.sqlite).

   The checksums and the command to check them are on the [environment page](/v3/part2/01-environment#download-the-prebuilt-index-files). They let you confirm that the files downloaded correctly.

6. In JupyterLab, open `00_check_setup.ipynb` and run all cells. Every line must be green, including "Ollama 0.40 or newer".

If you prefer pip to uv or VS Code to JupyterLab, or if you need the Windows notes, see [Set up the environment](/v3/part2/01-environment).

## Am I ready?

- [ ] I know my model size.
- [ ] Ollama or LM Studio is installed and was opened once.
- [ ] The model for my machine is downloaded.
- [ ] It answered a first message.
- [ ] Part 2 only: `qwen3-embedding:0.6b` is downloaded, the notebooks repository is on my computer, `uv sync` finished, the two index files are in `runs/`, and `00_check_setup` is green on every line.

Part 1 needs the first four. [Am I ready?](check) has the same checks with the commands to run.

## If something does not work

Look up the symptom on [Troubleshooting](troubleshooting); most problems are there. If yours is not there, post in the [forum topic](https://forum.swib.org/t/getting-started-with-local-llms/1732). Include your operating system, how much memory your computer has, and the exact error text. If you are doing Part 2, also include the output of the last cell of `00_check_setup.ipynb`. Or ask in the Zoom room, which opens at 03:30 UTC on the workshop day for installation help.

## On the day

- **Zoom:** the link is in the event block at the top of the [forum topic](https://forum.swib.org/t/getting-started-with-local-llms/1732). The room opens at 03:30 UTC for installation help.
- **Questions:** ask in the Zoom chat during the session, or in the [forum topic](https://forum.swib.org/t/getting-started-with-local-llms/1732) at any time. When you ask for help with the setup, paste the output of the last cell of `00_check_setup.ipynb`.
- **Recording:** the SWIB organizers decide this; ask at the start of the session.
- Use the green check and red X in Zoom's participant panel to tell us how you are doing.
- If you are stuck, say so in the chat and we help you in a breakout room.
- Cameras are optional.

On the day, have these open: this site and Ollama with your model downloaded. For Part 2, also have the `llm-workshop-notebooks` folder open, with `uv sync` finished.

## The detail pages

{{< cards >}}
  {{< card link="hardware" title="Hardware" icon="chip" subtitle="Choose a model size for your machine." >}}
  {{< card link="install-ollama" title="Install Ollama" icon="download" subtitle="macOS, Windows and Linux." >}}
  {{< card link="install-lm-studio" title="Install LM Studio" icon="desktop-computer" subtitle="The graphical alternative." >}}
  {{< card link="download-models" title="Download the models" icon="cloud-download" subtitle="Model files, sizes and checksums." >}}
  {{< card link="check" title="Am I ready?" icon="check-circle" subtitle="Check Part 1 and Part 2." >}}
  {{< card link="privacy" title="Privacy" icon="shield-check" subtitle="What stays on your machine." >}}
  {{< card link="troubleshooting" title="Troubleshooting" icon="support" subtitle="Find your symptom, apply the fix." >}}
{{< /cards >}}
