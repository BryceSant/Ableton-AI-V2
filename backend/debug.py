from rag.chain import create_chain
from rag.vectorestore import create_vector_store

#create_chain("Tell me a riddle!")

#load_pdfs("backend/documents/")

PDF_FILE_LOCATION = "backend/documents"
PERSIST_DIR = "backend/vectorstore"
MODEL = 'nomic-embed-text:latest'
INPUT = "What are the best keyboard shortcuts that I should know?"


vectorStore = create_vector_store(PDF_FILE_LOCATION, PERSIST_DIR)
chain, retriever = create_chain(vectorStore)

response = chain.stream({
    "input": INPUT
})

fullAnswer = ""

for chunk in response:
    if "answer" in chunk:
        print(chunk["answer"], end="", flush=True)
        fullAnswer += chunk

print("\n")

chunks = retriever.invoke(INPUT)
print(f"Chunks retrieved for query: '{INPUT}'\n")
for i, chunk in enumerate(chunks):
    print(f"--- Chunk {i+1} ---")
    print("Content:", chunk.page_content)
    print("Metadata:", chunk.metadata)
    print()