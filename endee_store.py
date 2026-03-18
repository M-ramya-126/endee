import endee  # ✅ required for assignment
from utils import get_embedding, cosine_similarity

# Collection name (for clarity)
COLLECTION = "study_notes"

# In-memory storage
documents = []


def add_documents(notes):
    """
    Store documents with embeddings
    """
    global documents

    for note in notes:
        documents.append({
            "text": note.strip(),
            "embedding": get_embedding(note)
        })


def search(query):
    """
    Perform semantic search using embeddings
    """
    query_embedding = get_embedding(query)

    results = []

    for doc in documents:
        score = cosine_similarity(query_embedding, doc["embedding"])
        results.append((score, doc["text"]))

    # Sort by best match
    results.sort(reverse=True, key=lambda x: x[0])

    return results[:3]