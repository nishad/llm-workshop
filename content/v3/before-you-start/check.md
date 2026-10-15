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
- [ ] The notebooks repository is cloned and `uv sync` finished.
- [ ] `00_check_setup.ipynb` is green on every line.

### Install the two tools the commands need

1. **uv.** The one-line installers for macOS, Linux and Windows are on the [environment page](/v3/part2/01-environment). uv installs the right Python (3.12 or 3.13) for you if the system one is older or newer.
2. **git.** Windows does not ship git: install Git for Windows from https://git-scm.com/download/win, or use the repository's green Code button and Download ZIP, then unpack it. macOS asks to install the command line tools on the first `git` call.

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
Every line must be green, including the "Ollama 0.40 or newer" line. The readiness notebook pulls nothing itself, so any missing model must be downloaded as described in [Download the models](/v3/before-you-start/download-models).
{{< /callout >}}

The materials were built and verified on Ollama 0.40.4 on 15 October 2026.

## What to paste when asking for help

Post in the forum topic (https://forum.swib.org/t/getting-started-with-local-llms/1732) and include:

1. The output of the last cell of `00_check_setup.ipynb`.
2. The exact error text.
3. Your operating system and memory.

See also [Troubleshooting](/v3/before-you-start/troubleshooting).
