from langchain_ollama import OllamaEmbeddings

EMBEDDING_MODEL = 'qwen3-embedding:0.6b' 

def return_embedding():
    return OllamaEmbeddings(model = EMBEDDING_MODEL)
