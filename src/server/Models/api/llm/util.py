from sentence_transformers import CrossEncoder
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

import chromadb
import chromadb.utils.embedding_functions as embedding_functions

from .hf_key import get_hf_api_token

HF_API_TOKEN = get_hf_api_token()

def rerank(query, passages):
    model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
    ranks = model.rank(query, passages)

    best_ranks = []
    n_passages = 1

    highest_rank_passage = ""
    highest_rank = -1000

    lr = 1000
    for rank in ranks:

        if(len(best_ranks) < n_passages):
            best_ranks.append(rank)
            
            for r in best_ranks:
                if r['score'] < lr:
                    lr = r['score']
        else:
            if(rank['score'] > lr):
                for r in best_ranks:
                    if r['score']==lr:
                        best_ranks.pop(r)

        
        #if(rank['score'] > highest_rank):
        #    highest_rank = rank['score']
        #    highest_rank_passage = passages[rank['corpus_id']]
        #print(f"{rank['score']:.2f}\t{passages[rank['corpus_id']]}")

    return( [passages[r['corpus_id']] for r in best_ranks] )
    #return(highest_rank_passage, highest_rank)

def select_similar_chunks(user_query):
    huggingface_ef = embedding_functions.HuggingFaceEmbeddingFunction(
        api_key=HF_API_TOKEN,
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    client = chromadb.PersistentClient(path="./data")
    #return rerank(user_query, client)
    col = client.get_or_create_collection("langchain", embedding_function = huggingface_ef)    
    results = col.query(query_texts=[user_query], n_results=20)
    
    return results['documents'][0]

def get_best_chuncks(user_query):
    passages = select_similar_chunks(user_query)
    print(user_query, passages)
    return rerank(user_query, passages)

