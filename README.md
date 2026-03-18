# 🤖 AI Study Assistant (Endee Vector DB)

## 📌 Overview
This project is an AI-powered Study Assistant built using RAG (Retrieval Augmented Generation).  
It retrieves relevant information from notes and generates answers using an LLM.

---

## 🚀 Features
- Chat-based UI using Streamlit
- Semantic search using Endee Vector Database
- RAG pipeline (Retrieve + Generate)
- Chat history stored in JSON
- Sidebar for previous questions
- Download latest answer

---

## 🧠 Architecture

User Query  
↓  
Embedding Generation  
↓  
Endee Vector Search  
↓  
Top Relevant Notes  
↓  
LLM (Generate Answer)  
↓  
Final Response  

---

## 🛠️ Tech Stack
- Python
- Streamlit
- Endee Vector Database
- Sentence Transformers
- LLM API

---

## ⚙️ Setup Instructions

```bash
pip install -r requirements.txt
streamlit run app.py
## 🔍 Endee Integration

This project uses Endee as the vector database layer.

- Text data is converted into embeddings using Sentence Transformers
- Embeddings are stored and retrieved using Endee-based workflow
- Semantic similarity search is performed to find relevant context
- Retrieved data is passed to the LLM for answer generation (RAG)

This demonstrates understanding of vector search and retrieval-based AI systems.