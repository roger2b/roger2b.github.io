#!/usr/bin/env python3
"""Regenerate _bibliography/papers.bib from INSPIRE-HEP for the author in pubs_config.yaml.

Usage:
  python3 scripts/generate_pubs.py --config scripts/pubs_config.yaml                 # live fetch
  python3 scripts/generate_pubs.py --config scripts/pubs_config.yaml \
      --offline-bib ../input/inspire_papers.bib --offline-json ../input/inspire_papers.json   # no network

Post-processing (all verified to render correctly with al-folio / jekyll-scholar):
  * {\\ensuremath{\\alpha}} -> α, Ly{\\,}α -> Lyα, {\\textquoteright} -> ’
  * "de Belsunce, X" -> "{de Belsunce}, X"  (keeps the particle, enables self-highlighting)
  * "… and others" + collaboration = "DESI" -> "… and DESI Collaboration"
  * other "… and others" entries -> full author list from the INSPIRE JSON (optional)
  * arxiv = {eprint}, abbr = {venue badge}, inspirehep_id + citations (for the INSPIRE badge, no API calls at build time),
    selected/bibtex_show flags, excluded texkeys dropped; $w_0w_a$-style math -> Unicode subscripts; author-name fixes from the config
Only the standard library is required (plus PyYAML).
"""
import argparse, json, re, sys, urllib.parse, urllib.request
import yaml

API = "https://inspirehep.net/api/literature"
JSON_FIELDS = "texkeys,authors.full_name,collaborations,citation_count,control_number,document_type"

def fetch(url):
    for attempt in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "rbelsunce.github.io pubs script"}), timeout=60) as r:
                return r.read().decode("utf-8")
        except Exception as e:  # noqa: BLE001
            print(f"  attempt {attempt+1} failed: {e}", file=sys.stderr)
    raise SystemExit("INSPIRE fetch failed")

def load_sources(cfg, args):
    q = urllib.parse.quote(f"a {cfg['author_query']}")
    if args.offline_bib:
        bib = open(args.offline_bib, encoding="utf-8").read()
    else:
        bib = fetch(f"{API}?q={q}&size=250&sort=mostrecent&format=bibtex")
    if args.offline_json:
        js = json.load(open(args.offline_json, encoding="utf-8"))
    else:
        js = json.loads(fetch(f"{API}?q={q}&size=250&sort=mostrecent&fields={JSON_FIELDS}"))
    return bib, js

def index_json(js):
    by_key = {}
    for hit in js.get("hits", {}).get("hits", []):
        m = hit["metadata"]
        for k in m.get("texkeys", []):
            by_key[k] = m
    return by_key

def fix_name(name, last):
    # "de Belsunce, Roger" -> "{de Belsunce}, Roger"
    return re.sub(r"(?<![{\w])" + re.escape(last) + r",", "{" + last + "},", name)

SUBSCRIPTS = str.maketrans("0123456789aehijklmnoprstuvx", "₀₁₂₃₄₅₆₇₈₉ₐₑₕᵢⱼₖₗₘₙₒₚᵣₛₜᵤᵥₓ")

def clean_title(t):
    t = t.replace(r"{\ensuremath{\alpha}}", "α").replace(r"Ly{\,}α", "Lyα").replace(r"{\textquoteright}", "’")
    t = re.sub(r"\\ensuremath\{\\alpha\}", "α", t)
    # $w_0w_a$ -> w₀wₐ ; $bc$ -> bc  (simple inline math made of letters with optional single-char subscripts)
    def _math(m):
        inner = m.group(1)
        if re.fullmatch(r"(?:[A-Za-z]_\{?[0-9a-z]\}?|[A-Za-z])+", inner):
            return re.sub(r"([A-Za-z])_\{?([0-9a-z])\}?", lambda k: k.group(1) + k.group(2).translate(SUBSCRIPTS), inner)
        return m.group(0)
    t = re.sub(r"\$([^$]+)\$", _math, t)
    return t

def fix_author_names(author, fixes):
    for bad, good in (fixes or {}).items():
        author = author.replace(bad, good)
    return author

