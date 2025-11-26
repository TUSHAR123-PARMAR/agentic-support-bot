# kb_loader.py
from typing import List, Dict, Tuple
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_faqs(path: str = "data/faqs.txt") -> List[Dict]:
    """
    Load FAQs from a simple text file with Q: and A: pairs.
    """
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"FAQ file not found at {path}")

    faqs = []
    current_q = None
    current_a = None

    with file_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("Q:"):
                if current_q and current_a:
                    faqs.append({"question": current_q, "answer": current_a})
                current_q = line[2:].strip()
                current_a = ""
            elif line.startswith("A:"):
                current_a = line[2:].strip()
            elif line:
                if current_a is not None:
                    current_a += " " + line

        if current_q and current_a:
            faqs.append({"question": current_q, "answer": current_a})

    return faqs


def search_faqs(
    user_query: str, faqs: List[Dict], top_k: int = 3
) -> List[Tuple[float, Dict]]:
    """
    Returns top_k FAQs most similar to user_query using TF-IDF cosine similarity.
    """
    if not faqs:
        return []

    questions = [f["question"] for f in faqs]
    corpus = questions + [user_query]

    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(corpus)

    query_vec = tfidf[-1]
    faq_vecs = tfidf[:-1]

    sims = cosine_similarity(query_vec, faq_vecs).flatten()
    ranked_indices = sims.argsort()[::-1][:top_k]

    results: List[Tuple[float, Dict]] = []
    for idx in ranked_indices:
        results.append((float(sims[idx]), faqs[idx]))

    return results
