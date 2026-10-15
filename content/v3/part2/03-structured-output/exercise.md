---
title: Exercise
weight: 2
---

This page follows sections 02.03 to 02.05 of notebook 02. Each code cell is quoted with the output it produced when the notebook was executed on 15 October 2026. The `Record` model is on the [concepts page](/v3/part2/03-structured-output/concepts). On the 16 GB tier `MODEL` is `nishad/apertus:8b`.

## One card, one record

The helper sends the card with instructions and the schema, at temperature 0.

```python
from pathlib import Path
from workshop.llm import chat

INSTRUCTIONS = ("Extract the bibliographic record from this catalogue card into the JSON schema. A card has these lines: "
                "the creator (surname first); the title; the imprint as 'Place : Publisher, year'; the extent; sometimes an identifier. "
                "Copy each value as written into its own field. Use an empty string for a field the card does not state; "
                "never guess a place or year.")

def extract(card_text: str, model: str = MODEL) -> Record:
    response = chat(
        [{"role": "user", "content": f"{INSTRUCTIONS}\n\nCard:\n{card_text}"}],
        model=model, format=Record.model_json_schema(), options={"num_predict": 300},
    )
    return Record.model_validate_json(response.message.content)

card = Path("data/cards/card-01.txt").read_text(encoding="utf-8")
print(card)
print(extract(card).model_dump())
```

```text
Goethe, Johann Wolfgang von
Die Leiden des jungen Werthers : Roman
Leipzig : Weygandsche Buchhandlung, 1774
2 Teile in 1 Bd. ; 8°

{'title': 'Die Leiden des jungen Werthers : Roman', 'creators': ['Goethe, Johann Wolfgang von'], 'place': 'Leipzig', 'publisher': 'Weygandsche Buchhandlung', 'date': '1774', 'language': 'de', 'identifier': ''}
```

From the executed notebook 02, 15 October 2026. The structure is perfect and most values are right. Note that the title still carries its subtitle ` : Roman`, although the description asked for the title proper. That slip comes back in the accuracy count below.

## A card that is silent about the place

Card 03 has no place of publication. The imprint line is only `Gallimard, 1949`.

```python
card3 = Path("data/cards/card-03.txt").read_text(encoding="utf-8")
print(card3)
rec3 = extract(card3)
print(rec3.model_dump())
print("place should be empty; the model said:", repr(rec3.place))
```

```text
Beauvoir, Simone de
Le deuxième sexe. I, Les faits et les mythes
Gallimard, 1949
395 p. ; 19 cm
Collection Folio essais

{'title': 'Le deuxième sexe. I, Les faits et les mythes', 'creators': ['Beauvoir, Simone de'], 'place': 'Gallimard', 'publisher': 'Gallimard', 'date': '1949', 'language': 'en', 'identifier': ''}
place should be empty; the model said: 'Gallimard'
```

From the executed notebook 02, 15 October 2026. Valid JSON, wrong fact: the model filled the missing place with the publisher's name. (It also labeled a French book `en`.) In the October 2026 tests both Apertus builds did this. The grammar cannot catch it, so a rule has to.

## A rule and a retry

`CheckedRecord` adds one validator. `extract_checked` feeds the error back once.

```python
from pydantic import ValidationError, model_validator

class CheckedRecord(Record):
    @model_validator(mode="after")
    def place_is_not_publisher(self):
        if self.place and self.publisher and self.place.strip().lower() == self.publisher.strip().lower():
            raise ValueError("place equals publisher; the card probably has no place")
        return self

def extract_checked(card_text: str, model: str = MODEL, retries: int = 1) -> CheckedRecord:
    messages = [{"role": "user", "content": f"{INSTRUCTIONS}\n\nCard:\n{card_text}"}]
    last_error: ValidationError | None = None
    for attempt in range(retries + 1):
        response = chat(messages, model=model, format=CheckedRecord.model_json_schema(), options={"num_predict": 300})
        try:
            return CheckedRecord.model_validate_json(response.message.content)
        except ValidationError as err:
            last_error = err
            print(f"attempt {attempt + 1}: validation failed: {err.errors()[0]['msg']}")
            messages += [{"role": "assistant", "content": response.message.content},
                         {"role": "user", "content": f"The record failed validation: {err.errors()[0]['msg']}. Fix it and return the JSON again. Use an empty string where the card is silent."}]
    raise last_error

print(extract_checked(card3).model_dump())
```

