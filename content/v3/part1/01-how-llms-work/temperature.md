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

## Two captured experiments

Both use nishad/apertus:8b with three runs per setting. Captured with nishad/apertus:8b, 15 October 2026.

### Experiment 1: a question with one answer

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

Both settings give the same completion in every run, and that is the point. When the model is nearly certain, the top token takes almost all the probability and temperature has nothing to change.

This prompt is also the chapter's captured failure: it asks for a five-word completion, and every run answers with the single word "Paris." The model ignored the five-word form and answered the question instead of completing the sentence, which is a reminder that an instruction in a prompt is a request, not a rule.

### Experiment 2: an open prompt

**Temperature 0**

**Prompt:**

```
Suggest a title for a library newsletter about local AI tools. Answer with the title only.
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.0, 15 October 2026):

```
"AI Insights: Local Tools & Innovations"
```

**Prompt:**

```
Suggest a title for a library newsletter about local AI tools. Answer with the title only.
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.0, 15 October 2026):

```
"AI Insights: Local Tools & Innovations"
```

**Prompt:**

```
Suggest a title for a library newsletter about local AI tools. Answer with the title only.
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.0, 15 October 2026):

```
"AI Insights: Local Tools & Innovations"
```

**Temperature 1.0**

**Prompt:**

```
Suggest a title for a library newsletter about local AI tools. Answer with the title only.
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 1.0, 15 October 2026):

```
Local AI Tools Newsletter
```

**Prompt:**

```
Suggest a title for a library newsletter about local AI tools. Answer with the title only.
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 1.0, 15 October 2026):

```
"AI Insights: Local Tools, Global Impact"
```

**Prompt:**

```
Suggest a title for a library newsletter about local AI tools. Answer with the title only.
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 1.0, 15 October 2026):

```
"AI Tools: Local Innovations & Community Insights"
```

At temperature 0 the three runs repeat themselves exactly. At 1.0 each run gives a different title. Temperature matters where the model is unsure. Try your own prompt in LM Studio at 0 and at 1.2.

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
