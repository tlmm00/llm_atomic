import pdfplumber
import requests
import os
import torch
from transformers import pipeline
from sentence_transformers import SentenceTransformer, util

from .hf_key import get_hf_api_token

# Replace with your Hugging Face API token
HUGGINGFACE_API_TOKEN = get_hf_api_token()

# Function to download and extract text from a PDF
def extract_text_from_pdf(pdf_path):
    text = ''
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Split the text into manageable chunks
def chunk_text(text, max_length=500):
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0
    for word in words:
        current_length += len(word) + 1
        current_chunk.append(word)
        if current_length >= max_length:
            chunks.append(' '.join(current_chunk))
            current_chunk = []
            current_length = 0
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    return chunks

# Get the embeddings for each chunk using Hugging Face's SentenceTransformer model
def get_embeddings(chunks):
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    embeddings = model.encode(chunks, convert_to_tensor=True)
    return embeddings

# Find the most similar chunks to the query
def find_similar_chunks(query, chunks, chunk_embeddings):
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    query_embedding = model.encode(query, convert_to_tensor=True)
    
    # Compute cosine similarities
    similarities = util.pytorch_cos_sim(query_embedding, chunk_embeddings)[0]
    top_k = torch.topk(similarities, k=3)  # Find top 3 most similar chunks
    return [chunks[idx] for idx in top_k.indices]

# Main function that puts everything together
def respond_based_on_pdf(query):
    # Step 1: Extract text from the PDF
    text = extract_text_from_pdf('/home/tlmm/Codes/llm_atomic/src/server/Models/api/llm/atomic_pdf/atomic.pdf')

    # Step 2: Chunk the text
    chunks = chunk_text(text)

    # Step 3: Get embeddings for each chunk
    chunk_embeddings = get_embeddings(chunks)

    # Step 4: Find similar chunks based on the query
    similar_chunks = find_similar_chunks(query, chunks, chunk_embeddings)

    # # Step 5: Combine the most relevant chunks as context
    # context = ' '.join(similar_chunks)

    # # Step 6: Get a response from the LLM
    # response = get_llm_response(context, query)

    return similar_chunks

# # Example usage
# pdf_path = './atomic_pdf/atomic.pdf'  # Replace with the path to your PDF
# query = 'What is the main purpose of the document?'  # Replace with the user's query
# response = respond_based_on_pdf(pdf_path, query)

# print(response)
