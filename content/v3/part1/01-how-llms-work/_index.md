---
title: How an LLM works
weight: 1
cascade:
  type: docs
---

A large language model does one thing: it predicts the next token, again and again.

```mermaid
flowchart LR
  A[Your text] --> B[Tokens]
  B --> C[Model: 8 billion learned numbers]
  C --> D[Probabilities for the next token]
  D --> E[Pick one]
  E --> B
```

The chosen token is added to the text, and the loop runs again until the answer is complete.

## The prompting mindset

When you work with an LLM, think of it as:

- **Literal**: it does exactly what you ask, not what you mean.
- **Context-dependent**: it uses only the information you provide.
- **A pattern matcher**: it generates text based on patterns learned from training data.
- **Non-deterministic** (usually): the same prompt can yield different responses.

{{< callout type="info" >}}
LLMs don't understand in the human sense; they predict likely continuations. Effective prompting works with this behavior, not against it.
{{< /callout >}}

## Before you read on

Will the German sentence cost more or fewer tokens than the English one? Make a guess, then open the first page.

## The pages

{{< cards >}}
  {{< card link="/v3/part1/01-how-llms-work/tokens" title="Tokens" icon="puzzle" subtitle="Text in pieces, and what each piece costs." >}}
  {{< card link="/v3/part1/01-how-llms-work/context" title="Context" icon="document-text" subtitle="The working memory of the model." >}}
  {{< card link="/v3/part1/01-how-llms-work/parameters-and-quantization" title="Parameters and quantization" icon="chip" subtitle="From learned numbers to file size." >}}
  {{< card link="/v3/part1/01-how-llms-work/temperature" title="Temperature" icon="adjustments" subtitle="How random the pick is." >}}
{{< /cards >}}
