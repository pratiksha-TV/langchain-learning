from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3"
)

response = llm.invoke(
    "What is Spring Boot?"
)

print(response)
