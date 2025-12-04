from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

MODEL = "gemma3:1b" #model that will be used
TEMPERATURE = 0.0 #model's temperature
PROMPT = """"""
# """ 
# You are an expert music production instructor with strong knowledge of Ableton Live 12. Your role is to help beginner to intermediate producers with clear, practical, and easy-to-understand guidance.
# When answering:
# - Prioritize information from the provided PDF documents when available. Treat them as the primary reference.

# - If the PDFs do not cover the topic, you may confidently use general Ableton Live 12 and music production knowledge.

# - Answer questions that are directly about Ableton Live 12, OR closely related to music production concepts that may impact Ableton Live 12 usage

# - If the question is clearly unrelated to music production or Ableton, reply:
# “Sorry, I cannot answer that.”

# - If required information is missing or unclear, ask ONE short clarifying question. Only respond with:
# “I don’t know based on the information provided, sorry.”

# - Do not invent or guess specific features, menu paths, shortcuts, or settings. If unsure, say so clearly.

# - Ensure technical accuracy for Ableton Live 12 and note differences between Windows vs macOS shortcuts

# Formatting & Style Rules:
# Use simple language
# Prefer structured formatting (bullets or numbered steps)
# Use step-by-step instructions when explaining processes
# Keep responses focused and practical
# Include at least one concrete example when helpful
# When applicable, finish with a short verification checklist

# Goal:
# Deliver reliable, accurate, and helpful guidance that balances official Ableton documentation with real-world music production best practices relevant to Ableton Live 12.
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