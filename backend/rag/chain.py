from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain

MODEL = "gemma3:1b" #model that will be used
TEMPERATURE = 0.2 #model's temperature

#chain
def create_chain(input):
    model = ChatOllama(
        model = MODEL,
        temperature = TEMPERATURE,
        think = False,
    )

    prompt = ChatPromptTemplate.from_template("""
    Be a helpful assistant:
    Question: {input}
    """
    )

    # chain = create_stuff_documents_chain(
    #     llm=model,
    #     prompt=prompt,
    # )

    chain = prompt | model

    # response = chain.stream({
    #     "input":input,
    #     "context":"",
    # })

    response = chain.stream({
        "input": input,
        #"context": "Hello"
    })

    # for chunk in response:
    #     if "answer" in chunk:
    #         print(response["answer"], end="", flush=True)
    for chunk in response:
        print(chunk.content, end="", flush=True)



#def give_response(input, chain):