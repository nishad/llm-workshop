---
title: Hands-On Exercises
weight: 3
---

## Prompting Practice Exercises

Put your prompting skills into practice with these hands-on exercises. Try them in your Ollama installation!

{{< callout type="info" >}}
**How to Use This Page**: For each exercise, try writing your own prompt first, then test it in Ollama. Compare your results with the example solutions provided.
{{< /callout >}}

---

## Exercise 1: Basic Information Extraction

### Task

Extract structured information from this text about historical events:

```
The French Revolution began in 1789 and lasted until 1799. The American
Civil War started in 1861 and ended in 1865. World War I began in 1914
and concluded in 1918. The Russian Revolution took place in 1917.
```

**Goal**: Create a table with columns: Event | Start Year | End Year | Duration (years)

### Your Turn

Try writing a prompt to accomplish this task. Test it in Ollama.

{{< details "Show Example Solution" >}}

**Prompt**:
```
Extract historical events from the following text and create a markdown
table with these columns: Event | Start Year | End Year | Duration (years)

Calculate the duration by subtracting start year from end year.

Text:
The French Revolution began in 1789 and lasted until 1799. The American
Civil War started in 1861 and ended in 1865. World War I began in 1914
and concluded in 1918. The Russian Revolution took place in 1917.
```

**Expected Output**:
```markdown
| Event | Start Year | End Year | Duration (years) |
|-------|------------|----------|------------------|
| French Revolution | 1789 | 1799 | 10 |
| American Civil War | 1861 | 1865 | 4 |
| World War I | 1914 | 1918 | 4 |
| Russian Revolution | 1917 | 1917 | 0 |
```

Note: Russian Revolution only has a start year in the text, so end year and duration might be handled differently by the model.

{{< /details >}}

---

## Exercise 2: Few-Shot Learning

### Task

Use few-shot prompting to teach the model a specific classification pattern.

**Classify library materials** into categories: BOOK, JOURNAL, DVD, or DATABASE

### Training Examples

```
"Pride and Prejudice" → BOOK
"Nature Scientific Journal" → JOURNAL
"The Matrix (1999)" → DVD
"JSTOR Academic Database" → DATABASE
```

### Test Inputs

Classify these:
1. "National Geographic Documentary Collection"
2. "The New York Times Historical Archive"
3. "To Kill a Mockingbird"
4. "Annual Review of Psychology"

### Your Turn

Write a few-shot prompt for this classification task.

{{< details "Show Example Solution" >}}

**Prompt**:
```
Classify library materials into categories: BOOK, JOURNAL, DVD, or DATABASE

Examples:
"Pride and Prejudice" → BOOK
"Nature Scientific Journal" → JOURNAL
"The Matrix (1999)" → DVD
"JSTOR Academic Database" → DATABASE

Now classify these:
1. "National Geographic Documentary Collection"
2. "The New York Times Historical Archive"
3. "To Kill a Mockingbird"
4. "Annual Review of Psychology"

Format: Number. "Title" → CATEGORY
```

**Expected Output**:
```
1. "National Geographic Documentary Collection" → DVD
2. "The New York Times Historical Archive" → DATABASE
3. "To Kill a Mockingbird" → BOOK
4. "Annual Review of Psychology" → JOURNAL
```

{{< /details >}}

---

## Exercise 3: Role-Based Prompting

### Task

Get different perspectives on the same question by using different roles.

**Question**: "How should libraries adapt to the digital age?"

### Your Turn

Write three prompts asking this question from different perspectives:
1. A traditional librarian with 30 years of experience
2. A tech startup founder
3. A library patron who is a college student

Test all three in Ollama and compare the responses.

{{< details "Show Example Prompts" >}}

**Prompt 1: Traditional Librarian**:
```
You are a librarian with 30 years of experience working in public
libraries. You value the traditional role of libraries as community
spaces and guardians of knowledge.

How should libraries adapt to the digital age while preserving their
core values and community role?

Provide a thoughtful response drawing on your experience.
```

**Prompt 2: Tech Startup Founder**:
```
You are the founder of a successful EdTech startup focused on digital
learning platforms. You believe technology can democratize access to
information.

How should libraries adapt to the digital age?

Share your perspective on innovation and digital transformation.
```

