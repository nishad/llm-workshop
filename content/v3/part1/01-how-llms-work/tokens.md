---
title: Tokens
weight: 2
---

A model does not read words. It reads **tokens**: pieces of text, some whole words, some word fragments, some single characters or digits.

Common words are usually one token. Rare or long words, names and identifiers are made of several tokens, and the pieces are rarely the ones a person would choose.

## What things cost

Counts are for the Apertus tokenizer, the set of rules that Apertus uses to cut text into tokens. Where another model's tokenizer gives a different count, it is shown in parentheses.

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

- **Context costs tokens.** Everything you send and everything the model answers uses up part of the [context window](/v3/part1/01-how-llms-work/context), the model's working memory.
- **Identifiers are fragile.** An ISBN or a DOI is split into many small pieces, so the model handles it as a series of fragments, not as one thing. Copying one exactly is harder than it looks.
- **Languages are not equal.** Depending on the tokenizer, text in other languages can cost noticeably more than English. The Apertus tokenizer was built to cover many languages well, so its counts for German, Japanese and Hindi stay moderate.

## Try it

Paste your own sentences into the [tiktokenizer playground](https://tiktokenizer.vercel.app/) to see how the GPT and Llama tokenizers split them. Part 2 shows the real count for any text you send. The response you get back carries it in two fields, `prompt_eval_count` and `eval_count` (see [Basics](/v3/part2/02-python-and-ollama/basics)).
