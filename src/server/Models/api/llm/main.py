from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEndpoint

from hf_key import get_hf_api_token
from util import *

HF_API_TOKEN = get_hf_api_token()

models = ["microsoft/Phi-3-mini-4k-instruct",
    "meta-llama/Meta-Llama-3-8B-Instruct",
    "mistralai/Mixtral-8x7B-Instruct-v0.1",
    "google/gemma-7b",
    "ericzzz/falcon-rw-1b-instruct-openorca",
    "mistralai/Mistral-7B-v0.1",
    'tiiuae/falcon-7b-instruct',
    "microsoft/DialoGPT-medium"]

selected_model = HuggingFaceEndpoint(
                                repo_id=models[1],
                                task="text-generation",
                                temperature=0.9,
                                huggingfacehub_api_token=HF_API_TOKEN
                            )

conversation_history = []

def prompt_llm(user_query, conv_history):
    model = selected_model
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Act like a professional software engineer specialized in atomic design methodology"),
        #("system", "Responda em até 50 palavras."),
        ("system", "The conversation history is as follows: {conv_history}"),
        ("system", "The chunks most related to the input text are the following: {con_info}."),
        # ("system", "Não responda além do extritamente necessário"),
    
        ("user", "{user_query}"),
    ])

    chain = prompt | model 

    response = chain.invoke({
        "user_query" : user_query,
        "con_info" : get_best_chuncks(user_query),
        "conv_history" : conv_history,
    })
    
    return response

print("\n> Hello, world!")
user_in = input("\n> ")

while (user_in!="QUIT"):

    chunks = select_similar_chunks(user_in)
    response = prompt_llm(user_in, conversation_history)
    
    conversation_history.append(user_in)
    conversation_history.append(response)

    print("> " + response)
    user_in = input("\n> ")
