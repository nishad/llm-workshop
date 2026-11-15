---
title: Wrap-up
weight: 7
---

Part 2 is done. You called a local model from Python, got structured records out of it, searched a vocabulary by meaning, answered from documents with citations, and let the model propose tool calls that a person approves. This page lists what to record so a result can be traced, what never to let the model do on its own, and where to go next.

## The provenance checklist

For any result you may use later, write down:

- [ ] **Model tag and digest.** For example `nishad/apertus:8b`, digest `4a85a6fea0b8` (`ollama list` shows it). A tag can be rebuilt; the digest says which build you used.
- [ ] **Options.** Temperature, `num_ctx`, and any others you set. The notebooks' helper uses temperature 0 and the tier's context size.
- [ ] **Prompt.** The system prompt and the user prompt, in full, with the instructions and the schema if you used one.
- [ ] **Data version.** Which documents, which vocabulary release, which index file, and when you retrieved them.
- [ ] **Date.** When the run happened. Services and models change.
- [ ] **Who approved what.** Which tool calls a person approved, corrected or refused, and who checked which outputs.

Most of this is recorded for you automatically. Every `workshop.llm.chat` call appends a line to `runs/log.jsonl` with the time, the model and its digest, the options, and the end of the prompt and the start of the answer. The RAG helper, the tool loop and the setup check go through the same function, so they are logged too. What is and is not logged is on the [reproducibility page](/v3/part2/02-python-and-ollama/reproducibility). Keep the file with your results.

## What never to let the model do unreviewed

- **Invent identifiers.** A model will produce a number that looks like a GND number. The October 2026 runs showed it, and the loop marked the invented numbers as `[UNVERIFIED]`. An identifier belongs in a record only if a service returned it and a person saw it.
- **Write to the catalog.** Let the model propose a record, then have a person review and load it.
- **Assign subject headings on its own.** Let the model suggest candidates from a vocabulary, as in the embeddings chapter, and let a cataloger accept or reject them.

The pattern throughout Part 2 is the same: the model proposes, a check catches what it can, and a person decides.

## Take-home

Every notebook is committed with its executed outputs, so you can read it later without running anything. The [notebooks page](/v3/part2/notebooks) lists all six with links. The `tier-8gb/` folder holds notebooks 04 and 05 as executed on the 8 GB tier, so you can see how the smaller model behaves.

## Next steps

- [Next steps](/v3/resources/next-steps): library tasks to try, tools to look at, communities.
- [Model guide](/v3/resources/models): the models, their sizes and measured behavior.
- [Library endpoints](/v3/resources/endpoints): services you can call from the tool loop, and the etiquette.
- [Data and licenses](/v3/resources/data): what is in `data/` and under which terms.
- [FAQ](/v3/resources/faq) and [Glossary](/v3/resources/glossary).

## At SWIB26

The workshop is part of SWIB26, on 16 November 2026, alongside the conference sessions of that day. The program is on the SWIB site; questions about this workshop go to the [forum topic](https://forum.swib.org/t/getting-started-with-local-llms/1732). The [next steps page](/v3/resources/next-steps) names the sessions that fit this topic.
