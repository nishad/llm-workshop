---
title: Data and licences
weight: 4
---

The data files for Part 2 live in the notebooks repository under `data/`. Each file's source and terms are recorded in `data/ATTRIBUTION.md`, summarized here.

## Licence table

| File | Source | Licence | Retrieved | Changes |
|---|---|---|---|---|
| `vocab/stw.json` | STW Thesaurus for Economics, ZBW | CC BY 4.0 | 2026-10-15 | Descriptors with prefLabel, altLabel, scopeNote and broader extracted into JSON |
| `vocab/unesco.json` | UNESCO Thesaurus | CC BY-SA 3.0 IGO | 2026-10-15 | Concepts with labels and scope notes extracted into JSON |
| `vocab/goldset.json`, `vocab/goldset-corpora.json` | Built for this workshop from the two vocabularies above | Labels keep their source licences; structure CC BY 4.0 | 2026-10-09 | Held-out synonyms and cross-lingual pairs |
| `texts/sample-works.txt` | Written for the 2024 edition of this workshop | CC BY 4.0 | 2024-11 | None |
| `cards/*.txt`, `cards/cards-gold.json` | Written for this workshop | CC BY 4.0 | 2026-10 | None |
| `docs/ifla-lrm.md` | IFLA Library Reference Model | CC BY 4.0 | 2026-10-15 | Text extracted from the PDF, section titles kept as plain lines |
| `docs/dcmi-terms.md` | DCMI Metadata Terms | CC BY 4.0 | 2026-10-15 | HTML converted to text |
| `fixtures/**.json` | lobid-gnd (hbz, CC0), Wikidata (CC0 for data; CC BY-SA 3.0 for text), LINDAS (Swiss federal open data) | As stated | 2026-10-15 | Recorded API responses for offline fallback |

## Prebuilt index files

Notebook 03 builds two label indexes and loads them from `runs/` when the files exist. The prebuilt files are not in the repository; the download post on the [forum topic](https://forum.swib.org/t/getting-started-with-local-llms/1732) links to them. They are built from the two vocabularies above, so their labels keep the source licences.

| File | Size | sha256 |
| --- | --- | --- |
| `stw-de-labels.sqlite` | 85.7 MB | `5d89c6704268b0c0ae29656dcfc31ea3d1402469edbd76f80a043f1843b07e8c` |
| `unesco-en-labels.sqlite` | 34.4 MB | `c4755d17a9c00c742f9f2b601e82e51165f69d5380395adaa083a7ea43ae10c7` |

Building the two indexes takes about five minutes on an Apple Silicon Mac with 64 GB and far longer on a CPU-only laptop, so on the 8 GB tier downloading them is the way to follow notebook 03 live.

## Vocabularies considered and not used

| Vocabulary | Why not |
|---|---|
| Dewey Decimal Classification | The endpoint is dead and OCLC's terms are restrictive. |
| Homosaurus v4 | Licensed CC BY-NC-ND, so it can be displayed but not adapted or used commercially. |
| Getty vocabularies | Bulk downloads are unavailable in 2026. |

## Retired dataset

The dataset used in the 2025 edition is no longer used. Its correct licence is CC BY-SA 4.0.
