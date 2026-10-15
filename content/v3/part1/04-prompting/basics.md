---
title: Basics
weight: 1
---

All the examples on this page work on one text. Learn it once, then watch one task get better with each rewrite of the prompt.

## The sample text

The text mentions 22 works in 12 languages: English, Spanish, Japanese, German, Russian, French, Ancient Greek, Persian, Chinese, Hindi, Swedish and Italian. Copy it into your chat window when an exercise says "the sample text".

```
John Steinbeck’s “Of Mice and Men” was published in English in 1937. Then there’s Gabriel García Márquez who wrote Cien años de soledad, a Spanish-language novel, published in 1967. Oh, and who can forget “Pride and Prejudice” by Jane Austen? That one came out way back in 1813 and, of course, is in English. Meanwhile, Haruki Murakami penned the Japanese novel ノルウェイの森 (Noruwei no Mori), published in 1987.

Jumping to modern times, “The Midnight Library” by Matt Haig was published in 2020 in English. In German literature, there’s Die Verwandlung (The Metamorphosis) by Franz Kafka, first published in 1915. Russian author Fyodor Dostoevsky wrote Преступление и наказание (Crime and Punishment), which was released in 1866. Oh, and in the realm of French literature, we have Les Misérables by Victor Hugo, first published in 1862.

Let’s not miss out on J.K. Rowling’s “Harry Potter and the Philosopher’s Stone,” which was released in English in 1997, or Don Quixote by Miguel de Cervantes—originally written in Spanish and first published in two parts, 1605 and 1615. Speaking of older classics, Homer’s Odyssey was written in Ancient Greek sometime in the 8th century BC.

In science fiction, Isaac Asimov’s “Foundation” series, originally published in English starting in 1951, stands out. Similarly, Jules Verne’s Vingt mille lieues sous les mers (Twenty Thousand Leagues Under the Sea), written in French, debuted in 1869.

For poetry, Pablo Neruda’s Cien sonetos de amor (One Hundred Love Sonnets), a Spanish collection, was first published in 1959. “Leaves of Grass” by Walt Whitman, an English collection of poetry, was originally published in 1855. From Persian literature, there’s رباعیات خیام (The Rubaiyat of Omar Khayyam), a collection of quatrains attributed to Omar Khayyam, written in the 12th century.

In contemporary Chinese literature, Mo Yan’s 蛙 (Frog) was published in 2009. Similarly, Jhumpa Lahiri wrote “The Namesake,” an English novel, published in 2003, focusing on Indian-American experiences. On the topic of India, गुंजन (Gunjan), a Hindi poetry collection by Harivansh Rai Bachchan, was published in 1935.

And don’t forget the Scandinavian gem “Pippi Longstocking” (Pippi Långstrump) by Astrid Lindgren, a Swedish novel published in 1945. “The Little Prince” (Le Petit Prince) by Antoine de Saint-Exupéry, a French novella, was released in 1943. In Italian literature, we have Dante Alighieri’s Divina Commedia (The Divine Comedy), written between 1308 and 1320 in Italian.
```

In the prompts below, the placeholder [the sample text from above] stands for the whole text, and [the first paragraph of the sample text] stands for its first paragraph only (the four works from Steinbeck to Murakami). The model received the actual text each time; the placeholder only keeps this page short.

## From "List the books." to a usable list

Prompting is iterative. Write a first version, read the answer, find the gap, and fix the prompt. Here is one task in four versions. Each version was run once.

### Version 1: too vague

**Prompt:**

```
List the books.

Text:
[the sample text from above]
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
The list of books includes:

1. John Steinbeck’s "Of Mice and Men" (1937)
2. Gabriel García Márquez's "Cien años de soledad" (1967)
3. Jane Austen's "Pride and Prejudice" (1813)
4. Haruki Murakami's "Noruwei no Mori" (1987)
5. Matt Haig's "The Midnight Library" (2020)
6. Franz Kafka's "Die Verwandlung" (1915)
7. Fyodor Dostoevsky's "Преступление и наказание" (1866)
8. Victor Hugo's "Les Misérables" (1862)
9. Homer's "Odyssey" (8th century BC)
10. Isaac Asimov's "Foundation" series (originally published in 1951)
11. Jules Verne's "Vingt mille lieues sous les mers" (1869)
12. Pablo Neruda's "Cien sonetos de amor" (1959)
13. Walt Whitman's "Leaves of Grass" (1855)
14. Omar Khayyam's "رباعیات خیام" (12th century)
15. Mo Yan's "蛙" (2009)
16. Jhumpa Lahiri's "The Namesake" (2003)
17. Harivansh Rai Bachchan's "गुंजन" (1935)
18. Astrid Lindgren's "Pippi Longstocking" (1945)
19. Antoine de Saint-Exupéry's "Le Petit Prince" (1943)
20. Dante Alighieri's "Divina Commedia" (1308-1320)

This list represents a diverse selection of books from various languages and genres, showcasing the richness of literary history across different cultures.
```


