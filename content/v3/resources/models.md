---
title: Model guide
weight: 1
---

Every model the workshop uses or mentions, with the facts that decide whether it suits your machine. Measurements were made in October 2026 on Ollama 0.35.1 and repeated on 0.40.4 with identical counts. To choose a model for your memory size, start with [Choose a model size for your hardware](/v3/before-you-start/hardware).

## Apertus models

Apertus is the fully open model family from the Swiss AI Initiative (EPFL, ETH Zurich, CSCS). The workshop tags below are built by the facilitator from community GGUF files; the Modelfiles are in the notebooks repository under `models/`. All three tags set `temperature 0.8` and `top_p 0.9`.

### `nishad/apertus:8b`

The reference model for both parts. Also available as `nishad/apertus:latest`.

| Field | Value |
|---|---|
| Model | Apertus-8B-Instruct-2509, Unsloth Q4_K_M |
| Parameters | 8 billion |
| Size | 5.06 GB |
| Memory in use | about 5.3 GB at 4,096 and 5.8 GB at 8,192 context |
| Context | 65,536 tokens supported; 8,192 set in the tag |
| License | Apache-2.0 plus the Apertus Acceptable Use Policy |
| Openness tier | Fully open (tier 3) |
| Digest | `4a85a6fea0b8` |
| Source | `hf.co/unsloth/Apertus-8B-Instruct-2509-GGUF:Q4_K_M` |
| GGUF sha256 | `87e7f0eb5a1d33e1a8ea4e7fdd2363764e0465061dd92962e0073aec31a7944d` |

Good at: extracting fields from catalog-style text, German, French and Italian, structured output, and calling tools when the prompt is in English. Weak at: code, math and following instructions (an IFEval benchmark score of 71.7). When a field is missing it sometimes fills it from a neighboring field, such as the publisher as the place (see notebook 02). It uses the GGUF's own chat template with Unsloth's fixes for tool arguments.

### `nishad/apertus:4b`

For 8 GB machines.

| Field | Value |
|---|---|
| Model | Apertus v1.1 4B Instruct, Q4_K_M |
| Parameters | 4 billion |
| Size | 2.43 GB |
| Memory in use | about 2.8 GB |
| Context | 4,096 tokens (hard limit) |
| License | Apache-2.0 weights, with the Apertus LLM Acceptable Use Policy |
| Openness tier | Fully open (tier 3) |
| Digest | `87ca69a79aed` |
| Source | `hf.co/jondale/Apertus-v1.1-4B-Instruct-GGUF:Q4_K_M` |
| GGUF sha256 | checksum not recorded |

The tag uses a workshop wrapper template that renders tools in Apertus's TypeScript-style format, so Ollama can parse tool calls. Without it, tool requests hang. Quality is visibly below the 8B: in testing it could not recall a fact from the previous turn, nor find one fact hidden in a 2,300-token text.

### `nishad/apertus:8b-v1.5-preview`

An optional preview for people with 16 GB or more who want to compare.

| Field | Value |
|---|---|
| Model | Apertus v1.5 8B, text only, Q4_K_M |
| Parameters | 8 billion |
| Size | 5.06 GB |
| Memory in use | as the 8B |
| Context | 8,192 set in the tag; the file's metadata says 262k |
| License | Apache-2.0, with the Apertus Acceptable Use Policy v1.5 (14 July 2026) |
| Openness tier | Fully open (tier 3) for Apertus 1.5 itself |
| Digest | `6f25f6ba0b62` |
| Source | `hf.co/Colby/apertus-v1.5-8b-text-Q4_K_M-GGUF:Q4_K_M` |
| GGUF sha256 | `a037df8d87ff6caacee794ee85f55342f2152e0d359b7389033300c3bee5f299` |

This is an unofficial community conversion. Someone extracted the text part of the gated multimodal v1.5 checkpoint; vision and audio are removed, and no parity check against the original exists. Thinking is not available in Ollama. The 262k metadata means a large Mac would allocate far more memory than you expect, so set the context yourself (the tag does). In testing it scored slightly better on tool calls than the 8B.

{{< callout type="info" >}}
A community audit of the published v1.5 fine-tuning data in September 2026 found benchmark items and duplicates; see [Apertus](/v3/part1/02-open-models/apertus#an-audit-in-september-2026).
{{< /callout >}}

## Verification of the tags

Run on Ollama 0.35.1 and repeated on 0.40.4 on 15 October 2026 with identical counts, one run per model through the OpenAI-compatible endpoint.

| Tag | Tool prompts with a structured call | Controls clean | Multi-turn loops | Structured output |
|---|---|---|---|---|
| `nishad/apertus:8b` | 16 of 20 | 10 of 10 | 5 of 5 | 5 of 6 |
| `nishad/apertus:4b` | 11 of 20 | 10 of 10 | 3 of 5 | 5 of 6 |

The one structured-output request that fails is a schema with an empty enum, which the server rejects with HTTP 400 as expected. The 4B fills a missing ISBN with the text `"2 Bände"`; the 8B correctly returns null.

## Embedding models

Embedding models turn text into vectors for semantic search (see [Glossary](/v3/resources/glossary)). The workshop default is `qwen3-embedding:0.6b`. It had the best result among the openly licensed models on a gold set built for this workshop: 50 queries over the STW Thesaurus for Economics and the UNESCO Thesaurus, evaluated in October 2026.

| Model | License | Size | Dimensions | Context | Prefixes | recall@1 | recall@5 |
|---|---|---|---|---|---|---|---|
| `qwen3-embedding:0.6b` (default) | Apache-2.0 | 639 MB | 1,024 | 32k tokens | instruction prefix on queries, added by the notebooks' helper | 0.62 | 0.82 |
| `embeddinggemma` | Google's Gemma Terms of Use, not an open-source license | 621 MB | 768 | not recorded here | task-string prefixes | 0.68 | 0.92 |
| `bge-m3` | MIT | 1.2 GB | 1,024 | 8k tokens | none | 0.34 | 0.48 |

`embeddinggemma` scored higher but its license is not an open-source one, so it is a documented alternative. `bge-m3` is permissively licensed and its fine-tuning data is released, but it scored lowest on this gold set. Index design matters as much as the model; notebook 03 shows the difference.

Apertus has no embedding model; the workshop uses `qwen3-embedding:0.6b` beside it.

## Small open-weight fallbacks

These are open weights only: the weights are downloadable and the license is Apache-2.0, but training data and code are not fully open. Use them only if no Apertus tag runs on your machine.

| Tag | License | Size | Note |
|---|---|---|---|
| `qwen3.5:4b` | Apache-2.0 | 3.3 GB | Thinking must be switched off |
| `granite4.1:3b` | Apache-2.0 | 2.1 GB | Smallest option |

## Ollama commands

| Command | What it does |
|---|---|
| `ollama list` | Show downloaded models with their digests |
| `ollama pull NAME` | Download a model |
| `ollama rm NAME` | Delete a model |
| `ollama show NAME` | Show details, template and capabilities |
| `ollama ps` | Show models loaded in memory |
| `ollama stop NAME` | Unload a model from memory |

## What may change after October 2026

These facts were checked in October 2026 and will be checked again the week before the workshop. Each would change something for you:

- An official Apertus entry in the Ollama library, or an official GGUF from the Apertus team, would replace the community builds behind the workshop tags.
- Support for the v1.5 architecture in llama.cpp and Ollama would make the preview tag unnecessary.
- New releases in the swiss-ai collection on Hugging Face may add sizes or versions.
