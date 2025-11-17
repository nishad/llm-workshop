---
title: Prompting Basics
weight: 1
---

## Fundamental Prompting Principles

> This guide is based on Meta's official documentation and best practices from the prompting community. For more details, see the [Llama prompting guide](https://www.llama.com/docs/how-to-guides/prompting/).

**Prompt engineering** is the practice of crafting effective inputs to get the best possible outputs from language models. It involves providing context, instructions, and examples to guide the model toward your desired result.

### The Anatomy of a Good Prompt

A well-crafted prompt typically includes:

1. **Context**: Background information the model needs
2. **Instruction**: What you want the model to do
3. **Input Data** (optional): Text or information to process
4. **Output Format** (optional): How you want the response structured
5. **Constraints** (optional): Limitations or requirements

**Example Structure**:
```
[Context] You are an expert librarian helping students.

[Instruction] Extract all books from the following text.

[Input Data] {text about books}

[Output Format] Return as a bullet list with: Title, Author, Year.

[Constraint] Only include books published after 1900.
```

---

## Core Prompting Principles

### 1. Be Clear and Specific

**Poor Prompt**:
```
Tell me about climate change.
```

**Better Prompt**:
```
Explain the primary causes of climate change in simple terms suitable
for a high school student. Focus on the top 3 factors and their impacts.
Limit your response to 200 words.
```

**Why It's Better**:
- Specifies audience level (high school)
- Defines scope (top 3 factors)
- Sets length constraint (200 words)
- Clarifies purpose (explain causes and impacts)

---

### 2. Provide Context

The model doesn't know who you are, what you're working on, or what you already know. Provide necessary context.

**Without Context**:
```
How do I organize this?
```

**With Context**:
```
I'm a librarian organizing a collection of 500 historical photographs
from the 1920s-1940s. How should I categorize and catalog these images
to make them easily searchable for researchers?
```

**Why It's Better**:
- Model knows your role (librarian)
- Understands the task (organizing photos)
- Has details (time period, quantity, purpose)

---

### 3. Use Examples (Few-Shot Learning)

Show the model what you want by providing examples.

**Zero-Shot** (no examples):
```
Extract book information from this text.
```

**Few-Shot** (with examples):
```
Extract book information from text and format as shown:

Example 1:
Input: "George Orwell's 1984 was published in 1949."
Output: Title: 1984 | Author: George Orwell | Year: 1949

Example 2:
Input: "To Kill a Mockingbird by Harper Lee came out in 1960."
Output: Title: To Kill a Mockingbird | Author: Harper Lee | Year: 1960

Now extract from this text:
"John Steinbeck wrote Of Mice and Men, published in 1937."
```

**Expected Output**:
```
Title: Of Mice and Men | Author: John Steinbeck | Year: 1937
```

---

### 4. Specify Output Format

Tell the model exactly how you want the response structured.

**Unspecified Format**:
```
List the books mentioned in this text.
```

**Specified Format**:
```
List the books mentioned in this text in the following format:

```json
{
  "books": [
    {
      "title": "Book Title",
      "author": "Author Name",
      "year": 1234,
      "language": "English"
    }
  ]
}
```

Return only valid JSON, no additional text.
```

---

### 5. Set Constraints and Boundaries

Define what the model should and shouldn't do.

**Example with Constraints**:
```
Summarize this research paper.

Requirements:
- Maximum 150 words
- Focus only on methodology and findings
- Do not include author opinions or speculation
- Write in present tense
- Use bullet points for key findings
```

---

## Practical Examples with Sample Text

Let's use the following sample text for our examples:

```
John Steinbeck's "Of Mice and Men" was published in English in 1937.
Gabriel García Márquez wrote Cien años de soledad, a Spanish-language
novel, published in 1967. "Pride and Prejudice" by Jane Austen came
out in 1813 in English. Haruki Murakami penned the Japanese novel
ノルウェイの森 (Norwegian Wood), published in 1987.
```

### Example 1: Simple Extraction

**Prompt**:
```
Extract all book titles from the following text:

{insert sample text above}

List only the titles, one per line.
```

**Expected Output**:
```
Of Mice and Men
Cien años de soledad
Pride and Prejudice
ノルウェイの森 (Norwegian Wood)
```

---

### Example 2: Structured Data Extraction

**Prompt**:
```
Extract book information from the following text and return as a table:

{insert sample text}

Create a markdown table with columns: Title | Author | Year | Language
```

**Expected Output**:
```markdown
| Title | Author | Year | Language |
|-------|--------|------|----------|
| Of Mice and Men | John Steinbeck | 1937 | English |
| Cien años de soledad | Gabriel García Márquez | 1967 | Spanish |
| Pride and Prejudice | Jane Austen | 1813 | English |
| ノルウェイの森 (Norwegian Wood) | Haruki Murakami | 1987 | Japanese |
```

