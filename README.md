# Local LLM Workshop website

Source of the website for the "Getting started with local LLMs" workshop at the Semantic Web in Libraries conference (SWIB). It is built with Hugo and the Hextra theme and is live at https://llm-workshop.thalhath.org/.

| Path | Edition |
|---|---|
| `/v1/` | SWIB24 (2024, archive) |
| `/v2/` | SWIB25 (2025, archive) |
| `/v3/` | SWIB26 (16 November 2026, current) |

Author: Nishad Thalhath ([ORCID 0000-0001-9845-9714](https://orcid.org/0000-0001-9845-9714)).

## Build

You need Hugo extended 0.167 or newer.

```bash
hugo server                  # live preview at http://localhost:1313/
python3 scripts/check_site.py   # build and check the site
```

`python3 scripts/check_site.py` must pass (`0 problem(s)`) before every content commit.

## Deployment

The site is deployed on Cloudflare Pages.

- Project: `llm-workshop`
- Production branch: `main`
- Environment variable: `HUGO_VERSION=0.167.0`
- Build command: `if [ "$CF_PAGES_BRANCH" = "main" ]; then hugo --gc --minify; else hugo --gc --minify -b "$CF_PAGES_URL"; fi`
- Every other branch gets a preview deployment.

## Content conventions

Every page has `title` and `weight` in its front matter, and every `_index.md` sets `cascade: {type: docs}`. Landing pages set `toc: false`. Pages live in numbered folders (`01-...`) so the order is visible on disk. Use the `cards` and `card` shortcodes for hub navigation only, and the `callout` shortcode with the types `info`, `warning`, `success` and `error`. Captured command or model output is labelled "captured with <tag>, <date>". Screenshots are taken in light mode and stay under 400 KB. Model facts (names, sizes, tags, licenses) appear only on the three model pages; other pages link to them. Write in American English, in plain sentences. The check script fails on build warnings, checks every internal link and asset under `/v3/`, and scans `content/v3` for banned phrases. It does not check front matter, shortcode usage, external links or in-page anchors; see `scripts/README.md`.

## Adding an edition

1. Create `content/vN/` with an `_index.md` (`cascade: {type: docs}`, `toc: false`).
2. Add the edition's entries to `menu.main` in `hugo.yaml`, and move the previous edition into the Archive dropdown.
3. On the previous edition's `_index.md`, add `excludeSearch: true` to the cascade and an "Archived edition" warning callout that points to the new edition.
4. Update the cards in `content/_index.md`, then run `python3 scripts/check_site.py`.

## Companion notebooks

The notebooks for Part 2 live in https://github.com/nishad/llm-workshop-notebooks.

## Licenses

Code is MIT. Prose and other materials are CC BY 4.0.
