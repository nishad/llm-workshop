---
title: First prompts
weight: 3
---

Here are five starter prompts, each with the answer the model gave. Every answer was captured with nishad/apertus:8b on 15 October 2026 at temperature 0.8, the default in the apps. Your answers will differ in wording. The model picks each token (a word or part of a word) with some randomness, and temperature controls how much. See [Temperature](/v3/part1/01-how-llms-work/temperature).

Paste each prompt into your own chat and compare the answers.

## 1. Explain a term

**Prompt:**

```
Explain in three sentences what an authority file is and why a library catalogue uses one.
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
An authority file is a centralized list of standardized terms used to refer to an entity, such as a person, organization, or concept. Library catalogues use authority files to ensure consistency in the way information about an entity is recorded and retrieved. This helps in providing accurate and efficient access to information.
```

## 2. Translate (German to English and French)

**Prompt:**

```
Übersetze ins Englische und Französische: 'Herstellung von Kino-, TV- oder Werbefilmen.'
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
Übersetzung ins Englische: 'Production of cinema, television or advertisement films.'

Übersetzung ins Französische: 'Production de films de cinéma, de télévision ou publicitaires.'
```

## 3. Suggest subject headings

**Prompt:**

```
List five subject headings a library might assign to a book about the history of printing in Basel. One line each.
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
1. History of Printing
2. Basel, History of Printing in
3. Printing Industry, History of
4. Basel, Economy of, History of Printing
5. Basel, Cultural History of, Printing
```

The headings look reasonable. Whether a real authority file contains them is for a cataloger to check.

## 4. Rewrite for another audience

**Prompt:**

```
Rewrite this for a public-library newsletter in two sentences: 'The repository ingests metadata via OAI-PMH and exposes it as linked data.'
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
At our library, we're excited to announce that we're integrating a state-of-the-art repository that not only harvests metadata through the open archive interface (OAI-PMH) but also presents it as interconnected data, making it easier for users to discover and access a wealth of information. This innovation allows us to create a more accessible and user-friendly platform for our patrons to explore and enjoy a broad spectrum of digital resources.
```

## 5. The hallucination probe

This prompt asks for a fact the model cannot look up. It is a probe for hallucination: a fluent answer that is wrong or invented.

**Prompt:**

```
What is the ISBN of 'Vita activa' by Hannah Arendt?
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
The ISBN of 'Vita activa' by Hannah Arendt is 0141039689.
```

The model states one ISBN, with no sign of doubt. Now check it.

### Verification

The book is "Vita activa oder Vom tätigen Leben" by Hannah Arendt, published by Piper. The ISBNs on record are:

- 1960 first edition: none.
- 1981 edition: 978-3-492-00517-3 (3-492-00517-9).
- 1987 and 1989 editions: 978-3-492-10217-9 (3-492-10217-4).
- 2005, 2008 and 2011 Piper paperbacks: 978-3-492-23623-2 (3-492-23623-5).

The model's answer, 0141039689, matches none of them. The model invented it. It even fails the ISBN-10 check: with these first nine digits, the last character would have to be X. Yet the model gave it as calmly as it would give a correct answer.

Source: Checked against the catalog of the DNB (the German National Library) through lobid-resources, 15 October 2026.

{{< callout type="warning" >}}
A model answers confidently whether it knows or not. Check names, numbers, dates and identifiers against a catalog or another source before you use them.
{{< /callout >}}

## What just happened

- A model file, a few gigabytes of numbers, was loaded into your computer's memory.
- Your computer did all the computation for each token.
- Your prompts and the answers were not sent anywhere. Your computer used the internet only to look up the model name and to download the model.

## Speed FAQ

**How fast is it?** Speed is measured in tokens per second. To measure it on your own machine, run `ollama run nishad/apertus:8b --verbose` in a terminal. After each answer, Ollama prints statistics. Look for the line "eval rate". The [Hardware](/v3/before-you-start/hardware) page shows what to expect on different machines.

**Why is the first answer slower?** Your computer has to load the model into memory first.

**The answer is slow or cut off.** See [Troubleshooting](/v3/before-you-start/troubleshooting).
