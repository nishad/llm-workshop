---
title: Library endpoints
weight: 3
---

Services checked in October 2026 from Python with a descriptive User-Agent. Most need no key. Services change, so treat this table as a starting point and test before you depend on one.

## Verified services

| Service | URL | Key needed | Notes |
|---|---|---|---|
| Wikidata SPARQL | `https://query.wikidata.org/sparql` | No | A descriptive User-Agent is required; generic Python agents get 403. Queries stop after 60 s. Avoid `SERVICE wikibase:label`. Fallback: `https://qlever.dev/api/wikidata`. QLever v2 endpoints open to the community in November 2026. |
| lobid-gnd | `https://lobid.org/gnd` | No | Use `format=json:suggest` for lookups. A reconciliation API is available for OpenRefine. |
| lobid-resources | `https://lobid.org/resources` | No | Bibliographic records from the German library networks. |
| DNB SRU and Linked Data Service | `https://services.dnb.de/sru` | No | Search service and linked data of the German National Library. |
| culturegraph Entity Facts | `https://hub.culturegraph.org/entityfacts` | No | Compact facts per GND entity. CC0. |
| id.loc.gov | `https://id.loc.gov` | No | Use the suggest2 service and the label service. |
| VIAF | `https://viaf.org` | No | Send an explicit `Accept: application/json` header. Bulk files have been frozen since 2024. |
| Getty vocabularies SPARQL | `https://vocab.getty.edu/sparql` | No | Bulk downloads return errors in 2026; a platform change is announced for autumn 2026. |
| data.bnf.fr | `https://data.bnf.fr/sparql` | No | SPARQL access to the French National Library's data. |
| Europeana SPARQL | `https://api.europeana.eu/sparql` | No | The Search API needs a free key. |
| Finto REST | `https://api.finto.fi` | No | 52 vocabularies. Send one request at a time. |
| STW Skosmos and SPARQL | `https://zbw.eu/stw` | No | The economics thesaurus used in the workshop. |
| EU Vocabularies SPARQL | `https://publications.europa.eu` | No | Includes EuroVoc. |
| LINDAS | `https://lindas.admin.ch` | No | Swiss federal linked data. |
| swisscovery SRU | `https://swisscovery.slsp.ch` | No | Records carry GND identifiers. |
| K10plus SRU | `https://sru.k10plus.de` | No | Union catalogue of the German libraries. |
| Kalliope SRU | `https://kalliope-verbund.info` | No | Union catalogue of manuscripts and archival material. |
| EconBiz | `https://www.econbiz.de` | No | Economics literature search. |
| RVK | `https://rvk.uni-regensburg.de` | No | Regensburg classification. |
| OpenAlex | `https://api.openalex.org` | Optional | Without a key the budget is about 100 searches a day; a free key gives more. |
| Crossref | `https://api.crossref.org` | No | Add a `mailto` parameter to join the polite pool. |
| Open Library | `https://openlibrary.org` | No | Limit yourself to 1 request per second. |

The URLs are service roots. The notebooks and fixtures contain the exact request forms that were tested.

## Etiquette

- **Identify yourself.** Send a User-Agent with the tool name and a contact address, for example `swib26-workshop (you@example.org)`. Some services reject anonymous clients.
- **Set timeouts.** Give every request a timeout, for example 60 seconds for SPARQL, so a slow service cannot hang your notebook.
- **Go slowly.** Send one request at a time to Finto, and respect any stated rate limit.
- **Cache results.** Save responses and reuse them. The notebooks ship recorded fixtures for offline use.
- **Never scrape Dewey.** Its endpoint is gone and its terms are restrictive. See [Data and licences](/v3/resources/data).

{{< callout type="warning" >}}
Part 2 lets a model draft SPARQL, but you read the query and approve it before it runs. Do not point a loop at a public endpoint.
{{< /callout >}}
