---
title: Effective Prompting
weight: 4
cascade:
  type: docs
sidebar:
  open: true
---

## Effective Prompting for LLMs

**Prompting** is the art and science of communicating with large language models. The quality of your prompts directly affects the quality of the model's responses. Learning to write effective prompts is one of the most valuable skills for working with LLMs.

### What is a Prompt?

A **prompt** is the input you provide to an LLM. It can be:
- A question: "What is photosynthesis?"
- An instruction: "Translate this text to Spanish"
- A request: "Write a poem about autumn"
- Context + question: "Given this data... what trends do you see?"

### Why Prompting Matters

The same model can produce vastly different outputs depending on how you prompt it:

**Poor Prompt**:
```
write code
```

**Better Prompt**:
```
Write a Python function that takes a list of numbers and returns the median value.
Include error handling for empty lists and non-numeric values.
Add docstring and type hints.
```

The second prompt produces dramatically better code because it's specific, clear, and provides context.

### What You'll Learn

This section covers:

{{< cards >}}
  {{< card link="/v2/part1-fundamentals/04-prompting/basics" title="Prompting Basics" icon="document-text" subtitle="Fundamental principles and best practices" >}}
  {{< card link="/v2/part1-fundamentals/04-prompting/techniques" title="Advanced Techniques" icon="sparkles" subtitle="Few-shot learning, chain-of-thought, and more" >}}
  {{< card link="/v2/part1-fundamentals/04-prompting/exercises" title="Hands-on Exercises" icon="pencil" subtitle="Practice with real examples" >}}
{{< /cards >}}

### The Prompting Mindset

When working with LLMs, think of them as:

- **Extremely literal**: They do exactly what you ask, not what you mean
- **Context-dependent**: They use only the information you provide
- **Pattern matchers**: They generate text based on patterns learned from training data
- **Non-deterministic** (usually): Same prompt can yield different responses

{{< callout type="info" >}}
**Key Insight**: LLMs don't "understand" in the human sense - they predict likely text continuations. Effective prompting works *with* this behavior, not against it.
{{< /callout >}}

### Quick Prompting Tips

Before diving deeper, here are five essential tips:

1. **Be Specific**: Vague prompts get vague responses
2. **Provide Context**: Give the model background information it needs
3. **Show Examples**: Demonstrate the format or style you want
4. **Iterate**: Refine your prompts based on the results
5. **Control Parameters**: Use temperature and other settings strategically

### Ready to Start?

Let's begin with the fundamentals:

{{< cards >}}
  {{< card link="/v2/part1-fundamentals/04-prompting/basics" title="Start with Basics" icon="arrow-right" subtitle="Learn fundamental prompting principles" >}}
{{< /cards >}}