Count the list: 20 entries. The text has 22 works. Harry Potter and Don Quixote are missing, and the model added a closing comment nobody asked for. Nothing in the prompt said how complete or how plain the answer should be.

### Version 2: clear task, no format

**Prompt:**

```
List all books mentioned in this text.

Text:
[the sample text from above]
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
Books mentioned in the text:

1. Of Mice and Men - John Steinbeck
2. Cien años de soledad - Gabriel García Márquez
3. Pride and Prejudice - Jane Austen
4. ノルウェイの森 (Noruwei no Mori) - Haruki Murakami
5. The Midnight Library - Matt Haig
6. Die Verwandlung - Franz Kafka
7. Преступление и наказание (Crime and Punishment) - Fyodor Dostoevsky
8. Les Misérables - Victor Hugo
9. Harry Potter and the Philosopher’s Stone - J.K. Rowling
10. Don Quixote - Miguel de Cervantes
11. Odyssey - Homer
12. Foundation series - Isaac Asimov
13. Vingt mille lieues sous les mers - Jules Verne
14. Cien sonetos de amor (One Hundred Love Sonnets) - Pablo Neruda
15. Leaves of Grass - Walt Whitman
16. رباعیات خیام (The Rubaiyat of Omar Khayyam)
17. 蛙 (Frog) - Mo Yan
18. The Namesake - Jhumpa Lahiri
19. Gunjan - Harivansh Rai Bachchan
20. Pippi Longstocking (Pippi Långstrump) - Astrid Lindgren
21. The Little Prince (Le Petit Prince) - Antoine de Saint-Exupéry
22. Divina Commedia (The Divine Comedy) - Dante Alighieri
```


Now 22 entries, but the format is loose. Some lines have the title first, some have a translated title in brackets, and the Rubaiyat has no author.

### Version 3: a format

**Prompt:**

```
List all books mentioned in this text in the format: Title by Author (Year).

Text:
[the sample text from above]
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
1. "Of Mice and Men" by John Steinbeck (1937)
2. "Cien años de soledad" by Gabriel García Márquez (1967)
3. "Pride and Prejudice" by Jane Austen (1813)
4. ノルウェイの森 (Noruwei no Mori) by Haruki Murakami (1987)
5. "The Midnight Library" by Matt Haig (2020)
6. "Die Verwandlung" (The Metamorphosis) by Franz Kafka (1915)
7. "Преступление и наказание" (Crime and Punishment) by Fyodor Dostoevsky (1866)
8. "Les Misérables" by Victor Hugo (1862)
9. “Harry Potter and the Philosopher’s Stone” by J.K. Rowling (1997)
10. “Don Quixote” by Miguel de Cervantes (Originally published in two parts, 1605 and 1615)
11. Homer’s "Odyssey" (Written in Ancient Greek, 8th century BC)
12. "Foundation" series by Isaac Asimov (Originally published in English starting in 1951)
13. "Vingt mille lieues sous les mers" (Twenty Thousand Leagues Under the Sea) by Jules Verne (1869)
14. "Cien sonetos de amor" by Pablo Neruda (1959)
15. "Leaves of Grass" by Walt Whitman (1855)
16. "The Rubaiyat of Omar Khayyam" (Attributed to Omar Khayyam, 12th century)
17. "蛙" (Frog) by Mo Yan (2009)
18. "The Namesake" by Jhumpa Lahiri (2003)
19. "गुंजन" (Gunjan) by Harivansh Rai Bachchan (1935)
20. "Pippi Longstocking" (Pippi Långstrump) by Astrid Lindgren (1945)
21. "The Little Prince" (Le Petit Prince) by Antoine de Saint-Exupéry (1943)
22. "Divina Commedia" (The Divine Comedy) by Dante Alighieri (Written between 1308 and 1320 in Italian)
```


Every entry now follows Title by Author (Year), with a few exceptions: Homer's Odyssey puts the author first, and the Rubaiyat gets an "Attributed to" note. Several entries carry extra notes in brackets. Formats are followed approximately, not exactly.

### Version 4: sorting and a filter

**Prompt:**

