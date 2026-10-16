---
title: Notebooks
weight: 8
---

The workshop uses six notebooks, numbered 00 to 05. Each one ends with a Checkpoint cell that tells you what you should have reached by that point.

## The six notebooks

| Notebook | Budget | What you do | Tier notes | On GitHub |
|---|---|---|---|---|
| `00_check_setup` | 10 min | Check Python, memory, disk, Ollama, the chat and embedding models (on 8 GB machines it checks for `nishad/apertus:4b` instead of the 8B) and one smoke call each | Same notebook on both tiers | [00_check_setup.ipynb](https://github.com/nishad/llm-workshop-notebooks/blob/main/00_check_setup.ipynb) |
| `01_python_and_ollama` | 20 min | Chat, system prompts, temperature, streaming, the OpenAI client, provenance logging | Same notebook on both tiers | [01_python_and_ollama.ipynb](https://github.com/nishad/llm-workshop-notebooks/blob/main/01_python_and_ollama.ipynb) |
| `02_structured_output` | 25 min | Extract catalog card records into a Pydantic schema, validate them, measure against a gold file | Same notebook on both tiers | [02_structured_output.ipynb](https://github.com/nishad/llm-workshop-notebooks/blob/main/02_structured_output.ipynb) |
| `03_vocabulary_search` | 25 min | Embeddings, cross-lingual search over STW and UNESCO labels, a sqlite-vec index | On the 8 GB tier, download the prebuilt index files | [03_vocabulary_search.ipynb](https://github.com/nishad/llm-workshop-notebooks/blob/main/03_vocabulary_search.ipynb) |
| `04_rag` | 20 min | Chunk documents, retrieve, answer with numbered citations, hit the context limit on purpose | 8 GB tier: 3 chunks, 4,096-token window; copy in `tier-8gb/` | [04_rag.ipynb](https://github.com/nishad/llm-workshop-notebooks/blob/main/04_rag.ipynb) |
| `05_tool_use` | 15 min | Let the model propose GND, Wikidata and SPARQL calls; approve, correct or refuse each one | 8 GB tier: single-tool cells only; copy in `tier-8gb/` | [05_tool_use.ipynb](https://github.com/nishad/llm-workshop-notebooks/blob/main/05_tool_use.ipynb) |

The tier notes refer to the two hardware tiers: a machine with 16 GB of memory or more runs the 8B model, an 8 GB machine runs the 4B.

The budgets in the table are the times given in the notebooks, and they are meant for self-study. In the live session we shorten them to fit the 110 minutes. The [Part 2 timeline](/v3/part2#timeline) shows the minutes for each segment.

<!-- screenshot nb-00-checkpoint.png: JupyterLab, notebook 00: the Checkpoint cell after a green run; add in Task 14 -->
<!-- screenshot nb-01-checkpoint.png: JupyterLab, notebook 01: the Checkpoint cell; add in Task 14 -->
<!-- screenshot nb-02-checkpoint.png: JupyterLab, notebook 02: the Checkpoint cell with the accuracy line above it; add in Task 14 -->
<!-- screenshot nb-03-checkpoint.png: JupyterLab, notebook 03: the Checkpoint cell with the recall lines above it; add in Task 14 -->
<!-- screenshot nb-04-checkpoint.png: JupyterLab, notebook 04: the Checkpoint cell; add in Task 14 -->
<!-- screenshot nb-05-checkpoint.png: JupyterLab, notebook 05: the Checkpoint cell; add in Task 14 -->

The site chapters that go with notebooks 01 to 05 are [Python and Ollama](/v3/part2/02-python-and-ollama), [structured output](/v3/part2/03-structured-output), [embeddings](/v3/part2/04-embeddings), [RAG](/v3/part2/05-rag) and [tool use](/v3/part2/06-tool-use).

## How to run them

Follow the [environment page](/v3/part2/01-environment): install uv, clone the repository, install the packages and start JupyterLab. Open `00_check_setup.ipynb` first; every line should show a check mark. Notebook 03 uses two prebuilt index files that you download into `runs/`. The steps and checksums are on the environment page, and the files are listed on the [data page](/v3/resources/data).

An 8 GB machine runs the same notebooks with the 4B model: set the environment variable `WORKSHOP_TIER=8gb` before you start JupyterLab, or change `"16gb"` to `"8gb"` in the first cell of each notebook.

## Read them without running them

Every notebook is saved on GitHub with its outputs, so you can read it there without Python. The `tier-8gb/` folder holds notebooks 04 and 05 as they ran on the 8 GB tier with `nishad/apertus:4b`. If you have an 8 GB machine, open them to see what to expect.

## The 2025 notebooks

The notebooks from the 2025 edition stay available at the repository tag [`swib25`](https://github.com/nishad/llm-workshop-notebooks/tree/swib25).

## Licenses

- Code: MIT.
- Vocabularies: STW under CC BY 4.0; UNESCO Thesaurus under CC BY-SA 3.0 IGO.
- Documents and catalog cards: CC BY 4.0.
- Model weights: Apache-2.0, with the Apertus LLM Acceptable Use Policy.

Sources, licenses and retrieval dates for every data file are on the [data and licenses page](/v3/resources/data).