**Prompt 3: College Student**:
```
You are a 20-year-old college student who uses the library regularly
for studying and research. You're comfortable with technology but also
appreciate quiet study spaces.

How should libraries adapt to the digital age to better serve students
like yourself?

Be specific about what would make libraries more useful for your studies.
```

{{< /details >}}

---

## Exercise 4: Chain-of-Thought Reasoning

### Task

Solve this problem using chain-of-thought prompting:

```
A library's late fee policy:
- Books: $0.25 per day
- DVDs: $1.00 per day
- Maximum fee: $5.00 per item

Sarah has:
- 2 books that are 12 days late
- 1 DVD that is 8 days late
- 1 book that is 3 days late

How much does Sarah owe in total?
```

### Your Turn

Write a prompt that encourages step-by-step reasoning.

{{< details "Show Example Solution" >}}

**Prompt**:
```
Solve this library late fee problem step-by-step, showing all calculations:

Policy:
- Books: $0.25 per day
- DVDs: $1.00 per day
- Maximum fee: $5.00 per item

Sarah's late items:
- 2 books that are 12 days late
- 1 DVD that is 8 days late
- 1 book that is 3 days late

Calculate the total late fees Sarah owes.

Show your work:
1. Calculate fee for each item
2. Apply maximum fee cap if needed
3. Sum all fees for total
```

**Expected Output**:
```
Step-by-step solution:

1. Calculate fee for each item:

   Book 1 (12 days late):
   - 12 days × $0.25 = $3.00

   Book 2 (12 days late):
   - 12 days × $0.25 = $3.00

   DVD (8 days late):
   - 8 days × $1.00 = $8.00
   - Exceeds $5.00 maximum
   - Capped at $5.00

   Book 3 (3 days late):
   - 3 days × $0.25 = $0.75

2. Apply maximum fee cap:
   - Book 1: $3.00 (under cap)
   - Book 2: $3.00 (under cap)
   - DVD: $5.00 (capped)
   - Book 3: $0.75 (under cap)

3. Total owed:
   $3.00 + $3.00 + $5.00 + $0.75 = $11.75

Sarah owes $11.75 in total late fees.
```

{{< /details >}}

---

## Exercise 5: JSON Structured Output

### Task

Extract data and return it as valid JSON.

**Input Text**:
```
Our library has the following upcoming events:
Book Club meets every Tuesday at 6pm in the Reading Room.
Story Time for kids happens on Saturdays at 10am in the Children's Section.
Tech Help sessions are offered Wednesdays at 2pm in the Computer Lab.
Author Talk with Jane Smith is scheduled for March 15th at 7pm in the Main Hall.
```

**Goal**: Extract events in JSON format with: name, day/date, time, location

### Your Turn

Write a prompt that produces clean, valid JSON output.

{{< details "Show Example Solution" >}}

**Prompt**:
```
Extract library events from the following text and return ONLY valid JSON.

Text:
Our library has the following upcoming events:
Book Club meets every Tuesday at 6pm in the Reading Room.
Story Time for kids happens on Saturdays at 10am in the Children's Section.
Tech Help sessions are offered Wednesdays at 2pm in the Computer Lab.
Author Talk with Jane Smith is scheduled for March 15th at 7pm in the Main Hall.

JSON Format:
{
  "events": [
    {
      "name": "event name",
      "schedule": "day or specific date",
      "time": "time in 12-hour format",
      "location": "location name"
    }
  ]
}

Return ONLY the JSON, no additional text or explanation.
```

**Expected Output**:
```json
{
  "events": [
    {
      "name": "Book Club",
      "schedule": "Every Tuesday",
      "time": "6:00 PM",
      "location": "Reading Room"
    },
    {
      "name": "Story Time",
      "schedule": "Saturdays",
      "time": "10:00 AM",
      "location": "Children's Section"
    },
    {
      "name": "Tech Help",
      "schedule": "Wednesdays",
      "time": "2:00 PM",
      "location": "Computer Lab"
    },
    {
      "name": "Author Talk with Jane Smith",
      "schedule": "March 15th",
      "time": "7:00 PM",
      "location": "Main Hall"
    }
  ]
}
```

