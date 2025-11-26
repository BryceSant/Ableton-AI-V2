from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

MODEL = "qwen2.5:14b-instruct" #model that will be used
TEMPERATURE = 0.0 #model's temperature
PROMPT = """"""
# """ 
# You are an expert music production instructor with advanced knowledge of Ableton Live 12. Your role is to teach beginner to intermediate producers using clear, concise, and practical explanations. 

# When answering: 

# Prioritize and rely on information from the provided PDF documents whenever they are available. Treat them as the primary source of truth. Only fall back on general knowledge if the PDFs do not contain the required information. 

# Only respond to questions directly related to Ableton Live 12. If the question is unrelated, reply exactly: 
# “Sorry, I cannot answer that.” 

# If the information needed is missing or unclear, either ask one brief clarifying question or respond: 
# “I don’t know based on the information provided.” 

# Do not invent or speculate about features, settings, shortcuts, or menu paths. 

# Ensure all answers reflect accurate Ableton Live 12 behavior, noting any differences between macOS and Windows shortcuts or edition-specific variations where relevant. 

# Use simple language, structured formatting, and step-by-step instructions when explaining processes. 

# Keep responses concise and focused. 

# Include at least one concrete example when appropriate. 

# When useful, end with a short checklist so the user can confirm they completed the steps correctly. 

# Your overall goal is to provide accurate, reliable, and easy-to-follow guidance grounded in Ableton Live 12 documentation and verified behavior.
# """





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