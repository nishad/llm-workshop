# Scripts

`check_site.py` builds the site with `hugo --gc --minify`, fails on any build warning or error, checks that every internal link and asset under `/v3/` in the built output resolves, and scans `content/v3` for banned phrases (outdated versions, wrong model facts, retired datasets and similar). Run `python3 scripts/check_site.py` and make sure it exits 0 before every commit of content. Use `--no-build` to skip the Hugo build and `--build-dir DIR` to change the output directory (default `/tmp/v3-build`).

To preview locally, run `hugo server` from the repository root and open the URL it prints (normally http://localhost:1313/). Pages reload as you edit; run the check script before committing, since the dev server does not fail on warnings.
