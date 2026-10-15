# Scripts

`check_site.py` builds the site with `hugo --gc --minify`, fails on any build warning or error, checks that every internal link and asset under `/v3/` in the built output resolves, and scans `content/v3` for banned phrases (outdated versions, wrong model facts, retired datasets and similar). Run `python3 scripts/check_site.py` and make sure it exits 0 before every commit of content. Use `--no-build` to skip the Hugo build and `--build-dir DIR` to change the output directory (default `/tmp/v3-build`).

External links (GitHub, Hugging Face, ollama.com and so on), in-page anchors and pages outside `/v3/` are not checked by `check_site.py`. Before the content freeze, run a manual pass, for example `grep -rhoE 'https?://[^ )"<>]+' content/v3 | sort -u | while read u; do curl -sIL -o /dev/null -w "%{http_code} $u\n" "$u"; done`.

To preview locally, run `hugo server` from the repository root and open the URL it prints (normally http://localhost:1313/). Pages reload as you edit; run the check script before committing, since the dev server does not fail on warnings.
