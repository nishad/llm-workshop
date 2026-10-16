---
title: Structured output
weight: 3
cascade:
  type: docs
---

A catalog needs separate fields: a title, a creator, a place, a year. A chat answer gives you a paragraph. A person can read a paragraph, but a spreadsheet, a record store or a validation script cannot. This chapter makes the model fill a fixed set of fields instead, and then checks every answer. That is what structured output means: an answer in a fixed format that a program can read.

Notebook 02, `02_structured_output`, has a 25-minute budget. In the session it gets about 22 minutes, from minute 28 to minute 50 of Part 2. We give the model a catalog card and get a record back. Then we watch it invent a value the card never stated, and we add a rule that catches the invention. Finally, we measure twenty cards against a gold file, which holds the correct answers.

## What the notebook covers

1. Define the shape of the answer as a Pydantic model, a Python class that lists the fields and their types. Hand its JSON schema to the model.
2. Validate what comes back, and learn what grammar-enforced output does and does not guarantee.
3. See the model invent a missing field, and add a rule that catches it.
4. Run twenty cards in a batch and measure field accuracy against a gold file.

{{< callout type="info" >}}
A small model will confidently fill a field the card is silent about. Valid JSON is not the same as a true record, so every extraction in this chapter is checked.
{{< /callout >}}

## The pages

{{< cards >}}
  {{< card link="/v3/part2/03-structured-output/concepts" title="Concepts" icon="template" subtitle="JSON schema, Pydantic, enforced decoding and the retry." >}}
  {{< card link="/v3/part2/03-structured-output/exercise" title="Exercise" icon="clipboard-check" subtitle="One card, one invented place, twenty cards measured." >}}
{{< /cards >}}

Setup is on the [environment page](/v3/part2/01-environment) and the notebooks are listed on the [notebooks page](/v3/part2/notebooks).
