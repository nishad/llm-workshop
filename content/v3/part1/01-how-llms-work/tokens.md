---
title: Tokens
weight: 2
---

A model does not read words. It reads **tokens**: pieces of text, some whole words, some word fragments, some single characters or digits.

Think of tokens as bricks. A house is built from bricks, and a sentence is built from tokens. Common words are often one brick; rare or long words are assembled from several.

## What things cost

Counts with the Apertus tokenizer unless stated otherwise. Models are named where their count differs.

| Text | Tokens |
|---|---|
| The library catalogue contains three million records. | 8 (the same in Llama, Gemma and Qwen) |
| Der Bibliothekskatalog enthält drei Millionen Datensätze. | 11 (Llama: 14) |
| The French and Italian versions of the same sentence | 11 each |
| The Japanese version (26 characters) | 22 (Gemma: 13) |
| The Arabic version | 11 |
| The Hindi version | 18 |
| `1234567890` | 10 (digit by digit; Llama: 4) |
| An ISBN, `978-3-16-148410-0` | 17 |
| A DOI, `10.1000/182` | 11 |
| Donaudampfschifffahrtsgesellschaftskapitän | 14 |
| `a b` | 2 |
| `a    b` (four spaces) | 3 |
| A 131-character SPARQL query | about 50 |
| A MARC 245 field | 29 to 34 |
| Two emoji | 8 |

The SPARQL query costs about twice as many tokens per character as ordinary prose.

## Why it matters

- **Context costs tokens.** Everything you send and everything the model answers counts against the [context window](/v3/part1/01-how-llms-work/context).
- **Identifiers are brittle.** An ISBN or a DOI is split into many small pieces, so the model handles it as a string of fragments, not as one thing. Copying one exactly is harder than it looks.
- **Languages are not equal.** Depending on the tokenizer, non-English text can cost noticeably more. The Apertus tokenizer was chosen for coverage of 55 languages, so its counts for German, Japanese and Hindi stay modest.

## Try it

Paste your own sentences into the [tiktokenizer playground](https://tiktokenizer.vercel.app/) to see how the GPT and Llama tokenizers split them. Part 2 shows the real count for any text you send: the response object's `prompt_eval_count` and `eval_count` fields (see [Basics](/v3/part2/02-python-and-ollama/basics)).
