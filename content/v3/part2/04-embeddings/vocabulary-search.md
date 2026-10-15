---
title: Vocabulary search
weight: 2
---

This page follows sections 03.02 to 03.08 of notebook 03. Each code cell is quoted with the output it produced when the notebook was executed on 15 October 2026. The embedding model is `qwen3-embedding:0.6b`; the helper adds its query prefix (see the [concepts page](/v3/part2/04-embeddings/concepts)). Setup creates `EMBED_MODEL`.

The notebook's query tables are HTML; here they are Markdown with the same cells.

## From SKOS to index entries

Each preferred and alternative label becomes one entry that remembers its concept, so a one-word query meets one-word entries. In the October 2026 tests, one long document per concept (label, all alternatives, scope note) put *Fernsehproduktion* below *Produktionsprozess* although the word is in the document; the label index puts it first.

```python
from scripts.build_vocab_extracts import load_vocab, concept_document
stw = load_vocab("data/vocab/stw.json")
unesco = load_vocab("data/vocab/unesco.json")
print(len(stw), "STW descriptors;", len(unesco), "UNESCO concepts")
c = next((x for x in stw if x["pref"].get("de") == "Bibliothek"), stw[0])
print("preferred:", c["pref"]["de"], "| alternatives:", c["alt"].get("de", []))
print("as one document:", concept_document(c, "de"))
```

```text
6198 STW descriptors; 4500 UNESCO concepts
preferred: Bibliothek | alternatives: ['Bibliothekswesen', 'Bücherei']
as one document: Bibliothek (Bibliothekswesen; Bücherei)
```

From the executed notebook 03, 15 October 2026. This is one STW descriptor: the preferred label, its alternatives, and the one-document form. The notebook indexes every label separately instead; `concept_document` is kept for the gold set below.

## Embed the German labels in one batch

About 20,000 short labels. In the executed notebook the index was built in 313 s on an Apple Silicon Mac with 64 GB; a CPU-only laptop takes far longer. With the prebuilt file `runs/stw-de-labels.sqlite` in place (see the [environment page](/v3/part2/01-environment)), the cell loads it instead of building, which is how to follow this notebook live on an 8 GB machine. The helper adds the embedding model's prefix (qwen3-embedding wants an instruction in front of every query and nothing in front of documents) and returns unit vectors.

```python
entries = []   # (entry id, label): every German preferred and alternative label, remembering its concept
for c in stw:
    for n, label in enumerate([c["pref"].get("de")] + c["alt"].get("de", [])):
        if label:
            entries.append((f'{c["id"]}#{n}', label))
pref = {c["id"]: c["pref"].get("de", "") for c in stw}
Path("runs").mkdir(exist_ok=True)
index_path = "runs/stw-de-labels.sqlite"
if Path(index_path).exists():
    index = load_index(index_path); print("loaded", len(index.ids), "label vectors from", index_path)
    if index.model != EMBED_MODEL:
        print(f"warning: index built with {index.model} but the session uses {EMBED_MODEL}; delete the file to rebuild")
else:
    t = time.time(); index = build_index([e for e, _ in entries], [l for _, l in entries], model=EMBED_MODEL); save_index(index, index_path)
    print(f"embedded {len(entries)} labels in {time.time()-t:.0f} s, dimension {index.vectors.shape[1]}, saved to {index_path}")
```

```text
embedded 19688 labels in 313 s, dimension 1024, saved to runs/stw-de-labels.sqlite
```

From the executed notebook 03, 15 October 2026 (the imports are omitted). The warning line prints only if the file was built with a different embedding model than the one in use; here it stayed silent because the cell built the index.

## Four kinds of query

Hits are labels. `search_concepts` keeps the best label per concept and shows the concept's preferred label next to the label that matched.

```python
def search_concepts(query, index, pref, k=3):
    """Search the labels and keep the best label per concept: (concept id, preferred label, matched label, score)."""
    best = {}
    for entry_id, label, score in search(query, index, k=k * 10):
        cid = entry_id.rsplit("#", 1)[0]
        if cid not in best or score > best[cid][1]:
            best[cid] = (label, score)
    ranked = sorted(best.items(), key=lambda kv: -kv[1][1])[:k]
    return [(cid, pref[cid], label, score) for cid, (label, score) in ranked]

show("Geld, das Eltern für Kinder bekommen")
show("wheat production")
show("Fernsehproduktion")
show("Which concept covers the taxation of inheritances?")
```

From the executed notebook 03, 15 October 2026 (the `show` helper is cut here).

**1. Free text that is not a label:** "Geld, das Eltern für Kinder bekommen"

