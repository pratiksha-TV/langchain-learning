from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are a senior Java and Spring Boot interviewer.

        Explain concepts in simple English.

        Give:
        1. Definition
        2. Real-world example
        3. Interview answer
        """
    ),
    ("human", "{question}")
])

llm = ChatOllama(model="qwen3")

chain = prompt | llm

response = chain.invoke({
    "question": "What is Dependency Injection?"
})

print(response.content)