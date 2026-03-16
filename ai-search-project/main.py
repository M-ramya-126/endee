from sentence_transformers 
import SentenceTransformer
import numpy as np

# Sample documents
documents = [
    "Artificial Intelligence is transforming industries",
    "Machine learning helps computers learn from data",
    "Vector databases store embeddings for fast search",
    "Semantic search finds meaning instead of keywords"
]

# Load AI model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Convert documents into vectors
doc_embeddings = model.encode(documents)

# Query
query = "How AI understands data"

# Convert query into vector
query_embedding = model.encode([query])

# Compute similarity
similarities = np.dot(doc_embeddings, query_embedding.T)

# Find best match
best_match_index = np.argmax(similarities)

print("Query:", query)
print("Best Match:", documents[best_match_index])
