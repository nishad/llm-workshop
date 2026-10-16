---
title: Temperature
weight: 5
---

**Temperature** controls how random the choice of the next token is. At each step the model has a probability for each possible next token. A low temperature widens the gaps between those probabilities, so the most likely token almost always wins. A high temperature brings the probabilities closer together, so less likely tokens get a chance.

## Ranges

- **0 to 0.3**: focused and factual.
- **0.4 to 0.7**: balanced.
- **0.8 to 1.2**: creative and varied.

A **seed** is a number that fixes the random choices, so the same prompt, settings and seed give the same answer again. That is how you make a run repeatable.

## Two captured experiments

We ran each experiment three times per setting with nishad/apertus:8b on 15 October 2026. The model's digest, a code that identifies the exact download, was 4a85a6fea0b8.

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

Both settings give the same answer in every run. When the model is nearly certain, the most likely token holds almost all the probability, and temperature has nothing to change.

The prompt also asked for five words, and every run gave a single word: the model answered the question instead of completing the sentence. A model does not always follow the instructions in a prompt.

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

At temperature 0 the three runs give exactly the same title. At 1.0 each run gives a different title. Temperature matters where the model is unsure. Try your own prompt in LM Studio at 0 and at 1.2.

## Where the setting lives

- **LM Studio**: in the sidebar, in Developer mode.
- **Ollama command line**: `/set parameter temperature 0.2` inside a chat.
- **Python**: in the options you pass with the request (Part 2).
- **Ollama app**: the setting is not available there.

{{< callout type="info" >}}
For the Part 1 exercise, use LM Studio if you want to change the temperature setting.
{{< /callout >}}
