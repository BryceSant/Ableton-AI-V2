from rag.embeddings import return_embedding
from rag.loader import load_pdfs
from langchain_chroma import Chroma

def create_vector_store(pdfs_file_location, persist_dir):
    embedding = return_embedding()

    docs = load_pdfs(pdfs_file_location)
    if not docs:
        raise ValueError("No docs found!")

    vector_store = Chroma.from_documents(
        documents = docs,
        embedding = embedding,
        persist_directory = persist_dir,
    )

    return vector_store