# RAG-Based Customer Support Assistant

📌 Project Overview

This project is a Retrieval-Augmented Generation (RAG) based Customer Support Assistant that answers user queries using information stored in a PDF knowledge base. It combines document retrieval, embeddings, vector search, and LLM-based response generation using a LangGraph workflow.

# Features
PDF document processing and text extraction

Text chunking for efficient retrieval

Embedding generation using Sentence Transformers

Vector storage using ChromaDB

Semantic search-based retrieval system

LangGraph-based workflow orchestration

Context-aware answer generation using LLM

Human-in-the-Loop (HITL) escalation support

# Tech Stack
Python

LangChain

LangGraph

ChromaDB

Sentence Transformers

Hugging Face Models

# Project Structure
rag-support-bot/
│
├── app.py
|
├── graph.py
|
├── retriever.py
|
├── ingest.py
|
├── data/ # PDF files
|
├── chroma_db/           # Vector database
|
├── requirements.txt
|
└── report/

# How It Works
PDF is loaded and text is extracted

Text is split into chunks

Chunks are converted into embeddings

Embeddings are stored in ChromaDB

User query is converted into embeddings

Similar chunks are retrieved

LLM generates final answer using context

Response is returned to user

# How to Run the Project
1. Install dependencies
pip install -r requirements.txt

3. Run ingestion (build vector DB)
python ingest.py

4. Start the chatbot
python app.py

# Example Queries
What is refund policy?

What services are provided

Pricing details?

# System Workflow

User Query → LangGraph → PDF Chunking → Embeddings → ChromaDB → Retrieval → LLM → Answer

# Future Enhancements
Multi-document support

Feedback learning system

Cloud deployment (AWS / Render)


# Author
Pradnya Kate
