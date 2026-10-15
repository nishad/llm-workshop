---
title: Concepts
weight: 1
---

Five ideas carry this chapter. Each is short.

## A JSON schema describes the shape of an answer

A JSON schema is a small JSON document that says which keys an answer has, what type each value is, and which values are allowed. It can also carry a description for each key. The model sees those descriptions, so they work as instructions.

## Pydantic is the way to write one in Python

You rarely write a schema by hand. Pydantic lets you write a class, and it produces the schema for you with `model_json_schema()` and parses an answer back with `model_validate_json()`. This is the `Record` model from notebook 02:

```python
from typing import Literal
from pydantic import BaseModel, Field

class Record(BaseModel):
    title: str = Field(max_length=200, description="Title proper as written on the card: the part before any ' : ' subtitle, without statement of responsibility")
    creators: list[str] = Field(max_length=6, description="Persons or bodies responsible, as written, surname first")
    place: str = Field(max_length=60, description="Place of publication, the part before the colon in the imprint line; empty string if the imprint has no place. Never guess it from the publisher")
    publisher: str = Field(max_length=100, description="Publisher name only, the part between the colon and the comma in the imprint line; empty string if absent")
    date: str = Field(max_length=20, description="Year of publication as written, for example 1774; empty string if the card says o.J. or s.d. or gives no year")
    language: Literal["de", "en", "fr", "it", "es", "ja", "other"] = Field(description="Language of the work")
    identifier: str = Field(max_length=60, description="ISBN or DOI if the card has one, digits and hyphens only (no 'ISBN' or 'doi:' prefix); empty string if none")
```

Three design choices are worth copying:

- Every free-text field has a `max_length`. It travels into the schema, and a small model with an open-ended string can run away.
- An empty string means "the card does not say". `Literal` limits the language to a fixed list.
- The fields follow the order of the card itself, and the descriptions are written as instructions.

### Why not `Optional` with `null`?

The notebook tried it, in October 2026. At temperature 0 the 8B model answered `null` for every optional field in turn, and then poured the whole imprint line into the first free-text field, sometimes repeating it until the window filled. Schema design is prompt design. The call also passes `options={"num_predict": 300}`, a hard ceiling on output tokens, so a runaway answer cannot eat the session.

## Enforced decoding: what `format=` guarantees

When you pass `format=Record.model_json_schema()`, Ollama constrains the model while it writes, so that only tokens that fit the schema can be chosen. This is grammar-enforced decoding.

| It guarantees | It does not guarantee |
|---|---|
| The output is well-formed JSON | The values are true |
| The keys are the ones in the schema | A number lies in a sensible range |
| Each value has the right type | A date is a real date |
| An enum or `Literal` value is one of the allowed ones | The model did not copy the wrong line into a field |

Shape is enforced; truth is not. That gap is the subject of the exercise.

## Validation rules encode what you know about the data

Pydantic can run your own checks after parsing. A rule such as "the place of publication is never identical to the publisher" is a few lines, and it catches a mistake the grammar cannot see.

## Retry with the error

When a rule fails, send the answer back with the error message and ask for a fix. The pattern is: call, validate, and on failure append the model's answer and the error to the conversation and call once more. One retry is usually enough, and you cap it so a stubborn case cannot loop.

## The OpenAI twin

The same extraction through the OpenAI client is one call: `oa.chat.completions.parse(model=MODEL, messages=..., response_format=Record)` returns `completion.choices[0].message.parsed`. See the [portability page](/v3/part2/02-python-and-ollama/portability) for the client set-up.

Next, [run it on real cards](/v3/part2/03-structured-output/exercise).
