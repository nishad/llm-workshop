---
title: Provenance
weight: 3
---

With a fully open model you can ask what it was trained on and get an answer. Here are three lookups you can do in a browser, without logging in.

## Lookup 1: the Common Crawl index

Common Crawl is a public archive of web pages, and many training sets start from it. Open this URL, and replace `swib.org` with your own domain:

```
https://index.commoncrawl.org/CC-MAIN-2026-39-index?url=*.swib.org&output=json&limit=5
```

Each line is one captured page. It proves your pages were crawled. It does not prove they were used: that depends on the filters of the model's builders and on your robots.txt. swib.org publishes no robots.txt.

## Lookup 2: infini-gram

Open the web demo at infini-gram.io and count a phrase in a training set. The same count works as a POST request with this body:

```json
{"index": "v4_dolma-v1_7_llama", "query_type": "count", "query": "Deutsche Nationalbibliothek"}
```

Counts from October 2026:

- "Semantic Web in Libraries" appears 159 times in Dolma 1.7.
- "Deutsche Nationalbibliothek" appears 4,291 times in OLMo 2's training data.

It proves the phrase is in the data, and how often.

## Lookup 3: OlmoTrace

In the Ai2 Playground, OlmoTrace links spans of a model's output back to the training documents that contain them. It proves where a phrase in an answer can come from.

## Why only tier 3

These lookups work because the training data is public. For Qwen, gpt-oss or DeepSeek there is nothing to query, so the same questions have no answer.

## The Apertus EU public summary

The EU public summary is the best single document to read. Five things to find in it:

- Named datasets, with their licences.
- Domains visited by the custom crawler.
- Which other models generated the synthetic data.
- The opt-out method.
- Size bands for the data.

{{< callout type="info" >}}
A summary is a claim you can read. A dataset you can query is a claim you can test.
{{< /callout >}}

## Exercise

Do as many tiers as you like.

1. Look up your institution's domain in the Common Crawl index.
2. Count your institution's name in infini-gram.
3. Stretch: compare two institutions and explain the difference.

{{< details title="Show a solution" >}}
A domain with no results in the index may not have been captured in this crawl. Try another crawl. A name with a low count may be spelled differently in other languages, so try variants.
{{< /details >}}

For how this connects to repeatable results, see [Part 2](/v3/part2).
