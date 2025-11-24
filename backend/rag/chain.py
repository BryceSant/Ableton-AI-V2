from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

MODEL = "qwen2.5:14b-instruct" #model that will be used
TEMPERATURE = 0.0 #model's temperature
PROMPT = """ """

#create_vector_store(PDF_FILE_LOCATION, PERSIST_DIR)

#chain
def create_chain(vectorStore):
    model = ChatOllama(
        model = MODEL,
        temperature = TEMPERATURE,
        think=False,
    )

    prompt = ChatPromptTemplate.from_template(f"""
    {PROMPT}
    Context:{{context}}
    Question: {{input}}
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

def create_chain_no_pdf():
    model = ChatOllama(
        model = MODEL,
        temperature = TEMPERATURE,
        think=False,
    )
    
    prompt = ChatPromptTemplate.from_template(f"""
    {PROMPT}
    Question: {{input}}
    """
    )

    chain = prompt | model

    return chain