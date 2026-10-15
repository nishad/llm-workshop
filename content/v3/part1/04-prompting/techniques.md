---
title: Techniques
weight: 2
---

Five techniques are live in the session. Five more are in a closed block at the end, for self-study. Each live technique has a captured answer from nishad/apertus:8b (temperature 0.8, 15 October 2026).

## 1. Few-shot: show the pattern

In **few-shot** prompting you put a few worked examples into the prompt. The model continues the pattern. This is the most reliable way to get an unusual label set or format.

Without examples this is zero-shot, the plain request. With one example it is one-shot.

**Prompt:**

```
Classify each library material as BOOK, JOURNAL, DVD or DATABASE.

Examples:
"Pride and Prejudice" -> BOOK
"Nature Scientific Journal" -> JOURNAL
"The Matrix (1999)" -> DVD
"JSTOR Academic Database" -> DATABASE

Now classify:
"National Geographic Documentary Collection"
"The New York Times Historical Archive"
"To Kill a Mockingbird"
"Annual Review of Psychology"
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
1. "National Geographic Documentary Collection" -> DVD
2. "The New York Times Historical Archive" -> DATABASE
3. "To Kill a Mockingbird" -> BOOK
4. "Annual Review of Psychology" -> JOURNAL
```

The four labels are right. The examples carried the label set (BOOK, JOURNAL, DVD, DATABASE) and the output shape. The model even copied the "->" arrow from the examples.

Few-shot works best when the format is unusual or domain-specific. Two to four examples are enough. Choose examples that differ from each other.

## 2. Role and system prompt

A **role** tells the model who it is speaking as. It sets vocabulary, depth and tone. A **system prompt** is a place for instructions that apply to the whole conversation, such as the role, so you do not repeat them in every message.

System prompt used here:

```
You are a rare books librarian with twenty years of experience in authenticating early printed books. Answer briefly and practically.
```

**Prompt:**

```
A patron brings in what they say is a first edition of Pride and Prejudice from 1813. List the five things you would check first, one line each.
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
1. The publisher's name and location.
2. The printing date - check for 1813 or earlier.
3. The title page to confirm the work is Pride and Prejudice.
4. The book's binding and paper quality for age.
5. The presence of an inscription or ownership mark which could indicate a later addition.
```

The answer is brief and practical, as the system prompt asked: five lines, one check each. A role changes the tone and the focus of an answer, not what the model knows. Whether this is the checklist a rare books specialist would give is for a specialist to judge.

### Where to set a system prompt

- **LM Studio:** open the sidebar in Developer mode and fill in the system prompt field. See [LM Studio](/v3/part1/03-first-chat/lm-studio).
- **Ollama in the terminal:** start `ollama run nishad/apertus:8b`, then type `/set system` followed by your text. The setting lasts for that session.
- **The Ollama app:** it has no system prompt field. Put the role at the start of your first message instead.

## 3. Structured answers

When the answer feeds a spreadsheet or a program, ask for a structure. Two common ones are a Markdown table and a JSON list. Both prompts below use the first paragraph of the sample text.

**A Markdown table:**

**Prompt:**

```
Extract every book from this text into a Markdown table with the columns Title | Author | Year.

Text:
[the first paragraph of the sample text]
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
| Title | Author | Year |
| --- | --- | --- |
| Of Mice and Men | John Steinbeck | 1937 |
| Cien años de soledad | Gabriel García Márquez | 1967 |
| Pride and Prejudice | Jane Austen | 1813 |
| ノルウェイの森 (Noruwei no Mori) | Haruki Murakami | 1987 |
```

**A JSON list:**

**Prompt:**

```
Extract every book from this text as a JSON list. Each item has the keys "title", "author" and "year" (a number). Return only the JSON.

Text:
[the first paragraph of the sample text]
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
[
    {
        "title": "Of Mice and Men",
        "author": "John Steinbeck",
        "year": 1937
    },
    {
        "title": "Cien años de soledad",
        "author": "Gabriel García Márquez",
        "year": 1967
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "year": 1813
    },
    {
        "title": "ノルウェイの森",
        "author": "Haruki Murakami",
        "year": 1987
    }
]
```

Both are correct for the four works. Look at what the model decided on its own: in the table it kept the romanized form in brackets, in the JSON it dropped it.

{{< callout type="info" >}}
Here the shape is only requested. A model can add a sentence before the JSON, wrap it in a code fence or leave out a key. In Part 2 the shape is enforced with a schema, and the answer is checked by code.
{{< /callout >}}

## 4. Constraints

Constraints limit length, vocabulary, scope or style. They work best when they are about what to include or leave out.

**Prompt:**

```
Explain what a call number is in exactly 20 words. Do not use the word "shelf".
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
A call number is a unique identifier assigned to a book, allowing it to be located in a library's catalog system.
```

The prompt asked for exactly 20 words and no "shelf". The answer has 21 words and avoids the forbidden word. Small models do not count: they predict one token at a time and have no counter running. Expect "about 20", not "exactly 20". If a limit matters, count the words yourself or check them with a script.

