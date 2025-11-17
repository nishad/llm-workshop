---
title: Practical Examples
weight: 3
---

## Practical Automation Scripts with Ollama

Build useful automation scripts that demonstrate real-world applications.

---

## Example 1: Batch Document Summarizer

Summarize multiple documents automatically:

```python
import ollama
import os
from pathlib import Path

def summarize_files(directory, output_file='summaries.txt'):
    """
    Summarize all text files in a directory.

    Args:
        directory: Path to directory containing .txt files
        output_file: Where to save summaries
    """
    summaries = []

    for filepath in Path(directory).glob('*.txt'):
        print(f"Processing: {filepath.name}")

        # Read file
        with open(filepath, 'r') as f:
            content = f.read()

        # Generate summary
        response = ollama.generate(
            model='llama3.2',
            prompt=f"Summarize this document in 2-3 sentences:\n\n{content}"
        )

        summary = {
            'filename': filepath.name,
            'summary': response['response'].strip()
        }
        summaries.append(summary)

    # Save all summaries
    with open(output_file, 'w') as f:
        for s in summaries:
            f.write(f"File: {s['filename']}\n")
            f.write(f"Summary: {s['summary']}\n\n")

    print(f"✓ Processed {len(summaries)} files")
    print(f"✓ Saved to {output_file}")

# Usage
summarize_files('my_documents/')
```

---

## Example 2: Data Extraction from Text

Extract structured data from unstructured text:

```python
import ollama
import json

def extract_contact_info(text):
    """Extract contact information from text."""

    prompt = f"""Extract contact information from this text and return as JSON.

    Text:
    {text}

    Return JSON with these fields (use null if not found):
    {{
        "name": "person's name",
        "email": "email address",
        "phone": "phone number",
        "organization": "organization name"
    }}

    Return ONLY valid JSON, no other text.
    """

    response = ollama.generate(
        model='llama3.2',
        prompt=prompt,
        options={'temperature': 0.1}  # Low for consistent extraction
    )

    try:
        data = json.loads(response['response'])
        return data
    except json.JSONDecodeError:
        print("Warning: Could not parse JSON, returning raw response")
        return {'raw': response['response']}

# Example usage
sample_text = """
Please contact Dr. Sarah Johnson at the Metropolitan Library.
Her email is sjohnson@metrolib.org and phone is (555) 123-4567.
"""

info = extract_contact_info(sample_text)
print(json.dumps(info, indent=2))
```

**Output**:
```json
{
  "name": "Dr. Sarah Johnson",
  "email": "sjohnson@metrolib.org",
  "phone": "(555) 123-4567",
  "organization": "Metropolitan Library"
}
```

---

## Example 3: Automated Content Classification

Classify documents into categories:

```python
import ollama

def classify_document(text, categories):
    """
    Classify a document into one of the provided categories.

    Args:
        text: Document text
        categories: List of possible categories

    Returns:
        str: The selected category
    """
    categories_str = ', '.join(categories)

    prompt = f"""Classify the following text into ONE of these categories:
    {categories_str}

    Text:
    {text}

    Return ONLY the category name, nothing else.
    """

    response = ollama.generate(
        model='llama3.2',
        prompt=prompt,
        options={'temperature': 0.0}  # Deterministic
    )

    classification = response['response'].strip()

    # Validate it's a known category
    if classification not in categories:
        print(f"Warning: '{classification}' not in categories, using first")
        classification = categories[0]

    return classification

# Example: Classify library materials
categories = ['Fiction', 'Non-Fiction', 'Reference', 'Periodical', 'Multimedia']

doc1 = "A thrilling mystery novel set in 19th century London..."
doc2 = "An encyclopedia covering world history from ancient times..."
doc3 = "The latest issue of Scientific American magazine..."

print(f"Doc 1: {classify_document(doc1, categories)}")  # Fiction
print(f"Doc 2: {classify_document(doc2, categories)}")  # Reference
print(f"Doc 3: {classify_document(doc3, categories)}")  # Periodical
```

---

## Example 4: Multi-Language Translation

Translate text to multiple languages:

```python
import ollama

def translate_text(text, target_languages):
    """
    Translate text to multiple languages.

    Args:
        text: Text to translate
        target_languages: List of language names

    Returns:
        dict: Translations keyed by language
    """
    translations = {}

    for lang in target_languages:
        prompt = f"Translate the following text to {lang}:\n\n{text}\n\nTranslation:"

        response = ollama.generate(
            model='llama3.2',
            prompt=prompt
        )

        translations[lang] = response['response'].strip()

    return translations

# Example
text = "Libraries preserve knowledge for future generations."
languages = ['Spanish', 'French', 'German', 'Japanese']

results = translate_text(text, languages)

for lang, translation in results.items():
    print(f"{lang}: {translation}")
```

**Output**:
```
Spanish: Las bibliotecas preservan el conocimiento para las generaciones futuras.
French: Les bibliothèques préservent les connaissances pour les générations futures.
German: Bibliotheken bewahren Wissen für zukünftige Generationen.
Japanese: 図書館は将来の世代のために知識を保存します。
```

---

## Example 5: Interactive Q&A System

Build a simple question-answering system:

