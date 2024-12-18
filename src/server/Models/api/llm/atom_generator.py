from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEndpoint

from .hf_key import get_hf_api_token
from .util import *
from .teste2 import *

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

def prompt_llm(user_query):
        model = selected_model
        prompt = ChatPromptTemplate.from_messages([
            ("system", "Act like a professional software engineer specialized in atomic design methodology"),
            ("system", "The answer should only contain code using Flutter framework for Dart"),
            ("system", "The answer should only contain the code for the atom"),
            ("system", "The chunks most related to the input text are the following: {con_info}."),
            # TODO: Create example responses 
            # https://python.langchain.com/docs/how_to/example_selectors/
            # TODO2: Estudar RAG

            ("user", "{user_query}"),
        ])

        chain = prompt | model 

        response = chain.invoke({
            "user_query" : user_query,
            "con_info" : respond_based_on_pdf(user_query),
            # "conv_history" : conv_history,
        })
        
        return response

def atomGenerator(atom_description):
    return prompt_llm(atom_description)

# print(atomGenerator("make a atom for a textfield using the principles of atomic design"))

