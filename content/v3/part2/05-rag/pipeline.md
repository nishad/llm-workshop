---
title: Pipeline
weight: 2
---

This page follows the cells of notebook 04 in order. Each code cell is quoted with the output it produced when the notebook was executed on 15 October 2026 with `nishad/apertus:8b` (the 16 GB tier). Where the 8 GB tier differed, the page says so and quotes the 8 GB copy in `tier-8gb/`. The notebook's HTML answers are shown here as plain text. Long outputs are cut and marked with "…".

The corpus is two documents in `data/docs/`: the IFLA Library Reference Model and the DCMI Metadata Terms, both CC BY 4.0, as text extracts.

## 04.01 Configuration

```python
import os
os.environ.setdefault("WORKSHOP_TIER", "16gb")
from workshop.config import load_settings, context_limit
settings = load_settings(); MODEL = settings.model; EMBED_MODEL = settings.embed_model
LIMIT = context_limit(MODEL)
K = 3 if LIMIT <= 4096 else 4         # fewer chunks on the 4B's 4k window
print("Model:", MODEL, "| context:", LIMIT, "| chunks per question:", K)
```

```text
Model: nishad/apertus:8b | context: 8192 | chunks per question: 4
```

From the executed notebook 04, 15 October 2026. `K` is the number of chunks per question. On the 8 GB tier the same cell printed `Model: nishad/apertus:4b | context: 4096 | chunks per question: 3`, from the executed notebook 04 on the 8 GB tier, 15 October 2026. The 4B has a 4,096-token window, so it gets one chunk fewer.

## 04.02 Load and chunk

```python
from pathlib import Path
from workshop.rag import load_document, chunk_text
chunks = []
for path in sorted(Path("data/docs").glob("*.md")):
    text = load_document(str(path))
    chunks += chunk_text(text, source=path.stem, size=300, overlap=50)
by_id = {c.id: c for c in chunks}
print(len(chunks), "chunks from", len(set(c.source for c in chunks)), "documents")
print(chunks[5].id, "→", chunks[5].text[:200], "...")
```

```text
173 chunks from 2 documents
dcmi-terms#5 → The distinction between titles and alternative titles is application-specific. Has Range http://www.w3.org/2000/01/rdf-schema#Literal Subproperty of Title (http://purl.org/dc/elements/1.1/title) Title ...
```

From the executed notebook 04, 15 October 2026. Two documents became 173 chunks of about 300 words with 50 words of overlap. The id `dcmi-terms#5` is the source and the position, which a citation points back to. Notice that chunk 5 starts in the middle of a term's description: the chunker cuts on word counts, not on the document's structure.

## 04.03 Embed once

```python
import time
from workshop.search import build_index, search
t = time.time()
index = build_index([c.id for c in chunks], [c.text for c in chunks], model=EMBED_MODEL)
print(f"indexed {len(chunks)} chunks in {time.time()-t:.0f} s")
```

```text
indexed 173 chunks in 17 s
```

From the executed notebook 04, 15 October 2026. The embedding model is `qwen3-embedding:0.6b`. The index lives in memory for the session, so closing the notebook discards it. The 17 seconds are the time on the machine that executed the notebook; expect longer on a slower or CPU-only machine.

## 04.04 Look at what was retrieved first

```python
question = "Which DCMI term expresses the date on which a resource was formally issued?"
for cid, text, score in search(question, index, k=K):
    print(f"{score:.3f}  {cid}\n      {text[:160]}...\n")
```

```text
0.721  dcmi-terms#7
      Definition A point or period of time associated with an event in the lifecycle of the resource. Comment Date may be used to express temporal information at any ...

0.630  dcmi-terms#8
      property Date, of which this is a subproperty. Has Range http://www.w3.org/2000/01/rdf-schema#Literal Subproperty of Date (http://purl.org/dc/elements/1.1/date)...

0.612  dcmi-terms#6
      resource, spatial applicability of the resource, or jurisdiction under which the resource is relevant. Comment Spatial topic and spatial applicability may be a ...

0.601  dcmi-terms#24
      resource. ### FileFormat Class More details → URI http://purl.org/dc/terms/FileFormat Label File Format Definition A digital resource format. Subclass of http:/...
```

From the executed notebook 04, 15 October 2026. This is a retrieval failure. The expected answer is `dcterms:issued`, and none of the four chunks is the one that defines it. The top hit is the generic definition of Date; the others are neighbors about date subproperties, spatial coverage and file formats. The notebook says so before the answer: if the right passage is not in the top hits, no prompt can fix it.

## 04.05 Ask with the documents in the prompt

```python
from workshop.rag import answer, build_prompt
from workshop.display import show_markdown
text, used = answer(question, index, by_id, k=K, model=MODEL)
show_markdown(text)
print("\nCited material:")
for n, c in enumerate(used, 1):
    print(f"[{n}] {c.source}#{c.position}: {c.text[:100]}...")
```

