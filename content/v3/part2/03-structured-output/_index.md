---
title: Structured output
weight: 3
cascade:
  type: docs
---

A catalog wants fields: a title, a creator, a place, a year. A chat answer gives you a paragraph. A person can read a paragraph. A spreadsheet, a record store or a validation script cannot. This chapter makes the model fill a fixed set of fields instead, and then checks every answer.

Notebook 02, `02_structured_output`, has a 25-minute budget; in the session it gets about 22 (minutes 28 to 50 of Part 2). We give the model a catalog card, get a record back, watch it invent a value the card never stated, add a rule that catches the invention, and then measure twenty cards against a gold file.

## What the notebook covers

1. Define the shape of the answer as a Pydantic model and hand its JSON schema to the model.
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
