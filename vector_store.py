from utils import get_embedding, cosine_similarity

class VectorStore:
    def __init__(self):
        self.documents = []
        self.embeddings = []

    def add_document(self, text):
        embedding = get_embedding(text)
        self.documents.append(text)
        self.embeddings.append(embedding)

    def search(self, query, top_k=3):
        query_embedding = get_embedding(query)

        results = []
        for i, emb in enumerate(self.embeddings):
            score = cosine_similarity(query_embedding, emb)
            results.append((score, self.documents[i]))

        results.sort(reverse=True, key=lambda x: x[0])
        return results[:top_k]