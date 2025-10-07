from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

MODEL = "gemma3:1b" #model that will be used
TEMPERATURE = 0.2 #model's temperature

#create_vector_store(PDF_FILE_LOCATION, PERSIST_DIR)

#chain
def create_chain(vectorStore):
    model = ChatOllama(
        model = MODEL,
        temperature = TEMPERATURE,
        think = False,
    )

    prompt = ChatPromptTemplate.from_template("""
    Answer the user's question:
    Context:{context}
    Question: {input}
    """
    )

    chain = create_stuff_documents_chain(
        llm=model,
        prompt=prompt,
    )

    retriever = vectorStore.as_retriever(search_kwargs={"k": 5}) 
    #gets the k number of relevant arguments

    retrieval_chain = create_retrieval_chain(
        retriever, #Will fetch most relevant documents from vectorStore
        chain,
    )

    return retrieval_chain, retriever #returning retriever to get chunks