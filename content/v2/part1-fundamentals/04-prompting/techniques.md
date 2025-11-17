---
title: Advanced Techniques
weight: 2
---

## Advanced Prompting Techniques

Once you master the basics, these advanced techniques can help you get even better results from LLMs.

---

## 1. Few-Shot Learning

**Few-shot learning** means providing examples of the task you want the model to perform. The model learns the pattern from your examples and applies it to new inputs.

### Zero-Shot (No Examples)

```
Translate this to Spanish: "Hello, how are you?"
```

### One-Shot (One Example)

```
Translate to Spanish:

Example:
English: Good morning
Spanish: Buenos días

Now translate:
English: Hello, how are you?
```

### Few-Shot (Multiple Examples)

```
Translate to Spanish following these examples:

English: Good morning → Spanish: Buenos días
English: Thank you → Spanish: Gracias
English: See you later → Spanish: Hasta luego

Now translate:
English: Hello, how are you?
```

**Expected Output**:
```
Spanish: Hola, ¿cómo estás?
```

{{< callout type="info" >}}
**When to Use**: Few-shot works best for tasks with specific formats, patterns, or styles that might be unusual or domain-specific.
{{< /callout >}}

---

## 2. Chain-of-Thought (CoT) Prompting

**Chain-of-Thought** prompting encourages the model to show its reasoning process step-by-step, leading to better answers for complex problems.

### Without Chain-of-Thought

```
A library has 150 books. On Monday, 23 books were checked out and
15 were returned. On Tuesday, 30 books were checked out and 12 were
returned. How many books are now in the library?
```

The model might jump to an answer without showing work.

### With Chain-of-Thought

```
A library has 150 books. On Monday, 23 books were checked out and
15 were returned. On Tuesday, 30 books were checked out and 12 were
returned. How many books are now in the library?

Let's solve this step by step:
```

**Expected Output**:
```
Let's solve this step by step:

1. Starting books: 150
2. Monday: 23 checked out, 15 returned
   - Net change: 15 - 23 = -8
   - Books after Monday: 150 - 8 = 142
3. Tuesday: 30 checked out, 12 returned
   - Net change: 12 - 30 = -18
   - Books after Tuesday: 142 - 18 = 124

Therefore, there are now 124 books in the library.
```

### Few-Shot Chain-of-Thought

Combine few-shot with CoT for complex tasks:

```
Solve these word problems step by step:

Example 1:
Problem: A store had 50 apples. They sold 20. How many remain?
Solution:
- Starting apples: 50
- Sold: 20
- Remaining: 50 - 20 = 30
Answer: 30 apples

Example 2:
Problem: Tom has 15 books, receives 8 more, then gives away 5. How many does he have?
Solution:
- Starting: 15 books
- Received: +8 → 15 + 8 = 23
- Gave away: -5 → 23 - 5 = 18
Answer: 18 books

Now solve:
A librarian cataloged 45 books on Monday, 33 on Tuesday, and 28 on Wednesday.
On Thursday, 12 books were removed. How many books were cataloged in total?
```

---

## 3. Role-Based Prompting

Assign a specific role or persona to the model to influence its responses.

### Example: Expert Librarian

```
You are an expert rare books librarian with 20 years of experience in
manuscript preservation and authentication.

A patron brings in what they claim is a first edition of "Pride and
Prejudice" from 1813. What steps would you take to verify its authenticity?

Provide a systematic approach with specific things to check.
```

### Example: Friendly Teacher

```
You are a friendly and enthusiastic elementary school teacher who loves
making learning fun.

Explain how libraries are organized using the Dewey Decimal System to
a 3rd grade student. Use simple language and examples they can relate to.
```

### Example: Technical Expert

```
You are a senior Python developer with expertise in natural language
processing and machine learning.

Review this code for extracting named entities from text and suggest
improvements for performance and accuracy:

[code here]
```

**Why It Works**: Roles provide context about expertise level, tone, and approach, helping the model calibrate its response.

---

## 4. Structured Output Prompting

Force the model to return data in specific formats like JSON, XML, CSV, or markdown.

### JSON Output

```
Extract book information from this text and return ONLY valid JSON:

"The Great Gatsby by F. Scott Fitzgerald was published in 1925.
To Kill a Mockingbird by Harper Lee came out in 1960."

Format:
{
  "books": [
    {"title": "...", "author": "...", "year": ...}
  ]
}

Return only JSON, no additional text.
```

### Table/CSV Output

```
Extract and format as a markdown table:

Text: "London has 9 million people. Tokyo has 14 million. New York has 8 million."

| City | Population (millions) |
|------|----------------------|
```

### Bullet List Output

```
Summarize the key points from this article as a bullet list:

- Each point should be one sentence
- Use past tense
- Focus on facts only
- Maximum 5 points
```

---

## 5. Constraint-Based Prompting

Add specific constraints to guide the model's behavior.

### Length Constraints

```
Explain quantum computing.

Constraints:
- Exactly 50 words
- Use no technical jargon
- Include one analogy
```

### Content Constraints

```
Write a product description for this book.

Requirements:
- Do NOT mention price
- Do NOT use superlatives (best, greatest, etc.)
- Do NOT make claims about reviews or ratings
- Focus only on content and target audience
- Maximum 100 words
```

### Style Constraints

```
Summarize this research paper.

Style requirements:
- Use present tense only
- Write in third person
- Use passive voice for methods
- No contractions
- Academic tone
```

---

## 6. Multi-Step Prompting

Break complex tasks into sequential steps.

### Example: Research Summary Pipeline

**Step 1**: Extract key information
```
From this research paper, extract:
1. Main research question
2. Methodology used
3. Key findings (top 3)
4. Limitations mentioned

[paper text]
```

