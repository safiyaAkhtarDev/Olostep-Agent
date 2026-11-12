# Chat with the Olostep Docs

A tiny Retrieval-Augmented Generation (RAG) app that turns a website's documentation into a question-answering bot that **cites its sources** — powered by [Olostep](https://www.olostep.com) for clean, LLM-ready web data.

Ask it *"How do I scrape a page as Markdown?"* and it answers in plain English, with links to the exact doc pages it used.

## Why this exists

Large language models can browse the web, but you can't wire a chat window into your product, point it at 10,000 pages, and trust the structure that comes back. That's the gap Olostep fills: the reliable layer that turns messy live web pages into clean Markdown an AI can actually use.

This demo shows how little code it takes to go from *a URL* to *a grounded, cited answer* when the ingestion is handled for you.

## How it works

Three small steps:

```
ingest.py  ->  Olostep scrapes the docs into clean Markdown   ->  data/pages/*.md
embed.py   ->  split into chunks + turn each into a vector     ->  data/chunks.json
ask.py     ->  find the closest chunks + answer with citations ->  your terminal
```

- **Retrieve** finds the passages that match your question *by meaning* (embeddings + cosine similarity).
- **Generate** writes the answer using *only* those passages, and cites their URLs — so it can't make things up.

## Use cases

**1. Turn your own site into a support bot — for free.**
Point `ingest.py` at your own website or docs and you have a cited Q&A bot in three commands. It runs entirely on free tiers — no paid OpenAI token. If you can scrape it, you can chat with it.

**2. Scale it: one bot over thousands of pages, across many sites.**
The same pipeline scales with Olostep's **Batch** endpoint — submit up to 100,000 URLs in a single request. Embed a whole knowledge base (every doc site, blog, and help center you care about) and the bot answers across all of them at once. Batching 10k+ pages across sites without breaking is exactly the job a hand-rolled scraper can't do reliably — and exactly what Olostep is for.

## Quickstart

```bash
# 1. install
python -m pip install -r requirements.txt

# 2. add your keys
cp .env.example .env     # then paste OLOSTEP_API_KEY and GEMINI_API_KEY

# 3. run the pipeline
python ingest.py         # scrape the docs into clean Markdown
python embed.py          # build the vector index
python ask.py            # chat with the docs
```

Two free keys needed: [Olostep](https://www.olostep.com) (scraping) and [Google Gemini](https://aistudio.google.com) (embeddings + answers).

## Design choices

- **Olostep for ingestion** — clean Markdown out of the box is 80% of whether a RAG bot works. No HTML-stripping, no proxy or anti-bot code to maintain.
- **Discovery via `llms.txt`** — Olostep publishes an AI-readable index of its docs, so there is nothing to crawl. For sites without one, swap in Olostep's **Map** endpoint (a one-function change).
- **Citations by design** — every chunk carries its source URL from ingestion through to the answer. A docs bot you cannot verify is a docs bot you cannot trust.
- **Gemini free tier** — embeddings and generation run on one free key, so the whole thing is reproducible by anyone who clones it.

## Honest limitations

- **Chunking is simple** — paragraph-based, ~1000 chars; a single paragraph longer than that stays one oversized chunk. Fine for docs, worth hardening for production.
- **In-memory search** — vectors live in a JSON file and are compared in memory. Great to a few thousand chunks; past that, reach for a real vector store.
- **`llms.txt`, not Map** — I used the published index for reliability; Map is the documented path for sites that do not publish one.
- **No reranking** — top-k cosine only. A reranking step would sharpen which chunks reach the model.

## What's next (v2)

- **Self-updating index** — use Olostep's Monitors API to detect when a doc page's *content* changes (not just when new pages appear) and re-embed only the pages that changed, so answers never go stale.
- **Self-updating via Olostep Monitors** — watch the docs with Olostep's Monitors API so that when a page's content changes, the bot re-embeds only that page instead of re-ingesting everything.
- **Batch ingestion** for large, multi-site knowledge bases.
- **Expose it as an MCP tool** so any agent can query the docs — not just this CLI.
- **A small web UI** over the CLI loop.
- **Smarter chunking** — semantic splits and token-aware sizes.

---

Built as a demo of what becomes easy when web data is clean and reliable. The hard part of RAG isn't the model — it's the ingestion. Olostep handles that part.

_Built with Claude as a coding partner — the architecture and design decisions are mine._