```text
The DCMI term that expresses the date on which a resource was formally issued is "dateAccepted". This term is defined as "Date of acceptance of the resource. Comment Recommended practice is to describe the date, date/time, or period of time as recommended for the property Date, of which this is a subproperty. Examples of resources to which a date of acceptance may be relevant are a thesis (accepted by a university department) or an article (accepted by a journal)."

[1] and [2] do not provide information about the date on which a resource was formally issued. [3] and [4] do not provide information about the date on which a resource was formally issued.

Cited material:
[1] dcmi-terms#7: Definition A point or period of time associated with an event in the lifecycle of the resource. Comm...
[2] dcmi-terms#8: property Date, of which this is a subproperty. Has Range http://www.w3.org/2000/01/rdf-schema#Litera...
[3] dcmi-terms#6: resource, spatial applicability of the resource, or jurisdiction under which the resource is relevan...
[4] dcmi-terms#24: resource. ### FileFormat Class More details → URI http://purl.org/dc/terms/FileFormat Label File For...
```

From the executed notebook 04, 15 October 2026. The answer is wrong: `dateAccepted` is a different term. The model quotes a definition that is not in any of the four numbered chunks, and then says that none of the four chunks provides the information. Two lessons follow. First, the retrieval failure in 04.04 caused this; the model had no chance. Second, the answer has no citation marks on its first claim, and its own last sentences contradict it. A citation you cannot find in the cited material is a warning sign.

On the 8 GB tier the 4B, with three chunks, answered with the single line `Date (http://purl.org/dc/terms/date)`, which is also wrong (from the executed notebook 04 on the 8 GB tier, 15 October 2026).

## 04.06 When the documents are silent

```python
text, used = answer("Who won the 2026 Nobel Prize in Literature?", index, by_id, k=K, model=MODEL)
show_markdown(text)
```

```text
The documents do not answer the question. The question asks who won the 2026 Nobel Prize in Literature, but the documents are about bibliographic identities, context of use, and the recognition of distinct bibliographic identities. They do not contain information about the Nobel Prize in Literature or its winners.
```

From the executed notebook 04, 15 October 2026. This is the refusal the prompt asks for: the model says the documents do not answer, with a reason.

On the 8 GB tier the 4B did not refuse. Its whole answer was a bare citation:

```text
[2]
```

From the executed notebook 04 on the 8 GB tier, 15 October 2026. Chunk 2 is a passage from the library standards that says nothing about the prize. A smaller model follows the refusal instruction less reliably. When no cited passage supports an answer, do not trust it.

## 04.07 The context budget

System text, retrieved chunks, the question and the answer must all fit in the model's window: 8,192 tokens for the 8B tag and 4,096 for the 4B tag. The helper estimates the size and refuses to build an oversized prompt. Ollama has its own check. The cell asks for 40 chunks, which is far too many, and shows both.

```python
from workshop.rag import PromptTooLong
import ollama
many = [by_id[cid] for cid, _, _ in search(question, index, k=40)]
try:
    build_prompt(question, many, max_tokens=LIMIT)
except PromptTooLong as err:
    print("helper refused:", err)
try:
    big = "\n\n".join(c.text for c in many)[: int(LIMIT * 1.5 * 3.5)]   # about one and a half windows of text
    ollama.Client(host=settings.host).chat(model=MODEL, messages=[{"role": "user", "content": big + "\n\nSummarize."}],
                                          options={"num_ctx": LIMIT, "temperature": 0, "num_predict": 20})
    print("Ollama accepted the long prompt (it may have truncated silently; check num_ctx).")
except ollama.ResponseError as err:
    print("Ollama said:", err)
```

```text
helper refused: About 25842 tokens of prompt for a 8192-token window. Use fewer or shorter chunks (lower k or size).
Ollama said: {"error":{"code":400,"message":"request (10162 tokens) exceeds the available context size (8192 tokens), try increasing it","type":"exceed_context_size_error","n_prompt_tokens":10162,"n_ctx":8192}} (status code: 400)
```

From the executed notebook 04, 15 October 2026. The helper's number is an estimate (one token per 3.5 characters, deliberately high) of the whole prompt, and it keeps 25 percent of the window free for the system prompt and the answer. Ollama's number, 10,162 tokens, is a real count of the shorter text the cell sent. Both refuse.

The 8 GB tier behaved differently. The helper refused as before (`About 25842 tokens of prompt for a 4096-token window`), but then the cell printed `Ollama accepted the long prompt (it may have truncated silently; check num_ctx).` (from the executed notebook 04 on the 8 GB tier, 15 October 2026). Ollama's server log for that run recorded the 5,076-token prompt cut to 2,051 tokens. The part that was cut off is gone and nothing tells the model or you. The helper's refusal is the only guard you can rely on there.

## 04.08 Five questions, scored by you

The questions come from `data/docs/questions.json`. The score is a judgement, not a string match; that is deliberate. Each answer was cut at 400 characters by the notebook.