---

### Example 3: Filtering with Constraints

**Prompt**:
```
From the following text, list only books published after 1900:

{insert sample text}

Format: "Title" by Author (Year)
```

**Expected Output**:
```
"Of Mice and Men" by John Steinbeck (1937)
"Cien años de soledad" by Gabriel García Márquez (1967)
"ノルウェイの森" by Haruki Murakami (1987)
```

---

### Example 4: Creative Rewriting

**Prompt**:
```
Rewrite the following text as if it's being explained to a 10-year-old
child who loves reading:

{insert sample text}

Use simple language, short sentences, and an enthusiastic tone.
```

**Expected Output** (example):
```
Wow, there are so many cool books to talk about! Let me tell you about them!

First, there's a book called "Of Mice and Men" written by a man named
John Steinbeck. It came out way back in 1937. That's a really long time ago!

Then there's this amazing Spanish book called "Cien años de soledad"
(that means "One Hundred Years of Solitude" in English!). A famous
writer named Gabriel García Márquez wrote it in 1967.

Have you ever heard of "Pride and Prejudice"? It's a super old book
from 1813, written by Jane Austen. It's in English and lots of people
still love reading it today!

And there's a cool Japanese book called "Norwegian Wood" (which is
"ノルウェイの森" in Japanese). A writer named Haruki Murakami wrote
it in 1987.
```

---

## Stylization Techniques

### Academic Style

**Prompt**:
```
Analyze the following text from an academic perspective, focusing on
the geographic and temporal distribution of literary works:

{insert sample text}

Use formal academic language and cite specific examples.
```

---

### Technical/Structured Output

**Prompt**:
```
Convert the following text into a JSON array of book objects:

{insert sample text}

Each object should have: title, author, year, language, and originalTitle
(if different from English title).

Return only valid JSON.
```

---

### Creative/Storytelling Style

**Prompt**:
```
Using the books mentioned in this text, write a short story about a
magical library where each book represents a different world:

{insert sample text}

Maximum 200 words. Make it whimsical and engaging.
```

---

## Common Prompting Pitfalls

### ❌ Pitfall 1: Being Too Vague

**Bad**:
```
summarize this
```

**Good**:
```
Summarize the following text in 3 bullet points, focusing on the
main themes:
```

---

### ❌ Pitfall 2: Assuming Context

**Bad**:
```
How do I fix this?
```

**Good**:
```
I'm seeing an error "ModuleNotFoundError: ollama" when running my
Python script. I'm using Python 3.11 on macOS. How do I fix this?
```

---

### ❌ Pitfall 3: No Output Format

**Bad**:
```
Give me the data
```

**Good**:
```
Extract the data and format as CSV with headers: title, author, year
```

---

### ❌ Pitfall 4: Multiple Unrelated Tasks

**Bad**:
```
Summarize this, translate it to French, and write a poem about it.
```

**Good**:
Break into separate prompts:
```
1. First: Summarize this text in 2-3 sentences.
2. Then: Translate the summary to French.
3. Finally: Write a haiku inspired by the main theme.
```

---

## Best Practices Checklist

Before submitting your prompt, ask:

- [ ] Is my instruction clear and specific?
- [ ] Have I provided necessary context?
- [ ] Have I specified the output format?
- [ ] Have I set appropriate constraints?
- [ ] Am I asking for one task or multiple related tasks?
- [ ] Have I provided examples if the task is complex?
- [ ] Is the prompt self-contained (doesn't assume prior knowledge)?

---

## Iterative Refinement

Prompting is an iterative process. Here's how to refine:

1. **Start Simple**: Begin with a basic prompt
2. **Evaluate Output**: Check if it meets your needs
3. **Identify Gaps**: What's missing or wrong?
4. **Refine**: Add specificity, examples, or constraints
5. **Test Again**: Try the improved prompt
6. **Repeat**: Keep refining until satisfied

**Example Iteration**:

**Version 1** (too vague):
```
List the books.
```

**Version 2** (better, but no format):
```
List all books mentioned in this text.
```

**Version 3** (specifies format):
```
List all books mentioned in this text in the format: Title by Author (Year).
```

**Version 4** (adds constraints and sorting):
```
List all books mentioned in this text in the format: Title by Author (Year).
Sort chronologically by year, oldest first.
Only include books published before 1950.
```

---

## Next Steps

Now that you understand the basics, let's explore advanced techniques:

{{< cards >}}
  {{< card link="/v2/part1-fundamentals/04-prompting/techniques" title="Advanced Techniques" icon="arrow-right" subtitle="Learn few-shot learning, chain-of-thought, and more" >}}
{{< /cards >}}

{{< callout type="info" >}}
**Practice Makes Perfect**: The best way to improve your prompting skills is to experiment with different approaches and see what works for your specific use cases.
{{< /callout >}}
