---
title: Temperature
weight: 5
---

**Temperature** controls how random the pick of the next token is. At each step the model has probabilities for many candidate tokens. A low temperature sharpens them, so the most likely token almost always wins. A high temperature flattens them, so less likely tokens get a chance.

## Ranges

- **0 to 0.3**: focused and factual.
- **0.4 to 0.7**: balanced.
- **0.8 to 1.2**: creative and varied.

A **seed** fixes the random choices, so the same prompt, settings and seed give the same answer again. That is how you make a run repeatable.

## A captured demo

The same prompt, three runs at each setting. Captured with nishad/apertus:8b, 2026-10-15.

**Temperature 0**

**Prompt:**

```
Complete this sentence in five words: The capital of France is
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.0, 15 October 2026):

```
Paris.
```

**Prompt:**

```
Complete this sentence in five words: The capital of France is
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.0, 15 October 2026):

```
Paris.
```

**Prompt:**

```
Complete this sentence in five words: The capital of France is
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.0, 15 October 2026):

```
Paris.
```


**Temperature 1.0**

**Prompt:**

```
Complete this sentence in five words: The capital of France is
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 1.0, 15 October 2026):

```
Paris.
```

**Prompt:**

```
Complete this sentence in five words: The capital of France is
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 1.0, 15 October 2026):

```
Paris.
```

**Prompt:**

```
Complete this sentence in five words: The capital of France is
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 1.0, 15 October 2026):

```
Paris.
```


All six runs gave the same answer. For a prompt with one overwhelmingly likely continuation, even a high temperature rarely changes the pick. The difference shows on open-ended prompts, such as "Suggest a title for a talk about library catalogues", where many continuations are plausible. Try one in LM Studio at 0 and at 1.2.

## Where the setting lives

- **LM Studio**: in the sidebar, in Developer mode.
- **Ollama command line**: `/set parameter temperature 0.2` inside a chat.
- **Python**: in the options you pass with the request (Part 2).
- **Not in the Ollama app.**

{{< callout type="info" >}}
For the Part 1 exercise, use LM Studio if you want to change the temperature setting.
{{< /callout >}}

## Thinking models

Some models reason at length before they answer, and the reasoning burns tokens and time. In testing, a 4B thinking model spent 821 characters of hidden reasoning on a one-sentence answer, and 82 seconds on a short SPARQL query. Apertus 1.0 has no thinking mode, which keeps things simple here.
