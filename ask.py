"""
ask.py — Piece 3 of the "Chat with the Olostep docs" RAG demo.

The actual chatbot: a question goes in, a cited answer comes out.

Flow for every question:
  1. EMBED     the question with Gemini (same model used for the chunks)
  2. RETRIEVE  the top-k most similar chunks (cosine similarity, done locally)
  3. ANSWER    with Gemini, grounded ONLY in those chunks, citing their URLs

Run (after ingest.py and embed.py):
  python ask.py
"""

import os
import json
import pathlib
import numpy as np
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

EMBED_MODEL = "models/gemini-embedding-001"
CHAT_MODEL = "gemini-3.5-flash-lite"
CHUNKS = pathlib.Path("data/chunks.json")
TOP_K = 5                                  # how many chunks to feed the model


def load_index():
    """Load the embedded chunks and stack their vectors into one matrix."""
    records = json.loads(CHUNKS.read_text(encoding="utf-8"))
    vectors = np.array([r["embedding"] for r in records], dtype=float)
    return records, vectors


def embed_question(question):
    """Embed the user's question into the same vector space as the chunks."""
    r = genai.embed_content(model=EMBED_MODEL, content=question)
    return np.array(r["embedding"], dtype=float)


def top_chunks(qvec, vectors, records, k=TOP_K):
    """Return the k chunks whose vectors point most like the question's vector."""
    # cosine similarity = how aligned two vectors are (1 = same meaning direction)
    sims = (vectors @ qvec) / (
        np.linalg.norm(vectors, axis=1) * np.linalg.norm(qvec) + 1e-9
    )
    top = np.argsort(sims)[::-1][:k]       # indices of the k highest scores
    return [records[i] for i in top]


def answer(question, chunks):
    """Ask Gemini to answer using ONLY the retrieved chunks, and cite sources."""
    context = "\n\n---\n\n".join(
        f"[Source: {c['url']}]\n{c['text']}" for c in chunks
    )
    prompt = (
        "You are a helpful assistant for the Olostep documentation. "
        "Answer the question using ONLY the context below. "
        "If the answer isn't in the context, say you don't know. "
        "Cite the source URL(s) you used.\n\n"
        f"CONTEXT:\n{context}\n\n"
        f"QUESTION: {question}\n\nANSWER:"
    )
    model = genai.GenerativeModel(CHAT_MODEL)
    response = model.generate_content(prompt)
    try:
        return response.text
    except Exception:
        return "(No text returned — try rephrasing the question.)"


def main():
    records, vectors = load_index()
    print(f"Loaded {len(records)} chunks. Ask about Olostep (Ctrl+C to quit).\n")
    while True:
        question = input("You: ").strip()
        if not question:
            continue
        print("Thinking...")
        chunks = top_chunks(embed_question(question), vectors, records)
        print("\nBot:", answer(question, chunks))
        print("\nSources:")
        for url in sorted({c["url"] for c in chunks}):
            print("  -", url)
        print()


if __name__ == "__main__":
    main()