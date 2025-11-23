from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from rag.chain import create_chain, create_chain_no_pdf
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

if vectorStore == None:
    chain = create_chain_no_pdf()
else:
    chain, retriever = create_chain(vectorStore)

# Define input schema
class Message(BaseModel):
    message: str


@app.post("/chat")
async def chat_endpoint(msg: Message):
    fullAnswer = ""

    if vectorStore == None:
        response = chain.stream({
        "input": msg.message
        })

        print(type(response))

        for chunk in response:
            print(chunk.content, end="", flush=True)
            fullAnswer += chunk.content
        
        #print(response.content)
        #fullAnswer = response.content
        print("\n\n")
        print("No Chunks are printed as No PDF's were found.")

    else:
    #For Debugging
        print("PDF is found! Huzzah.")
        print("\n")
        
        response = chain.stream({
        "input": msg.message
        })

        for chunk in response:
            if "answer" in chunk:
                print(chunk["answer"], end="", flush=True)
                fullAnswer += chunk["answer"]
            
        else:
            chunks = retriever.invoke(msg.message)
            print(f"Chunks retrieved for query: '{msg.message}'\n")
            for i, chunk in enumerate(chunks):
                print(f"--- Chunk {i+1} ---")
                print("Content:", chunk.page_content)
                print("Metadata:", chunk.metadata)
                print()

    print("\n\n")
    print(type(fullAnswer))

    return {"reply": str(fullAnswer)}






        
    


