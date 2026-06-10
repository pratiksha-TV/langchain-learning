from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings

with open("data/java_notes.txt") as file:
    text = file.read()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20
)

chunks = splitter.create_documents([text])

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

vector_store = FAISS.from_documents(
    chunks,
    embeddings
)

vector_store.save_local("faiss_store")

print("Vector Store Created")