---
title: Library endpoints
weight: 3
---

Library and linked-data services you can call from the tool loop, where the model asks for a lookup and your program runs it. Most need no key (an access code that some services require before they answer). We tested the rows marked "October 2026" live from Python in that month. We used the URL shown and a descriptive User-Agent (a header that says who is calling). Rows marked "not checked" link to the service's documentation instead. Services change, so test a service before you depend on it.

## Services

| Service | URL | Key needed | Checked | Notes |
|---|---|---|---|---|
| Wikidata SPARQL | `https://query.wikidata.org/sparql` | No | October 2026 | A descriptive User-Agent is required; generic Python agents get 403. Queries stop after 60 s. The label service (`SERVICE wikibase:label`) is slow on large result sets and not every mirror supports it; fetch labels with `rdfs:label` and a language filter where you can. QLever announced v2 endpoints for the community for November 2026. |
| QLever (Wikidata fallback) | `https://qlever.dev/api/wikidata` | No | October 2026 | A working fallback for Wikidata queries. |
| lobid-gnd | `https://lobid.org/gnd/search` | No | October 2026 | Use `format=json:suggest` for lookups. |
| lobid-gnd reconciliation | `https://lobid.org/gnd/reconcile` | No | October 2026 | OpenRefine reconciliation API. |
| lobid-resources | documentation: https://lobid.org/resources/api | No | not checked | Bibliographic records from the German library networks. |
| DNB SRU | `https://services.dnb.de/sru/dnb` | No | October 2026 | Also `/sru/authorities` for the GND. Up to 100 records per request. |
| DNB Linked Data Service | documentation: https://data.dnb.de/opendata/ | No | not checked | Open data of the German National Library. |
| culturegraph Entity Facts | `https://hub.culturegraph.org/entityfacts/118540238` | No | October 2026 | Replace the number with a GND identifier. CC0. |
| id.loc.gov suggest2 | `https://id.loc.gov/authorities/subjects/suggest2` | No | October 2026 | Pass the search text as `q`. A label service also exists. |
| VIAF | `https://viaf.org/viaf/AutoSuggest` | No | October 2026 | Send `Accept: application/json`, otherwise an HTML page comes back. Bulk files have been frozen since 2024. |
| Getty vocabularies SPARQL | `https://vocab.getty.edu/sparql.json` | No | October 2026 | Bulk downloads returned errors in 2026, and a platform change was announced for autumn 2026. |
| data.bnf.fr | `https://data.bnf.fr/sparql` | No | October 2026 | SPARQL access to the French National Library's data. |
| Europeana SPARQL | `https://api.europeana.eu/sparql` | No | October 2026 | The Search API needs a free key. |
| Finto REST | `https://api.finto.fi/rest/v1/vocabularies` | No | October 2026 | 52 vocabularies. Send one request at a time. |
| STW SPARQL | `https://zbw.eu/beta/sparql/stw/query` | No | October 2026 | The economics thesaurus used in the workshop. |
| STW Skosmos | `https://zbw.eu/beta/skosmos/rest/v1/stw/search` | No | October 2026 | Skosmos search for the same thesaurus. |
| EU Vocabularies SPARQL | `https://publications.europa.eu/webapi/rdf/sparql` | No | October 2026 | Includes EuroVoc. |
| LINDAS | `https://lindas.admin.ch/query` | No | October 2026 | Swiss federal linked data. |
| swisscovery SRU | `https://swisscovery.slsp.ch/view/sru/41SLSP_NETWORK` | No | October 2026 | MARC records carry GND identifiers. |
| K10plus SRU | `https://sru.k10plus.de/opac-de-627` | No | October 2026 | Union catalog of the German libraries. |
| Kalliope SRU | `https://kalliope-verbund.info/sru` | No | October 2026 | Version 1.2, MODS records. |
| EconBiz | `https://api.econbiz.de/v1/search` | No | October 2026 | No key and no quota. |
| RVK | `https://rvk.uni-regensburg.de/api/json/node/AN%2073000` | No | October 2026 | Regensburg classification; the example fetches one notation. |
| OpenAlex | `https://api.openalex.org/works` | Optional | October 2026 | Without a key the budget is about 100 searches a day; a free key gives more. |
| Crossref | `https://api.crossref.org/works` | No | October 2026 | Add a `mailto` parameter to join the polite pool, observed at 10 requests per second. |
| Open Library | documentation: https://openlibrary.org/developers/api | No | not checked | 1 request per second anonymous, 3 when identified. |

The exact requests we tested are in the notebooks and in the recorded fixtures (saved responses kept for offline use).

## Etiquette

- **Identify yourself.** Send a User-Agent with the tool name and a contact address, for example `swib26-workshop (you@example.org)`. Some services reject requests that do not say who sent them.
- **Set timeouts.** Give every request a timeout, for example 60 seconds for SPARQL, so a slow service cannot leave your notebook waiting forever.
- **Go slowly.** Send one request at a time to Finto, and respect any rate limit the service states (the number of requests it allows in a given time).
- **Cache results.** Save responses and reuse them. The notebooks include recorded fixtures for offline use.
- **Never scrape Dewey.** Do not use a script to collect Dewey Decimal Classification data from web pages. Its endpoint is gone and its terms are restrictive. See [Data and licenses](/v3/resources/data).

{{< callout type="warning" >}}
Part 2 lets a model draft SPARQL, but you read the query and approve it before it runs. Do not let a loop send queries to a public endpoint without a person approving each one.
{{< /callout >}}
