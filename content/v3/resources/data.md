---
title: Data and licenses
weight: 4
---

The data files for Part 2 are in the notebooks repository under `data/`. The source and license terms of each file are recorded in `data/ATTRIBUTION.md`. This page summarizes them.

## License table

| File | Source | License | Retrieved | Changes |
|---|---|---|---|---|
| `vocab/stw.json` | STW Thesaurus for Economics, ZBW | CC BY 4.0 | 2026-10-15 | Descriptors with prefLabel, altLabel, scopeNote and broader extracted into JSON |
| `vocab/unesco.json` | UNESCO Thesaurus | CC BY-SA 3.0 IGO | 2026-10-15 | Concepts with labels and scope notes extracted into JSON |
| `vocab/goldset.json`, `vocab/goldset-corpora.json` | Built for this workshop from the two vocabularies above | Labels keep their source licenses; structure CC BY 4.0 | 2026-10-09 | Held-out synonyms and cross-lingual pairs |
| `texts/sample-works.txt` | Written for the 2024 edition of this workshop | CC BY 4.0 | 2024-11 | None |
| `cards/*.txt`, `cards/cards-gold.json` | Written for this workshop | CC BY 4.0 | 2026-10 | None |
| `docs/ifla-lrm.md` | IFLA Library Reference Model | CC BY 4.0 | 2026-10-15 | Text extracted from the PDF, section titles kept as plain lines |
| `docs/dcmi-terms.md` | DCMI Metadata Terms | CC BY 4.0 | 2026-10-15 | HTML converted to text |
| `fixtures/**.json` | lobid-gnd (hbz, CC0), Wikidata (CC0 for data; CC BY-SA 3.0 for text), LINDAS (Swiss federal open data) | As stated | 2026-10-15 | Recorded API responses for offline fallback |

## Prebuilt index files

Notebook 03 builds two label indexes, or loads them from `runs/` if the files are already there. The prebuilt files are not in the repository. Download them from the [swib26 release](https://github.com/nishad/llm-workshop-notebooks/releases/tag/swib26) of the notebooks repository; the direct links are in step 4 of [Before you start](/v3/before-you-start#4-part-2-only-python-and-the-notebooks). The indexes are built from the two vocabularies above, so their labels keep the source licenses.

| File | Size | sha256 |
| --- | --- | --- |
| `stw-de-labels.sqlite` | 85.7 MB | `d85108cd6d38b949ac6c80decbf405021a61a7db4670495b2dea4e63807559bf` |
| `unesco-en-labels.sqlite` | 34.4 MB | `47728635aff8bd8fb9d19197c34d1f1e5e05efea039bd9429bbfa4448ddda537` |

The steps to download and check the files are on the [environment page](/v3/part2/01-environment#download-the-prebuilt-index-files).

## Vocabularies considered and not used

| Vocabulary | Why not |
|---|---|
| Dewey Decimal Classification | The endpoint is dead and OCLC's terms are restrictive. |
| Homosaurus v4 | Licensed CC BY-NC-ND, so it can be displayed but not adapted or used commercially. |
| Getty vocabularies | Bulk downloads are unavailable in 2026. |

## Retired dataset

The 2025 edition's sample book is no longer used. It is licensed CC BY-SA 4.0.