{{< /details >}}

---

## Exercise 6: Multi-Step Task

### Task

Complete this multi-step research task:

**Step 1**: Summarize this abstract
**Step 2**: Identify the methodology
**Step 3**: Generate research questions
**Step 4**: Suggest related topics

**Input**:
```
Abstract: This study examines the impact of digital literacy programs in
public libraries across three metropolitan areas. Using surveys (n=450)
and interviews (n=45), we found that participants showed a 35% improvement
in basic computer skills and a 28% increase in online safety awareness
after completing the 6-week program. Participants over 60 showed the
greatest improvement. The study suggests that public libraries play a
crucial role in bridging the digital divide.
```

### Your Turn

Write separate prompts for each step, using the output of each as input for the next.

{{< details "Show Example Solution" >}}

**Step 1 Prompt**:
```
Summarize this research abstract in exactly 2 sentences:

[insert abstract]

Focus on: what was studied, what was found.
```

**Step 2 Prompt**:
```
Based on this abstract, identify and describe the research methodology used:

[insert abstract]

Include: research design, data collection methods, sample size.
Format as bullet points.
```

**Step 3 Prompt**:
```
Given this research about digital literacy programs in libraries:

[insert abstract]

Generate 5 follow-up research questions that would extend this work.
Each question should investigate a different aspect or angle.
```

**Step 4 Prompt**:
```
Based on this research:

[insert abstract]

Suggest 5 related topics that a librarian might want to research next.
Focus on practical applications and program improvements.
Format as: "Topic: Brief description (1 sentence)"
```

{{< /details >}}

---

## Exercise 7: Style Transformation

### Task

Rewrite the same content for three different audiences:

**Original Text**:
```
The library's new digital repository provides access to over 50,000
digitized historical documents, including photographs, letters, and
official records from 1850-1950. Users can search by keyword, date,
person, or location using advanced filtering options.
```

**Audiences**:
1. Write for a general audience (newsletter)
2. Write for researchers (academic announcement)
3. Write for children (library website kids section)

### Your Turn

Create three prompts for these transformations.

{{< details "Show Example Prompts" >}}

**Prompt 1: General Audience**:
```
Rewrite this text for a general audience reading a library newsletter.

Original:
[insert text]

Requirements:
- Warm, friendly tone
- Explain technical terms
- Emphasize benefits to community
- Maximum 75 words
- No jargon
```

**Prompt 2: Researchers**:
```
Rewrite this text for an academic audience as a formal announcement.

Original:
[insert text]

Requirements:
- Formal, professional tone
- Technical accuracy
- Emphasize research value
- Mention search capabilities
- 100-150 words
```

**Prompt 3: Children**:
```
Rewrite this text for children aged 8-12.

Original:
[insert text]

Requirements:
- Simple, clear language
- Enthusiastic tone
- Short sentences
- Use "you" to make it personal
- Include one example of what they might find
- Maximum 50 words
```

{{< /details >}}

---

## Exercise 8: Debugging Bad Prompts

### Task

These prompts have problems. Identify what's wrong and fix them.

**Bad Prompt 1**:
```
tell me stuff about libraries
```

**Bad Prompt 2**:
```
Extract the data from this text and make it look nice and also translate it to
Spanish and summarize it in French and create a chart showing the timeline
and write a poem about it.
```

**Bad Prompt 3**:
```
How do I fix this?
```

### Your Turn

For each prompt:
1. Identify the problem(s)
2. Rewrite as an effective prompt

{{< details "Show Example Solutions" >}}

**Bad Prompt 1 Problems**:
- Too vague ("stuff")
- No context
- No output format
- Unclear what aspect of libraries

**Fixed Version**:
```
Explain the role of public libraries in modern communities.

Focus on:
- Educational programs
- Community services
- Digital resources

Target audience: Someone considering a career in library science
Length: 200-300 words
Tone: Informative and encouraging
```

---

**Bad Prompt 2 Problems**:
- Too many unrelated tasks
- No priorities
- Unclear output format
- Likely to produce confused results

