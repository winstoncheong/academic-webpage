# Agent notes

## Project
Academic webpage for Winston Cheong. Content is authored in Markdown and published via GitHub Pages.

## Source of truth
Edit Markdown, not generated HTML:
- `index.md`
- `latex.md`
- `lect/*/index.md`
- `recit/*/index.md`

## Build
Regenerate HTML after editing Markdown or `assets/site.css` changes that affect markup structure:

```bash
python scripts/build.py
```

Requirements:
- Python
- Pandoc

The script renders every Markdown source with `templates/page.html` and links `assets/site.css`.

## Design
- Shared CSS: `assets/site.css`
- Shared HTML template: `templates/page.html`
- Prefer editing Markdown content; adjust CSS only for presentation.

## Deploy
GitHub Pages workflow `.github/workflows/static.yml` installs Pandoc and runs `python scripts/build.py` before deployment.

## Notes
- Keep relative paths intact; teaching pages are nested under `lect/` and `recit/`.
- Math is written as `$...$` in Markdown and rendered with MathJax.