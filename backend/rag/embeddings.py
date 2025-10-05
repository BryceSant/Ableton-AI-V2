from langchain_ollama import OllamaEmbeddings

EMBEDDING_MODEL = 'nomic-embed-text:latest' #EMBEDDING MODEL

def return_embedding():
    return OllamaEmbeddings(model = EMBEDDING_MODEL)