**Step 2**: Synthesize findings
```
Using this extracted information:
[output from Step 1]

Write a 150-word abstract suitable for a conference submission.
```

**Step 3**: Generate questions
```
Based on this abstract:
[output from Step 2]

Generate 5 critical questions that reviewers might ask.
```

{{< callout type="info" >}}
**Pro Tip**: For multi-step tasks, use separate prompts rather than asking the model to do everything at once. This improves accuracy and gives you checkpoints to verify.
{{< /callout >}}

---

## 7. Negative Prompting

Tell the model what NOT to do.

### Example

```
Explain machine learning to a business executive.

DO:
- Use business-relevant examples
- Focus on practical applications
- Keep it under 200 words

DO NOT:
- Use mathematical equations
- Mention specific algorithms
- Get into technical implementation details
- Use computer science jargon
```

**Why It Works**: Explicitly stating what to avoid prevents common errors and keeps the model focused.

---

## 8. Iterative Refinement

Use the model's output as input for improvement.

### Step 1: Initial Prompt

```
Write a brief description of what vector databases are.
```

### Step 2: Refine

```
Here's a description of vector databases:
[previous output]

Improve this description by:
1. Adding a concrete real-world example
2. Explaining why they're better than traditional databases for certain tasks
3. Keeping it under 150 words
```

### Step 3: Further Refine

```
Here's the improved description:
[previous output]

Make it more accessible to someone with no database experience.
Replace technical terms with analogies.
```

---

## 9. Template-Based Prompting

Create reusable templates for common tasks.

### Book Review Template

```
Write a book review following this template:

Book: [TITLE] by [AUTHOR]
Genre: [GENRE]

Structure:
1. Opening Hook: One engaging sentence about the book
2. Summary: 2-3 sentence plot summary (no spoilers)
3. What Works: 2 strengths of the book
4. What Could Be Better: 1 constructive criticism
5. Recommendation: Who would enjoy this book?
6. Rating: X/5 stars with brief justification

Total length: 200-250 words
Tone: Balanced, thoughtful, accessible
```

### Data Extraction Template

```
Extract data from text using this template:

INPUT: [text]

EXTRACT:
- Entities: [list of people, places, organizations]
- Dates: [list of dates mentioned]
- Key Numbers: [important numerical data]
- Topics: [main themes, max 3]

FORMAT: JSON
```

---

## 10. Comparative Prompting

Ask the model to compare and contrast for deeper analysis.

### Example

```
Compare and contrast these two books based on the following text:

[text mentioning multiple books]

Create a comparison table with these dimensions:
- Publication era
- Language/Culture
- Genre
- Estimated complexity level
- Target audience

Present as markdown table.
```

---

## Combining Techniques

The most powerful prompts often combine multiple techniques:

### Example: Complex Extraction Task

```
[ROLE] You are a data analyst specializing in literary metadata.

[TASK] Extract book information from the text below and analyze patterns.

[FEW-SHOT EXAMPLE]
Input: "Orwell's 1984 was published in 1949."
Output: {"title": "1984", "author": "Orwell", "year": 1949}

[CONSTRAINT] Only include books published between 1800-2000.

[OUTPUT FORMAT]
1. JSON array of books
2. Summary paragraph identifying patterns (languages, time periods, genres)

[CHAIN OF THOUGHT] Show your analysis reasoning.

[TEXT]
{insert sample text}
```

---

## Advanced Tips

### 1. Use Delimiters

Separate different parts of your prompt clearly:

```
###INSTRUCTION###
Summarize the following text

###CONSTRAINTS###
- Maximum 100 words
- Focus on key findings

###TEXT###
[your text here]

###OUTPUT###
```

### 2. Specify Tone and Audience

```
Write this for: [audience description]
Tone: [formal/casual/technical/etc.]
Reading level: [grade level or expertise]
```

### 3. Request Self-Critique

```
[task]

After providing your answer, critique it and suggest one improvement.
```

### 4. Use System Messages (When Available)

Some interfaces let you set a system message that persists:

```
System: You are a meticulous fact-checker. Always cite sources when possible
and express uncertainty when appropriate.

User: Tell me about the history of libraries.
```

---

## Practice Exercise

Try improving this weak prompt using techniques from this section:

**Weak Prompt**:
```
Tell me about the books
```

**Your Improved Prompt Should Include**:
- Clear context
- Specific instruction
- Output format
- At least one advanced technique

{{< details "Show Example Solution" >}}

**Improved Prompt**:
```
[ROLE] You are a literary analyst specializing in world literature.

[CONTEXT] I have a text describing various books from different cultures
and time periods.

[TASK] Analyze the following text and extract book information.

[OUTPUT FORMAT]
1. Create a JSON array of books with: title, author, year, language, genre
2. Write a 100-word analysis of geographic and temporal distribution
3. Identify the 3 most culturally significant works and explain why

[CONSTRAINTS]
- Only include books explicitly mentioned with clear publication dates
- Use ISO 639-1 language codes (en, es, ja, etc.)
- Analysis should be objective and data-driven

[TEXT]
{insert your text here}
```

{{< /details >}}

---

## Next: Hands-On Practice

Ready to put these techniques into action?

{{< cards >}}
  {{< card link="/v2/part1-fundamentals/04-prompting/exercises" title="Practice Exercises" icon="arrow-right" subtitle="Apply what you've learned with hands-on exercises" >}}
{{< /cards >}}

{{< callout type="success" >}}
**Mastering These Techniques**: Don't try to use all techniques at once. Pick 1-2 that fit your task and master them first. You can always combine more as you gain experience.
{{< /callout >}}