```
List all books mentioned in this text in the format: Title by Author (Year).
Sort chronologically by year, oldest first.
Only include books published before 1950.

Text:
[the sample text from above]
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
1. Of Mice and Men by John Steinbeck (1937)
2. Cien años de soledad by Gabriel García Márquez (1967)
3. Pride and Prejudice by Jane Austen (1813)
4. ノルウェイの森 (Noruwei no Mori) by Haruki Murakami (1987)
5. Die Verwandlung by Franz Kafka (1915)
6. Преступление и наказание by Fyodor Dostoevsky (1866)
7. Les Misérables by Victor Hugo (1862)
8. The Odyssey by Homer (8th century BC)
9. “Foundation” series by Isaac Asimov (originally published in English starting in 1951)
10. Vingt mille lieues sous les mers by Jules Verne (1869)
11. “Leaves of Grass” by Walt Whitman (1855)
12. رباعیات خیام (The Rubaiyat of Omar Khayyam) by Omar Khayyam (12th century)
13. 蛙 (Frog) by Mo Yan (2009)
14. “The Namesake” by Jhumpa Lahiri (2003)
15. Gunjan by Harivansh Rai Bachchan (1935)
16. Pippi Longstocking by Astrid Lindgren (1945)
17. “The Little Prince” by Antoine de Saint-Exupéry (1943)
18. Divina Commedia by Dante Alighieri (written between 1308 and 1320)
```


### What went wrong in version 4

Version 4 asked for three things at once: the format, a chronological sort and a filter on the year. The model did the format and gave up on the rest.

- **Not sorted.** The list starts 1937, 1967, 1813, 1987. It follows the order of the text.
- **The filter let five works through.** Cien años de soledad (1967), Norwegian Wood (1987), Foundation (1951), Frog (2009) and The Namesake (2003) were published after 1950. Of the 18 entries, 13 belong and 5 do not.
- **One work that belongs is missing.** Don Quixote (1605 and 1615) is not on the list.

A small model treats "before 1950" as a phrase to echo rather than a rule to apply to each year. Comparing numbers is exactly where small models slip. The usual repair is to split the task: first extract everything with the year, then filter and sort in a second prompt, or in a spreadsheet. [Techniques](/v3/part1/04-prompting/techniques) shows the multi-step version.

{{< callout type="warning" >}}
Read the answer before you trust it. The list looked tidy. Five of its entries should not have been there, one that belonged was missing, and nothing was sorted.
{{< /callout >}}

## Five principles

Each principle comes with a poor prompt, a better one and the captured answers. These use short inputs, so you can try them quickly.

### 1. Be clear and specific

**Poor:**

**Prompt:**

```
Tell me about subject headings.
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
Subject headings are terms or phrases used to identify the content of a resource, such as a book, article, or database record. They are assigned by catalogers, librarians, or other subject experts to help users find information on a specific topic.

Subject headings are typically standardized terms, meaning they are assigned by a recognized authority, such as the Library of Congress Subject Headings (LCSH) or the Dewey Decimal Classification. This standardization ensures that different resources on the same topic will have the same subject heading, making it easier for users to locate them.

Subject headings can be assigned to various types of resources, including books, articles, images, and multimedia content. They can also be used to organize and structure information in databases, libraries, and other information systems.

Some common types of subject headings include:

* Descriptive headings: These describe the content of a resource and provide context for the subject heading.
* Analytical headings: These break down a subject into its constituent parts to provide more detailed information.
* Combining terms: These combine two or more subject headings to indicate relationships between topics.

For example, if a book is about the history of the Roman Empire, the subject heading might be "Roman Empire -- History." This heading provides a clear and concise description of the book's content and allows users to find it when searching for information on the Roman Empire.

Overall, subject headings play a critical role in information retrieval and organization, enabling users to locate specific information and navigate complex topics efficiently.
```


**Better:**

**Prompt:**

```
Explain in three sentences what a subject heading is, for a new library assistant who has never catalogued. Use plain words.
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
Subject headings are like keywords that help people find books or resources in the library. They are used to describe the main topic or theme of a book, article, or other material. For example, if you're looking for books about cats, you could use the subject heading "cats" or "felines." This makes it easier for others to find what they need.
```


The poor prompt returned a lecture of about 250 words that nobody can use at a reference desk. The better prompt names the audience, the length and the register. It returned about 60 words. (It also wrote four sentences where three were asked for, a first sign that length instructions are approximate.)

### 2. Provide context

**Poor:**

**Prompt:**

```
How do I organize this?
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
If you are asking about organizing a project, document, or tasks, it depends on the context. Here are a few general tips:

1. **Identify the Goals**: Start by clearly defining what you want to achieve. What is the purpose of this project or task? What are the end results?

2. **Create a List**: Make a list of all the tasks that need to be completed. Break down larger tasks into smaller, manageable parts.

3. **Prioritize**: Determine the order in which tasks should be completed. Which ones are urgent? Which ones are important?

4. **Assign Time Frames**: Estimate how long each task will take. Be realistic and leave some buffer time for unexpected delays.

5. **Use a Tool**: Utilize a tool or app to keep track of your tasks. Popular options include Trello, Asana, Todoist, or even a simple spreadsheet.

6. **Review Regularly**: Schedule regular check-ins with yourself to review your progress and adjust your plan if needed.

If you are referring to organizing physical items, like books or documents, the process is quite different. Here are some steps to follow:

1. **Categorize**: Group items by category (e.g., books by genre, documents by subject).

2. **Label**: Use labels or tags to identify items quickly.

3. **Store**: Find a place for each category of items. Shelves, drawers, or filing cabinets can be used.

4. **Maintain**: Regularly review and update your organization system to ensure it remains effective.

If you are referring to organizing digital information, like files or emails, the process can be similar. You can use folders, tags, or search features to keep your digital items organized.

Please provide more context so I can give you more specific advice.
```


