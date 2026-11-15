---
title: Provenance
weight: 3
---

Provenance is the record of where something came from, and libraries already keep it for their own collections. With a fully open model you can ask what it was trained on and get an answer. Here are three lookups you can do in a browser, without logging in.

## Lookup 1: the Common Crawl index

Common Crawl is a public archive of web pages, and many training sets start from it. Open this URL, and replace `swib.org` with your own domain:

```
https://index.commoncrawl.org/CC-MAIN-2026-39-index?url=*.swib.org&output=json&limit=5
```

Each line is one captured page. A result shows that your pages were crawled. It does not prove they were used for training. That depends on how the model's builders filtered the data, and on your robots.txt file (where a website tells crawlers which pages they may not collect). As of 15 November 2026, the site swib.org published no robots.txt.

## Lookup 2: infini-gram

Open the web demo at infini-gram.io. Type in a phrase, and it counts how often that phrase appears in a training set. You can also get the same count from a program, by sending a POST request with this body:

```json
{"index": "v4_dolma-v1_7_llama", "query_type": "count", "query": "Semantic Web in Libraries"}
```

Counts from October 2026:

- "Semantic Web in Libraries" appears 159 times in Dolma 1.7.
- "Deutsche Nationalbibliothek" appears 4,291 times in OLMo 2's training data (a different index in the same demo).

A count shows that the phrase is in the data, and how often.

## Lookup 3: OlmoTrace

In the Ai2 Playground, OlmoTrace links phrases in a model's answer back to the training documents that contain the same phrases.

## Why only tier 3

These lookups work because the training data is public. For Qwen, gpt-oss or DeepSeek there is nothing to query, so the same questions have no answer.

## The Apertus EU public summary

The EU public summary (the training-content summary that the EU AI Act requires) is the best single document to read. Five things to find in it:

- Named datasets, with their licenses.
- Domains visited by the custom crawler.
- Which other models generated the synthetic data (training text written by a model rather than a person).
- The opt-out method (how content owners could ask to be left out).
- The size of the data, given in ranges rather than exact figures.

{{< callout type="info" >}}
A summary tells you what the developers say they used. Only a dataset you can query lets you check it.
{{< /callout >}}

## Exercise

Do as many of these as you like.

1. Look up your institution's domain in the Common Crawl index.
2. Count your institution's name in infini-gram.
3. A harder one: compare two institutions and explain the difference.

{{< details title="Show a solution" >}}
A domain with no results in the index may not have been captured in this crawl. Try another crawl. A name with a low count may be spelled differently in other languages, so try variants.
{{< /details >}}

For how this connects to repeatable results, see [Reproducibility](/v3/part2/02-python-and-ollama/reproducibility) in Part 2.

## Check yourself

- [ ] I looked up a domain in the Common Crawl index.
- [ ] I counted a name in infini-gram and read the number with care.
- [ ] I can say why only a tier 3 model lets me check what it read.

{{< callout type="success" >}}
**What you should see:** a list of crawl captures (or none) for your domain, and a count for your institution's name, with a note on spelling variants.
{{< /callout >}}
