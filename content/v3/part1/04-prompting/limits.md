---
title: Limits
weight: 4
---

Small local models are useful, and they make mistakes in predictable ways. This page shows five of them, each with a captured example, so you can recognize them in your own work.

All captures come from thalhath/apertus:8b at temperature 0.8 on 15 October 2026, unless stated otherwise. Temperature is the setting that controls how much the answers vary.

## 1. An invented place of publication

This one comes from the notebooks in Part 2. Notebook 02 reads catalog cards and fills in a record that follows a schema, a fixed list of the allowed fields and what goes in each. Card 03 has no place of publication:

```
Beauvoir, Simone de
Le deuxième sexe. I, Les faits et les mythes
Gallimard, 1949
395 p. ; 19 cm
Collection Folio essais
```

The instruction said to use an empty string (a blank value) for any field the card does not state, and never to guess a place. The model returned this (from the executed notebook 02, 15 October 2026):

```
{'title': 'Le deuxième sexe. I, Les faits et les mythes', 'creators': ['Beauvoir, Simone de'], 'place': 'Gallimard', 'publisher': 'Gallimard', 'date': '1949', 'language': 'en', 'identifier': ''}
place should be empty; the model said: 'Gallimard'
```

The model put the publisher's name into the place field. A second error sits in the same line: the language of this French book is marked 'en', the code for English. Both values look normal. Nothing in the answer signals a problem.

## 2. A fabricated identifier

The probe from [Exercise 6](/v3/part1/04-prompting/exercises#exercise-6-the-hallucination-probe-live):

**Prompt:**

```
What is the ISBN of the book "Das Parfum" by Patrick Süskind, published by Diogenes?
```

**Output** (captured with thalhath/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
The ISBN of the book "Das Parfum" by Patrick Süskind, published by Diogenes, is 9783257061675.
```

The ISBN is not valid: its check digit is wrong, and the DNB catalog has no record of it. The same number with the correct check digit is a different book, "Verrechnet" by Dick Francis. The model gave one number and showed no doubt. The DOI in the same exercise was real but belonged to a different article. The full check is on the exercises page.

## 3. A rule missed in a calculation

A late-fee problem with a maximum fee per item:

**Prompt:**

```
A library's late fee policy: books cost $0.25 per day, DVDs cost $1.00 per day, and the maximum fee is $5.00 per item. Sarah has 2 books that are 12 days late, 1 DVD that is 8 days late and 1 book that is 3 days late. How much does Sarah owe in total?
```

**Output** (captured with thalhath/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
To calculate Sarah's total late fee, we need to calculate the late fees for each item and then add them together.

Books:
Sarah has 2 books that are 12 days late. The late fee for each book is $0.25 per day.
So, the total late fee for the books is 2 * $0.25 * 12 = $6.

DVD:
Sarah has 1 DVD that is 8 days late. The late fee for the DVD is $1.00 per day.
So, the total late fee for the DVD is $1.00 * 8 = $8.

Book (3 days late):
Sarah has 1 book that is 3 days late. The late fee for this book is $0.25 per day.
So, the total late fee for this book is $0.25 * 3 = $0.75.

Total Late Fee:
Now, let's add up the total late fees for all items: $6 (books) + $8 (DVD) + $0.75 (book) = $14.75.

Therefore, Sarah owes a total of $14.75 in late fees.
```

Each multiplication is correct: 2 books at 12 days is 2 x 0.25 x 12 = $6. But the policy caps the fee at $5.00 per item, so the DVD should cost $5. The model ignored the cap and charged $8. The right total is $6 + $5 + $0.75 = $11.75. The model's $14.75 is $3 too much. The steps are written out and look careful, which makes the mistake easy to miss.

## 4. A missed word limit

**Prompt:**

```
Summarize in no more than 15 words: The library will close for two weeks in August to replace the roof, move the periodicals to the basement and install a new self-service checkout system. All loans are automatically extended until the day after reopening.
```

**Output** (captured with thalhath/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
The library will close for two weeks in August to replace the roof, move periodicals to the basement, and install a new self-service checkout system. All loans are automatically extended until the day after reopening.
```

The prompt asked for no more than 15 words. The answer has 35, and it is a near copy of the original text. The model has no word counter. Earlier on the [techniques page](/v3/part1/04-prompting/techniques), a request for exactly 20 words produced 21.

## 5. A wrong term in translation

The prompt below translates German economics terms into English. The reference is the English label in the STW Thesaurus for Economics, version 9.20.

**Prompt:**

```
Translate these German economics terms into English, one per line: Schattenwirtschaft, Lenkungsabgabe, Nutzungsdauer, Urheberrecht, Eigentum
```

**Output** (captured with thalhath/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
1. Shadow Economy
2. Regulatory Fee
3. Service Life
4. Copyright
5. Ownership
```

| German | Model | STW 9.20 English label |
|---|---|---|
| Schattenwirtschaft | Shadow Economy | Underground economy |
| Lenkungsabgabe | Regulatory Fee | Steering tax |
| Nutzungsdauer | Service Life | Useful life |
| Urheberrecht | Copyright | Copyright law |
| Eigentum | Ownership | Property |

Four of the five are acceptable English, but each differs from the label in the thesaurus. Lenkungsabgabe is a different kind of problem. In STW it is a levy (a tax or charge) whose main purpose is to steer behavior, and the model's "Regulatory Fee" does not say that. A reader who does not know German would not notice. When a vocabulary sets the label, the model's translation is no more than a suggestion.

## Two checks anyone can do

1. **Ask for the source, then look it up.** Ask "Where does this come from?" and check what you get against a catalog, Crossref, the thesaurus or the original text. If the model names a source, confirm that it exists and says what the model claims. If it cannot name one, treat the answer as unverified.
2. **Ask the same question twice and compare.** Run the prompt again in a new chat. At temperature 0.8, the default in the apps, answers can vary between runs. Facts the model has actually learned tend to come back the same. A guess changes between runs. If two runs disagree, treat both answers as unverified.

Neither check proves an answer is right. They only tell you where to look.

{{< callout type="warning" >}}
A confident tone is not evidence. Every example on this page was delivered as calmly as a correct answer would have been.
{{< /callout >}}

## From here to Part 2

In Part 2 you meet the tools that make these errors visible: a schema that rejects a wrong shape, a validator (a check written in code) that rejects a place that is the same as the publisher, and a human who approves a record before it is used. See [Part 2](/v3/part2).