```python
import ollama

def qa_system(context, questions):
    """
    Answer multiple questions about a context.

    Args:
        context: Background text
        questions: List of questions

    Returns:
        list: Answers to questions
    """
    answers = []

    for q in questions:
        prompt = f"""Context:
        {context}

        Question: {q}

        Answer the question based only on the context provided. If the answer is not in the context, say "Information not available in the context."

        Answer:"""

        response = ollama.generate(
            model='llama3.2',
            prompt=prompt,
            options={'temperature': 0.2}
        )

        answers.append({
            'question': q,
            'answer': response['response'].strip()
        })

    return answers

# Example
context = """
The Dewey Decimal Classification (DDC) system was created by Melvil Dewey in 1876.
It organizes library materials into 10 main classes, each divided into 10 divisions,
and each division into 10 sections. The system uses three-digit numbers, with
decimals for further specificity. For example, 500 represents Natural Sciences,
510 is Mathematics, and 512 is Algebra.
"""

questions = [
    "Who created the Dewey Decimal Classification?",
    "When was it created?",
    "What number represents Mathematics?",
    "How many main classes are there?"
]

results = qa_system(context, questions)

for r in results:
    print(f"Q: {r['question']}")
    print(f"A: {r['answer']}\n")
```

---

## Example 6: Streaming Progress Indicator

Show progress while generating long responses:

```python
import ollama
import sys

def generate_with_progress(prompt):
    """Generate text with a visual progress indicator."""

    print("Generating response", end='')
    sys.stdout.flush()

    full_response = ""
    word_count = 0

    stream = ollama.generate(
        model='llama3.2',
        prompt=prompt,
        stream=True
    )

    for chunk in stream:
        full_response += chunk['response']
        word_count += len(chunk['response'].split())

        # Print dot every 10 words
        if word_count % 10 == 0:
            print('.', end='')
            sys.stdout.flush()

    print('\n\nResponse:')
    print(full_response)
    return full_response

# Example
generate_with_progress("Write a detailed explanation of how vector databases work.")
```

---

## Example 7: Template-Based Generation

Use Jinja2 templates for consistent prompts:

```python
import ollama
from jinja2 import Template

# Define a template
email_template = Template("""
Write a professional email with the following details:

To: {{ recipient }}
Subject: {{ subject }}
Tone: {{ tone }}
Key points to include:
{% for point in points %}
- {{ point }}
{% endfor %}

Email:
""")

def generate_email(recipient, subject, points, tone="professional"):
    """Generate an email using a template."""

    prompt = email_template.render(
        recipient=recipient,
        subject=subject,
        tone=tone,
        points=points
    )

    response = ollama.generate(
        model='llama3.2',
        prompt=prompt
    )

    return response['response']

# Example
email = generate_email(
    recipient="Library Board Members",
    subject="Upcoming Digital Literacy Program",
    points=[
        "Program starts next month",
        "Open to all community members",
        "Free registration available online",
        "Volunteer instructors needed"
    ],
    tone="friendly and informative"
)

print(email)
```

---

## Example 8: Error-Tolerant Batch Processing

Process many items with error handling and retry logic:

```python
import ollama
import time

def process_batch_safely(items, process_func, max_retries=3):
    """
    Process a batch of items with error handling.

    Args:
        items: List of items to process
        process_func: Function to process each item
        max_retries: Maximum retry attempts per item

    Returns:
        dict: Results and errors
    """
    results = []
    errors = []

    for i, item in enumerate(items):
        print(f"Processing {i+1}/{len(items)}: {item[:50]}...")

        for attempt in range(max_retries):
            try:
                result = process_func(item)
                results.append({
                    'item': item,
                    'result': result,
                    'status': 'success'
                })
                break  # Success, move to next item

            except Exception as e:
                if attempt == max_retries - 1:
                    # Final attempt failed
                    errors.append({
                        'item': item,
                        'error': str(e),
                        'status': 'failed'
                    })
                    print(f"  ✗ Failed after {max_retries} attempts")
                else:
                    # Retry
                    print(f"  ⚠ Attempt {attempt + 1} failed, retrying...")
                    time.sleep(1)  # Brief pause before retry

    print(f"\n✓ Successes: {len(results)}")
    print(f"✗ Failures: {len(errors)}")

    return {'results': results, 'errors': errors}

# Example process function
def summarize(text):
    response = ollama.generate(
        model='llama3.2',
        prompt=f"Summarize in one sentence: {text}"
    )
    return response['response']

# Use it
documents = [
    "Long document text here...",
    "Another document...",
    "Third document..."
]

batch_results = process_batch_safely(documents, summarize)
```

---

## Best Practices for Production Scripts

### 1. Add Logging

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('ollama_scripts.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

logger.info("Starting processing...")
```

### 2. Configuration Files

```python
import json

# config.json
{
    "model": "llama3.2",
    "temperature": 0.7,
    "max_tokens": 500
}

# Load config
with open('config.json') as f:
    config = json.load(f)

response = ollama.generate(
    model=config['model'],
    prompt=prompt,
    options={'temperature': config['temperature']}
)
```

### 3. Command-Line Arguments

```python
import argparse

parser = argparse.ArgumentParser(description='Summarize documents')
parser.add_argument('input_dir', help='Directory containing documents')
parser.add_argument('--model', default='llama3.2', help='Model to use')
parser.add_argument('--output', default='summaries.txt', help='Output file')

args = parser.parse_args()

summarize_files(args.input_dir, args.output)
```

---

## Next: Vector Embeddings

Ready to learn about semantic search?

{{< cards >}}
  {{< card link="/v2/part2-intermediate/02-embeddings" title="Vector Embeddings" icon="arrow-right" subtitle="Learn about semantic search and vector databases" >}}
{{< /cards >}}
