# agent.py
from typing import Dict, Any, List, Tuple

from kb_loader import load_faqs, search_faqs
from llm_utils import call_llm


def build_context_from_results(results: List[Tuple[float, Dict]]) -> str:
    """
    Convert search results into a text block for LLM context.
    """
    lines = []
    for score, faq in results:
        lines.append(f"Q: {faq['question']}\nA: {faq['answer']}\n")
    return "\n".join(lines)


def answer_question(user_query: str) -> Dict[str, Any]:
    """
    Agent pipeline:
    1. Load FAQs (knowledge base)
    2. Use tool: search_faqs to retrieve top matches
    3. Use LLM to generate final natural language answer
    """
    faqs = load_faqs()
    search_results = search_faqs(user_query, faqs, top_k=3)

    if not search_results:
        # No knowledge found – still try LLM without context
        prompt = f"""
User question: {user_query}

You are a support assistant. No relevant FAQ context was found.
Respond honestly, briefly (2-3 lines), and if you don't know, say you don't know.
"""
        llm_answer = call_llm(prompt)
        return {
            "query": user_query,
            "answer": llm_answer,
            "used_context": False,
            "matches": [],
        }

    context = build_context_from_results(search_results)

    prompt = f"""
You are a support assistant for an AI product.

Here is the FAQ context (knowledge base):

{context}

User question:
{user_query}

Using only the information in the FAQ context, answer the user in 3-4 concise lines.
If the answer is not clearly present in the context, say that you are not sure and advise the user to contact support.
"""
    llm_answer = call_llm(prompt)

    return {
        "query": user_query,
        "answer": llm_answer,
        "used_context": True,
        "matches": [
            {
                "similarity": round(score, 3),
                "question": faq["question"],
                "answer": faq["answer"],
            }
            for score, faq in search_results
        ],
    }
