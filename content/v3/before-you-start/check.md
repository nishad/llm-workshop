---
title: Am I ready?
weight: 6
---

Work through both checklists. Part 1 needs only the first.

## Part 1

- [ ] The app opens (Ollama or LM Studio).
- [ ] The model answers a message.

## Part 2

- [ ] Python 3.12 or 3.13 is installed.
- [ ] `uv` is installed.
- [ ] The notebooks repository is on your computer (cloned or unpacked) and `uv sync` finished.
- [ ] `qwen3-embedding:0.6b` is downloaded (`ollama list` shows it).
- [ ] The two index files for notebook 03 are in `runs/`.
- [ ] `00_check_setup.ipynb` is green on every line.

### Install the two tools the commands need

1. **uv.** This tool installs Python and the packages the notebooks need. The one-line installers for macOS, Linux and Windows are on the [environment page](/v3/part2/01-environment). If the Python on your system is not 3.12 or 3.13, uv installs the right version for you.
2. **git.** On macOS, the first time you run `git`, the system asks to install the command line tools. Windows does not include git: install Git for Windows from https://git-scm.com/download/win. If you prefer not to install git, go to the repository page, click the green Code button, choose Download ZIP, and unpack the file. Then, in the commands below, skip the `git clone` line and `cd` into the unpacked folder instead.

Then run the commands:

{{< tabs >}}

{{< tab name="macOS and Linux" >}}
```bash
python3 --version
uv --version
git clone https://github.com/nishad/llm-workshop-notebooks
cd llm-workshop-notebooks
uv sync
uv run jupyter lab
```
{{< /tab >}}

{{< tab name="Windows PowerShell" >}}
```powershell
py --version
uv --version
git clone https://github.com/nishad/llm-workshop-notebooks
cd llm-workshop-notebooks
uv sync
uv run jupyter lab
```
{{< /tab >}}

{{< /tabs >}}

In JupyterLab, open `00_check_setup.ipynb` and run all cells.

{{< callout type="success" >}}
Every line must be green, including the "Ollama 0.40 or newer" line. The check notebook does not download anything itself. If a model is missing, download it as described in [Download the models](/v3/before-you-start/download-models).
{{< /callout >}}

We built and tested the materials with Ollama 0.40.4 on 15 October 2026.

## What to paste when asking for help

Post in the forum topic (<https://forum.swib.org/t/getting-started-with-local-llms/1732>) and include:

1. The output of the last cell of `00_check_setup.ipynb`.
2. The exact error text.
3. Your operating system and how much memory your computer has.

See also [Troubleshooting](/v3/before-you-start/troubleshooting).