```text
attempt 1: validation failed: Value error, place equals publisher; the card probably has no place

{'title': 'Le deuxième sexe. I, Les faits et les mythes', 'creators': ['Beauvoir, Simone de'], 'place': '', 'publisher': 'Gallimard', 'date': '1949', 'language': 'en', 'identifier': ''}
```

From the executed notebook 02, 15 October 2026. The rule caught the invented place and the retry returned an empty one. The wrong language is still there: no rule looked at it.

## Twenty cards, measured

Run every card, write a CSV and compare with the gold file.

```python
import csv, json
gold = {g["file"]: g for g in json.loads(Path("data/cards/cards-gold.json").read_text(encoding="utf-8"))}
rows, correct, total = [], 0, 0
for path in sorted(Path("data/cards").glob("card-*.txt")):
    rec = extract(path.read_text(encoding="utf-8"))
    rows.append({"file": path.name, **rec.model_dump()})
    g = gold[path.name]
    for field in ("title", "date", "place", "publisher", "language", "identifier"):
        total += 1
        correct += (str(getattr(rec, field) or "").strip().lower() == str(g[field] or "").strip().lower())
Path("runs").mkdir(exist_ok=True)
with open("runs/cards-extracted.csv", "w", newline="", encoding="utf-8") as fh:
    writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); writer.writeheader(); writer.writerows(rows)
print(f"{len(rows)} cards, field accuracy {correct}/{total} = {correct/total:.0%}; wrote runs/cards-extracted.csv")
```

```text
20 cards, field accuracy 97/120 = 81%; wrote runs/cards-extracted.csv
```

{{< callout type="success" >}}
**What you should see:** `20 cards, field accuracy 97/120 = 81%`. If your number is far from that, check that `MODEL` is the 8B tag.
{{< /callout >}}

Which fields fail most? This is where a human reviewer should look first.

```python
from collections import Counter
misses = Counter()
for row in rows:
    g = gold[row["file"]]
    for field in ("title", "date", "place", "publisher", "language", "identifier"):
        if str(row[field] or "").strip().lower() != str(g[field] or "").strip().lower():
            misses[field] += 1
print(misses.most_common())
```

```text
[('title', 7), ('language', 7), ('identifier', 4), ('place', 4), ('publisher', 1)]
```

From the executed notebook 02, 15 October 2026. Title and language are where the 8B slips most. It copies the subtitle after ` : ` although the description asks for the title proper, and it guesses the language of a French or Italian book as English from the imprint. A field description is a hint, not a guarantee; that is what the gold file and a human reviewer are for. The count is a measure of how much review the field needs.

## Three tiers

### GUI

Paste the text of `data/cards/card-03.txt` into the Ollama app together with the `INSTRUCTIONS` text from the first cell above and the field list from the `Record` model, and see whether the model invents a place of publication. Compare the answer with the enforced version above. Is its JSON always well-formed?

### Run and change

Add a field `pages: str = Field(default="", max_length=40, ...)` with a description, and re-run the single-card cell on `card-02.txt`. Did the model copy "375 S."? Then change `INSTRUCTIONS` to ask for the title in English translation, and decide whether that is extraction or invention.

### Stretch

Add `confidence: float = Field(description="0 to 1")`, run five cards, and compare the confidence values with the actual errors from the batch. Small models fill this field without meaning; a real confidence needs a second check, not a number.

A second stretch is the same extraction through the OpenAI client: create the client as in the [portability page](/v3/part2/02-python-and-ollama/portability), then `oa.chat.completions.parse(model=MODEL, messages=..., response_format=Record)` returns `completion.choices[0].message.parsed`.

The next chapter turns from the chat model to a second, smaller model: [embeddings](/v3/part2/04-embeddings).

## Check yourself

- [ ] I can define a record as a Pydantic model and hand its schema to the model.
- [ ] I can say what grammar-enforced output guarantees and what it does not.
- [ ] I saw the model invent a place and a rule that catches it.
- [ ] I can run a batch and read the field accuracy against a gold file.

{{< callout type="success" >}}
**What you should see:** one valid record for the first card, a rejected invented place on the silent card, and a batch line close to `20 cards, field accuracy 97/120 = 81%`.
{{< /callout >}}