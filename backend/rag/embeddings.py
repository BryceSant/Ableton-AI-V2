from langchain_ollama import OllamaEmbeddings

#EMBEDDING_MODEL = 'nomic-embed-text:latest' #EMBEDDING MODEL

def return_embedding(embedding_model_name):
    return OllamaEmbeddings(model = embedding_model_name)