**Better:**

**Prompt:**

```
I am a librarian organizing 500 historical photographs from the 1920s to the 1940s. In five bullet points, how should I categorize them so researchers can search them?
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
- **Subject Matter**: Categorize photographs by the subject they feature, such as landscapes, portraits, events, historical figures, or cultural icons.
- **Location**: Use geographic location as a category, such as country, city, or region, to help researchers find specific images from particular places.
- **Time Period**: Divide the photographs into categories based on the decade they were taken, i.e., 1920s, 1930s, or 1940s, to help researchers locate images from specific historical eras.
- **Event or Occasion**: Categorize photographs by significant events or occasions they depict, such as elections, wars, festivals, or inaugurations.
- **Technique or Style**: Use photographic techniques or styles as a category, such as black and white, color, documentary, or artistic photography, to help researchers find images with specific aesthetic qualities.
```


Without context the model guessed at three different meanings of "organize" (a project, physical items, digital files) and asked for more information. With the role, the collection and the purpose, it answered the actual question.

### 3. Show an example (few-shot)

**Poor (no example):**

**Prompt:**

```
Extract the book information from this sentence: Homo faber by Max Frisch came out in 1957.
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
Book Title: Homo faber
Author: Max Frisch
Year Published: 1957
```


**Better (two examples):**

**Prompt:**

```
Extract book information and format it as shown.

Input: Of Mice and Men by John Steinbeck was published in 1937.
Output: Title: Of Mice and Men | Author: John Steinbeck | Year: 1937

Input: Pride and Prejudice by Jane Austen came out in 1813.
Output: Title: Pride and Prejudice | Author: Jane Austen | Year: 1813

Input: Homo faber by Max Frisch came out in 1957.
Output:
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
Title: Homo faber | Author: Max Frisch | Year: 1957
```


Both are correct. Only the second matches the format you wanted, so you can paste it into a spreadsheet or parse it.

### 4. Say how the answer should look

**Poor:**

**Prompt:**

```
List the books mentioned in this text.

Text:
[the first paragraph of the sample text]
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
1. "Of Mice and Men" by John Steinbeck (1937)
2. "Cien años de soledad" by Gabriel García Márquez (1967)
3. "Pride and Prejudice" by Jane Austen (1813)
4. "ノルウェイの森" (Noruwei no Mori) by Haruki Murakami (1987)
```


**Better:**

**Prompt:**

```
List the books mentioned in this text. Return only a JSON array of objects with the keys "title", "author" and "year". No other text.

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


The second answer is JSON, ready for a program to read. The first is text a person has to read.

### 5. Set constraints

**Poor:**

**Prompt:**

```
Summarize why libraries keep authority files.
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
Libraries keep authority files to maintain consistency in the way they organize and record information about entities such as authors, subjects, and geographic locations. This ensures that all records relating to a particular entity are treated in the same way, which helps to improve the accuracy and reliability of the library's catalog and database. Authority files are also used to provide a standardized vocabulary for searching and retrieving information, making it easier for users to find what they are looking for. By maintaining authority files, libraries can also ensure that information is correctly linked and cross-referenced, which is essential for creating a comprehensive and cohesive collection of resources.
```


**Better:**

**Prompt:**

```
Summarize why libraries keep authority files. Use at most 40 words. Mention one benefit only. Do not use bullet points.
```

**Output** (captured with nishad/apertus:8b, digest 4a85a6fea0b8, temperature 0.8, 15 October 2026):

```
Libraries keep authority files to ensure consistency in cataloging. A benefit of this is that it helps users find and access information more efficiently and accurately.
```


The poor prompt produced a paragraph of 108 words. The better one stayed under 40 words (it used 26) and followed the other two rules. Constraints about content and style work well. Constraints about exact numbers work less well, as the [techniques page](/v3/part1/04-prompting/techniques) shows.

## A checklist for every prompt

Before you press send, ask:

- [ ] Is my instruction clear and specific?
- [ ] Have I given the context the model cannot know?
- [ ] Have I said what format the answer should have?
- [ ] Have I set constraints that matter (length, scope, what to leave out)?
- [ ] Am I asking for one task, or several unrelated ones?
- [ ] For an unusual format or a tricky task, have I added an example?
- [ ] Is the prompt self-contained, without assuming earlier conversation?
