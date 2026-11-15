---
title: Environment
weight: 1
---

This page takes about 10 minutes. You install `uv`, a tool that sets up Python and the packages for you. Then you get the notebooks, start JupyterLab, run one notebook that checks everything, and download two index files for notebook 03. The page assumes that you have already installed Ollama and downloaded the models (see [Install Ollama](/v3/before-you-start/install-ollama) and [Download the models](/v3/before-you-start/download-models)).

{{< tabs >}}

{{< tab name="macOS and Linux" >}}
{{% steps %}}

### Install uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Clone the repository

```bash
git clone https://github.com/nishad/llm-workshop-notebooks.git
cd llm-workshop-notebooks
```

### Install the packages

```bash
uv sync
```

uv installs Python 3.12 or 3.13 for you if needed.

### Start JupyterLab

```bash
uv run jupyter lab
```

### Run the check

Open `00_check_setup.ipynb` and choose Run All Cells.

{{% /steps %}}
{{< /tab >}}

{{< tab name="Windows PowerShell" >}}
{{% steps %}}

### Install uv

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Close PowerShell and open it again so that it can find `uv`.

### Clone the repository

```powershell
git clone https://github.com/nishad/llm-workshop-notebooks.git
cd llm-workshop-notebooks
```

### Install the packages

```powershell
uv sync
```

uv installs Python 3.12 or 3.13 for you if needed.

### Start JupyterLab

```powershell
uv run jupyter lab
```

### Run the check

Open `00_check_setup.ipynb` and choose Run All Cells.

{{% /steps %}}
{{< /tab >}}

{{< /tabs >}}

{{< details title="pip and venv instead of uv" >}}
You need Python 3.12 or 3.13 installed. Run these four commands inside the cloned folder.

macOS and Linux:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

Windows PowerShell:

```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
jupyter lab
```
{{< /details >}}

## Download the prebuilt index files

Notebook 03 builds search indexes for two vocabularies, STW and UNESCO. On an Apple Silicon Mac with 64 GB, building them takes about seven minutes: five for STW and two for UNESCO. On a CPU-only laptop it takes far longer, so download the prebuilt files instead. On an 8 GB machine this download is the only way to follow notebook 03 live. Download both files from the [swib26 release](https://github.com/nishad/llm-workshop-notebooks/releases/tag/swib26) of the notebooks repository. Put both files in the `runs/` folder of the repository (create the folder if it does not exist). The notebook then loads the files instead of building them.

| File | Size | sha256 |
| --- | --- | --- |
| `stw-de-labels.sqlite` | 85.7 MB | `d85108cd6d38b949ac6c80decbf405021a61a7db4670495b2dea4e63807559bf` |
| `unesco-en-labels.sqlite` | 34.4 MB | `47728635aff8bd8fb9d19197c34d1f1e5e05efea039bd9429bbfa4448ddda537` |

To check that a file downloaded correctly, run `shasum -a 256 runs/stw-de-labels.sqlite` on macOS and Linux, or `Get-FileHash runs\stw-de-labels.sqlite` in PowerShell. The result should match the sha256 column in the table.

## VS Code instead of JupyterLab

Open the cloned folder in VS Code and select the `.venv` interpreter as the kernel. You can then run the notebooks there and skip `uv run jupyter lab`.

## Windows notes

- Use PowerShell, not Command Prompt. The commands above are written for it.
- The `py` launcher picks a Python version: `py -3.12` runs Python 3.12. It is useful when several versions are installed.
- Clone into a short path such as `C:\src` to avoid long path names.
- If PowerShell refuses to run the activation script, use the `uv` steps instead. They do not need that script.

## What a ready machine shows

The readiness report is cell 00.02 of notebook 00. This is how it looks on a machine where everything is in place, with every line green.

```text
✅ Python 3.12 or newer: found 3.12.12
✅ Memory: 64 GB, use nishad/apertus:8b (16 GB tier)
✅ Free disk 20 GB: 635 GB free
✅ Ollama 0.40 or newer: version 0.40.4 at http://localhost:11434
✅ Model nishad/apertus:8b: present
✅ Chat template (Unsloth fixes): present
✅ Embedding model qwen3-embedding:0.6b: 1024 dimensions
✅ Smoke chat: model said: 'OK'
✅ Smoke tool call: proposed lookup_authority({'name': 'Hannah Arendt'})

All good.
```

This output comes from notebook 00, run on Ollama 0.40.4 on 15 October 2026.

Your memory and disk numbers will differ. The Memory line tells you which tier you are on, and so which model to use: 16 GB or more uses `nishad/apertus:8b`, 8 GB uses `nishad/apertus:4b`. On an 8 GB laptop, set the environment variable `WORKSHOP_TIER=8gb` before you start JupyterLab, or change `"16gb"` to `"8gb"` in the first cell of each notebook. The `tier-8gb/` folder of the repository also holds notebooks 04 and 05 with the outputs of a run on the 8 GB tier, so you can see what the 4B model does before you run it.

If a line is red, follow the hint in it and run the cell again. Paste the output into your message when you ask for help, in the session or in the [forum topic](https://forum.swib.org/t/getting-started-with-local-llms/1732). More fixes are on [Troubleshooting](/v3/before-you-start/troubleshooting).
