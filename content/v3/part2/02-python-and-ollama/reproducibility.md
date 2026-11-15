---
title: Reproducibility
weight: 3
---

A result cannot be checked later without its provenance, the record of how it was produced. This page covers section 01.07 of notebook 01: what to record with every result, and the code that records it.

## What to record

Write these down with every result:

- **Tag**, for example `thalhath/apertus:8b`.
- **Digest**, the fingerprint of the exact file and template.
- **Quantization**, for example Q4_K_M.
- **Options**, such as temperature, seed and `num_ctx`.
- **Prompt**, including the system message.
- **Date** of the run.
- **Runtime version**, the Ollama version.

## Why

On the same runtime and hardware, the same digest at temperature 0 with a seed gives the same answer. Without the digest, you cannot say you used the same model: a tag can be pointed to a new file. A different quantization is a different model, with different answers. The runtime version belongs in the record too, so that you can trace a difference that appears later. Each item on the list removes one way that two runs could differ without anyone noticing.

This matters for metadata work in two ways. A record that a model created needs to say how it was made. Anyone who checks it later needs to be able to repeat the run.

## The provenance record

The helper `provenance()` collects the facts from Ollama. `workshop.llm.chat` already logs every call (see below), so this cell shows the full provenance record just once. The cell writes the record with `log_run`, the same function the chat helper uses.

```python
from workshop.llm import provenance, log_run
prov = provenance(MODEL)
record = {"notebook": "01", "prompt": messages[-1]["content"], "answer": response.message.content, **prov,
          "options": {"temperature": 0, "num_ctx": context_limit(MODEL)}}
log_run(record)
print({k: record[k] for k in ("model", "digest", "quantization", "ollama_version", "captured_at")})
print("appended to runs/log.jsonl")
```

```text
{'model': 'thalhath/apertus:8b', 'digest': '4a85a6fea0b8748229840a797cdeb5f45075b681040dc538f8ed17bf9e55059e', 'quantization': 'Q4_K_M', 'ollama_version': '0.40.4', 'captured_at': '2026-10-15T10:32:13+00:00'}
appended to runs/log.jsonl
```

From the executed notebook 01, 15 October 2026. If you pulled the tag from ollama.com, your digest is `61041b337fa9` rather than `4a85a6fea0b8`; both name the same model file, see [Digests and sources](/v3/before-you-start/download-models#digests-and-sources). Your version and time will differ.

Notebook 00 shows the full record as JSON. Besides the fields above, it has `parameter_size` (`8.05B`), `context_length` (65536) and `template_header`.

## The log file

`runs/log.jsonl` holds one JSON object per line, one per logged call. It is plain text: open it in an editor, load it with any JSON tool or search it with `grep`. Every `workshop.llm.chat` call appends a line with the time, the model and its digest, the options, the last 300 characters of the prompt and the first 300 of the answer. Streamed calls log the request only. The RAG helper, the tool loop and the setup check's smoke calls (quick test calls) all go through `chat`, so they are logged too. Three kinds of call are not logged: embedding calls, the OpenAI client call in 01.06 and the oversized prompt in 04.07. The last two skip the helper on purpose. Keep the file with your results.

## Citing a model in a workflow document

Name the model by tag and digest, not by tag alone. For example:

> Records were generated with `thalhath/apertus:8b` (digest `4a85a6fea0b8`, Q4_K_M), run through Ollama 0.40.4 at temperature 0 with seed 42, context 8,192 tokens, on 15 October 2026. Prompts and answers are in `runs/log.jsonl`.

Add the full digest in an appendix or the log.

## What a digest does and does not tell you

A digest identifies one thing: this exact file. It does not tell you what text the model was trained on. For that, you need the model's public documentation, such as the EU training-data summary that [Apertus](/v3/part1/02-open-models/apertus) publishes. The [provenance chapter](/v3/part1/02-open-models/provenance) shows how to look it up. Record both: the digest for the file, the summary for the data.
