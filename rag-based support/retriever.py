from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# Embeddings model
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Load existing vector DB
db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

def retrieve(query):
    docs = db.similarity_search(query, k=2)
    return docs