def _find_field(entry, name):
    """Locate `name = "value"` or `name = {value}` (nested braces allowed).
    Returns (value_start, value_end, inner_value) or None; value_start/end span the delimiters."""
    m = re.search(r'^\s*' + name + r'\s*=\s*', entry, re.M)
    if not m:
        return None
    i = m.end()
    if i >= len(entry):
        return None
    if entry[i] == '"':
        j = i + 1
        while j < len(entry):
            if entry[j] == '\\':
                j += 2
                continue
            if entry[j] == '"':
                return (i, j + 1, entry[i + 1 : j])
            j += 1
        return None
    if entry[i] == '{':
        depth, j = 0, i
        while j < len(entry):
            if entry[j] == '{':
                depth += 1
            elif entry[j] == '}':
                depth -= 1
                if depth == 0:
                    return (i, j + 1, entry[i + 1 : j])
            j += 1
    return None

def get_field(entry, name):
    r = _find_field(entry, name)
    return r[2] if r else None

def replace_field(entry, name, value):
    r = _find_field(entry, name)
    if not r:
        return entry
    return entry[: r[0]] + '"' + value + '"' + entry[r[1] :]

def set_field(entry, name, value):
    """Insert `name = {value}` after the first line of the entry (jekyll-scholar accepts braces)."""
    first_nl = entry.index("\n")
    return entry[: first_nl + 1] + f"    {name} = {{{value}}},\n" + entry[first_nl + 1 :]

def process(bib, js, cfg):
    by_key = index_json(js)
    last = cfg["self"]["last"]
    out = []
    kept = excluded = 0
    for entry in re.split(r"\n(?=@)", bib.strip()):
        if not entry.strip():
            continue
        m = re.match(r"@(\w+)\{([^,]+),", entry)
        if not m:
            continue
        etype, key = m.group(1).lower(), m.group(2).strip()
        if key in cfg.get("exclude", []) or etype in ("phdthesis", "mastersthesis"):
            excluded += 1
            continue
        meta = by_key.get(key, {})
        # --- authors ---
        author = get_field(entry, "author") or ""
        coll = get_field(entry, "collaboration")
        new_author = author
        if author.endswith(" and others"):
            if coll:
                new_author = author[: -len(" and others")] + f" and {coll} Collaboration"
            elif cfg.get("expand_author_lists") and meta.get("authors") and len(meta["authors"]) <= cfg.get("max_expanded_authors", 80):
                new_author = " and ".join(a["full_name"] for a in meta["authors"])
        new_author = fix_name(fix_author_names(new_author, cfg.get("author_name_fixes")), last)
        entry = replace_field(entry, "author", new_author)
        # --- title ---
        title = get_field(entry, "title")
        if title is not None:
            new_title = cfg.get("title_overrides", {}).get(key) or clean_title(title)
            if key in cfg.get("title_overrides", {}):
                new_title = "{" + new_title.strip("{}") + "}"
            entry = replace_field(entry, "title", new_title)
        # --- extra fields ---
        eprint = get_field(entry, "eprint")
        if eprint and get_field(entry, "arxiv") is None:
            entry = set_field(entry, "arxiv", eprint)
        journal = get_field(entry, "journal")
        abbr = cfg.get("journal_abbr", {}).get(journal) if journal else None
        if abbr and "abbr =" not in entry:
            entry = set_field(entry, "abbr", abbr)
        if meta.get("control_number") and "inspirehep_id =" not in entry:
            entry = set_field(entry, "inspirehep_id", str(meta["control_number"]))
        if "citation_count" in meta and "citations =" not in entry:
            entry = set_field(entry, "citations", str(meta.get("citation_count", 0)))
        if cfg.get("bib_button_on_all", True) and "bibtex_show =" not in entry:
            entry = set_field(entry, "bibtex_show", "true")
        if key in cfg.get("selected", []) and "selected =" not in entry:
            entry = set_field(entry, "selected", "true")
        out.append(entry.rstrip() + "\n")
        kept += 1
    print(f"  kept {kept} entries, excluded {excluded}")
    return "---\n---\n\n" + "\n".join(out)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--offline-bib"); ap.add_argument("--offline-json")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    cfg = yaml.safe_load(open(args.config, encoding="utf-8"))
    import os
    out = args.out or os.path.join(os.path.dirname(os.path.abspath(args.config)), "..", "_bibliography", "papers.bib")
    print("Loading INSPIRE records" + (" (offline)" if args.offline_bib else ""))
    bib, js = load_sources(cfg, args)
    result = process(bib, js, cfg)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(result)
    print(f"  wrote {os.path.normpath(out)}")

if __name__ == "__main__":
    main()
