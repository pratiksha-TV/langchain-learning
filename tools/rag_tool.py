from langchain_core.tools import tool
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings


embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

vector_store = FAISS.load_local(
    "faiss_store",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vector_store.as_retriever()


@tool
def search_knowledge(question: str) -> str:
    """
    Search knowledge base for Java, Kafka, Redis and Spring questions.
    """

    docs = retriever.invoke(question)

    return "\n".join(
        doc.page_content
        for doc in docs
    )