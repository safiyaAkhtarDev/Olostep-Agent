"""
embed.py — Piece 2 of the "Chat with the Olostep docs" RAG demo.

Turns the clean Markdown pages from Piece 1 into a searchable index of
vectors, so later we can FIND the passages that match a question by meaning.

Uses Gemini for embeddings — the same key you'll use to WRITE answers in
Piece 3 — so the whole demo runs on just two keys: Olostep + Gemini.

Pipeline:
  1. LOAD   data/index.json (manifest) + each scraped .md file
  2. CHUNK  split each page into ~1000-char passages
  3. EMBED  turn each chunk into a vector via Gemini
  4. SAVE   data/chunks.json = [{text, url, title, embedding}]

Run (after ingest.py):
  python embed.py
"""

import os
import json
import time
import pathlib
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

EMBED_MODEL = "models/gemini-embedding-001"
MANIFEST = pathlib.Path("data/index.json")
CHUNKS_OUT = pathlib.Path("data/chunks.json")

CHUNK_SIZE = 1000                   # target characters per chunk
CHUNK_OVERLAP = 150                 # characters carried between chunks


def read_pages():
    """Load the manifest and return [{url, title, text}] for each scraped page."""
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    pages = []
    for item in manifest:
        body = pathlib.Path(item["file"]).read_text(encoding="utf-8")
        pages.append({"url": item["url"], "title": item["title"], "text": body})
    return pages


def chunk_text(text, size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    """Split one page into ~`size`-char chunks, breaking on blank lines."""
    paras = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks, cur = [], ""
    for p in paras:
        if cur and len(cur) + len(p) + 2 > size:
            chunks.append(cur)
            cur = cur[-overlap:]            # carry a tail so context isn't lost at the seam
        cur = (cur + "\n\n" + p).strip()
    if cur:
        chunks.append(cur)
    return chunks


def embed_text(text, retries=3):
    """Turn one chunk into a vector via Gemini, retrying on transient errors."""
    for attempt in range(retries):
        try:
            r = genai.embed_content(model=EMBED_MODEL, content=text)
            return r["embedding"]
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(2 * (attempt + 1))   # back off, then retry
                continue
            raise
    return None


def main():
    pages = read_pages()

    # 1. chunk every page, keeping each chunk's source url + title alongside it
    records = []
    for page in pages:
        for chunk in chunk_text(page["text"]):
            records.append({"text": chunk, "url": page["url"], "title": page["title"]})
    print(f"{len(pages)} pages -> {len(records)} chunks. Embedding with Gemini...")

    # 2. embed each chunk (small sleep keeps us under the free-tier rate limit)
    for i, rec in enumerate(records, 1):
        rec["embedding"] = embed_text(rec["text"])
        if i % 20 == 0 or i == len(records):
            print(f"  embedded {i}/{len(records)}")
        time.sleep(0.3)

    # 3. save everything (text + metadata + vector) for the query step
    CHUNKS_OUT.write_text(json.dumps(records), encoding="utf-8")
    print(f"\nDone. Saved {len(records)} embedded chunks -> {CHUNKS_OUT}")


if __name__ == "__main__":
    main()