---
title: Environment
weight: 1
---

This page takes about 10 minutes. You install `uv`, get the notebooks, start JupyterLab and run one notebook that checks everything. Ollama and the models come from [Am I ready?](/v3/before-you-start/check); this page assumes they are done.

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

uv installs Python 3.12 for you if needed.

### Start JupyterLab

```bash
uv run jupyter lab
```

### Run the check

Open `00_check_setup.ipynb` and choose Run All Cells.

### Download the prebuilt index files

Download the two prebuilt vocabulary index files for notebook 03 from the link in the download post on the [forum topic](https://forum.swib.org/t/getting-started-with-local-llms/1732) into the `runs/` folder of the repository (create it if it does not exist):

| File | Size | sha256 |
| --- | --- | --- |
| `stw-de-labels.sqlite` | 85.7 MB | `5d89c6704268b0c0ae29656dcfc31ea3d1402469edbd76f80a043f1843b07e8c` |
| `unesco-en-labels.sqlite` | 34.4 MB | `c4755d17a9c00c742f9f2b601e82e51165f69d5380395adaa083a7ea43ae10c7` |

Check a file with `shasum -a 256 runs/stw-de-labels.sqlite`. Building the two indexes takes about seven minutes for both (about five for STW, two for UNESCO) on an Apple Silicon Mac with 64 GB and far longer on a CPU-only laptop, so on the 8 GB tier downloading them is the way to follow notebook 03 live.

{{% /steps %}}
{{< /tab >}}

{{< tab name="Windows PowerShell" >}}
{{% steps %}}

### Install uv

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Close PowerShell and open it again so that `uv` is found.

### Clone the repository

```powershell
git clone https://github.com/nishad/llm-workshop-notebooks.git
cd llm-workshop-notebooks
```

### Install the packages

```powershell
uv sync
```

uv installs Python 3.12 for you if needed.

### Start JupyterLab

```powershell
uv run jupyter lab
```

### Run the check

Open `00_check_setup.ipynb` and choose Run All Cells.

### Download the prebuilt index files

Download the two prebuilt vocabulary index files for notebook 03 from the link in the download post on the [forum topic](https://forum.swib.org/t/getting-started-with-local-llms/1732) into the `runs/` folder of the repository (create it if it does not exist):

| File | Size | sha256 |
| --- | --- | --- |
| `stw-de-labels.sqlite` | 85.7 MB | `5d89c6704268b0c0ae29656dcfc31ea3d1402469edbd76f80a043f1843b07e8c` |
| `unesco-en-labels.sqlite` | 34.4 MB | `c4755d17a9c00c742f9f2b601e82e51165f69d5380395adaa083a7ea43ae10c7` |

Check a file with `Get-FileHash runs\stw-de-labels.sqlite`. Building the two indexes takes about seven minutes for both (about five for STW, two for UNESCO) on an Apple Silicon Mac with 64 GB and far longer on a CPU-only laptop, so on the 8 GB tier downloading them is the way to follow notebook 03 live.

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

## VS Code instead of JupyterLab

Open the cloned folder in VS Code and select the `.venv` interpreter as the kernel. You can then run the notebooks there and skip `uv run jupyter lab`.

## Windows notes

- Use PowerShell, not Command Prompt. The commands above are written for it.
- The `py` launcher picks a Python version: `py -3.12` runs Python 3.12. It is useful when several versions are installed.
- Clone into a short path such as `C:\src`, to stay clear of long path names.
- If PowerShell refuses to run the activation script, the `uv` route avoids it.

## What a ready machine shows

The readiness report is cell 00.02 of the notebook. This is how it looks on a current install. Every line is green.

```text
✅ Python 3.12 or newer: found 3.12.12
✅ Memory: 64 GB, use nishad/apertus:8b (16 GB tier)
✅ Free disk 20 GB: 635 GB free
✅ Ollama 0.40 or newer: version 0.40.1 at http://localhost:11434
✅ Model nishad/apertus:8b: present
✅ Chat template (Unsloth fixes): present
✅ Embedding model qwen3-embedding:0.6b: 1024 dimensions
✅ Smoke chat: model said: 'OK'
✅ Smoke tool call: proposed lookup_authority({'name': 'Hannah Arendt'})
```

From the executed notebook 00, 15 October 2026. The materials were built in October 2026 on Ollama 0.35.1 and are re-verified on 0.40 before the workshop.

Your memory and disk numbers will differ. The Memory line tells you which tier you are on: 16 GB or more uses `nishad/apertus:8b`, 8 GB uses `nishad/apertus:4b`. On an 8 GB laptop, set `WORKSHOP_TIER` to `8gb` in the first cell. The repository also holds notebooks 04 and 05 as executed on the 8 GB tier, in `tier-8gb/`, so you can see what the 4B does before you run it.

If a line is red, follow the hint in it and run the cell again. Paste the output into the shared document when you ask for help. More fixes are on [Am I ready?](/v3/before-you-start/check).
