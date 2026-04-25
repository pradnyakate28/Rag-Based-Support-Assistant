# RAG-Based Customer Support Assistant

📘 RAG-Based Customer Support Assistant

📌 Project Overview

This project is a Retrieval-Augmented Generation (RAG) based Customer Support Assistant that answers user queries using information extracted from a PDF knowledge base. It uses embeddings, vector search, and a LangGraph workflow to generate accurate and context-aware responses.

The system ensures that answers are grounded in real document data instead of hallucinated outputs.

🚀 Features
- PDF document loading and processing
- Text chunking for efficient retrieval
- Embedding generation using Sentence Transformers
- Vector storage using ChromaDB
- Semantic search-based retrieval system
- LangGraph workflow orchestration
- Context-aware answer generation using LLM
- Human-in-the-Loop (HITL) support for uncertain queries

🏗️ Tech Stack
- Python
- LangChain
- LangGraph
- ChromaDB
- Sentence Transformers
- Hugging Face Transformers

## 📂 Files
- Main App: app.py  
- Workflow: graph.py  
- Retrieval: retriever.py  
- Ingestion: ingest.py  

## 📁 Folders
- data/ → PDF files  
- chroma_db/ → Vector DB
- 
⚙️ How It Works
- PDF document is loaded
- Text is extracted and split into chunks
- Chunks are converted into embeddings
- Embeddings are stored in ChromaDB
- User query is converted into embeddings
- Similar chunks are retrieved from vector database
- LLM generates answer using retrieved context
- Final response is returned to user
  
▶️ How to Run the Project
1. Create virtual environment
python -m venv venv
venv\Scripts\activate
2. Install dependencies
pip install -r requirements.txt
3. Run ingestion (create vector database)
python ingest.py
4. Start the application
python app.py

💬 Sample Queries
- What is the refund policy?
- What services are provided?
- What is the pricing structure?
  
📊 System Workflow

User Query → LangGraph → PDF Chunking → Embeddings → ChromaDB → Retrieval → LLM → Final Answer

🔮 Future Enhancements

- Multi-document support
- Web-based UI
- Feedback learning system
- Cloud deployment (AWS / Azure / Render)
- Chat memory for better conversations
  
👩‍💻 Author

Pradnya Kate
