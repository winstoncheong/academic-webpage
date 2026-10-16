#!/usr/bin/env python3
"""Render all Markdown sources to styled HTML using Pandoc."""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "templates" / "page.html"
MATHJAX_URL = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"


def find_sources() -> list[Path]:
    sources: list[Path] = []
    for name in ("index.md", "latex.md"):
        p = ROOT / name
        if p.exists():
            sources.append(p)
    sources.extend(sorted((ROOT / "lect").rglob("index.md")))
    sources.extend(sorted((ROOT / "recit").rglob("index.md")))
    return sources


def title_of(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.parent.name or "Winston Cheong"


def root_rel(source: Path) -> str:
    # path from the source's directory to ROOT, as a (possibly empty) URL prefix
    rel = os.path.relpath(ROOT, source.parent)
    if rel == ".":
        return "./"
    return rel.replace(os.sep, "/") + "/"


def css_rel(source: Path) -> str:
    rel = os.path.relpath(ROOT / "assets" / "site.css", source.parent)
    return rel.replace(os.sep, "/")


def convert(source: Path) -> None:
    out = source.with_suffix(".html")
    cmd = [
        "pandoc",
        str(source),
        "-o",
        str(out),
        "--from=gfm",
        "--to=html5",
        "--standalone",
        f"--template={TEMPLATE}",
        "--section-divs",
        f"--css={css_rel(source)}",
        f"--mathjax={MATHJAX_URL}",
        f"--metadata=title:{title_of(source)}",
        f"--metadata=root:{root_rel(source)}",
    ]
    subprocess.run(cmd, check=True)
    print(f"rendered {source.relative_to(ROOT)} -> {out.relative_to(ROOT)}")


def main() -> int:
    sources = find_sources()
    if not sources:
        print("no markdown sources found", file=sys.stderr)
        return 1
    for source in sources:
        convert(source)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
PY