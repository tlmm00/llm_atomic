from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from langchain_community.embeddings import GPT4AllEmbeddings
import requests

from dotenv import load_dotenv
load_dotenv()

# URL_ATOMIC = "https://www.softouch.on.ca/kb/data/Atomic%20Design.pdf"
URL_ATOMIC = "./atomic_pdf/atomic.pdf"

loader = PyPDFLoader(URL_ATOMIC)
pages = loader.load() # devolve um Document, envelopando a string
pages =  [page.page_content for page in pages] # tiro a string de dentro do document

text_splitter = RecursiveCharacterTextSplitter(
    separators=['\n\n', '\n', ' ', ''],
    chunk_size=400,
    chunk_overlap=0,
    #length_function=len,
    is_separator_regex=False,
)

chunks = text_splitter.split_text("\n".join(pages)) # chunks estavam em str

docs = [Document(page_content=chunk) for chunk in chunks] # chunks estao em formato de Document

db = Chroma.from_documents(docs, 
                            embedding=GPT4AllEmbeddings(model_name="all-MiniLM-L6-v2.gguf2.f16.gguf"),
                            persist_directory="./data")
