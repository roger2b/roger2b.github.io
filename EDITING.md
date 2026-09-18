# Editing and deploying roger2b.github.io

Maintenance notes for the site source (Jekyll + [al-folio](https://github.com/alshedivat/al-folio)).

## Preview locally (macOS, Homebrew Ruby 3.3)

```bash
export PATH="/opt/homebrew/opt/ruby@3.3/bin:/opt/homebrew/lib/ruby/gems/3.3.0/bin:$PATH"
bundle install                      # first time only (gems go to vendor/bundle)
bundle exec jekyll serve --livereload
# open http://127.0.0.1:4000
```

`_config.yml` changes need a server restart.

## Where things live

| What | File |
|---|---|
| Site settings, name, feature flags | `_config.yml` |
| Home page text | `_pages/about.md` (the four cards live in `_layouts/about.liquid`) |
| Research highlights | `_pages/research.md`; figures in `assets/img/research/` |
| Publications | `_bibliography/papers.bib` and `_data/citation_summary.yml` — **generated**, never hand-edit; see below |
| In the Media (home page) | `_data/media.yml` |
| Code list | `_pages/code.md` |
| CV (HTML only, no PDF) | `_data/cv.yml` (rendered by `_pages/cv.md`) |
| Social icons | `_data/socials.yml`; venue badges: `_data/venues.yml` |
| Theme colour | `$purple-color` in `_sass/_variables.scss` |
| Photo | `assets/img/prof_pic.jpg` (square, ~800 px); favicon `assets/img/favicon.png` |

## Common edits

- **Home page "Recent publications"**: shows the five newest entries automatically (`_includes/selected_papers.liquid`). To show a hand-picked set instead, change it to `{% bibliography --group_by none --query @*[selected=true]* %}` and edit the `selected:` list in `scripts/pubs_config.yaml`.
- **Hide a paper or fix a title / author spelling**: `exclude:`, `title_overrides:` or `author_name_fixes:` in `scripts/pubs_config.yaml`, then regenerate.
- **Swap a research figure**: replace the PNG in `assets/img/research/` and, if needed, the `alt` text in `_pages/research.md`.

## Regenerate the publication list

```bash
python3 scripts/generate_pubs.py --config scripts/pubs_config.yaml                      # live from INSPIRE-HEP
python3 scripts/generate_pubs.py --config scripts/pubs_config.yaml \
    --offline-bib ../input/inspire_papers.bib --offline-json ../input/inspire_papers.json   # from saved exports
```

Needs Python 3 with PyYAML (`pip install -r requirements.txt`). The GitHub Actions workflow (`.github/workflows/deploy.yml`) runs the same
script on every push and every Monday, commits a changed `papers.bib` back to `main`, builds the site and deploys it to the `gh-pages` branch.
If the publication list looks stale, check *Actions → Deploy site* on GitHub (GitHub pauses scheduled workflows in repositories with no activity for 60 days; re-enable it there).

## Hard rules

- No CV PDF is published anywhere; the CV page says "available upon request".
- No "FAQ about my name" section.
- `baseurl` stays empty: the site is served at the domain root (`https://roger2b.github.io`).
- `Gemfile.lock` is committed on purpose. If the first Actions run fails at "Set up Ruby", regenerate it with Bundler 2.x
  (`gem install bundler -v 2.6.9 && bundle _2.6.9_ lock --update`).
