---
title: Basics
weight: 1
---

This page follows sections 01.02 to 01.05 of notebook 01. Each code cell is quoted with the output it produced when the notebook was executed on 15 October 2026. Setup (section 01.01) creates `settings` and `MODEL`; on the 16 GB tier `MODEL` is `nishad/apertus:8b`.

## Which models do I have?

`ollama.list()` shows what is downloaded, with a digest for each model.

```python
import ollama
client = ollama.Client(host=settings.host)
for m in client.list().models:
    print(f"{m.model:45} {m.size/1e9:5.1f} GB  digest {m.digest[:12]}")
```

```text
qwen3-embedding:0.6b                            0.6 GB  digest ac6da0dfba84
nishad/apertus:8b-v1.5-preview                  5.1 GB  digest 6f25f6ba0b62
nishad/apertus:4b                               2.4 GB  digest 87ca69a79aed
nishad/apertus:8b                               5.1 GB  digest 4a85a6fea0b8
…
```

From the executed notebook 01, 15 October 2026. This is the facilitator's list, cut to the workshop rows. Your list will be shorter: only what you pulled.

A tag such as `nishad/apertus:8b` is a name that can point to different files over time. The digest is the fingerprint of the exact file. Keep that difference in mind for the [reproducibility page](/v3/part2/02-python-and-ollama/reproducibility).

## What is in the file?

`ollama.show()` reads the model's metadata. This is where the Part 1 concepts become numbers: parameters, quantization and context length.

```python
info = client.show(MODEL)
print("parameters:  ", info.details.parameter_size)
print("quantization:", info.details.quantization_level)
print("context:     ", {k: v for k, v in info.modelinfo.items() if k.endswith("context_length")})
print("capabilities:", getattr(info, "capabilities", None))
print("template starts with:", (info.template or "").splitlines()[0])
```

```text
parameters:   8.05B
quantization: Q4_K_M
context:      {'apertus.context_length': 65536}
capabilities: ['tools', 'completion']
template starts with: {# Unsloth template fixes #}
```

From the executed notebook 01, 15 October 2026. Read it as a recap of Part 1:

- **8.05B parameters** is the "8B" in the name.
- **Q4_K_M** is the quantization: a few bits per parameter instead of 16, which is why the file is 5.1 GB.
- **65,536** is the most the model can hold in its context window. Ollama's default is far below that, 4,096 tokens on most laptops (see [Context](/v3/part1/01-how-llms-work/context)). The notebooks set the value for your tier, as the next cell shows.
- **tools** in the capabilities list says this build can call tools. Part 2 needs it for the last notebook.
- The **template** header tells you which chat template is in use. `{# Unsloth template fixes #}` is the one the workshop tags carry.

## A first chat with a system prompt

The `messages` list is the whole conversation. The system message sets the role; the user message is the question. The helper `workshop.llm.chat` sets temperature 0 and the `num_ctx` for your tier, so results are repeatable.

```python
from workshop.llm import chat
from workshop.display import show_markdown

messages = [
    {"role": "system", "content": "You are a cataloguing assistant in a research library. Be brief and precise."},
    {"role": "user", "content": "In two sentences: what is an authority file, and why do catalogues use one?"},
]
response = chat(messages, model=MODEL)
show_markdown(response.message.content)
```

The notebook displays the answer as formatted text:

> An authority file is a centralized list of standardized names, titles, and subjects used in a library's catalog. Catalogues use authority files to ensure consistency in the way information is recorded and retrieved, making it easier for users to find relevant materials.

From the executed notebook 01, 15 October 2026.

{{< details title="How the helper differs from calling ollama directly" >}}
The helper adds two defaults and a log line (see the [reproducibility page](/v3/part2/02-python-and-ollama/reproducibility)). Without it, the same call is three lines:

```python
import ollama
client = ollama.Client(host="http://localhost:11434")
client.chat(model="nishad/apertus:8b", messages=[{"role": "user", "content": "..."}], options={"temperature": 0, "num_ctx": 8192})
```

The helper sets `temperature` to 0 and `num_ctx` to the value for your tier (8,192 on the 16 GB tier, shown in the setup cell). You can override either through its `options` argument.
{{< /details >}}

## The response object

`response` is more than the text. Besides `message`, it carries the numbers Ollama reports for the call: how many tokens it read from your prompt (`prompt_eval_count`), how many it generated (`eval_count`), and how long each phase took (`total_duration`, `load_duration` and the others, in nanoseconds). Those are the tokens and the speed from Part 1, now available to your code. Divide `eval_count` by the generation time and you have your own tokens per second, for every call you make.

## Temperature, seed and repeatability

The same question runs three times at temperature 0 with a fixed seed, then three times at 0.8. This is the difference between a reproducible pipeline and a creative assistant.

```python
question = [{"role": "user", "content": "Suggest a title for a newsletter about open data in libraries. One line, no explanation."}]
for temp in (0, 0.8):
    print(f"--- temperature {temp} ---")
    for run in range(3):
        r = chat(question, model=MODEL, options={"temperature": temp, "seed": 42} if temp == 0 else {"temperature": temp})
        print(run + 1, r.message.content.strip().replace("\n", " | ")[:160])
```

```text
--- temperature 0 ---
1 "Open Data in Libraries: Insights and Innovations"
2 "Open Data in Libraries: Insights and Innovations"
3 "Open Data in Libraries: Insights and Innovations"
--- temperature 0.8 ---
1 "Open Data Insights: Libraries and the Future of Knowledge"
2 "Open Data in Libraries: Transparency, Accessibility, and Community Building"
3 "Library Open Data: Discovering Transparency and Accessibility"
```

From the executed notebook 01, 15 October 2026. The output is quoted as committed (blank lines between the notebook's print calls removed).

Look at the six lines. At temperature 0 the three answers are identical, as expected. At 0.8 all three differ. A creative prompt has no single favored answer, so sampling picks different tokens on each run. Sampling makes variation possible, not certain: for a short factual question the top candidates dominate, and a higher temperature may change nothing. Try the 0.8 loop with a factual question such as "Name three controlled vocabularies used in libraries" and compare.

Run and change: change the seed in one of the temperature-0 runs. Does the answer change? Then ask the question in German and compare.

## Streaming

Long answers arrive token by token. Streaming shows them as they come, like the chat window did.

```python
from workshop.display import stream_markdown
stream = chat([{"role": "user", "content": "Explain in five short bullet points what a library would use a local language model for."}],
              model=MODEL, stream=True)
text = stream_markdown(stream)
```

The cell prints the answer progressively and returns the full text in `text`. In the committed notebook the answer is five bullet points; the saved copy holds only the final display, so there is no per-token output to quote. Run the cell to watch it arrive.
