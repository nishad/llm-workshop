---
title: "Part 1: Fundamentals"
weight: 10
sidebar:
  open: true
cascade:
  type: docs
---

Part 1 runs from 04:00 to 06:00 UTC. It needs no programming: everything is done in a chat window.

## Learning outcomes

After Part 1 you can:

1. Explain next-token prediction, tokens, context window, parameters and quantization in plain words, and connect them to file size, memory and speed.
2. Place a model on the four-tier openness ladder and say why libraries care (provenance, reproducibility, vendor independence).
3. Install Ollama or LM Studio, configure privacy settings, download a model that fits your hardware and verify it works.
4. Write and iteratively improve prompts for cataloguing-style tasks.
5. Recognize a confident wrong answer and know two checks for it.

## Timeline

Minutes are counted from 04:00 UTC.

| Minutes | Segment | Mode |
|---|---|---|
| 0-10 | Welcome: what changed since 2024, why libraries care, how the four hours work, how to get help (shared document, Zoom reactions) | demo |
| 10-35 | How an LLM works: next-token prediction; tokens (live tokenizer, multilingual costs); context window and its memory cost; parameters and quantization (file size equals memory); live `ollama ps` | demo with prediction checks |
| 35-55 | Open source, open weights, fully open: the ladder; Apertus as the case; the EU public summary; "was my library in the training data?" | demo |
| 55-80 | Setup recap and privacy settings; first chat with Apertus in the Ollama app or LM Studio; choosing a model size; measure your own speed | type-along (GUI) |
| 80-110 | Prompting for library tasks: anatomy, iterative refinement, few-shot classification, structured answers, multilingual prompts, the hallucination probe | exercise (three tiers) |
| 110-120 | Recap, self-check, what Part 2 assumes, how to leave or join at the break | demo |

## Three ways to take part

GUI-only (all of Part 1, Part 2 as a reader), run the notebooks (Part 2), or read the executed notebooks afterwards (both parts).

## The chapters

{{< cards >}}
  {{< card link="/v3/part1/01-how-llms-work" title="How an LLM works" icon="chip" subtitle="Tokens, context, parameters, quantization, temperature." >}}
  {{< card link="/v3/part1/02-open-models" title="Open models" icon="book-open" subtitle="Open source, open weights, fully open." >}}
  {{< card link="/v3/part1/03-first-chat" title="First chat" icon="chat" subtitle="Talk to Apertus on your own machine." >}}
  {{< card link="/v3/part1/04-prompting" title="Prompting" icon="pencil" subtitle="Prompts for library tasks." >}}
  {{< card link="/v3/part1/05-wrap-up" title="Wrap-up" icon="check-circle" subtitle="Recap and what Part 2 assumes." >}}
{{< /cards >}}

{{< callout type="success" >}}
You are ready for Part 1 if the model answers in your chat window.
{{< /callout >}}
