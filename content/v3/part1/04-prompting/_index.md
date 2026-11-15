---
title: Prompting
weight: 4
cascade:
  type: docs
---

Prompting is how you tell a model what you want. This chapter is the main exercise block of Part 1 (minutes 80 to 110). You need only the chat window from the previous chapter. Nothing here needs programming.

Every example output on these pages was captured with thalhath/apertus:8b at temperature 0.8, on 15 October 2026. Temperature is the setting that controls how much the answers vary, so yours will differ in wording. The lessons hold anyway, and the places where the model gets it wrong are kept on purpose.

## The anatomy of a prompt

A good prompt has up to five parts. Only the instruction is required.

1. **Context**: background the model needs.
2. **Instruction**: what you want done.
3. **Input**: the text or data to work on.
4. **Output format**: how the answer should look.
5. **Constraints**: limits and rules.

Here is one prompt with all five parts, marked with bracket tags:

```
[Context] You are an expert librarian helping students.

[Instruction] Extract all books from the following text.

[Input] {text about books}

[Output format] Return a bullet list with: Title, Author, Year.

[Constraints] Only include books published after 1900.
```

You do not need the brackets in real use. They are here to show the five jobs a prompt can do.

## What is live and what is self-study

| Part | Live (in the session) | Self-study (afterwards) |
|---|---|---|
| Basics | The sample text, four versions of one prompt, five principles | The checklist, for your desk |
| Techniques | Few-shot, role and system prompt, structured answers, constraints, multi-step | Chain-of-thought, negative prompting, templates, comparative prompts, iterative refinement |
| Exercises | 1 (table), 2 (few-shot), 4 (multilingual terms), 6 (hallucination probe) | 3, 5, 7, 8 |
| Limits | Read the five examples | Run your own versions |

If you want the background on why models behave this way, see the [prompting mindset](/v3/part1/01-how-llms-work#the-prompting-mindset).

## The pages

{{< cards >}}
  {{< card link="/v3/part1/04-prompting/basics" title="Basics" icon="pencil" subtitle="The sample text, four versions of one prompt, five principles." >}}
  {{< card link="/v3/part1/04-prompting/techniques" title="Techniques" icon="adjustments" subtitle="Few-shot, roles, structured answers, constraints, multi-step." >}}
  {{< card link="/v3/part1/04-prompting/exercises" title="Exercises" icon="clipboard-list" subtitle="Eight exercises with three tiers each." >}}
  {{< card link="/v3/part1/04-prompting/limits" title="Limits" icon="exclamation" subtitle="What small local models get wrong, with captured examples." >}}
{{< /cards >}}