| score | concept | matched label | id |
|:--|:--|:--|:--|
| 0.654 | Elternzeit | Erziehungsgeld | 18911-4 |
| 0.635 | Unterhaltsrecht | Elternunterhalt | 19839-2 |
| 0.625 | Familienleistungsausgleich | Kindergeld | 11564-6 |

The query describes child benefit without naming it. *Kindergeld* is third, under *Familienleistungsausgleich*; a person would pick it.

**2. Cross-lingual:** "wheat production" against the German index

| score | concept | matched label | id |
|:--|:--|:--|:--|
| 0.608 | Weizenanbau | Weizenanbau | 19302-3 |
| 0.580 | Agrarproduktion | Landwirtschaftliche Produktion | 18980-6 |
| 0.545 | Getreideanbau | Getreideanbau | 18198-5 |

**3. A held-out synonym:** "Fernsehproduktion" (the descriptor is *Filmproduktion*)

| score | concept | matched label | id |
|:--|:--|:--|:--|
| 0.761 | Filmproduktion | Fernsehproduktion | 18929-6 |
| 0.618 | Serienfertigung | Serienproduktion | 12727-6 |
| 0.611 | Fernsehprogramm | Fernsehprogramm | 18934-6 |

The alternative label matches itself, and the concept it belongs to comes back.

**4. A scope-note question:** "Which concept covers the taxation of inheritances?"

| score | concept | matched label | id |
|:--|:--|:--|:--|
| 0.581 | Erbschaftsteuer | Erbschaftsteuerrecht | 11651-4 |
| 0.545 | Besteuerungsprinzip | Grundsatz der Besteuerung | 11684-3 |
| 0.537 | Vermögensteuer | Vermögenssteuer | 11682-0 |

## Suggest three, let a person choose

A score is not a decision. Below a threshold we show nothing; above it we show up to three candidates and record the choice. The machine proposes, the cataloger decides.

```python
def suggest(text, k=3, threshold=0.55):
    hits = [h for h in search_concepts(text, index, pref, k) if h[3] >= threshold]
    if not hits:
        print(f"No confident suggestion for: {text!r}"); return None
    for n, (cid, p, label, s) in enumerate(hits, 1):
        print(f"[{n}] {s:.3f}  {p}  (matched: {label})")
    choice = input("Pick 1-3, or 0 for none: ") if os.environ.get("WORKSHOP_AUTO_APPROVE") != "1" else "1"
    return hits[int(choice) - 1][0] if choice in ("1", "2", "3") and int(choice) <= len(hits) else None

print("chosen:", suggest("Streik der Lokführer"))
```

```text
[1] 0.614  Arbeitskampf  (matched: Streik)
[2] 0.572  Bahnberufe  (matched: Eisenbahnarbeiter)
chosen: http://zbw.eu/stw/descriptor/11348-5
```

From the executed notebook 03, 15 October 2026. Only two candidates cleared the threshold, so only two are shown. The notebook was run unattended, so the first was chosen automatically; in the room, you choose.

## The UNESCO Thesaurus in French and German

A second label index from the English labels, queried in French and German. Cross-lingual retrieval is where embedding models differ most. The prebuilt file `runs/unesco-en-labels.sqlite` is the second file in the download post; with it in `runs/`, the notebook loads the index instead of building it.

```python
for q in ("Grossesse", "bibliothèque numérique", "Rechte der Frau", "changement climatique"):
    print(q, "→", [(p, round(s, 3)) for _, p, _, s in search_concepts(q, u_index, u_pref)])
```

```text
Grossesse → [('Gross national product', 0.426), ('Overpopulation', 0.423), ('Grade repetition', 0.408)]
bibliothèque numérique → [('Library automation', 0.703), ('Digital libraries', 0.675), ('Information/library networks', 0.673)]
Rechte der Frau → [('Womens rights', 0.609), ('Womens status', 0.567), ('Civil and political rights', 0.555)]
changement climatique → [('Environmental degradation', 0.666), ('Climate change', 0.661), ('Climate change adaptation', 0.641)]
```

From the executed notebook 03, 15 October 2026. Three of the four work. "Grossesse" (pregnancy) misses: the model matched the look of the word ("Gross national product", "Grade repetition"), not its meaning. All three scores are below 0.45, which a threshold would have caught. Even for the good queries, the right concept is not always first: for "changement climatique", *Climate change* is second.

## Measure, don't guess: recall on the gold set

Fifty queries with known targets (held-out German synonyms, STW English to German, UNESCO French and English, scope-note questions), scored against one document per concept with the synonym removed. This is the hard case, and it is the same corpus for every model. recall@1 is the share of queries whose correct concept is the top hit; recall@5 is the share found in the top five. This cell embeds 15,198 documents and takes about six minutes; it is optional.

