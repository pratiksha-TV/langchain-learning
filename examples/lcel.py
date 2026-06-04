from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

prompt = PromptTemplate.from_template(
    "Explain {topic}"
)

llm = ChatOllama(model="llama3")

chain = prompt | llm

response = chain.invoke({
    "topic": "Kafka"
})

print(response.content)