from langchain_ollama import OllamaEmbeddings

EMBEDDING_MODEL = 'nomic-embed-text:latest' 

def return_embedding():
    return OllamaEmbeddings(model = EMBEDDING_MODEL)
