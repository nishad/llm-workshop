---
title: Concepts
weight: 1
---

## A JSON schema describes the shape of an answer

A JSON schema is a small JSON document that says which keys an answer has, what type each value is, and which values are allowed. It can also carry a description for each key. The model sees those descriptions, so they work as instructions.

## Pydantic is the way to write one in Python

You rarely write a schema by hand. Pydantic is a Python library that defines data shapes as classes and checks data against them. You write a class, and Pydantic produces the schema for you with `model_json_schema()`. It also parses an answer back into the class with `model_validate_json()`. This is the `Record` model from notebook 02:

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

Four design choices are worth copying:

- Every free-text field has a `max_length`, and that limit goes into the schema. Without a limit, a small model can keep writing into a string field and never stop.
- An empty string means "the card does not say".
- `Literal` limits the language to a fixed list.
- The fields follow the order of the card itself, and the descriptions are written as instructions.

### Why not `Optional` with `null`?

We tried it in the notebook in October 2026. At temperature 0, the least random setting, the 8B model answered `null` for every optional field, one after another. It then wrote the whole imprint line into the first free-text field, sometimes repeating it until the context window was full. The schema works as part of the prompt, so how you design it changes the answers. The extraction call in the notebook also passes `options={"num_predict": 300}`, a hard limit on the number of output tokens. That way, an answer that does not stop cannot block the rest of the session.

## Enforced decoding: what `format=` guarantees

When you pass `format=Record.model_json_schema()`, Ollama limits the model's choices while it writes: at each step, the model can choose only tokens that fit the schema. This is called grammar-enforced decoding.

| It guarantees | It does not guarantee |
|---|---|
| The output is well-formed JSON | The values are true |
| The keys are the ones in the schema | A number lies in a sensible range |
| Each value has the right type | A date is a real date |
| An enum or `Literal` value is one of the allowed ones | The model did not copy the wrong line into a field |

Shape is enforced; truth is not. That gap is the subject of the exercise.

## Validation rules encode what you know about the data

Pydantic can run your own checks after parsing. A rule such as "the place of publication is never the same as the publisher" takes a few lines of code, and it catches a mistake the grammar cannot see.

## Retry with the error

When a rule fails, send the answer back with the error message and ask for a fix. The pattern goes like this: call the model and validate the answer. If validation fails, add the model's answer and the error to the conversation, then call once more. One retry is usually enough. Set a limit on retries, so a case that never passes cannot loop forever.

## The same call through the OpenAI client

The same extraction through the OpenAI client is one call: `oa.chat.completions.parse(model=MODEL, messages=..., response_format=Record)` returns `completion.choices[0].message.parsed`. See the [portability page](/v3/part2/02-python-and-ollama/portability) for the client setup.

Next, [run it on real cards](/v3/part2/03-structured-output/exercise).
