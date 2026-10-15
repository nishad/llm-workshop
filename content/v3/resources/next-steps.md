---
title: Next steps
weight: 5
---

Ideas for continuing after the workshop. Start small, keep a person in the loop, and check every output against your own data.

## Library tasks to try next

**Subject indexing against GND or LCSH, with review.** Ask the model to propose subject headings for a title and abstract, then match each proposal to a real heading by search, and have a cataloger accept or reject. Builds on notebook 03 (vocabulary search) and notebook 02 (structured output). For production indexing, look at Annif first.

**Authority reconciliation.** Match names in a spreadsheet to GND records with the lobid reconciliation API, using OpenRefine as the interface. A model can help by normalizing messy name strings before matching. Builds on notebook 05 (tool use).

**Record quality assurance.** Ask the model to flag suspicious values such as an ISBN in the wrong field or a date that does not parse, returning a validated list of issues. Builds on notebook 02.

**OCR post-correction.** Give the model a noisy OCR passage and ask for a corrected version, then compare the two with a diff before accepting anything. Builds on notebook 01 (Python and Ollama).

**Multilingual catalog text.** Extract fields from German, French or Italian cards, or translate subject notes, and keep the original beside the result. Builds on notebook 02.

**SPARQL drafting with human review.** Let the model propose a query from a plain-language question, show it to the user, and run it only after approval. Builds on notebook 05.

## Tools to look at

- **Annif** for automated subject indexing with your own vocabulary.
- **The lobid reconciliation service** for matching against GND from OpenRefine.
- **Skosmos** for publishing and browsing SKOS vocabularies, as the STW does.

## SWIB26 sessions on the same day

- The keynote on critical AI literacies
- The CUNY talk on a human-in-the-loop approach to authority work
- The talk on open LLMs for keyword assignment
- The AI policy community session

See the SWIB26 program for times.

## Communities

- The [SWIB forum](https://forum.swib.org/t/getting-started-with-local-llms/1732)
- [ai4lam](https://ai4lam.org)
- [Code4Lib](https://code4lib.org)

## Reading list

- The Apertus technical report, arXiv 2509.14233
- The Open Source Initiative's Open Source AI Definition
- The European Union's AI Act template for the public summary of training content
- Simon Willison's writing on embeddings
