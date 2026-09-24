"""Weekly SEO refresh for akashicmonk.blog.

- Pulls the Akashic Monk catalog from the public iTunes/Apple Music API
  and rewrites the RELEASES block in website/index.html, so new singles and
  albums appear on the site automatically.
- Updates the release count in the site's structured data description.
- Refreshes <lastmod> dates in website/sitemap.xml when a page changed.
Exits 0 with no changes when nothing new was released.
"""
import datetime
import json
import re
import sys
import urllib.request
from pathlib import Path

ARTIST_ID = 1258188977
ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "website" / "index.html"
SITEMAP = ROOT / "website" / "sitemap.xml"


def fetch_albums():
    url = f"https://itunes.apple.com/lookup?id={ARTIST_ID}&entity=album&limit=200"
    with urllib.request.urlopen(url, timeout=30) as r:
        data = json.load(r)["results"][1:]
    rows = []
    for a in sorted(data, key=lambda r: r["releaseDate"], reverse=True):
        view = a["collectionViewUrl"].split("?")[0]
        rows.append({
            "t": re.sub(r"( - Single)+$", "", a["collectionName"]).replace(" - Single", "").strip(),
            "d": a["releaseDate"][:10],
            "n": a["trackCount"],
            "id": view.rsplit("/", 1)[1],
            "slug": view.rsplit("/", 2)[1],
            "art": a["artworkUrl100"].split("/image/thumb/")[1].rsplit("/", 1)[0],
        })
    return rows


def js_block(rows):
    lines = []
    for r in rows:
        body = json.dumps(r, ensure_ascii=False, separators=(",", ":"))
        body = re.sub(r'"(t|d|n|id|slug|art)":', r"\1:", body)
        lines.append("  " + body)
    return "const RELEASES = [\n" + ",\n".join(lines) + "\n];"


def main():
    rows = fetch_albums()
    if len(rows) < 10:
        print("Catalog lookup returned too few releases; leaving site unchanged.")
        return 0
    html = INDEX.read_text()
    new_block = js_block(rows)
    updated = re.sub(
        r"(// AUTO-RELEASES:START[^\n]*\n)const RELEASES = \[.*?\n\];",
        lambda m: m.group(1) + new_block,
        html,
        flags=re.S,
    )
    updated = re.sub(r"\d+ releases since 2016", f"{len(rows)} releases since 2016", updated)
    if updated == html:
        print(f"No catalog changes ({len(rows)} releases).")
        return 0
    INDEX.write_text(updated)
    today = datetime.date.today().isoformat()
    sm = SITEMAP.read_text()
    sm = re.sub(r"(<loc>https://akashicmonk\.blog/</loc><lastmod>)[^<]+", rf"\g<1>{today}", sm)
    SITEMAP.write_text(sm)
    print(f"Updated catalog: {len(rows)} releases, newest '{rows[0]['t']}' ({rows[0]['d']}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