```python
import json
questions = json.loads(Path("data/docs/questions.json").read_text(encoding="utf-8"))
for q in questions:
    text, used = answer(q["question"], index, by_id, k=K, model=MODEL)
    print("Q:", q["question"]); print("A:", text.strip()[:400]); print("expected:", q["expected"]); print("-" * 80)
```

| Question | Expected | 8B answer (executed notebook 04, 15 October 2026) | 4B answer (8 GB tier) |
|---|---|---|---|
| Which four entities make up the IFLA LRM's work, expression, manifestation, item chain, and what does each one stand for? | work, expression, manifestation, item (the WEMI entities): the intellectual content, its realization, its physical embodiment, and a single exemplar | "The four entities that make up the IFLA LRM's work, expression, manifestation, item chain are: 1. Work: Represents the intellectual or artistic content, without consideration of its physical or digital embodiment. It is the abstract concept of the creative work. 2. Expression: Represents the realization of a work in a particular form of language or medium. It is the specific realization of the w…" | `[3]` |
| Which DCMI term expresses the date on which a resource was formally issued? | `dcterms:issued` | "The DCMI term that expresses the date on which a resource was formally issued is "dateAccepted". …" | `Date (http://purl.org/dc/terms/date)` |
| In the IFLA LRM, what is the difference between a manifestation and an item? | a manifestation is the set of all carriers sharing the same characteristics; an item is a single exemplar | "In the IFLA LRM, a manifestation is a set of items that reflect the characteristics of that manifestation. An item, on the other hand, is a physical entity that exemplifies a manifestation. The difference between a manifestation and an item is that a manifestation is a set of items, while an item is a single physical entity. For example, a book is a manifestation, and each copy of the book is an i…" | `[3]` |
| What is the range of dcterms:language? | `LinguisticSystem` | "The range of dcterms:language is Includes http://purl.org/dc/terms/LinguisticSystem [1]. This is specified in the document [1] which provides details on the dcterms:language property. The document [1] also mentions that the recommended practice is to use either a non-literal value representing a language from a controlled vocabulary such as ISO 639-2 or ISO 639-3, or a literal value consisting of…" | `[2]` |
| Who won the 2026 Nobel Prize in Literature? | not in the documents (the model must say so) | "The documents do not answer the question. The question asks who won the 2026 Nobel Prize in Literature, but the documents are about bibliographic identities, context of use, and the recognition of distinct bibliographic identities. They do not contain information about the Nobel Prize in Literature or its winners." | `[2]` |

My reading of the 8B column: question 1 starts correctly and the visible part matches the expected entities; question 2 is wrong, as in 04.05; question 3 gets the item right and the manifestation roughly right; question 4 names `LinguisticSystem`, though the opening sentence is awkward; question 5 refuses correctly. Four out of five are usable, and you only know which four by reading. On the 4B every answer is a bare citation or a wrong term, so none of them can be trusted. The 4B column is from the executed notebook 04 on the 8 GB tier, 15 October 2026.

## 04.09 Bring your own document

Drop a PDF, Markdown or text file into `data/my/` and run the cell. It chunks the files with the default sizes, builds an index, and asks one question. When you run it headless it asks a fixed question, "What is this document about?"; in a live session it waits for yours. On the executed run `data/my/` was empty, so the cell printed `Put a .pdf, .md or .txt file into data/my/ and run this cell again.`

{{< callout type="warning" >}}
Text is read as UTF-8. Two-column PDFs extract badly: the text of the left and right columns can interleave line by line. Print a few hundred characters of the extracted text and compare it with the page before you trust any answer.
{{< /callout >}}

## Three tiers

### GUI

LM Studio's Chat with Documents does this retrieval without code. Attach `dcmi-terms.md` from `data/docs/` (save a copy as `.txt` if the app does not accept `.md`) and ask the `dcterms:issued` question from 04.04. Compare the answer with 04.05 above. Does the app find the right term? Which chunks did it show you, if any?

### Run and change

Set `K = 1` and re-run 04.08. Which questions break? Then try `size=150` in 04.02, which makes the chunks smaller, and see whether the `dcterms:issued` question retrieves a better passage. Then ask the same question in German: does retrieval over English documents still find the passage?

### Stretch

Rerank. Ask the chat model, with `format=` and a tiny Pydantic model `{"relevant": bool, "reason": str}`, whether each of the top 10 chunks answers the question; keep only the relevant ones and answer again. Compare with 04.05. A second stretch: index this workshop's website pages (download them as Markdown) and ask the index about itself.

### On the 8 GB tier

The same notebook runs with `WORKSHOP_TIER=8gb`: three chunks per question and a 4,096-token window. Expect bare citations and no refusals, as above, and treat every answer as unchecked until you have read the cited chunk.

## What you should have now

You can turn documents into cited chunks, read the retrieved passages before the answer, see the model cite and refuse, and know what happens when a prompt does not fit. Next: [tool use](/v3/part2/06-tool-use), for the questions a document index cannot answer.
