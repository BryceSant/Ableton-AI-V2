from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from rag.chain import create_chain
from rag.vectorestore import create_vector_store
from pydantic import BaseModel


PDF_FILE_LOCATION = "documents"
PERSIST_DIR = "vectorstore"
#MODEL = 'nomic-embed-text:latest'
#INPUT = "What are the best keyboard shortcuts that I should know?"

origins = [
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    "null",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

vectorStore = create_vector_store(PDF_FILE_LOCATION, PERSIST_DIR)
chain, retriever = create_chain(vectorStore)

# Define input schema
class Message(BaseModel):
    message: str


@app.post("/chat")
async def chat_endpoint(msg: Message):
    response = chain.stream({
    "input": msg.message
    })

    fullAnswer = ""

    #For Debugging
    for chunk in response:
        if "answer" in chunk:
            print(chunk["answer"], end="", flush=True)
            fullAnswer += chunk["answer"]
    
    print("\n\n")
    print(type(fullAnswer))

    chunks = retriever.invoke(msg.message)
    print(f"Chunks retrieved for query: '{msg.message}'\n")
    for i, chunk in enumerate(chunks):
        print(f"--- Chunk {i+1} ---")
        print("Content:", chunk.page_content)
        print("Metadata:", chunk.metadata)
        print()
        
    return {"reply": fullAnswer}


