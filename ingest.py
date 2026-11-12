"""
ingest.py — Piece 1 of the "Chat with the Olostep docs" RAG demo.

Goal: pull Olostep's own documentation into clean, local Markdown files that
the next pieces will chunk, embed, and answer questions over.

Pipeline in this file:
  1. DISCOVER  which doc pages exist  (read Olostep's published llms.txt index)
  2. FETCH     each page as clean Markdown via the Olostep Scrape API
  3. SAVE      each page to data/pages/*.md + a data/index.json manifest

Run:
  pip install -r requirements.txt
  cp .env.example .env        # then paste your OLOSTEP_API_KEY into .env
  python ingest.py
"""

import os
import re
import json
import time
import pathlib
import requests
from dotenv import load_dotenv

load_dotenv()

OLOSTEP_API_KEY = os.environ["OLOSTEP_API_KEY"]
OLOSTEP_SCRAPE_URL = "https://api.olostep.com/v1/scrapes"

# Olostep publishes an AI-friendly index of its docs at this URL.
DOCS_INDEX_URL = "https://docs.olostep.com/llms.txt"

MAX_PAGES = 35                      # keep well inside the free plan
OUT_DIR = pathlib.Path("data/pages")
MANIFEST = pathlib.Path("data/index.json")


def discover_doc_urls(limit=MAX_PAGES):
    """Read Olostep's llms.txt index and pull out the documentation page URLs."""
    resp = requests.get(DOCS_INDEX_URL, timeout=30)
    resp.raise_for_status()

    # llms.txt is plain text/markdown; doc links look like https://docs.olostep.com/...
    urls = re.findall(r"https://docs\.olostep\.com/[^\s)]+", resp.text)

    # dedupe, treat "page" and "page.md" as one, drop the index itself, keep order
    seen, cleaned = set(), []
    for u in urls:
        u = u.rstrip(".,").removesuffix(".md")
        if u in seen or u.endswith("llms.txt"):
            continue
        seen.add(u)
        cleaned.append(u)

    return cleaned[:limit]


def scrape_markdown(url, retries=2):
    """Fetch one page as clean Markdown via the Olostep Scrape API."""
    headers = {
        "Authorization": f"Bearer {OLOSTEP_API_KEY}",
        "Content-Type": "application/json",
    }
    body = {
        "url_to_scrape": url,
        "formats": ["markdown"],
        "wait_before_scraping": 0,
    }

    for attempt in range(retries + 1):
        r = requests.post(OLOSTEP_SCRAPE_URL, json=body, headers=headers, timeout=120)

        if r.status_code == 200:
            result = r.json().get("result", {})
            md = result.get("markdown_content")
            title = (result.get("page_metadata") or {}).get("title") or url
            return md, title

        # 504 scrape_poll_timeout is documented as safe to retry
        if r.status_code == 504 and attempt < retries:
            time.sleep(2)
            continue

        # anything else: surface Olostep's error envelope and skip this page
        try:
            err = r.json().get("error", {})
            print(f"  x {url} -> {err.get('code')}: {err.get('message')}")
        except Exception:
            print(f"  x {url} -> HTTP {r.status_code}")
        return None, None

    return None, None


def slugify(url):
    tail = url.split("docs.olostep.com/")[-1].lower()
    return re.sub(r"[^a-z0-9]+", "-", tail).strip("-") or "index"


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    urls = discover_doc_urls()
    print(f"Discovered {len(urls)} doc pages. Scraping (max {MAX_PAGES})...\n")

    manifest = []
    for i, url in enumerate(urls, 1):
        md, title = scrape_markdown(url)
        if not md:
            continue
        slug = slugify(url)
        path = OUT_DIR / f"{slug}.md"
        # keep the source URL at the top so later pieces can cite it
        path.write_text(f"<!-- source: {url} -->\n# {title}\n\n{md}", encoding="utf-8")
        manifest.append({"slug": slug, "url": url, "title": title, "file": str(path)})
        print(f"  ok [{i}/{len(urls)}] {title[:60]}")
        time.sleep(0.5)   # be polite; don't hammer the API

    MANIFEST.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"\nDone. Saved {len(manifest)} pages -> {OUT_DIR}/  (manifest: {MANIFEST})")


if __name__ == "__main__":
    main()