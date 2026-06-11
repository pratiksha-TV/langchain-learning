from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen3"
)

question = """
What is Spring Boot and what time is it?
"""

response = llm.invoke(question)

print(response.content)