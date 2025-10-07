from rag.chain import create_chain
from rag.loader import load_pdfs
from rag.vectorestore import create_vector_store
import os

#create_chain("Tell me a riddle!")

#load_pdfs("backend/documents/")

PDF_FILE_LOCATION = "backend/documents"
PERSIST_DIR = "backend/vectorstore"
MODEL = 'nomic-embed-text:latest'


create_vector_store(PDF_FILE_LOCATION, PERSIST_DIR, MODEL)

#print(os.getcwd())