```text
qwen3-embedding:0.6b: recall@1 0.62, recall@5 0.82
  A_stw_de_alt_to_concept          recall@1 5/12  recall@5 9/12
  B_stw_en_to_de                   recall@1 8/12  recall@5 10/12
  C_unesco_fr_to_en                recall@1 6/10  recall@5 8/10
  D_unesco_en_to_fr                recall@1 10/10  recall@5 10/10
  E_unesco_scopenote_to_concept    recall@1 2/6  recall@5 4/6
```

From the executed notebook 03, 15 October 2026.

| Kind | Query type | recall@1 | recall@5 |
|:--|:--|:--|:--|
| A | STW German synonym to concept | 5/12 | 9/12 |
| B | STW English to German | 8/12 | 10/12 |
| C | UNESCO French to English | 6/10 | 8/10 |
| D | UNESCO English to French | 10/10 | 10/10 |
| E | UNESCO scope-note question to concept | 2/6 | 4/6 |
| All | 50 queries | 0.62 | 0.82 |

Last year's English-only model scored 0.17 on kind B (English to German). The alternatives measured on the same gold set are on the [models page](/v3/resources/models); the headline is that `embeddinggemma` scored higher under a license that is not open source, and `bge-m3` scored lower.

### The same queries against the label index

The same held-out queries against the label index, with the query's own label removed first. This keeps the model constant and changes only the index design.

```text
label index  A_stw_de_alt_to_concept          recall@1 8/12  recall@5 11/12
label index  B_stw_en_to_de                   recall@1 6/12  recall@5 10/12
```

From the executed notebook 03, 15 October 2026.

| Kind | One document per concept | Label index |
|:--|:--|:--|
| A, recall@1 | 5/12 | 8/12 |
| A, recall@5 | 9/12 | 11/12 |
| B, recall@1 | 8/12 | 6/12 |
| B, recall@5 | 10/12 | 10/12 |

The label index helps the synonym kind most and does not help the cross-lingual kind at rank 1: one-word labels carry less context for a translation than a document does. Index design changed recall as much as the model did.

## sqlite-vec

The index lives in one SQLite file. Any program that can open SQLite can query it, and the vector search is a SQL clause.

```python
from workshop.search import knn_sqlite
q = embed(["Inflation"], "query", model=EMBED_MODEL)[0]
for i, t, d in knn_sqlite(index_path, q, k=3):
    print(f"distance {d:.3f}  {t[:80]}")
```

```text
distance 0.689  Inflation
distance 0.785  Anspruchsinflation
distance 0.796  Inflationstheorie
```

From the executed notebook 03, 15 October 2026. Here a smaller distance is better.

## Three tiers

### GUI

This notebook has no chat-app equivalent. Read the four tables above and decide for each query which hit a cataloger would accept.

### Run and change

Lower the threshold in the suggest cell to 0.4 and query something outside economics, such as "Mondlandung". What does the model suggest, and would a cataloger accept it? Then query the German index in Italian or Spanish. Which kinds of terms survive translation, and which do not?

### Stretch

Swap the embedding model: set `WORKSHOP_EMBED_MODEL=embeddinggemma` (pull it first; it is under Google's Gemma Terms of Use, not an open-source license), delete or rename the two index files in `runs/` first (they hold qwen3-embedding vectors), restart the kernel and run from the setup cell to the gold-set cell. Note the prefixes the helper adds for each model (`workshop.embed.prefix_for`). Or build an index over a GND subject-heading subset (the DNB publishes GND dumps under CC0 at https://data.dnb.de/opendata/) and query it with STW labels, a first step towards vocabulary mapping.

## Data and licenses

STW Thesaurus for Economics: CC BY 4.0. UNESCO Thesaurus: CC BY-SA 3.0 IGO. See the [data page](/v3/resources/data) for sources and dates, and the [models page](/v3/resources/models) for the embedding models and their licenses. The next chapter uses an index like this one: [RAG](/v3/part2/05-rag).

## Check yourself

- [ ] I can turn a list of labels into an index and query it.
- [ ] I know which kinds of query find the right concept and which do not.
- [ ] I can read recall@1 and recall@5 and say what they measure.
- [ ] I treat the suggestions as candidates for a person to choose from.

{{< callout type="success" >}}
**What you should see:** ranked suggestions for German, English and French queries, the gold-set line `qwen3-embedding:0.6b: recall@1 0.62, recall@5 0.82` if you ran the optional cell, and two `.sqlite` files in `runs/`.
{{< /callout >}}