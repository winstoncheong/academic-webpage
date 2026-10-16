# Academic webpage

Source content lives in Markdown (`index.md`, `latex.md`, `lect/.../index.md`, `recit/.../index.md`).
The published HTML is generated from those sources so the design stays consistent.

## Build

```bash
python scripts/build.py
```

This uses [Pandoc](https://pandoc.org/) and `templates/page.html` to render every Markdown file with
`assets/site.css`. The design supports light/dark themes and small screens.

## Agent workflow

See `AGENTS.md` for agent-specific guidance. The short version: edit the Markdown sources, then run `python scripts/build.py`.

## Deploy

GitHub Pages deployment runs the same build in `.github/workflows/static.yml`
before uploading the site.