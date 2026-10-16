---
title: Exercises
weight: 3
---

This page has eight exercises, and each has three tiers:

- **GUI**: do the task in your chat window. GUI is short for graphical user interface, the kind of app you click and type in.
- **Run and change**: change one thing in the prompt and compare.
- **Stretch**: go one step further.

Try your own prompt first. Then open the solution and compare. The solutions show one captured run (nishad/apertus:8b, temperature 0.8, 15 October 2026). Temperature is the setting that controls how much the answers vary, so yours will differ.

We do Exercises 1, 2, 4 and 6 together in the live session. Exercises 3, 5, 7 and 8 are for you to do afterwards.

{{< callout type="info" >}}
Where an exercise uses "the sample text", paste the text from [Basics](/v3/part1/04-prompting/basics#the-sample-text).
{{< /callout >}}

## Exercise 1: Extract to a table (live)

Turn the sample text into a table with the columns Title, Author, Year, Language and Original title.

- **GUI:** write a prompt that gives that table from the sample text.
- **Run and change:** add a column "Script" (Latin, Cyrillic, Han, and so on).
- **Stretch:** ask for CSV (comma-separated values, a plain-text format that spreadsheets can open) instead of a table. Then paste in a sentence with a title that contains a comma, such as the made-up title "Love, Death and Taxes". Check how the answer handles the comma.

{{< details title="Show a solution" >}}

**Prompt:**

```
Extract every book from this text into a Markdown table with the columns Title | Author | Year | Language | Original title. Put the original title in its own script where the text gives it; otherwise leave the cell empty.
Return only the table.

Text:
[the sample text from above]
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
| Title                | Author       | Year | Language | Original title |
|----------------------|--------------|------|----------|---------------|
| Of Mice and Men     | John Steinbeck | 1937 | English   | None           |
| Cien años de soledad | Gabriel García Márquez | 1967 | Spanish   | Cien años de soledad |
| Pride and Prejudice | Jane Austen    | 1813 | English   | None           |
| ノルウェイの森 (Noruwei no Mori) | Haruki Murakami | 1987 | Japanese  | ノルウェイの森 (Noruwei no Mori) |
| The Midnight Library | Matt Haig      | 2020 | English   | None           |
| Die Verwandlung      | Franz Kafka   | 1915 | German    | Die Verwandlung |
| Преступление и наказание | Fyodor Dostoevsky | 1866 | Russian   | Преступление и наказание |
| Les Misérables      | Victor Hugo    | 1862 | French    | Les Misérables |
| Harry Potter and the Philosopher’s Stone | J.K. Rowling | 1997 | English   | None           |
| Don Quixote         | Miguel de Cervantes | 1605 and 1615 | Spanish   | Don Quixote |
| The Odyssey         | Homer         | ~8th century BC | Ancient Greek | None           |
| Foundation         | Isaac Asimov  | 1951 (original publication) | English | None           |
| Vingt mille lieues sous les mers | Jules Verne | 1869 | French | Vingt mille lieues sous les mers |
| Cien sonetos de amor | Pablo Neruda | 1959 | Spanish | Cien sonetos de amor |
| Leaves of Grass     | Walt Whitman  | 1855 | English   | None           |
| رباعیات خیام (The Rubaiyat of Omar Khayyam) | Attributed to Omar Khayyam | 12th century | Persian | رباعیات خیام (The Rubaiyat of Omar Khayyam) |
| 蛙 (Frog)           | Mo Yan        | 2009 | Chinese    | 蛙 (Frog) |
| The Namesake       | Jhumpa Lahiri | 2003 | English   | None           |
| Gunjan              | Harivansh Rai Bachchan | 1935 | Hindi | Gunjan |
| Pippi Longstocking | Astrid Lindgren | 1945 | Swedish | Pippi Långstrump |
| The Little Prince   | Antoine de Saint-Exupéry | 1943 | French | Le Petit Prince |
| Divina Commedia    | Dante Alighieri | 1308–1320 | Italian | La Divina Commedia |
```

All 22 works are there, in the right order, with the right years and languages. Look closely at the last column:

- Where the text gives no original title, the model wrote "None" instead of leaving the cell empty.
- For Don Quixote it repeated "Don Quixote" as the original title. The text does not give the Spanish title.
- For the Divina Commedia it wrote "La Divina Commedia", which is not in the text. It filled a gap from memory.
- For the Japanese and Persian works it repeated the romanized or bracketed form from the text.

When the text gives no value, the cell should stay empty. The prompt already asked for that. Add "Do not use your own knowledge." to the prompt and compare.

{{< /details >}}

## Exercise 2: Few-shot classification (live)

Classify library materials as BOOK, JOURNAL, DVD or DATABASE. In a few-shot prompt you show the model a few examples first, like these:

```
"Pride and Prejudice" -> BOOK
"Nature Scientific Journal" -> JOURNAL
"The Matrix (1999)" -> DVD
"JSTOR Academic Database" -> DATABASE
```

Items to classify:

1. "National Geographic Documentary Collection"
2. "The New York Times Historical Archive"
3. "To Kill a Mockingbird"
4. "Annual Review of Psychology"

- **GUI:** write a few-shot prompt for these four items.
- **Run and change:** ask for the answers in the form: Number. "Title" -> CATEGORY.
- **Stretch:** add an ambiguous item, for example an audio recording that fits none of the four labels. Then ask for a confidence word (high, medium or low) for each item.

{{< details title="Show a solution" >}}

This solution is for the stretch version: five items, one of them ambiguous, with a confidence word.

**Prompt:**

```
Classify library materials into categories: BOOK, JOURNAL, DVD or DATABASE.

Examples:
"Pride and Prejudice" -> BOOK
"Nature Scientific Journal" -> JOURNAL
"The Matrix (1999)" -> DVD
"JSTOR Academic Database" -> DATABASE

Now classify these:
1. "National Geographic Documentary Collection"
2. "The New York Times Historical Archive"
3. "To Kill a Mockingbird"
4. "Annual Review of Psychology"
5. "Hamlet (audio recording, 2 CDs)"

Format: Number. "Title" -> CATEGORY (confidence: high, medium or low)
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
1. "National Geographic Documentary Collection" -> DATABASE (confidence: high)
2. "The New York Times Historical Archive" -> DATABASE (confidence: high)
3. "To Kill a Mockingbird" -> BOOK (confidence: high)
4. "Annual Review of Psychology" -> JOURNAL (confidence: high)
5. "Hamlet (audio recording, 2 CDs)" -> DVD (confidence: high)
```

The book and the journal are right. You could argue about the other three. The Documentary Collection could be DVDs or a streaming database. The audio recording of Hamlet fits none of the four labels, and the model forced it into DVD and called it "high" confidence. Every answer carries "high". The confidence word shows what the model writes, not how reliable it is.

When the labels do not fit, add a fifth label such as OTHER and say "use OTHER when none of the labels fits".

{{< /details >}}

## Exercise 3: Library events to JSON

Turn this text into JSON, a text format that programs can read directly.

```
Our library has the following upcoming events:
Book Club meets every Tuesday at 6pm in the Reading Room.
Story Time for kids happens on Saturdays at 10am in the Children's Section.
Tech Help sessions are offered Wednesdays at 2pm in the Computer Lab.
Author Talk with Jane Smith is scheduled for March 15th at 7pm in the Main Hall.
```

- **GUI:** ask for a JSON list with name, day or date, time and location.
- **Run and change:** ask for times in 24-hour format.
- **Stretch:** ask for ISO dates (2026-03-15) and check them. Which events have a date, and which repeat?

{{< details title="Show a solution" >}}

**Prompt:**

```
Extract the library events from the text below. Return only valid JSON: a list of objects with the keys "name", "day_or_date", "time" and "location".

Text:
Our library has the following upcoming events:
Book Club meets every Tuesday at 6pm in the Reading Room.
Story Time for kids happens on Saturdays at 10am in the Children's Section.
Tech Help sessions are offered Wednesdays at 2pm in the Computer Lab.
Author Talk with Jane Smith is scheduled for March 15th at 7pm in the Main Hall.
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

````
```json
[
    {
        "name": "Book Club",
        "day_or_date": "every Tuesday",
        "time": "6pm",
        "location": "Reading Room"
    },
    {
        "name": "Story Time for kids",
        "day_or_date": "on Saturdays",
        "time": "10am",
        "location": "Children's Section"
    },
    {
        "name": "Tech Help sessions",
        "day_or_date": "Wednesdays",
        "time": "2pm",
        "location": "Computer Lab"
    },
    {
        "name": "Author Talk with Jane Smith",
        "day_or_date": "March 15th",
        "time": "7pm",
        "location": "Main Hall"
    }
]
```
````

The JSON is valid and the values are right.

The prompt said "Return only valid JSON", and the model still wrapped it in a code fence. A code fence is a pair of lines with three backtick characters that mark the start and end of a code block. The answer above is shown as the model wrote it, so you see a fence inside a fence. A program that reads the answer has to remove the fence first.

The values are copied as written ("every Tuesday", "on Saturdays", "6pm"). That is faithful to the text and not yet clean data. Only one event has a date, and it has no year, so an ISO date would need a guess. For the stretch task, decide what should go into a date field for the three events that repeat.

{{< /details >}}

## Exercise 4: Multilingual subject terms (live)

Give the German, French and English preferred term for three concepts. Then ask whether the terms exist in a thesaurus. The model cannot look the thesaurus up. The point is to notice a confident guess.

- **GUI:** ask: "Give the German, French and English preferred term for these concepts: inflation, copyright, climate change." Then ask: "Which of these terms exist in the STW Thesaurus for Economics?" with your list.
- **Run and change:** add two concepts of your own from your field.
- **Stretch:** ask in a new chat for the same translations and compare the two answers.

{{< details title="Show a solution" >}}

**Step 1: the terms**

**Prompt:**

```
Give the German, French and English preferred term for these concepts: inflation, copyright, climate change. Answer as a table.
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
| Concept              | German          | French          | English       |
|----------------------|----------------|----------------|---------------|
| Inflation              | Inflation       | Inflation      | Inflation     |
| Copyright             | Urheberrecht    | Droit d'auteur | Copyright    |
| Climate Change        | Klimawandel     | Changement climatique | Climate Change |
```

The German and French terms look reasonable and consistent. For comparison, the STW Thesaurus for Economics (version 9.20) uses Inflation, Urheberrecht (with the English label "Copyright law") and Klimawandel (with the English label "Climate change").

**Step 2: do they exist in STW?**

**Prompt:**

```
Which of these terms exist in the STW Thesaurus for Economics? Answer yes or no for each: Inflation, Urheberrecht, Klimawandel, Teuerung, Bibliotheksnutzung.
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
Inflation: yes
Urheberrecht: no
Klimawandel: no
Teuerung: yes
Bibliotheksnutzung: yes
```

We checked these five terms against the STW 9.20 data held in the notebooks repository. We looked for each term as a preferred label and as an alternative label, in German and in English:

| Term | The model said | In STW 9.20 |
|---|---|---|
| Inflation | yes | yes |
| Urheberrecht | no | yes |
| Klimawandel | no | yes |
| Teuerung | yes | no |
| Bibliotheksnutzung | yes | no |

Four of five answers are wrong, and the model sounded equally sure of each. The model has no access to the thesaurus. Asking it whether a term exists in a vocabulary invites a guess. Part 2 checks terms against the real vocabulary.

{{< /details >}}

## Exercise 5: Assign from a controlled list

You get ten descriptors from the STW Thesaurus for Economics and three abstracts. Assign at most two descriptors to each abstract.

Descriptors:

```
Inflation, Geldpolitik, Arbeitslosigkeit, Klimawandel, Umweltpolitik, Energiepolitik, Urheberrecht, Datenschutz, Open Access, Filmproduktion
```

Abstracts (written for this exercise):

1. This paper studies how interest rate decisions by the European Central Bank affected consumer prices and youth unemployment in southern Europe between 2022 and 2024.
2. The article analyses how the revised EU copyright rules changed licensing contracts between streaming services and independent producers of cinema and television films.
3. We compare national energy and climate policies and estimate how carbon pricing changed household heating costs in Germany.

- **GUI:** write a prompt that makes the model use only the descriptors from the list.
- **Run and change:** remove "at most two" and see whether the model adds descriptors that are not in the list.
- **Stretch:** ask the model to justify each assignment with a quote from the abstract.

{{< details title="Show a solution" >}}

**Prompt:**

```
Assign at most two descriptors to each abstract. Use only descriptors from this list, written exactly as given.

Descriptors: Inflation, Geldpolitik, Arbeitslosigkeit, Klimawandel, Umweltpolitik, Energiepolitik, Urheberrecht, Datenschutz, Open Access, Filmproduktion

Abstract 1: This paper studies how interest rate decisions by the European Central Bank affected consumer prices and youth unemployment in southern Europe between 2022 and 2024.

Abstract 2: The article analyses how the revised EU copyright rules changed licensing contracts between streaming services and independent producers of cinema and television films.

Abstract 3: We compare national energy and climate policies and estimate how carbon pricing changed household heating costs in Germany.

Answer in the form: Abstract number: descriptor, descriptor
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
Abstract 1: Geldpolitik, Inflation
Abstract 2: Urheberrecht, Filmproduktion
Abstract 3: Energiepolitik, Klimawandel
```

Every descriptor comes from the list, and the pairs are sensible. Abstract 1 has three topics (prices, interest rates, unemployment) and room for only two, so the model dropped Arbeitslosigkeit. That is a matter of judgment. In the stretch version, a quote for each choice shows what the model relied on. The model can still break an instruction such as "use only these descriptors", so check each answer against the list.

{{< /details >}}

## Exercise 6: The hallucination probe (live)

Ask for identifiers the model cannot look up. When a model invents an answer and presents it as fact, we call that a hallucination.

- **GUI:** ask for the ISBN of a book and the DOI of an article, both real. Look the answers up in a catalog (for example the DNB catalog or your own) and in Crossref. Write down what is wrong.
- **Run and change:** ask for the same identifier twice in new chats. Do the two answers agree?
- **Stretch:** ask "How sure are you? Where did you get this?" and see what the model offers.

{{< details title="Show a solution" >}}

**Book:**

**Prompt:**

```
What is the ISBN of the book "Das Parfum" by Patrick Süskind, published by Diogenes?
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
The ISBN of the book "Das Parfum" by Patrick Süskind, published by Diogenes, is 9783257061675.
```

**Article:**

**Prompt:**

```
What is the DOI of the article "The FAIR Guiding Principles for scientific data management and stewardship" by Mark D. Wilkinson and colleagues, published in Scientific Data in 2016?
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
The DOI for the article "The FAIR Guiding Principles for scientific data management and stewardship" by Mark D. Wilkinson and colleagues is 10.1038/sdata.2016.44.
```

We checked both on 15 October 2026.

**The ISBN.** The number 9783257061675 is not a valid ISBN-13. Its check digit is wrong: for those first twelve digits, the correct check digit is 3, not 5. A search for it in the DNB catalog (through lobid-resources) returns no records. The same number with the correct check digit, 9783257061673, belongs to a different book: "Verrechnet" by Dick Francis, published by Diogenes (Zürich, 1998). The DNB records for Patrick Süskind, "Das Parfum", published by Diogenes include these ISBNs, among others: 978-3-257-22800-7, 978-3-257-06540-4, 978-3-257-80233-7, 978-3-257-80037-1, 978-3-257-01787-8 and 978-3-257-01678-9. None matches the model's answer.

**The DOI.** Crossref lists the FAIR article by Wilkinson and colleagues (Scientific Data, 2016) under 10.1038/sdata.2016.18. The model's DOI, 10.1038/sdata.2016.44, is real, but it belongs to another paper: "The brain imaging data structure, a format for organizing and describing outputs of neuroimaging experiments" (Scientific Data, 2016). So the model produced a DOI that works as a link but points to the wrong article. That is worse than an invalid one, because a quick click on the link would look like success.

Sources: DNB catalog via lobid-resources (lobid.org/resources) and the Crossref REST API, queried 15 October 2026.

{{< /details >}}

## Exercise 7: Debugging bad prompts

These prompts have problems. Find them and fix them.

```
tell me stuff about libraries
```

```
Extract the data from this text and make it look nice and also translate it to Spanish and summarize it in French and create a chart showing the timeline and write a poem about it.
```

```
How do I fix this?
```

- **GUI:** write down what is wrong with each, in one line.
- **Run and change:** rewrite the first prompt and compare the answers.
- **Stretch:** split the second prompt into steps, and decide which steps need a checkpoint, a pause to check the result before going on.

{{< details title="Show a solution" >}}

What is wrong:

- **Prompt 1:** "stuff" and "libraries" are both vague, and the prompt names no audience, length or focus.
- **Prompt 2:** six unrelated tasks with no priority and no format. Split them.
- **Prompt 3:** "this" points to nothing the model can see, and there is no error message, system or goal.

Here is the first prompt as written:

**Prompt:**

```
tell me stuff about libraries
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
Sure, I'd be happy to share some information about libraries! Here's a brief overview:

1. **What is a Library?**
   - A library is an institution that collects, stores, and provides access to a variety of resources such as books, magazines, audio-visual materials, digital media, and online databases.

2. **Types of Libraries**
   - Public Libraries: Open to the general public and often offer a wide range of services.
   - Academic Libraries: Found in universities and colleges, these libraries provide resources for research and study purposes.
   - Special Libraries: Focus on a specific field or topic, such as medical libraries or law libraries.
   - School Libraries: Found in elementary and secondary schools, they provide resources for students and teachers.

3. **Services Offered by Libraries**
   - Circulation Services: Allowing users to borrow and return materials.
   - Reference Services: Providing research assistance and answering user inquiries.
   - Programming Services: Organizing workshops, seminars, and other events to promote literacy and learning.
   - Access to Digital Resources: Many libraries offer online databases, e-books, and other digital resources.

4. **Benefits of Using Libraries**
   - Free or low-cost access to a wide range of materials.
   - Expert assistance from librarians.
   - A quiet and conducive environment for studying and research.
   - Community hubs for educational and social activities.

5. **How to Use a Library**
   - Obtain a library card, which is usually free.
   - Use the library catalog to search for materials.
   - Visit the library in person or use its online services.
   - Ask a librarian for help if needed.

6. **Digital Libraries**
   - Online platforms that offer access to digital materials such as e-books, audiobooks, and online courses.
   - Examples include OverDrive, Hoopla Digital, and Project Gutenberg.

7. **Future of Libraries**
   - Libraries are evolving to meet changing user needs. Many are incorporating digital resources, makerspaces (equipped with cutting-edge technology), and community meeting areas.

Remember, libraries are not just about books anymore. They offer a range of services and resources to support learning, research, and community engagement. If you have any specific questions about libraries, feel free to ask!
```

And here is a repaired version:

**Prompt:**

```
Explain the role of public libraries in modern communities. Focus on educational programs, community services and digital resources. Target audience: someone considering a career in library science. Length: about 150 words. Tone: informative and encouraging.
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
As a potential career in library science, understanding the role of public libraries in modern communities is crucial. Public libraries act as vibrant community hubs, offering educational programs that range from literacy classes for adults to coding workshops for children. These programs foster a love of learning and support skill development.

Community services, such as book clubs, author talks, and cultural events, bring people together, promoting a sense of belonging and social cohesion. Libraries also provide essential digital resources, including e-books, online databases, and internet access, which are especially important in areas with limited technological infrastructure.

In summary, public libraries are dynamic and integral to modern communities, offering a range of educational programs, community services, and digital resources that enhance the social, economic, and educational well-being of their patrons. This diverse role is both a challenge and an opportunity for library professionals, making it a rewarding career choice.
```

The first answer is 340 words long and covers a bit of everything about libraries. The repaired one is about 150 words and written for the stated reader. It is not perfect (the opening sentence is awkward), but it does what was asked. The model handled "about 150 words" well. It is exact counts that it misses.

{{< /details >}}

## Exercise 8: Challenge, the rare-book cataloger

Write one prompt that combines four techniques: a role, two examples, a JSON shape and constraints. The book:

```
Pride and Prejudice by Jane Austen, 1813, original boards partially detached, pages complete with some browning and no tears, bookplate of a previous owner present.
```

Ask for a catalog entry with title, author, year, condition and notes. Do not ask for a valuation.

- **GUI:** build the prompt in your chat window.
- **Run and change:** change the condition scale and see if the model follows it.
- **Stretch:** ask for a second field with the reason for the condition grade, in at most ten words.

{{< details title="Show a solution" >}}

**Prompt:**

```
You are a rare books cataloguer. Create a catalogue entry for the book below. Return only JSON with the keys "title", "author", "year", "condition" and "notes". Condition must be one of: Fine, Good, Fair, Poor. Do not include a valuation or any price.

Example 1
Input: First edition of Dickens, leather binding, some foxing, spine intact.
Output: {"title": "Oliver Twist", "author": "Charles Dickens", "year": 1838, "condition": "Good", "notes": "Foxing typical for age"}

Example 2
Input: Second edition of Austen, cloth binding, water damage, loose pages.
Output: {"title": "Emma", "author": "Jane Austen", "year": 1816, "condition": "Fair", "notes": "Restoration recommended"}

Now catalogue this book:
Pride and Prejudice by Jane Austen, 1813, original boards partially detached, pages complete with some browning and no tears, bookplate of a previous owner present.
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
{"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813, "condition": "Fine", "notes": "Bookplate present, boards partially detached, browning typical for age"}
```

The JSON is valid, the keys are right and there is no valuation. The condition grade is open to question: with the boards partially detached, "Fine" is generous, and "Fair" or "Good" would be easier to defend. The model followed the format and the constraints, and it chose the grade by matching patterns. A cataloger reads the grade and decides.

{{< /details >}}

## Self-assessment

Tick what you can do now.

- [ ] I can split a prompt into context, instruction, input, output format and constraints.
- [ ] I can improve a vague prompt in steps and say what each step fixed.
- [ ] I can write a few-shot prompt for a classification task.
- [ ] I can ask for a table, a JSON list or CSV, and I know the shape is only requested, not enforced.
- [ ] I know that small models miss exact counts and numeric filters.
- [ ] I check identifiers and vocabulary terms against a real source.
- [ ] I can say why a confident answer is not the same as a correct one.

{{< callout type="success" >}}
**What you should see:** a table from Exercise 1, valid JSON from Exercise 3, and in Exercise 6 a confident answer that your own check shows to be wrong. If a model ignored a numeric filter or invented an identifier, that is the expected result, not a mistake of yours.
{{< /callout >}}