**Fixed Version** (break into steps):
```
Step 1: Extract the key data from this text and format as a table:
[text]

Step 2: [After getting results] Translate this table to Spanish:
[table from Step 1]

[Note: Do other tasks separately if needed]
```

---

**Bad Prompt 3 Problems**:
- No context at all
- Unclear what "this" refers to
- No information about what's wrong
- Cannot be answered

**Fixed Version**:
```
I'm getting this error when running Ollama:
"Error: could not connect to server at localhost:11434"

My setup:
- macOS 13.5
- Ollama version 0.10.0
- Just installed today

How can I fix this connection error?
```

{{< /details >}}

---

## Challenge Exercise: Combine Everything

### Ultimate Challenge

Use multiple advanced techniques in one comprehensive prompt:

**Scenario**: You're creating a digital catalog entry for a rare book.

**Requirements**:
- Use role-based prompting (you're a rare books cataloger)
- Include few-shot examples
- Specify JSON output format
- Add constraints (what NOT to include)
- Use chain-of-thought for condition assessment

**Input**: Information about a book that needs cataloging

### Your Turn

Create a master prompt that combines at least 4 different techniques we've learned.

{{< details "Show Example Solution" >}}

**Comprehensive Prompt**:
```
[ROLE] You are an expert rare books cataloger with specialization in
19th-century literature.

[TASK] Create a catalog entry for this rare book, assessing its
condition and estimating its significance.

[FEW-SHOT EXAMPLES]
Example 1:
Input: First edition Dickens, leather binding, some foxing, spine intact
Output: {"condition": "Good", "significance": "High", "notes": "Foxing typical for age"}

Example 2:
Input: Second edition Austen, cloth binding, water damage, loose pages
Output: {"condition": "Fair", "significance": "Medium", "notes": "Restoration recommended"}

[INPUT BOOK INFORMATION]
Title: Pride and Prejudice
Author: Jane Austen
Edition: First edition, second printing
Year: 1813
Binding: Original boards, partially detached
Pages: Complete, some browning, no tears
Provenance: Estate sale, previous owner's bookplate present

[CHAIN OF THOUGHT ANALYSIS]
Assess the condition step-by-step:
1. Evaluate binding condition
2. Check page condition
3. Consider historical significance
4. Note provenance value
5. Determine overall grade

[OUTPUT FORMAT - JSON]
{
  "catalogEntry": {
    "title": "",
    "author": "",
    "edition": "",
    "year": ,
    "condition": {
      "overall": "Excellent/Good/Fair/Poor",
      "binding": "",
      "pages": "",
      "grade": "A-F"
    },
    "significance": "High/Medium/Low",
    "estimatedValue": "$X,XXX - $X,XXX",
    "notes": "",
    "recommendedAction": ""
  }
}

[CONSTRAINTS]
- Do NOT include insurance valuations
- Do NOT make authentication claims without caveats
- DO include condition assessment reasoning
- DO note any red flags for authenticity

[ANALYSIS]
Now assess the book and create the catalog entry.
```

{{< /details >}}

---

## Self-Assessment Checklist

After completing these exercises, can you:

- [ ] Write clear, specific prompts with context?
- [ ] Use few-shot learning for pattern-based tasks?
- [ ] Apply chain-of-thought for complex reasoning?
- [ ] Assign roles to influence model responses?
- [ ] Get structured output (JSON, tables, etc.)?
- [ ] Add effective constraints to your prompts?
- [ ] Break complex tasks into steps?
- [ ] Identify and fix bad prompts?
- [ ] Combine multiple techniques effectively?

{{< callout type="success" >}}
**Congratulations!** If you've completed these exercises, you now have practical experience with effective prompting. These skills will be valuable throughout the workshop and beyond.
{{< /callout >}}

---

## What's Next?

You've completed Part 1: Fundamentals!

{{< cards >}}
  {{< card link="/v2/part2-intermediate" title="Part 2: Intermediate Topics" icon="arrow-right" subtitle="Python integration, embeddings, and RAG" >}}
{{< /cards >}}

Or take a break - you've earned it! When you're ready, Part 2 covers programmatic interaction with LLMs, vector embeddings, and building RAG systems.
