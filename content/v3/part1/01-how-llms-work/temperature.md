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

Both ran three times per setting with nishad/apertus:8b (digest 4a85a6fea0b8) on 15 October 2026.

### Experiment 1: a question with one answer

**Prompt:**

```
Complete this sentence in five words: The capital of France is
```

**Temperature 0**, all three runs:

```
Paris.
```

**Temperature 1.0**, all three runs:

```
Paris.
```

Both settings give the same completion in every run. When the model is nearly certain, the top token takes almost all the probability and temperature has nothing to change.

The prompt also asked for five words, and every run answered with one: the model answered the question instead of completing the sentence. A model does not always follow the instructions in a prompt.

### Experiment 2: an open prompt

**Prompt:**

```
Suggest a title for a library newsletter about local AI tools. Answer with the title only.
```

**Temperature 0**, all three runs:

```
"AI Insights: Local Tools & Innovations"
```

**Temperature 1.0**, run 1:

```
Local AI Tools Newsletter
```

Run 2:

```
"AI Insights: Local Tools, Global Impact"
```

Run 3:

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
