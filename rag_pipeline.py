from dotenv import load_dotenv
from langchain_groq import ChatGroq
from vectordb import get_vector_db

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.0,
    timeout=20
)

def retrieve_from_documents(query):
    db = get_vector_db()
    docs = db.similarity_search(query, k=6)

    if not docs:
        return None, []

    context = "\n\n".join(d.page_content for d in docs)
    sources = list({d.metadata.get("source", "Unknown") for d in docs})

    return context, sources


def generate_strict_answer(query):
    context, sources = retrieve_from_documents(query)

    if not context:
        return "The answer is not available in the uploaded documents.", [], 0.0

    prompt = f"""
You are a STRICT document-based assistant.

RULES:
- Answer ONLY using the given context.
- If answer is not clearly present, say:
  "The answer is not available in the uploaded documents."
- Do NOT use external knowledge.
- Provide a neat, well-structured answer (5–10 lines).
- Be clear and precise.

Context:
{context}

Question:
{query}

Final Answer:
"""

    try:
        response = llm.invoke(prompt).content.strip()
    except:
        response = "The answer is not available in the uploaded documents."

    confidence = 1.0 if context else 0.0

    return response, sources, confidence