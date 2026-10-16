---
title: Next steps
weight: 5
---

Ideas for continuing after the workshop. Start small, keep a person in the loop to review what the model produces, and check every output against your own data.

## Library tasks to try next

**Subject indexing against GND or LCSH, with review.** Ask the model to propose subject headings for a title and abstract. Then use search to match each proposal to a real heading, and have a cataloger accept or reject it. Builds on notebook 03 (vocabulary search) and notebook 02 (structured output). For indexing in your everyday work, look at Annif first.

**Authority reconciliation.** Match names in a spreadsheet to GND records with the lobid reconciliation API, using OpenRefine as the interface. A model can help by putting messy name strings into a consistent form before matching. Builds on notebook 05 (tool use).

**Record quality assurance.** Ask the model to point out suspicious values, such as an ISBN in the wrong field or a date in a form that software cannot read. Have it return the issues as a validated list. Builds on notebook 02.

**OCR post-correction.** Give the model a passage of OCR text that contains errors and ask for a corrected version. Then compare the two with a diff tool before you accept anything. The tool shows exactly what changed. Builds on notebook 01 (Python and Ollama).

**Multilingual catalog text.** Extract fields from German, French or Italian cards, or translate subject notes, and keep the original beside the result. Builds on notebook 02.

**SPARQL drafting with human review.** Let the model propose a query from a plain-language question, show it to the person who asked, and run it only after they approve. Builds on notebook 05.

## Tools to look at

- **Annif** for automated subject indexing with your own vocabulary.
- **The lobid reconciliation service** for matching against GND from OpenRefine.
- **Skosmos** for publishing and browsing SKOS vocabularies, as the STW thesaurus does.

## SWIB26 sessions on the same day

- The keynote on critical AI literacies
- The CUNY talk on a human-in-the-loop approach to authority work
- The talk on open LLMs for keyword assignment
- The AI policy community session

See the SWIB26 program for times.

## Communities

- The [SWIB forum topic for this workshop](https://forum.swib.org/t/getting-started-with-local-llms/1732)
- [ai4lam](https://ai4lam.org)
- [Code4Lib](https://code4lib.org)

## Reading list

- [The Apertus technical report](https://arxiv.org/abs/2509.14233), arXiv 2509.14233
- [The Open Source Initiative's Open Source AI Definition](https://opensource.org/ai/open-source-ai-definition)
- The European Commission's template for the public summary of training content under the AI Act
- [Simon Willison's writing on embeddings](https://simonwillison.net/tags/embeddings/)