## 5. Multi-step with checkpoints

Instead of one big prompt, split the work into steps and check each result before the next. Here is a three-step chain on a short abstract (written for this exercise): summarize, then extract the methods, then classify the study.

**Step 1: summarize**

**Prompt:**

```
Summarize this abstract in two sentences.

Public libraries in three cities ran a six-week course on computer skills for adults. The authors surveyed 450 participants before and after the course and interviewed 45 of them. Participants reported better basic computer skills and more awareness of online safety. The largest gains were among participants over 60.
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
This abstract is about a six-week course on computer skills for adults in public libraries in three cities. The course involved 450 participants, who were surveyed before and after the course, and 45 were interviewed. The results showed that participants had better basic computer skills and a greater awareness of online safety, particularly among those over 60.
```

**Step 2: extract**

**Prompt:**

```
From this summary, list the research methods used and the number of participants, one line each.

This abstract is about a six-week course on computer skills for adults in public libraries in three cities. The course involved 450 participants, who were surveyed before and after the course, and 45 were interviewed. The results showed that participants had better basic computer skills and a greater awareness of online safety, particularly among those over 60.
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
1. Surveys (before and after the course) involving 450 participants.
2. Interviews (45 participants).
```

**Step 3: classify**

**Prompt:**

```
Classify the study as qualitative, quantitative or mixed methods. Answer with one of the three terms, then one sentence of justification.

Methods:
1. Surveys (before and after the course) involving 450 participants.
2. Interviews (45 participants).
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
Quantitative

Justification: The study uses surveys and quantitative methods to evaluate the effect of the course on participants' knowledge and attitudes. Interviews (45 participants) provide qualitative insights but are not the primary method of data collection.
```

Each step fits on one screen, so a person can see where it went wrong. This chain also shows why checkpoints matter. At step 2 the model listed surveys and interviews. At step 3 it called the study "Quantitative", yet its own justification says the interviews provide qualitative insight. A study with both surveys and interviews is usually called mixed methods. If you had only looked at the final label, you would not have seen the shaky reasoning.

## Combining techniques

The most capable prompts combine a few techniques. A bracket template makes the parts easy to see and reuse:

```
[ROLE] You are a cataloguer specializing in literary metadata.
[TASK] Extract book information from the text below.
[EXAMPLE]
Input: "Orwell's 1984 was published in 1949."
Output: {"title": "1984", "author": "Orwell", "year": 1949}
[CONSTRAINTS] Only include books published between 1800 and 2000.
[OUTPUT FORMAT] A JSON array. No other text.
[TEXT]
{insert the text}
```

Do not use all techniques at once. Pick one or two that fit the task.

## Thinking models and Apertus

Some newer models have a thinking mode: they write out a stretch of reasoning before the final answer, and the app may hide or show it. Apertus 1.0 has no thinking mode. When you ask it to "think step by step", the steps are simply part of its answer. That helps with arithmetic and multi-part questions, but nothing checks the steps. You are the checker.

## Self-study: five more techniques

{{< details title="Show the five self-study techniques" >}}

### Chain-of-thought

Ask the model to write its working before the answer. Compare these two prompts on the same problem.

```
A library has 150 books. On Monday, 23 books were checked out and 15 were returned. On Tuesday, 30 books were checked out and 12 were returned. How many books are now in the library?
```

```
A library has 150 books. On Monday, 23 books were checked out and 15 were returned. On Tuesday, 30 books were checked out and 12 were returned. How many books are now in the library?

Work through it step by step and give the answer on the last line.
```

The correct answer is 124: Monday changes the count by 15 - 23 = -8, Tuesday by 12 - 30 = -18, and 150 - 8 - 18 = 124. Run both prompts a few times. See whether the steps make the answer more reliable, and whether a wrong step is easy to spot.

### Negative prompting

Tell the model what to avoid: "Do not use mathematical equations", "Do not mention prices". It works for style. For small models there is a catch: naming the forbidden thing puts it in the context, and the model may then use it. If "no equations" produces an equation, say what you want instead: "Explain in words only".

### Templates

Write the prompt once with blanks, then reuse it.

```
Write a short book note.
Book: [TITLE] by [AUTHOR]
Audience: [AUDIENCE]
Length: [NUMBER] sentences
Tone: [TONE]
```

Keep templates in a text file. Then your results are comparable from one run to the next.

### Comparative prompts

Ask for a comparison along named dimensions, as a table.

```
Compare these two works in a table with the rows: language, period, form, and one theme. Works: Les Misérables, Pride and Prejudice.
```

Named dimensions keep the answer from drifting into an essay.

### Iterative refinement

Use the model's answer as the start of the next prompt: "Here is your last answer. Shorten it to 50 words and keep the two examples." Treat each reply as a draft. Start a new chat when the thread gets long, because the whole thread counts against the context window.

{{< /details >}}
