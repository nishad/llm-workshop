#!/usr/bin/env python3
"""Build the site, check internal links under /v3/, scan content/v3 for banned phrases.

Usage: python3 scripts/check_site.py [--build-dir DIR] [--no-build]
Exit status 1 on any warning, broken link or banned phrase.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content" / "v3"

BANNED = [
    (r"Python 3\.8", "Python 3.8 (3.12+ required)"),
    (r"Python 3\.11", "Python 3.11"),
    (r"128K\b|128,000 tokens", "Llama-era context claim"),
    (r"--ctx-size|--temperature", "nonexistent ollama run flags"),
    (r"Airplane mode", "removed Ollama setting; it is the Cloud switch now"),
    (r"[Nn]omic.{0,60}1,024 dimensions|1,024 dimensions.{0,60}[Nn]omic", "wrong nomic dimension; nomic-embed-text is 768"),
    (r"seconds per word", "inverted speed unit"),
    (r"GDPR/HIPAA", "compliance overclaim"),
    (r"[Ll]lama ?3\.2", "2025 model reference"),
    (r"[Mm]ade with [Cc]reative [Cc]ommons", "retired dataset"),
    (r"ollama\.ai", "old domain"),
    (r"[Nn]etlify", "wrong host"),
    (r"search for apertus\b", "picker needs the full tag name"),
    (r"\b[Oo]pen [Ss]ource\b.{0,20}\b[Ll]lama\b|\b[Ll]lama\b.{0,20}\b[Oo]pen [Ss]ource\b", "Llama is open weights, not open source"),
]
FILE_BANNED = {"parameters-and-quantization.md": [(r"not recommended", "2025 quantization table wording")]}


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag in ("a", "img", "link", "script"):
            for k, v in attrs:
                if k in ("href", "src") and v:
                    self.hrefs.append(v)


def check_links(build_dir: Path) -> list[str]:
    problems = []
    for page in (build_dir / "v3").rglob("*.html"):
        parser = Links()
        parser.feed(page.read_text(encoding="utf-8", errors="replace"))
        for href in parser.hrefs:
            if href.startswith(("http://", "https://", "mailto:", "#", "data:")):
                continue
            target = href.split("#")[0].split("?")[0]
            if not target:
                continue
            path = re.sub(r"^https?://llm-workshop\.thalhath\.org", "", target)
            local = (build_dir / path.lstrip("/")) if path.startswith("/") else (page.parent / path)
            if local.is_dir():
                local = local / "index.html"
            if not local.exists():
                problems.append(f"{page.relative_to(build_dir)}: broken link {href}")
    return problems


def check_phrases() -> list[str]:
    problems = []
    for md in CONTENT.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        rules = BANNED + FILE_BANNED.get(md.name, [])
        for pattern, why in rules:
            for m in re.finditer(pattern, text):
                line = text.count("\n", 0, m.start()) + 1
                problems.append(f"{md.relative_to(ROOT)}:{line}: '{m.group(0)}' ({why})")
    return problems


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--build-dir", default="/tmp/v3-build")
    ap.add_argument("--no-build", action="store_true")
    args = ap.parse_args()
    build_dir = Path(args.build_dir)
    problems: list[str] = []
    if not args.no_build:
        run = subprocess.run(["hugo", "--gc", "--minify", "-d", str(build_dir)], capture_output=True, text=True, cwd=ROOT)
        warnings = [l for l in (run.stdout + run.stderr).splitlines() if "WARN" in l or "ERROR" in l]
        problems += [f"build: {w}" for w in warnings]
        if run.returncode != 0:
            problems.append(f"build failed with status {run.returncode}")
    if CONTENT.exists():
        problems += check_phrases()
    if (build_dir / "v3").exists():
        problems += check_links(build_dir)
    for p in problems:
        print(p)
    print(f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
