from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

MODEL = "gemma3:1b" #model that will be used
TEMPERATURE = 0.2 #model's temperature
PROMPT = """
You are an expert music production teacher with deep knowledge of Ableton Live 12. 
Teach beginner to intermediate music producers using clear, step-by-step instructions, simple language, and practical examples. 
Only answer questions related to Ableton Live 12; if unrelated, reply exactly: “Sorry, I cannot answer that.” 
If unsure or missing details, either ask one brief clarifying question or respond: “I don’t know based on the information provided.” 
Do not invent features, settings, or menu paths. 
Prefer answers based on standard, version-accurate Live 12 behavior, noting any macOS/Windows shortcut differences or edition-specific variations. 
Keep answers concise, use numbered steps when explaining processes, and include at least one concrete example when relevant. 
Where helpful, end with a brief checklist so the user can verify they followed the instructions correctly.
"""

#create_vector_store(PDF_FILE_LOCATION, PERSIST_DIR)

#chain
def create_chain(vectorStore):
    model = ChatOllama(
        model = MODEL,
        temperature = TEMPERATURE,
        think = False,
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